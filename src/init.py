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
from citation_functions import *
from gui import Citation_GUI
from info import InfoBox

class GtkCitationProgram(Gtk.Window):
	
	def __init__(self):
		Gtk.Window.__init__(self)
		self.app_width = 400
		self.app_height = 400
		self.set_default_size(self.app_width, self.app_height)
		self.set_border_width(15)
		self.set_title("~Gtk Citation Program v1.1~")
		self.create_main_menu()
					
	def create_main_menu(self):
		"""create the main menu gui"""
		# widget containers of main menu
		self.box_main_menu = Gtk.Box(orientation = Gtk.Orientation.VERTICAL,spacing = 0)
		self.add(self.box_main_menu)
		self.box_main_one = Gtk.Box(orientation = Gtk.Orientation.VERTICAL,spacing = 5)
		self.box_main_menu.pack_start(self.box_main_one,True,True,0)
		self.box_main_two = Gtk.Box(orientation = Gtk.Orientation.HORIZONTAL,spacing = 30)
		self.box_main_menu.pack_start(self.box_main_two,True,True,0)
		self.box_main_three = Gtk.Box(orientation = Gtk.Orientation.HORIZONTAL,spacing = 5)
		self.box_main_menu.pack_start(self.box_main_three,True,True,0)		
		# labels of main menu
		main_label = Gtk.Label()
		main_label.set_markup("<i>Prokakis Emmanouil (C) 2021 </i>\nlicensed under the GNU GPLv3")
		self.box_main_one.pack_start(main_label, True,True,0)		
		self.create_main_menu_buttons()	
		
	def get_citation_type(self):			
		return self.combo.get_active_text()
		
	def cite_paper(self,widget):
		window_paper = Citation_GUI("paper",self.get_citation_type())
				
	def cite_book(self,widget):
		window_book = Citation_GUI("book",self.get_citation_type())
		
	def cite_chapter(self,widget):
		window_book = Citation_GUI("chapter",self.get_citation_type())
		
	def show_info(self,widget):
		window_info = InfoBox()
		
	def create_main_menu_buttons(self):
		# images for buttons of main menu
		image_paper = Gtk.Image()
		image_paper.set_from_file("../res/paper.png")
		image_book = Gtk.Image()
		image_book.set_from_file("../res/book.png")
		image_chapter = Gtk.Image()
		image_chapter.set_from_file("../res/chapter.png")
		image_info = Gtk.Image()
		image_info.set_from_file("../res/info_small.png")	
		
		but_paper = Gtk.Button()
		but_paper.add(image_paper)
		but_paper.set_hexpand(False)
		but_paper.set_halign(Gtk.Align.CENTER)
		but_paper.set_vexpand(False)
		but_paper.set_valign(Gtk.Align.CENTER)
		but_paper.connect("clicked",self.cite_paper)
		self.box_main_two.pack_start(but_paper,True,True,0)
		
		but_book = Gtk.Button()
		but_book.add(image_book)
		but_book.set_hexpand(True)
		but_book.set_halign(Gtk.Align.CENTER)
		but_book.set_vexpand(False)
		but_book.set_valign(Gtk.Align.CENTER)
		but_book.connect("clicked",self.cite_book)
		self.box_main_two.pack_start(but_book,True,True,0)
		
		but_chapter = Gtk.Button()
		but_chapter.add(image_chapter)
		but_chapter.set_hexpand(True)
		but_chapter.set_halign(Gtk.Align.CENTER)
		but_chapter.set_vexpand(False)
		but_chapter.set_valign(Gtk.Align.CENTER)
		but_chapter.connect("clicked",self.cite_chapter)
		self.box_main_two.pack_start(but_chapter,True,True,0)
		
		but_other = Gtk.Button()
		but_other.add(image_info)
		but_other.set_vexpand(False)
		but_other.set_valign(Gtk.Align.CENTER)
		but_other.connect("clicked",self.show_info)
		self.box_main_three.pack_end(but_other,False,False,1)
		
		# combobox of main menu
		self.combo = Gtk.ComboBoxText()
		self.combo.insert(0,"0","Harvard Style")
		self.combo.insert(1,"1","APA Style")
		self.combo.set_active(0)
		self.combo.set_hexpand(False)
		self.combo.set_halign(Gtk.Align.CENTER)
		self.combo.set_vexpand(False)
		self.combo.set_valign(Gtk.Align.CENTER)
		self.box_main_three.pack_start(self.combo,False,False,0)
		
