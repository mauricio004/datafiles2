__author__ = 'MFlores1'


class Playlist:
    def __init__(self, name):
        self.name = name
        self.playlist_tracks = []

    def add_song(self, song):
        self.playlist_tracks.append(song)


class Album:
    def __init__(self, name, artist, year):
        self.name = name
        self.artist = artist
        self.year = year
        self.tracks = []

    def add_track(self, song):
        self.tracks.append(song)


class Song:
    def __init__(self, name, artist, album, track_number):
        self.name = name
        self.artist = artist
        self.album = album
        self.track_number = track_number


class Artist:
    def __init__(self, name):
        self.name = name
        self.albums = []
        self.songs = []

    def add_album(self, album):
        self.albums.append(album)

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