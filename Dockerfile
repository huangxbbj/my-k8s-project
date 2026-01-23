# 1. Use an official lightweight Python image
FROM python:3.9-slim

# 2. Set the working directory inside the container
WORKDIR /app

# 3. Copy only the requirements file first 
# This leverages Docker cache so you don't re-install libs if code changes
COPY requirements.txt .

# 4. Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# 5. Copy the rest of your application code
COPY . .

# 6. Expose the port FastAPI will run on
EXPOSE 80

# 7. Command to run the application
# We use uvicorn to serve the FastAPI app defined in main.py
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "80"]
