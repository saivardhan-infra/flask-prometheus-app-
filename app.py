from flask import Flask, Response
from prometheus_client import Counter, Histogram, generate_latest, CONTENT_TYPE_LATEST
import time
import random

app = Flask(__name__)

# Metrics
REQUEST_COUNT = Counter('http_requests_total', 'Total HTTP Requests')
REQUEST_LATENCY = Histogram('http_request_duration_seconds', 'Request latency')

@app.route("/")
def home():
    REQUEST_COUNT.inc()
    
    start_time = time.time()
    time.sleep(random.uniform(0.1, 0.5))  # simulate delay
    REQUEST_LATENCY.observe(time.time() - start_time)

    return "Hello DevOps 🚀"

@app.route("/metrics")
def metrics():
    return Response(generate_latest(), media_type=CONTENT_TYPE_LATEST)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
