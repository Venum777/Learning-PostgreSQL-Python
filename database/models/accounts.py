# Local
from database.core import Connection
from database.models.users import User


class Account:

    id: int
    number: str
    owner_id: int
    balance: float
    type: str

    @staticmethod
    def create(
        conn: Connection,
        number: str,
        owner: User,
        balance: float,
        type: str
    ):
        with conn.cursor() as cur:
            cur.execute(f"""
                INSERT INTO accounts(
                    number,
                    owner_id,
                    balance,
                    type
                )
                VALUES(
                    '{number}',
                    {owner.id},
                    {balance},
                    '{type}'
                )
                """
            )