#
# main.py
#
# Copyright (C) 2007 Andrew Resch ('andar') <andrewresch@gmail.com>
# 
# Deluge is free software.
# 
# You may redistribute it and/or modify it under the terms of the
# GNU General Public License, as published by the Free Software
# Foundation; either version 2 of the License, or (at your option)
# any later version.
# 
# deluge is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.
# See the GNU General Public License for more details.
# 
# You should have received a copy of the GNU General Public License
# along with deluge.    If not, write to:
# 	The Free Software Foundation, Inc.,
# 	51 Franklin Street, Fifth Floor
# 	Boston, MA    02110-1301, USA.
#
#    In addition, as a special exception, the copyright holders give
#    permission to link the code of portions of this program with the OpenSSL
#    library.
#    You must obey the GNU General Public License in all respects for all of
#    the code used other than OpenSSL. If you modify file(s) with this
#    exception, you may extend this exception to your version of the file(s),
#    but you are not obligated to do so. If you do not wish to do so, delete
#    this exception statement from your version. If you delete this exception
#    statement from all source files in the program, then also delete it here.

# The main starting point for the program.    This function is called when the 
# user runs the command 'deluge'.

"""Main starting point for Deluge.  Contains the main() entry point."""

import os
from optparse import OptionParser

import deluge.common

def start_ui():
    """Entry point for ui script"""
    # Setup the argument parser
    parser = OptionParser(usage="%prog [options] [actions]", 
                                           version=deluge.common.get_version())

    # Get the options and args from the OptionParser
    (options, args) = parser.parse_args()

    from deluge.log import LOG as log

    log.info("Deluge ui %s", deluge.common.get_version())        
    log.debug("options: %s", options)
    log.debug("args: %s", args)

    from deluge.ui.ui import UI
    log.info("Starting ui..")
    UI(args)
                                                      
def start_daemon():
    """Entry point for daemon script"""
    # Setup the argument parser
    parser = OptionParser(usage="%prog [options] [actions]", 
                                           version=deluge.common.get_version())
    parser.add_option("-p", "--port", dest="port", 
        help="Port daemon will listen on", action="store", type="int")

    # Get the options and args from the OptionParser
    (options, args) = parser.parse_args()

    from deluge.log import LOG as log
    
    log.info("Deluge daemon %s", deluge.common.get_version())        
    log.debug("options: %s", options)
    log.debug("args: %s", args)

    from deluge.core.daemon import Daemon
            
    log.info("Starting daemon..")
    pid = os.fork()
    if not pid:
        Daemon(options.port)
