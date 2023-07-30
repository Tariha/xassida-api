#!/usr/bin/env bash
# Time: 2023-07-30 10:34:31
cd data
python parse_xassida.py
python parse_translations.py
python parse_author.py
cd ../utils/db
python insert.py
