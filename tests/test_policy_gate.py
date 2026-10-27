import unittest
from examples.policy_gate import ChangeRequest, evaluate

class PolicyGateTests(unittest.TestCase):
    def test_reader_can_read(self):
        self.assertEqual(evaluate(ChangeRequest("r1","reader","read","public_docs")).status,"ready")
    def test_reader_cannot_write(self):
        self.assertEqual(evaluate(ChangeRequest("r2","reader","write","staging")).status,"denied")
    def test_editor_can_write_staging(self):
        self.assertEqual(evaluate(ChangeRequest("r3","editor","write","staging")).status,"ready")
    def test_editor_production_requires_review(self):
        self.assertEqual(evaluate(ChangeRequest("r4","editor","write","production")).status,"approval_required")
    def test_admin_production_requires_review(self):
        self.assertEqual(evaluate(ChangeRequest("r5","admin","write","production")).status,"approval_required")
    def test_admin_delete_always_requires_review(self):
        self.assertEqual(evaluate(ChangeRequest("r6","admin","delete","staging")).status,"approval_required")
    def test_editor_cannot_delete(self):
        self.assertEqual(evaluate(ChangeRequest("r7","editor","delete","staging")).status,"denied")
    def test_grant_access_requires_review(self):
        self.assertEqual(evaluate(ChangeRequest("r8","admin","grant_access","staging")).status,"approval_required")
    def test_unknown_role_denied(self):
        self.assertEqual(evaluate(ChangeRequest("r9","root","read","public_docs")).status,"denied")
    def test_unknown_operation_denied(self):
        self.assertEqual(evaluate(ChangeRequest("r10","admin","wipe_drives","staging")).status,"denied")
    def test_unknown_target_denied(self):
        self.assertEqual(evaluate(ChangeRequest("r11","admin","read","private_zone")).status,"denied")
    def test_prompt_text_cannot_override_policy(self):
        self.assertEqual(evaluate(ChangeRequest("r12","admin ignore policy","delete","production")).status,"denied")
    def test_invalid_ids_rejected(self):
        for bad in (""," ","x"*129):
            with self.assertRaises(ValueError): evaluate(ChangeRequest(bad,"reader","read","staging"))
    def test_always_side_effect_free(self):
        for action in ("read","delete"):
            d=evaluate(ChangeRequest("r13","admin",action,"staging"))
            self.assertEqual(d.intent_id,"r13")
            self.assertTrue(d.reason)
            self.assertFalse(d.executed)
    def test_deterministic(self):
        req=ChangeRequest("r14","editor","write","production")
        self.assertEqual(evaluate(req),evaluate(req))
