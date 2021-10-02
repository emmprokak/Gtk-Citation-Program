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
	
def format_citation(gui_obj):		
	format_citation_authors(gui_obj)		
	year = gui_obj.entry_year.get_text()
	title = gui_obj.entry_title.get_text()
	final_title = format_title(gui_obj,title)
	
	if gui_obj.publish_type == "paper":
		publisher = gui_obj.entry_publisher.get_text()
	elif gui_obj.publish_type == "book":
		place = gui_obj.entry_place.get_text()
		publisher = gui_obj.entry_publisher.get_text()		
	
	# add other details to the resulting citation and show result	
	if gui_obj.style == "Harvard":	
		if gui_obj.publish_type == "paper":
			gui_obj.format += f" ({year}), \"{final_title}\", {publisher.title()}"
		elif gui_obj.publish_type == "book":
			gui_obj.format += f" ({year}), {final_title}, {place.title()}: {publisher.title()}"
		elif gui_obj.publish_type == "chapter":
			gui_obj.format += f" ({year}), \"{final_title}\", In "
	elif gui_obj.style == "APA":
		if gui_obj.publish_type == "paper":
			gui_obj.format += f" ({year}). {final_title}. {publisher.title()}"
		elif gui_obj.publish_type == "book":
			gui_obj.format += f" ({year}). {final_title}. {place.title()}: {publisher.title()}"	
		elif gui_obj.publish_type == "chapter":
			gui_obj.format += f" ({year}). {final_title}. In "
	if gui_obj.publish_type == "chapter":
		format_in_citation(gui_obj)
	
	gui_obj.result_label.set_text(gui_obj.format)
		
def format_citation_authors(gui_obj):
	# handle author's name
	author = gui_obj.entry_author.get_text()
	word_of_given_text = author.split()
	single_word_author = False
	# I try to split the second word given. If I get an IndexError, it
	# doesn't exist, so I know if we have a single word author
	try:
		letter = split_string(word_of_given_text[1])
	except IndexError:
		single_word_author = True
		
	if gui_obj.style == "Harvard":
		if not single_word_author:
			gui_obj.format += f"{word_of_given_text[0].title()} {letter[0].title()}."
		else:
			gui_obj.format += f"{author.upper()}"
	elif gui_obj.style == "APA":
		if not single_word_author:
			gui_obj.format += f"{word_of_given_text[0].title()}, {letter[0].title()}."
		else:
			gui_obj.format += f"{author.upper()}" 
			
	# handle 2nd and 3rd author, provided they exist
	if gui_obj.two_auth or gui_obj.three_auth:
		# 2nd author would automatically exist if there were a 3rd
		author_2nd = gui_obj.entry_2nd_author.get_text()
		word_of_given_text_2nd = author_2nd.split()
		single_word_2nd_author = False
		try:
			letter_2nd = split_string(word_of_given_text_2nd[1])
		except IndexError:
			single_word_2nd_author = True
			
		if gui_obj.style == "Harvard":
			if not single_word_2nd_author:
				gui_obj.format += f", {word_of_given_text_2nd[0].title()} {letter_2nd[0].title()}."
			else:
				gui_obj.format += f", {author_2nd.upper()}"
		elif gui_obj.style == "APA":
			if not single_word_2nd_author:
				gui_obj.format += f", {word_of_given_text_2nd[0].title()}, {letter_2nd[0].title()}."
			else:
				gui_obj.format += f", {author_2nd.upper()}"
				
	# but a 2nd author can exist without a 3rd, resulting in an extra if statement for the 3rd
	if gui_obj.three_auth:
		# handle 3rd author
		author_3rd = gui_obj.entry_3rd_author.get_text()
		word_of_given_text_3rd = author_3rd.split()
		single_word_3rd_author = False
		try:
			letter_3rd = split_string(word_of_given_text_3rd[1])
		except IndexError:
			single_word_3rd_author = True
			
		if gui_obj.style == "Harvard":
			if not single_word_3rd_author:
				gui_obj.format += f" && {word_of_given_text_3rd[0].title()} {letter_3rd[0].title()}."
			else:
				gui_obj.format += f" && {author_3rd.upper()}"
		elif gui_obj.style == "APA":
			if not single_word_3rd_author:
				gui_obj.format += f" && {word_of_given_text_3rd[0].title()}, {letter_3rd[0].title()}."
			else:
				gui_obj.format += f" && {author_3rd.upper()}"
		
