from gi.repository import Gtk


class Handler:
    def onDeleteWindow(self, *args):
        Gtk.main_quit(*args)
        system.exit();

    def onButtonPressed(self, b2):
		Gtk.main_quit(*args)
		print ("O is hacker")
		system.exit()
		
		
		
		
		
x = Gtk.Builder()

x.add_from_file("first.glade")



y1 = x.get_object("window1")
y3 = x.get_object("window2")
y2 = x.get_object("button1")	
y4 = x.get_object("button2")	

def omar_1 (z) :
	y3.show_all()
	y1.hide()

y2.connect("clicked", omar_1)

def omar_2 (z) :
	y1.show_all()
	y3.hide()

y4.connect("clicked", omar_2)


y1.show_all()
Gtk.main()


