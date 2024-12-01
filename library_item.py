class LibraryItem:
    def __init__(self, name, artist, rating=0):
        self.name = name # Set the name of the track (e.g., "Shape of You")
        self.artist = artist # Set the artist or band (e.g., "Ed Sheeran")
        self.rating = rating # Set the initial rating (default is 0 if not provided)
        self.play_count = 0 # Initialize play count to 0 (number of times played)

    def info(self):
        return f"{self.name} - {self.artist} {self.stars()}" # Combine name, artist, and stars into a single string

    def stars(self):
        stars = "" # Initialize an empty string to hold the stars
        for i in range(self.rating): # Loop through the range of the rating
            stars += "*" # Add an asterisk to the string for each loop iteration
        return stars # Return the complete string of stars
 
