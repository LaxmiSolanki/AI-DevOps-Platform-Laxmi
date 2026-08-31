# AI DevOps Platform

An AI-powered DevOps platform designed to automate application deployment, monitoring, failure detection, and intelligent problem analysis.

The platform is being developed as a final-year project with the long-term goal of combining **DevOps automation, monitoring, and AI-assisted troubleshooting** into a single platform.

---

## 1. Project Overview

Modern applications require continuous development, testing, deployment, monitoring, and troubleshooting.

When a production application fails, developers and DevOps engineers normally need to:

1. Detect the failure.
2. Identify the affected service.
3. Inspect logs and metrics.
4. Determine the possible root cause.
5. Fix the problem.
6. Deploy the fix.
7. Verify that the application has recovered.

The goal of this project is to build a platform that can automate as much of this process as possible.

The final platform is intended to:

* Automate application build and deployment.
* Run automated tests.
* Containerize applications.
* Deploy applications using Kubernetes.
* Monitor application health and system metrics.
* Collect logs and operational information.
* Detect failures and abnormal behavior.
* Use AI to analyze detected problems.
* Provide possible causes and remediation recommendations.

---

# 2. Current Project Status

## Milestone 1 — Project Foundation & Local Development Environment

### Completed

* GitHub repository and collaboration setup.
* Feature-branch development workflow.
* Basic Flask web application.
* `/` application endpoint.
* `/health` health-check endpoint.
* Python virtual environment.
* Dependency management using `requirements.txt`.
* Automated testing using `pytest`.
* Pytest configuration using `pytest.ini`.
* Environment-based configuration using `.env`.
* `.env.example` configuration template.
* Git protection for `.env` and development files.
* Initial project documentation.

### Current application

```text
Flask Application
       │
       ├── GET /
       │
       └── GET /health
```

---

# 3. Project Architecture

The final project is planned to evolve toward the following architecture:

```text
                         Developer
                             │
                             ▼
                          GitHub
                             │
                             ▼
                         Jenkins
                             │
              ┌──────────────┼──────────────┐
              │              │              │
              ▼              ▼              ▼
           Testing         Build       Quality/Security
              │              │              │
              └──────────────┼──────────────┘
                             │
                             ▼
                       Docker Image
                             │
                             ▼
                        Kubernetes
                             │
                    ┌────────┴────────┐
                    │                 │
                    ▼                 ▼
              Application         Monitoring
                    │                 │
                    │          ┌──────┴──────┐
                    │          │             │
                    │          ▼             ▼
                    │      Prometheus     Grafana
                    │
                    ▼
                  Logs
                    │
                    ▼
                AI Analysis
                    │
                    ▼
          Failure Detection /
          Root Cause Analysis /
          Recommendations
```

> **Note:** Components shown beyond Milestone 1 are part of the planned project roadmap and are not yet implemented.

---

# 4. Technology Stack

The project will progressively use the following technologies.

| Technology | Purpose                                            |
| ---------- | -------------------------------------------------- |
| Python     | Application and automation development             |
| Flask      | Initial web application                            |
| pytest     | Automated testing                                  |
| Git        | Version control                                    |
| GitHub     | Source-code hosting and collaboration              |
| Docker     | Application containerization                       |
| Jenkins    | CI/CD automation                                   |
| Kubernetes | Container orchestration                            |
| Prometheus | Metrics collection and monitoring                  |
| Grafana    | Monitoring dashboards and visualization            |
| AI/LLM     | Failure analysis and intelligent recommendations   |
| Ansible    | Configuration/deployment automation where required |
| Terraform  | Infrastructure provisioning where required         |

Technologies will be introduced gradually according to the project milestones.

---

# 5. Project Structure

Current project structure:

```text
project-root/
│
├── app/
│   ├── __init__.py
│   └── main.py
│
├── tests/
│   └── test_health.py
│
├── config/
│   └── .gitkeep
│
├── docs/
│   └── architecture.md
│
├── .env.example
├── .gitignore
├── README.md
├── pytest.ini
└── requirements.txt
```

### Directory and file purposes

#### `app/`

Contains the application source code.

#### `app/main.py`

Contains the Flask application and its endpoints.

#### `app/__init__.py`

Marks the `app` directory as a Python package.

#### `tests/`

Contains automated application tests.

#### `tests/test_health.py`

Tests the `/health` endpoint.

#### `config/`

Reserved for application/configuration-related files that will be introduced as the project grows.

#### `docs/`

Contains project documentation and architecture information.

#### `.env.example`

Example environment configuration that can safely be committed to GitHub.

#### `.env`

Local environment configuration.

This file must **not** be committed to GitHub.

#### `.gitignore`

Specifies files and directories that Git should ignore.

#### `pytest.ini`

Contains pytest configuration, including the test directory and Python import path.

#### `requirements.txt`

Contains Python dependencies required by the project.

---

# 6. Prerequisites

For the current Milestone 1 environment, install:

* Python 3.13
* Git
* Visual Studio Code
* A GitHub account with access to the project repository

Later milestones will introduce additional tools such as:

