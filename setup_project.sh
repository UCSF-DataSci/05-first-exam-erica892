#!/bin/bash
# This shell script sets up a directory structure for a bioinformatics project.

# Create the main project directory
mkdir -p bioinformatics_project

# Navigate into the main project directory
cd bioinformatics_project

# In the main directory, create the subdirectories
mkdir -p data scripts results

# In the scripts directory, create empty Python files
touch scripts/generate_fasta.py scripts/dna_operations.py scripts/find_cutsites.py

# In the results directory, create an empty file
touch results/cutsite_summary.txt

# In the data directory, create an empty file
touch data/random_sequence.fasta

# Create a README.md file with a brief description
echo "# Bioinformatics Project" > README.md
echo "This project is composed of 3 subdirectories to organize a bioinformatics analysis:" >> README.md
echo "- **data/**: Contains input and output data files." >> README.md
echo "- **scripts/**: Contains python scripts for processing and analyzing the data." >> README.md
echo "- **results/**: Contains results files from the analysis." >> README.md
