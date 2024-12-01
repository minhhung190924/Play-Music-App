import tkinter as tk
import tkinter.messagebox as messagebox
import tkinter.scrolledtext as tkst
import random
import webbrowser
import track_library as lib
import font_manager as fonts

def set_text(text_area, content):
    text_area.delete("1.0", tk.END)
    text_area.insert(1.0, content)


class TrackViewer:
    def __init__(self, window):
        self.window = window
        window.geometry("750x400")
        window.title("View Tracks")

        # Create the "List All Tracks" button
        list_tracks_btn = tk.Button(window, text="List All Tracks", command=self.list_tracks_clicked)
        list_tracks_btn.grid(row=0, column=0, padx=10, pady=10)

        # Create the "Enter Track Number" label
        enter_lbl = tk.Label(window, text="Enter Track Number")
        enter_lbl.grid(row=0, column=1, padx=10, pady=10)

        # Create the input field to enter Track ID
        vcmd = (window.register(self.validate_input), '%P')
        self.input_txt = tk.Entry(window, width=3, validate="key", validatecommand=vcmd)
        self.input_txt.grid(row=0, column=2, padx=10, pady=10)

        # Create the "View Track" button
        view_track_btn = tk.Button(window, text="View Track", command=self.view_tracks_clicked)
        view_track_btn.grid(row=0, column=3, padx=10, pady=10)

        # Create the ScrolledText widget for listing all tracks
        self.list_txt = tkst.ScrolledText(window, width=48, height=12, wrap="none")
        self.list_txt.grid(row=1, column=0, columnspan=3, sticky="W", padx=10, pady=10)

        # Create the Text widget to display track details
        self.track_txt = tk.Text(window, width=24, height=4, wrap="none")
        self.track_txt.grid(row=1, column=3, sticky="NW", padx=10, pady=10)

        # Create the status label to show messages
        self.status_lbl = tk.Label(window, text="", font=("Helvetica", 10))
        self.status_lbl.grid(row=2, column=0, columnspan=4, sticky="W", padx=10, pady=10)

        # Create the "Delete Track" button
        delete_track_btn = tk.Button(window, text="Delete Track", command=self.delete_track_clicked)
        delete_track_btn.grid(row=2, column=1, padx=10, pady=10)

        # Create the "Undo Delete" button
        undo_delete_btn = tk.Button(window, text="Undo Delete", command=self.undo_delete_clicked)
        undo_delete_btn.grid(row=2, column=2, padx=10, pady=10)

        # Create the "Shuffle Play" button
        shuffle_play_btn = tk.Button(window, text="Shuffle Play", command=self.shuffle_play_clicked)
        shuffle_play_btn.grid(row=3, column=1, padx=10, pady=10)

        # Create the "Play Online" button
        online_play_btn = tk.Button(window, text="Play Online", command=self.play_online_clicked)
        online_play_btn.grid(row=3, column=2, padx=10, pady=10)

        # Initially load and display the list of tracks
        self.list_tracks_clicked()

    # Input validation to ensure the Track ID is a number
    def validate_input(self, input_value):
        if input_value.isdigit() or input_value == "":
            return True
        else:
            messagebox.showerror("Invalid Input", "Track ID must be a number!")
            return False

    # Load and display the list of all tracks in the library
    def list_tracks_clicked(self):
        track_list = lib.list_all()
        set_text(self.list_txt, track_list)
        self.status_lbl.configure(text="List Tracks button was clicked!")

    # Display details of a specific track when the user enters the Track ID
    def view_tracks_clicked(self):
        key = self.input_txt.get().strip()

        if not key:
            messagebox.showerror("Input Error", "Please enter a Track ID!")
            return

        name = lib.get_name(key)
        if name:
            artist = lib.get_artist(key)
            rating = lib.get_rating(key)
            play_count = lib.get_play_count(key)
            track_details = f"{name}\n{artist}\nRating: {rating}\nPlays: {play_count}"
            set_text(self.track_txt, track_details)
            self.status_lbl.configure(text="Track details loaded successfully!", fg="green")
        else:
            messagebox.showerror("Track Not Found", f"Track ID '{key}' not found!")
            set_text(self.track_txt, "")

    # Shuffle play functionality: pick a random track from the library
    def shuffle_play_clicked(self):
        if not lib.library:
            messagebox.showerror("Library Error", "No tracks available in the library!")
            return

        random_key = random.choice(list(lib.library.keys()))
        track = lib.library[random_key]

        track_details = f"{track.name}\n{track.artist}\nRating: {track.rating}\nPlays: {track.play_count}"
        set_text(self.track_txt, track_details)

        lib.increment_play_count(random_key)

        self.status_lbl.configure(text=f"Now playing: {track.name} by {track.artist}", fg="green")

        # Update the input field with the random track ID
        self.input_txt.delete(0, tk.END)
        self.input_txt.insert(0, random_key)

    # Delete the track from the library based on the entered Track ID
    def delete_track_clicked(self):
        key = self.input_txt.get().strip()
        if not key:
            messagebox.showerror("Input Error", "Please enter a Track ID!")
            return

        if lib.delete_track(key):
            self.status_lbl.configure(text=f"Track {key} deleted successfully!", fg="green")
            self.list_tracks_clicked()
        else:
            messagebox.showerror("Track Not Found", f"Track ID '{key}' not found!")

    # Undo the last deletion of a track and restore it to the library
    def undo_delete_clicked(self):
        if lib.undo_last_delete():
            self.status_lbl.configure(text="Last deleted track restored!", fg="green")
            self.list_tracks_clicked()
        else:
            messagebox.showerror("Undo Error", "No track to restore!")

    # Play the track online via YouTube by opening the search URL
    def play_online_clicked(self):
        key = self.input_txt.get().strip()

        if not key.isdigit():
            tk.messagebox.showerror("Input Error", "Track ID must be a valid number!")
            return

        url = lib.get_youtube_search_url(key)
        if url:
            webbrowser.open(url)
            self.status_lbl.configure(text=f"Opening song ID {key} on YouTube...", fg="blue")
        else:
            tk.messagebox.showerror("Track Not Found", f"No information found for Track ID '{key}'!")

