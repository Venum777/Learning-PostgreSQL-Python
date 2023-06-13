# Python
from decouple import config
import datetime
# Local
from database.core import Connection
from database.models.users import User
from database.models.cards import Card
from database.models.accounts import Account


my_connection: Connection = Connection(
    host=config('DB_HOST', str),
    port=config('DB_PORT', int),
    user=config('DB_USER', str),
    password=config('DB_PASSWORD', str),
    dbname=config('DB_NAME', str)
)
if __name__ == '__main__':
    my_connection.create_tables()
    # print(User.get(conn=my_connection.conn, first_name='Bob'))
    # print(User.filter(conn=my_connection.conn, first_name='Bob'))
    # print(User.get_all(conn=my_connection.conn))