#!/bin/bash
for file in *.sql;
do
    psql seshatdbqing postgres -f "$file"
    echo "$file ---> Done."
done