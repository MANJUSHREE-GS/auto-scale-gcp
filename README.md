# Auto Scaling from Local VM to GCP

## Overview
This project demonstrates auto-scaling from a local VM to a cloud VM using Google Cloud Platform when CPU usage exceeds 75%.

## Architecture
(Local VM → Monitoring → Threshold → Cloud VM → Deployment)

## Steps
1. Monitor CPU using psutil
2. Trigger GCP VM using gcloud CLI
3. Deploy Flask app on cloud VM

## Technologies Used
- Python
- GCP Compute Engine
- Flask
- psutil

## Output
Auto-scaled successfully to Cloud VM!