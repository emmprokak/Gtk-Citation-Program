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

class CitePaper(Gtk.Window):
	"""this class cites papers"""
	
	def __init__(self,style):
		Gtk.Window.__init__(self)
		self.app_width = 400
		self.style = style
		self.app_height = 330
		self.set_default_size(self.app_width, self.app_height)
		self.set_border_width(15)
		self.set_title(f"Enter information to cite paper in {self.style} Style:")
		self.clipboard = Gtk.Clipboard().get(Gdk.SELECTION_CLIPBOARD)
		self.REFRESH = False
		self.one_auth = False
		self.two_auth = False
		self.three_auth = False
		self.create_citepaper_interface()
		self.format = ""
		self.connect("destroy", self.close_window)
		self.show_all()
		
	def create_citepaper_interface(self):
		"""create the gui for citing papers"""		
		# widget containers of book
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
			
		# labels of paper
		label_author = Gtk.Label(xalign = 0)
		label_author.set_text("Author: ")
		label_year = Gtk.Label(xalign = 0)
		label_year.set_text("Year: ")
		label_title = Gtk.Label(xalign = 0)
		label_title.set_text("Title: ")
		label_publisher = Gtk.Label(xalign = 0)
		label_publisher.set_text("Details: ")
		
		self.box_1.pack_start(label_author,True,True,0)
		self.box_5.pack_start(label_year,True,True,0)
		self.box_6.pack_start(label_title,True,True,0)
		self.box_7.pack_start(label_publisher,True,True,0)
		
		# entries of paper
		self.entry_author = Gtk.Entry(xalign = 0)
		self.entry_year = Gtk.Entry(xalign = 0)
		self.entry_title = Gtk.Entry(xalign = 0)		
		self.entry_publisher = Gtk.Entry(xalign = 0)
		
		self.box_1.pack_start(self.entry_author,True,True,0)
		self.box_5.pack_start(self.entry_year,True,True,0)
		self.box_6.pack_start(self.entry_title,True,True,0)
		self.box_7.pack_start(self.entry_publisher,True,True,0)
		
		# radiobuttons
		self.radio_auth1 = Gtk.RadioButton.new_with_label_from_widget(None, "One Author")
		self.radio_auth1.connect("toggled",self.check_radio_toggled,True)
		self.radio_auth2 = Gtk.RadioButton.new_with_label_from_widget(self.radio_auth1, "Two Authors")
		self.radio_auth2.connect("toggled",self.check_radio_toggled,True)
		self.radio_auth3 = Gtk.RadioButton.new_with_label_from_widget(self.radio_auth2, "Three Authors")
		self.radio_auth3.connect("toggled",self.check_radio_toggled,True)
		
		self.box_2.pack_start(self.radio_auth1, False, False, 0)
		self.box_2.pack_start(self.radio_auth2, False, False, 0)
		self.box_2.pack_start(self.radio_auth3, False, False, 0)
		
		# extra authors labels and their entries
		self.entry_2nd_author = Gtk.Entry(xalign = 0)
		self.entry_3rd_author = Gtk.Entry(xalign = 0)
		
		self.label_2nd_author = Gtk.Label(xalign = 0)
		self.label_2nd_author.set_text("2nd Author: ")
		self.label_3rd_author = Gtk.Label(xalign = 0)
		self.label_3rd_author.set_text("3rd Author: ")
				
		# back button
		back_image = Gtk.Image()
		back_image.set_from_file("../res/back_small.png")
		back_button = Gtk.Button()
		back_button.add(back_image)
		back_button.connect("clicked",self.close_window)
		self.box_8.pack_start(back_button,False,False,0)
		
		# go and copy button
		but_go = Gtk.Button(label = "Go!")
		self.box_8.pack_end(but_go,False,False,0)
		but_go.connect("clicked",self.butclicked)
		
		but_copy = Gtk.Button(label = "Copy")
		self.box_8.pack_end(but_copy,False,False,0)
		but_copy.connect("clicked",self.copy_to_clipboard)
				
		# result label
		self.result_label = Gtk.Label()
		self.result_label.set_text(" ")
		self.result_label.set_line_wrap(True)
		self.result_label.set_selectable(True)
		self.box_9.pack_start(self.result_label,True,True,0)
		
			
	def butclicked(self,widget):
		"""Go button gets clicked, citation gets formatted"""	
		# clear the result variable
		self.format = ""				
		# check if citation has to be done in harvard or apa style
		if self.style == 'Harvard':
			self.harvard_citation()							
		elif self.style == 'APA':
			self.apa_citation()
			
	
	def harvard_citation(self):
		"""format citation in harvard style"""
		# handle author's name
		author = self.entry_author.get_text()
		word_of_given_text = author.split()
		single_word_author = False
		# I try to split the second word given. If I get an IndexError, it
		# doesn't exist, so I know if we have a single word author
		try:
			letter = self.split_string(word_of_given_text[1])
		except IndexError:
			single_word_author = True
				
		if not single_word_author:
			self.format += f"{word_of_given_text[0].title()} {letter[0].title()}."
		else:
			self.format += f"{author.upper()}" 
			
		# handle 2nd and 3rd author, provided they exist
		if self.two_auth or self.three_auth:
			# 2nd author would automatically exist if there were a 3rd
			author_2nd = self.entry_2nd_author.get_text()
			word_of_given_text_2nd = author_2nd.split()
			single_word_2nd_author = False
			try:
				letter_2nd = self.split_string(word_of_given_text_2nd[1])
			except IndexError:
				single_word_2nd_author = True
					
			if not single_word_2nd_author:
				self.format += f", {word_of_given_text_2nd[0].title()} {letter_2nd[0].title()}."
			else:
				self.format += f", {author_2nd.upper()}"
			
			# but a 2nd author can exist without a 3rd, resulting in an extra if statement for the 3rd
			if self.three_auth:
				# handle 3rd author
				author_3rd = self.entry_3rd_author.get_text()
				word_of_given_text_3rd = author_3rd.split()
				single_word_3rd_author = False
				try:
					letter_3rd = self.split_string(word_of_given_text_3rd[1])
				except IndexError:
					single_word_3rd_author = True
						
				if not single_word_3rd_author:
					self.format += f" && {word_of_given_text_3rd[0].title()} {letter_3rd[0].title()}."
				else:
					self.format += f" && {author_3rd.upper()}"
		
		# get other details	
		year = self.entry_year.get_text()
		title = self.entry_title.get_text()
		publisher = self.entry_publisher.get_text()
		
		# add other details to the resulting citation and show result	
		self.format += f" ({year}), \"{title.title()}\", {publisher.title()}"
		self.result_label.set_text(self.format)	
	
	def apa_citation(self):
		"""format citation in apa style"""		
		# handle author's name
		author = self.entry_author.get_text()
		word_of_given_text = author.split()
		single_word_author = False
		# I try to split the second word given. If I get an IndexError, it
		# doesn't exist, so I know if we have a single word author
		try:
			letter = self.split_string(word_of_given_text[1])
		except IndexError:
			single_word_author = True
				
		if not single_word_author:
			self.format += f"{word_of_given_text[0].title()}, {letter[0].title()}."
		else:
			self.format += f"{author.upper()}" 
			
		# handle 2nd and 3rd author, provided they exist
		if self.two_auth or self.three_auth:
			# 2nd author would automatically exist if there were a 3rd
			author_2nd = self.entry_2nd_author.get_text()
			word_of_given_text_2nd = author_2nd.split()
			single_word_2nd_author = False
			try:
				letter_2nd = self.split_string(word_of_given_text_2nd[1])
			except IndexError:
				single_word_2nd_author = True
					
			if not single_word_2nd_author:
				self.format += f", {word_of_given_text_2nd[0].title()}, {letter_2nd[0].title()}."
			else:
				self.format += f", {author_2nd.upper()}"
			
			# but a 2nd author can exist without a 3rd, resulting in an extra if statement
			if self.three_auth:
				# handle 3rd author
				author_3rd = self.entry_3rd_author.get_text()
				word_of_given_text_3rd = author_3rd.split()
				single_word_3rd_author = False
				try:
					letter_3rd = self.split_string(word_of_given_text_3rd[1])
				except IndexError:
					single_word_3rd_author = True
						
				if not single_word_3rd_author:
					self.format += f" && {word_of_given_text_3rd[0].title()}, {letter_3rd[0].title()}."
				else:
					self.format += f" && {author_3rd.upper()}"
		
		# get other details	
		year = self.entry_year.get_text()
		title = self.entry_title.get_text()
		publisher = self.entry_publisher.get_text()
		
		# add other details to the resulting citation and show result	
		self.format += f" ({year}). {title.title()}. {publisher.title()}"
		self.result_label.set_text(self.format)
		
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
		# draw the modifications	
		self.show_all()
								
	def split_string(self,text):
		return [word for word in text]
		
	def copy_to_clipboard(self,widget):
		self.clipboard.set_text(self.format, -1)
		
	def close_window(self,widget):
		self.destroy()
