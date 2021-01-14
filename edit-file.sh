#!/bin/bash

echo $(uuidgen) > random
for i in {0..9};
do
    echo $(uuidgen) >> random
done