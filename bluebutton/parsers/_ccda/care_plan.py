###############################################################################
# Copyright 2015 University of Florida. All rights reserved.
# This file is part of the BlueButton.py project.
# Use of this source code is governed by the license found in the LICENSE file.
###############################################################################

from bluebutton import core
from ...core import wrappers, ccda_enum


def care_plan(ccda):

    data = []

    care_plan = ccda.section('care_plan')

    for i, entry in ccda_enum(care_plan.entries(), ccda):

        name = None
        code = None
        code_system = None
        code_system_name = None

        # Plan of care encounters, which have no other details
        el = entry.template('2.16.840.1.113883.10.20.22.4.40')
        if not el.is_empty():
            name = 'encounter'
        else:
            el = entry.tag('code')

            name = el.attr('displayName')
            code = el.attr('code')
            code_system = el.attr('codeSystem')
            code_system_name = el.attr('codeSystemName')

        text = core.strip_whitespace(entry.tag('text').val())

        data.append(
            wrappers.ObjectWrapper(
                section_title=care_plan.tag('title')._element.text,
                entry_index=str(i),
                source_line=entry._element.sourceline,
                text=text,
                name=name,
                code=code,
                code_system=code_system,
                code_system_name=code_system_name
            ))

    return wrappers.ListWrapper(data)
