FROM postgres:latest

# Set environment variables for PostgreSQL
ENV POSTGRES_USER=myuser
ENV POSTGRES_PASSWORD=mypassword
ENV POSTGRES_DB=auth_db

# Copy init.sql to entrypoint
COPY init.sql /docker-entrypoint-initdb.d/