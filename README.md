# AI DevOps Platform

An AI-powered DevOps platform designed to automate application
deployment, monitoring, failure detection, and intelligent problem
analysis.

The platform is being developed as a final-year project with the
long-term goal of combining **DevOps automation, monitoring, and
AI-assisted troubleshooting** into a single platform.

------------------------------------------------------------------------

## 1. Project Overview

Modern applications require continuous development, testing, deployment,
monitoring, and troubleshooting.

When a production application fails, developers and DevOps engineers
normally need to:

1.  Detect the failure.
2.  Identify the affected service.
3.  Inspect logs and metrics.
4.  Determine the possible root cause.
5.  Fix the problem.
6.  Deploy the fix.
7.  Verify that the application has recovered.

The goal of this project is to build a platform that can automate as
much of this process as possible.

The final platform is intended to:

-   Accept and support different types of applications through a
    standardized deployment contract.
-   Automate application build and deployment.
-   Run automated tests.
-   Containerize applications.
-   Deploy applications using Kubernetes.
-   Monitor application health and system metrics.
-   Collect logs and operational information.
-   Detect failures and abnormal behavior.
-   Use AI to analyze detected problems.
-   Provide possible causes and remediation recommendations.
-   Progressively reduce the amount of application-specific DevOps
    configuration required from a developer.

------------------------------------------------------------------------

# 2. Project Vision & Application Strategy

The platform is **not intended to be limited to the current Flask
application**.

The Flask application used during M1 and M2 is a deliberately small
**reference/demo workload**. It provides a stable application on which
the DevOps infrastructure can be developed and verified without allowing
application-development complexity to dominate the project.

The long-term vision is to make the platform as **application-agnostic
as reasonably practical**.

A suitable application should be able to enter the platform through a
standardized interface such as:

``` text
Application Source
       │
       ├── Source code
       ├── Build configuration
       ├── Dependencies
       ├── Environment variables
       ├── Application port
       ├── Health endpoint/check
       └── Deployment requirements
                │
                ▼
        AI-DevOps Platform
```

The platform should therefore be capable of working with different
application technologies, for example:

  Application type               Target support
  ------------------------------ ---------------------------------------
  Flask                          Reference application
  FastAPI                        Potential final/reference application
  Django                         Planned/general compatibility
  Node.js / Express              Planned/general compatibility
  React or other frontend        Planned/general compatibility
  Java / Spring Boot             Planned/general compatibility
  Go applications                Planned/general compatibility
  .NET applications              Planned/general compatibility
  Static websites                Potential support
  Multi-container applications   Support with additional configuration

> **Important:** "Application-agnostic" does not mean that literally
> every application can be deployed with zero configuration.
> Applications may have different runtimes, dependencies, databases,
> hardware requirements, networking requirements, secrets, or deployment
> architectures. The platform will aim to standardize the common
> deployment workflow while allowing application-specific configuration
> where necessary.

### Current application vs. final showcase application

The project will use the current Flask application as the **initial
reference workload** while the DevOps foundation is established.

Later in the project, the application layer may be enhanced into a more
realistic demonstration application, potentially including:

-   A web dashboard.
-   A REST API.
-   A database.
-   Authentication where appropriate.
-   Application health endpoints.
-   Metrics and operational information.
-   A small AI-related component or integration where it supports the
    project objective.

The final application should remain intentionally small enough that the
main focus of the project remains **DevOps automation, infrastructure,
observability, and AI-assisted troubleshooting**, rather than becoming a
separate large web-development project.

### Flask vs. FastAPI

The current application uses Flask because it is lightweight, mature,
and sufficient for establishing the initial application and DevOps
foundation.

FastAPI is also a suitable option, particularly if the application
evolves toward a more API-centric architecture. It provides modern
API-development features such as request validation and automatic
OpenAPI/Swagger documentation.

The project does **not** need to switch from Flask to FastAPI during M3
merely for framework modernization. A framework change would be
considered later if it provides a clear benefit to the final application
architecture.

