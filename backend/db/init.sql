DO
$$
BEGIN
    IF NOT EXISTS (SELECT 1 FROM pg_database WHERE datname = 'auth_db') THEN
        CREATE DATABASE auth_db;
    END IF;
END
$$;

DO
$$
BEGIN
    IF NOT EXISTS (SELECT 1 FROM pg_roles WHERE rolname = 'myuser') THEN
        CREATE USER myuser WITH ENCRYPTED PASSWORD 'mypassword';
        GRANT ALL PRIVILEGES ON DATABASE auth_db TO myuser;
    END IF;
END
$$;

\c auth_db;

CREATE TABLE IF NOT EXISTS users (
    id SERIAL PRIMARY KEY, 
    username VARCHAR(255) UNIQUE NOT NULL,
    hashed_password TEXT NOT NULL
);

