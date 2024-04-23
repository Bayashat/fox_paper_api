# Use the official Python image as a base image
FROM python:3.11-bullseye


# Set the working directory in the container
WORKDIR /app


# Copy the requirements file into the container
RUN pip install --upgrade pip
COPY requirements.txt .

# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application code into the container
COPY . .

COPY scripts/wait-for-it.sh /scripts/wait-for-it.sh
COPY scripts/entrypoint.sh /scripts/entrypoint.sh
RUN chmod +x /scripts/wait-for-it.sh /scripts/entrypoint.sh

ENTRYPOINT ["/scripts/entrypoint.sh"]

