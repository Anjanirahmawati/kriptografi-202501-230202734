import hashlib

# hash MD5 target (contoh: password = "password123")
target_hash = "482c811da5d5b4bc6d497ffa98491e38"

# dictionary sederhana
wordlist = [
    "123456",
    "password",
    "admin",
    "password123",
    "qwerty"
]

def md5_hash(text):
    return hashlib.md5(text.encode()).hexdigest()

for word in wordlist:
    hashed = md5_hash(word)
    print(f"Mencoba: {word} -> {hashed}")
    if hashed == target_hash:
        print(f"\n[✓] Password ditemukan: {word}")
        break