The important design principle is:

> **The DevOps platform should not depend on one particular application
> framework.**

The application framework is therefore a replaceable workload-level
decision, while Docker, Jenkins, Terraform, Ansible, Kubernetes,
monitoring, and AI-assisted analysis form the platform-level
architecture.

### Long-term AI-assisted application onboarding

A future enhancement is to allow the platform's AI layer to inspect an
application and identify information such as:

``` text
Detected language
Detected framework
Dependencies
Likely application entry point
Application port
Build requirements
Health-check capability
Containerization requirements
Deployment requirements
```

The AI could then assist in generating or validating deployment
configuration.

This is a **future capability**, not a claim that the current M3
implementation already performs automatic application discovery.

------------------------------------------------------------------------

# 3. Current Project Status

## Milestone 1 --- Project Foundation & Local Development Environment

**Status: Completed**

### Completed

-   GitHub repository and collaboration setup.
-   Feature-branch development workflow.
-   Basic Flask web application.
-   `/` application endpoint.
-   `/health` health-check endpoint.
-   Python virtual environment.
-   Dependency management using `requirements.txt`.
-   Automated testing using `pytest`.
-   Pytest configuration using `pytest.ini`.
-   Environment-based configuration using `.env`.
-   `.env.example` configuration template.
-   Git protection for `.env` and development files.
-   Initial project documentation.

### Current reference application

``` text
Flask Application
       │
       ├── GET /
       │
       └── GET /health
```

This application is the current reference workload for M1--M3. It is
intentionally simple so that the project can establish the DevOps
pipeline before increasing application complexity.

------------------------------------------------------------------------

## Milestone 2 --- Docker Containerization

**Status: Completed**

### Completed

-   Docker Desktop and Docker Engine verification.
-   Docker fundamentals and container lifecycle understanding.
-   Docker-ready Flask application configuration.
-   `.dockerignore` creation.
-   Dockerfile creation using `python:3.13-slim`.
-   Docker image build and verification.
-   Docker container execution with port mapping.
-   Runtime environment variable override testing.
-   Docker `HEALTHCHECK` configuration using `/health`.
-   Container failure and recovery testing.
-   Git feature branch, commit, push, Pull Request, and merge workflow.
-   Final Docker and Git verification on `main`.

### M2 Docker flow

``` text
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

``` text
Container: running
Health:     healthy
GET /:      HTTP 200
GET /health: HTTP 200
Git:        main synchronized and clean
```

------------------------------------------------------------------------

# 4. Project Architecture

The final project is planned to evolve toward an application-agnostic
architecture in which the current Flask application is one reference
workload rather than the platform's permanent limitation:

``` text
                    Developer
                        │
                        ▼
             Application Source / GitHub
                        │
                        ▼
                AI-Assisted Analysis
                        │
            ┌───────────┼───────────┐
            ▼           ▼           ▼
        Language     Framework    Dependencies
        Detection    Detection     / Config
            │           │           │
            └───────────┼───────────┘
                        ▼
                Deployment Contract
                        │
                        ▼
                     Jenkins
                        │
          ┌─────────────┼─────────────┐
          │             │             │
          ▼             ▼             ▼
       Testing        Build      Quality/Security
          │             │             │
          └─────────────┼─────────────┘
                        ▼
                  Docker Image
                        │
                        ▼
                Registry / Artifact
                        │
                        ▼
                  Kubernetes
                        │
                 ┌──────┴──────┐
                 │             │
                 ▼             ▼
           Application     Monitoring
                 │             │
                 │       ┌─────┴─────┐
                 │       │           │
                 │       ▼           ▼
                 │   Prometheus   Grafana
                 │
                 ▼
                Logs
                 │
                 ▼
             AI Analysis
                 │
        ┌────────┼─────────┐
        ▼        ▼         ▼
     Failure   Root Cause  Recommended
     Detection  Analysis    Actions
