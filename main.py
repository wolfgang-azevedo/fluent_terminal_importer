'''
Script to import terminal Sessions from Putty, Kitty or SuperPutty to
Fluent Terminal on Microsoft Windows.
'''
__author__ = "Developed by: Wolfgang Azevedo"
__email__ = "wolgang@ildt.io"
__license__ = "GPL"
__version__ = "1.0"

import os
import yaml
import argparse
from src import putty_exporter
from src import super_putty_exporter

parser = argparse.ArgumentParser()
parser.add_argument("-c", "--config", default='config.yml', help="set configuration file")
args = parser.parse_args()

try:
    with open(args.config, 'r') as config_file:
        config = yaml.safe_load(config_file)
except FileNotFoundError as error:
    print(f'Configuration file not found! Please check --> {error}....')


def export_sessions(**kwargs):


    def gen_files(**kwargs):

        try:
            source_app = kwargs.get('source')
            session_name = kwargs.get("values")[0]
            hostname = kwargs.get("values")[1]
            port = kwargs.get("values")[2]
            dest_dir = config['importer']['output_dir']
            dest_dir = f'{dest_dir}\\{source_app}'
            tab_color = config["importer"]["tab_color"]

            if kwargs.get('values')[3] == '':
                username = config["importer"]["username"]
            else:
                username = kwargs.get('values')[3]

            if not os.path.exists(dest_dir):
                os.makedirs(dest_dir)

            path = os.path.join(dest_dir, f'{session_name}.url')
            target = f'ssh://{username}@{hostname}:{port}/?conpty=True&buffer=True&tab={tab_color}'

            shortcut = open(path, 'w')
            shortcut.write('[InternetShortcut]\n')
            shortcut.write('URL=%s' % target)
            shortcut.close()

            print(f'Session: {kwargs.get("values")[0]}, username: {username} has been exported succesfully!')
        except OSError as error:
            print(error)

    if kwargs.get('source') == 'putty' or kwargs.get('source') == 'kitty':
        for values in putty_exporter.reg_scanner(source=kwargs.get('source_app'), sessions=config['importer']['max_sessions']):
            gen_files(values=values, source=kwargs.get('source'))

    elif kwargs.get('source') == 'super_putty':
        for values in super_putty_exporter.gen_shortcuts(input_file=config['importer']['source']['super_putty']['input_file']):
            gen_files(values=values, source=kwargs.get('source'))

for sources in config['importer']['source']:
    if sources == 'putty' or sources == 'kitty':
        if config['importer']['source'][sources]['enabled'] is True:
            source = sources
            export_sessions(source_app=source, source=source)
    elif sources == 'super_putty':
        if config['importer']['source'][sources]['enabled'] is True:
            source = sources
            export_sessions(source=source)