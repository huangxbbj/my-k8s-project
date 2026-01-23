from fastapi import FastAPI
import os
import socket

app = FastAPI()

@app.get("/")
def read_root():
    # Returning the Hostname is a great way to see K8s load balancing in action
    # as you refresh, you'll see different Pod IDs.
    return {
        "message": "Hello from Kubernetes!",
        "hostname": socket.gethostname(),
        "version": "1.0.0"
    }

@app.get("/health")
def health_check():
    # Kubernetes uses this to ensure your app hasn't crashed
    return {"status": "healthy"}

if __name__ == "__main__":
    import uvicorn
    # Important: Bind to 0.0.0.0 so it's accessible outside the container
    uvicorn.run(app, host="0.0.0.0", port=80)
