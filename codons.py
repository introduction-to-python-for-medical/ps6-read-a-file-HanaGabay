def create_codon_dict(path):
    file = open(path)
    rows = file.readlines()
    file.close()

    amino_acids = {}
    for row in rows:
     cells = row.strip().split('\t')
     codon = cells[0]
     amino_acid = cells[2]
     amino_acids[codon] = amino_acid
    return amino_acids