```

The platform-level pipeline should be reusable across different
supported application workloads.

> **Note:** Components beyond the completed M2 Docker layer are part of
> the planned project roadmap and are not yet implemented.

------------------------------------------------------------------------

# 5. Technology Stack

The project will progressively use the following technologies.

  -----------------------------------------------------------------------
  Technology                          Purpose
  ----------------------------------- -----------------------------------
  Python                              Application and automation
                                      development

  Flask                               Current lightweight reference
                                      application

  FastAPI                             Possible later API-oriented
                                      application framework

  pytest                              Automated testing

  Git                                 Version control

  GitHub                              Source-code hosting and
                                      collaboration

  Docker                              Standardized application
                                      containerization

  Jenkins                             CI/CD automation

  Kubernetes                          Container orchestration

  Prometheus                          Metrics collection and monitoring

  Grafana                             Monitoring dashboards and
                                      visualization

  AI/LLM                              Application analysis, failure
                                      analysis, and intelligent
                                      recommendations

  Ansible                             Configuration/deployment automation
                                      where required

  Terraform                           Infrastructure provisioning where
                                      required
  -----------------------------------------------------------------------

Technologies will be introduced gradually according to the project
milestones.

------------------------------------------------------------------------

# 6. Project Structure

Current project structure:

``` text
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

> Local-only files such as `venv/` and `.env` exist during development
> but are intentionally not part of the tracked project structure.

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

Reserved for application/configuration-related files that will be
introduced as the project grows.

#### `docs/`

Contains project documentation and architecture information.

#### `.env.example`

Example environment configuration that can safely be committed to
GitHub.

#### `.env`

Local environment configuration.

This file must **not** be committed to GitHub.

#### `.gitignore`

Specifies files and directories that Git should ignore.

#### `pytest.ini`

Contains pytest configuration, including the test directory and Python
import path.

#### `requirements.txt`

Contains Python dependencies required by the project.

#### `Dockerfile`

Defines how the Flask application is packaged into a Docker image. The
current Dockerfile uses Python 3.13 slim, installs dependencies from
`requirements.txt`, copies the application, configures `APP_ENV` and
`APP_PORT`, exposes port `5000`, defines a Docker `HEALTHCHECK`, and
starts the application with `python -m app.main`.

#### `.dockerignore`

Controls which local files are excluded from the Docker build context.
It excludes the virtual environment, `.env`, Git metadata, Python cache
files, editor configuration, and log files.

------------------------------------------------------------------------

# 7. Prerequisites

For the completed M1 and M2 development environment, install:

-   Python 3.13
-   Git
-   Visual Studio Code
-   A GitHub account with access to the project repository
-   Docker Desktop with Linux containers enabled

Later milestones will introduce additional tools such as:

-   Jenkins
-   Kubernetes
-   Prometheus
-   Grafana
-   Terraform
-   Ansible

------------------------------------------------------------------------

# 8. Clone the Repository

Clone the appropriate project repository:

``` bash
git clone <repository-url>
```

Move into the project directory:

``` bash
cd <project-folder>
```

Verify that Git is working:

``` bash
git status
```

------------------------------------------------------------------------

# 9. Python Virtual Environment

The project uses a Python virtual environment so that project
dependencies remain isolated from the global Python installation.

## Create the virtual environment

From the project root:

### Windows PowerShell

``` powershell
python -m venv venv
```

This creates:

``` text
venv/
```

inside the project directory.

------------------------------------------------------------------------

# 10. Activate the Virtual Environment

For Windows PowerShell:

``` powershell
.\venv\Scripts\Activate.ps1
```

After successful activation, the terminal should show:

``` text
(venv)
```

For example:

``` text
(venv) PS D:\Project\AI-DevOps-Platform>
```

------------------------------------------------------------------------

# 11. Verify the Python Environment

After activating the virtual environment, verify which Python executable
is being used:

``` powershell
python -c "import sys; print(sys.executable)"
```

The output should point to the project's virtual environment:

``` text
...\project-root\venv\Scripts\python.exe
```

