# Environment Access & Service Validation Platform

A software validation project demonstrating **Python application validation, PHP/Laravel REST API development, automated testing, and CI/CD using GitHub Actions**.

The project simulates an environment-access and application-validation workflow where a Python validation layer communicates with a Laravel service through a REST API and verifies the service health.

---

## Project Overview

Modern software environments often contain multiple services built with different technologies.

This project demonstrates a simple cross-stack validation architecture:

```text
┌─────────────────────────────┐
│      Python Validator       │
│                             │
│  Environment validation     │
│  Service health checking    │
└──────────────┬──────────────┘
               │
               │ HTTP / JSON
               ▼
┌─────────────────────────────┐
│      Laravel Service        │
│                             │
│      GET /api/health        │
│                             │
│  Returns service status     │
└──────────────┬──────────────┘
               │
               ▼
        JSON Health Response
               │
               ▼
┌─────────────────────────────┐
│    Automated Validation     │
│                             │
│  Python check + Laravel     │
│  feature tests              │
└─────────────────────────────┘
```

The project is designed as a portfolio demonstration of **backend development, API integration, software validation, and DevOps practices**.

---

## Key Features

* Python-based application validation
* PHP/Laravel REST API
* Laravel health-check endpoint
* Python-to-Laravel HTTP integration
* JSON API communication
* Laravel feature testing
* Python code-quality analysis with Pylint
* GitHub Actions CI/CD
* Composer dependency management
* Environment configuration
* Application logging
* Git-based development workflow

---

## Technology Stack

| Area                  | Technology                       |
| --------------------- | -------------------------------- |
| Validation layer      | Python                           |
| Backend service       | PHP / Laravel                    |
| API                   | REST / JSON                      |
| Testing               | Laravel PHPUnit/Pest test runner |
| Code quality          | Pylint                           |
| Dependency management | Composer                         |
| Version control       | Git / GitHub                     |
| CI/CD                 | GitHub Actions                   |
| Operating environment | Linux / Ubuntu                   |

---

## Project Structure

```text
ENVIRONMENT-ACCESS-VALIDATION/
│
├── .github/
│   └── workflows/
│       ├── pylint.yml
│       └── php-laravel.yml
│
├── logs/
│   └── app.log
│
├── pipeline_simulation/
│   ├── build_status.txt
│   └── validate environment.txt
│
├── repo_simulation/
│   ├── app.py
│   ├── config.yml
│   └── laravel_health_check.py
│
├── php-service/
│   ├── app/
│   ├── routes/
│   │   └── api.php
│   ├── tests/
│   │   └── Feature/
│   │       └── HealthApiTest.php
│   ├── composer.json
│   └── ...
│
├── access_checklist_report.txt
├── pipeline_flow_documentation_v1.md
└── README.md
```

---

# 1. Python Validation Layer

The Python component simulates an environment/application validation service.

The application provides:

* application identification
* version information
* environment information
* health status
* timestamp generation
* application logging

Example health information:

```json
{
    "app": "environment-access-validator",
    "version": "1.0.0",
    "env": "development",
    "status": "healthy"
}
```

The Python application is located at:

```text
repo_simulation/app.py
```

---

# 2. Laravel REST Service

The project includes a Laravel application located at:

```text
php-service/
```

A health-check API endpoint was implemented:

```text
GET /api/health
```

The endpoint returns JSON containing the Laravel application's:

* application name
* version
* status
* environment
* timestamp

Example response:

```json
{
    "app": "php-validation-service",
    "version": "1.0.0",
    "status": "healthy",
    "environment": "local",
    "timestamp": "..."
}
```

This provides a simple REST interface that can be consumed by another application.

---

# 3. Python → Laravel Integration

The Python validation layer communicates with the Laravel service through HTTP.

The integration component is:

```text
repo_simulation/laravel_health_check.py
```

It performs the following process:

```text
Python Validator
      │
      │ HTTP GET
      ▼
/api/health
      │
      │ JSON
      ▼
Laravel Service
      │
      ▼
Python validates:
      │
      ├── status
      ├── application name
      ├── version
      └── environment
```

