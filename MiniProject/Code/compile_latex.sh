#!/bin/bash
# Author: wz2812@ic.ac.uk
# Script: compile_latex.sh
# Desc: a bach script to compile tex file
# Arguments: tex file for latex compiling
# Date: March 2020

pdflatex report.tex
bibtex report
pdflatex report.tex

## Cleanup
rm *~
rm *.aux
rm *.dvi
rm *.log
rm *.nav
rm *.out
rm *.snm
rm *.toc
rm *.bbl
rm *.blg

mv report.pdf ../Report/