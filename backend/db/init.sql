--AUTHENTICATION
-- DO
-- $$
-- BEGIN
--     IF NOT EXISTS (SELECT 1 FROM pg_database WHERE datname = 'auth_db') THEN
--         CREATE DATABASE auth_db;
--     END IF;
-- END
-- $$;

-- DO
-- $$
-- BEGIN
--     IF NOT EXISTS (SELECT 1 FROM pg_roles WHERE rolname = 'myuser') THEN
--         CREATE USER myuser WITH ENCRYPTED PASSWORD 'mypassword';
--         GRANT ALL PRIVILEGES ON DATABASE auth_db TO myuser;
--     END IF;
-- END
-- $$;

-- \c auth_db;

-- CREATE TABLE IF NOT EXISTS users (
--     id SERIAL PRIMARY KEY, 
--     username VARCHAR(255) UNIQUE NOT NULL,
--     hashed_password TEXT NOT NULL
-- );




--FOOD DATA
-- DO
-- $$
-- BEGIN
--     IF NOT EXISTS (SELECT 1 FROM pg_database WHERE datname = 'food_db') THEN
--         CREATE DATABASE food_db;
--     END IF;
-- END
-- $$;

-- DO
-- $$
-- BEGIN
--     IF NOT EXISTS (SELECT 1 FROM pg_roles WHERE rolname = 'myuser') THEN
--         CREATE USER myuser WITH ENCRYPTED PASSWORD 'mypassword';
--         GRANT ALL PRIVILEGES ON DATABASE food_db TO myuser;
--     END IF;
-- END
-- $$;

-- \c food_db;

-- CREATE TABLE IF NOT EXISTS food_info (
--     label VARCHAR(255),
--     calories INT,
--     protein INT,
--     carbohydrates INT,
--     fats INT,
--     fiber INT,
--     sugars INT,
--     sodium INT
-- );




--FOOD POSTS
-- CREATE TABLE users (
--     id SERIAL PRIMARY KEY,
--     username VARCHAR(100) UNIQUE NOT NULL,
--     email VARCHAR(100) UNIQUE NOT NULL,
--     password_hash VARCHAR(255) NOT NULL,
--     created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
-- );

-- CREATE TABLE posts (
--     id SERIAL PRIMARY KEY,
--     user_id INTEGER REFERENCES users(id) ON DELETE CASCADE,
--     image_url TEXT,
--     description TEXT,
--     created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
-- );

-- CREATE TABLE comments (
--     id SERIAL PRIMARY KEY,
--     post_id INTEGER REFERENCES posts(id) ON DELETE CASCADE,
--     user_id INTEGER REFERENCES users(id) ON DELETE CASCADE,
--     content TEXT,
--     created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
-- );

-- CREATE TABLE likes (
--     id SERIAL PRIMARY KEY,
--     post_id INTEGER REFERENCES posts(id) ON DELETE CASCADE,
--     user_id INTEGER REFERENCES users(id) ON DELETE CASCADE,
--     created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
-- );

-- CREATE TABLE tags (
--     id SERIAL PRIMARY KEY,
--     name VARCHAR(50) UNIQUE NOT NULL
-- );

-- CREATE TABLE post_tags (
--     post_id INTEGER REFERENCES posts(id) ON DELETE CASCADE,
--     tag_id INTEGER REFERENCES tags(id) ON DELETE CASCADE
-- );
