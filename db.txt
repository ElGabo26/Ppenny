from mysql.connector import connection
from config import env


variables = env()


def connectionDB():
    db = connection.MySQLConnection(
        host=variables["DB_HOST"], user=variables["DB_USER"], passwd=variables["DB_PASS"], database=variables["DB_DATABASE"])
    if db:
        print("DB connection established")
    else:
        print("No connection established")
    return db