This verification is important because installing packages with the
wrong Python environment can cause dependency and import errors.

------------------------------------------------------------------------

# 12. Install Dependencies

With the virtual environment activated:

``` powershell
python -m pip install -r requirements.txt
```

Using:

``` text
python -m pip
```

is preferred because it ensures that pip is associated with the
currently selected Python interpreter.

To verify installed dependencies:

``` powershell
python -m pip list
```

------------------------------------------------------------------------

# 13. Environment Configuration

The application uses environment variables for configuration.

## `.env.example`

The repository contains:

``` text
APP_ENV=development
APP_PORT=5000
```

This file acts as a template for developers.

## Create `.env`

Create a `.env` file in the project root:

``` text
APP_ENV=development
APP_PORT=5000
```

The `.env` file is intended for local configuration and must not be
committed to Git.

The `.gitignore` file contains:

``` text
.env
```

to prevent accidental commits.

------------------------------------------------------------------------

# 14. Run the Application

Make sure the virtual environment is active.

Run:

``` powershell
python -m app.main
```

The application should start on:

``` text
http://127.0.0.1:5000
```

------------------------------------------------------------------------

# 15. Application Endpoints

## Home Endpoint

### Request

``` text
GET /
```

URL:

``` text
http://127.0.0.1:5000/
```

Expected response:

``` text
AI DevOps Platform is running
```

------------------------------------------------------------------------

## Health Endpoint

### Request

``` text
GET /health
```

URL:

``` text
http://127.0.0.1:5000/health
```

Expected response:

``` json
{
    "status": "healthy",
    "environment": "development"
}
```

The health endpoint will become important in later milestones because it
can be used by deployment and orchestration systems to determine whether
the application is healthy.

------------------------------------------------------------------------

# 16. Docker Containerization

Milestone 2 adds Docker support so the Flask application can be built
and run as a reproducible container.

## Dockerfile

The current Dockerfile is:

``` dockerfile
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

-   Uses Python 3.13 slim as the base image.
-   Sets `/app` as the working directory.
-   Installs dependencies from `requirements.txt`.
-   Copies the application source into the image.
-   Provides default `APP_ENV=development`.
-   Provides default `APP_PORT=5000`.
-   Exposes container port `5000`.
-   Uses `/health` as the Docker health-check target.
-   Starts the Flask application with `python -m app.main`.

## `.dockerignore`

The Docker build context excludes:

``` text
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

This keeps local development artifacts, Git metadata, environment
secrets, and cache files out of the Docker build context.

## Build the Docker image

From the project root:

``` powershell
docker build -t ai-devops-platform:m2.10 .
```

The M2 implementation was successfully built and verified using the
image tag:

``` text
ai-devops-platform:m2.10
```

## Run the container

``` powershell
docker run --name ai-devops-platform-m2 -p 5000:5000 ai-devops-platform:m2.10
```

The application is exposed through:

``` text
http://localhost:5000
```

The host port `5000` is mapped to container port `5000`.

## Verify the container

``` powershell
docker ps --filter "name=ai-devops-platform-m2"
```

Expected state:

``` text
Up ... (healthy)
```

## Verify the application

``` powershell
(Invoke-WebRequest http://localhost:5000/).StatusCode
```

Expected:

``` text
200
```

``` powershell
(Invoke-WebRequest http://localhost:5000/).Content
```

Expected:

``` text
AI DevOps Platform is running
```

For the health endpoint:

``` powershell
(Invoke-WebRequest http://localhost:5000/health).StatusCode
```

Expected:

``` text
200
```

``` powershell
(Invoke-WebRequest http://localhost:5000/health).Content
```

Expected:

``` json
{"environment":"development","status":"healthy"}
```

## Runtime environment configuration

The container supports runtime environment overrides.

Example:

``` powershell
docker run --name ai-devops-platform-m2-env -p 5001:5000 -e APP_ENV=container-test ai-devops-platform:m2.10
```

This allows the container environment to override the default `APP_ENV`
without changing application source code.

