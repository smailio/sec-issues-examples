from flask import Flask, request
from defusedxml import ElementTree as ET
from lxml import etree
app = Flask(__name__)


@app.route('/parse-xml-unsafe', methods=['POST'])
def parse_xml_unsafe():
    xml_data = request.data

    # Parse XML using defusedxml to mitigate XXE vulnerability
    try:
        tree = etree.fromstring(xml_data)
    except etree.ParseError as e:
        return 'Invalid XML data', 400

    # Process the XML tree
    # ...

    return tree.text

@app.route('/parse-xml', methods=['POST'])
def parse_xml():
    xml_data = request.data

    # Parse XML using defusedxml to mitigate XXE vulnerability
    try:
        tree = ET.fromstring(xml_data)
    except ET.ParseError:
        return 'Invalid XML data', 400

    # Process the XML tree
    # ...

    return 'XML parsed successfully'

if __name__ == '__main__':
    app.run()
