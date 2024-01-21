from kivy.properties import ObjectProperty
from kivymd.toast import toast
from kivymd.uix.screen import MDScreen
from Utility.observer import Observer
from libs.singleton import screen_extras


class BaseScreenView(MDScreen, Observer):
    """
    A base class that implements a visual representation of the model data.
    The view class must be inherited from this class.
    """

    controller = ObjectProperty()
    """
    Controller object - :class:`~Controller.controller_screen.ClassScreenControler`.

    :attr:`controller` is an :class:`~kivy.properties.ObjectProperty`
    and defaults to `None`.
    """

    model = ObjectProperty()
    """
    Model object - :class:`~Model.model_screen.ClassScreenModel`.

    :attr:`model` is an :class:`~kivy.properties.ObjectProperty`
    and defaults to `None`.
    """

    def __init__(self, app, **kw):
        super().__init__(**kw)
        # Often you need to get access to the application object from the view
        # class. You can do this using this attribute.
        self.app = app
        # Adding a view class as observer.
        self.model.add_observer(self)
        self.md_bg_color = self.theme_cls.surfaceColor
        self.theme_cls.bind(surfaceColor=self.setter("md_bg_color"))
    
    @staticmethod
    def put_extra(key, value):
        screen_extras[key] = value

    @staticmethod
    def get_extra(key):
        return screen_extras[key]
    
    @staticmethod
    def remove_extra(key):
        del screen_extras[key]

    def switch_screen(self, screen_name):
        self.app.add_screen(screen_name)

    @staticmethod
    def toast(text):
        toast(text)

