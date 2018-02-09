###############################################################################
# Copyright 2015 University of Florida. All rights reserved.
# This file is part of the BlueButton.py project.
# Use of this source code is governed by the license found in the LICENSE file.
###############################################################################

from ._ccda.allergies import allergies
from ._ccda.care_plans import care_plans
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
from ._ccda.social_historys import social_historys
from ._ccda.vitals import vitals
from ..core import wrappers


def run(ccda):
    data = wrappers.ObjectWrapper()

    ccda._entry_counter = 0

    data.document = document(ccda)

    data.allergies = allergies(ccda)

    data.care_plans = care_plans(ccda)

    data.chief_complaint = free_text(ccda, 'chief_complaint')

    data.demographics = demographics(ccda)

    data.encounters = encounters(ccda)

    data.functional_statuses = functional_statuses(ccda)

    data.immunizations = immunizations(ccda).administered

    data.immunization_declines = immunizations(ccda).declined

    data.instructions = instructions(ccda)

    data.results = results(ccda)

    data.medications = medications(ccda)

    data.problems = problems(ccda)

    data.procedures = procedures(ccda)

    data.social_historys = social_historys(ccda)

    data.vitals = vitals(ccda)

    return data
