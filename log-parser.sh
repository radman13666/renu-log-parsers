#!/usr/bin/env bash
LOG_PARSER_HOME=$1

DOWNLOADED_LOGS_DIR=$2
if [ ! -d $DOWNLOADED_LOGS_DIR ]; then
  exit 1
fi

PARSED_LOGS_DIR=$3
if [ ! -d $PARSED_LOGS_DIR ]; then
  mkdir -p $PARSED_LOGS_DIR
fi

function mark_parsed_logs {
  if [ $1 -eq 0 ]; then
    mv $DOWNLOADED_LOGS_DIR/$2 $DOWNLOADED_LOGS_DIR/.parsed-$2
  else
    mv $DOWNLOADED_LOGS_DIR/$2 $DOWNLOADED_LOGS_DIR/.error-parsing-$2
  fi
}

function parse_logs {
  for file in $1; do
    /bin/bash -c "$2 \"$DOWNLOADED_LOGS_DIR/$file\" \"$PARSED_LOGS_DIR/`date +%Y%m%d.%H%M%S.%N`.logdata.csv\""
    mark_parsed_logs $? $file
  done
}

RENU_CSV_FILES=`ls $DOWNLOADED_LOGS_DIR | grep 'renu.*txt'`
SINKHOLE_BOTNET_CSV_FILES=`ls $DOWNLOADED_LOGS_DIR | grep '\(sinkhole\|botnet\)'`
GENERIC_CSV_FILES=`ls $DOWNLOADED_LOGS_DIR | grep -v '\(renu.*txt\|sinkhole\|botnet\)'`

parse_logs "$GENERIC_CSV_FILES" $LOG_PARSER_HOME/general-csv-parser.py
parse_logs "$RENU_CSV_FILES" $LOG_PARSER_HOME/renu-csv-parser.py
parse_logs "$SINKHOLE_BOTNET_CSV_FILES" $LOG_PARSER_HOME/sinkhole-botnet-csv-parser.py
