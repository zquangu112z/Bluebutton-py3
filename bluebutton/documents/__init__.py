###############################################################################
# Copyright 2015 University of Florida. All rights reserved.
# This file is part of the BlueButton.py project.
# Use of this source code is governed by the license found in the LICENSE file.
###############################################################################

from ..core import wrappers, strip_whitespace
from . import c32
from . import ccda
import logging as logger
from dateutil.parser import parse
unstructerdValueTypes = ["ST", "ED"]


def detect(data):
    if not hasattr(data, 'template'):
        return 'json'

    if not data.template('2.16.840.1.113883.3.88.11.32.1').is_empty():
        return 'c32'

    if not data.template('2.16.840.1.113883.10.20.22.1.1').is_empty():
        return 'ccda'
    logger.warning("type: unknown")

    return 'unknown'


def entries(element):
    """
    Get entries within an element (with tag name 'entry'),
    adds an `each` method
    """
    els = element.els_by_tag('entry')
    els.each = lambda callback: map(callback, els)
    return els


def parse_findings(entry, start_date, end_date):
    # Parse entryRelationship parts
    findings = []
    for entryRela in entry.els_by_tag('entryRelationship'):
        entry = entryRela.tag('observation')
        el = entry.tag('effectiveTime')
        if el.is_empty():
            start_date_rela = start_date
            end_date_rela = end_date
        else:
            start_date_rela, end_date_rela = parse_effectiveTime(
                el)

        el = entry.tag('code')
        name = el.attr('displayName')
        code = el.attr('code')
        code_system = el.attr('codeSystem')
        code_system_name = el.attr('codeSystemName')

        if not name:
            # if we'd like to get content only, use val() instead
            name = strip_whitespace(
                entry.tag('text').val_tostring())

        findings.append(wrappers.ObjectWrapper(
            date_range=wrappers.ObjectWrapper(
                start=start_date_rela,
                end=end_date_rela
            ),
            source_line=entry._element.sourceline,
            name=name,
            code=code,
            code_system=code_system,
            code_system_name=code_system_name
        ))

    return findings


def parse_address(address_element):
    """
    Parses an HL7 address (streetAddressLine [], city, state, postalCode,
    country)

    :param address_element:
    :return:
    """
    # Parse all streetAdressLine
    # els = address_element.els_by_tag('streetAddressLine')
    # street = [e.val() for e in els if e.val()]

    street = address_element.tag('streetAddressLine').val()

    city = address_element.tag('city').val()
    state = address_element.tag('state').val()
    zip = address_element.tag('postalCode').val()
    country = address_element.tag('country').val()

    return wrappers.ObjectWrapper(
        street=street,
        city=city,
        state=state,
        zip=zip,
        country=country,
    )


def parse_effectiveTime(effectiveTime_element):
    entry_date = parse_date(effectiveTime_element.attr('value'))
    if not entry_date:
        start_date = parse_date(effectiveTime_element.tag('low').attr('value'))
        end_date = parse_date(effectiveTime_element.tag('high').attr('value'))
    else:
        start_date = entry_date
        end_date = entry_date
    return start_date, end_date


def parse_date(string):
    """
    Parses an HL7 date in String form.
    If the parser failed (i.e wrong format, 'UNK'), return the original text
    """
    if not isinstance(string, str):
        return None

    try:
        return parse(string).isoformat()
    except ValueError as e:
        # In case we cannot parse the effectiveTime, return the string
        logger.warning("Cannnot parse %r to datetime", string)
        return string


def parse_name(name_element):
    prefix = name_element.tag('prefix').val()
    els = name_element.els_by_tag('given')
    given = [e.val() for e in els if e.val()]
    family = name_element.tag('family').val()

    return wrappers.ObjectWrapper(
        prefix=prefix,
        given=given,
        family=family
    )


def extract_uom(string):
    ''' Extract unit of measure from text '''
    words = str.split(string, " ")
    if len(words) > 1 and is_number(words[0]) and not is_number(words[1]):
        return words[0], words[1]
    else:
        return string, None


def is_number(s):
    try:
        float(s)
        return True
    except ValueError:
        pass

    try:
        import unicodedata
        unicodedata.numeric(s)
        return True
    except (TypeError, ValueError):
        pass

    return False
