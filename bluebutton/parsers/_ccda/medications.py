###############################################################################
# Copyright 2015 University of Florida. All rights reserved.
# This file is part of the BlueButton.py project.
# Use of this source code is governed by the license found in the LICENSE file.
###############################################################################

"""
Parser for the CCDA medications section
"""

from ...core import wrappers, ccda_enum, strip_whitespace
from ... import documents


def medications(ccda):
    data = wrappers.ListWrapper()

    medications = ccda.section('medications')

    for i, entry in ccda_enum(medications.entries(), ccda):

        el = entry.tag('text')
        sig = strip_whitespace(el.val())

        effective_times = entry.els_by_tag('effectiveTime')

        # the first effectiveTime is the med start date
        try:
            el = effective_times[0]
        except IndexError:
            el = None
        start_date = None
        end_date = None
        if el:
            start_date, end_date = documents.parse_effectiveTime(el)

        # the second effectiveTime might the schedule period or it might just
        # be a random effectiveTime from further in the entry... xsi:type
        # should tell us
        try:
            el = effective_times[1]
        except IndexError:
            el = None
        schedule_type = None
        schedule_period_value = None
        schedule_period_unit = None
        if el and el.attr('xsi:type') == 'PIVL_TS':
            institution_specified = el.attr('institutionSpecified')
            if institution_specified == 'true':
                schedule_type = 'frequency'
            elif institution_specified == 'false':
                schedule_type = 'interval'

            el = el.tag('period')
            schedule_period_value = el.attr('value')
            schedule_period_unit = el.attr('unit')

        el = entry.tag('manufacturedProduct').tag('code')
        product_name = el.attr('displayName')
        product_code = el.attr('code')
        product_code_system = el.attr('codeSystem')

        product_original_text = None
        el = entry.tag('manufacturedProduct').tag('originalText')
        if not el.is_empty():
            # if we'd like to get content only, use val() instead
            product_original_text = strip_whitespace(el.val_tostring())
        # if we don't have a product name yet, try the originalText version
        if not product_name and product_original_text:
            product_name = product_original_text

        translations = []
        for el in entry.tag('manufacturedProduct').els_by_tag('translation'):
            translations.append(wrappers.ObjectWrapper(
                name=el.attr('displayName'),
                code=el.attr('code'),
                code_system=el.attr('codeSystem'),
                code_system_name=el.attr('codeSystemName')
            ))

        el = entry.tag('doseQuantity')
        dose_value = el.attr('value')
        dose_unit = el.attr('unit')

        el = entry.tag('rateQuantity')
        rate_quantity_value = el.attr('value')
        rate_quantity_unit = el.attr('unit')

        el = entry.tag('precondition').tag('value')
        precondition_name = el.attr('displayName')
        precondition_code = el.attr('code')
        precondition_code_system = el.attr('codeSystem')

        el = entry.template('2.16.840.1.113883.10.20.22.4.19').tag('value')
        reason_name = el.attr('displayName')
        reason_code = el.attr('code')
        reason_code_system = el.attr('codeSystem')

        el = entry.tag('routeCode')
        route_name = el.attr('displayName')
        route_code = el.attr('code')
        route_code_system = el.attr('codeSystem')
        route_code_system_name = el.attr('codeSystemName')

        # participant/playingEntity => vehicle
        el = entry.tag('participant').tag('playingEntity')
        vehicle_name = el.tag('name').val()

        el = el.tag('code')
        # prefer the code vehicle_name but fall back to the non-coded one
        vehicle_name = el.attr('displayName') or vehicle_name
        vehicle_code = el.attr('code')
        vehicle_code_system = el.attr('codeSystem')
        vehicle_code_system_name = el.attr('codeSystemName')

        el = entry.tag('administrationUnitCode')
        administration_name = el.attr('displayName')
        administration_code = el.attr('code')
        administration_code_system = el.attr('codeSystem')
        administration_code_system_name = el.attr('codeSystemName')

        # performer => prescriber
        el = entry.tag('performer')
        prescriber_organization = el.tag('name').val()
        prescriber_person = None

        # Parse entryRelationship parts
        findings = documents.parse_findings(entry, start_date, end_date)

        data.append(wrappers.ObjectWrapper(
            section_title=medications.tag('title')._element.text,
            date_range=wrappers.ObjectWrapper(
                start=start_date,
                end=end_date
            ),
            entry_index=str(i),
            text=sig,
            product=wrappers.ObjectWrapper(
                source_line=entry._element.sourceline,
                name=product_name,
                code=product_code,
                code_system=product_code_system,
                text=product_original_text,
                translations=translations,
                findings=findings
            ),
            dose_quantity=wrappers.ObjectWrapper(
                value=dose_value,
                unit=dose_unit
            ),
            rate_quantity=wrappers.ObjectWrapper(
                value=rate_quantity_value,
                unit=rate_quantity_unit
            ),
            precondition=wrappers.ObjectWrapper(
                name=precondition_name,
                code=precondition_code,
                code_system=precondition_code_system
            ),
            reason=wrappers.ObjectWrapper(
                name=reason_name,
                code=reason_code,
                code_system=reason_code_system
            ),
            route=wrappers.ObjectWrapper(
                name=route_name,
                code=route_code,
                code_system=route_code_system,
                code_system_name=route_code_system_name
            ),
            schedule=wrappers.ObjectWrapper(
                type=schedule_type,
                period_value=schedule_period_value,
                period_unit=schedule_period_unit
            ),
            vehicle=wrappers.ObjectWrapper(
                name=vehicle_name,
                code=vehicle_code,
                code_system=vehicle_code_system,
                code_system_name=vehicle_code_system_name
            ),
            administration=wrappers.ObjectWrapper(
                name=administration_name,
                code=administration_code,
                code_system=administration_code_system,
                code_system_name=administration_code_system_name
            ),
            prescriber=wrappers.ObjectWrapper(
                organization=prescriber_organization,
                person=prescriber_person
            )
        ))

    return data
