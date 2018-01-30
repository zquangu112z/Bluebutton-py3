###############################################################################
# Copyright 2015 University of Florida. All rights reserved.
# This file is part of the BlueButton.py project.
# Use of this source code is governed by the license found in the LICENSE file.
###############################################################################

"""
Parser for the CCDA functional & cognitive status
"""
from ... import documents
from ...core import wrappers, ccda_enum


def functional_statuses(ccda):
    data = wrappers.ListWrapper()

    statuses = ccda.section('functional_statuses')

    for i, entry in ccda_enum(statuses.entries(), ccda):

        el = entry.tag('effectiveTime')
        start_date, end_date = documents.parse_effectiveTime(el)

        el = entry.tag('value')

        name = el.attr('displayName')
        code = el.attr('code')
        code_system = el.attr('codeSystem')
        code_system_name = el.attr('codeSystemName')

        data.append(wrappers.ObjectWrapper(
            section_title=statuses.tag('title')._element.text,
            date_range=wrappers.ObjectWrapper(
                start=start_date,
                end=end_date
            ),
            entry_index=str(i),
            source_line=entry._element.sourceline,
            name=name,
            code=code,
            code_system=code_system,
            code_system_name=code_system_name
        ))

    return data
