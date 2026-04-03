USERS_FILE = "data/users.json"


def load_users():
    if not os.path.exists(USERS_FILE):
        with open(USERS_FILE, "w") as file:
            json.dump([], file)

    with open(USERS_FILE, "r") as file:
        return json.load(file)


def login_user(username, password):
    users = load_users()

    for user in users:
        if user["username"] == username and user["password"] == password:
            return user

    return None