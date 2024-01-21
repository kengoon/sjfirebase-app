from sjfirebase.jinterface import OnCompleteListener

from Model.base_model import BaseScreenModel


class SignupScreenModel(BaseScreenModel):
    """
    Implements the logic of the
    :class:`~View.SignupScreen.signup_screen.SignupScreenView` class.
    """

    def __init__(self, database):
        super().__init__(database)

    def signup(self, email, password, callback):
        listener = OnCompleteListener(callback)
        auth = self.database.auth.get_instance()
        auth.createUserWithEmailAndPassword(email, password).addOnCompleteListener(listener)