If the Laravel service reports a healthy status, the Python validation process succeeds.

If the service cannot be reached or returns an invalid response, the validation process fails.

---

# 4. Automated Testing

The Laravel application contains a feature test:

```text
php-service/tests/Feature/HealthApiTest.php
```

The test verifies that:

* `/api/health` responds successfully
* the application name is correct
* the version is correct
* the service reports a healthy status

Laravel tests can be executed with:

```bash
cd php-service
php artisan test
```

---

# 5. Python Code Quality

Pylint is used to analyze the Python validation components.

Run:

```bash
pylint repo_simulation/*.py
```

The current Python validation code passes local Pylint analysis with:

```text
10.00/10
```

---

# 6. CI/CD with GitHub Actions

The project uses GitHub Actions to automatically validate changes.

Two workflows are configured.

### Python Pylint Workflow

```text
.github/workflows/pylint.yml
```

This workflow:

1. Checks out the repository
2. Installs Python
3. Installs Pylint
4. Analyzes Python source files

### Laravel Validation Workflow

```text
.github/workflows/php-laravel.yml
```

This workflow:

1. Checks out the repository
2. Installs PHP
3. Installs Composer dependencies
4. Creates the Laravel environment
5. Generates the application key
6. Runs Laravel tests

This means code changes can be automatically validated before being considered ready.

---

# 7. Local Setup

## Clone the repository

```bash
git clone https://github.com/rey26341-sudo/ENVIRONMENT-ACCESS-VALIDATION.git
cd ENVIRONMENT-ACCESS-VALIDATION
```

---

## Run the Python application

```bash
python3 repo_simulation/app.py
```

---

## Install Laravel dependencies

```bash
cd php-service
composer install
```

Create the environment file:

```bash
cp .env.example .env
```

Generate the Laravel application key:

```bash
php artisan key:generate
```

---

## Start the Laravel server

```bash
php artisan serve --port=8001
```

The application will be available at:

```text
http://127.0.0.1:8001
```

---

## Test the Laravel API

Open another terminal and run:

```bash
curl http://127.0.0.1:8001/api/health
```

Expected result:

```json
{
    "app": "php-validation-service",
    "version": "1.0.0",
    "status": "healthy",
    "environment": "local"
}
```

---

## Run the Python → Laravel integration

With Laravel running:

```bash
python3 repo_simulation/laravel_health_check.py
```

Expected output:

```text
Laravel service is healthy.
App: php-validation-service
Version: 1.0.0
Environment: local
```

---

# 8. Run Tests

Laravel:

```bash
cd php-service
php artisan test
```

Python:

```bash
cd ..
pylint repo_simulation/*.py
```

---

# 9. CI/CD Workflow

The intended development workflow is:

```text
Developer
    │
    ▼
Git branch
    │
    ▼
Code changes
    │
    ▼
Git commit
    │
    ▼
GitHub
    │
    ├───────────────┐
    ▼               ▼
Python Pylint    Laravel Tests
    │               │
    ▼               ▼
Code Quality     API Validation
    │               │
    └───────┬───────┘
            ▼
       CI Result
```

---

# 10. Engineering Objective

Although this project is primarily a software project, it demonstrates an important engineering practice:

> **Validating the behavior of one system component from another system component through an automated interface.**

The same principle is commonly used in larger distributed systems, industrial monitoring applications, automation platforms, robotics systems, and IoT environments.

The project therefore provides a foundation for extending the validation architecture toward:

* service monitoring
* IoT device validation
* hardware telemetry
* robotics systems
* equipment monitoring
* automated diagnostics
* cloud-based validation services

---

# 11. Future Improvements

Planned improvements include:

* Automated Laravel server startup inside CI
* Python → Laravel integration testing inside GitHub Actions
* API request/response validation
* Configuration-driven validation checks
* Structured logging
* Docker containerization
* API authentication
* Database-backed validation records
* Monitoring dashboard
* Health and readiness endpoints
* Automated deployment pipeline