* Docker
* Jenkins
* Kubernetes
* Prometheus
* Grafana
* Terraform
* Ansible

---

# 7. Clone the Repository

Clone the appropriate project repository:

```bash
git clone <repository-url>
```

Move into the project directory:

```bash
cd <project-folder>
```

Verify that Git is working:

```bash
git status
```

---

# 8. Python Virtual Environment

The project uses a Python virtual environment so that project dependencies remain isolated from the global Python installation.

## Create the virtual environment

From the project root:

### Windows PowerShell

```powershell
python -m venv venv
```

This creates:

```text
venv/
```

inside the project directory.

---

# 9. Activate the Virtual Environment

For Windows PowerShell:

```powershell
.\venv\Scripts\Activate.ps1
```

After successful activation, the terminal should show:

```text
(venv)
```

For example:

```text
(venv) PS D:\Project\AI-DevOps-Platform>
```

---

# 10. Verify the Python Environment

After activating the virtual environment, verify which Python executable is being used:

```powershell
python -c "import sys; print(sys.executable)"
```

The output should point to the project's virtual environment:

```text
...\project-root\venv\Scripts\python.exe
```

This verification is important because installing packages with the wrong Python environment can cause dependency and import errors.

---

# 11. Install Dependencies

With the virtual environment activated:

```powershell
python -m pip install -r requirements.txt
```

Using:

```text
python -m pip
```

is preferred because it ensures that pip is associated with the currently selected Python interpreter.

To verify installed dependencies:

```powershell
python -m pip list
```

---

# 12. Environment Configuration

The application uses environment variables for configuration.

## `.env.example`

The repository contains:

```text
APP_ENV=development
APP_PORT=5000
```

This file acts as a template for developers.

## Create `.env`

Create a `.env` file in the project root:

```text
APP_ENV=development
APP_PORT=5000
```

The `.env` file is intended for local configuration and must not be committed to Git.

The `.gitignore` file contains:

```text
.env
```

to prevent accidental commits.

---

# 13. Run the Application

Make sure the virtual environment is active.

Run:

```powershell
python -m app.main
```

The application should start on:

```text
http://127.0.0.1:5000
```

---

# 14. Application Endpoints

## Home Endpoint

### Request

```text
GET /
```

URL:

```text
http://127.0.0.1:5000/
```

Expected response:

```text
AI DevOps Platform is running
```

---

## Health Endpoint

### Request

```text
GET /health
```

URL:

```text
http://127.0.0.1:5000/health
```

Expected response:

```json
{
    "status": "healthy",
    "environment": "development"
}
```

The health endpoint will become important in later milestones because it can be used by deployment and orchestration systems to determine whether the application is healthy.

---

# 15. Automated Testing

The project uses `pytest` for automated testing.

Make sure the virtual environment is active.

Run:

```powershell
python -m pytest
```

Expected result:

```text
1 passed
```

The current test verifies that:

* The `/health` endpoint exists.
* The endpoint returns HTTP status `200`.
* The response reports the application as healthy.

---

# 16. Pytest Configuration

The project contains:

```text
pytest.ini
```

Current configuration:

```ini
[pytest]
pythonpath = .
testpaths = tests
```

### Purpose

```ini
pythonpath = .
```

Adds the project root to Python's import path so application modules can be imported reliably during testing.

```ini
testpaths = tests
```

Tells pytest to look for tests inside the `tests/` directory.

---

# 17. Git Development Workflow

Development should be performed using feature branches.

Do not normally develop directly on `main`.

## Update local `main`

```bash
git checkout main
git pull origin main
```

## Create a feature branch

```bash
git checkout -b feature/<feature-name>
```

Example:

```bash
git checkout -b feature/m1-documentation
```

## Check changes

```bash
git status
```

## Stage changes

```bash
git add .
```

## Commit changes

```bash
git commit -m "feat: add project documentation"
```

## Push the feature branch

```bash
git push -u origin feature/<feature-name>
```

## Create Pull Request

Create a Pull Request on GitHub:

```text
feature/<feature-name>
        │
        ▼
      main
```

Changes should be reviewed and merged through the Pull Request workflow.

---

# 18. Git Safety

The following should not be committed:

```text
venv/
.env
__pycache__/
.pytest_cache/
*.pyc
```

The following should be committed:

```text
app/
tests/
docs/
config/
.env.example
.gitignore
README.md
pytest.ini
requirements.txt
```

---

# 19. Important Environment Rules

### Rule 1 — Use the project virtual environment

Before running Python-related commands, verify that the terminal is using:

```text
venv\Scripts\python.exe
```

### Rule 2 — Install dependencies using `requirements.txt`

Use:

```powershell
python -m pip install -r requirements.txt
```

### Rule 3 — Update `requirements.txt`

Whenever a new Python dependency is intentionally added to the project, update:

```text
requirements.txt
```

so that another developer and future CI/CD environments can reproduce the same dependency setup.

### Rule 4 — Never commit `.env`

Use:

```text
.env.example
```

for documenting required environment variables.

Keep actual local configuration in:

```text
.env
```

