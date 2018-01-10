###############################################################################
# Copyright 2015 University of Florida. All rights reserved.
# This file is part of the BlueButton.py project.
# Use of this source code is governed by the license found in the LICENSE file.
###############################################################################

from .. import documents


def process(c32):
    """
    Preprocesses the c32 docuemnt
    """
    c32.section = section
    return c32


def section(c32, name):
    """
    Finds the section of a c32 document
    """

    entries = documents.entries

    if 'document' == name:
        return c32.template('2.16.840.1.113883.3.88.11.32.1')
    if 'allergies' == name:
        templateIDs = ['2.16.840.1.113883.3.88.11.83.102',
                       '2.16.840.1.113883.10.20.1.2'
                       ]
        for templateID in templateIDs:
            el = c32.template(templateID)
            if not el.is_empty():
                el.entries = entries
                return el

    if 'demographics' == name:
        return c32.template('2.16.840.1.113883.3.88.11.32.1')
    if 'encounters' == name:
        templateIDs = ['2.16.840.1.113883.3.88.11.83.127',
                       '2.16.840.1.113883.10.20.1.3'
                       ]
        for templateID in templateIDs:
            el = c32.template(templateID)
            if not el.is_empty():
                el.entries = entries
                return el
    if 'immunizations' == name:
        templateIDs = ['2.16.840.1.113883.3.88.11.83.117',
                       '2.16.840.1.113883.10.20.1.6'
                       ]
        for templateID in templateIDs:
            el = c32.template(templateID)
            if not el.is_empty():
                el.entries = entries
                return el

    if 'results' == name:
        templateIDs = ['2.16.840.1.113883.3.88.11.83.122',
                       '2.16.840.1.113883.10.20.1.14'
                       ]
        for templateID in templateIDs:
            el = c32.template(templateID)
            if not el.is_empty():
                el.entries = entries
                return el

    if 'medications' == name:
        templateIDs = ['2.16.840.1.113883.3.88.11.83.112',
                       '2.16.840.1.113883.10.20.1.8'
                       ]
        for templateID in templateIDs:
            el = c32.template(templateID)
            if not el.is_empty():
                el.entries = entries
                return el

    if 'problems' == name:
        templateIDs = ['2.16.840.1.113883.3.88.11.83.103',
                       '2.16.840.1.113883.10.20.1.11'
                       ]
        for templateID in templateIDs:
            el = c32.template(templateID)
            if not el.is_empty():
                el.entries = entries
                return el

    if 'procedures' == name:
        templateIDs = ['2.16.840.1.113883.3.88.11.83.108',
                       '2.16.840.1.113883.10.20.1.12'

                       ]
        for templateID in templateIDs:
            el = c32.template(templateID)
            if not el.is_empty():
                el.entries = entries
                return el

    if 'vitals' == name:
        templateIDs = ['2.16.840.1.113883.3.88.11.83.119',
                       '2.16.840.1.113883.10.20.1.16'
                       ]
        for templateID in templateIDs:
            el = c32.template(templateID)
            if not el.is_empty():
                el.entries = entries
                return el

    return None