## Docker HEALTHCHECK

The Dockerfile defines:

``` dockerfile
HEALTHCHECK --interval=30s --timeout=5s --start-period=5s --retries=3 CMD python -c "import urllib.request; urllib.request.urlopen('http://localhost:5000/health', timeout=3)"
```

Docker periodically requests the application's `/health` endpoint from
inside the container.

A successful check produces:

``` text
Health=healthy
```

The final M2 verification showed repeated health-check results with
`ExitCode=0` and:

``` text
FailingStreak=0
Status=healthy
```

## Failure and recovery testing

M2 also tested the container failure/recovery lifecycle.

The application/container was intentionally stopped and Docker reported:

``` text
exited | Health=unhealthy | ExitCode=137
```

The existing container was then started again:

``` powershell
docker start ai-devops-platform-m2
```

After recovery, the final state was:

``` text
running | Health=healthy | ExitCode=0
```

Both application endpoints returned HTTP `200` after recovery.

> **Important:** Docker `HEALTHCHECK` detects and reports health; it
> does not by itself provide the full orchestration and recovery
> behavior that will later be handled by Kubernetes.

# 17. Automated Testing

The project uses `pytest` for automated testing.

Make sure the virtual environment is active.

Run:

``` powershell
python -m pytest
```

Expected result:

``` text
1 passed
```

The current test verifies that:

-   The `/health` endpoint exists.
-   The endpoint returns HTTP status `200`.
-   The response reports the application as healthy.

------------------------------------------------------------------------

# 18. Pytest Configuration

The project contains:

``` text
pytest.ini
```

Current configuration:

``` ini
[pytest]
pythonpath = .
testpaths = tests
```

### Purpose

``` ini
pythonpath = .
```

Adds the project root to Python's import path so application modules can
be imported reliably during testing.

``` ini
testpaths = tests
```

Tells pytest to look for tests inside the `tests/` directory.

------------------------------------------------------------------------

# 19. Git Development Workflow

Development should be performed using feature branches.

Do not normally develop directly on `main`.

## Update local `main`

``` bash
git checkout main
git pull origin main
```

## Create a feature branch

``` bash
git checkout -b feature/<feature-name>
```

Example:

``` bash
git checkout -b feature/m1-documentation
```

## Check changes

``` bash
git status
```

## Stage changes

``` bash
git add .
```

## Commit changes

``` bash
git commit -m "feat: add project documentation"
```

## Push the feature branch

``` bash
git push -u origin feature/<feature-name>
```

## Create Pull Request

Create a Pull Request on GitHub:

``` text
feature/<feature-name>
        │
        ▼
      main
```

Changes should be reviewed and merged through the Pull Request workflow.

------------------------------------------------------------------------

# 20. Git Safety

The following should not be committed:

``` text
venv/
.env
__pycache__/
.pytest_cache/
*.pyc
```

The following should be committed:

