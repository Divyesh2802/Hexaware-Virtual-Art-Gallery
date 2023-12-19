class UserNotFoundException(Exception):
    def __init__(self, user_id):
        super().__init__(f"User ID: {user_id} not found in the system.")
