#!/bin/bash
set -euo pipefail
curl -O https://s3.amazonaws.com/ds2002-resources/labs/lab3-bundle.tar.gz
tar -xzf lab3-bundle.tar.gz
awk '!/^[[:space:]]*$/' lab3_data.tsv > cleaned.tsv
tr '\t' ',' < cleaned.tsv > cleaned.csv
line_count=$(tail -n +2 cleaned.csv | wc -l)
echo "$line_count"

