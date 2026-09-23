"""Create the MySQL database for Kutwal Dream Resort (XAMPP)."""
import MySQLdb

DB_NAME = 'kutwal_dream_resort'
HOST = '127.0.0.1'
USER = 'root'
PASSWORD = ''
PORT = 3306


def main():
    conn = MySQLdb.connect(host=HOST, user=USER, passwd=PASSWORD, port=PORT)
    cur = conn.cursor()
    cur.execute(
        f"CREATE DATABASE IF NOT EXISTS `{DB_NAME}` "
        "CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci"
    )
    conn.commit()
    cur.close()
    conn.close()
    print(f"Database '{DB_NAME}' is ready.")


if __name__ == '__main__':
    main()
