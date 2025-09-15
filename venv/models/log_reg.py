import database.library as db

class Login:
    def __init__(self, username, password):
        self.username = username
        self.password = password

        self.authenticated = self.authenticate(username, password)
        
    def authenticate(self, username, password):
        if db.login_account(username, password):
            return True
        return False
    
class Register:
    def __init__(self, studId, studName, studPass):
        self.id = studId
        self.username = studName
        self.password = studPass

        self.registered = self.register_to_db()
        if self.registered:
            print("Registration successful.")
        else:
            print("Registration failed. Try again.")
    
    def register_to_db(self):
        if db.register_account(self.id, self.username, self.password):
            return True
        return False