find . -xdev  -type f ! -name '*.pyc' ! -name '__init__.py'  | cut -d "/" -f 2 | sort | uniq -c | sort -n
