def user_schemas(user) -> dict:
    return {
        'id': str(user['_id']),
        'firstname': str(user['firstname']),
        'lastname': str(user['lastname']),
        'email': str(user['email']),
        'avatar': str(user['avatar'])
    }


def users_schemas(users) -> list:
    return [user_schemas(user) for user in users]
