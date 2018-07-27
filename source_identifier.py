#!/usr/bin/env python3
import re

csv_filename_regex = re.compile(r'.*csv$')
txt_filename_regex = re.compile(r'.*txt$')
log_source_regex = re.compile(r'\d{4}-\d{2}-\d{2}-(.*)-research_and_education_network_for_uganda_renu-asn.csv')

def get_download_source(filename):
  if csv_filename_regex.match(filename):
    return "ShadowServer/Email"
  elif txt_filename_regex.match(filename):
    return "Team Cymru"
  else:
    return ""


def get_log_source(filename):
  result = re.search(log_source_regex, filename)
  return result.group(1)


