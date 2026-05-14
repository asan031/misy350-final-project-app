from utils.data_manager import DataManager, USERS_FILE

def load_users():
    return DataManager.load_json(USERS_FILE)


def login_user(username, password):
    users = load_users()

    for user in users:
        if user["username"] == username and user["password"] == password:
            return user

    return None


def username_exists(users, username):
    for user in users:
        if user.get("username", "").lower() == username.lower():
            return True
    return False


def next_user_id(users):
    if not users:
        return 1

    existing_ids = [user.get("id", 0) for user in users]
    return max(existing_ids) + 1