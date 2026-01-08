import random

# Membuat shares
def generate_shares(secret, k, n, prime=2087):
    coeffs = [secret] + [random.randint(1, prime-1) for _ in range(k-1)]

    def f(x):
        return sum(coeffs[i] * (x ** i) for i in range(len(coeffs))) % prime

    shares = [(i, f(i)) for i in range(1, n+1)]
    return shares

# Rekonstruksi secret (Lagrange)
def reconstruct_secret(shares, prime=2087):
    secret = 0
    for i, (xi, yi) in enumerate(shares):
        num, den = 1, 1
        for j, (xj, _) in enumerate(shares):
            if i != j:
                num = (num * (-xj)) % prime
                den = (den * (xi - xj)) % prime
        secret = (secret + yi * num * pow(den, -1, prime)) % prime
    return secret


# ======================
# CONTOH PENGGUNAAN
# ======================
secret = 123
k = 3
n = 5

shares = generate_shares(secret, k, n)
print("Shares:", shares)

recovered = reconstruct_secret(shares[:3])
print("Recovered Secret:", recovered)
