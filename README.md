# Fluent Terminal Importer (Putty, Kitty and SuperPutty)

This script was created to help session migration from Putty, Kitty and SuperPutty to the brand new Windows Fluent Terminal.

# Requirments

- System Requirments

    - Latest version of Microsoft Windows
    - Latest version of Fluent Terminal for Microsoft Windows installed
    - Python3.7+ (script was developed using Python3.8, but you can run with 3.7x) for Microsoft Windows

- Dependencies, you can run the following command:

      $ pip3 - r requirements
     
# Configuration

- To use this script you must set some parameter in config.yml configuration file as per sample below:

      ---
      importer:
        output_dir: 'output' # Define the output path, default is the output folder of the script
        max_sessions: 500 # Number of sessions to search for Putty or Kitty
        username: jsnow # Set the default username for the session, if no username or if empty
        tab_color: 6 # [default: 0, red: 1, green: 2, blue: 3, purple: 4, orange: 5, aquamarine: 6]
        source: # Change chose the source and set True on enabled parameter, you can set multiples
          putty: 
            enabled: False
          kitty: 
            enabled: False
          super_putty:
            enabled: True
            input_file: 'all_sessions.xml' # Change for your SuperPutty exported sessions XML file
