#!/bin/bash

set -e

date=$1
commits_number=$2
for commit_num in $(seq $commits_number )
do
    echo "commit $commit_num/$commits_number for $date";
    sh ./edit-file.sh
    git add random
    git commit -m "automatic ${commit_num}." --date "$date"
done
exit 0