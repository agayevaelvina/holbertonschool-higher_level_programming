#!/bin/bash
# x
if [ -z "$1" ]; then
  echo "Usage: $0 <database_name>"
  exit 1
fi

DB_NAME="$1"

# List all tables in the specified MySQL database
mysql "$DB_NAME" -e "SHOW TABLES;"
