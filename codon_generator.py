
# Python Project: Codon Table Generator

# Standard genetic code: DNA codons and amino acids
codon_table = {
    "TTT": "Phenylalanine", "TTC": "Phenylalanine",
    "TTA": "Leucine", "TTG": "Leucine",
    "TCT": "Serine", "TCC": "Serine",
    "TCA": "Serine", "TCG": "Serine",
    "TAT": "Tyrosine", "TAC": "Tyrosine",
    "TAA": "Stop", "TAG": "Stop",
    "TGT": "Cysteine", "TGC": "Cysteine",
    "TGA": "Stop", "TGG": "Tryptophan",

    "CTT": "Leucine", "CTC": "Leucine",
    "CTA": "Leucine", "CTG": "Leucine",
    "CCT": "Proline", "CCC": "Proline",
    "CCA": "Proline", "CCG": "Proline",
    "CAT": "Histidine", "CAC": "Histidine",
    "CAA": "Glutamine", "CAG": "Glutamine",
    "CGT": "Arginine", "CGC": "Arginine",
    "CGA": "Arginine", "CGG": "Arginine",

    "ATT": "Isoleucine", "ATC": "Isoleucine",
    "ATA": "Isoleucine", "ATG": "Methionine",
    "ACT": "Threonine", "ACC": "Threonine",
    "ACA": "Threonine", "ACG": "Threonine",
    "AAT": "Asparagine", "AAC": "Asparagine",
    "AAA": "Lysine", "AAG": "Lysine",
    "AGT": "Serine", "AGC": "Serine",
    "AGA": "Arginine", "AGG": "Arginine",

    "GTT": "Valine", "GTC": "Valine",
    "GTA": "Valine", "GTG": "Valine",
    "GCT": "Alanine", "GCC": "Alanine",
    "GCA": "Alanine", "GCG": "Alanine",
    "GAT": "Aspartic acid", "GAC": "Aspartic acid",
    "GAA": "Glutamic acid", "GAG": "Glutamic acid",
    "GGT": "Glycine", "GGC": "Glycine",
    "GGA": "Glycine", "GGG": "Glycine"
}

start_codon = "ATG"
stop_codons = {"TAA", "TAG", "TGA"}

def translate_codons(codons):
    amino_acids = translate_codons(codons)
    return amino_acids
def main():
    print("=== CODON TABLE GENERATOR ===")
    print("1. DNA sequence")
    print("2. RNA sequence")

    choice = input("Choose 1 or 2: ").strip()

    if choice not in ("1", "2"):
        print("Error: Please choose 1 or 2.")
        return

    sequence = input("Enter your sequence: ").strip().upper()

    if not sequence:
        print("Error: Sequence cannot be empty.")
        return

    # Convert RNA to DNA notation for translation
    if choice == "2":
        if any(base not in "AUGC" for base in sequence):
            print("Error: RNA must contain only A, U, G, C.")
            return
        sequence = sequence.replace("U", "T")
    else:
        if any(base not in "ATGC" for base in sequence):
            print("Error: DNA must contain only A, T, G, C.")
            return

    # Divide sequence into complete codons
    codons = [
        sequence[i:i + 3]
        for i in range(0, len(sequence) - 2, 3)
    ]

    remainder = sequence[len(codons) * 3:]

    print("\n=== CODON TABLE ===")
    for codon in sorted(codon_table):
        print(f"{codon} : {codon_table[codon]}")

    print("\n=== TRANSLATION RESULT ===")
    print(f"Codons: {' - '.join(codons) if codons else 'None'}")

    amino_acids = [codon_table[codon] for codon in codons]
    print(f"Amino acids: {' - '.join(amino_acids) if amino_acids else 'None'}")

    starts = [c for c in codons if c == start_codon]
    stops = [c for c in codons if c in stop_codons]

    print(f"Start codons: {', '.join(starts) if starts else 'None'}")
    print(f"Stop codons: {', '.join(stops) if stops else 'None'}")

    if remainder:
        print(f"Incomplete codon: {remainder}")
    else:
        print("Incomplete codon: None")

    if choice == "2":
        print("Input type: RNA")


if __name__ == "__main__":
    main()
