# Autonomous Self-Healing Infrastructure Bot

## Project Overview
This project demonstrates an **Autonomous Self-Healing Pipeline**. By integrating Python-based monitoring with intelligent diagnostic logic, this bot detects system anomalies, interprets their cause, and executes automated remediation—reducing downtime and manual intervention.

## Why I Built This
Most automation focuses on the "happy path." I designed this architecture to handle **exceptions**. By treating IT infrastructure with the same rigor as mechanical preventative maintenance, I built a system that ensures operational reliability.

## Architecture
- **Monitor:** Continuous health checking of system logs.
- **Diagnose:** AI-integrated logic to identify root causes.
- **Heal:** Automated execution of corrective actions to restore service.

## How to Run
1. Ensure Python is installed.
2. Clone this repository.
3. Modify `system_log.txt` to simulate an error and run `python main.py`.
