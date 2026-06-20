# ADR 001: MongoDB as primary database

**Status:** Accepted  
**Date:** June 2026

## Context

SOCVault stores heterogeneous scan outputs (L1–L9), AI reports, incidents, and tenant metadata. Schema varies by scan layer.

## Decision

Use **MongoDB Atlas** with `tenant_id` on every document and middleware-enforced query filters.

## Consequences

- Flexible scan result schemas without migrations per layer
- DynamoDB used separately for high-write telemetry and credits ledger
- Team must enforce tenant isolation in application code and indexes
