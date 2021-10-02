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

class Citation_GUI(Gtk.Window):
	
	def __init__(self,publish_type,style):
		Gtk.Window.__init__(self)
		self.app_width = 400
		self.app_height = 330
		self.set_default_size(self.app_width, self.app_height)
		self.set_border_width(15)
		self.style = style
		self.publish_type = publish_type
		self.set_title(f"Enter information to cite {self.publish_type} in {self.style} Style:")
		if self.publish_type == "chapter":
			self.app_height == 400
			self.set_default_size(self.app_width, self.app_height)
			# The "in" variables, in general, refer to the In part of the citation,
			# referencing the book that the chapter is published on
			self.in_one_auth = False
			self.in_two_auth = False
			self.in_three_auth = False
		self.clipboard = Gtk.Clipboard().get(Gdk.SELECTION_CLIPBOARD)
		self.one_auth = False
		self.two_auth = False
		self.three_auth = False
		self.create_gui_interface()
		self.format = ""
		self.connect("destroy", self.close_window)
		self.show_all()
	
	def create_gui_interface(self):
		"""create the gui for citing papers"""					
		self.create_labels(self.publish_type)	
		self.create_entries(self.publish_type)	
		self.create_radio_buttons(self.publish_type)
		self.create_buttons(self.publish_type)		
		
	def butclicked(self,widget):
		"""Go button gets clicked, citation gets formatted"""	
		self.format = ""				
		format_citation(self)			
	
	def create_labels(self,publish_type):
		# labels of paper
		self.init_gui_containers()
		label_author = Gtk.Label(xalign = 0)
		label_author.set_text("Author: ")
		label_year = Gtk.Label(xalign = 0)
		label_year.set_text("Year: ")
		label_title = Gtk.Label(xalign = 0)
		label_title.set_text("Title: ")
		self.label_2nd_author = Gtk.Label(xalign = 0)
		self.label_2nd_author.set_text("2nd Author: ")
		self.label_3rd_author = Gtk.Label(xalign = 0)
		self.label_3rd_author.set_text("3rd Author: ")
		
		if self.publish_type == "paper":
			label_publisher = Gtk.Label(xalign = 0)
			label_publisher.set_text("Details: ")
			self.box_7.pack_start(label_publisher,True,True,0)
		elif self.publish_type == "book":
			label_place = Gtk.Label(xalign = 0)
			label_place.set_text("Place: ")
			label_publisher = Gtk.Label(xalign = 0)
			label_publisher.set_text("Publisher: ")
			self.box_7.pack_start(label_place,True,True,0)
			self.box_8.pack_start(label_publisher,True,True,0)
		elif self.publish_type == "chapter":
			in_label = Gtk.Label()
			in_label.set_text("In: ")
			in_label_author = Gtk.Label(xalign = 0)
			in_label_author.set_text("Author: ")
			in_label_year = Gtk.Label(xalign = 0)
			in_label_year.set_text("Year: ")
			in_label_title = Gtk.Label(xalign = 0)
			in_label_title.set_text("Title: ")
			in_label_place = Gtk.Label(xalign = 0)
			in_label_place.set_text("Place: ")
			in_label_publisher = Gtk.Label(xalign = 0)
			in_label_publisher.set_text("Publisher: ")
			self.in_label_2nd_author = Gtk.Label(xalign = 0)
			self.in_label_2nd_author.set_text("2nd Author: ")
			self.in_label_3rd_author = Gtk.Label(xalign = 0)
			self.in_label_3rd_author.set_text("3rd Author: ")
				
			self.box_8.pack_start(in_label,True,True,0)
			self.box_9.pack_start(in_label_author,True,True,0)
			self.box_13.pack_start(in_label_year,True,True,0)
			self.box_14.pack_start(in_label_title,True,True,0)
			self.box_15.pack_start(in_label_place,True,True,0)
			self.box_16.pack_start(in_label_publisher,True,True,0)
				
		self.box_1.pack_start(label_author,True,True,0)
		self.box_5.pack_start(label_year,True,True,0)
		self.box_6.pack_start(label_title,True,True,0)	
	
	def create_entries(self,publish_type):
		self.entry_author = Gtk.Entry(xalign = 0)
		self.entry_year = Gtk.Entry(xalign = 0)
		self.entry_title = Gtk.Entry(xalign = 0)
		self.entry_2nd_author = Gtk.Entry(xalign = 0)
		self.entry_3rd_author = Gtk.Entry(xalign = 0)			
		
		if self.publish_type == "paper":
			self.entry_publisher = Gtk.Entry(xalign = 0)
			self.box_7.pack_start(self.entry_publisher,True,True,0)
		elif self.publish_type == "book":
			self.entry_place = Gtk.Entry()
			self.entry_publisher = Gtk.Entry()
			self.box_7.pack_start(self.entry_place,True,True,0)
			self.box_8.pack_start(self.entry_publisher,True,True,0)	
		elif self.publish_type == "chapter":
			self.in_entry_author = Gtk.Entry(xalign = 0)
			self.in_entry_year = Gtk.Entry(xalign = 0)
			self.in_entry_title = Gtk.Entry(xalign = 0)
			self.in_entry_place = Gtk.Entry(xalign = 0)
			self.in_entry_publisher = Gtk.Entry(xalign = 0)
			self.in_entry_2nd_author = Gtk.Entry(xalign = 0)
			self.in_entry_3rd_author = Gtk.Entry(xalign = 0)	
			
			self.box_9.pack_start(self.in_entry_author,True,True,0)
			self.box_13.pack_start(self.in_entry_year,True,True,0)
			self.box_14.pack_start(self.in_entry_title,True,True,0)
			self.box_15.pack_start(self.in_entry_place,True,True,0)
			self.box_16.pack_start(self.in_entry_publisher,True,True,0)
					
		self.box_1.pack_start(self.entry_author,True,True,0)
		self.box_5.pack_start(self.entry_year,True,True,0)
		self.box_6.pack_start(self.entry_title,True,True,0)
			
	def create_radio_buttons(self,publish_type):
		self.radio_auth1 = Gtk.RadioButton.new_with_label_from_widget(None, "One Author")
		self.radio_auth1.connect("toggled",self.check_radio_toggled,True)
		self.radio_auth2 = Gtk.RadioButton.new_with_label_from_widget(self.radio_auth1, "Two Authors")
		self.radio_auth2.connect("toggled",self.check_radio_toggled,True)
		self.radio_auth3 = Gtk.RadioButton.new_with_label_from_widget(self.radio_auth2, "Three Authors")
		self.radio_auth3.connect("toggled",self.check_radio_toggled,True)
		
		self.box_2.pack_start(self.radio_auth1, False, False, 0)
		self.box_2.pack_start(self.radio_auth2, False, False, 0)
		self.box_2.pack_start(self.radio_auth3, False, False, 0)
		
		if self.publish_type == "chapter":
			self.radio_auth4 = Gtk.RadioButton.new_with_label_from_widget(None, "One Author")
			self.radio_auth4.connect("toggled",self.check_radio_toggled_in,True)
			self.radio_auth5 = Gtk.RadioButton.new_with_label_from_widget(self.radio_auth4, "Two Authors")
			self.radio_auth5.connect("toggled",self.check_radio_toggled_in,True)
			self.radio_auth6 = Gtk.RadioButton.new_with_label_from_widget(self.radio_auth5, "Three Authors")
			self.radio_auth6.connect("toggled",self.check_radio_toggled_in,True)
			
			self.box_10.pack_start(self.radio_auth4, False, False, 0)
			self.box_10.pack_start(self.radio_auth5, False, False, 0)
			self.box_10.pack_start(self.radio_auth6, False, False, 0)	
			
	def create_buttons(self,publish_type):
		# back button
		back_image = Gtk.Image()
		back_image.set_from_file("../res/back_small.png")
		self.back_button = Gtk.Button()
		self.back_button.add(back_image)
		self.back_button.connect("clicked",self.close_window)
		
		# go and copy button
		self.but_go = Gtk.Button(label = "Go!")
		self.but_go.connect("clicked",self.butclicked)
		self.but_copy = Gtk.Button(label = "Copy")
		self.but_copy.connect("clicked",self.copy_to_clipboard)
				
		# result label
		self.result_label = Gtk.Label()
		self.result_label.set_text(" ")
		self.result_label.set_line_wrap(True)
		self.result_label.set_selectable(True)
				
		if self.publish_type == "paper":
			self.box_8.pack_start(self.back_button,False,False,0)
			self.box_8.pack_end(self.but_go,False,False,0)
			self.box_8.pack_end(self.but_copy,False,False,0)
			self.box_9.pack_start(self.result_label,True,True,0)
		elif self.publish_type == "book":
			self.box_9.pack_start(self.back_button,False,False,0)
			self.box_9.pack_end(self.but_go,False,False,0)
			self.box_9.pack_end(self.but_copy,False,False,0)
			self.box_10.pack_start(self.result_label,True,True,0)
		elif self.publish_type == "chapter":
			self.box_17.pack_start(self.back_button,False,False,0)
			self.box_17.pack_end(self.but_go,False,False,0)
			self.box_17.pack_end(self.but_copy,False,False,0)
			self.box_18.pack_start(self.result_label,True,True,0)
				
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
			
	def check_radio_toggled_in(self,button,name):
		"""monitor which of the IN radio buttons is activated"""
		if self.radio_auth4.get_active():
			self.in_one_auth = True
			self.in_two_auth = False
			self.in_three_auth = False
			self.mod_window_based_on_authors()
		elif self.radio_auth5.get_active():
			self.in_two_auth = True
			self.in_one_auth = False
			self.in_three_auth = False
			self.mod_window_based_on_authors()
		elif self.radio_auth6.get_active():
			self.in_three_auth = True
			self.in_one_auth = False
			self.in_two_auth = False
			self.mod_window_based_on_authors()
		else:
			self.in_one_auth = False
			self.in_two_auth = False
			self.in_three_auth = False
			
	def mod_window_based_on_authors(self):
		"""modify the gui based on number of authors"""
		if self.two_auth and not self.three_auth:
			self.box_3.pack_start(self.label_2nd_author,True,True,0)
			self.box_3.pack_start(self.entry_2nd_author,True,True,0)
			self.box_4.remove(self.label_3rd_author)
			self.box_4.remove(self.entry_3rd_author)
			
		elif self.three_auth:
			self.box_3.pack_start(self.label_2nd_author,True,True,0)
			self.box_3.pack_start(self.entry_2nd_author,True,True,0)
			self.box_4.pack_start(self.label_3rd_author,True,True,0)
			self.box_4.pack_start(self.entry_3rd_author,True,True,0)
			
		elif self.one_auth:
			self.box_3.remove(self.label_2nd_author)
			self.box_3.remove(self.entry_2nd_author)
			self.box_4.remove(self.label_3rd_author)
			self.box_4.remove(self.entry_3rd_author)		
		if self.publish_type == "chapter":
			if self.in_two_auth and not self.in_three_auth:
				self.box_11.pack_start(self.in_label_2nd_author,True,True,0)
				self.box_11.pack_start(self.in_entry_2nd_author,True,True,0)
				self.box_12.remove(self.in_label_3rd_author)
				self.box_12.remove(self.in_entry_3rd_author)
				
			elif self.in_three_auth:
				self.box_11.pack_start(self.in_label_2nd_author,True,True,0)
				self.box_11.pack_start(self.in_entry_2nd_author,True,True,0)
				self.box_12.pack_start(self.in_label_3rd_author,True,True,0)
				self.box_12.pack_start(self.in_entry_3rd_author,True,True,0)
				
			elif self.in_one_auth:
				self.box_11.remove(self.in_label_2nd_author)
				self.box_11.remove(self.in_entry_2nd_author)
				self.box_12.remove(self.in_label_3rd_author)
				self.box_12.remove(self.in_entry_3rd_author)
		# draw the modifications	
		self.show_all()
		
	def init_gui_containers(self):
		# widget containers
		self.box_main_book = Gtk.Box(orientation = Gtk.Orientation.VERTICAL, spacing = 2)
		self.add(self.box_main_book)
		self.box_1 = Gtk.Box(orientation = Gtk.Orientation.HORIZONTAL, spacing = 5)
		self.box_main_book.pack_start(self.box_1,True,True,0)
		self.box_2 = Gtk.Box(orientation = Gtk.Orientation.HORIZONTAL, spacing = 5)
		self.box_main_book.pack_start(self.box_2,True,True,0)
		self.box_3 = Gtk.Box(orientation = Gtk.Orientation.HORIZONTAL, spacing = 5)
		self.box_main_book.pack_start(self.box_3,True,True,0)
		self.box_4 = Gtk.Box(orientation = Gtk.Orientation.HORIZONTAL, spacing = 5)
		self.box_main_book.pack_start(self.box_4,True,True,0)
		self.box_5 = Gtk.Box(orientation = Gtk.Orientation.HORIZONTAL, spacing = 5)
		self.box_main_book.pack_start(self.box_5,True,True,0)
		self.box_6 = Gtk.Box(orientation = Gtk.Orientation.HORIZONTAL, spacing = 5)
		self.box_main_book.pack_start(self.box_6,True,True,0)
		self.box_7 = Gtk.Box(orientation = Gtk.Orientation.HORIZONTAL, spacing = 5)
		self.box_main_book.pack_start(self.box_7,True,True,0)
		self.box_8 = Gtk.Box(orientation = Gtk.Orientation.HORIZONTAL, spacing = 5)
		self.box_main_book.pack_start(self.box_8,True,True,0)
		self.box_9 = Gtk.Box(orientation = Gtk.Orientation.HORIZONTAL, spacing = 5)
		self.box_main_book.pack_start(self.box_9,True,True,0)
		self.box_10 = Gtk.Box(orientation = Gtk.Orientation.HORIZONTAL, spacing = 5)
		self.box_main_book.pack_start(self.box_10,True,True,0)
		if self.publish_type == "chapter":
			self.box_11 = Gtk.Box(orientation = Gtk.Orientation.HORIZONTAL, spacing = 5)
			self.box_main_book.pack_start(self.box_11,True,True,0)
			self.box_12 = Gtk.Box(orientation = Gtk.Orientation.HORIZONTAL, spacing = 5)
			self.box_main_book.pack_start(self.box_12,True,True,0)
			self.box_13 = Gtk.Box(orientation = Gtk.Orientation.HORIZONTAL, spacing = 5)
			self.box_main_book.pack_start(self.box_13,True,True,0)
			self.box_14 = Gtk.Box(orientation = Gtk.Orientation.HORIZONTAL, spacing = 5)
			self.box_main_book.pack_start(self.box_14,True,True,0)
			self.box_15 = Gtk.Box(orientation = Gtk.Orientation.HORIZONTAL, spacing = 5)
			self.box_main_book.pack_start(self.box_15,True,True,0)
			self.box_16 = Gtk.Box(orientation = Gtk.Orientation.HORIZONTAL, spacing = 5)
			self.box_main_book.pack_start(self.box_16,True,True,0)
			self.box_17 = Gtk.Box(orientation = Gtk.Orientation.HORIZONTAL, spacing = 5)
			self.box_main_book.pack_start(self.box_17,True,True,0)
			self.box_18 = Gtk.Box(orientation = Gtk.Orientation.HORIZONTAL, spacing = 5)
			self.box_main_book.pack_start(self.box_18,True,True,0)
			
	def copy_to_clipboard(self,widget):
		self.clipboard.set_text(self.format, -1)		
			
	def close_window(self,widget):
		self.destroy()
