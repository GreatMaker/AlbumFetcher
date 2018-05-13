from .__init__ import logger
from . import music_query
from . import settings

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

    def has_album(self, alb_id):
        ret = 0
        for alb in self.albums:
            if alb_id == alb[2]:
                ret = 1
                break

        return ret


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
        if settings.is_verbose:
            logger.info("Creating artist: %s", artist_name)
        obj = MusicArtist(artist_name, artist_id)
    else:
        obj = music_data[list_index]

    # Set album name if it's not already in
    if obj.has_album(group_id) == 0:
        if settings.is_verbose:
            logger.info("Inserting album: %s for artist: %s", album_name, artist_name)
        obj.set_album(album_name, album_year, group_id, local)

    # Adding object to music_data list at first artist appearence
    if list_index == -1:
        music_data.append(obj)


def process_data():

    # process artists
    for artist_data in music_data:

        a = artist_data.get_artist_id()
        getdata = music_query.get_artist_releases(artist_data.get_artist_id())

        if getdata is not None:
            for releases in getdata:
                insert_entry(artist_data.get_artist_name(), releases[0], artist_data.get_artist_id(), '2000', releases[1], False)
    pass