Miniproject summary

Author: Wenhua Zhou (wz2812@ic.ac.uk)

Contents covered: Shell script, python, R , LATEX, git

Packages used: 

Python (version 3.7.4)

pandas : used in data_preparation.py to load and write csv data 

R (version 3.6.1):

minpack.lm : used in NLLS_script.R for NLLS fitting for different models

ggplot2 : used in plotting_analysis.R for plotting the fitted values for consumption rates

####################

Code directory:

run_MiniProject.sh
# bash script to runs the whole project

compile_latex.sh
# bash script to compile pdf report from the tex file

data_preparation.py
# the data preparation script

NLLS_script.R
# the NLLS fitting script

plotting_analysis.R
# the plotting and analysis script

report.tex
# latex source code for the report

bibtexfile.bib
# the bibtex file for the latex report




Data directory:

BiotraitsTemplateDescription.pdf
# pdf defining the field names explaining the data from the original dataset

CRat.csv
# original dataset containing measurements of rates of consumption rate and resource density
# essential for functional response model fitting

data.csv
# the filtered data from CRat.csv after the data preparation step

FR.pdf
# an image showing the difference in the plot of Holling's type I II III response

modelfitting_CRat.csv
# the dataset containing the prediction consumption rate from 4 different models
# also including the AIC, BIC and R square value for all individuals in these four models


Results directory:
plot subdirectory:

Funtional_response_curve_6.pdf and etc.
# a total of 295 pdf plots
# the function response data compared with the predicted functional response value in the functional response curves for all 4 models
# the number is the number of ID value for these 295 individuals


The Report directory:

report.pdf
# pdf form of the written report
