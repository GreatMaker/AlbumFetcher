from . import settings
from .__init__ import logger, arguments
from os import walk
import taglib

is_verbose = False

if __name__.endswith('__main__'):
    logger.info("%s started" % settings.PROG_NAME)

    if arguments["--verbose"]:
        logger.info("Verbose mode activated")
        is_verbose = True

    if arguments["<PATH>"]:
        if is_verbose:
            logger.info("Running in the folder: %s" % arguments["<PATH>"])

        # for (dirpath, dirnames, filenames) in walk(settings.dataset_folder):
        for (dirpath, dirnames, filenames) in walk(arguments["<PATH>"]):

            for name in filenames:

                if name[-3:] == "mp3" or name[-3:] == "mp4":

                    logger.info("Found file: %s in %s", name, dirpath)

                    song = taglib.File(dirpath + "/" + name)
                    logger.info("Song info: %s", song.tags)

    else:
        print("")
        logger.info("required parameter PATH not passed. abort")
