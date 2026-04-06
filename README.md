# 🛡️ Environment Access Validation

![Python](https://img.shields.io/badge/Python-3.10%2B-blue?logo=python)
![CI](https://img.shields.io/badge/CI-GitHub%20Actions-green?logo=githubactions)
![Status](https://img.shields.io/badge/Checks-4%20Passing-brightgreen)
![License](https://img.shields.io/badge/License-MIT-lightgrey)

A Python-based DevOps utility that **automatically validates critical environment access** before a CI/CD pipeline runs. It performs SSH/shell checks, repository structure verification, pipeline simulation status, and log directory access — then generates a structured checklist report.

---

## 📋 Table of Contents

- [Overview](#overview)
- [Features](#features)
- [Project Structure](#project-structure)
- [Getting Started](#getting-started)
- [How It Works](#how-it-works)
- [CI/CD Pipeline](#cicd-pipeline)
- [Sample Output](#sample-output)
- [Roadmap](#roadmap)

---

## Overview

Before deploying any application, it's critical to confirm that the target environment is correctly configured and accessible. This project automates that pre-flight validation, replacing manual checklists with a single Python script that:

- Verifies shell/SSH access and collects system info
- Confirms all required repository files are present
- Reads and validates the pipeline simulation status
- Confirms log directory accessibility
- Generates a time-stamped `access_checklist_report.txt`

---

## Features

- ✅ **4 automated environment checks** (SSH, repo, pipeline, logs)
- 📄 **Auto-generated checklist report** with timestamps and command output
- 🔁 **Graceful fallbacks** (e.g., `uname -n` when `hostname` is unavailable)
- ⚙️ **YAML-based configuration** via `repo_simulation/config.yml`
- 🤖 **GitHub Actions CI workflow** runs on every push to `main`
- 🐍 **Pure Python stdlib** — no external dependencies for core validation

---

## Project Structure

```
ENVIRONMENT-ACCESS-VALIDATION/
│
├── .github/
│   └── workflows/
│       └── validate.yml              # GitHub Actions CI pipeline
│
├── logs/
│   └── app.log                       # Application runtime log
│
├── pipeline_simulation/
│   └── build_status.txt              # Simulated CI/CD build status
│
├── repo_simulation/
│   ├── app.py                        # Simulated application entry point
│   └── config.yml                    # Application configuration
│
├── validate_environment.py           # ⭐ Main validation script
├── access_checklist_report.txt       # Auto-generated validation report
├── pipeline_flow_documentation_v1.md # Full CI/CD pipeline documentation
├── requirements.txt                  # Python dependencies (pytest, flake8)
└── README.md
```

---

## Getting Started

### Prerequisites

- Python 3.10+
- Git

### Installation

```bash
# 1. Clone the repository
git clone https://github.com/rey26341-sudo/ENVIRONMENT-ACCESS-VALIDATION.git
cd ENVIRONMENT-ACCESS-VALIDATION

# 2. Install dependencies
pip install -r requirements.txt

# 3. Run the validation
python validate_environment.py
```

### Expected Output

```
==================================================
  ENVIRONMENT ACCESS VALIDATION
  2026-04-06 09:00:03
==================================================

CHECK 1: SSH / Shell Environment
  whoami   → your-username
  hostname → your-host
  uptime   → ...
  [✔] SSH / Shell Access: SUCCESS

CHECK 2: Repository Structure
  ✔ Found   : repo_simulation/app.py
  ✔ Found   : repo_simulation/config.yml
  [✔] Repository Structure: SUCCESS

CHECK 3: Pipeline Simulation
  ✔ File found : pipeline_simulation/build_status.txt
  [✔] Pipeline Simulation: SUCCESS

CHECK 4: Log Directory Access
  ✔ Log file  : logs/app.log
  [✔] Log Directory Access: SUCCESS

  Report written → access_checklist_report.txt
```

---

## How It Works

The script runs four sequential checks:

| # | Check | Method | Fallback |
|---|---|---|---|
| 1 | SSH / Shell Environment | `whoami`, `hostname`, `uptime` | `uname -n` if `hostname` unavailable |
| 2 | Repository Structure | `os.path.exists()` on required files | Reports missing files |
| 3 | Pipeline Simulation | Reads `pipeline_simulation/build_status.txt` | Reports if file missing |
| 4 | Log Directory Access | Reads `logs/app.log`, counts lines | Reports if file missing |

Each check logs its result, and a final report is written to `access_checklist_report.txt`.

---

## CI/CD Pipeline

The GitHub Actions workflow (`.github/workflows/validate.yml`) automatically:

1. **Triggers** on push or pull request to `main`
2. **Sets up** Python 3.10
3. **Lints** all Python files with `flake8`
4. **Runs** `validate_environment.py`
5. **Archives** the checklist report and log as pipeline artifacts (30-day retention)

See [`pipeline_flow_documentation_v1.md`](./pipeline_flow_documentation_v1.md) for full pipeline documentation.

---

## Sample Output

**`access_checklist_report.txt`** (auto-generated):

```
==================================================
  ENVIRONMENT ACCESS VALIDATION REPORT
  Generated : 2026-04-06 09:00:04
  System    : Linux 5.15.0
  Python    : 3.10.12
==================================================

[SUCCESS] SSH / Shell Access
commands used: whoami, hostname, uptime
status: SUCCESS

[SUCCESS] Repository Structure
Files verified: repo_simulation/app.py, repo_simulation/config.yml
status: SUCCESS

[SUCCESS] Pipeline Simulation
file: pipeline_simulation/build_status.txt
status: SUCCESS

[SUCCESS] Log Directory Access
file: logs/app.log | lines: 11
status: SUCCESS

==================================================
  OVERALL: ALL CHECKS PASSED ✔
==================================================
```

---

## Roadmap

- [ ] Add `pytest` unit tests for each validation function
- [ ] Add `--json` output flag for machine-readable reports
- [ ] Extend checks to include network connectivity (ping / DNS)
- [ ] Support environment profiles (`dev`, `staging`, `prod`) via config
- [ ] Send validation summary as GitHub Actions job summary

---

## Author

**rey26341-sudo** — [GitHub](https://github.com/rey26341-sudo)

---

## License

This project is licensed under the MIT License.
