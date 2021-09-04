# Gtk Citation Program
## Prokakis Emmanouil (C) 2021

Hi there! I am happy to see you found my software on github and I hope you may find some use in it.

This Citation Program, based on the Gtk toolkit and written in Python, aims to help the user format his/her citations in a more automated way. The program formats the data given by the user to a complete citation, ready to be pasted into school/university projects and academic papers!

![central](https://user-images.githubusercontent.com/89413115/132100397-15bf6735-e87a-45f0-a21c-b5a048211195.png)


The program allows users to cite papers, books and in-book chapters in both the Harvard and APA citation standards. All the user has to do is enter data in the entries of the GUI, and the program will format the citation in a proper manner.

![Screenshot from 2021-09-02 19-35-32](https://user-images.githubusercontent.com/89413115/132100419-4340183d-44aa-4c9d-a048-20d53b36dbb7.png)

The icons of the program are all made by Dany Lip.

**Beware that this program is currently running only on Linux (Gnome, Kde, Xfce and Pantheon have been tested). A Windows version will probably come in the future.**

For Linux: Just download the zip file, extract it and run the citation_program.py module from terminal with
```
python3 citation_program.py
```
  
A feature, that the program is currently missing, is the automatic formatting of parts of the resulting citation as italics text, which is needed for some citations. It can be done for Gtk.Label() objects with label_obj.set_markup(), but I seem unable to store the italics text to a variable, in order for it to be copied to clipboard by the Copy button. I am certain that with more time, and given the help of this large community, a solution will be found.

Please remember that I am a self-taught programmer, and that I do this as a hobby because: a) It's fun and b) I want to give back to the Free and Open Source Software community.

If there is anything in the code that could be classified as a bad practice, please don't hesitate to point it out, since it's going to make the software better and help me improve in the future.

I'm always open to suggestions and very grateful for useful feedback.
