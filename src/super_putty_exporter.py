'''
Script to Export Windows SuperPutty terminal sessions from XML file to Windows Fluent Terminal
'''
__author__ = "Developed by: Wolfgang Azevedo"
__email__ = "wolgang@ildt.io"
__license__ = "GPL"
__version__ = "1.0"

import xml.etree.ElementTree as ET


def gen_shortcuts(**kwargs):

    try:
        xml = ET.parse(kwargs.get('input_file'))
        root = xml.getroot()

        for session in root.findall('SessionData'): 
            username = session.get("Username")
            session_name = session.get("SessionName")
            hostname = session.get("Host")
            port = session.get("Port")

            yield session_name, hostname, port, username
    except Exception as error:
        print(f'Invalid source, please check configuration file or typo... -> {error}')