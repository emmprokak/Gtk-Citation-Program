"""
Gtk Citation Program
Copyright (C) 2021 Prokakis Emmanouil

Gtk Citation Program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

Gtk Citation Program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with Gtk Citation Program. If not, see <https://www.gnu.org/licenses/>.

"""

import gi

gi.require_version("Gtk", "3.0")

from gi.repository import Gtk

class InfoWindow(Gtk.Window):
	
	def __init__(self):
		
		glade_file = "info.glade"	
		self.builder = Gtk.Builder()
		self.builder.add_from_file(glade_file)
		
		self.window = self.builder.get_object("info_window")
		self.window.set_border_width(15)
		self.window.set_title("About")
		
		self.window.connect("delete-event", self.close_window)
		self.window.show()
		

	def close_window(self,widget,window):		
		self.window.hide()
