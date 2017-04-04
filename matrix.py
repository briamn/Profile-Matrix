import numpy as np
seq = {}
with open('matrices.txt', 'r') as f:
    for line in f:
        if line.startswith('>'):
            name = line.strip('>\n')
            seq[name] = ''
        else:
            seq[name] = line.rstrip('\n')

sequences = [seq[i] for i in seq]
a = np.zeros((4,len(sequences[0])))
k = len(sequences[0])
dicter = {
'A': [0] * k,
'C': [0] * k,
'G': [0] * k,
'T': [0] * k
}
for stuff in sequences:
    c = 0
    for i in stuff:
        if i == "A":
            a[0,c] +=1
            dicter['A'][c] += 1
            c += 1
        elif i == "C":
            a[1,c] +=1
            dicter['C'][c] += 1
            c += 1
        elif i == "G":
            a[2,c] +=1
            dicter['G'][c] += 1
            c += 1
        else:
            a[3,c] +=1
            dicter['T'][c] += 1
            c += 1
k = len(sequences[0])
consensus = []
for i in a.T:
    if i[0] == max(i):
        consensus.append("A")
    if i[1] == max(i):
        consensus.append("C")
    if i[2] == max(i):
        consensus.append("G")
    if i[3] == max(i):
        consensus.append("T")

for i in dicter:
    print(i, dicter[i])

print("Your consensus sequence is : ", ''.join(consensus))
