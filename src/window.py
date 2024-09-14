from gi.repository import Adw
from gi.repository import Gtk

@Gtk.Template(resource_path='/org/gnome/test/window.ui')
class TestWindow(Adw.ApplicationWindow):
    __gtype_name__ = 'TestWindow'

    label = Gtk.Template.Child()

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    @Gtk.Template.Callback()
    def btn_click(self,*argv):
        print("Hii")
