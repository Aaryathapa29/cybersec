ciphertext = input("Enter the ciphertext: ").upper()

print("\nTrying all possible keys...\n")

# Outer loop for keys
for k in range(1, 26):

    plaintext = ""

    # Inner loop for each character
    for ch in ciphertext:

        if ch.isalpha():
            plaintext += chr((ord(ch) - 65 - k) % 26 + 65)
        else:
            plaintext += ch

    print("Key =", k, ":", plaintext)