### Rule 5 — Run tests before committing

Use:

```powershell
python -m pytest
```

A change should not be considered ready until the automated tests pass.

---

# 20. Troubleshooting

## Python points to the wrong environment

Run:

```powershell
python -c "import sys; print(sys.executable)"
```

If the output does not point to:

```text
venv\Scripts\python.exe
```

activate the virtual environment:

```powershell
.\venv\Scripts\Activate.ps1
```

---

## Pytest cannot import the application

First make sure you are running pytest from the project root:

```powershell
python -m pytest
```

Then verify that `pytest.ini` exists at the project root:

```text
project-root/
└── pytest.ini
```

The configuration should contain:

```ini
[pytest]
pythonpath = .
testpaths = tests
```

---

## Flask is not installed

With the virtual environment activated:

```powershell
python -m pip install -r requirements.txt
```

---

## `.env` appears in Git status

Check `.gitignore` and make sure it contains:

```text
.env
```

Then run:

```powershell
git status
```

---

# 21. Development Principles

The project will follow these principles throughout development:

### Reproducibility

The same project should be reproducible on different development and CI environments.

### Automation

Manual repetitive DevOps tasks should progressively be automated.

### Testing

Changes should be validated through automated tests wherever practical.

### Observability

The deployed application should eventually expose useful health, metrics, and logging information.

### Security

Secrets should not be stored in source code or committed to Git.

### Infrastructure as Code

Infrastructure and deployment configuration should eventually be represented as version-controlled code.

### Continuous Improvement

The platform will be developed incrementally through milestones rather than implementing the entire system at once.

---

# 22. Project Roadmap

The project is planned to progress through the following stages.

## M0 — GitHub Repository & Collaboration Setup

* Repository creation
* Repository configuration
* Branch strategy
* Collaboration setup
* Git workflow

**Status: Completed**

---

## M1 — Project Foundation & Local Development Environment

* Flask application
* Health endpoint
* Python virtual environment
* Dependency management
* Automated tests
* Environment configuration
* Documentation

**Status: Completed**

---

## M2 — Docker Containerization

Planned work:

* Create Dockerfile
* Build application image
* Run application in Docker
* Configure container environment
* Add container health checks
* Test reproducibility

---

## M3 — Jenkins CI/CD

Planned work:

* Jenkins installation/configuration
* Source-code integration
* Automated testing
* Docker image building
* Pipeline automation
* Build failure handling

---

## M4 — Infrastructure Automation

Planned work:

* Infrastructure definition
* Terraform configuration
* Ansible configuration where appropriate
* Automated environment setup

---

## M5 — Kubernetes Deployment

Planned work:

* Kubernetes cluster setup
* Deployment manifests
* Services
* ConfigMaps
* Secrets
* Health probes
* Scaling
* Rolling deployments

---

## M6 — Monitoring & Observability

Planned work:

* Prometheus
* Grafana
* Application metrics
* Infrastructure metrics
* Dashboards
* Alerts
* Log collection

---

## M7 — AI-Powered DevOps Analysis

Planned work:

* Collect application and infrastructure information
* Detect abnormal behavior
* Analyze logs and metrics
* Identify possible root causes
* Generate troubleshooting recommendations
* Provide intelligent DevOps assistance

---

## M8 — Failure Simulation & Recovery

Planned work:

* Introduce controlled application failures
* Simulate deployment failures
* Simulate configuration problems
* Simulate resource problems
* Detect failures
* Analyze failures using the AI layer
* Validate recovery procedures

---

## M9 — Integration & Final Validation

Planned work:

* Integrate all major components
* End-to-end CI/CD validation
* Monitoring validation
* AI analysis validation
* Failure-recovery testing
* Performance evaluation
* Security review
* Final documentation

---

# 23. Final Project Goal

The final goal is to create a platform where a software change can progress through an automated DevOps lifecycle:

```text
Developer
    │
    ▼
GitHub
    │
    ▼
CI/CD Pipeline
    │
    ├── Build
    ├── Test
    ├── Security/Quality Checks
    │
    ▼
Docker
    │
    ▼
Kubernetes
    │
    ▼
Running Application
    │
    ├── Metrics
    ├── Logs
    └── Health Information
             │
             ▼
        AI Analysis
             │
             ▼
      Problem Detection
             │
             ▼
       Root Cause Analysis
             │
             ▼
     Recommended Actions
```

The objective is not simply to create another deployment pipeline.

The project aims to demonstrate how **DevOps automation, observability, and AI-assisted troubleshooting can work together to reduce the time and effort required to identify and resolve application problems.**

---

# 24. Current Milestone Verification

Before moving to the next milestone, verify:

```text
[ ] Repository is configured correctly
[ ] Feature branch is being used
[ ] Python virtual environment works
[ ] Dependencies install successfully
[ ] Flask application starts
[ ] GET / works
[ ] GET /health works
[ ] pytest runs successfully
[ ] pytest reports 1 passed
[ ] .env is ignored by Git
[ ] .env.example is present
[ ] README is up to date
```

---

## License

This project is developed as an academic final-year project.