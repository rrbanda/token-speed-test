# token-speed-test

This is a simple test to simulate various token speeds for large language models. The goal is to measure the time it takes to generate a single token for a given model. This can be useful for understanding the performance characteristics of different models and for optimizing the performance of models in production.

[![Try with Replit](https://replit.com/badge?caption=Try%20with%20Replit)](https://replit.com/@HunterGerlach/token-speed-test)

## Usage

Setup your environment:

```bash
python3 -m venv venv
source venv/bin/activate
pip install --upgrade pip
```

Run the script:

```bash
python token_speed_test.py
```

Alternatively, you can run the script with specific arguments to set the token speed as well as whether or not the output is streamed:

An example of running the scr


## Build Image using Podman
 
```bash
podman build -t yourusername/generate-tokens-job .
```

Push the Image to a Container Registry:


```bash
docker push yourusername/generate-tokens-job
```

## Steps to Deploy the Job to a OpenShift Cluster

```bash
oc apply -f generate-tokens-job.yaml
```

## Check the Status of the Job:

oc get jobs

## View the Logs of the Job:

```bash
oc logs job/generate-tokens-job
```
