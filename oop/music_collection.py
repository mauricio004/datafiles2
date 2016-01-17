__author__ = 'MFlores1'


class Artist:
    def __init__(self, name_artist):
        self.name_artist = name_artist
        self.albums = []
        self.songs = []

    def add_album(self, album):
        self.albums.append(album)

    def add_song(self, song):
        self.songs.append(song)

    def __str__(self):
        return self.name_artist


class Song:
    def __init__(self, name_song, artist, album, track_number):
        self.name_song = name_song
        self.artist = artist
        self.album = album
        self.track_number = track_number
        artist.add_song(self)


class Album:
    def __init__(self, name_album, artist, year):
        self.name_album = name_album
        self.artist = artist
        self.year = year
        self.tracks = []
        artist.add_album(self)

    def add_track(self, title, artist=None):
        if artist is None:
            artist = self.artist

        track_number = len(self.tracks)

        song = Song(title, artist, self, track_number)

        self.tracks.append(song)


class Playlist:
    def __init__(self, name):
        self.name = name
        self.songs = []

    def add_song(self, song):
        self.songs.append(song)


band = Artist("Bob's Awesome Band")
album = Album("Bob's First Single", band, 2013)
album.add_track("A Ballad about Cheese")
album.add_track("A Ballad about Cheese (dance remix)")
album.add_track("A Third Song to Use Up the Rest of the Space")

playlist = Playlist("My Favourite Songs")

for song in album.tracks:
    playlist.add_song(song)

