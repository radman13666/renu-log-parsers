#!/usr/bin/env python3

import csv
import sys
import re

file_name = sys.argv[1]

required_columns = [
  re.compile(r'^(category|type|infection)$'),
  re.compile(r'^(address|ip)$'),
  re.compile(r'^asn$'),
  re.compile(r'^timestamp$'),
  re.compile(r'^city$'),
  re.compile(r'^error message^'),
  re.compile(r'^url^'),
  re.compile(r'^(http_agent|agent)^'),
  re.compile(r'^http_host$'),
  re.compile(r'^(infection|type|category)$'),
  re.compile(r'^(dst_port|dest_port|cc_port)$'),
  re.compile(r'^(dst_asn|dest_asn|cc_asn)$'),
  re.compile(r'^(dest_ip|dst_ip|cc_ip)$'),
  re.compile(r'^service$'),
  re.compile(r'^source$'),
  re.compile(r'^reason$'),
  re.compile(r'^notes$'),
  re.compile(r'^src_port$')
]

col_index = []

with open(file_name) as file_to_process:
  # for standard csv files
  rows = csv.reader(file_to_process, 
                    delimiter = ',',
                    doublequote = False,
                    escapechar = '\\',
                    lineterminator = '\n',
                    quotechar = '"',
                    quoting = csv.QUOTE_NONNUMERIC,
                    skipinitialspace = True
                    )
  titles = list(rows)[0]

  print(titles)
  
  for i in range(len(titles)):
    for col in required_columns:
      if col.match(titles[i]):
        col_index.append(i)
        break
  
  print(col_index)

  #for row in rows:
  #  print(row)

  

