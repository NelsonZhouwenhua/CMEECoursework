#!/bin/bash
# Author: Wenhua Zhou wz2812@ic.ac.uk
# Script: csvtospace.sh
# Description: substitute the commas in the files with space
#
# Saves the output into a .csv file
# Arguments: 1 -> input variable, csv file
# Date: Oct 2019

echo "Creating a space delimited version of $1 ..."
# convert csv into space separated values and write into a new txt file
cat $1 | tr -s "," " " >> $1.txt
echo "Done!"
exit