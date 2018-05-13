from .__init__ import logger
from . import settings
from . import data_list
import os
import xml.etree.cElementTree as ET


def indent(elem, level=0):
    i = "\n" + level*"  "
    if len(elem):
        if not elem.text or not elem.text.strip():
            elem.text = i + "  "
        if not elem.tail or not elem.tail.strip():
            elem.tail = i
        for elem in elem:
            indent(elem, level+1)
        if not elem.tail or not elem.tail.strip():
            elem.tail = i
    else:
        if level and (not elem.tail or not elem.tail.strip()):
            elem.tail = i


def export_xml_data():
    if settings.is_verbose:
        logger.info("Exporting XML data to file")

    music = ET.Element("music")

    for artists in data_list.music_data:

        # artist root node
        artist_node = ET.SubElement(music, "artist")
        artist_node.set('name', artists.get_artist_name())

        # artist albums
        for albums in artists.get_albums():
            album_node = ET.SubElement(artist_node, "album")
            album_node.set('name', albums[0])

            y = ET.SubElement(album_node, "year")
            y.text = albums[1]

            f = ET.SubElement(album_node, "present")
            f.text = ('1' if albums[3] else '0')

    indent(music)

    tree = ET.ElementTree(music)
    tree.write(os.path.join(settings.dataset_folder, '%s.xml' % settings.PROG_NAME), xml_declaration=True, encoding='utf-8', method="xml")

