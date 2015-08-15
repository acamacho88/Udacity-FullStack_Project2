-- Table definitions for the tournament project.
--
-- Put your SQL 'create table' statements in this file; also 'create view'
-- statements if you choose to use it.
--
-- You can write comments in this file by starting them with two dashes, like
-- these lines here.


CREATE TABLE players (id serial primary key, name text);

CREATE TABLE matches (match_id serial, winner integer references players (id), loser integer references players (id));