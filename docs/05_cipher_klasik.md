# 05 Cipher Klasik (Caesar, Vigenère, Transposisi)

## Tujuan Pembelajaran
1.Menerapkan algoritma Caesar Cipher untuk enkripsi dan dekripsi teks
Mahasiswa mampu memahami prinsip kerja Caesar Cipher yang menggunakan pergeseran huruf dalam alfabet dengan kunci tertentu.
Tujuannya adalah agar mahasiswa dapat membuat program sederhana yang mengubah pesan teks menjadi bentuk terenkripsi (ciphertext) dan mengembalikannya lagi ke bentuk asli (plaintext) menggunakan logika pergeseran huruf.
2.Menerapkan algoritma Vigenère Cipher dengan variasi kunci
Mahasiswa diharapkan memahami cara kerja Vigenère Cipher yang menggunakan kata kunci untuk menentukan besar pergeseran setiap huruf.
Dengan demikian, mahasiswa dapat membandingkan kompleksitas dan keamanan Vigenère terhadap Caesar Cipher, serta memahami konsep penggunaan key stream dalam kriptografi.
3.Mengimplementasikan algoritma transposisi sederhana
Mahasiswa mampu memahami perbedaan cipher substitusi dan transposisi.
Pada cipher transposisi, posisi huruf pada plaintext ditukar mengikuti pola tertentu tanpa mengubah hurufnya.
Melalui implementasi ini, mahasiswa dapat mempelajari bagaimana pola penataan karakter dapat digunakan sebagai dasar sistem penyandian.
4.Menjelaskan kelemahan algoritma kriptografi klasik
Mahasiswa dapat mengidentifikasi keterbatasan cipher klasik seperti ruang kunci yang kecil, kemudahan diserang menggunakan analisis frekuensi, serta ketidakmampuan melindungi pesan dari serangan modern.
Dengan pemahaman ini, mahasiswa diharapkan mampu menjelaskan mengapa kriptografi klasik hanya digunakan sebagai dasar pembelajaran dan bukan untuk keamanan data masa kini.
---

## Capaian Kegiatan
Pada akhir sesi ini mahasiswa menghasilkan:  
- Program Python untuk Caesar Cipher dan Vigenère Cipher (minimal 2 algoritma klasik).  
- Screenshot hasil uji coba enkripsi dan dekripsi.  
- Laporan singkat yang berisi ringkasan teori, kelemahan algoritma klasik, dan hasil percobaan.  
- Commit Git dengan format `week5-cipher-klasik`.  

---

## Persiapan Lingkungan
1. Buat folder berikut:  
   ```
   praktikum/week5-cipher-klasik/
   ├─ src/
   ├─ screenshots/
   └─ laporan.md
   ```
2. Gunakan Python 3.11 atau lebih baru.  
3. Materi rujukan: Stallings (2017), Bab 3.  

---

## Panduan Langkah demi Langkah

### Langkah 1 — Implementasi Caesar Cipher
```python
def caesar_encrypt(plaintext, key):
    result = ""
    for char in plaintext:
        if char.isalpha():
            shift = 65 if char.isupper() else 97
            result += chr((ord(char) - shift + key) % 26 + shift)
        else:
            result += char
    return result

def caesar_decrypt(ciphertext, key):
    return caesar_encrypt(ciphertext, -key)

# Contoh uji
msg = "CLASSIC CIPHER"
key = 3
enc = caesar_encrypt(msg, key)
dec = caesar_decrypt(enc, key)
print("Plaintext :", msg)
print("Ciphertext:", enc)
print("Decrypted :", dec)
```

---

### Langkah 2 — Implementasi Vigenère Cipher
```python
def vigenere_encrypt(plaintext, key):
    result = []
    key = key.lower()
    key_index = 0
    for char in plaintext:
        if char.isalpha():
            shift = ord(key[key_index % len(key)]) - 97
            base = 65 if char.isupper() else 97
            result.append(chr((ord(char) - base + shift) % 26 + base))
            key_index += 1
        else:
            result.append(char)
    return "".join(result)

def vigenere_decrypt(ciphertext, key):
    result = []
    key = key.lower()
    key_index = 0
    for char in ciphertext:
        if char.isalpha():
            shift = ord(key[key_index % len(key)]) - 97
            base = 65 if char.isupper() else 97
            result.append(chr((ord(char) - base - shift) % 26 + base))
            key_index += 1
        else:
            result.append(char)
    return "".join(result)

# Contoh uji
msg = "KRIPTOGRAFI"
key = "KEY"
enc = vigenere_encrypt(msg, key)
dec = vigenere_decrypt(enc, key)
print("Plaintext :", msg)
print("Ciphertext:", enc)
print("Decrypted :", dec)
```

---

### Langkah 3 — Implementasi Transposisi Sederhana
```python
def transpose_encrypt(plaintext, key=5):
    ciphertext = [''] * key
    for col in range(key):
        pointer = col
        while pointer < len(plaintext):
            ciphertext[col] += plaintext[pointer]
            pointer += key
    return ''.join(ciphertext)

def transpose_decrypt(ciphertext, key=5):
    num_of_cols = int(len(ciphertext) / key + 0.9999)
    num_of_rows = key
    num_of_shaded_boxes = (num_of_cols * num_of_rows) - len(ciphertext)
    plaintext = [''] * num_of_cols
    col = 0
    row = 0
    for symbol in ciphertext:
        plaintext[col] += symbol
        col += 1
        if (col == num_of_cols) or (col == num_of_cols - 1 and row >= num_of_rows - num_of_shaded_boxes):
            col = 0
            row += 1
    return ''.join(plaintext)

# Contoh uji
msg = "TRANSPOSITIONCIPHER"
enc = transpose_encrypt(msg, key=5)
dec = transpose_decrypt(enc, key=5)
print("Plaintext :", msg)
print("Ciphertext:", enc)
print("Decrypted :", dec)
```

---

## Pertanyaan Diskusi
1. Apa kelemahan utama algoritma Caesar Cipher dan Vigenère Cipher?  
2. Mengapa cipher klasik mudah diserang dengan analisis frekuensi?  
3. Bandingkan kelebihan dan kelemahan cipher substitusi vs transposisi.  

---

## Tugas yang Dikumpulkan
1. Implementasi minimal **2 algoritma cipher klasik** (Caesar, Vigenère, atau Transposisi).  
2. Screenshot hasil enkripsi dan dekripsi.  
3. Laporan `laporan.md` berisi:  
   - Penjelasan singkat teori cipher klasik.  
   - Hasil uji implementasi.  
   - Jawaban pertanyaan diskusi.  

Struktur akhir folder:
```
praktikum/week5-cipher-klasik/
 ├─ src/caesar.py
 ├─ src/vigenere.py
 ├─ src/transpose.py
 ├─ screenshots/
 │   └─ hasil.png
 └─ laporan.md
```

Commit dengan pesan:  
```
week5-cipher-klasik
```

---

## Rubrik Penilaian
Mengacu pada RPS Minggu 5: **Total bobot 5% (Implementasi 3%, Upload kode di Git 2%)**  

| Aspek Penilaian            | Bobot | Kriteria                                                                |
|-----------------------------|-------|-------------------------------------------------------------------------|
| Implementasi cipher klasik  | 3%    | Program Caesar, Vigenère, atau Transposisi berjalan sesuai teori        |
| Upload kode di Git & laporan| 2%    | Commit sesuai format, folder rapi, laporan singkat dengan screenshot    |
| Evidence Git & repo         | -     | History commit sesuai instruksi                                         |

---