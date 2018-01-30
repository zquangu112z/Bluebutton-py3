###############################################################################
# Copyright 2015 University of Florida. All rights reserved.
# This file is part of the BlueButton.py project.
# Use of this source code is governed by the license found in the LICENSE file.
###############################################################################

"""
Parser for the CCDA vitals section
"""

from ...core import wrappers, ccda_enum
from ... import documents


def vitals(ccda):
    data = wrappers.ListWrapper()

    vitals = ccda.section('vitals')

    for entry in vitals.entries():

        el = entry.tag('effectiveTime')
        start_date, end_date = documents.parse_effectiveTime(el)

        results = entry.els_by_tag('component')
        results_data = wrappers.ListWrapper()

        for i, result in ccda_enum(results, ccda):
            el = result.tag('code')
            name = el.attr('displayName')
            code = el.attr('code')
            code_system = el.attr('codeSystem')
            code_system_name = el.attr('codeSystemName')

            el = result.tag('value')
            value = wrappers.parse_number(el.attr('value'))
            unit = el.attr('unit')

            results_data.append(wrappers.ObjectWrapper(
                section_title=vitals.tag('title')._element.text,
                source_line=result._element.sourceline,
                date_range=wrappers.ObjectWrapper(
                    start=start_date,
                    end=end_date
                ),
                entry_index=str(i),
                name=name,
                code=code,
                code_system=code_system,
                code_system_name=code_system_name,
                value=value,
                unit=unit
            ))

        data.append(wrappers.ObjectWrapper(
            results=results_data
        ))

    return data