``` text
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

------------------------------------------------------------------------

# 21. Important Environment Rules

### Rule 1 --- Use the project virtual environment

Before running Python-related commands, verify that the terminal is
using:

``` text
venv\Scripts\python.exe
```

### Rule 2 --- Install dependencies using `requirements.txt`

Use:

``` powershell
python -m pip install -r requirements.txt
```

### Rule 3 --- Update `requirements.txt`

Whenever a new Python dependency is intentionally added to the project,
update:

``` text
requirements.txt
```

so that another developer and future CI/CD environments can reproduce
the same dependency setup.

### Rule 4 --- Never commit `.env`

Use:

``` text
.env.example
```

for documenting required environment variables.

Keep actual local configuration in:

``` text
.env
```

### Rule 5 --- Run tests before committing

Use:

``` powershell
python -m pytest
```

A change should not be considered ready until the automated tests pass.

------------------------------------------------------------------------

# 22. Troubleshooting

## Python points to the wrong environment

Run:

``` powershell
python -c "import sys; print(sys.executable)"
```

If the output does not point to:

``` text
venv\Scripts\python.exe
```

activate the virtual environment:

``` powershell
.\venv\Scripts\Activate.ps1
```

------------------------------------------------------------------------

## Pytest cannot import the application

First make sure you are running pytest from the project root:

``` powershell
python -m pytest
```

Then verify that `pytest.ini` exists at the project root:

``` text
project-root/
└── pytest.ini
```

The configuration should contain:

``` ini
[pytest]
pythonpath = .
testpaths = tests
```

------------------------------------------------------------------------

## Flask is not installed

With the virtual environment activated:

``` powershell
python -m pip install -r requirements.txt
```

------------------------------------------------------------------------

## `.env` appears in Git status

Check `.gitignore` and make sure it contains:

``` text
.env
```

Then run:

``` powershell
git status
```

------------------------------------------------------------------------

# 23. Development Principles

The project will follow these principles throughout development:

### Reproducibility

The same project should be reproducible on different development and CI
environments.

### Automation

Manual repetitive DevOps tasks should progressively be automated.

### Testing

Changes should be validated through automated tests wherever practical.

### Observability

The deployed application should eventually expose useful health,
metrics, and logging information.

### Security

Secrets should not be stored in source code or committed to Git.

### Infrastructure as Code

Infrastructure and deployment configuration should eventually be
represented as version-controlled code.

### Continuous Improvement

The platform will be developed incrementally through milestones rather
than implementing the entire system at once.

------------------------------------------------------------------------

# 24. Project Roadmap

The project is planned to progress through the following stages.

## M0 --- GitHub Repository & Collaboration Setup

-   Repository creation
-   Repository configuration
-   Branch strategy
-   Collaboration setup
-   Git workflow

**Status: Completed**

------------------------------------------------------------------------

## M1 --- Project Foundation & Local Development Environment

-   Flask application
-   Health endpoint
-   Python virtual environment
-   Dependency management
-   Automated tests
-   Environment configuration
-   Documentation

**Status: Completed**

------------------------------------------------------------------------

## M2 --- Docker Containerization

**Status: Completed**

Completed work:

-   Verified Docker Desktop and Docker Engine.
-   Prepared the Flask application for containerization.
-   Created `.dockerignore`.
-   Created the Dockerfile.
-   Built the `ai-devops-platform:m2.10` image.
-   Ran the `ai-devops-platform-m2` container.
-   Verified host-to-container port mapping on port `5000`.
-   Tested `/` and `/health`.
-   Tested runtime environment variable override.
-   Added and verified Docker `HEALTHCHECK`.
-   Tested container failure and recovery.
-   Committed Docker changes through a feature branch.
-   Created and merged GitHub Pull Request #3 into `main`.
-   Performed final Docker and Git verification on `main`.

------------------------------------------------------------------------

## M3 --- Jenkins CI/CD

Planned work:

-   Jenkins installation/configuration
-   Source-code integration
-   Automated testing
-   Docker image building
-   Pipeline automation
-   Build failure handling
-   Reproducible CI/CD execution for the current reference application
-   Pipeline design that can later be reused for other supported
    application workloads

The current Flask application will continue to be used during M3. The
objective is to establish a reusable CI/CD foundation rather than
tightly coupling Jenkins to Flask-specific behavior.

------------------------------------------------------------------------

## M4 --- Infrastructure Automation

Planned work:

-   Infrastructure definition
-   Terraform configuration
-   Ansible configuration where appropriate
-   Automated environment setup
-   Separation of application configuration from platform infrastructure

------------------------------------------------------------------------

## M5 --- Kubernetes Deployment

Planned work:

-   Kubernetes cluster setup
-   Deployment manifests
-   Services
-   ConfigMaps
-   Secrets
-   Health probes
-   Scaling
-   Rolling deployments

------------------------------------------------------------------------

## M6 --- Monitoring & Observability

Planned work:

-   Prometheus
-   Grafana
-   Application metrics
-   Infrastructure metrics
-   Dashboards
-   Alerts
-   Log collection

------------------------------------------------------------------------

## M7 --- AI-Powered DevOps Analysis

Planned work:

-   Collect application and infrastructure information
-   Detect abnormal behavior
-   Analyze logs and metrics
-   Identify possible root causes
-   Generate troubleshooting recommendations
-   Provide intelligent DevOps assistance
-   Explore AI-assisted application/framework/configuration detection
-   Explore generation or validation of deployment configuration from
    detected application characteristics

AI-generated deployment configuration will be treated as an assisted
capability and validated before being used in deployment.

------------------------------------------------------------------------

## M8 --- Failure Simulation & Recovery

Planned work:

-   Introduce controlled application failures
-   Simulate deployment failures
-   Simulate configuration problems
-   Simulate resource problems
-   Detect failures
-   Analyze failures using the AI layer
-   Validate recovery procedures

------------------------------------------------------------------------

## M9 --- Integration & Final Validation

Planned work:

-   Integrate all major components
-   End-to-end CI/CD validation
-   Monitoring validation
-   AI analysis validation
-   Failure-recovery testing
-   Performance evaluation
-   Security review
-   Final documentation
-   Demonstrate the platform with the final reference application
-   Where practical, demonstrate reuse with at least one additional
    application type/workload

------------------------------------------------------------------------

# 25. Final Project Goal

The final goal is to create a reusable AI-assisted DevOps platform where
a supported application can progress through an automated DevOps
lifecycle:

``` text
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

