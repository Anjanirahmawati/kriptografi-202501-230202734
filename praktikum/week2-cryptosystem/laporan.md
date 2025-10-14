# Laporan Praktikum Kriptografi
Minggu ke-: 2  
Topik: [cryptosystem]  
Nama: [Anjani Rahmawati]  
NIM: [230202734]  
Kelas: [5ikrb]  

---

## 1. Tujuan
1.Mengidentifikasi komponen dasar kriptosistem seperti plaintext, ciphertext, kunci, dan algoritma.

2.Memahami proses enkripsi dan dekripsi menggunakan algoritma sederhana.

3.Menjelaskan perbedaan antara sistem kriptografi simetris dan asimetris.

---

## 2. Dasar Teori
(Kriptosistem adalah sistem yang digunakan untuk menjaga kerahasiaan informasi melalui proses enkripsi dan dekripsi.

Enkripsi adalah proses mengubah pesan asli (plaintext) menjadi bentuk tidak terbaca (ciphertext) menggunakan algoritma tertentu dan kunci.

Dekripsi adalah proses mengembalikan ciphertext ke bentuk aslinya menggunakan kunci yang sesuai.
Salah satu algoritma paling sederhana adalah Caesar Cipher, yaitu algoritma substitusi yang menggeser setiap huruf dalam teks sejauh n posisi dalam alfabet. Operasi yang digunakan adalah modular aritmetika (mod 26).

Kriptografi terbagi menjadi dua jenis utama:

Simetris, di mana kunci enkripsi dan dekripsi sama (contoh: AES, DES).

Asimetris, di mana digunakan pasangan kunci publik dan privat yang berbeda (contoh: RSA, ECC).)

---

## 3. Alat dan Bahan
Python 3.11

Visual Studio Code

Git & GitHub

---

## 4. Langkah Percobaan
Membuat folder praktikum/week2-cryptosystem/ dengan struktur sesuai panduan.

Membuat file simple_crypto.py di dalam folder src/.

Menulis program enkripsi–dekripsi menggunakan metode Caesar Cipher yang dapat mengenkripsi huruf dan angka.

Menjalankan program menggunakan perintah:

python src/simple_crypto.py


Menyimpan hasil output program (screenshot) ke folder screenshots/hasil_eksekusi.png.

---

## 5. Source Code
(Salin kode program utama yang dibuat atau dimodifikasi.  
Gunakan blok kode:

```python
# file: praktikum/week2-cryptosystem/src/simple_crypto_with_digits.py

def encrypt(plaintext, key):
    """
    Encrypt plaintext:
    - letters: rotated within A-Z or a-z (26)
    - digits: rotated within 0-9 (10)
    - other chars: unchanged
    """
    result = []
    for char in plaintext:
        if char.isalpha():
            shift = 65 if char.isupper() else 97
            result.append(chr((ord(char) - shift + key) % 26 + shift))
        elif char.isdigit():
            result.append(chr((ord(char) - 48 + key) % 10 + 48))
        else:
            result.append(char)
    return "".join(result)


def decrypt(ciphertext, key):
    """
    Decrypt ciphertext using inverse rotation.
    """
    result = []
    for char in ciphertext:
        if char.isalpha():
            shift = 65 if char.isupper() else 97
            result.append(chr((ord(char) - shift - key) % 26 + shift))
        elif char.isdigit():
            result.append(chr((ord(char) - 48 - key) % 10 + 48))
        else:
            result.append(char)
    return "".join(result)


if __name__ == "__main__":
    message = "<230202734><anjani rahmawati>"
    key = 5  

    enc = encrypt(message, key)
    dec = decrypt(enc, key)

    print("Plaintext :", message)
    print("Ciphertext:", enc)
    print("Decrypted :", dec)


## 6. Hasil dan Pembahasan
(- Lampirkan screenshot hasil eksekusi program (taruh di folder `screenshots/`).  
- Berikan tabel atau ringkasan hasil uji jika diperlukan.  
- Jelaskan apakah hasil sesuai ekspektasi.  
- Bahas error (jika ada) dan solusinya. 

Hasil eksekusi program Caesar Cipher:

![Hasil Eksekusi](/praktikum/week2-cryptosystem/screenshots/hasil_eksekusi.png.png)
![Diagram](/praktikum/week2-cryptosystem/screenshots/diagram_kriptosistem.png)
)

---

## 7. Jawaban Pertanyaan
1. Sebutkan komponen utama dalam sebuah kriptosistem.
Komponen utamanya adalah:

Plaintext: pesan asli yang ingin diamankan.

Ciphertext: pesan yang sudah dienkripsi.

Kunci (key): nilai rahasia yang digunakan dalam proses enkripsi dan dekripsi.

Algoritma: aturan atau metode matematika untuk melakukan enkripsi dan dekripsi.

2. Apa kelebihan dan kelemahan sistem simetris dibandingkan asimetris?

Kelebihan: proses enkripsi dan dekripsi lebih cepat dan efisien.

Kelemahan: distribusi kunci sulit karena kunci yang sama harus dijaga kerahasiaannya oleh kedua pihak.

3. Mengapa distribusi kunci menjadi masalah utama dalam kriptografi simetris?
Karena jika kunci rahasia diketahui pihak lain saat dikirimkan, maka keamanan seluruh sistem dapat terancam. Distribusi kunci memerlukan saluran komunikasi yang aman agar tidak disadap.

---

## 8. Kesimpulan
Praktikum ini menunjukkan bahwa proses enkripsi dan dekripsi dapat disimulasikan dengan algoritma sederhana seperti Caesar Cipher. Mahasiswa dapat memahami konsep dasar kriptosistem, fungsi kunci, serta perbedaan antara sistem simetris dan asimetris.

---

## 9. Daftar Pustaka


---

## 10. Commit Log
Tuliskan bukti commit Git yang relevan.  
Contoh:
```
commit abc12345
Author: Anjani Rahmawati <anjanirahmawati1204@gmail.com>
Date:   2025-10-14

    week2-cryptosystem: implementasi Caesar Cipher dan laporan )
```
