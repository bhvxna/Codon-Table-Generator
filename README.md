# Codon Table Generator

## Project Description
This project is a Python-based program that translates DNA and RNA sequences into amino acids using the standard genetic code.

## Features
- Stores codons in a Python dictionary.
- Accepts DNA and RNA sequences.
- Validates input sequences.
- Splits sequences into groups of three bases.
- Translates codons into amino acids.
- Identifies start and stop codons.
- Handles incomplete codons.
- Displays the codon table and translated sequence.

## Technology Used
- Python 3

## Example Input
`ATGGCTTTTTAA`

## Expected Output
- Codons: ATG - GCT - TTT - TAA
- Amino acids: Methionine - Alanine - Phenylalanine - Stop
- Start codon: ATG
- Stop codon: TAA

## How to Run
1. Install Python 3.
2. Download or clone this repository.
3. Open a terminal in the project folder.
4. Run:

```bash
python codon_generator.py
```

## Author
Bhavana m Pradeep

## Comparison with a Reference Codon Table

The codon mappings in this project are based on the standard genetic code. They can be compared with the reference repository:

Reference: https://github.com/linsalrob/genetic_codes

### Example Codon Comparison

| Codon | Amino Acid |
|---|---|
| ATG | Methionine |
| GCT | Alanine |
| TTT | Phenylalanine |
| TAA | Stop |
| TAG | Stop |
| TGA | Stop |

These example codons match the standard genetic code.


