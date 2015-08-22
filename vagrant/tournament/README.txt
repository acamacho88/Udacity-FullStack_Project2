Alex Camacho - 8/22/15

This is for PROJECT 2 of the Udacity Full Stack Nanodegree

The tournament system can be operated first by downloading the files in this
repository into a folder, then creating the tournament database in postgresql
by activating postgresql in the command prompt with:

psql

then create the database with the command

CREATE DATABASE tournament;

After creating the databse, the necessary tables and views can be instantiated
by importing the tournament.sql file with the command

\i tournament.sql

After this has been done, exit out of psql with the command

\q

The tournament can be tested by running the python file tournament_test.py
with the command

python tournament_test.py

The program will run through each of its tests.

The python file tournament.py and the SQL file tournament.sql have been
commented, I added a "Camacho" at the beginning of each one so they can be
easily searched.