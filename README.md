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

**Status: Completed**

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

## Milestone 2 — Docker Containerization

**Status: Completed**

### Completed

* Docker Desktop and Docker Engine verification.
* Docker fundamentals and container lifecycle understanding.
* Docker-ready Flask application configuration.
* `.dockerignore` creation.
* Dockerfile creation using `python:3.13-slim`.
* Docker image build and verification.
* Docker container execution with port mapping.
* Runtime environment variable override testing.
* Docker `HEALTHCHECK` configuration using `/health`.
* Container failure and recovery testing.
* Git feature branch, commit, push, Pull Request, and merge workflow.
* Final Docker and Git verification on `main`.

### M2 Docker flow

```text
Flask Application
       │
       ▼
   Dockerfile
       │
       ▼
Docker Image
ai-devops-platform:m2.10
       │
       ▼
Docker Container
ai-devops-platform-m2
       │
       ├── Host port 5000 → Container port 5000
       │
       ├── GET /
       │
       └── GET /health
                │
                ▼
        Docker HEALTHCHECK
```

### M2 verification result

```text
Container: running
Health:     healthy
GET /:      HTTP 200
GET /health: HTTP 200
Git:        main synchronized and clean
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

> **Note:** Components beyond the completed M2 Docker layer are part of the planned project roadmap and are not yet implemented.

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
├── .dockerignore
├── .env.example
├── .gitignore
├── Dockerfile
├── README.md
├── pytest.ini
└── requirements.txt
```

> Local-only files such as `venv/` and `.env` exist during development but are intentionally not part of the tracked project structure.


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

#### `Dockerfile`

Defines how the Flask application is packaged into a Docker image. The current Dockerfile uses Python 3.13 slim, installs dependencies from `requirements.txt`, copies the application, configures `APP_ENV` and `APP_PORT`, exposes port `5000`, defines a Docker `HEALTHCHECK`, and starts the application with `python -m app.main`.

#### `.dockerignore`

Controls which local files are excluded from the Docker build context. It excludes the virtual environment, `.env`, Git metadata, Python cache files, editor configuration, and log files.

---

# 6. Prerequisites

For the completed M1 and M2 development environment, install:

* Python 3.13
* Git
* Visual Studio Code
* A GitHub account with access to the project repository
* Docker Desktop with Linux containers enabled

Later milestones will introduce additional tools such as:

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

# 16. Docker Containerization

Milestone 2 adds Docker support so the Flask application can be built and run as a reproducible container.

## Dockerfile

The current Dockerfile is:

```dockerfile
FROM python:3.13-slim

WORKDIR /app

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY app ./app

ENV APP_ENV=development
ENV APP_PORT=5000

EXPOSE 5000

HEALTHCHECK --interval=30s --timeout=5s --start-period=5s --retries=3 CMD python -c "import urllib.request; urllib.request.urlopen('http://localhost:5000/health', timeout=3)"

CMD ["python", "-m", "app.main"]
```

### Dockerfile responsibilities

* Uses Python 3.13 slim as the base image.
* Sets `/app` as the working directory.
* Installs dependencies from `requirements.txt`.
* Copies the application source into the image.
* Provides default `APP_ENV=development`.
* Provides default `APP_PORT=5000`.
* Exposes container port `5000`.
* Uses `/health` as the Docker health-check target.
* Starts the Flask application with `python -m app.main`.

## `.dockerignore`

The Docker build context excludes:

```text
venv/
.env
.git/
.github/
__pycache__/
.pytest_cache/
*.pyc
*.pyo
*.pyd
.vscode/
*.log
```

This keeps local development artifacts, Git metadata, environment secrets, and cache files out of the Docker build context.

## Build the Docker image

From the project root:

```powershell
docker build -t ai-devops-platform:m2.10 .
```

The M2 implementation was successfully built and verified using the image tag:

```text
ai-devops-platform:m2.10
```

## Run the container

```powershell
docker run --name ai-devops-platform-m2 -p 5000:5000 ai-devops-platform:m2.10
```

The application is exposed through:

```text
http://localhost:5000
```

The host port `5000` is mapped to container port `5000`.

## Verify the container

```powershell
docker ps --filter "name=ai-devops-platform-m2"
```

Expected state:

```text
Up ... (healthy)
```

## Verify the application

```powershell
(Invoke-WebRequest http://localhost:5000/).StatusCode
```

Expected:

```text
200
```

```powershell
(Invoke-WebRequest http://localhost:5000/).Content
```

Expected:

