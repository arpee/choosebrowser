#!/usr/bin/python
import sys
import webbrowser
import subprocess
from gi.repository import Gtk

class ButtonWindow(Gtk.Window):

    def __init__(self):
        Gtk.Window.__init__(self, title="Choose Browser")
        self.set_border_width(120)

        hbox = Gtk.Box(spacing=20)
        self.add(hbox)

        button = Gtk.Button("Firefox")
        button.connect("clicked", self.on_ff_clicked)
        #button.set_border_width(40)
        hbox.pack_start(button, True, True, 0)

        button = Gtk.Button("Chrome")
        button.connect("clicked", self.on_cr_clicked)
        #button.set_border_width(40)
        hbox.pack_start(button, True, True, 0)

        button = Gtk.Button("Chromium")
        button.connect("clicked", self.on_cr_clicked)
        #button.set_border_width(40)
        hbox.pack_start(button, True, True, 0)

        button = Gtk.Button("_Close", use_underline=True)
        button.connect("clicked", self.on_close_clicked)
        #button.set_border_width(40)
        hbox.pack_start(button, True, True, 0)

    def on_ff_clicked(self, button):
        webbrowser.get('firefox').open_new_tab(sys.argv[1])
        Gtk.main_quit()

    def on_cr_clicked(self, button):
        #webbrowser.get('chromium').open_new_tab(sys.argv[1])
        process_one = subprocess.Popen(['google-chrome-stable', sys.argv[1]])
        Gtk.main_quit()

    def on_cr_clicked(self, button):
        webbrowser.get('chromium').open_new_tab(sys.argv[1])
        Gtk.main_quit()

    def on_close_clicked(self, button):
        print("Closing application")
        Gtk.main_quit()

win = ButtonWindow()
win.connect("delete-event", Gtk.main_quit)
win.show_all()
Gtk.main()

