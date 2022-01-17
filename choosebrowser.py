#!/usr/bin/python
import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk
import sys
import webbrowser
import subprocess
#import pyperclip
#try:
#        from Tkinter import Tk
#except ImportError:
#        from tkinter import Tk
#        r = Tk()


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

        button = Gtk.Button("Web")
        button.connect("clicked", self.on_web_clicked)
        hbox.pack_start(button, True, True, 0)

        button = Gtk.Button("Chrome")
        button.connect("clicked", self.on_gc_clicked)
        hbox.pack_start(button, True, True, 0)

        button = Gtk.Button("Chromium")
        button.connect("clicked", self.on_cr_clicked)
        hbox.pack_start(button, True, True, 0)

        button = Gtk.Button("Vivaldi")
        button.connect("clicked", self.on_vv_clicked)
        hbox.pack_start(button, True, True, 0)

        button = Gtk.Button("Edge")
        button.connect("clicked", self.on_edge_clicked)
        hbox.pack_start(button, True, True, 0)

        button = Gtk.Button("Brave")
        button.connect("clicked", self.on_brave_clicked)
        hbox.pack_start(button, True, True, 0)

        button = Gtk.Button("Zoom")
        button.connect("clicked", self.on_zoom_clicked)
        hbox.pack_start(button, True, True, 0)

        button = Gtk.Button("Copy")
        button.connect("clicked", self.on_cp_clicked)
        hbox.pack_start(button, True, True, 0)

        button = Gtk.Button("_Close", use_underline=True)
        button.connect("clicked", self.on_close_clicked)
        #button.set_border_width(40)
        hbox.pack_start(button, True, True, 0)

    def on_ff_clicked(self, button):
        webbrowser.get('firefox').open_new_tab(sys.argv[1])
        Gtk.main_quit()

    def on_web_clicked(self, button):
        webbrowser.get('epiphany').open_new_tab(sys.argv[1])
        Gtk.main_quit()

    def on_gc_clicked(self, button):
        process_one = subprocess.Popen(['google-chrome-stable', sys.argv[1]])
        Gtk.main_quit()

    def on_cr_clicked(self, button):
        webbrowser.get('chromium').open_new_tab(sys.argv[1])
        Gtk.main_quit()

    def on_vv_clicked(self, button):
        process_one = subprocess.Popen(['vivaldi-stable', sys.argv[1]])
        Gtk.main_quit()

    def on_edge_clicked(self, button):
        process_one = subprocess.Popen(['microsoft-edge-dev', sys.argv[1]])
        Gtk.main_quit()

    def on_brave_clicked(self, button):
        process_one = subprocess.Popen(['brave', sys.argv[1]])
        Gtk.main_quit()

    def on_zoom_clicked(self, button):
        process_one = subprocess.Popen(['zoom', '--url='+sys.argv[1]])
        Gtk.main_quit()

    def on_cp_clicked(self, button):
        #pyperclip.copy(sys.argv[1])
        r.withdraw()
        r.clipboard_clear()
        r.clipboard_append('i can has clipboardz?')
        r.update() # now it stays on the clipboard after the window is closed
        #r.destroy()
        Gtk.main_quit()

    def on_close_clicked(self, button):
        print("Closing application")
        Gtk.main_quit()

win = ButtonWindow()
win.connect("delete-event", Gtk.main_quit)
win.show_all()
Gtk.main()

