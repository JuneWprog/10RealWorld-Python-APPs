# |************************************************|
# | //    A Simple English Dictionary  //          |
# |        using remote MySQL server.              |
# |                                                |
#  ************************************************|

from difflib import get_close_matches
import mysql.connector

#connect to remote database server

con=mysql.connector.connect(
    user="ardit700_student",
    password="ardit700_student",
    host='108.167.140.122',
    database='ardit700_pm1database'
)
cursor=con.cursor()

#retrieve all data from database
word=input("Enter a word: ")
query=cursor.execute("SELECT * FROM Dictionary WHERE Expression='%s'"%word)

results=cursor.fetchall()
if results:
    print(results)
    for i in range(len(results)):
        print(f"{i+1}. ",end=' ')
        print(results[i][1])

else:
    print("No translation found!")

