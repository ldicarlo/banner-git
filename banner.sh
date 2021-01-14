#!/bin/bash


# sed -ir 's/\t//g' input/input-ex

./remove-commits.sh

./csv-creator.py

cat output/output-ex | xargs -I {} sh -c './commit.sh {}'

git push -f