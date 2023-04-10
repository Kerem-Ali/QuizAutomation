class InvalidLoginError(Exception):
    """Exception raised for errors in the login."""
    
    def __init__(self,message="Email or password is invalid"):
        self.message=message
        super().__init__(self.message)

class NullInputError(Exception):
    """Exception raised for errors in the login."""
    
    def __init__(self,message="Email or password you entered is null"):
        self.message=message
        super().__init__(self.message)
