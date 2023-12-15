DROP TABLE IF EXISTS last_viewed_listings;
-- DROP TABLE IF EXISTS listings;
-- DROP SEQUENCE IF EXISTS listings_id_seq;
-- DROP TABLE IF EXISTS users;
-- DROP SEQUENCE IF EXISTS users_id_seq;

CREATE SEQUENCE IF NOT EXISTS users_id_seq;
CREATE TABLE users (
    id SERIAL PRIMARY KEY,
    username TEXT NOT NULL UNIQUE,
    email TEXT NOT NULL UNIQUE,
    password TEXT
);

CREATE SEQUENCE IF NOT EXISTS listings_id_seq;
CREATE TABLE listings (
    id SERIAL PRIMARY KEY,
    listing_name TEXT,
    description TEXT,
    bedrooms INTEGER,
    price NUMERIC(10, 2), 
    user_id INTEGER,
  CONSTRAINT fk_user foreign key(user_id) references users(id) on delete cascade
);

CREATE TABLE last_viewed_listings (
    user_id INTEGER UNIQUE,
    listing_id INTEGER,
    FOREIGN KEY (user_id) REFERENCES users(id) on delete cascade,
    FOREIGN KEY (listing_id) REFERENCES listings(id) on delete cascade
);



-- INSERT INTO users (username, email, password) VALUES ('Liam', 'liam@shame.com', 'password1');
-- INSERT INTO users (username, email, password) VALUES ('Sabirah', 'sabirah@shame.com', 'password1');
-- INSERT INTO users (username, email, password) VALUES ('Zoe', 'zoe@shame.com', 'password1');
-- INSERT INTO users (username, email, password) VALUES ('Joceline', 'joceline@shame.com', 'password1');


-- INSERT INTO listings (listing_name, description, bedrooms, price, user_id) VALUES ('Rose View House', 'A beautiful family home with a view of roses.', 5, 300, 1);
-- INSERT INTO listings (listing_name, description, bedrooms, price, user_id) VALUES ('Shame Cottage', 'A dank dungeon in the heart of York.', 1, 10000, 2);
-- INSERT INTO listings (listing_name, description, bedrooms, price, user_id) VALUES ('The Basement Of Zoe', 'Ideal for Gremlins.', 1, 2, 3);
