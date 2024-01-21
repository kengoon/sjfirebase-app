from sjfirebase.jinterface import OnCompleteListener

from Model.base_model import BaseScreenModel


class LoginScreenModel(BaseScreenModel):
    """
    Implements the logic of the
    :class:`~View.LoginScreen.login_screen.LoginScreenView` class.
    """

    def __init__(self, database):
        super().__init__(database)

    def login(self, email, password, callback):
        listener = OnCompleteListener(callback)
        auth = self.database.auth.get_instance()
        auth.signInWithEmailAndPassword(email, password).addOnCompleteListener(listener)
