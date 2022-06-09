from models.user import UserModel
import hmac
#users = [
#    User(1, 'bob', 'asdf')
#]
#username_mapping = {u.username: u for u in users}
#userid_mapping = {u.id: u for u in users}

def authenicate(username, password):
    user = UserModel.find_by_username(username)
    if user and hmac.compare_digest(user.password, password):
        return user

def identity(payload):
    user_id=payload['identity']
    return UserModel.find_by_id(user_id)


