"""
Script to Export Windows Putty or Kitty terminal sessions to Windows Fluent Terminal
"""
__author__ = "Developed by: Wolfgang Azevedo"
__email__ = "wolgang@ildt.io"
__license__ = "GPL"
__version__ = "1.0"

from winreg import (ConnectRegistry,
                    HKEY_CURRENT_USER,
                    OpenKey,
                    EnumKey,
                    QueryValueEx)


def reg_scanner(**kwargs):

    try:
        if kwargs.get('source') == 'putty':
            parent_key = r"SOFTWARE\SimonTatham\PuTTY\Sessions"
        elif kwargs.get('source') == 'kitty':
            parent_key = r"SOFTWARE\9bis.com\KiTTY\Sessions"
    except Exception as error:
        print(f'Invalid source, please check configuration file or typo... -> {error}')

    parent_reg = ConnectRegistry(None,HKEY_CURRENT_USER)
    parent_key = OpenKey(parent_reg, parent_key)

    for sessions in range(int(kwargs.get('sessions'))):
        try:
            subkey_name=EnumKey(parent_key,sessions)
            subkey=OpenKey(parent_key,subkey_name)
            host=QueryValueEx(subkey, "HostName")
            port=QueryValueEx(subkey, "PortNumber")
            
            yield (subkey_name, host[0], port[0])
        except OSError as error:
            #print(error)
            break