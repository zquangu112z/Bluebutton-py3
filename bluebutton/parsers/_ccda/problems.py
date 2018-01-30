###############################################################################
# Copyright 2015 University of Florida. All rights reserved.
# This file is part of the BlueButton.py project.
# Use of this source code is governed by the license found in the LICENSE file.
###############################################################################

"""
Parser for the CCDA problems section
"""

from ...core import wrappers, ccda_enum, strip_whitespace
from ... import documents


def problems(ccda):
    data = wrappers.ListWrapper()

    problems = ccda.section('problems')

    for i, problem_entry in ccda_enum(problems.entries(), ccda):

        entry = problem_entry.tag('act')
        el = entry.tag('effectiveTime')
        start_date, end_date = documents.parse_effectiveTime(el)

        el = entry.tag('code')
        name = el.attr('displayName')
        code = el.attr('code')
        code_system = el.attr('codeSystem')
        code_system_name = el.attr('codeSystemName')

        # Parse entryRelationship parts
        findings = documents.parse_findings(entry, start_date, end_date)

        data.append(wrappers.ObjectWrapper(
            section_title=problems.tag('title')._element.text,
            date_range=wrappers.ObjectWrapper(
                start=start_date,
                end=end_date
            ),
            entry_index=str(i),
            findings=findings,
            source_line=entry._element.sourceline,
            name=name,
            code=code,
            code_system=code_system,
            code_system_name=code_system_name
        ))

    return data


'''
Original code
'''
# def problems(ccda):

#     parse_date = documents.parse_date
#     data = wrappers.ListWrapper()

#     problems = ccda.section('problems')

#     for entry in problems.entries():

#         el = entry.tag('effectiveTime')
#         start_date = parse_date(el.tag('low').attr('value'))
#         end_date = parse_date(el.tag('high').attr('value'))

#         el = entry.template('2.16.840.1.113883.10.20.22.4.4').tag('value')
#         name = el.attr('displayName')
#         code = el.attr('code')
#         code_system = el.attr('codeSystem')
#         code_system_name = el.attr('codeSystemName')

#         el = entry.template('2.16.840.1.113883.10.20.22.4.4').tag('translation')
#         translation_name = el.attr('displayName')
#         translation_code = el.attr('code')
#         translation_code_system = el.attr('codeSystem')
#         translation_code_system_name = el.attr('codeSystemName')

#         el = entry.template('2.16.840.1.113883.10.20.22.4.6')
#         status = el.tag('value').attr('displayName')

#         age = None
#         el = entry.template('2.16.840.1.113883.10.20.22.4.31')
#         if not el.is_empty():
#             age = wrappers.parse_number(el.tag('value').attr('value'))

#         el = entry.template('2.16.840.1.113883.10.20.22.4.64')
#         comment = core.strip_whitespace(el.tag('text').val())

#         data.append(wrappers.ObjectWrapper(
#             date_range=wrappers.ObjectWrapper(
#                 start=start_date,
#                 end=end_date
#             ),
#             name=name,
#             status=status,
#             age=age,
#             code=code,
#             code_system=code_system,
#             code_system_name=code_system_name,
#             translation=wrappers.ObjectWrapper(
#                 name=translation_name,
#                 code=translation_code,
#                 code_system=translation_code_system,
#                 code_system_name=translation_code_system_name
#             ),
#             comment=comment
#         ))

#     return data
