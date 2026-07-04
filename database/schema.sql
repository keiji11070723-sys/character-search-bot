CREATE TABLE IF NOT EXISTS characters (
    id SERIAL PRIMARY KEY,
    name TEXT UNIQUE NOT NULL,
    attribute TEXT NOT NULL,
    rarity TEXT NOT NULL
);