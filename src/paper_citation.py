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

from gi.repository import Gtk,Gdk
from citation_functions import format_citation

class PaperCitationGUI(Gtk.Window):
	
	def __init__(self,style):
		
		self.init_glade_file()
		self.style = style
		self.publish_type = "paper"
		self.init_window_and_buttons()
		self.init_entries_and_labels()
						
		self.one_auth = True
		self.two_auth = False
		self.three_auth = False
		
		self.mod_window_based_on_authors()		
		
		self.clipboard = Gtk.Clipboard().get(Gdk.SELECTION_CLIPBOARD)
		
		self.window.connect("delete-event", self.close_window)
		self.window.show()
	
	def init_glade_file(self):
		glade_file = "paper.glade"
		self.builder = Gtk.Builder()
		self.builder.add_from_file(glade_file)
		
	def init_window_and_buttons(self):
		self.window = self.builder.get_object("paper_window")
		self.window.set_title(f"Citing in {self.style}")
		
		self.grid = self.builder.get_object("grid")
			
		self.back_button = self.builder.get_object("back_button")
		self.back_go = self.builder.get_object("go_button")
		self.back_copy = self.builder.get_object("copy_button")
		self.back_button.connect("clicked",self.back_out_of_window)
		self.back_go.connect("clicked",self.butclicked)
		self.back_copy.connect("clicked",self.copy_to_clipboard)
		
		self.radio_auth1 = self.builder.get_object("radiobutton1")
		self.radio_auth2 = self.builder.get_object("radiobutton2")
		self.radio_auth3 = self.builder.get_object("radiobutton3")
		
		self.radio_auth1.connect("toggled",self.check_radio_toggled,True)
		self.radio_auth2.connect("toggled",self.check_radio_toggled,True)
		self.radio_auth3.connect("toggled",self.check_radio_toggled,True)
		
	def init_entries_and_labels(self):
		self.entry_author = self.builder.get_object("entry_author")
		self.entry_2nd_author = self.builder.get_object("entry_2nd_author")
		self.entry_3rd_author = self.builder.get_object("entry_3rd_author")
		self.entry_year = self.builder.get_object("entry_year")
		self.entry_title = self.builder.get_object("entry_title")
		self.entry_details = self.builder.get_object("entry_details")
		
		self.result_label = self.builder.get_object("result_label")
		self.result_label.set_line_wrap(True)
		self.result_label.set_selectable(True)
		
	def butclicked(self,widget):
		"""Go button gets clicked, citation gets formatted"""	
		self.format = ""				
		format_citation(self)			
				
	def check_radio_toggled(self, button, name):
		"""monitor which of the radio buttons is activated"""			
		if self.radio_auth1.get_active():
			self.one_auth = True
			self.two_auth = False
			self.three_auth = False
			self.mod_window_based_on_authors()
		elif self.radio_auth2.get_active():
			self.two_auth = True
			self.one_auth = False
			self.three_auth = False
			self.mod_window_based_on_authors()
		elif self.radio_auth3.get_active():
			self.three_auth = True
			self.one_auth = False
			self.two_auth = False
			self.mod_window_based_on_authors()
		else:
			self.one_auth = False
			self.two_auth = False
			self.three_auth = False
									
	def mod_window_based_on_authors(self):
		"""modify the gui based on number of authors"""
		if self.two_auth and not self.three_auth:
			self.grid.get_child_at(0,1).show()
			self.grid.get_child_at(1,1).show()
			self.grid.get_child_at(0,2).hide()
			self.grid.get_child_at(1,2).hide()
			self.grid.set_row_spacing(5)
			
		elif self.three_auth:
			self.grid.get_child_at(0,1).show()
			self.grid.get_child_at(1,1).show()
			self.grid.get_child_at(0,2).show()
			self.grid.get_child_at(1,2).show()
			self.grid.set_row_spacing(5)
			
		elif self.one_auth:
			self.grid.get_child_at(0,1).hide()
			self.grid.get_child_at(1,1).hide()
			self.grid.get_child_at(0,2).hide()
			self.grid.get_child_at(1,2).hide()
			self.grid.set_row_spacing(11)		

	def copy_to_clipboard(self,widget):
		self.clipboard.set_text(self.format, -1)		
			
	def back_out_of_window(self,widget):		
		self.window.hide()
		
	def close_window(self,widget,window):		
		self.window.hide()
		
