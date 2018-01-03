###############################################################################
# Copyright 2015 University of Florida. All rights reserved.
# This file is part of the BlueButton.py project.
# Use of this source code is governed by the license found in the LICENSE file.
###############################################################################

def strip_whitespace(text):
    """ Remove leading and trailing whitespace from a string """
    if not isinstance(text, str):
        return text
    return text.strip()
