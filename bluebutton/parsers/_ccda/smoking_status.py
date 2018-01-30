###############################################################################
# Copyright 2015 University of Florida. All rights reserved.
# This file is part of the BlueButton.py project.
# Use of this source code is governed by the license found in the LICENSE file.
###############################################################################

"""
Parser for the CCDA smoking status in social history section
"""

from ...core import wrappers, ccda_enum
from ... import documents


def smoking_status(ccda):
    name = None
    code = None
    code_system = None
    code_system_name = None

    # We can parse all of the social_history sections
    # but in practice, this section seems to be used for
    # smoking status, so we're just going to break that out.
    data = wrappers.ListWrapper()
    social_history = ccda.section('social_history')
    entries = social_history.entries()
    for i, entry in ccda_enum(entries, ccda):

        smoking_status_ = entry.template('2.16.840.1.113883.10.20.22.4.78')
        if smoking_status_.is_empty():
            smoking_status_ = entry.template('2.16.840.1.113883.10.22.4.78')

        if smoking_status_.is_empty():
            continue

        el = smoking_status_.tag('effectiveTime')
        start_date, end_date = documents.parse_effectiveTime(el)

        el = smoking_status_.tag('value')
        source_line = el._element.sourceline
        name = el.attr('displayName')
        code = el.attr('code')
        code_system = el.attr('codeSystem')
        code_system_name = el.attr('codeSystemName')

        data.append(wrappers.ObjectWrapper(
            section_title=social_history.tag('title')._element.text,
            date_range=wrappers.ObjectWrapper(
                start=start_date,
                end=end_date
            ),
            entry_index=str(i),
            source_line=source_line,
            name=name,
            code=code,
            code_system=code_system,
            code_system_name=code_system_name
        ))

    return data
