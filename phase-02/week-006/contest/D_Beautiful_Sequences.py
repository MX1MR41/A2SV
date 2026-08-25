k = int(input())
sequences = []
for _ in range(k):
    n = int(input())
    a = list(map(int, input().split()))
    sequences.append(a)

encountered_sums = {}

for j in range(k):
    sequence = sequences[j]
    seq_tot = sum(sequence)

    for y in range(len(sequence)):
        dif = seq_tot - sequence[y]

        # if the difference exists it shouldn't be in the same sequence
        if dif in encountered_sums and encountered_sums[dif][0] != j:
            # i = the sequence index where we saw this dif before, x the index of the number removed to get this sum in sequence i
            i, x = encountered_sums[dif] 
            print('YES')
            print(i + 1, x + 1)
            print(j + 1, y + 1)
            exit()

        # store the sequence sum with the current number excluded
        encountered_sums[dif] = (j, y)

print('NO')