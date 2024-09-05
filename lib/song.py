class Song:
    count = 0
    artists = []
    genres = []
    genre_count ={}
    artist_count = {}

    def __init__(self, name, artist, genre):
        self.name = name
        self.artist = artist
        self.genre = genre 

        # Increment song count
        Song.add_song_to_count()

        #Add to artist and genre lists
        Song.add_to_artists(artist)
        Song.add_to_genres(genre)

        # Update genre and artist counts
        Song.add_to_genre_count(genre)
        Song.add_to_artist_count(artist)

    @classmethod
    def add_song_to_count(cls):
        cls.count += 1

    @classmethod
    def add_to_artists(cls, artist):
        if artist not in cls.artists:
            cls.artists.append(artist)

    @classmethod
    def add_to_genres(cls, genre):
        if genre not in cls.genres:
            cls.genres.append(genre)        

    @classmethod
    def add_to_genre_count(cls, genre):
        if genre in cls.genre_count:
            cls.genre_count[genre] += 1
        else:
            cls.genre_count[genre] = 1

    @classmethod 
    def add_to_artist_count(cls, artist):
        if artist in cls.artist_count:
            cls.artist_count[artist] += 1
        else:
            cls.artist_count[artist] = 1


# Example 
song1 = Song("99 Problems", "Jay-Z", "Rap")
song2 = Song("Halo", "Beyonce", "Pop")
song3 = Song("God's Plan", "Drake", "Rap")
song4 = Song("Formation", "Beyonce", "Pop")

# Accwessing the class attributes 
print(Song.count)
print(Song.artists)
print(Song.genres)
print(Song.genre_count)
print(Song.artist_count)

