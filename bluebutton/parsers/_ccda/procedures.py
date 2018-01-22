###############################################################################
# Copyright 2015 University of Florida. All rights reserved.
# This file is part of the BlueButton.py project.
# Use of this source code is governed by the license found in the LICENSE file.
###############################################################################

"""
Parser for the CCDA procedures section
"""

from ...core import wrappers
from ... import core
from ... import documents


def procedures(ccda):

    parse_date = documents.parse_date
    parse_address = documents.parse_address
    data = wrappers.ListWrapper()

    procedures = ccda.section('procedures')

    for entry in procedures.entries():

        el = entry.tag('effectiveTime')
        date = parse_date(el.attr('value'))

        el = entry.tag('code')
        name = el.attr('displayName')
        code = el.attr('code')
        code_system = el.attr('codeSystem')
        code_system_name = el.attr('codeSystemName')

        if not name:
            # if we'd like to get content only, use val() instead
            name = core.strip_whitespace(
                entry.tag('originalText').val_tostring())

        el = entry.tag('code').tag('translation')
        translation_name = el.attr('displayName')
        translation_code = el.attr('code')
        translation_code_system = el.attr('codeSystem')
        translation_code_system_name = el.attr('codeSystemName')

        # 'specimen' tag not always present
        specimen_name = None
        specimen_code = None
        specimen_code_system = None

        el = entry.tag('performer').tag('addr')
        organization = el.tag('name').val()
        phone = el.tag('telecom').attr('value')

        performer_dict = parse_address(el)
        performer_dict.organization = organization
        performer_dict.phone = phone

        # participant => device
        el = entry.template('2.16.840.1.113883.10.20.22.4.37').tag('code')
        device_name = el.attr('displayName')
        device_code = el.attr('code')
        device_code_system = el.attr('codeSystem')

        data.append(wrappers.ObjectWrapper(
            section_title=procedures.tag('title')._element.text,
            source_line=entry._element.sourceline,
            date=date,
            name=name,
            code=code,
            code_system=code_system,
            code_system_name=code_system_name,
            translation=wrappers.ObjectWrapper(
                    name=translation_name,
                    code=translation_code,
                    code_system=translation_code_system,
                    code_system_name=translation_code_system_name
                    ),
            specimen=wrappers.ObjectWrapper(
                name=specimen_name,
                code=specimen_code,
                code_system=specimen_code_system
            ),
            performer=performer_dict,
            device=wrappers.ObjectWrapper(
                name=device_name,
                code=device_code,
                code_system=device_code_system
            )
        ))

    return data
