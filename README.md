# Autonomous AI Router (AAIR)

A lightweight, Linux-native infrastructure for orchestrating autonomous AI agent workflows. This router manages multi-node inference routing, context-switching for agentic tasks, and automated process recovery.

## Why this exists
Current AI workflows often struggle with API reliability. AAIR provides:
- **Resilient Inference Routing:** Multi-provider failover.
- **Systemd-Orchestrated Workers:** Self-healing processes.
- **Audit Logs:** Tracks instruction-following metrics.

## Quick Start
1. Clone: `git clone https://github.com/Trisman21/autonomous-ai-router.git`
2. Config: `cp .env.example .env`
3. Launch: `python3 src/router.py`

## Roadmap
- [ ] Implement advanced RAG context-switching.
- [ ] Add real-time log-based root cause analysis (RCA).
