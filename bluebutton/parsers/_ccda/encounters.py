###############################################################################
# Copyright 2015 University of Florida. All rights reserved.
# This file is part of the BlueButton.py project.
# Use of this source code is governed by the license found in the LICENSE file.
###############################################################################

"""
Parser for the CCDA encounters section
"""

from ...core import wrappers, ccda_enum
from ...documents import parse_address, parse_date


def encounters(ccda):

    data = []

    encounters = ccda.section('encounters')

    for i, entry in ccda_enum(encounters.entries(), ccda):

        date = parse_date(entry.tag('effectiveTime').attr('value'))

        el = entry.tag('code')
        name = el.attr('displayName')
        code = el.attr('code')
        code_system = el.attr('codeSystem')
        code_system_name = el.attr('codeSystemName')
        code_system_version = el.attr('codeSystemVersion')

        # translation
        translations = []
        for el in entry.els_by_tag('translation'):
            translations.append(wrappers.ObjectWrapper(
                name=el.attr('displayName'),
                code=el.attr('code'),
                code_system=el.attr('codeSystem'),
                code_system_name=el.attr('codeSystemName')
            ))

        # performer
        el = entry.tag('performer').tag('code')
        performer_name = el.attr('displayName')
        performer_code = el.attr('code')
        performer_code_system = el.attr('codeSystem')
        performer_code_system_name = el.attr('codeSystemName')

        # participant => location
        el = entry.tag('participant')
        organization = el.tag('code').attr('displayName')

        location_dict = parse_address(el)
        location_dict.organization = organization

        # findings
        findings = []
        findings_els = entry.els_by_tag('entryRelationship')
        for current in findings_els:
            el = current.tag('value')
            findings.append(wrappers.ObjectWrapper(
                name=el.attr('displayName'),
                code=el.attr('code'),
                code_system=el.attr('codeSystem'),
            ))

        data.append(wrappers.ObjectWrapper(
            section_title=encounters.tag('title')._element.text,
            source_line=entry._element.sourceline,
            date=date,
            date_range=wrappers.ObjectWrapper(
                start=date,
                end=date
            ),
            entry_index=str(i),
            name=name,
            code=code,
            code_system=code_system,
            code_system_name=code_system_name,
            code_system_version=code_system_version,
            findings=findings,
            translations=translations,
            performer=wrappers.ObjectWrapper(
                name=performer_name,
                code=performer_code,
                code_system=performer_code_system,
                code_system_name=performer_code_system_name
            ),
            location=location_dict
        ))

    return wrappers.ListWrapper(data)
