#!/usr/bin/env python

# Author: urain39@cyfan.cf

import os
import sys
import time
import xml.etree.ElementTree as ET

def main(argv):
    if len(argv) < 2:
        print('Usage: {0} <xmlfile>'.format(argv[0]))
        sys.exit(1)

    if os.path.exists(argv[1]):
        output = []
        root = ET.parse(argv[1]).getroot()        
        profile_name = argv[1].strip('.xml')

        for child in root.getchildren():
            if 'value' in child.attrib.keys():
                output.append('{0}={1}={2}'.format(
                        child.attrib['name'],
                        child.tag,
                        child.attrib['value']
                    )
                )
            else:
                output.append('{0}={1}={2}'.format(
                        child.attrib['name'],
                        child.tag,
                        child.text or ''
                    )
                )

        with open(profile_name + '.prf', 'w') as fp:
            fp.write(
                (
                    '# Date: {0}\n\n' +
                    'profile_name={1}\n\n'
                ).format(time.strftime('%Y-%m-%d'), profile_name)
            )

            fp.write('\n'.join(sorted(output)))

if __name__ == '__main__':
    main(sys.argv)
