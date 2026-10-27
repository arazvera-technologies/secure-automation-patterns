# Tested permission-aware change-policy simulator

A dependency-free OFFLINE Python example. It does not modify files, access the
operating system, contact APIs or handle real accounts. The simulated roles
are NOT authenticated identities and outputs are NOT authorization tokens.

## Run locally (Python 3.10+)

~~~bash
python -m examples.policy_gate --role reader --operation read --environment public_docs
python -m examples.policy_gate --role editor --operation write --environment staging
python -m examples.policy_gate --role editor --operation write --environment production
python -m examples.policy_gate --role admin --operation delete --environment staging
python -m examples.policy_gate --role reader --operation delete --environment production
python -m unittest discover -s tests -v
~~~

## Explicit policy contract

Function: evaluate(ChangeRequest(intent_id, role, operation, environment)).
Response: PolicyDecision(intent_id, status, operation, environment, reason, executed).
Possible statuses: ready, approval_required, denied.
The executed field is ALWAYS false.

| Role | Allowed operations |
| --- | --- |
| reader | read |
| editor | read, draft, write |
| admin | read, draft, write, delete, grant_access |

Only public_docs, staging, production are sample targets.
Unknown roles, tools and targets are denied. All delete, grant_access and
production write intents require independent review. A declared role is
untrusted until authenticated by a real identity system.

Real software additionally requires authenticated identities, trusted policy
enforcement outside prompts, audit logs, resource-bound approvals, rollback,
idempotent execution and monitoring. This demo provides none of those.
It does not claim production deployment, measured safety or commercial delivery.

Also read [approval and access controls](approval-and-access.md) and
[defensive response playbook](defensive-response.md).