---

## Portfolio Summary

This project demonstrates practical experience across multiple layers of modern software development:

```text
Python
  +
PHP / Laravel
  +
REST APIs
  +
Automated Testing
  +
Git
  +
GitHub Actions
  +
CI/CD
```

The project focuses on building and validating a small multi-language service architecture rather than demonstrating a single isolated programming language.



## What I Actually Did — Step by Step

1. Opened **AWS CloudShell** in browser (ap-south-1, Mumbai region)
2. Created project folder: `mkdir env_acc_val && cd env_acc_val`

   <img width="1920" height="1020" alt="2026-03-03 (5)" src="https://github.com/user-attachments/assets/83a46c1b-459e-4191-8e00-74a06d9741b4" />

4. Created all files using Linux commands (`echo`, `mkdir`, `nano`)
5. Ran real validation checks: `whoami`, `uname -n`, `uptime`, `ls -R`

   <img width="1920" height="1020" alt="2026-03-03 (16)" src="https://github.com/user-attachments/assets/4e36d030-b2e4-47f7-bc7b-2015275e94e7" />

   <img width="1920" height="1020" alt="2026-03-03 (17)" src="https://github.com/user-attachments/assets/0eb07b79-0b7c-475a-9d6a-43bc81c751ed" />
   
6.Wrote the checklist report using `nano`

   <img width="1920" height="1020" alt="2026-03-03 (19)" src="https://github.com/user-attachments/assets/6e0cbfac-5fb0-4402-822b-15f76a61ce4b" />
   
   <img width="1920" height="1020" alt="2026-03-03 (21)" src="https://github.com/user-attachments/assets/174cf6ee-eb95-4054-8ac4-54ec1b58d5c9" />

8. Initialized Git: `git init` → `git add .` → `git commit`

   <img width="1920" height="1020" alt="2026-03-03 (25)" src="https://github.com/user-attachments/assets/d67b070e-fbfe-42ab-892a-cd57a6431daa" />

   <img width="1920" height="1020" alt="2026-03-03 (26)" src="https://github.com/user-attachments/assets/7c31d73a-6f8c-447b-8faa-68627879a292" />

   <img width="1920" height="1020" alt="2026-03-03 (29)" src="https://github.com/user-attachments/assets/66a1545e-d813-47d8-bb30-532f361ad9ac" />

10. Fixed Git identity error with `git config --global`
11. Generated SSH key pair: `ssh-keygen -t ed25519`

<img width="1920" height="1020" alt="2026-03-03 (28)" src="https://github.com/user-attachments/assets/bade8a7b-9007-408f-acda-7fefeeacdd84" />

11. Connected repo to GitHub: `git remote set-url origin`
12. Pushed all files to GitHub

---

## What I Learned

- How a real Linux cloud environment (AWS CloudShell) works
- Linux commands: `mkdir`, `echo`, `cat`, `ls`, `nano`, `cd`, `pwd`, `whoami`, `uname`, `uptime`
- Setting up Git from scratch in a new environment
- Configuring SSH key authentication for GitHub
- What pre-deployment checks actually are and why they matter
- Writing a CI/CD pipeline with GitHub Actions
- Documenting real issues and their resolutions

---

## Tools & Technologies

- **AWS CloudShell** — real Linux terminal on AWS (ap-south-1, Mumbai)
- **Python 3** — scripting and automation
- **Bash / Linux** — all file creation done via terminal commands
- **Git** — version control initialized from scratch
- **GitHub Actions** — CI/CD pipeline automation
- **SSH (ed25519)** — secure key authentication to GitHub
- **nano** — terminal text editor

--

## Project Status

This is a **learning and practice project** built to understand DevOps pre-deployment validation concepts.
Executed in a real cloud environment (AWS CloudShell) but does not connect to a live production server.

---

## Author

**Rey** — Aspiring DevOps Engineer
Self-taught | DevOps Course Certified | Hands-on Practice
[GitHub Profile](https://
