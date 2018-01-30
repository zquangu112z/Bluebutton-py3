###############################################################################
# Copyright 2015 University of Florida. All rights reserved.
# This file is part of the BlueButton.py project.
# Use of this source code is governed by the license found in the LICENSE file.
###############################################################################

from bluebutton.core import codes
from bluebutton import documents
from ...core import wrappers


def demographics(ccda):
    parse_date = documents.parse_date
    parse_name = documents.parse_name
    parse_address = documents.parse_address

    demographics = ccda.section('demographics')

    patient = demographics.tag('patientRole')
    els = patient.els_by_tag('id')
    ids = wrappers.ListWrapper()
    SSN = None
    for e in els:
        if e.attr('root') == "2.16.840.1.113883.4.1":  # SSN root
            SSN = e.attr('extension')
        ids.append(wrappers.ObjectWrapper(
            root=e.attr('root'),
            extension=e.attr('extension'),
            assigningAuthorityName=e.attr('assigningAuthorityName')
        ))

    el = patient.tag('patient').tag('name')
    patient_name_dict = parse_name(el)
    sourceline = el._element.sourceline

    el = patient.tag('patient')
    dob = parse_date(el.tag('birthTime').attr('value'))
    gender = codes.gender(el.tag('administrativeGenderCode').attr('code'))
    marital_status = codes.marital_status(
        el.tag('maritalStatusCode').attr('code'))

    el = patient.tag('addr')
    patient_address_dict = parse_address(el)

    el = patient.tag('telecom')
    home = el.attr('value')
    work = None
    mobile = None

    email = None

    language = patient.tag('languageCommunication').tag(
        'languageCode').attr('code')
    race = patient.tag('raceCode').attr('displayName')
    ethnicity = patient.tag('ethnicGroupCode').attr('displayName')
    religion = patient.tag('religiousAffiliationCode').attr('displayName')

    el = patient.tag('birthplace')
    birthplace_dict = parse_address(el)

    el = patient.tag('guardian')
    guardian_relationship = el.tag('code').attr('displayName')
    guardian_relationship_code = el.tag('code').attr('code')
    guardian_home = el.tag('telecom').attr('value')

    el = el.tag('guardianPerson').tag('name')
    guardian_name_dict = parse_name(el)

    el = patient.tag('guardian').tag('addr')
    guardian_address_dict = parse_address(el)

    el = patient.tag('providerOrganization')
    provider_organization = el.tag('name').val()
    provider_phone = el.tag('telecom').attr('value')

    provider_address_dict = parse_address(el.tag('addr'))

    return wrappers.ObjectWrapper(
        source_line=sourceline,
        name=patient_name_dict,
        ids=ids,
        ssn=SSN,
        dob=dob,
        gender=gender,
        marital_status=marital_status,
        address=patient_address_dict,
        phone=wrappers.ObjectWrapper(
            home=home,
            work=work,
            mobile=mobile
        ),
        email=email,
        language=language,
        race=race,
        ethnicity=ethnicity,
        religion=religion,
        birthplace=wrappers.ObjectWrapper(
            state=birthplace_dict.state,
            zip=birthplace_dict.zip,
            country=birthplace_dict.country
        ),
        guardian=wrappers.ObjectWrapper(
            name=wrappers.ObjectWrapper(
                given=guardian_name_dict.given,
                family=guardian_name_dict.family
            ),
            relationship=guardian_relationship,
            relationship_code=guardian_relationship_code,
            address=guardian_address_dict,
            phone=wrappers.ObjectWrapper(
                home=guardian_home
            )
        ),
        provider=wrappers.ObjectWrapper(
            organization=provider_organization,
            phone=provider_phone,
            address=provider_address_dict
        )
    )
