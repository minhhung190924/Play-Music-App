import tkinter as tk
import track_library as lib
import font_manager as fonts


class TrackUpdater:
    def __init__(self, window):
        window.title("Update Track") # Set the window title
        window.geometry("400x300") # Set the size of the window

        # Label and entry for track ID
        tk.Label(window, text="Enter Track ID:").grid(row=0, column=0, padx=10, pady=10) # Prompt for track ID
        self.id_entry = tk.Entry(window, width=5) # Entry for track ID
        self.id_entry.grid(row=0, column=1, padx=10, pady=10)

        # Label and entry for updating the track name
        tk.Label(window, text="Update Name:").grid(row=1, column=0, padx=10, pady=10) # Prompt for new name
        self.name_entry = tk.Entry(window, width=30) # Entry for the new track name
        self.name_entry.grid(row=1, column=1, padx=10, pady=10)

        # Label and entry for updating the artist name
        tk.Label(window, text="Update Artist:").grid(row=2, column=0, padx=10, pady=10) # Prompt for new artist
        self.artist_entry = tk.Entry(window, width=30) # Entry for the new artist name
        self.artist_entry.grid(row=2, column=1, padx=10, pady=10)

        # Label and entry for updating the track rating
        tk.Label(window, text="Update Rating:").grid(row=3, column=0, padx=10, pady=10) # Prompt for new rating 
        self.rating_entry = tk.Entry(window, width=5) # Entry for the new rating (0-5)
        self.rating_entry.grid(row=3, column=1, padx=10, pady=10)

        # Button to update the track
        tk.Button(window, text="Update Track", command=self.update_track).grid(row=4, column=0, columnspan=2, pady=20)

         # Label to display the status of the update
        self.status_lbl = tk.Label(window, text="", fg="green") # Default is green for success
        self.status_lbl.grid(row=5, column=0, columnspan=2)

    def update_track(self):
        # Get the track ID from the user input
        track_id = self.id_entry.get().strip()

        # Check if the track ID exists in the library
        if track_id in lib.library:
            # Get and strip user input for name and artist
            name = self.name_entry.get().strip() # New name
            artist = self.artist_entry.get().strip() # New artist
            try:
                # Get and validate the rating input
                rating = self.rating_entry.get().strip()
                if rating: # If rating is provided, validate it
                    rating = int(rating) # Convert rating to integer
                    if not (0 <= rating <= 5): # Check if rating is within range
                        self.status_lbl.config(text="Rating must be between 0 and 5!", fg="red") # Error message
                        return
                else:
                    # If no rating is provided, keep the current rating
                    rating = lib.library[track_id].rating

                # Update the track details if the respective fields are provided
                if name:
                    lib.library[track_id].name = name # Update name
                if artist:
                    lib.library[track_id].artist = artist # Update artist
                lib.library[track_id].rating = rating # Update rating

                # Display success message
                self.status_lbl.config(text="Track successfully updated!")
            except ValueError:
                # Handle invalid input for rating
                self.status_lbl.config(text="Invalid rating. Please enter a number!", fg="red") # Error message
        else:
            # Display error if track ID is not found
            self.status_lbl.config(text="Track ID not found!", fg="red") # Error message
