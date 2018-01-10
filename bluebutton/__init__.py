###############################################################################
# Copyright 2015 University of Florida. All rights reserved.
# This file is part of the BlueButton.py project.
# Use of this source code is governed by the license found in the LICENSE file.
###############################################################################

from . import core
from . import documents
from . import parsers
import logging
# import documents.ccda
# import parsers.ccda

__version__ = '0.4.1'


class BlueButton(object):
    def __init__(self, source, options=None):
        cdaType, parsed_document, parsed_data = None, None, None

        if options is None:
            opts = dict()

        # parsed_data is an instance of core/xml.py/_Element
        parsed_data = core.parse_data(source)

        logging.info('Init BlueButton')
        if 'parser' in opts:
            logging.info('Init BlueButton in parser')
            parsed_document = opts['parser']()
        else:
            cdaType = documents.detect(parsed_data)
            if 'c32' == cdaType:
                logging.info("c32 format")
                try:
                    parsed_data = documents.c32.process(parsed_data)
                except Exception as e:
                    logging.warning(e)
                    raise e

                # @TODO: add specific parser for C32
                try:
                    parsed_document = parsers.ccda.run(parsed_data)
                except Exception as e:
                    logging.warning(e)
                    raise e
            elif 'ccda' == cdaType:
                logging.warning("ccda")
                parsed_data = documents.ccda.process(parsed_data)
                parsed_document = parsers.ccda.run(parsed_data)
            elif 'json' == cdaType:
                logging.warning("json")
                # @TODO: add support for JSON
                pass
            else:
                logging.warning(cdaType)

        self.type = cdaType
        self.data = parsed_document
        self.source = parsed_data
