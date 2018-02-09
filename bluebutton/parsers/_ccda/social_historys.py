###############################################################################
# Copyright 2015 University of Florida. All rights reserved.
# This file is part of the BlueButton.py project.
# Use of this source code is governed by the license found in the LICENSE file.
###############################################################################

"""
Parser for the CCDA social history section
"""

from ...core import wrappers, ccda_enum
from ... import documents


# @TODO: rename this method to social_history
def social_historys(ccda):
    name = None
    code = None
    code_system = None
    code_system_name = None

    data = wrappers.ListWrapper()
    social_historys = ccda.section('social_historys')
    entries = social_historys.entries()
    for i, entry in ccda_enum(entries, ccda):

        observation = entry.tag("observation")

        el = observation.tag('effectiveTime')
        start_date, end_date = documents.parse_effectiveTime(el)

        el = observation.tag('code')
        source_line = el._element.sourceline
        name = el.attr('displayName')
        code = el.attr('code')
        code_system = el.attr('codeSystem')
        code_system_name = el.attr('codeSystemName')

        el = observation.tag('value')
        value = el.attr('displayName')

        data.append(wrappers.ObjectWrapper(
            section_title=social_historys.tag('title')._element.text,
            date_range=wrappers.ObjectWrapper(
                start=start_date,
                end=end_date
            ),
            entry_index=str(i),
            source_line=source_line,
            name=name,
            code=code,
            code_system=code_system,
            code_system_name=code_system_name,
            value=value,
            unit=None
        ))

    return data
