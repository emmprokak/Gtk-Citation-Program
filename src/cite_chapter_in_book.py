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

class CiteChapter(Gtk.Window):
	"""this class cites chapters of books"""
	
	def __init__(self,style):
		Gtk.Window.__init__(self)
		self.app_width = 400
		self.app_height = 400
		self.style = style
		self.set_default_size(self.app_width, self.app_height)
		self.set_border_width(15)
		self.set_title(f"Enter information to cite chapter in {self.style} Style:")
		self.clipboard = Gtk.Clipboard().get(Gdk.SELECTION_CLIPBOARD)
		self.REFRESH = False
		self.one_auth = False
		self.two_auth = False
		self.three_auth = False
		# The "in" variables, in general, refer to the In part of the citation,
		# referencing the book that the chapter is published on
		self.in_one_auth = False
		self.in_two_auth = False
		self.in_three_auth = False
		self.format = ""
		self.create_citechapter_interface()
		self.connect("destroy", self.close_window)
		self.show_all()
		
	def create_citechapter_interface(self):
		"""create the gui for book chapters"""		
		# widget box containers of chapter
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
			
		# labels of chapter
		label_author = Gtk.Label(xalign = 0)
		label_author.set_text("Author: ")
		label_year = Gtk.Label(xalign = 0)
		label_year.set_text("Year: ")
		label_title = Gtk.Label(xalign = 0)
		label_title.set_text("Title: ")
		
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
		
		self.box_1.pack_start(label_author,True,True,0)
		self.box_5.pack_start(label_year,True,True,0)
		self.box_6.pack_start(label_title,True,True,0)
		self.box_8.pack_start(in_label,True,True,0)
		self.box_9.pack_start(in_label_author,True,True,0)
		self.box_13.pack_start(in_label_year,True,True,0)
		self.box_14.pack_start(in_label_title,True,True,0)
		self.box_15.pack_start(in_label_place,True,True,0)
		self.box_16.pack_start(in_label_publisher,True,True,0)
				
		# entries of chapter
		self.entry_author = Gtk.Entry(xalign = 0)
		self.entry_year = Gtk.Entry(xalign = 0)
		self.entry_title = Gtk.Entry(xalign = 0)
		self.in_entry_author = Gtk.Entry(xalign = 0)
		self.in_entry_year = Gtk.Entry(xalign = 0)
		self.in_entry_title = Gtk.Entry(xalign = 0)
		self.in_entry_place = Gtk.Entry(xalign = 0)
		self.in_entry_publisher = Gtk.Entry(xalign = 0)
		
		self.box_1.pack_start(self.entry_author,True,True,0)
		self.box_5.pack_start(self.entry_year,True,True,0)
		self.box_6.pack_start(self.entry_title,True,True,0)
		self.box_9.pack_start(self.in_entry_author,True,True,0)
		self.box_13.pack_start(self.in_entry_year,True,True,0)
		self.box_14.pack_start(self.in_entry_title,True,True,0)
		self.box_15.pack_start(self.in_entry_place,True,True,0)
		self.box_16.pack_start(self.in_entry_publisher,True,True,0)
		
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
		
		# in_radio_buttons
		self.radio_auth4 = Gtk.RadioButton.new_with_label_from_widget(None, "One Author")
		self.radio_auth4.connect("toggled",self.check_radio_toggled_in,True)
		self.radio_auth5 = Gtk.RadioButton.new_with_label_from_widget(self.radio_auth4, "Two Authors")
		self.radio_auth5.connect("toggled",self.check_radio_toggled_in,True)
		self.radio_auth6 = Gtk.RadioButton.new_with_label_from_widget(self.radio_auth5, "Three Authors")
		self.radio_auth6.connect("toggled",self.check_radio_toggled_in,True)
		
		self.box_10.pack_start(self.radio_auth4, False, False, 0)
		self.box_10.pack_start(self.radio_auth5, False, False, 0)
		self.box_10.pack_start(self.radio_auth6, False, False, 0)
			
		# extra authors labels and entries
		self.entry_2nd_author = Gtk.Entry(xalign = 0)
		self.entry_3rd_author = Gtk.Entry(xalign = 0)
		
		self.label_2nd_author = Gtk.Label(xalign = 0)
		self.label_2nd_author.set_text("2nd Author: ")
		self.label_3rd_author = Gtk.Label(xalign = 0)
		self.label_3rd_author.set_text("3rd Author: ")
		
		self.in_entry_2nd_author = Gtk.Entry(xalign = 0)
		self.in_entry_3rd_author = Gtk.Entry(xalign = 0)
		
		self.in_label_2nd_author = Gtk.Label(xalign = 0)
		self.in_label_2nd_author.set_text("2nd Author: ")
		self.in_label_3rd_author = Gtk.Label(xalign = 0)
		self.in_label_3rd_author.set_text("3rd Author: ")
		
		# back button
		back_image = Gtk.Image()
		back_image.set_from_file("../res/back_small.png")
		back_button = Gtk.Button()
		back_button.add(back_image)
		back_button.connect("clicked",self.close_window)
		self.box_17.pack_start(back_button,False,False,0)
		
		# go and copy button
		but_go = Gtk.Button(label = "Go!")
		self.box_17.pack_end(but_go,False,False,0)
		but_go.connect("clicked",self.butclicked)
		
		but_copy = Gtk.Button(label = "Copy")
		self.box_17.pack_end(but_copy,False,False,0)
		but_copy.connect("clicked",self.copy_to_clipboard)
				
		# result label
		self.result_label = Gtk.Label()
		self.result_label.set_text(" ")
		self.result_label.set_line_wrap(True)
		self.result_label.set_selectable(True)
		self.box_18.pack_start(self.result_label,True,True,0)
		
			
	def butclicked(self,widget):
		"""go button gets clicked, citation gets formatted"""
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
		
		# add other details to the resulting citation and show result	
		self.format += f" ({year}), \"{title.title()}\", In "
		
		# the function handles the In part of the citation and creates the final citation
		self.harvard_in_citation()
	
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
					self.format += f" && {word_of_given_text_3rd[0].title()}, {letter_3rd[0].title()}."
				else:
					self.format += f" && {author_3rd.upper()}"
		
		# get other details	
		year = self.entry_year.get_text()
		title = self.entry_title.get_text()
		
		# add other details to the resulting citation and show result	
		self.format += f" ({year}). {title.title()}. In "
		
		# the function handles the In part of the citation and creates the final citation
		self.apa_in_citation()
		
	def harvard_in_citation(self):
		"""handle the In part of the citation in harvard style"""
		# handle author's name
		in_author = self.in_entry_author.get_text()
		in_word_of_given_text = in_author.split()
		in_single_word_author = False
		try:
			in_letter = self.split_string(in_word_of_given_text[1])
		except IndexError:
			in_single_word_author = True
				
		if not in_single_word_author:
			self.format += f"{in_word_of_given_text[0].title()} {in_letter[0].title()}."
		else:
			self.format += f"{in_author.upper()}" 
			
		# handle 2nd and 3rd author, provided they exist
		if self.in_two_auth or self.in_three_auth:
			# 2nd author would automatically exist if there were a 3rd
			in_author_2nd = self.in_entry_2nd_author.get_text()
			in_word_of_given_text_2nd = in_author_2nd.split()
			in_single_word_2nd_author = False
			try:
				in_letter_2nd = self.split_string(in_word_of_given_text_2nd[1])
			except IndexError:
				in_single_word_2nd_author = True
					
			if not in_single_word_2nd_author:
				self.format += f", {in_word_of_given_text_2nd[0].title()} {in_letter_2nd[0].title()}."
			else:
				self.format += f", {in_author_2nd.upper()}"
			
			# but a 2nd author can exist without a 3rd, resulting in an extra if statement for the 3rd
			if self.in_three_auth:
				# handle 3rd author
				in_author_3rd = self.in_entry_3rd_author.get_text()
				in_word_of_given_text_3rd = in_author_3rd.split()
				in_single_word_3rd_author = False
				try:
					in_letter_3rd = self.split_string(in_word_of_given_text_3rd[1])
				except IndexError:
					in_single_word_3rd_author = True
						
				if not in_single_word_3rd_author:
					self.format += f" && {in_word_of_given_text_3rd[0].title()} {in_letter_3rd[0].title()}."
				else:
					self.format += f" && {in_author_3rd.upper()}"
					
		# get other details	
		in_year = self.entry_year.get_text()
		in_title = self.entry_title.get_text()
		in_place = self.in_entry_place.get_text()
		in_publisher = self.in_entry_publisher.get_text()
		
		# add other details to the resulting citation and show result
		# check if it will be (ed) or (eds)
		if self.in_two_auth or self.in_three_auth:	
			self.format += f" (eds) ({in_year}), {in_title.title()}, {in_place.title()}: {in_publisher.title()}"
		else:
			self.format += f" (ed) ({in_year}), {in_title.title()}, {in_place.title()}: {in_publisher.title()}"
		
		self.result_label.set_text(self.format)	
		
	def apa_in_citation(self):
		"""handle the In part of the citation in apa style"""
		# handle author's name
		in_author = self.in_entry_author.get_text()
		in_word_of_given_text = in_author.split()
		in_single_word_author = False
		try:
			in_letter = self.split_string(in_word_of_given_text[1])
		except IndexError:
			in_single_word_author = True
				
		if not in_single_word_author:
			self.format += f"{in_word_of_given_text[0].title()}, {in_letter[0].title()}."
		else:
			self.format += f"{in_author.upper()}" 
			
		# handle 2nd and 3rd author, provided they exist
		if self.in_two_auth or self.in_three_auth:
			# 2nd author would automatically exist if there were a 3rd
			in_author_2nd = self.in_entry_2nd_author.get_text()
			in_word_of_given_text_2nd = in_author_2nd.split()
			in_single_word_2nd_author = False
			try:
				in_letter_2nd = self.split_string(in_word_of_given_text_2nd[1])
			except IndexError:
				in_single_word_2nd_author = True
					
			if not in_single_word_2nd_author:
				self.format += f", {in_word_of_given_text_2nd[0].title()}, {in_letter_2nd[0].title()}."
			else:
				self.format += f"{in_author_2nd.upper()}"
			
			# but a 2nd author can exist without a 3rd, resulting in an extra if statement for the 3rd
			if self.three_auth:
				# handle 3rd author
				in_author_3rd = self.in_entry_3rd_author.get_text()
				in_word_of_given_text_3rd = in_author_3rd.split()
				in_single_word_3rd_author = False
				try:
					in_letter_3rd = self.split_string(in_word_of_given_text_3rd[1])
				except IndexError:
					in_single_word_3rd_author = True
						
				if not in_single_word_3rd_author:
					self.format += f" && {in_word_of_given_text_3rd[0].title()}, {in_letter_3rd[0].title()}."
				else:
					self.format += f" && {in_author_3rd.upper()}"
					
		# get other details	
		in_year = self.entry_year.get_text()
		in_title = self.entry_title.get_text()
		in_place = self.in_entry_place.get_text()
		in_publisher = self.in_entry_publisher.get_text()
		
		# add other details to the resulting citation and show result
		# check if it will be (ed) or (eds)
		if self.in_two_auth or self.in_three_auth:	
			self.format += f"  (eds) ({in_year}). {in_title.title()}. {in_place.title()}: {in_publisher.title()}"
		else:
			self.format += f" (ed) ({in_year}). {in_title.title()}. {in_place.title()}: {in_publisher.title()}"
						
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
			
	def check_radio_toggled_in(self,button,name):
		"""monitor which of the IN radio buttons is activated"""
		if self.radio_auth4.get_active():
			self.in_one_auth = True
			self.in_two_auth = False
			self.in_three_auth = False
			self.mod_window_based_on_in_authors()
		elif self.radio_auth5.get_active():
			self.in_two_auth = True
			self.in_one_auth = False
			self.in_three_auth = False
			self.mod_window_based_on_in_authors()
		elif self.radio_auth6.get_active():
			self.in_three_auth = True
			self.in_one_auth = False
			self.in_two_auth = False
			self.mod_window_based_on_in_authors()
		else:
			self.in_one_auth = False
			self.in_two_auth = False
			self.in_three_auth = False
	
			
	def mod_window_based_on_authors(self):
		"""modify the window based on number of authors"""
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
		
	def mod_window_based_on_in_authors(self):
		"""modify the window based on number of IN authors"""
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
		
	def split_string(self,text):
		return [word for word in text]
		
	def copy_to_clipboard(self,widget):
		self.clipboard.set_text(self.format, -1)
		
	def close_window(self,widget):
		self.destroy()
