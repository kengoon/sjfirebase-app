from Controller.base_controller import BaseScreenController


class LoginScreenController(BaseScreenController):
    """
    The `LoginScreenController` class represents a controller implementation.
    Coordinates work of the view with the model.
    The controller implements the strategy pattern. The controller connects to
    the view to control its actions.
    """

    def account_login(self, email, password):
        self.model.login(email, password, callback=self.on_complete)

    def on_complete(self, task):
        print(dir(task))
        if task.isSuccessful():
            self.view.toast("login success")
        else:
            self.view.toast("login failed")

