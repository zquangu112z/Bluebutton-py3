###############################################################################
# Copyright 2015 University of Florida. All rights reserved.
# This file is part of the BlueButton.py project.
# Use of this source code is governed by the license found in the LICENSE file.
###############################################################################

from ..core import wrappers
from . import ccda
from . import c32
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


def parse_address(address_element):
    """
    Parses an HL7 address (streetAddressLine [], city, state, postalCode,
    country)

    :param address_element:
    :return:
    """
    els = address_element.els_by_tag('streetAddressLine')
    street = [e.val() for e in els if e.val()]

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
