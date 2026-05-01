def require_auth(func):
    def wrapper(user, *args, **kwargs):
        if not user.get("is_authenticated"):
            print("Access Denied")
            return
        return func(user, *args, **kwargs)
    return wrapper

@require_auth
def dashboard(user):
    print("Welcome to dashboard")

user1 = {"name": "Raman", "is_authenticated": False}
dashboard(user1)