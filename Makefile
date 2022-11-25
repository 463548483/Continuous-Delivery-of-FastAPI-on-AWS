install:
	pip install --upgrade pip &&\
		pip install -r requirements.txt

test:
	python -m pytest -vv test_*.py

format:
	black *.py 

deploy:
	aws ecr get-login-password --region us-east-1 | docker login --username AWS --password-stdin 216514549505.dkr.ecr.us-east-1.amazonaws.com
	docker build -t proj2 .
	docker tag proj2:latest 216514549505.dkr.ecr.us-east-1.amazonaws.com/proj2:proj4
	docker push 216514549505.dkr.ecr.us-east-1.amazonaws.com/proj2:proj4

all: install format test deploy