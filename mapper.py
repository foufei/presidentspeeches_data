# #!/usr/bin/env python
# import sys, re
import re
import pandas as pd
import os
import sys

# build valience lookup table
# valences_df = pd.read_csv('AFINN-en-165.txt', sep='\t', header=None, names = ["word", "valence"])
# valence_lookup_table = dict(zip(valences_df.word, valences_df.valence))

def main(argv):
    word_count = 0
    valence_aggregate = 0

    # input comes from STDIN (standard input)
    for line in sys.stdin:
        # remove leading and trailing whitespace
        line = line.strip()
        # keep alphabets
        pattern = re.compile("[a-zA-Z][a-zA-Z0-9]*")
        # split the line into words
        words = line.split()
        try:
            for word in pattern.findall(line):
                print ("LongValueSum:" + word.lower() + "\t" + "1")

        except EOFError as error:
            return None



if __name__ == "__main__":
    main(sys.argv)

