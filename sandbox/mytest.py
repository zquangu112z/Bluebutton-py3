from bluebutton import BlueButton
import logging


def test_simple():
    try:
        with open('./sandbox/CDA.xml') as fp:
            ccd = BlueButton(fp)

            print(ccd.data.demographics.name.family)

            for id in ccd.data.demographics.ids:
                print(id.root)
                print(id.extension)
                print(id.assigningAuthorityName)

            assert True
    except Exception as e:
        logging.critical(e)
        assert False
