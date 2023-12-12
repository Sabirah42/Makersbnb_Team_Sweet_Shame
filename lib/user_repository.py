from lib.user import User


class UserRepository:
    def __init__(self, connection):
        self.connection = connection  

    def all(self):
        rows = self.connection.execute('SELECT * from users')
        users = []
        for row in rows:
            item = User(row["id"], row["username"], row["email"], row['password'])
            users.append(item)
        return users

    def create(self, user):
        rows = self.connection.execute('INSERT INTO users (username, email, password) VALUES (%s, %s, %s) RETURNING id', [
                                 user.username, user.email, user.password])
        return rows[0]['id']

    def get_username_from_id(self, user_id):
        rows = self.connection.execute('SELECT username FROM users WHERE id=%s', [user_id])
        return rows[0]['username']
    
    def get_user_id_from_email(self, email):
        rows = self.connection.execute('SELECT id FROM users WHERE email=%s', [email])
        return rows[0]['id']