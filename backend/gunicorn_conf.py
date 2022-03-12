import multiprocessing
import os


# bind
host = os.getenv("HOST", "0.0.0.0")  # host inside container
port = os.getenv("PORT", "80")  # port container should listen to
bind = f"{host}:{port}"

# workers (number of worker processes for handling requests)
cores = multiprocessing.cpu_count()
workers_per_core = os.getenv("WORKERS_PER_CORE", 1)
workers = int(cores * workers_per_core)

# graceful timeout (time for graceful workers restart)
graceful_timeout = os.getenv("GRACEFUL_TIMEOUT", 120)

# timeout (time for idle workers to be killed and restarted)
timeout = os.getenv("TIMEOUT", 120)

# keepalive (time to wait for requests on a keep-alive connection)
keepalive = os.getenv("KEEPALIVE", 5)
