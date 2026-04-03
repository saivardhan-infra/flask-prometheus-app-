# Flask App with Prometheus Metrics

This is a simple Flask application where I added Prometheus monitoring.
The goal of this project is to understand how real applications expose metrics and how tools like Prometheus can collect them.

---

## What I did in this project

* Built a basic Flask app
* Added a `/metrics` endpoint using Prometheus
* Tracked request count and response time
* Dockerized the application

---

## Why I built this

I wanted to learn how monitoring works in real systems.
Instead of just theory, I tried adding metrics to an actual app and running it in Docker.

---

## How to run locally

```bash
pip install -r requirements.txt
python app.py
```

---

## Run using Docker

```bash
docker build -t flask-prometheus .
docker run -p 5000:5000 flask-prometheus
```

---

## Endpoints

* `/` → returns a simple response
* `/metrics` → shows Prometheus metrics

---

## What I learned

* How to expose metrics from an application
* Basics of Prometheus metrics (counter, histogram)
* How Docker helps in running apps easily

---

## Next steps

* Connect this app to Prometheus
* Visualize metrics in Grafana
* Add alerts

---

This is part of my DevOps learning journey.
