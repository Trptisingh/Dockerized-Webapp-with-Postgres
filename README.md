

#  STEP 1 — Prerequisites

Ensure Docker is installed:

```sh
sudo apt install docker.io -y
sudo apt install docker-compose -y
```

Verify installation:

```sh
docker --version
```

If Docker prints a version → you're good.

---

#  STEP 2 — Create Project Folder

```sh
mkdir docker-demo
cd docker-demo
```

This folder will contain:

```
app.py
requirements.txt
Dockerfile
docker-compose.yml
```

(You will place these files manually — contents are explained inside the project.)

---

#  STEP 3 — Create the Flask Web App

Inside `docker-demo`, create your application file.
The app will:

* Start a Flask web server
* Connect to PostgreSQL using container hostname (`db`)
* Show the database version in the browser

This demonstrates container networking.

---

#  STEP 4 — Create requirements.txt

Add Flask and PostgreSQL client library so Docker installs dependencies when building the image.

---

# STEP 5 — Create Dockerfile for Flask App

The Dockerfile will:

* Use a Python base image
* Copy the app files
* Install dependencies
* Start the Flask server

This file ensures consistent environments inside the container.

---

#  STEP 6 — Create docker-compose.yml

Your `docker-compose.yml` will define:

| Service     | Description                                |
| ----------- | ------------------------------------------ |
| **db**      | Runs PostgreSQL container                  |
| **web**     | Builds & runs the Flask container          |
| **db_data** | Docker volume for persistent DB storage    |
| **backend** | Docker network for container communication |

Important concepts used:

* **depends_on** → ensures DB starts before Flask
* **ports** → maps Flask app to host
* **volumes** → stores PostgreSQL data even if container is removed
* **networks** → secure, internal communication

---

#  STEP 7 — Build & Run Containers

Run everything with:

```sh
sudo docker-compose up -d --build
```

This command:

1. Builds the Flask Docker image
2. Creates a Docker network
3. Creates a Docker volume
4. Starts both containers

---

#  STEP 8 — Verify Containers, Volumes & Networks

### View running containers:

```sh
sudo docker ps
```

### View volumes:

```sh
sudo docker volume ls
```

### View networks:

```sh
sudo docker network ls
```

You will see:

* `web` → Flask app
* `db` → PostgreSQL
* `docker-demo_db_data` → persistent volume
* `docker-demo_backend` → internal network

---

# STEP 9 — Access the Application

Open your browser:

```
http://localhost:5000
```

You should see:

```
Connected to PostgreSQL!
Version: PostgreSQL 15.x ...
```

This confirms:

* Containers are running
* Flask app is working
* DB is reachable via Docker Network
* psycopg2 successfully queried PostgreSQL

---

#  STEP 10 — Test Persistence 

Stop all containers:

```sh
sudo docker compose down
```

Check if the volume still exists:

```sh
sudo docker volume ls
```

Restart everything:

```sh
sudo docker compose up -d
```

Your PostgreSQL data remains intact → **volume persistence is working**.

---

#  STEP 11 — Docker Internals (Behind the Scenes)

| Concept                     | Explained                                                     |
| --------------------------- | ------------------------------------------------------------- |
| **Docker Container**        | Isolated environment running the app & DB                     |
| **Docker Volume**           | Stores DB data under `/var/lib/docker/volumes/`               |
| **Docker Network (bridge)** | Virtual internal LAN for container-to-container communication |
| **DNS Resolution**          | `web` can reach `db` using hostname (no IP needed)            |
| **Port Mapping**            | `5000:5000` exposes the Flask app to host machine             |

Docker Compose automates:

* Network provisioning
* Volume lifecycle
* Container startup order
* Environment variables
* Service isolation

---

# 🎯 Final Outcome

You now have:

✔ 2 containers (Flask + PostgreSQL)
✔ 1 Docker network for communication
✔ 1 Docker volume for persistent DB storage
✔ Flask app successfully connecting to PostgreSQL
✔ Application accessible on `localhost:5000`
✔ Fully functional multi-container architecture
