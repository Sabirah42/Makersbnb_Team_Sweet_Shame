from lib.user import User
from lib.user_repository import UserRepository 

def test_create_new_user_returns_id(db_connection):
    db_connection.connect()
    db_connection.seed('seeds/bnb_tables.sql')
    repo = UserRepository(db_connection)
    user = User(None, 'Kate', 'kate@mail.com', 'password1')
    result = repo.create(user)
    assert result == 5


def test_get_user_name_for_id(db_connection):
    db_connection.connect()
    db_connection.seed('seeds/bnb_tables.sql')
    repo = UserRepository(db_connection)
    result = repo.get_username_from_id(1)
    assert result == 'Liam'

def test_get_id_from_email(db_connection):
    db_connection.connect()
    db_connection.seed('seeds/bnb_tables.sql')
    repo = UserRepository(db_connection)
    result = repo.get_user_id_from_email('liam@shame.com')
    assert result == 1