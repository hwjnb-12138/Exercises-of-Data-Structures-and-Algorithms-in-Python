# Describe an efficient algorithm for finding the ten largest elements in a
#  sequence of size n. What is the running time of your algorithm?

def top_10(seq):
    if len(seq) <= 10:
        return seq

    tar = []
    for _ in range(10):
        seq_max = seq[0]
        idx = 0
        for j in range(len(seq)):
            if seq[j] >= seq_max:
                seq_max = seq[j]
                idx = j
        tar.append(seq_max)
        del seq[idx]
    return tar
# O(n)
