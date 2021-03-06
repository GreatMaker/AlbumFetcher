from .__init__ import logger
import musicbrainzngs

musicbrainzngs.set_useragent("AlbumFetcher", "0.1", "https://github.com/GreatMaker/AlbumFetcher")


def get_artist_releases(artist_id):
    music_data = []
    try:
        result = musicbrainzngs.get_artist_by_id(artist_id, includes=["release-groups"], release_type=["album", "ep"])

        for release_group in result["artist"]["release-group-list"]:
            music_data.append((release_group["title"], release_group["id"], release_group["first-release-date"]))
    except musicbrainzngs.WebServiceError as exc:
        logger.error("Something went wrong with the request: %s" % exc)
        return None

    return music_data
