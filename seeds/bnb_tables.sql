DROP TABLE IF EXISTS last_viewed_listings;
DROP TABLE IF EXISTS listings;
DROP SEQUENCE IF EXISTS listings_id_seq;
DROP TABLE IF EXISTS users;
DROP SEQUENCE IF EXISTS users_id_seq;

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


INSERT INTO users (username, email, password) VALUES ('Liam', 'liam@shame.com', 'password1');
INSERT INTO users (username, email, password) VALUES ('Sabirah', 'sabirah@shame.com', 'password1');
INSERT INTO users (username, email, password) VALUES ('Zoe', 'zoe@shame.com', 'password1');
INSERT INTO users (username, email, password) VALUES ('Joceline', 'joceline@shame.com', 'password1');


INSERT INTO listings (listing_name, description, bedrooms, price, user_id) VALUES ('Rose View House', 'A beautiful family home with a view of roses.', 5, 300, 1);
INSERT INTO listings (listing_name, description, bedrooms, price, user_id) VALUES ('Shame Cottage', 'A dank dungeon in the heart of Scarborough.', 1, 10000, 2);
INSERT INTO listings (listing_name, description, bedrooms, price, user_id) VALUES ('Zoe''s Basement', 'Ideal for Gremlins.', 1, 2, 3);
INSERT INTO listings (listing_name, description, bedrooms, price, user_id) VALUES ('Crimson Carnage Castle', 'A castle stained with the echoes of past crimson carnage and unsolved mysteries.', 8, 600, 4);
INSERT INTO listings (listing_name, description, bedrooms, price, user_id) VALUES ('Lurking Shadows Sanctuary', 'A foreboding sanctuary where lurking shadows conceal sinister secrets.', 4, 200, 5);
INSERT INTO listings (listing_name, description, bedrooms, price, user_id) VALUES ('Noose Knot Manor', 'A manor adorned with noose knots, each telling a tale of a macabre past.', 6, 400, 6);
INSERT INTO listings (listing_name, description, bedrooms, price, user_id) VALUES ('Dreadful Dismal Dwelling', 'A dwelling with a dreadful atmosphere, where dismal thoughts linger in the air.', 5, 250, 7);
INSERT INTO listings (listing_name, description, bedrooms, price, user_id) VALUES ('Sinister Slaughterhouse', 'A slaughterhouse with a sinister history, its walls whispering tales of unspeakable horrors.', 7, 500, 8);
INSERT INTO listings (listing_name, description, bedrooms, price, user_id) VALUES ('Gory Gallows Garden', 'A garden surrounding a gallows, where gory tales unfold beneath the moonlight.', 3, 300, 9);
INSERT INTO listings (listing_name, description, bedrooms, price, user_id) VALUES ('Malevolent Morgue Mansion', 'A mansion adjacent to a malevolent morgue, where the deceased may not rest in peace.', 4, 280, 10);
INSERT INTO listings (listing_name, description, bedrooms, price, user_id) VALUES ('Bloodstained Ballroom Bungalow', 'A bungalow with a bloodstained ballroom, haunted by the waltzing spirits of the past.', 6, 450, 11);
INSERT INTO listings (listing_name, description, bedrooms, price, user_id) VALUES ('Macabre Murder Mill', 'A mill with a macabre history, where the sound of grinding echoes the tales of unsolved murders.', 7, 380, 12);
INSERT INTO listings (listing_name, description, bedrooms, price, user_id) VALUES ('Chilling Crime Crypt', 'A crypt where chilling crimes were committed, leaving a lingering sense of unease.', 5, 320, 13);

