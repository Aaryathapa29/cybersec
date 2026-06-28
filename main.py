# Caesar Cipher Encryption Function
def caesare(k, x):
    ciphertext = ""

    for ch in x.upper():
        if ch.isalpha():
            ciphertext += chr((ord(ch) - 65 + k) % 26 + 65)
        else:
            ciphertext += ch

    return ciphertext


# Caesar Cipher Decryption Function
def caesard(k, y):
    plaintext = ""

    for ch in y.upper():
        if ch.isalpha():
            plaintext += chr((ord(ch) - 65 - k) % 26 + 65)
        else:
            plaintext += ch

    return plaintext


# ================= Main Program =================

# Roll Number
roll_no = 1

# Secure Key
k = roll_no % 26

# Plaintext (Your Full Name)
x = "AARYA THAPA"

# ---------------- Sender Side ----------------
print("========== SENDER ==========")
print("Plaintext :", x)
print("Key       :", k)

# Encrypt the message
y = caesare(k, x)

print("Ciphertext:", y)

# Simulate sending
print("\nSending Ciphertext and Key...")
print("Ciphertext Sent:", y)
print("Key Sent       :", k)

# ---------------- Receiver Side ----------------
print("\n========== RECEIVER ==========")
print("Received Ciphertext:", y)
print("Received Key       :", k)

# Decrypt the message
received_text = caesard(k, y)

print("Recovered Plaintext:", received_text)