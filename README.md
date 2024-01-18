# FastAPI example

## Summary
Little example of the fastapi-based service with healthcheck and metrics (prometheus-based) endpoints.

## How to build
```
docker build --platform linux/amd64 -t fastapi-docker .
docker tag fastapi-docker <docker_repo_with_tag>
docker push <docker_repo_with_tag>
```