-- キャラクターテーブル

CREATE TABLE IF NOT EXISTS characters (
    id SERIAL PRIMARY KEY,
    name VARCHAR(100) UNIQUE NOT NULL,
    attribute VARCHAR(50) NOT NULL,
    rarity VARCHAR(50) NOT NULL
);

CREATE INDEX IF NOT EXISTS idx_character_name
ON characters(name);