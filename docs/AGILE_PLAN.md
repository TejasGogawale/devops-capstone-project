# Agile Planning — Customer Accounts Microservice

## GitHub Project columns
Create a GitHub Project board with these seven columns/statuses in this order:
1. New issues
2. Icebox
3. Product backlog
4. Sprint backlog
5. In progress
6. Review/QA
7. Done

Create each story below as an issue. Initially place all seven in **New issues**.

## Story 1: Set up the development environment
**As a** developer  
**I need** a working local development environment  
**So that** I can safely develop and test the customer accounts microservice.

### Details and assumptions
- Python and the existing Flask application are used.
- The existing account model and create-account endpoint are already provided.
- Dependencies and test commands should be documented.

### Acceptance criteria
- Given a fresh checkout, when I follow setup instructions, then I can install dependencies and run the application.
- Given the application is running, when I execute the documented test command, then the tests run and report results.
- Given required configuration is missing, when startup is attempted, then the application provides a clear configuration error.

**Suggested label:** technical debt · **Priority:** 1 · **Story points:** 3

## Story 2: Read an account from the service
**As a** service client  
**I need** to retrieve one account by its identifier  
**So that** I can view a customer's stored name and address.

### Details and assumptions
- Use the existing account data model.
- Return JSON and appropriate HTTP status codes.

### Acceptance criteria
- Given an existing account ID, when the client requests it, then the API returns account details with HTTP 200.
- Given an unknown account ID, when the client requests it, then the API returns HTTP 404.
- Given a valid request, then the response contains the account identifier, name, and address.

**Suggested label:** enhancement · **Priority:** 2 · **Story points:** 5

## Story 3: Update an account in the service
**As a** service client  
**I need** to update an existing customer's account details  
**So that** the stored name and address remain accurate.

### Details and assumptions
- Validate incoming fields.
- Do not silently create an account when the ID does not exist.

### Acceptance criteria
- Given an existing account and valid fields, when the client submits an update, then the account is updated and a success status is returned.
- Given an unknown account ID, when the client submits an update, then the API returns HTTP 404.
- Given invalid input, when the client submits an update, then the API returns a validation error and does not change stored data.

**Suggested label:** enhancement · **Priority:** 3 · **Story points:** 5

## Story 4: Delete an account from the service
**As a** service client  
**I need** to delete an account by its identifier  
**So that** obsolete customer records can be removed.

### Details and assumptions
- A successful delete must not leave the account retrievable.
- Unknown IDs must be handled consistently.

### Acceptance criteria
- Given an existing account ID, when the client deletes it, then the API returns a success status and the account is no longer retrievable.
- Given an unknown account ID, when the client requests deletion, then the API returns HTTP 404.
- Given a successful deletion, when the account is requested again, then the API returns HTTP 404.

**Suggested label:** enhancement · **Priority:** 4 · **Story points:** 5

## Story 5: List all accounts in the service
**As a** service client  
**I need** to list customer accounts  
**So that** I can view the accounts currently managed by the service.

### Details and assumptions
- Return a JSON collection.
- An empty database should return an empty collection rather than an error.

### Acceptance criteria
- Given accounts exist, when the client requests the collection, then the API returns accounts as JSON.
- Given no accounts exist, when the client requests the collection, then the API returns an empty collection with HTTP 200.
- Given a successful response, then each account contains its identifier, name, and address.

**Suggested label:** enhancement · **Priority:** 5 · **Story points:** 5

## Story 6: Containerize the microservice using Docker
**As a** developer  
**I need** a Docker image for the accounts microservice  
**So that** the application can run consistently across environments.

### Details and assumptions
- Planned for a later sprint.
- The image should not include secrets.

### Acceptance criteria
- Given the Dockerfile and dependencies, when I build the image, then the build completes successfully.
- Given a built image and valid configuration, when I run a container, then the service starts and responds to a health/API request.
- Given the repository, then build and run instructions are documented.

**Suggested label:** technical debt · **Initial triage:** Icebox · **Story points:** 8

## Story 7: Deploy the Docker image to Kubernetes
**As a** platform operator  
**I need** to deploy the accounts service to Kubernetes  
**So that** the service can be operated in a container orchestration environment.

### Details and assumptions
- Planned for a later sprint.
- Cluster credentials and secrets must not be committed to the repository.

### Acceptance criteria
- Given a reachable Kubernetes cluster and image, when deployment manifests are applied, then application pods become ready.
- Given a running deployment, when the service is exposed using the documented method, then an API request reaches the application.
- Given a deployment failure, then documented commands can be used to inspect pod and deployment status.

**Suggested label:** technical debt · **Initial triage:** Icebox · **Story points:** 8

## Backlog refinement
Move stories 1–5 from **New issues** to **Product backlog**. Move stories 6–7 to **Icebox**, as Docker and Kubernetes are planned for a few sprints later.

Suggested Product backlog order:
1. Set up the development environment
2. Read an account
3. Update an account
4. Delete an account
5. List all accounts

Create a repository label named `technical debt` with yellow color `#FBCA04`. Use `enhancement` for customer-visible functionality, reusing an existing label if present.

## Sprint planning
Create three one-week iterations named Sprint 1, Sprint 2, and Sprint 3. Use actual dates appropriate to the course schedule.

Story-point scale from the lab: 3 = S, 5 = M, 8 = L, 13 = XL.

Suggested Sprint 1 plan, preserving order:
1. Set up development environment — 3
2. Read an account — 5
3. Update an account — 5
4. Delete an account — 5
5. List all accounts — 5

The lab instructs you to close each current issue when moving it from Product backlog to Sprint backlog. Follow that instruction if required by the grader, although in normal production workflows issues are generally closed only after work is completed.

## Evidence screenshots
Capture actual screenshots from GitHub and save them using the lab's requested names:
- `planning-repository-done.png` — public repository and name
- `planning-storytemplate-done.png` — template path and contents
- `planning-userstories-done.png` — seven issues in New issues
- `planning-productbacklog-done.png` — triaged backlog and Icebox
- `planning-labels-done.png` — labels visible on board
- `planning-kanban-done.png` — Sprint backlog and final board

Do not use mock screenshots as evidence.
