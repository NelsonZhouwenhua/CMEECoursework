#!/bin/bash
# Author: wz2812@ic.ac.uk
# Script: run_vectorize.sh
# Desc: shell scripts to test computational performance for Vectorize1 and 2
# in both python and R
# Arguments: Vectorize1.py, Vectorize2.py, Vectorize1.R, Vectorize2.R
# Date: Oct 2019

echo -e "\nThe run time for Vectorize1.py:"
python Vectorize1.py
echo -e "\nThe run time for Vectorize1.R is:"
Rscript Vectorize1.R

echo -e "\nThe run time for Vectorize2.py:"
python Vectorize2.py
echo -e "\nThe run time for Vectorize2.R is:"
Rscript Vectorize2.R

echo -e "\nSummary:"
echo -e "\n1.From the run time for Vectorize2.R and Vectorize2.py, I manage to write a vectorization \nfor both file to vectorize the given Ricker function."
echo -e "\n2.From the run time for each file, we can see that vectorized method takes shorter time \nto run"
echo -e "\n3.From the 4 files, we can see that R run the loops slightly quicker and python using \nvectorized function is most computational efficient."

#exit