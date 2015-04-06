###############################################################################
# Copyright 2015 University of Florida. All rights reserved.
# This file is part of the BlueButton.py project.
# Use of this source code is governed by the license found in the LICENSE file.
###############################################################################

"""
Parser for any freetext section (i.e., contains just a single <text> element)
"""
from ... import core
from bluebutton.core import wrappers


def free_text(ccda, section_name):

    doc = ccda.section(section_name)
    text = core.strip_whitespace(doc.tag('text').val())

    return wrappers.ObjectWrapper(
        text=text
    )