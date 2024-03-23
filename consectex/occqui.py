    if close_button:
        # Set up a close button.
        close_button = gtk.Button(label="Close")
        close_button.connect("clicked", self.close_application)
        self.vbox.pack_start(close_button, False, True, 0)  
