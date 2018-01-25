###############################################################################
# Copyright 2015 University of Florida. All rights reserved.
# This file is part of the BlueButton.py project.
# Use of this source code is governed by the license found in the LICENSE file.
###############################################################################

"""
Parser for the CCDA results (labs) section
"""
from ...core import wrappers
from ... import core
from ... import documents


def results(ccda):

    parse_date = documents.parse_date
    data = wrappers.ListWrapper()

    results = ccda.section('results')

    for i, entry in enumerate(results.entries()):

        # panel
        el = entry.tag('code')
        panel_name = el.attr('displayName')
        panel_code = el.attr('code')
        panel_code_system = el.attr('codeSystem')
        panel_code_system_name = el.attr('codeSystemName')

        # observation
        tests = entry.els_by_tag('observation')
        tests_data = wrappers.ListWrapper()

        for observation in tests:

            date = parse_date(observation.tag('effectiveTime').attr('value'))

            el = observation.tag('code')
            name = el.attr('displayName')
            code = el.attr('code')
            code_system = el.attr('codeSystem')
            code_system_name = el.attr('codeSystemName')

            if not name:
                # if we'd like to get content only, use val() instead
                name = core.strip_whitespace(
                    observation.tag('text').val_tostring())

            el = observation.tag('translation')
            translation_name = el.attr('displayName')
            translation_code = el.attr('code')
            translation_code_system = el.attr('codeSystem')
            translation_code_system_name = el.attr('codeSystemName')

            el = observation.tag('value')
            # value = el.attr('value')  # old code
            # unit = el.attr('unit')
            # if el.val() is not None and el.attr('unit') is None and el.attr("xsi:type") in documents.unstructerdValueTypes :
            if el.attr("xsi:type") in documents.unstructerdValueTypes and \
                    el.val() is not None:
                # manual parse value tag
                value, unit = documents.extractUnit(el.val())
            else:
                value = el.attr('value')
                unit = el.attr('unit')

            # old code
            # We could look for xsi:type="PQ" (physical quantity) but it seems
            # better not to trust that that field has been used correctly...
            # if value and wrappers.parse_number(value):
            #     value = wrappers.parse_number(value)

            if not value:
                value = el.val()  # look for free-text values

            el = observation.tag('referenceRange')
            reference_range_text = core.strip_whitespace(
                el.tag('observationRange').tag('text').val())
            reference_range_low_unit = el.tag(
                'observationRange').tag('low').attr('unit')
            reference_range_low_value = el.tag(
                'observationRange').tag('low').attr('value')
            reference_range_high_unit = el.tag(
                'observationRange').tag('high').attr('unit')
            reference_range_high_value = el.tag(
                'observationRange').tag('high').attr('value')

            tests_data.append(wrappers.ObjectWrapper(
                section_title=results.tag('title')._element.text,
                source_line=observation._element.sourceline,
                date=date,
                entry_index=str(i),
                name=name,
                value=value,
                unit=unit,
                code=code,
                code_system=code_system,
                code_system_name=code_system_name,
                translation=wrappers.ObjectWrapper(
                    name=translation_name,
                    code=translation_code,
                    code_system=translation_code_system,
                    code_system_name=translation_code_system_name
                ),
                reference_range=wrappers.ObjectWrapper(
                    text=reference_range_text,
                    low_unit=reference_range_low_unit,
                    low_value=reference_range_low_value,
                    high_unit=reference_range_high_unit,
                    high_value=reference_range_high_value
                )
            ))

        data.append(wrappers.ObjectWrapper(
            name=panel_name,
            code=panel_code,
            code_system=panel_code_system,
            code_system_name=panel_code_system_name,
            tests=tests_data
        ))

    return data
