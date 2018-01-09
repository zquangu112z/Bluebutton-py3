###############################################################################
# Copyright 2015 University of Florida. All rights reserved.
# This file is part of the BlueButton.py project.
# Use of this source code is governed by the license found in the LICENSE file.
###############################################################################

from ._ccda.allergies import allergies
from ._ccda.care_plan import care_plan
from ._ccda.demographics import demographics
from ._ccda.document import document
from ._ccda.encounters import encounters
from ._ccda.free_text import free_text
from ._ccda.functional_statuses import functional_statuses
from ._ccda.immunizations import immunizations
from ._ccda.instructions import instructions
from ._ccda.medications import medications
from ._ccda.problems import problems
from ._ccda.procedures import procedures
from ._ccda.results import results
from ._ccda.smoking_status import smoking_status
from ._ccda.vitals import vitals
from ..core import wrappers


def run(ccda):
    data = wrappers.ObjectWrapper()

    try:
        data.document = document(ccda)
    except AttributeError as e:
        data.document = None

    try:
        data.allergies = allergies(ccda)
    except AttributeError as e:
        data.allergies = None

    try:
        data.care_plan = care_plan(ccda)
    except AttributeError as e:
        data.care_plan = None

    try:
        data.chief_complaint = free_text(ccda, 'chief_complaint')
    except AttributeError as e:
        data.chief_complaint = None

    try:
        data.demographics = demographics(ccda)
    except AttributeError as e:
        data.demographics = None

    try:
        data.encounters = encounters(ccda)
    except AttributeError as e:
        data.encounters = None

    try:
        data.functional_statuses = functional_statuses(ccda)
    except AttributeError as e:
        data.functional_statuses = None

    try:
        data.immunizations = immunizations(ccda).administered
    except AttributeError as e:
        data.immunizations = None

    try:
        data.immunization_declines = immunizations(ccda).declined
    except AttributeError as e:
        data.immunization_declines = None

    try:
        data.instructions = instructions(ccda)
    except AttributeError as e:
        data.instructions = None

    try:
        data.results = results(ccda)
    except AttributeError as e:
        data.results = None

    try:
        data.medications = medications(ccda)
    except AttributeError as e:
        data.medications = None

    try:
        data.problems = problems(ccda)
    except AttributeError as e:
        data.problems = None

    try:
        data.procedures = procedures(ccda)
    except AttributeError as e:
        data.procedures = None

    try:
        data.smoking_status = smoking_status(ccda)
    except AttributeError as e:
        data.smoking_status = None

    try:
        data.vitals = vitals(ccda)
    except AttributeError as e:
        data.vitals = None

    return data
