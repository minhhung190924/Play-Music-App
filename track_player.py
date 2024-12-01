import tkinter as tk
import font_manager as fonts
from view_tracks import TrackViewer
from track_creator import TrackCreator
from track_updater import TrackUpdater

# Functions to handle button clicks

# Function to open the Track Viewer window
def view_tracks_clicked():
    TrackViewer(tk.Toplevel(window))

# Function to open the Track Creator window
def create_track_clicked():
    TrackCreator(tk.Toplevel(window))

# Function to open the Track Updater window
def update_tracks_clicked():
    TrackUpdater(tk.Toplevel(window))

# Main application window
window = tk.Tk() 
window.geometry("520x200") # Set the initial window size
window.title("JukeBox") # Set the title of the main window
window.configure(bg="gray") # Set the background color of the window

# Initialize and configure fonts (imported from font_manager)
fonts.configure()

# Header label for the main menu
header_lbl = tk.Label(window, text="Select an option by clicking one of the buttons below")
header_lbl.grid(row=0, column=0, columnspan=3, padx=10, pady=10) # Position the header label

# Button to view all tracks
view_tracks_btn = tk.Button(window, text="View Tracks", command=view_tracks_clicked)
view_tracks_btn.grid(row=1, column=0, padx=10, pady=10) # Position the "View Tracks" button

# Button to create a new track
create_track_list_btn = tk.Button(window, text="Create Track", command=create_track_clicked)
create_track_list_btn.grid(row=1, column=1, padx=10, pady=10) # Position the "Create Track" button

# Button to update an existing track
update_tracks_btn = tk.Button(window, text="Update Tracks", command=update_tracks_clicked)
update_tracks_btn.grid(row=1, column=2, padx=10, pady=10) # Position the "Update Tracks" button

# Label to display status messages
status_lbl = tk.Label(window, bg='gray', text="", font=("Helvetica", 10))
status_lbl.grid(row=2, column=0, columnspan=3, padx=10, pady=10) # Position the status label

# Run the main application loop
window.mainloop()