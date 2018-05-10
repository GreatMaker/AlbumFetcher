from .__init__ import logger

music_data = []


class MusicArtist:

    def __init__(self, name):
        self.name = name
        self.albums = []

    def get_artist_name(self):
        return self.name

    def set_album(self, album):
        self.albums.append(album)

    def get_albums(self):
        return self.albums


def insert_entry(artist_name, album_name):
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
        obj = MusicArtist(artist_name)
    else:
        obj = music_data[list_index]

    # Set album name
    logger.info("Inserting album: %s for artist: %s", album_name, artist_name)
    obj.set_album(album_name)

    # Adding object to music_data list
    music_data.append(obj)
