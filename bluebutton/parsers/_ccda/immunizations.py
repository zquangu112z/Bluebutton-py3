###############################################################################
# Copyright 2015 University of Florida. All rights reserved.
# This file is part of the BlueButton.py project.
# Use of this source code is governed by the license found in the LICENSE file.
###############################################################################

"""
Parser for the CCDA immunizations section
"""
from ... import documents
from ...core import wrappers
from ... import core


def immunizations(ccda):

    parse_date = documents.parse_date
    administered_data = wrappers.ListWrapper()
    declined_data = wrappers.ListWrapper()

    immunizations = ccda.section('immunizations')

    for i, entry in enumerate(immunizations.entries()):

        # date
        el = entry.tag('effectiveTime')
        date = parse_date(el.attr('value'))
        if not date:
            date = parse_date(el.tag('low').attr('value'))

        # if 'declined' is true, this is a record that this vaccine WASN'T
        # administered
        el = entry.tag('substanceAdministration')
        declined = el.bool_attr('negationInd')

        # product
        product = entry.template('2.16.840.1.113883.10.20.22.4.54')
        el = product.tag('code')
        product_name = el.attr('displayName')
        product_code = el.attr('code')
        product_code_system = el.attr('codeSystem')
        product_code_system_name = el.attr('codeSystemName')

        # translations @TODO: remove it
        # el = product.tag('translation')
        # translation_name = el.attr('displayName')
        # translation_code = el.attr('code')
        # translation_code_system = el.attr('codeSystem')
        # translation_code_system_name = el.attr('codeSystemName')
        translations = []
        for el in product.els_by_tag('translation'):
            translations.append(wrappers.ObjectWrapper(
                name=el.attr('displayName'),
                code=el.attr('code'),
                code_system=el.attr('codeSystem'),
                code_system_name=el.attr('codeSystemName')
            ))

        # misc product details
        el = product.tag('lotNumberText')
        lot_number = el.val()

        el = product.tag('manufacturerOrganization')
        manufacturer_name = el.tag('name').val()

        # route
        el = entry.tag('routeCode')
        route_name = el.attr('displayName')
        route_code = el.attr('code')
        route_code_system = el.attr('codeSystem')
        route_code_system_name = el.attr('codeSystemName')

        # instructions
        el = entry.template('2.16.840.1.113883.10.20.22.4.20')
        instructions_text = core.strip_whitespace(el.tag('text').val())
        el = el.tag('code')
        education_name = el.attr('displayName')
        education_code = el.attr('code')
        education_code_system = el.attr('codeSystem')

        # dose
        el = entry.tag('doseQuantity')
        dose_value = el.attr('value')
        dose_unit = el.attr('unit')

        data = declined_data if declined else administered_data
        data.append(wrappers.ObjectWrapper(
            section_title=immunizations.tag('title')._element.text,
            date=date,
            date_range=wrappers.ObjectWrapper(
                start=date,
                end=date
            ),
            entry_index=str(i),
            product=wrappers.ObjectWrapper(
                source_line=entry._element.sourceline,
                name=product_name,
                code=product_code,
                code_system=product_code_system,
                code_system_name=product_code_system_name,
                translations=translations,
                lot_number=lot_number,
                manufacturer_name=manufacturer_name,
            ),
            dose_quantity=wrappers.ObjectWrapper(
                value=dose_value,
                unit=dose_unit,
            ),
            route=wrappers.ObjectWrapper(
                name=route_name,
                code=route_code,
                code_system=route_code_system,
                code_system_name=route_code_system_name
            ),
            instructions=instructions_text,
            education_type=wrappers.ObjectWrapper(
                name=education_name,
                code=education_code,
                code_system=education_code_system,
            ),
        ))

    return wrappers.ObjectWrapper(
        administered=administered_data,
        declined=declined_data
    )
