###############################################################################
# Copyright 2015 University of Florida. All rights reserved.
# This file is part of the BlueButton.py project.
# Use of this source code is governed by the license found in the LICENSE file.
###############################################################################

from . import core
from . import documents
import documents.ccda
import parsers.ccda


class BlueButton(object):
    def __init__(self, source, options=None):
        type, parsed_document, parsed_data = None, None, None

        if options is None:
            opts = dict()

        parsed_data = core.parse_data(source)

        if 'parser' in opts:
            parsed_document = opts['parser']()
        else:
            type = documents.detect(parsed_data)

            if 'c32' == type:
                # TODO: add support for legacy C32
                # parsed_data = documents.C32.process(parsed_data)
                # parsed_document = parsers.C32.run(parsed_data)
                pass
            elif 'ccda' == type:
                parsed_data = documents.ccda.process(parsed_data)
                parsed_document = parsers.ccda.run(parsed_data)
            elif 'json' == type:
                # TODO: add support for JSON
                pass

        self.type = type
        self.data = parsed_document
        self.source = parsed_data
