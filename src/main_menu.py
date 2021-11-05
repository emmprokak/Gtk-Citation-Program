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
from paper_citation import PaperCitationGUI
from book_citation import BookCitationGUI
from chapter_citation import ChapterCitationGUI
from info import InfoWindow	

class GtkCitationProgram(Gtk.Window):
	
	def __init__(self):
		glade_file = "main_menu.glade"
		
		self.builder = Gtk.Builder()
		self.builder.add_from_file(glade_file)
		window = self.builder.get_object("main_menu")
		window.set_title("Gtk Citation Program")
		window.set_border_width(15)
		window.connect("delete-event", Gtk.main_quit)
		self.fetch_gui_widgets()
		
		window.show()
			
	def get_citation_type(self):			
		return self.combo.get_active_text()
		
	def cite_paper(self,widget):
		window_paper = PaperCitationGUI(self.get_citation_type())
				
	def cite_book(self,widget):
		window_book = BookCitationGUI(self.get_citation_type())
		
	def cite_chapter(self,widget):
		window_chapter = ChapterCitationGUI(self.get_citation_type())
		
	def show_info(self,widget):
		window_info = InfoWindow()
		
	def fetch_gui_widgets(self):
		self.combo = self.builder.get_object("combo_box")
		# buttons
		but_paper = self.builder.get_object("button_paper")
		but_book = self.builder.get_object("button_book")
		but_chapter = self.builder.get_object("button_chapter")
		but_info = self.builder.get_object("button_info")
		
		but_paper.connect("clicked",self.cite_paper)
		but_book.connect("clicked",self.cite_book)
		but_chapter.connect("clicked",self.cite_chapter)
		but_info.connect("clicked",self.show_info)
		
		
