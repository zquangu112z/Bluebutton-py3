BlueButton.py: Blue Button Python Library
=========================================

[![Build Status](https://travis-ci.org/ctsit/bluebutton.py.svg)](https://travis-ci.org/ctsit/bluebutton.py)

BlueButton.py helps developers and non-developers alike to parse and extract
information from C-CDA files without the need to understand the [entire
specification][1].

[1]: http://www.hl7.org/implement/standards/product_brief.cfm?product_id=258


Example
-------

The following code reads in a CCD and prints out the Patient's Name and
Medications:

```python
from bluebutton import BlueButton

ccd = BlueButton('CCD.sample.xml')

ccd.type   # The document type ('ccda', 'c32', and such)
ccd.source # The parsed source data (XML) with added querying methods
ccd.data   # The final parsed document data

name = ccd.data.demographics.name
print name.prefix, name.given, name.family

print 'Medications:'
for medication in ccd.data.medications:
	print medication.product.name
```


Development
-----------

BlueButton.py is a port of [BlueButton.js][], the excellent Blue Button
JavaScript Library. _Many thanks go out to the [Blue Button developer
community](https://github.com/orgs/blue-button/people)!_ Currently, only
parsing of C-CDA documents is ported.

It is an open-source project created by the the [Clinical and
Translational Science Informatics and Technology (CTS-IT) group][CTS-IT] at the
University of Florida for the [OneFlorida Clinical Research
Consortium][OneFlorida]. See the AUTHORS.md file for more information.

BlueButton.py is covered by the Apache License, Version 2.0. More information
can be found in the LICENSE file.

The source code is available on GitHub:

	git clone https://github.com/ctsit/bluebutton.py

For instructions on setting up the developer's environment, run:

	make develop

The Technical Specification can be found in docs/specs.md.


Additional Resources
--------------------

 * CTS-IT:
   http://ufl.to/ctsit

 * OneFlorida CRC:
   https://onefloridaconsortium.org

 * BlueButton.js:
   http://bluebuttonjs.com

 * HL7 Consolidated CDA Specification:
   http://www.hl7.org/implement/standards/product_brief.cfm?product_id=258


[BlueButton.js]: http://bluebuttonjs.com
[CTS-IT]: http://ufl.to/ctsit
[OneFlorida]: https://onefloridaconsortium.org