```text
AI DevOps Platform is running
```

For the health endpoint:

```powershell
(Invoke-WebRequest http://localhost:5000/health).StatusCode
```

Expected:

```text
200
```

```powershell
(Invoke-WebRequest http://localhost:5000/health).Content
```

Expected:

```json
{"environment":"development","status":"healthy"}
```

## Runtime environment configuration

The container supports runtime environment overrides.

Example:

```powershell
docker run --name ai-devops-platform-m2-env -p 5001:5000 -e APP_ENV=container-test ai-devops-platform:m2.10
```

This allows the container environment to override the default `APP_ENV` without changing application source code.

## Docker HEALTHCHECK

The Dockerfile defines:

```dockerfile
HEALTHCHECK --interval=30s --timeout=5s --start-period=5s --retries=3 CMD python -c "import urllib.request; urllib.request.urlopen('http://localhost:5000/health', timeout=3)"
```

Docker periodically requests the application's `/health` endpoint from inside the container.

A successful check produces:

```text
Health=healthy
```

The final M2 verification showed repeated health-check results with `ExitCode=0` and:

```text
FailingStreak=0
Status=healthy
```

## Failure and recovery testing

M2 also tested the container failure/recovery lifecycle.

The application/container was intentionally stopped and Docker reported:

```text
exited | Health=unhealthy | ExitCode=137
```

The existing container was then started again:

```powershell
docker start ai-devops-platform-m2
```

After recovery, the final state was:

```text
running | Health=healthy | ExitCode=0
```

Both application endpoints returned HTTP `200` after recovery.

> **Important:** Docker `HEALTHCHECK` detects and reports health; it does not by itself provide the full orchestration and recovery behavior that will later be handled by Kubernetes.

# 16. Automated Testing

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

# 17. Pytest Configuration

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

# 18. Git Development Workflow

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

# 19. Git Safety

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

# 20. Important Environment Rules

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

# 21. Troubleshooting

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

# 22. Development Principles

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

# 23. Project Roadmap

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

**Status: Completed**

Completed work:

* Verified Docker Desktop and Docker Engine.
* Prepared the Flask application for containerization.
* Created `.dockerignore`.
* Created the Dockerfile.
* Built the `ai-devops-platform:m2.10` image.
* Ran the `ai-devops-platform-m2` container.
* Verified host-to-container port mapping on port `5000`.
* Tested `/` and `/health`.
* Tested runtime environment variable override.
* Added and verified Docker `HEALTHCHECK`.
* Tested container failure and recovery.
* Committed Docker changes through a feature branch.
* Created and merged GitHub Pull Request #3 into `main`.
* Performed final Docker and Git verification on `main`.

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

# 24. Final Project Goal

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

# 25. Current Milestone Verification

M0, M1, and M2 have been completed. The following checks have been verified during development:

```text
[x] Repository is configured correctly
[x] Feature-branch workflow is used
[x] Python virtual environment works
[x] Dependencies install successfully
[x] Flask application starts
[x] GET / works
[x] GET /health works
[x] pytest configuration is present
[x] .env is ignored by Git
[x] .env.example is present
[x] Docker Desktop/Engine works
[x] Dockerfile is present and tracked
[x] .dockerignore is present and tracked
[x] Docker image builds successfully
[x] Docker container starts successfully
[x] Host port 5000 maps to container port 5000
[x] Docker runtime environment override was tested
[x] Docker HEALTHCHECK reports healthy
[x] Container failure and recovery were tested
[x] Docker endpoints return HTTP 200
[x] M2 changes were merged through Pull Request #3
[x] Local main is synchronized with origin/main
[x] Working tree is clean
```

### Current verified Docker state

```text
Docker image:
ai-devops-platform:m2.10

Container:
ai-devops-platform-m2

Container state:
running

Health:
healthy

GET /:
HTTP 200

GET /health:
HTTP 200
```

---

# 26. Milestone Summary

```text
M0  GitHub Repository & Collaboration       Completed
M1  Project Foundation & Local Development  Completed
M2  Docker Containerization                 Completed
M3  Jenkins CI/CD                           Planned
M4  Infrastructure Automation               Planned
M5  Kubernetes Deployment                   Planned
M6  Monitoring & Observability              Planned
M7  AI-Powered DevOps Analysis              Planned
M8  Failure Simulation & Recovery           Planned
M9  Integration & Final Validation          Planned
```

The project is currently ready to proceed from the completed Docker foundation into the planned CI/CD stage.

## License

This project is developed as an academic final-year project.