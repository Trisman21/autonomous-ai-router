# Autonomous AI Router (AAIR)

A lightweight, Linux-native infrastructure for orchestrating autonomous AI agent workflows. This router manages multi-node inference routing, context-switching for agentic tasks, and automated process recovery.

## Why this exists
Current AI workflows often struggle with API reliability and state management. AAIR provides a robust layer to ensure your agents stay online even when individual providers hit rate limits.

## Key Features
- **Resilient Inference Routing:** Multi-provider failover strategy using round-robin and random selection for maximum uptime.
- **Systemd-Orchestrated Workers:** Self-healing architecture optimized for 24/7 deployment on Ubuntu Linux.
- **Audit Logs:** Tracks instruction-following metrics, providing deep-dive insights into agent performance.
- **Configurable Strategy:** Easily switch between different routing algorithms via a centralized YAML configuration.

## Project Architecture
The system employs a modular design:
- **Router Layer:** Handles provider selection and request validation.
- **Worker Layer:** Executes the actual agent logic as a background service.
- **Logging Layer:** Captures model performance for real-time root cause analysis (RCA).

## Quick Start
1. Clone the repository:
   ```bash
   git clone https://github.com/Trisman21/autonomous-ai-router.git
   cd autonomous-ai-router
   ```
2. Setup your configuration:
   ```bash
   cp .env.example .env
   # Add your API keys for Gemini, DeepSeek, or other providers
   ```
3. Launch the worker:
   ```bash
   python3 src/router.py
   ```

## Contributing
We welcome contributions to improve the agentic workflow management! Feel free to open an issue or submit a pull request.

## License
MIT License - Developed as an open-source project to advance AI agent infrastructure.
EOF
