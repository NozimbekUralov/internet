import json, mysql.connector
import socket

connection = mysql.connector.connect(
    host="localhost",
    user="root",
    password="password",
)

cursor = connection.cursor()

def create_database():
    cursor.execute("CREATE DATABASE IF NOT EXISTS Internet")
    cursor.execute("USE Internet")
    cursor.execute(
        """CREATE TABLE IF NOT EXISTS domain (
        id INT AUTO_INCREMENT PRIMARY KEY,
        domain VARCHAR(255),
        ip VARCHAR(255))"""
        )
    
def insert_data(domain, ip):
    cursor.execute(
        "INSERT INTO domain (domain, ip) VALUES (%s, %s)",
        (domain, ip),
    )
    connection.commit()

def main():
    create_database()

    with open("domains.txt", "r") as file:
        for line in file:
            domain = line.strip()
            ip = socket.gethostbyname(domain)
            insert_data(domain, ip)

    cursor.close()
    connection.close()

if __name__ == "__main__":
    main()

