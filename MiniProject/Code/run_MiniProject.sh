#!/bin/bash
# Author: wz2812@ic.ac.uk
# Script: run_MiniProject.sh
# Desc: a bach script to run the whole project
# Arguments: none
# Date: March 2020

# run python script data_preparation.py for filtering the data
echo -e "\nrun data_preparation.py for data preparation"
python3 data_preparation.py

# run R the main NLLS fitting for 4 different models
echo -e "\nrun NLLS_script.R fpr NLLS fitting in R"
Rscript NLLS_script.R

# run R for the fitted model plotting and AIC, AICc analysis
echo -e "\nrun plotting_analysis.R in R for plotting and analysis"
Rscript plotting_analysis.R

