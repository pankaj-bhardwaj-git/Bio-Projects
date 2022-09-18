# reading fasta file
data = open(r"C:\\Users\\Pankaj\\Desktop\\DSA Python\\Bio Projects\\dna.fasta")
a = data.read()
# eliminating starting text from sequence
seq = a[26:]
n = 0
total = 0
arr = []
# defining a reverse function ,not using the default reverse function


def reverse(k):
    rev_a = ""
    for i in range(len(k)-1, -1, -1):
        rev_a = rev_a + k[i]
    return rev_a

# using self defined complement function


def comp(a):
    k = ""
    for i in range(0, len(a)):
        if a[i] == "A":
            k = k + "T"
        elif a[i] == "G":
            k = k + "C"
        elif a[i] == "T":
            k = k+"A"
        elif a[i] == "C":
            k = k + "G"
    return k


for k in range(2,len(seq)):
  n = 0
  for i in range(len(seq)-k):
      check = ""
      for j in range(i, i+k):
          check = check + seq[j]
      if check == reverse(comp(check)):
          n += 1
          print(f"palindrome of {k} letters at position no {i} is {check}")    
      
  total += n
  arr.append(n)  

  print(f"Total number of palindromic sites of length {k} is {n}")

print(f"total palindromes  in the sequence is {total}\n {arr}")
