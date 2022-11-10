import sys
import mysql.connector
from mysql.connector import errorcode

def main():
    
    answer = ""
    while(answer != "c"):
        print("1 for station or 2 for line or c to quit")
        answer = input()
        if answer == "1":
            ask_station()
        if answer == "2":
            ask_line()
    

def connection():
    try:
        return mysql.connector.connect(user = "sully", password = "",
                                       host = "127.0.0.1", database="vaticle")
    except mysql.connector.Error as err:
        if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
            print("Something is wrong with your user name or password")
        elif err.errno == errorcode.ER_BAD_DB_ERROR:
            print("Database does not exist")
        else:
            print(err)
    else:
        mydb.close()

        
def ask_station():
    answer = ""
    
    while (answer == ""):
        print("Which station ?")
        answer = input()
        print()
        
    cnx = connection()

    query = ('SELECT lineName FROM line INNER JOIN connection ON connection.idLine = line.idLine WHERE idStation = (SELECT idStation FROM station WHERE stationName = "' + answer + '" LIMIT 1);')

    cursor = cnx.cursor()
    cursor.execute(query)

    for StationName in cursor:
        print (StationName[0])

    print()
    cnx.close()
    

def ask_line():
    answer = ""
    
    while (answer == ""):
        print("Which line ?")
        answer = input()
        print()
        
    cnx = connection()
    
    query = ('SELECT stationName FROM station INNER JOIN connection ON connection.idStation = station.idStation WHERE idLine = (SELECT idLine FROM line WHERE lineName = "' + answer + '" LIMIT 1);')

    cursor = cnx.cursor()
    cursor.execute(query)

    for lineName in cursor:
        print (lineName[0])

    print()
    cnx.close()



    
if __name__ == '__main__':
   main()
