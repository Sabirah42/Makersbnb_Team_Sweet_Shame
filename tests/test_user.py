from lib.user import User 

def test_initiate_user():
    user = User(1, 'bob', 'bob@mail.com', 'password')
    assert user.id == 1
    assert user.username == 'bob'
    assert user.email == 'bob@mail.com'
    assert user.password == 'password' 
