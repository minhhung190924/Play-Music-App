import tkinter as tk
import track_library as lib
import font_manager as fonts


class TrackCreator:
    def __init__(self, window):
        window.title("Create Track") # Set the title of the window
        window.geometry("400x250") # Set the size of the window

        # Label and entry for track name
        tk.Label(window, text="Enter Track Name:").grid(row=0, column=0, padx=10, pady=10) # Prompt for track name
        self.name_entry = tk.Entry(window, width=30) # Text entry for track name
        self.name_entry.grid(row=0, column=1, padx=10, pady=10)

        # Label and entry for artist name
        tk.Label(window, text="Enter Artist Name:").grid(row=1, column=0, padx=10, pady=10) # Prompt for artist name
        self.artist_entry = tk.Entry(window, width=30) # Text entry for artist name
        self.artist_entry.grid(row=1, column=1, padx=10, pady=10)

        # Label and entry for rating
        tk.Label(window, text="Enter Rating (0-5):").grid(row=2, column=0, padx=10, pady=10) # Prompt for rating
        self.rating_entry = tk.Entry(window, width=5) # Text entry for rating (0-5)
        self.rating_entry.grid(row=2, column=1, padx=10, pady=10)

        # Button to add the track
        tk.Button(window, text="Add Track", command=self.add_track).grid(row=3, column=0, columnspan=2, pady=20)

        # Label to display status messages
        self.status_lbl = tk.Label(window, text="", fg="green") # Default is green for success messages
        self.status_lbl.grid(row=4, column=0, columnspan=2)

    def add_track(self):

        # Get and strip whitespace from input fields
        name = self.name_entry.get().strip() # Get the track name
        artist = self.artist_entry.get().strip() # Get the artist name

        # Check if the track name is empty
        if not name:
            self.status_lbl.config(text="Track name cannot be empty!", fg="red") # Error message
            return
        
        # Check if the artist name is empty
        if not artist:
            self.status_lbl.config(text="Artist name cannot be empty!", fg="red") # Error message
            return

        # Check if the track already exists in the library
        for track_id, track in lib.library.items():
            if track.name.lower() == name.lower() and track.artist.lower() == artist.lower():
                self.status_lbl.config(text="Error: Song already exists in the library!", fg="red")
                return # Exit the function if the track exists

        try:
            # Validate and parse the rating input
            rating = int(self.rating_entry.get()) # Convert rating to integer
            if 0 <= rating <= 5: # Ensure the rating is within the valid range (0-5)
                # Generate a new track ID (zero-padded to 2 digits)
                track_id = str(len(lib.library) + 1).zfill(2)
                # Add the new track to the library
                lib.library[track_id] = lib.LibraryItem(name, artist, rating)
                self.status_lbl.config(text="Track successfully added!", fg="green")# Success message
            else:
                self.status_lbl.config(text="Rating must be between 0 and 5!", fg="red") # Error message
        except ValueError:
            # Handle non-numeric input for rating
            self.status_lbl.config(text="Invalid rating. Please enter a number!", fg="red") # Error message
