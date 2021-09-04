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

class InfoBox(Gtk.Window):
	"""this class creates the info window"""
	
	def __init__(self):
		Gtk.Window.__init__(self)
		self.app_width = 300		
		self.app_height = 300
		self.set_default_size(self.app_width, self.app_height)
		self.set_border_width(15)
		self.set_title("Information")
		self.create_info_window()
		self.connect("destroy", self.close_window)
		self.show_all()
		
		
	def create_info_window(self):
		"""create gui of info window"""			
		# widget containers of infobox
		self.box_main = Gtk.Box(orientation = Gtk.Orientation.VERTICAL, spacing = 10)
		self.add(self.box_main)
		self.box_1 = Gtk.Box(orientation = Gtk.Orientation.HORIZONTAL, spacing = 135)
		self.box_main.pack_start(self.box_1,True,True,0)
		self.box_2 = Gtk.Box(orientation = Gtk.Orientation.HORIZONTAL, spacing = 5)
		self.box_main.pack_start(self.box_2,True,True,0)

		# back button and its icon
		back_image = Gtk.Image()
		back_image.set_from_file("../res/back.png")
		back_but = Gtk.Button()
		back_but.add(back_image)
		back_but.set_hexpand(False)
		back_but.set_halign(Gtk.Align.START)
		back_but.set_vexpand(False)
		back_but.set_valign(Gtk.Align.CENTER)
		back_but.connect("clicked",self.close_window)
		self.box_1.pack_start(back_but,False,False,0)
		
		# labels of info
		title_label = Gtk.Label()
		title_label.set_markup("<b>~~~Info~~~</b>")
		
		info_label = Gtk.Label()
		info_label.set_text("This application aims to help users cite their references in a more automated way.\n\n"
								"The user can choose between the citation of a paper, a book and an in-book chapter.\n"
								 "The icons of the main menu appear in this sequence. The user is also given the ability \n"
								"to choose between the Harvard and the APA Citation Style from the main menu. After \n"
								"importing the data in the textboxes(entries), the user can create the citation by \n"
								"clicking the \"Go!\" button. Finally, the user can copy the formatted citation directly\n"
		  						"to clipboard by clicking the \"Copy\" button, and from there paste it where needed.\n\n"
		  						"Please note that this program comes without any warranty!") 				
		self.box_1.pack_start(title_label,False,False,1)
		self.box_2.pack_start(info_label,True,True,0)	


	def close_window(self,widget):
		self.destroy()

