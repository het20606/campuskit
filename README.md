# CampusKit

CampusKit is a small study shelf for keeping track of notes, practice tasks and revision items by subject. It is a Flask app with a simple interface.

## Run locally

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
pip install -r requirements.txt
python -m pytest -q
python app.py
```

Open http://127.0.0.1:5000.

## Docker

```bash
docker build -t campuskit:local .
docker run --rm -p 5000:5000 campuskit:local
```

## CI/CD pipeline

The Jenkinsfile defines these stages: checkout, test, Docker build, image push, deployment to Minikube, and verification.

Before running Jenkins:
1. Push this project to GitHub and configure a Pipeline job for the repository.
2. Make sure the Jenkins agent has Python, pip, Docker, kubectl and access to the target Kubernetes cluster.
3. Create a Jenkins username/password credential with ID `dockerhub-creds`.
4. Replace `YOUR_DOCKERHUB_USERNAME/campuskit` in the Jenkinsfile and `k8s/deployment.yaml` with the actual Docker Hub repository.
5. Run the pipeline, then edit a visible heading in `templates/index.html`, commit and push the change, and run the pipeline again to demonstrate the update.

## Scope

This version uses in-memory sample data, so added items reset when the application restarts. It is intended as a compact student project demonstration.
