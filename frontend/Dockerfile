# Use NGINX to serve the static files
FROM nginx:alpine

# Set the working directory in the container
WORKDIR /app

# Copy FastAPI app files to the container
COPY . /usr/share/nginx/html

# Expose the default NGINX port
EXPOSE 80

# No need to define a CMD, as NGINX image has a default entrypoint to run the server
