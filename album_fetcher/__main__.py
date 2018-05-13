from . import settings
from . import data_list
from . import export_xml
from .__init__ import logger, arguments
from os import walk
import taglib

if __name__.endswith('__main__'):
    logger.info("%s started" % settings.PROG_NAME)

    if arguments["--verbose"]:
        logger.info("Verbose mode activated")
        settings.is_verbose = True

    if arguments["<PATH>"]:
        if settings.is_verbose:
            logger.info("Running in the folder: %s" % arguments["<PATH>"])

        # for (dirpath, dirnames, filenames) in walk(settings.dataset_folder):
        for (dirpath, dirnames, filenames) in walk(arguments["<PATH>"]):

            for name in filenames:

                if name[-3:] == "mp3" or name[-3:] == "mp4":

                    if settings.is_verbose:
                        logger.info("Found file: %s in %s", name, dirpath)

                    song = taglib.File(dirpath + "/" + name)

                    if settings.is_verbose:
                        logger.info("Song info: %s", song.tags)

                    abm_artist = song.tags["ALBUMARTIST"][0] if song.tags["ALBUMARTIST"][0] else ''
                    abm_name = song.tags["ALBUM"][0] if song.tags["ALBUM"][0] else ''
                    abm_artistid = song.tags["MUSICBRAINZ_ARTISTID"][0] if song.tags["MUSICBRAINZ_ARTISTID"][0] else ''
                    abm_year = song.tags["ORIGINALYEAR"][0] if song.tags["ORIGINALYEAR"][0] else ''
                    abm_relgroup = song.tags["MUSICBRAINZ_RELEASEGROUPID"][0] if song.tags["MUSICBRAINZ_RELEASEGROUPID"][0] else ''

                    data_list.insert_entry(abm_artist, abm_name, abm_artistid, abm_year, abm_relgroup)

    else:
        print("")
        logger.info("required parameter PATH not passed. abort")

    # process data list by artist and add musicbrainz results
    data_list.process_data()

    # export xml
    export_xml.export_xml_data()
    pass