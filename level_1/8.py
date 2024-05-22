import decimal
import uuid

from constants import ___


def get_user_balance(user_id: uuid.UUID) -> decimal.Decimal:
    pass
    reveal_type(user_id)
    reveal_type(get_user_balance)
    


if __name__ == "__main__":
    assert get_user_balance(user_id=uuid.uuid4()) == decimal.Decimal("265.2")
