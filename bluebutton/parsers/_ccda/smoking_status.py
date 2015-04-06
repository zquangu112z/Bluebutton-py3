###############################################################################
# Copyright 2015 University of Florida. All rights reserved.
# This file is part of the BlueButton.py project.
# Use of this source code is governed by the license found in the LICENSE file.
###############################################################################

"""
Parser for the CCDA smoking status in social history section
"""

from ...core import wrappers
from ... import documents


def smoking_status(ccda):

    parse_date = documents.parse_date

    social_history = ccda.section('social_history')

    # We can parse all of the social_history sections
    # but in practice, this section seems to be used for
    # smoking status, so we're just going to break that out.
    entry = social_history.template('2.16.840.1.113883.10.20.22.4.78')
    if entry.is_empty():
        entry = social_history.template('2.16.840.1.113883.10.22.4.78')

    el = entry.tag('effectiveTime')
    entry_date = parse_date(el.attr('value'))

    el = entry.tag('value')
    name = el.attr('displayName')
    code = el.attr('code')
    code_system = el.attr('codeSystem')
    code_system_name = el.attr('codeSystemName')

    data = wrappers.ObjectWrapper(
        date=entry_date,
        name=name,
        code=code,
        code_system=code_system,
        code_system_name=code_system_name
    )

    return data