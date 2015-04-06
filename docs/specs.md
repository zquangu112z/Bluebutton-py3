Technical Specification for PyCCDA
==================================

This document outlines the port of [BlueButton.js][] to Python.

[BlueButton.js]: https://github.com/blue-button/bluebutton.js/


Values
------

 - **Pythonic**
   - The code should feel natural to a Python developer.

 - **Excellent documentation**
   - Classes and functions should be well documented.
   - Seasoned developers and new or part-time coders should all get use out of
   the documentation.
   - Code should be self-documenting, meaning written for readability.

 - **Utilize the original BlueButton.js**
   - BlueButton.js serves as an implementation guide.
   - Translation is easier than re-implementing. _(Hopefully this is true!)_
   - User communities should be able to share, help, and understand each other.


Concepts
--------

 * Parser ...
 * Generator ...
 * Section ...
 * Document ...
 * Allergies
 * Care Plan
 * Chief Complaint
 * Demographics
 * Encounters
 * Functional Statuses
 * Immunizations
 * Instructions
 * Results
 * Medications
 * Problems
 * Procedures
 * Smoking Status
 * Vitals

References
----------

 * [BlueButton.js](http://bluebuttonjs.com)
 * [HL7 Consolidated CDA Specification](http://www.hl7.org/implement/standards/product_brief.cfm?product_id=258)


Todo
----

 * Convert all BlueButton.js files from JavaScript to Python

<table>
	<thead>
	<tr>
		<th>BlueButton.js file</th>
		<th>Python equivalent</th>
		<th>Notes</th>
		<th>Ported?</th>
	</tr>
	</thead>
	<tbody>
	<tr>
	<td> <code>lib/bluebutton.js</code> </td>
	<td> <code>pyccda/__init__.py</code> </td>
	<td>&nbsp;</td>
	<td>Not yet</td>
	</tr>
	<tr class="alt">
	<td> <code>lib/core.js</code> </td>
	<td> <code>pyccda/core/__init__.py</code> </td>
	<td>&nbsp;</td>
	<td>Not yet</td>
	</tr>
	<tr class="alt">
	<td> <code>lib/core/codes.js</code> </td>
	<td> <code>pyccda/core/codes.py</code> </td>
	<td>&nbsp;</td>
	<td>Not yet</td>
	</tr>
	<tr class="alt">
	<td> <code>lib/core/xml.js</code> </td>
	<td> <code>pyccda/core/xml.py</code> </td>
	<td>&nbsp;</td>
	<td>Not yet</td>
	</tr>
	<tr>
	<td> <code>lib/documents.js</code> </td>
	<td> <code>pyccda/documents/__init__.py</code> </td>
	<td>&nbsp;</td>
	<td>Not yet</td>
	</tr>
	<tr>
	<td> <code>lib/documents/c32.js</code> </td>
	<td> <code>pyccda/documents/c32.py</code> </td>
	<td>&nbsp;</td>
	<td>Not yet</td>
	</tr>
	<tr>
	<td> <code>lib/documents/ccda.js</code> </td>
	<td> <code>pyccda/documents/ccda.py</code> </td>
	<td>&nbsp;</td>
	<td>Not yet</td>
	</tr>
	<tr class="alt">
	<td> <code>lib/generators.js</code> </td>
	<td> <code>pyccda/generators/__init__.py</code> </td>
	<td>&nbsp;</td>
	<td>Not yet</td>
	</tr>
	<tr class="alt">
	<td> <code>lib/generators/c32.js</code> </td>
	<td> <code>pyccda/generators/c32.py</code> </td>
	<td>&nbsp;</td>
	<td>Not yet</td>
	</tr>
	<tr class="alt">
	<td> <code>lib/generators/ccda.js</code> </td>
	<td> <code>pyccda/generators/ccda.py</code> </td>
	<td>&nbsp;</td>
	<td>Not yet</td>
	</tr>
	<tr class="alt">
	<td> <code>lib/generators/ccda_template.ejs</code> </td>
	<td>
	<em>N/A</em>
	</td>
	<td>&nbsp;</td>
	<td>&nbsp;</td>
	</tr>
	<tr>
	<td> <code>lib/parsers.js</code> </td>
	<td> <code>pyccda/parsers/__init__.py</code> </td>
	<td>&nbsp;</td>
	<td>Not yet</td>
	</tr>
	<tr>
	<td> <code>lib/parsers/c32.js</code> </td>
	<td> <code>pyccda/parsers/c32/__init__.py</code> </td>
	<td>&nbsp;</td>
	<td>Not yet</td>
	</tr>
	<tr>
	<td> <code>lib/parsers/c32/allergies.js</code> </td>
	<td> <code>pyccda/parsers/c32/allergies.py</code> </td>
	<td>&nbsp;</td>
	<td>Not yet</td>
	</tr>
	<tr>
	<td> <code>lib/parsers/c32/demographics.js</code> </td>
	<td> <code>pyccda/parsers/c32/demographics.py</code> </td>
	<td>&nbsp;</td>
	<td>Not yet</td>
	</tr>
	<tr>
	<td> <code>lib/parsers/c32/document.js</code> </td>
	<td> <code>pyccda/parsers/c32/document.py</code> </td>
	<td>&nbsp;</td>
	<td>Not yet</td>
	</tr>
	<tr>
	<td> <code>lib/parsers/c32/encounters.js</code> </td>
	<td> <code>pyccda/parsers/c32/encounters.py</code> </td>
	<td>&nbsp;</td>
	<td>Not yet</td>
	</tr>
	<tr>
	<td> <code>lib/parsers/c32/immunizations.js</code> </td>
	<td> <code>pyccda/parsers/c32/immunizations.py</code> </td>
	<td>&nbsp;</td>
	<td>Not yet</td>
	</tr>
	<tr>
	<td> <code>lib/parsers/c32/medications.js</code> </td>
	<td> <code>pyccda/parsers/c32/medications.py</code> </td>
	<td>&nbsp;</td>
	<td>Not yet</td>
	</tr>
	<tr>
	<td> <code>lib/parsers/c32/problems.js</code> </td>
	<td> <code>pyccda/parsers/c32/problems.py</code> </td>
	<td>&nbsp;</td>
	<td>Not yet</td>
	</tr>
	<tr>
	<td> <code>lib/parsers/c32/procedures.js</code> </td>
	<td> <code>pyccda/parsers/c32/procedures.py</code> </td>
	<td>&nbsp;</td>
	<td>Not yet</td>
	</tr>
	<tr>
	<td> <code>lib/parsers/c32/results.js</code> </td>
	<td> <code>pyccda/parsers/c32/results.py</code> </td>
	<td>&nbsp;</td>
	<td>Not yet</td>
	</tr>
	<tr>
	<td> <code>lib/parsers/c32/vitals.js</code> </td>
	<td> <code>pyccda/parsers/c32/vitals.py</code> </td>
	<td>&nbsp;</td>
	<td>Not yet</td>
	</tr>
	<tr>
	<td> <code>lib/parsers/ccda.js</code> </td>
	<td> <code>pyccda/parsers/ccd/__init__.py</code> </td>
	<td>&nbsp;</td>
	<td>Not yet</td>
	</tr>
	<tr>
	<td> <code>lib/parsers/ccda/allergies.js</code> </td>
	<td> <code>pyccda/parsers/ccda/allergies.py</code> </td>
	<td>&nbsp;</td>
	<td>Not yet</td>
	</tr>
	<tr>
	<td> <code>lib/parsers/ccda/care_plan.js</code> </td>
	<td> <code>pyccda/parsers/ccda/care_plan.py</code> </td>
	<td>&nbsp;</td>
	<td>Not yet</td>
	</tr>
	<tr>
	<td> <code>lib/parsers/ccda/demographics.js</code> </td>
	<td> <code>pyccda/parsers/ccda/demographics.py</code> </td>
	<td>&nbsp;</td>
	<td>Not yet</td>
	</tr>
	<tr>
	<td> <code>lib/parsers/ccda/document.js</code> </td>
	<td> <code>pyccda/parsers/ccda/document.py</code> </td>
	<td>&nbsp;</td>
	<td>Not yet</td>
	</tr>
	<tr>
	<td> <code>lib/parsers/ccda/encounters.js</code> </td>
	<td> <code>pyccda/parsers/ccda/encounters.py</code> </td>
	<td>&nbsp;</td>
	<td>Not yet</td>
	</tr>
	<tr>
	<td> <code>lib/parsers/ccda/free_text.js</code> </td>
	<td> <code>pyccda/parsers/ccda/free_text.py</code> </td>
	<td>&nbsp;</td>
	<td>Not yet</td>
	</tr>
	<tr>
	<td> <code>lib/parsers/ccda/functional_statuses.js</code> </td>
	<td> <code>pyccda/parsers/ccda/functional_statuses.py</code> </td>
	<td>&nbsp;</td>
	<td>Not yet</td>
	</tr>
	<tr>
	<td> <code>lib/parsers/ccda/immunizations.js</code> </td>
	<td> <code>pyccda/parsers/ccda/immunizations.py</code> </td>
	<td>&nbsp;</td>
	<td>Not yet</td>
	</tr>
	<tr>
	<td> <code>lib/parsers/ccda/instructions.js</code> </td>
	<td> <code>pyccda/parsers/ccda/instructions.py</code> </td>
	<td>&nbsp;</td>
	<td>Not yet</td>
	</tr>
	<tr>
	<td> <code>lib/parsers/ccda/medications.js</code> </td>
	<td> <code>pyccda/parsers/ccda/medications.py</code> </td>
	<td>&nbsp;</td>
	<td>Not yet</td>
	</tr>
	<tr>
	<td> <code>lib/parsers/ccda/problems.js</code> </td>
	<td> <code>pyccda/parsers/ccda/problems.py</code> </td>
	<td>&nbsp;</td>
	<td>Not yet</td>
	</tr>
	<tr>
	<td> <code>lib/parsers/ccda/procedures.js</code> </td>
	<td> <code>pyccda/parsers/ccda/procedures.py</code> </td>
	<td>&nbsp;</td>
	<td>Not yet</td>
	</tr>
	<tr>
	<td> <code>lib/parsers/ccda/results.js</code> </td>
	<td> <code>pyccda/parsers/ccda/results.py</code> </td>
	<td>&nbsp;</td>
	<td>Not yet</td>
	</tr>
	<tr>
	<td> <code>lib/parsers/ccda/smoking_status.js</code> </td>
	<td> <code>pyccda/parsers/ccda/smoking_status.py</code> </td>
	<td>&nbsp;</td>
	<td>Not yet</td>
	</tr>
	<tr>
	<td> <code>lib/parsers/ccda/vitals.js</code> </td>
	<td> <code>pyccda/parsers/ccda/vitals.py</code> </td>
	<td>&nbsp;</td>
	<td>Not yet</td>
	</tr>
	<tr class="alt">
	<td> <code>lib/renderers.js</code> </td>
	<td> <code>pyccda/renderers/__init__.py</code> </td>
	<td>&nbsp;</td>
	<td>Not yet</td>
	</tr>
	<tr class="alt">
	<td> <code>lib/renderers/html.js</code> </td>
	<td> <code>pyccda/renderers/html.py</code> </td>
	<td>&nbsp;</td>
	<td>Not yet</td>
	</tr>
	</tbody>
</table>

Testing
-------

	shell$ make test

Testing serves a dual-purpose: to ensure our code works as expected and to
document its intended use.

 - Port original tests:
   - spec/javascripts/amd_specs/bluebutton_spec.js
   - spec/javascripts/amd_specs/c32_spec.js
   - spec/javascripts/amd_specs/ccda_generator_spec.js
   - spec/javascripts/amd_specs/ccda_spec.js
   - spec/javascripts/browser_specs/bluebutton_spec.js
   - spec/javascripts/browser_specs/c32_spec.js
   - spec/javascripts/browser_specs/ccda_generator_spec.js
   - spec/javascripts/browser_specs/ccda_spec.js
   - spec/javascripts/fixtures/c32/HITSP_C32_with_HL7_IDs.xml
   - spec/javascripts/fixtures/c32/HITSP_C32v2.5_Rev6_16Sections_Entries_MinimalErrors.xml
   - spec/javascripts/fixtures/ccda/hl7_expected_ccda.xml
   - spec/javascripts/fixtures/ccda/nist_expected_ccda.xml
   - spec/javascripts/fixtures/json/allscripts_ccda_expected_output.json
   - spec/javascripts/fixtures/json/c32_expected_browser_output.json
   - spec/javascripts/fixtures/json/emerge_ccda_expected_output.json
   - spec/javascripts/fixtures/json/hl7_ccda_expected_output.json
   - spec/javascripts/fixtures/json/nist_ccda_expected_output.json
   - spec/javascripts/helpers/ejs.js
   - spec/javascripts/helpers/jasmine-jquery.js
   - spec/javascripts/helpers/jquery.js
   - spec/javascripts/helpers/shared_spec.js
   - spec/javascripts/helpers/underscore.js
   - spec/javascripts/node_specs/bluebutton_spec.js
   - spec/javascripts/node_specs/c32_spec.js
   - spec/javascripts/node_specs/ccda_generator_spec.js
   - spec/javascripts/node_specs/ccda_spec.js

 - Add additional tests to showcase Python functionality if necessary

Rationale
---------

There are tools out there which parse and generate C-CDA, so why have another
one and, furthermore, why port an existing one?

We wanted to write a C-CDA parser for use by our medical researchers and
informaticians. Many of them do not have a background in computer science, but
are familiar with data processing and logic.

These days, it's not difficult to search for how to do something, copy some
code from a question-and-answer site, tweak a few things, and be able to, for
example, pull out valuable information from one flat file format into another
one that can be ingested into a database.

We have heard from these willing researchers-turned-coders who have said the
existing C-CDA tools for Java have too steep of a learning curve. Also, they'd
prefer to use Python since their other tools are in Python.

According to [the ACM][1], as of July 2014, Python is the most popular language for
teaching introductory computer science courses at top-ranked U.S. departments.
Python is written to be easy for newcomers, but still allows coders the ability
to use OOP, lambda functions, parallel programming, and much more.

[1]: http://cacm.acm.org/blogs/blog-cacm/176450-python-is-now-the-most-popular-introductory-teaching-language-at-top-us-universities/fulltext

Having found no active, Python libraries for C-CDA, we started to write our
own. We were able to manipulate the HL7 XML Schemas to generate Python bindings
from the HL7 XML Schemas using [PyXB][], but the resulting code was difficult
to decipher. We then tried [generateDS][], but that failed to generate working
code.

[PyXB]: http://pyxb.sourceforge.net/
[generateDS]: http://www.davekuhlman.org/generateDS.html

We were just about to dive into implementing the giant, 595-page specification
when we found BlueButton.js. It was straigt-forward to use and we could even
call it from Python and use the standard JSON module to convert the JSON into
Python objects.

While that solution (XML to JSON to Python) might work for some, we wanted to
completely remove the dependency on NodeJS, thus we decided to port
BlueButton.js.

