#!/bin/bash
# Author: wz2812@ic.ac.uk
# Script: run_get_TreeHeight.sh
# Desc: shell scripts to run_get_TreeHeight.R with Trees data, use trees.csv as example
# Arguments: run_get_TreeHeight.R, Trees.csv
# Date: Oct 2019

# run R with example trees.csv
echo -e "\nrun R with example trees.csv"
Rscript get_TreeHeight.R ../Data/trees.csv

# run python with example trees.csv
echo -e "\nrun python with example trees.csv"
python3 get_TreeHeight.py ../Data/trees.csv