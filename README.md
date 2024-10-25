# codecrusaders bayhackathon
Hackathon repositoyr

#Build and Push the Docker Image to Google Container Registry

## Authenticate Docker with GCP
gcloud auth configure-docker

## Build the Docker image
docker build -t gcr.io/your-project-id/image-processor .

## Push the Docker image to Google Container Registry
docker push gcr.io/your-project-id/image-processor

Used Artifactory Registry instead of Google Container Registry

# Google Cloud Run
https://console.cloud.google/run/detail/europe-west4/ch4restapi/metrics?csesidx=1978676054&project=pbeat03002010-prod-2afb-cc-def