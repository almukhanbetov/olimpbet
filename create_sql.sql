CREATE DATABASE sports_events;

CREATE TABLE events (
    id SERIAL PRIMARY KEY,
    event_name TEXT NOT NULL,
    event_link TEXT NOT NULL
);

