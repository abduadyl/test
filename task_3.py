
# Function to calculate Hamming_distance
def hamming_distance(first_dna, second_dna):

    # Checking the case when the lengths are not equal
    if len(first_dna) != len(second_dna):
        return 0

    # variable to count distance by default its 0
    counter = 0

    # Will be counting every time when there is no match in DNA's
    for i in range(len(first_dna)):
        if first_dna[i] != second_dna[i]:
            counter += 1

    return counter

# -----------------------------Test function----------------------------:

dna_1 = "GAGCCTACTAACGGGAT"
dna_2 = "CATCGTAATGACGGCCT"

print(hamming_distance(dna_1, dna_2))
