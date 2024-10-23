# This python script performs various operations on DNA sequences.

# Import Python's sys module.
import sys

# Define the 3 functions to perform on DNA sequences.
def complement(sequence):
    """Return the complement of a DNA sequence."""
    complement_map = str.maketrans('ACGTacgt', 'TGCAtgca')
    return sequence.translate(complement_map)

def reverse(sequence):
    """Return the reverse of a DNA sequence."""
    return sequence[::-1]

def reverse_complement(sequence):
    """Return the reverse complement of a DNA sequence."""
    return complement(reverse(sequence))

if __name__ == "__main__":
    # Check if a sequence was provided as a command-line argument
    if len(sys.argv) != 2:
        print("Usage: python dna_operations.py <DNA_sequence>")
        sys.exit(1)

    # Get the DNA sequence from the command-line argument
    original_sequence = sys.argv[1]

    # Generate the complement, reverse, and reverse complement of the sequence
    complement_sequence = complement(original_sequence)
    reverse_sequence = reverse(original_sequence)
    reverse_complement_sequence = reverse_complement(original_sequence)

    # Print results
    print(f"Original sequence: {original_sequence}")
    print(f"Complement: {complement_sequence}")
    print(f"Reverse: {reverse_sequence}")
    print(f"Reverse Complement: {reverse_complement_sequence}")