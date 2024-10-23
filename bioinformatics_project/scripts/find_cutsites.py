# This python script finds distant cutsites in FASTA data.

# Import python sys and os modules.
import sys
import os

# Define functions as described in the question prompt with docstring annotation.
def read_fasta(file_path):
    """Read a FASTA file and save the DNA sequence without whitespace."""
    with open(file_path, 'r') as file:
        # Join sequences into a single string, removing whitespace, excluding the header
        sequence = ''.join(line.strip() for line in file if not line.startswith('>'))
    return sequence

def find_cut_sites(dna, cut_site):
    """Find all occurrences of the cut site in the DNA sequence."""
    cut_site_clean = cut_site.replace('|', '')  # Remove the '|' character from the cut site
    locations = []
    start = 0

    # Find all positions of the cut site in the DNA sequence
    while True:
        start = dna.find(cut_site_clean, start)
        if start == -1:
            break
        locations.append(start)
        start += 1  # Move to the next position

    return locations

def find_cut_site_pairs(locations):
    """Find all pairs of cut sites that are 80-120 kbp apart."""
    pairs = []

    for i in range(len(locations)):
        for j in range(i + 1, len(locations)):
            distance = locations[j] - locations[i]
            if 80000 <= distance <= 120000:
                pairs.append((locations[i], locations[j]))

    return pairs

def save_summary(pairs, output_file):
    """Save a summary of the cut site pairs to a file."""
    with open(output_file, 'w') as file:
        file.write(f"Total cut site pairs found: {len(pairs)}\n")
        file.write("First 5 cut site pairs:\n")
        for i, (pos1, pos2) in enumerate(pairs[:5]):
            file.write(f"Pair {i + 1}: ({pos1}, {pos2})\n")

if __name__ == "__main__":

    # Get arguments from the command line
    fasta_file = sys.argv[1]
    cut_site = sys.argv[2]

    # Fix the path to the FASTA file
    base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    fasta_file_path = os.path.join(base_dir, fasta_file)

    # Read the DNA sequence from the FASTA file
    dna_sequence = read_fasta(fasta_file_path)

    # Find all cut site locations
    cut_site_locations = find_cut_sites(dna_sequence, cut_site)

    # Find all cut site pairs that are 80-120 kbp apart
    cut_site_pairs = find_cut_site_pairs(cut_site_locations)

    # Print results
    print(f"Total cut site pairs found: {len(cut_site_pairs)}")
    if len(cut_site_pairs) > 0:
        print("First 5 cut site pairs:")
        for i, (pos1, pos2) in enumerate(cut_site_pairs[:5]):
            print(f"Pair {i + 1}: ({pos1}, {pos2})")

    # Save results to a file in the 'results' directory
    output_file = "/workspaces/05-first-exam-erica892/bioinformatics_project/results/cutsite_summary.txt"
    os.makedirs(os.path.dirname(output_file), exist_ok=True)
    save_summary(cut_site_pairs, output_file)

    print(f"Summary saved to {output_file}")