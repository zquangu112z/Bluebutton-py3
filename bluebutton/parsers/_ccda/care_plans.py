###############################################################################
# Copyright 2015 University of Florida. All rights reserved.
# This file is part of the BlueButton.py project.
# Use of this source code is governed by the license found in the LICENSE file.
###############################################################################

from ...core import wrappers, ccda_enum, strip_whitespace
from ... import documents


def care_plans(ccda):

    data = []

    care_plans = ccda.section('care_plans')

    for i, entry in ccda_enum(care_plans.entries(), ccda):

        name = None
        code = None
        code_system = None
        code_system_name = None

        el = entry.tag('code')
        name = el.attr('displayName')
        code = el.attr('code')
        code_system = el.attr('codeSystem')
        code_system_name = el.attr('codeSystemName')

        text = strip_whitespace(entry.tag('text').val())

        el = entry.tag('effectiveTime')
        start_date, end_date = documents.parse_effectiveTime(el)

        # Parse entryRelationship parts
        findings = documents.parse_findings(entry, start_date, end_date)

        data.append(
            wrappers.ObjectWrapper(
                section_title=care_plans.tag('title')._element.text,
                date_range=wrappers.ObjectWrapper(
                    start=start_date,
                    end=end_date
                ),
                findings=findings,
                entry_index=str(i),
                source_line=entry._element.sourceline,
                text=text,
                name=name,
                code=code,
                code_system=code_system,
                code_system_name=code_system_name
            ))

    return wrappers.ListWrapper(data)
