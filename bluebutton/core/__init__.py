###############################################################################
# Copyright 2015 University of Florida. All rights reserved.
# This file is part of the BlueButton.py project.
# Use of this source code is governed by the license found in the LICENSE file.
###############################################################################

import json as std_json
import logging

# from .xml import *
# from ._core import *
from . import xml
from . import _core


# Initialize the logging module
logging.getLogger(__name__).addHandler(logging.NullHandler())


def json():
    raise NotImplementedError()


def parse_data(source):
    try:
        return xml.parse(source)
    except Exception as e:
        raise e

    # source_stripped = strip_whitespace(source)

    # if source_stripped.startswith('<?xml'):
    #     return xml.parse(source)

    # try:
    #     return std_json.loads(source)
    # except:
    #     logging.error(
    #         "Error: Cannot parse this file. BB.js only accepts valid XML (for "
    #         "parsing) or JSON (for generation). If you are attempting to "
    #         "provide XML or JSON, please run your data through a validator to "
    #         "see if it is malformed.\n")
    #     raise


strip_whitespace = _core.strip_whitespace


def trim():
    # I don't think this is needed with the standard JSONEncoder
    raise NotImplementedError()


def ccda_enum(it, ccda):
    for item in it:
        ccda._entry_counter += 1
        yield ccda._entry_counter, item

# __all__ = ('parse_data')
