-- Table definitions for the tournament project.
--
-- Put your SQL 'create table' statements in this file; also 'create view'
-- statements if you choose to use it.
--
-- You can write comments in this file by starting them with two dashes, like
-- these lines here.

-- Camacho: Main players table created, all that's needed is a unique ID
-- and the player's name

CREATE TABLE players (id serial primary key, name text);

-- Camacho: Table to store records of the matches.  The winner/loser IDs
-- must match what's in the players table, hence the references back to
-- the players table

CREATE TABLE matches (match_id serial, winner integer references players (id),
                      loser integer references players (id));

-- Camacho: Created useful views that could be referenced when needed, for
-- wins, losses, and the total number of matches
-- Used Right Joins in case the player had no wins/losses/matches

CREATE VIEW wins as SELECT id, COUNT(winner) wins FROM matches
RIGHT JOIN players ON winner = id
GROUP BY id;

CREATE VIEW losses as SELECT id, COUNT(loser) losses FROM matches
RIGHT JOIN players ON loser = id
GROUP BY id;

CREATE VIEW tot_matches as SELECT id, COUNT(winner) total FROM matches
RIGHT JOIN players ON id = winner OR id = loser
GROUP BY id;