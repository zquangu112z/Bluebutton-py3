###############################################################################
# Copyright 2015 University of Florida. All rights reserved.
# This file is part of the BlueButton.py project.
# Use of this source code is governed by the license found in the LICENSE file.
###############################################################################

"""
Parser for the CCDA functional & cognitive status
"""
from ... import documents
from ...core import wrappers


def functional_statuses(ccda):

    parse_date = documents.parse_date
    data = wrappers.ListWrapper()

    statuses = ccda.section('functional_statuses')

    for entry in statuses.entries():

        date = parse_date(entry.tag('effectiveTime').attr('value'))

        if not date:
            date = parse_date(entry.tag('effectiveTime').tag('low').attr('value'))

        el = entry.tag('value')

        name = el.attr('displayName')
        code = el.attr('code')
        code_system = el.attr('codeSystem')
        code_system_name = el.attr('codeSystemName')

        data.append(wrappers.ObjectWrapper(
            date=date,
            name=name,
            code=code,
            code_system=code_system,
            code_system_name=code_system_name
        ))

    return data
