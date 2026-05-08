# Safety And Approval Gates

Smart Skill User turns risky task types into explicit gates.

## Visual Or CRO Work

- preview before commit
- check mobile and desktop if responsive behavior is affected
- do not commit subjective design changes without user approval when requested by repo policy

## Deploy, Publish, DNS, CRM, And Production Connectors

- require explicit approval
- confirm target environment
- confirm branch or release source
- avoid credential changes unless specifically requested

## Cleanup, Revert, And Destructive Work

- create a backup patch first
- do not remove broad file sets without review
- do not revert unrelated user changes

## Secrets And Private Data

- never expose secrets
- do not paste credentials into docs or logs
- scrub examples before publication

## Unclear Scope

Stop and ask. Asking early is cheaper than repairing wrong-scope work later.
