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
    
    def get_user_from_email(self, email):
        rows = self.connection.execute('SELECT * from users WHERE email=%s', [email])
        if len(rows) == 0:
            raise Exception('User not found')
        return User(rows[0]['id'], rows[0]['username'], rows[0]['email'], rows[0]['password'])
    
    def get_user_from_id(self, id):
        rows = self.connection.execute('SELECT * from users WHERE id=%s', [id])
        if len(rows) == 0:
            raise Exception('User not found')
        return User(rows[0]['id'], rows[0]['username'], rows[0]['email'], rows[0]['password'])
    
    def retrieve_last_viewed(self, user_id):
        rows = self.connection.execute('SELECT * from last_viewed_listings WHERE user_id=%s', [user_id])
        if len(rows) == 0:
            return None
        else:
            return rows[0]['listing_id']
        
    def set_last_viewed(self, user_id, listing_id):
        rows = self.connection.execute('INSERT INTO last_viewed_listings (user_id, listing_id) VALUES (%s, %s) ON CONFLICT (user_id) DO UPDATE SET listing_id = EXCLUDED.listing_id', [user_id, listing_id])
        return None