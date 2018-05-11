from .__init__ import logger
from . import music_query

music_data = []


class MusicArtist:

    def __init__(self, name, id):
        self.name = name
        self.ID = id
        self.albums = []

    def get_artist_name(self):
        return self.name

    def get_artist_id(self):
        return self.ID

    def set_album(self, album, year, group_id, local):
        abm = (album, year, group_id, local)
        self.albums.append(abm)

    def get_albums(self):
        return self.albums


def insert_entry(artist_name, album_name, artist_id, album_year, group_id, local=True):
    list_index = -1
    cnt = 0
    obj = None

    # walk list to check if artist is already in
    for artist in music_data:
        if artist.get_artist_name() == artist_name:
            list_index = cnt
            break
        cnt = cnt + 1

    # Create artist or use the existing one
    if list_index == -1:
        logger.info("Creating artist: %s", artist_name)
        obj = MusicArtist(artist_name, artist_id)
    else:
        obj = music_data[list_index]

    # Set album name if it's not already in
    if (album_name, album_year, group_id, local) not in obj.get_albums():
        logger.info("Inserting album: %s for artist: %s", album_name, artist_name)
        obj.set_album(album_name, album_year, group_id, local)

    # Adding object to music_data list at first artist appearence
    if list_index == -1:
        music_data.append(obj)


def process_data():

    # process artists
    for artist_data in music_data:
        print(artist_data.get_artist_name())
        getdata = music_query.get_artist_releases(artist_data.get_artist_id())
    pass
