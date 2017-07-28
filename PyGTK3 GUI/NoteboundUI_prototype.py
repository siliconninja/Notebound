#!/usr/bin/env python

# http://www.pygtk.org/articles/pygtk-glade-gui/Creating_a_GUI_using_PyGTK_and_Glade.htm

''' Copyright (C) 2017

This file is part of Notebound.

Notebound is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

Notebound is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with Notebound.  If not, see <http://www.gnu.org/licenses/>.

Author: siliconninja '''

import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk
    
class Handler:
    def onDeleteWindow(self, *args):
        Gtk.main_quit(*args)

    def onButtonPressed(self, button):
        print("Hello World!")

builder = Gtk.Builder()
builder.add_from_file("NoteboundUI_prototype.glade")
builder.connect_signals(Handler())

window = builder.get_object("MainWindow")
window.set_title("Notebound")
window.show_all()

Gtk.main()
