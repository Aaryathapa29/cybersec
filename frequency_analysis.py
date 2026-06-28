from collections import Counter

# -------------------- Cipher Text --------------------

cipher = """UQ UZ D EMDRQUNRX GDB . TPB DYM TM ZUQQUIO UI D GDYW YJJH YMDGUIO
QPUZ HMZZDOM ? EMFDRZM UQ UZ NRI , ERQ UN TM GJ IJQ OMQ HJYM M Z TM
TUXX ZQDB PMYM NJYMSMY"""

# ---------------- Standard Frequency Distribution ----------------

sfd = {
    'E':12.7,'T':9.1,'A':8.2,'O':7.5,'I':7.0,'N':6.7,'S':6.3,
    'R':6.0,'H':6.1,'D':4.3,'L':4.0,'C':2.8,'U':2.8,'M':2.4,
    'W':2.4,'F':2.2,'G':2.0,'Y':2.0,'P':1.9,'B':1.5,'V':1.0,
    'K':0.7,'J':0.2,'X':0.2,'Q':0.1,'Z':0.1
}

# ---------------- Count Single Letters ----------------

letters = [c for c in cipher if c.isalpha()]
single = Counter(letters)

# ---------------- Count Digrams ----------------

words = [''.join(filter(str.isalpha, w)) for w in cipher.split()]
digrams = Counter(w for w in words if len(w) == 2)

# ---------------- Count Trigrams ----------------

trigrams = Counter(w for w in words if len(w) == 3)

print("="*60)
print("STANDARD FREQUENCY DISTRIBUTION")
print("="*60)

for k, v in sfd.items():
    print(f"{k} : {v}%")

print("\n" + "="*60)
print("SINGLE LETTER FREQUENCY")
print("="*60)

for letter, count in single.most_common():
    print(f"{letter} : {count}")

print("\n" + "="*60)
print("DIGRAM FREQUENCY")
print("="*60)

for word, count in digrams.most_common():
    print(f"{word} : {count}")

print("\n" + "="*60)
print("TRIGRAM FREQUENCY")
print("="*60)

for word, count in trigrams.most_common():
    print(f"{word} : {count}")
    # ---------------- Build Initial Substitution ----------------

print("\n" + "="*60)
print("INITIAL SUBSTITUTION TABLE")
print("="*60)

# Cipher letters sorted by frequency
cipher_rank = [letter for letter, _ in single.most_common()]

# English letters sorted by SFD
english_rank = sorted(sfd, key=sfd.get, reverse=True)

# Create substitution dictionary
mapping = {}

for c, p in zip(cipher_rank, english_rank):
    mapping[c] = p
    print(f"{c}  -->  {p}")

# ---------------- Partial Decryption ----------------

partial = ""

for ch in cipher:

    if ch.isalpha():
        partial += mapping.get(ch, ch)
    else:
        partial += ch

print("\n" + "="*60)
print("PARTIALLY DECRYPTED TEXT")
print("="*60)
print(partial)

# ---------------- Manual Refinement ----------------

print("\n" + "="*60)
print("MANUAL SUBSTITUTION")
print("="*60)
print("Enter substitutions like: M E")
print("Type EXIT to finish.\n")

while True:

    choice = input("Substitute (Cipher Plain): ").upper()

    if choice == "EXIT":
        break

    parts = choice.split()

    if len(parts) != 2:
        print("Example: M E")
        continue

    cipher_letter = parts[0]
    plain_letter = parts[1]

    # Update substitution table
    mapping[cipher_letter] = plain_letter

    # Regenerate plaintext from ORIGINAL ciphertext
    current = ""

    for ch in cipher:

        if ch.isalpha():

            if ch in mapping:
                current += mapping[ch].lower()

            else:
                current += "_"

        else:
            current += ch

    print("\nCurrent Plaintext:\n")
    print(current)

# ---------------- Final Output ----------------

print("\n" + "="*60)
print("FINAL ESTIMATED PLAINTEXT")
print("="*60)

print(current)

print("\nSubstitution Table")

for k in sorted(mapping):
    print(f"{k} -> {mapping[k]}")

  