"""Example policy gate (offline simulator, not a security product).

Actor roles are unverified sample inputs. No system tools or external actions run.
"""
from __future__ import annotations
import argparse
from dataclasses import dataclass,asdict
import json

@dataclass(frozen=True)
class ChangeRequest:
    intent_id:str
    role:str
    operation:str
    environment:str

@dataclass(frozen=True)
class PolicyDecision:
    intent_id:str
    status:str
    operation:str
    environment:str
    reason:str
    executed:bool=False

_PERMISSIONS={
    "reader":frozenset(("read",)),
    "editor":frozenset(("read","draft","write")),
    "admin":frozenset(("read","draft","write","delete","grant_access")),
}
_TARGETS=frozenset(("public_docs","staging","production"))
_REVIEW=frozenset(("delete","grant_access"))

def evaluate(request:ChangeRequest)->PolicyDecision:
    """Pure, fail-closed decision; ready is not real authorization."""
    if not isinstance(request,ChangeRequest):
        raise ValueError("Expected ChangeRequest")
    key=request.intent_id
    if (not isinstance(key,str) or not key.strip() or key!=key.strip() or len(key)>128):
        raise ValueError("Invalid intent_id")
    if not all(isinstance(x,str) for x in
               (request.role,request.operation,request.environment)):
        raise ValueError("Role, operation and environment must be strings")
    def result(status,reason):
        return PolicyDecision(key,status,request.operation,request.environment,reason)
    permissions=_PERMISSIONS.get(request.role)
    if permissions is None: return result("denied","Unknown role")
    if request.environment not in _TARGETS: return result("denied","Unknown environment")
    if request.operation not in permissions: return result("denied","Operation outside role permission")
    if request.operation in _REVIEW:
        return result("approval_required","High-impact change requires independent review")
    if request.operation=="write" and request.environment=="production":
        return result("approval_required","Production write requires independent review")
    return result("ready","Simulated routing only; no operation executed")

def main():
    parser=argparse.ArgumentParser(description="Offline policy-decision simulator")
    parser.add_argument("--intent-id",default="demo-001")
    parser.add_argument("--role",required=True)
    parser.add_argument("--operation",required=True)
    parser.add_argument("--environment",required=True)
    a=parser.parse_args()
    print(json.dumps(asdict(evaluate(ChangeRequest(a.intent_id,a.role,a.operation,a.environment))),indent=2))

if __name__=="__main__": main()
