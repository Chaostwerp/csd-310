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

try:
    """ try/catch block for handling potential MySQL database errors """ 

    db = mysql.connector.connect(**config)
    
    cursor = db.cursor()

    cursor.execute("SELECT player_id, first_name, last_name, team_name FROM player INNER JOIN team ON player.team_id = team.team_id")

    players = cursor.fetchall()
    print ("\n  -- DISPLAYING PLAYER RECORDS --")

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