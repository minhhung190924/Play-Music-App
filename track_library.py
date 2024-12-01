from library_item import LibraryItem
import urllib.parse

# Initialize a library containing a collection of tracks, stored as LibraryItem objects
library = {
    "01": LibraryItem("Another Brick in the Wall", "Pink Floyd", 4),
    "02": LibraryItem("Stayin' Alive", "Bee Gees", 5),
    "03": LibraryItem("Highway to Hell", "AC/DC", 2),
    "04": LibraryItem("Shape of You", "Ed Sheeran", 1),
    "05": LibraryItem("Someone Like You", "Adele", 3),
}

# List all tracks in the library, sorted alphabetically by track name
def list_all():
    output = ""
    for key, item in sorted(library.items(), key=lambda x: x[1].name):
        output += f"{key} {item.info()}\n"
    return output

# Retrieve the name of a track given its key
def get_name(key):
    return library.get(key).name if key in library else None

# Retrieve the artist of a track given its key
def get_artist(key):
    return library.get(key).artist if key in library else None

# Retrieve the rating of a track given its key
def get_rating(key):
    return library.get(key).rating if key in library else -1

# Update the rating of a track given its key
def set_rating(key, rating):
    if key in library:
        library[key].rating = rating

# Retrieve the play count of a track given its key
def get_play_count(key):
    return library.get(key).play_count if key in library else -1

# Increment the play count of a track given its key
def increment_play_count(key):
    if key in library:
        library[key].play_count += 1

# Add a new track to the library if the key does not already exist
def add_track(key, name, artist, rating=0):
    if key not in library:
        new_item = LibraryItem(name, artist, rating)
        new_item.is_user_added = True # Mark the item as added by the user
        library[key] = new_item
    else:
        raise ValueError("Track with this key already exists!")

# Update an existing track's details in the library
def update_track(key, name=None, artist=None, rating=None, play_count=None):
    if key in library:
        if name is not None:
            library[key].name = name
        if artist is not None:
            library[key].artist = artist
        if rating is not None:
            library[key].rating = rating
        if play_count is not None:
            library[key].play_count = play_count
        return f"Track {key} updated successfully!"
    return f"Track {key} not found!"

# Stack to store deleted tracks for undo functionality
undo_stack = []

# Delete a track from the library and save it in the undo stack
def delete_track(key):
    if key in library:
        undo_stack.append({'key': key, 'item': library[key]})
        del library[key]
        return True
    return False

# Undo the last deleted track by restoring it from the undo stack
def undo_last_delete():
    if undo_stack:
        deleted_track = undo_stack.pop()
        library[deleted_track['key']] = deleted_track['item']
        return True
    return False

# Generate a YouTube search URL for a given track ID
def get_youtube_search_url(track_id):
    if track_id in library:
        item = library[track_id]
        query = f"{item.name} {item.artist}"
        search_url = f"https://www.youtube.com/results?search_query={urllib.parse.quote(query)}"
        return search_url
    return None