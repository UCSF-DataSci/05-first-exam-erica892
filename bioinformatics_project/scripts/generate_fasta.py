# This python script generates a random DNA sequence and saves it in FASTA format.

# Import Python's random module.
import random

# Define the functions with docstring annotation. 
def generate_random_dna(length=1000000):
    """Generate a random DNA sequence of specified length using A, C, G, T."""
    bases = ['A', 'C', 'G', 'T']
    return ''.join(random.choices(bases, k=length))

def format_sequence(sequence, line_length=80):
    """Format the sequence to have a specified number of base pairs per line."""
    return '\n'.join(sequence[i:i+line_length] for i in range(0, len(sequence), line_length))

def save_sequence(sequence, filename):
    """Save the sequence to a file in FASTA format."""
    with open(filename, 'w') as file:
        file.write(">Erica's Random Sequence\n")
        file.write(sequence)

if __name__ == "__main__":
    # Step 1: Generate a random DNA sequence of 1 million base pairs.
    dna_sequence = generate_random_dna()

    # Step 2: Format the DNA sequence with 80 base pairs per line.
    formatted_sequence = format_sequence(dna_sequence)

    # Step 3: Save the sequence in FASTA format.
    save_sequence(formatted_sequence, "/workspaces/05-first-exam-erica892/bioinformatics_project/data/random_sequence.fasta")

    print("Random DNA sequence generated and saved to bioinformatics_project/data/random_sequence.fasta")