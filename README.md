## BlueButton.py3: a python3-based version of BlueButton.py

### What's new?
- Support Python3
- Support C32 format
- Parse more sections and entries

### Initially, install the library:

```bash
make install
```

### Usage
You can view the mapping in */docs* folder

### Example

```python
from bluebutton import BlueButton

with open('CDA.xml') as fp:
    ccd = BlueButton(fp.read())

    ccd.type   # The document type ('ccda', 'c32', and such)
    ccd.source  # The parsed source data (XML) with added querying methods
    ccd.data   # The final parsed document data

    name = ccd.data.demographics.name
    print("Patient: ", name.prefix, name.given, name.family)
    print("Date of Birth: ", ccd.data.demographics.dob)
```

