#!/usr/bin/env python
#
#    verify_schema.py: simple LXML wrapper for checking XML against
#                      a RelaxNG schema.
#
#    Copyright (C) 2014 VyOS Development Group <maintainers@vyos.net>
#
#    This library is free software; you can redistribute it and/or
#    modify it under the terms of the GNU Lesser General Public
#    License as published by the Free Software Foundation; either
#    version 2.1 of the License, or (at your option) any later version.
#
#    This library is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU
#    Lesser General Public License for more details.
#
#    You should have received a copy of the GNU Lesser General Public
#    License along with this library; if not, write to the Free Software
#    Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston, MA  02110-1301
#    USA
import sys

from lxml import etree as ET

if len(sys.argv) < 2:
    print("Usage: {0} <RelaxNG schema file> <XML file>".format(sys.argv[0]))
    sys.exit(1)

schema = sys.argv[1]
xml_source = sys.argv[2]

xml_tree = ET.parse(xml_source)
relaxng_xml = ET.parse(schema)
validator = ET.RelaxNG(relaxng_xml)

if not validator.validate(xml_tree):
    print(validator.error_log)
    print("File {0} does not match the schema!".format(xml_source))
    sys.exit(1)
