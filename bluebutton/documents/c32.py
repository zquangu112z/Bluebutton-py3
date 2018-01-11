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
        el = c32.template('2.16.840.1.113883.3.88.11.83.102')
        if el.is_empty():
            el = c32.template('2.16.840.1.113883.10.20.1.2')
        el.entries = entries
        return el

    # @TODO this section is not avail in C32 format. However, try to parse it
    if 'care_plan' == name:
        el = c32.template('2.16.840.1.113883.10.20.22.2.10')
        el.entries = entries
        return el

    # @TODO this section is not avail in C32 format. However, try to parse it
    if 'chief_complaint' == name:
        el = c32.template('2.16.840.1.113883.10.20.22.2.13')
        if el.is_empty():
            el = c32.template('1.3.6.1.4.1.19376.1.5.3.1.1.13.2.1')
        # no entries in Chief Complaint
        return el

    if 'demographics' == name:
        return c32.template('2.16.840.1.113883.3.88.11.32.1')

    if 'encounters' == name:
        el = c32.template('2.16.840.1.113883.3.88.11.83.127')
        if el.is_empty():
            el = c32.template('2.16.840.1.113883.10.20.1.3')
        el.entries = entries
        return el

    # @TODO this section is not avail in C32 format. However, try to parse it
    if 'functional_statuses' == name:
        el = c32.template('2.16.840.1.113883.10.20.22.2.14')
        el.entries = entries
        return el

    if 'immunizations' == name:
        el = c32.template('2.16.840.1.113883.3.88.11.83.117')
        if el.is_empty():
            el = c32.template('2.16.840.1.113883.10.20.1.6')
        el.entries = entries
        return el

    # @TODO this section is not avail in C32 format. However, try to parse it
    if 'instructions' == name:
        el = c32.template('2.16.840.1.113883.10.20.22.2.45')
        el.entries = entries
        return el

    if 'results' == name:
        el = c32.template('2.16.840.1.113883.3.88.11.83.122')
        if el.is_empty():
            el = c32.template('2.16.840.1.113883.10.20.1.14')
        el.entries = entries
        return el

    if 'medications' == name:
        el = c32.template('2.16.840.1.113883.3.88.11.83.112')
        if el.is_empty():
            el = c32.template('2.16.840.1.113883.10.20.1.8')
        el.entries = entries
        return el

    if 'problems' == name:
        el = c32.template('2.16.840.1.113883.3.88.11.83.103')
        if el.is_empty():
            el = c32.template('2.16.840.1.113883.10.20.1.11')
        el.entries = entries
        return el

    if 'procedures' == name:
        el = c32.template('2.16.840.1.113883.3.88.11.83.108')
        if el.is_empty():
            el = c32.template('2.16.840.1.113883.10.20.1.12')
        el.entries = entries
        return el

    # @TODO this section is not avail in C32 format. However, try to parse it
    if 'social_history' == name:
        el = c32.template('2.16.840.1.113883.10.20.22.2.17')
        el.entries = entries
        return el

    if 'vitals' == name:
        el = c32.template('2.16.840.1.113883.3.88.11.83.119')
        if el.is_empty():
            el = c32.template('2.16.840.1.113883.10.20.1.16')
        el.entries = entries
        return el

    return None
