#!/usr/bin/env python3

import csv
import sys

file_name = sys.argv[1]

with open(file_name) as file_to_process:
  # for some special csv files
  rows = csv.reader(file_to_process, 
                    delimiter = '|',
                    doublequote = False,
                    escapechar = '\\',
                    lineterminator = '\n',
                    quotechar = '',
                    quoting = csv.QUOTE_NONE,
                    skipinitialspace = True
                    )

  for row in rows:
    print(row)



