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

An example of running the script with a token speed of 400 tokens per second and streaming the output:

```bash
python token_speed_test.py 400 true
```

An example of running the script with a token speed of 100 tokens per second and not streaming the output:

```bash
python token_speed_test.py 100 false
```
