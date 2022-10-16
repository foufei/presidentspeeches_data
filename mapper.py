# #!/usr/bin/env python
# import sys, re
# import random
# import pandas as pd
# import os
#
# # build valience lookup table
# # valences_df = pd.read_csv('AFINN-en-165.txt', sep='\t', header=None, names = ["word", "valence"])
# # valence_lookup_table = dict(zip(valences_df.word, valences_df.valence))
#
# def main(argv):
#     word_count = 0
#     valence_aggregate = 0
#
#     # input comes from STDIN (standard input)
#     for line in sys.stdin:
#         # remove leading and trailing whitespace
#         line = line.strip()
#         # split the line into words
#         words = line.split()
#         # increase counters
#         for word in words:
#             # write the results to STDOUT (standard output);
#             # what we output here will be the input for the
#             # Reduce step, i.e. the input for reducer.py
#             #
#             # tab-delimited; the trivial word count is 1
#             # valence_aggregate += valence_lookup_table[word]
#             # word_count += 1
#             print(word + "\t" + "1")
#
#
# if __name__ == "__main__":
#     main(sys.argv)
#
#

#!/usr/bin/env python
import sys, re
import random

def main(argv):
    line = sys.stdin.readline()
    pattern = re.compile("[a-zA-Z][a-zA-Z0-9]*")
    try:
        while line:
            for word in pattern.findall(line):
                print ("LongValueSum:" + word.lower() + "\t" + "1")
                # x = 1 / random.randint(0,99)
            line = sys.stdin.readline()
    except EOFError as error:
        return None

if __name__ == "__main__":
    main(sys.argv)
