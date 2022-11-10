import mysql.connector
import json


mydb = mysql.connector.connect(
    host="localhost",
    user="sully",
    passwd="",
    database="vaticle"
)

mycursor = mydb.cursor()

with open('train-network.json', encoding="utf8") as json_file:
    data = json.load(json_file)

for current in data['stations']: 
    sqlArgument = '("'+ current["id"] +'", "' + current["name"] + '", ' + str(current["longitude"]) + ', ' + str(current["latitude"]) + ');'
    sqlFormula = 'INSERT INTO station (idStation, stationName, longitude, latitude) VALUES' + sqlArgument 
    print(sqlFormula)
    mycursor.execute(sqlFormula)

for current in data['lines']:
    sqlArgument = '("'+ current["name"] + '");'
    sqlFormula = 'INSERT INTO line (lineName) VALUES' + sqlArgument
    print(sqlFormula)
    mycursor.execute(sqlFormula)

for current in data['lines']:
    query = ('SELECT idLine FROM line WHERE lineName = "' + current["name"] +'"')
    cursor = mydb.cursor()
    idLine = 0
    cursor.execute(query)
    for currentId in cursor:
        idLine = currentId[0]

    for currentStation in current['stations']:
        sqlArgument = '("' + currentStation + '", "' + str(idLine) + '");';
        sqlFormula = 'INSERT INTO connection (idStation, idLine) VALUES' + sqlArgument
        print(sqlFormula)
        mycursor.execute(sqlFormula)
        
mydb.commit()
mydb.close()
