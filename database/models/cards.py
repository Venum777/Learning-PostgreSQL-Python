# Python
import datetime
# Local
from database.core import Connection
from database.models.accounts import Account

class Card:

    id: int
    number: str
    cvv: int
    date_end: datetime.datetime
    account_id: Account
    is_active: bool
    pin: int

    @staticmethod
    def create(
        conn: Connection,
        number: str,
        cvv: str,
        date_end: datetime,
        account_id: int,
        is_active: bool,
        pin: str
    ):
        with conn.cursor() as cur:
            cur.execute(f"""
                INSERT INTO cards(
                    number,
                    account_id,
                    cvv,
                    date_end,
                    is_active,
                    pin
                )
                VALUES(
                    '{number}',
                    '{account_id}',
                    '{cvv}',
                    '{date_end}',
                    '{is_active}',
                    '{pin}'
                )
                """
            )




        