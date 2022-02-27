import mysql.connector
from mysql.connector import errorcode

""" database config object """
config = {
    "user": "root",
    "password": "ClipperTeaHabitatBlue",
    "host": "localhost",
    "database": "pysports",
    "raise_on_warnings": True
}


#Code block for insert operation
try:
    """ try/catch block for handling potential MySQL database errors """ 

    db = mysql.connector.connect(**config)
    
    cursor = db.cursor()

    cursor.execute("INSERT INTO player (first_name, last_name, team_id) VALUES('Smeagol', 'Shire Folk', 1);")

    cursor.execute("SELECT player_id, first_name, last_name, team_name FROM player INNER JOIN team ON player.team_id = team.team_id")

    players = cursor.fetchall()
    print ("\n  -- DISPLAYING PLAYERS AFTER INSERT --")

    for player in players:
        print("\nPlayer ID: ", player[0],
        "\nFirst Name: ", player[1],
        "\nLast Name: ", player[2],
        "\nTeam Name:", player[3])

    cursor.execute("UPDATE player SET team_id = 2, first_name = 'Gollum', last_name = 'Ring Stealer' WHERE first_name = 'Smeagol';")

    cursor.execute("SELECT player_id, first_name, last_name, team_name FROM player INNER JOIN team ON player.team_id = team.team_id")

    players = cursor.fetchall()
    print ("\n  -- DISPLAYING PLAYERS AFTER UPDATE --")

    for player in players:
        print("\nPlayer ID: ", player[0],
        "\nFirst Name: ", player[1],
        "\nLast Name: ", player[2],
        "\nTeam Name:", player[3])

    cursor.execute("DELETE FROM player WHERE first_name = 'Gollum'")

    cursor.execute("SELECT player_id, first_name, last_name, team_name FROM player INNER JOIN team ON player.team_id = team.team_id")

    players = cursor.fetchall()
    print ("\n  -- DISPLAYING PLAYERS AFTER DELETION --")

    for player in players:
        print("\nPlayer ID: ", player[0],
        "\nFirst Name: ", player[1],
        "\nLast Name: ", player[2],
        "\nTeam Name:", player[3])

except mysql.connector.Error as err:
    """ on error code """

    if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
        print("  The supplied username or password are invalid")

    elif err.errno == errorcode.ER_BAD_DB_ERROR:
        print("  The specified database does not exist")

    else:
        print(err)

#Code block for update operation
try:
    """ try/catch block for handling potential MySQL database errors """ 

    db = mysql.connector.connect(**config)
    
    cursor = db.cursor()

    cursor.execute("UPDATE player SET team_id = 2, first_name = 'Gollum', last_name = 'Ring Stealer' WHERE first_name = 'Smeagol';")

    cursor.execute("SELECT player_id, first_name, last_name, team_name FROM player INNER JOIN team ON player.team_id = team.team_id")

    players = cursor.fetchall()
    print ("\n  -- DISPLAYING PLAYERS AFTER UPDATE --")

    for player in players:
        print("\nPlayer ID: ", player[0],
        "\nFirst Name: ", player[1],
        "\nLast Name: ", player[2],
        "\nTeam Name:", player[3])

except mysql.connector.Error as err:
    """ on error code """

    if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
        print("  The supplied username or password are invalid")

    elif err.errno == errorcode.ER_BAD_DB_ERROR:
        print("  The specified database does not exist")

    else:
        print(err)



finally:
    """ close the connection to MySQL """
    db = mysql.connector.connect(**config)
    db.close()