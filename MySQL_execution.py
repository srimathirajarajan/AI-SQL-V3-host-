import mysql.connector 
conn = mysql.connector.connect(host="localhost",password='Srimathi@16',user='root')

if conn.is_connected():
    print("Connection established")