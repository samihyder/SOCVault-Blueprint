# ADR 002: Anthropic Claude as sole AI provider

**Status:** Accepted  
**Date:** June 2026

## Context

SOCVault requires JSON-structured security reports, financial risk translation, SOAR triage, malware analysis, L9 agent reasoning, and AI Chat.

## Decision

Use **Anthropic Claude** exclusively:
- `claude-sonnet-4-6` — reasoning, SOAR, malware, chat
- `claude-haiku-4-5-20251001` — fast triage
- `claude-opus-4-8` — L9 AI Agent Scan with extended thinking

Enable **prompt caching** on all system prompts.

## Consequences

- Single vendor dependency; offline fallback required (FR-047)
- Cost telemetry per tenant mandatory (FR-105, Metrics Observatory)
