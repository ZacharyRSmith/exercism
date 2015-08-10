from string import maketrans
import re

def to_rna(dna=''):
    """
    Converts DNA strand to RNA. The following is DNA -> complementary RNA:
    # * `G` -> `C`
    # * `C` -> `G`
    # * `T` -> `A`
    # * `A` -> `U`
    """
    if re.search(r'[^GCTA]', dna):
        raise Exception("Invalid DNA!")

    trans_tbl = maketrans("GCTA", "CGAU")

    return dna.translate(trans_tbl)
