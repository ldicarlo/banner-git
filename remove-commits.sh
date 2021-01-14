#!/bin/bash 

git reset --soft "$(cat first-commit)"
git add .
git commit -m "clean commit"
git push -f