#!/usr/bin/env python3

import csv
import sys
import re
import datetime

input_file_name = sys.argv[1]
output_file_name = sys.argv[2]

required_columns = [
  re.compile(r'^(category|type|infection)$'),
  re.compile(r'^(address|ip)$'),
  re.compile(r'^asn$'),
  re.compile(r'^timestamp$'),
  re.compile(r'^city$'),
  re.compile(r'^error message$'),
  re.compile(r'^url$'),
  re.compile(r'^(http_agent|agent)$'),
  re.compile(r'^http_host$'),
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
parsed_data = []

# READING LOG DATA
with open(input_file_name) as file_to_process:
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

  row_items = list(rows)
  
  titles = row_items[1]

  #search for required columns
  for i in range(len(titles)):
    for col in required_columns:
      if col.match(titles[i]):
        col_index.append(i)
        break

  #get data in that column
  row_items.pop(0) #remove useless data
  for row in row_items:
    out_row = []
    for j in col_index:
      out_row.append(row[j])
    parsed_data.append(out_row)

  #convert all asn to integers
  for row in parsed_data:
    for i in range(len(row)):
      if isinstance(row[i], str) and row[i].isdecimal():
        row[i] = int(row[i])


# WRITING PARSED LOG DATA
with open(output_file_name, 'w', newline='') as output_file:
  writer = csv.writer(output_file,
                      delimiter = ',',
                      doublequote = False,
                      escapechar = '\\',
                      lineterminator = '\n',
                      quotechar = '"',
                      quoting = csv.QUOTE_NONNUMERIC,
                      skipinitialspace = True
                      )

  for row in parsed_data:
    writer.writerow(row)
  
