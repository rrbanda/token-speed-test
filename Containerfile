# Use Red Hat Universal Base Image with Python runtime
FROM registry.access.redhat.com/ubi8/python-39

# Set the working directory in the container
WORKDIR /usr/src/app

# Copy the current directory contents into the container at /usr/src/app
COPY . .

# Install any needed packages specified in requirements.txt
# (Add a requirements.txt file if there are dependencies. For this script, it seems there are none)
# RUN pip install --no-cache-dir -r requirements.txt

# Run the script when the container launches
ENTRYPOINT ["python", "./token-speed-test.py"]
