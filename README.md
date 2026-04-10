# Environment Access Validation

![Python](https://img.shields.io/badge/Python-3.10+-blue?logo=python&logoColor=white)
![Shell](https://img.shields.io/badge/Shell-Bash-green?logo=gnubash&logoColor=white)
![CI/CD](https://img.shields.io/badge/CI/CD-GitHub%20Actions-orange?logo=githubactions&logoColor=white)
![Status](https://img.shields.io/badge/Checks-4%20Passing-brightgreen)

A DevOps practice project that simulates the pre-deployment environment validation process.  
Before any application is deployed to a server, a DevOps engineer must confirm that the environment is correctly set up and accessible. This project automates those checks using Python and documents the results.

---

## What Problem Does This Solve?

In real DevOps work, before deploying an app, engineers manually verify:

- Can I access the server? (SSH check)
- Is the code repository available? (Repo check)
- Is the pipeline running? (CI/CD check)
- Can I read the application logs? (Log access check)

Doing this manually every time is slow and error-prone.  
This project automates all 4 checks with a single Python script and generates a report.

---

## What I Built

```
validate_environment.py        → Main Python script that runs all 4 checks
access_checklist_report.txt    → Auto-generated report after each run
logs/app.log                   → Application log file
pipeline_simulation/
  build_status.txt             → Simulated CI/CD pipeline status
repo_simulation/
  app.py                       → Simulated application file
  config.yml                   → App configuration file
.github/workflows/
  validate.yml                 → GitHub Actions CI pipeline
pipeline_flow_documentation_v1.md → Full pipeline documentation
```

---

## The 4 Checks

| # | Check | What It Does |
|---|---|---|
| 1 | Shell / SSH Access | Runs `whoami`, `uname -n`, `uptime` to verify server access |
| 2 | Repository Structure | Confirms `app.py` and `config.yml` exist in the repo |
| 3 | Pipeline Status | Reads `build_status.txt` to verify pipeline ran successfully |
| 4 | Log Access | Opens `app.log` and confirms it is readable |

---

## How To Run It

```bash
# Clone the repo
git clone https://github.com/rey26341-sudo/ENVIRONMENT-ACCESS-VALIDATION.git
cd ENVIRONMENT-ACCESS-VALIDATION

# Run the validation script
python validate_environment.py
```

### Output

```
==================================================
  ENVIRONMENT ACCESS VALIDATION
  2026-04-10 09:00:03
==================================================

CHECK 1: SSH / Shell Environment
  whoami   → rey
  hostname → cloudshell
  uptime   → up 2 min
  [✔] SSH / Shell Access: SUCCESS

CHECK 2: Repository Structure
  ✔ Found: repo_simulation/app.py
  ✔ Found: repo_simulation/config.yml
  [✔] Repository Structure: SUCCESS

CHECK 3: Pipeline Simulation
  ✔ File found: pipeline_simulation/build_status.txt
  [✔] Pipeline Simulation: SUCCESS

CHECK 4: Log Directory Access
  ✔ Log file: logs/app.log — 10 lines
  [✔] Log Directory Access: SUCCESS

  Report written → access_checklist_report.txt
==================================================
  OVERALL: ALL CHECKS PASSED ✔
==================================================
```

---

## CI/CD Pipeline

A GitHub Actions workflow runs automatically on every push to `main`:

1. Sets up Python 3.10
2. Installs dependencies
3. Runs `validate_environment.py`
4. Saves the checklist report as a downloadable artifact

See `.github/workflows/validate.yml` for the full workflow.

---

## What I Learned

- How environment validation works in a real DevOps workflow
- Writing Python scripts that interact with the operating system
- Using `subprocess` to run shell commands from Python
- Setting up a CI/CD pipeline with GitHub Actions
- Structuring a project and documenting it for GitHub
- Using Google Cloud Shell as a Linux environment for practice

---

## Issues Faced & How I Solved Them

| Issue | Solution |
|---|---|
| `hostname` command not found in Cloud Shell | Used `uname -n` as a fallback |
| Google Cloud Shell session expired | Saved all work to GitHub before timeout |

---

## Tools & Technologies Used

- **Python 3** — scripting and automation
- **Bash / Linux** — shell commands via Google Cloud Shell
- **Git & GitHub** — version control
- **GitHub Actions** — CI/CD pipeline
- **YAML** — configuration files

---

## Project Status

This is a learning / practice project built to understand DevOps pre-deployment validation concepts.  
It is not connected to a live server or production environment.

---

## Author

**Rey** — Aspiring DevOps Engineer  
Self-taught | DevOps Course Certified | Hands-on Practice Projects  
[GitHub Profile](https://github.com/rey26341-sudo)