The objective is not simply to create a deployment pipeline for one
Flask application.

The project aims to demonstrate how **application-agnostic DevOps
automation, observability, and AI-assisted troubleshooting can work
together to reduce the time and effort required to build, deploy,
monitor, diagnose, and recover supported applications.**

The current Flask application is therefore a **reference workload for
developing and validating the platform**, while the final showcase
should demonstrate the platform concept rather than making Flask itself
the central product.

------------------------------------------------------------------------

# 26. Current Milestone Verification

M0, M1, and M2 have been completed. The following checks have been
verified during development:

``` text
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

``` text
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

------------------------------------------------------------------------

# 27. Milestone Summary

``` text
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

The project is currently ready to proceed from the completed Docker
foundation into the planned CI/CD stage.

The next milestones should continue to use the current Flask reference
workload while keeping the CI/CD and deployment design sufficiently
modular to support additional application types later.

# 28. Architecture Decision Notes

These decisions should be treated as the current project direction
unless a later milestone explicitly revises them.

### Decision 1 --- Current application

Keep the existing Flask application as the reference workload through
the current CI/CD foundation.

### Decision 2 --- Final application

The final showcase may evolve the reference workload into a more
realistic small application/dashboard with an API, database,
health/metrics endpoints, and other features that strengthen the
demonstration.

### Decision 3 --- Framework

Flask remains the current framework. FastAPI is a possible future choice
if the final application becomes strongly API-oriented. A framework
migration is not required merely for modernization.

### Decision 4 --- Platform scope

The platform should be designed around a reusable deployment workflow
rather than around Flask-specific assumptions.

### Decision 5 --- Application portability

Docker is the primary standardization boundary. Applications that can
satisfy the platform's deployment contract can potentially use the same
CI/CD, containerization, infrastructure, Kubernetes, monitoring, and
AI-analysis layers.

### Decision 6 --- AI application onboarding

AI-assisted detection of application language, framework, dependencies,
ports, health checks, and deployment requirements is a future
enhancement. It should not be treated as already implemented.

### Decision 7 --- Final demonstration

The strongest final demonstration should show:

``` text
Application
    ↓
GitHub
    ↓
Jenkins
    ↓
Test
    ↓
Docker
    ↓
Kubernetes
    ↓
Monitoring
    ↓
Failure Simulation
    ↓
AI Analysis
    ↓
Root Cause / Recommendations
    ↓
Recovery
```

Where feasible, the final showcase should also demonstrate that the
platform can handle more than one application workload.

## License

This project is developed as an academic final-year project.
