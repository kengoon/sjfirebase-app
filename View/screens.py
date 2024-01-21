# The screens dictionary contains the objects of the models and controllers
# of the screens of the application.


from Model.signup_screen import SignupScreenModel
from Controller.signup_screen import SignupScreenController
from View.SignupScreen.signup_screen import SignupScreenView
from Model.login_screen import LoginScreenModel
from Controller.login_screen import LoginScreenController
from View.LoginScreen.login_screen import LoginScreenView

screens = {
    "signup screen": {
        "model": SignupScreenModel,
        "controller": SignupScreenController,
        "view": SignupScreenView,
        "kv": "./View/SignupScreen/signup_screen.kv"
    },

    "login screen": {
        "model": LoginScreenModel,
        "controller": LoginScreenController,
        "view": LoginScreenView,
        "kv": "./View/LoginScreen/login_screen.kv"
    },
}
