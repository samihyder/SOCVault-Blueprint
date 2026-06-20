# ADR 003: AWS Cognito for authentication

**Status:** Accepted  
**Date:** June 2026

## Context

Multi-tenant SaaS needs OTP/MFA, business-email validation, sub-users, and future Enterprise SSO.

## Decision

- **No local JWT phase** — Cognito User Pool in **each** AWS workspace (staging, production) with custom `tenant_id` attribute (ADR-004).
- Lambda pre-signup trigger blocks freemail domains
- Sub-users get separate Cognito accounts linked to tenant

## Consequences

- AWS-native integration with SNS for OTP
- SAML SSO added in Phase 4 for Enterprise
- Staging and production have **isolated** user pools — test tenants never in production pool
