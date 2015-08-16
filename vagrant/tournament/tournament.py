#!/usr/bin/env python
# 
# tournament.py -- implementation of a Swiss-system tournament
#

import psycopg2
import bleach


def connect():
    """Connect to the PostgreSQL database.  Returns a database connection."""
    return psycopg2.connect("dbname=tournament")


def deleteMatches():
    """Remove all the match records from the database."""
    conn = connect()
    curs = conn.cursor()
    curs.execute("DELETE FROM matches;")
    conn.commit()
    conn.close()


def deletePlayers():
    """Remove all the player records from the database."""
    conn = connect()
    curs = conn.cursor()
    curs.execute("DELETE FROM players;")
    conn.commit()
    conn.close()


def countPlayers():
    """Returns the number of players currently registered."""
    conn = connect()
    curs = conn.cursor()
    curs.execute("SELECT COUNT(*) FROM players;")
    record = curs.fetchall()[0]
    number = str(record[0])
    conn.close()
    return number


def registerPlayer(name):
    """Adds a player to the tournament database.
  
    The database assigns a unique serial id number for the player.  (This
    should be handled by your SQL database schema, not in your Python code.)
  
    Args:
      name: the player's full name (need not be unique).
    """
    conn = connect()
    curs = conn.cursor()
    cleaned = bleach.clean(name)
    curs.execute("INSERT INTO players (name) VALUES (%s)" , (cleaned,))
    conn.commit()
    conn.close()


def playerStandings():
    """Returns a list of the players and their win records, sorted by wins.

    The first entry in the list should be the player in first place, or a player
    tied for first place if there is currently a tie.

    Returns:
      A list of tuples, each of which contains (id, name, wins, matches):
        id: the player's unique id (assigned by the database)
        name: the player's full name (as registered)
        wins: the number of matches the player has won
        matches: the number of matches the player has played
    """
    conn = connect()
    curs = conn.cursor()
    curs.execute("SELECT tot_matches.id, name, wins, total FROM wins " +
                 "INNER JOIN tot_matches ON tot_matches.id = wins.id " +
                 "INNER JOIN players ON tot_matches.id = players.id;")
    standings = ({'id': str(row[0]), 'name': str(row[1]), 'wins': str(row[2]),
                  'total': str(row[3])} for row in curs.fetchall())
    conn.close()
    return standings

def reportMatch(winner, loser):
    """Records the outcome of a single match between two players.

    Args:
      winner:  the id number of the player who won
      loser:  the id number of the player who lost
    """
    conn = connect()
    curs = conn.cursor()
    curs.execute("INSERT INTO matches (winner, loser) VALUES (%s,%s)" , (winner,loser))
    conn.commit()
    conn.close()
 
 
def swissPairings():
    """Returns a list of pairs of players for the next round of a match.
  
    Assuming that there are an even number of players registered, each player
    appears exactly once in the pairings.  Each player is paired with another
    player with an equal or nearly-equal win record, that is, a player adjacent
    to him or her in the standings.
  
    Returns:
      A list of tuples, each of which contains (id1, name1, id2, name2)
        id1: the first player's unique id
        name1: the first player's name
        id2: the second player's unique id
        name2: the second player's name
    """

record = playerStandings()
for line in record:
    print line