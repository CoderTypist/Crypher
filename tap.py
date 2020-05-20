#!/usr/bin/env python3

# Author: Christian Bargraser

# Encrypted text should be in the following format:
#     #,#|#,#|#,#
#
# Example:
#     1,3|1,1|4,2

import argparse
from argparse import RawTextHelpFormatter
import crypher.tap as tap

strEpilog = '''
  **************
  * UTSA - NSA *
  **************
  --- CAE-CO ---
                
'''

parser = argparse.ArgumentParser(epilog=strEpilog, formatter_class=RawTextHelpFormatter)

group_action = parser.add_mutually_exclusive_group(required=True)
group_action.add_argument('-e', '--encode', help='plaintext file')
group_action.add_argument('-d', '--decode', help='tap code encoded file')

parser.add_argument('-o', '--output',  help = 'output file')
dictArgs = vars(parser.parse_args())

if dictArgs.get('encode'):
    tap.encode(dictArgs.get('encode'), dictArgs.get('output'))

else:
    tap.decode(dictArgs.get('decode'), dictArgs.get('output'))
