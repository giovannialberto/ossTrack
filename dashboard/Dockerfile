# Use the official Python image as base
FROM python:3.9-slim-buster

# Set the working directory inside the container
WORKDIR /app

# Copy the requirements file to the container
COPY requirements.txt .

# Install the Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the Dash app to the container
COPY app.py .

# Expose the port where the Flask app will run
EXPOSE 8050

# Start the Flask app when the container starts
CMD ["python", "app.py", "--database-url", "data/github_metrics.db"]