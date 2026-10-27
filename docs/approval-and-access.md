# Approval and access controls

## Example policy tiers

| Tier | Typical operation | Recommended gate |
| --- | --- | --- |
| Read | Inspect permitted telemetry, metadata or public pages | Scoped authorization |
| Low-impact write | Create a review draft in a test environment | Logged policy check |
| Production write | Change live configuration or customer-facing content | Context-aware approval |
| Destructive | Delete, overwrite, revoke or change access controls | Explicit operator confirmation and verified backup |
| Financial | Purchase service, transfer funds or change billing | Owner approval and independent record |

## Controls
1. Enforce scopes at the tool boundary rather than only through prompts.
2. Record actor, requested action, target, decision and execution outcome.
3. Redact credentials, sensitive messages and personal information before logging.
4. Limit task duration, concurrency and API budgets.
5. Test denied actions and interrupted workflows.
6. Provide safe rollback instructions before risky changes.
7. Avoid silent privilege expansion, unattended high-risk actions and policy bypass.

Permission reduction should not require disabling host protections.
