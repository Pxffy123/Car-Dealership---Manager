from functools import wraps 

def login_required(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        # Check if the user is logged in
        if not getattr(args[0], 'is_authenticated', False):
            raise PermissionError("User must be logged in to access this function.")
        return func(*args, **kwargs)
    return wrapper

    def admin_required(func):
        @wraps(func)
        def wrapper(self, *args, **kwargs):
        
            if self.current_user is None:
                print ("Please login first.")
                return None

                # Check if the current user is an admin