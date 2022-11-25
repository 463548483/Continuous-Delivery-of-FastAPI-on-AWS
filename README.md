# FastAPI

![example workflow](https://github.com/nogibjj/Zijing-codespcase/actions/workflows/main.yml/badge.svg)

This is Zijing's project 4 repo, which contains a big data script that use Databricks API and Streamlit app to show word cloud for job salary analysis. 

Dataset: https://www.kaggle.com/code/raghurayirath/plotly-data-science-job-salary-dataset-eda/data

## Project Structure
![image](https://github.com/463548483/Zijing-proj4/blob/main/proj4.png)

## Build FastAPI
root("/") page: show welcome information
predict("/predict/") page: predict api for GaussianNB towards iris dataset

## Containerzed FastAPI
`docker build .`
`docker image ls`
`docker run -p 127.0.0.1:8080:8080  9436eaf1859b`

## Push to ECR
Retrieve an authentication token and authenticate Docker client to registry
`aws ecr get-login-password --region us-east-1 | docker login --username AWS --password-stdin 216514549505.dkr.ecr.us-east-1.amazonaws.com`

Build Docker image
`docker build -t proj2 .`

Tag image:
`docker tag proj2:proj4 216514549505.dkr.ecr.us-east-1.amazonaws.com/proj2:proj4`

Run the following command to push this image to your newly created AWS repository:
`docker push 216514549505.dkr.ecr.us-east-1.amazonaws.com/proj2:proj4`

## Continuely Deployment
`make all` or git push to github will trigger the re-deployment of api