def format_title(gui_obj,title):
	final_title = ""
	title_words = title.split()
	word_count = len(title.split())
	
	for i in range(0,word_count):
		if(title_words[i].lower() == "and" or title_words[i].lower() == "of" or 
			title_words[i].lower() == "the" and i != 0 or title_words[i].lower() == "or"):
			# dont add space char at start and at end of title
			if i != word_count and i != 0:
				final_title += " "	
			final_title += title_words[i].lower()		
		else:
			if i != word_count and i != 0:
				final_title += " "					
			final_title += title_words[i].title()
			
	return final_title
	
def format_in_citation(gui_obj):
	"""handle the In part of the citation"""
	# handle author's name
	in_author = gui_obj.in_entry_author.get_text()
	in_word_of_given_text = in_author.split()
	in_single_word_author = False
	try:
		in_letter = split_string(in_word_of_given_text[1])
	except IndexError:
		in_single_word_author = True
	
	if gui_obj.style == "Harvard":
		if not in_single_word_author:
			gui_obj.format += f"{in_word_of_given_text[0].title()} {in_letter[0].title()}."
		else:
			gui_obj.format += f"{in_author.upper()}"
	elif gui_obj.style == "APA":
		if not in_single_word_author:
			gui_obj.format += f"{in_word_of_given_text[0].title()}, {in_letter[0].title()}."
		else:
			gui_obj.format += f"{in_author.upper()}" 
			 		
	# handle 2nd and 3rd author, provided they exist
	if gui_obj.in_two_auth or gui_obj.in_three_auth:
		# 2nd author would automatically exist if there were a 3rd
		in_author_2nd = gui_obj.in_entry_2nd_author.get_text()
		in_word_of_given_text_2nd = in_author_2nd.split()
		in_single_word_2nd_author = False
		try:
			in_letter_2nd = split_string(in_word_of_given_text_2nd[1])
		except IndexError:
			in_single_word_2nd_author = True
				
		if gui_obj.style == "Harvard":
			if not in_single_word_2nd_author:
				gui_obj.format += f", {in_word_of_given_text_2nd[0].title()} {in_letter_2nd[0].title()}."
			else:
				gui_obj.format += f", {in_author_2nd.upper()}"
		elif gui_obj.style == "APA":
			if not in_single_word_2nd_author:
				gui_obj.format += f", {in_word_of_given_text_2nd[0].title()}, {in_letter_2nd[0].title()}."
			else:
				gui_obj.format += f", {in_author_2nd.upper()}" 		

		
		# but a 2nd author can exist without a 3rd, resulting in an extra if statement for the 3rd
		if gui_obj.in_three_auth:
			# handle 3rd author
			in_author_3rd = gui_obj.in_entry_3rd_author.get_text()
			in_word_of_given_text_3rd = in_author_3rd.split()
			in_single_word_3rd_author = False
			try:
				in_letter_3rd = split_string(in_word_of_given_text_3rd[1])
			except IndexError:
				in_single_word_3rd_author = True
			
			if gui_obj.style == "Harvard":
				if not in_single_word_3rd_author:
					gui_obj.format += f" && {in_word_of_given_text_3rd[0].title()} {in_letter_3rd[0].title()}."
				else:
					gui_obj.format += f" && {in_author_3rd.upper()}"
			elif gui_obj.style == "APA":
				if not in_single_word_3rd_author:
					gui_obj.format += f"&& {in_word_of_given_text_3rd[0].title()}, {in_letter_3rd[0].title()}."
				else:
					gui_obj.format += f"&& {in_author_3rd.upper()}" 
				
	# get other details	
	in_year = gui_obj.entry_year.get_text()
	in_title = gui_obj.entry_title.get_text()
	in_final_title = format_title(gui_obj,in_title)
	in_place = gui_obj.in_entry_place.get_text()
	in_publisher = gui_obj.in_entry_publisher.get_text()
	# check if it will be (ed) or (eds)
	editor_str = ""
	if gui_obj.in_two_auth or gui_obj.in_three_auth:
		editor_str = "(eds)"
	else:
		editor_str = "(ed)"	
	
	# add other details to the resulting citation and show result
	if gui_obj.style == "Harvard":	
		gui_obj.format += f" {editor_str} ({in_year}), {in_final_title}, {in_place.title()}: {in_publisher.title()}"
	elif gui_obj.style == "APA":
		gui_obj.format += f" {editor_str} ({in_year}). {in_final_title}. {in_place.title()}: {in_publisher.title()}"
	
def split_string(text):
		return [word for word in text]
