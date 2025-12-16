# Laporan Praktikum Kriptografi
Minggu ke-: 9  
Topik: [digital_signature]  
Nama: [Anjani Rahmawati]  
NIM: [230202734]  
Kelas: [5IKRB]  

---

## 1. Tujuan
# 09 Digital Signature (RSA/DSA)

## Tujuan Pembelajaran

---

## 1. Implementasi Tanda Tangan Digital Menggunakan RSA/DSA

Digital Signature (tanda tangan digital) merupakan teknik kriptografi yang digunakan untuk menjamin keaslian pengirim, integritas pesan, dan mencegah penyangkalan (non-repudiation). Proses utama dalam digital signature adalah melakukan hashing pada pesan dan mengenkripsi hasil hash tersebut menggunakan kunci privat.

---

### Implementasi Digital Signature dengan RSA
RSA menggunakan pasangan kunci publik dan privat. Kunci privat digunakan untuk membuat tanda tangan digital, sedangkan kunci publik digunakan untuk melakukan verifikasi.

--- 

Langkah-langkah:
1. Membuat pasangan kunci RSA (public key dan private key).
2. Melakukan hashing terhadap pesan menggunakan algoritma hash (misalnya SHA-256).
3. Mengenkripsi hash pesan menggunakan private key RSA.
4. Hasil enkripsi hash menjadi digital signature.

---  

Implementasi Digital Signature dengan DSA
DSA (Digital Signature Algorithm) merupakan algoritma yang secara khusus digunakan untuk pembuatan tanda tangan digital dan tidak digunakan untuk enkripsi data.

--- 

Langkah-langkah:

1. Menentukan parameter DSA (p, q, g).

2. Membuat pasangan kunci DSA (private key dan public key).

3. Melakukan hashing pesan.

4. Menghasilkan tanda tangan digital berupa dua nilai, yaitu (r, s).

---  

2. Verifikasi Keaslian Tanda Tangan Digital

Verifikasi tanda tangan digital dilakukan oleh penerima pesan untuk memastikan bahwa pesan benar-benar berasal dari pengirim yang sah dan tidak mengalami perubahan.

Verifikasi Digital Signature Menggunakan RSA

Langkah-langkah verifikasi RSA:

1. Menerima pesan dan digital signature.
2. Melakukan hashing ulang terhadap pesan.
3. Mendekripsi digital signature menggunakan public key RSA.
4. Membandingkan hasil dekripsi dengan hash pesan.

Jika hasilnya sama, maka tanda tangan digital dinyatakan valid.

---

Verifikasi Digital Signature Menggunakan DSA

Langkah-langkah verifikasi DSA:

1. Melakukan hashing pesan.

2. Menggunakan public key serta nilai tanda tangan (r, s).

3. Melakukan perhitungan matematis sesuai algoritma DSA.

4. Membandingkan hasil perhitungan dengan nilai signature.

Jika hasil perhitungan sesuai, maka tanda tangan digital dinyatakan valid.

3. Manfaat Tanda Tangan Digital dalam Otentikasi Pesan dan Integritas Data
Otentikasi Pesan

Digital signature memastikan bahwa pesan benar-benar berasal dari pengirim yang sah sehingga dapat mencegah pemalsuan identitas.
Integritas Data Digital signature menjamin bahwa isi pesan tidak mengalami perubahan selama proses pengiriman. Perubahan sekecil apa pun pada pesan akan menyebabkan tanda tangan digital menjadi tidak valid.Non-Repudiation Tanda tangan digital mencegah pengirim menyangkal bahwa ia telah mengirim atau menandatangani pesan karena hanya pemilik private key yang dapat membuat signature.

Keamanan Transaksi Digital

Digital signature banyak digunakan dalam berbagai sistem digital, seperti:
1. E-banking
2. E-commerce
3. Sertifikat SSL/TLS
Dokumen elektronik dan e-signature

---

## 2. Dasar Teori

Digital Signature (tanda tangan digital) merupakan teknik kriptografi yang digunakan untuk menjamin keaslian pengirim, integritas pesan, dan non-repudiation (pengirim tidak dapat menyangkal pesan yang telah dikirim). Tanda tangan digital dibuat dengan cara melakukan hashing terhadap pesan menggunakan fungsi hash kriptografis (seperti SHA-256), kemudian mengenkripsi hasil hash tersebut menggunakan kunci privat pengirim. Hasil enkripsi ini menjadi tanda tangan digital yang dikirim bersama pesan.

Algoritma RSA dan DSA merupakan algoritma kriptografi kunci publik yang umum digunakan dalam implementasi tanda tangan digital. RSA menggunakan pasangan kunci publik dan privat yang didasarkan pada kesulitan faktorisasi bilangan prima besar. Dalam tanda tangan digital RSA, kunci privat digunakan untuk membuat tanda tangan, sedangkan kunci publik digunakan untuk memverifikasi keaslian tanda tangan tersebut.

DSA (Digital Signature Algorithm) adalah algoritma yang dirancang khusus untuk pembuatan tanda tangan digital dan tidak digunakan untuk enkripsi data. DSA bergantung pada konsep matematika modular aritmetika dan masalah logaritma diskrit. Proses tanda tangan DSA menghasilkan dua nilai, yaitu (r, s), yang digunakan dalam proses verifikasi untuk memastikan bahwa pesan tidak mengalami perubahan dan benar-benar berasal dari pengirim yang sah.


---

## 3. Alat dan Bahan
(- Python 3.x  
- Visual Studio Code / editor lain  
- Git dan akun GitHub  
- Library tambahan (misalnya pycryptodome, jika diperlukan)  )

---

## 4. Langkah Percobaan
(Tuliskan langkah yang dilakukan sesuai instruksi.  
Contoh format:
1. Membuat file `caesar_cipher.py` di folder `praktikum/week2-cryptosystem/src/`.
2. Menyalin kode program dari panduan praktikum.
3. Menjalankan program dengan perintah `python caesar_cipher.py`.)

---

## 5. Source Code
(Salin kode program utama yang dibuat atau dimodifikasi.  
Gunakan blok kode:

```python
from Crypto.PublicKey import RSA
from Crypto.Signature import pkcs1_15
from Crypto.Hash import SHA256

# Generate pasangan kunci RSA
key = RSA.generate(2048)
private_key = key
public_key = key.publickey()

# Pesan yang akan ditandatangani
message = b"Hello, ini pesan penting."
h = SHA256.new(message)

# Buat tanda tangan dengan private key
signature = pkcs1_15.new(private_key).sign(h)
print("Signature:", signature.hex())
try:
    pkcs1_15.new(public_key).verify(h, signature)
    print("Verifikasi berhasil: tanda tangan valid.")
except (ValueError, TypeError):
    print("Verifikasi gagal: tanda tangan tidak valid.")
    # Modifikasi pesan
fake_message = b"Hello, ini pesan palsu."
h_fake = SHA256.new(fake_message)

try:
    pkcs1_15.new(public_key).verify(h_fake, signature)
    print("Verifikasi berhasil (seharusnya gagal).")
except (ValueError, TypeError):
    print("Verifikasi gagal: tanda tangan tidak cocok dengan pesan.")
```
)

---

## 6. Hasil dan Pembahasan
(- Lampirkan screenshot hasil eksekusi program (taruh di folder `screenshots/`).  
- Berikan tabel atau ringkasan hasil uji jika diperlukan.  
- Jelaskan apakah hasil sesuai ekspektasi.  
- Bahas error (jika ada) dan solusinya. 

Hasil eksekusi program Caesar Cipher:

![Hasil Eksekusi](screenshots/hasil.png)
)

---

## Pertanyaan Diskusi

### 1. Apa perbedaan utama antara enkripsi RSA dan tanda tangan digital RSA?
Perbedaan utama antara enkripsi RSA dan tanda tangan digital RSA terletak pada tujuan penggunaan dan jenis kunci yang digunakan. Enkripsi RSA bertujuan untuk menjaga kerahasiaan pesan, di mana pesan dienkripsi menggunakan public key penerima dan hanya dapat didekripsi menggunakan private key penerima. Sebaliknya, tanda tangan digital RSA bertujuan untuk menjamin keaslian dan integritas pesan. Pada tanda tangan digital RSA, hash dari pesan dienkripsi menggunakan private key pengirim dan diverifikasi menggunakan public key pengirim.

---

### 2. Mengapa tanda tangan digital menjamin integritas dan otentikasi pesan?
Tanda tangan digital menjamin integritas pesan karena proses penandatanganan melibatkan hashing pesan. Jika pesan diubah, hasil hash akan berbeda sehingga verifikasi tanda tangan gagal. Selain itu, tanda tangan digital menjamin otentikasi pesan karena hanya pemilik private key yang sah yang dapat membuat tanda tangan tersebut, sehingga penerima dapat memastikan identitas pengirim menggunakan public key yang sesuai.

---

### 3. Bagaimana peran Certificate Authority (CA) dalam sistem tanda tangan digital modern?
Certificate Authority (CA) berperan sebagai pihak tepercaya yang menerbitkan dan memverifikasi sertifikat digital. CA memastikan bahwa public key benar-benar milik entitas yang sah dengan cara melakukan validasi identitas sebelum menerbitkan sertifikat. Dalam sistem tanda tangan digital modern, CA membantu membangun kepercayaan, mencegah pemalsuan identitas, serta memastikan keamanan komunikasi melalui penggunaan sertifikat digital yang valid.

---

## 8. Kesimpulan
Berdasarkan praktikum yang telah dilakukan, dapat disimpulkan bahwa algoritma RSA dan DSA dapat digunakan untuk mengimplementasikan tanda tangan digital secara efektif. Proses penandatanganan dan verifikasi berhasil membuktikan bahwa tanda tangan digital mampu menjamin keaslian pengirim serta menjaga integritas pesan. Dengan demikian, digital signature memiliki peran penting dalam mendukung keamanan komunikasi dan transaksi digital modern.


---

## 9. Daftar Pustaka
(Cantumkan referensi yang digunakan.  
Contoh:  
- Katz, J., & Lindell, Y. *Introduction to Modern Cryptography*.  
- Stallings, W. *Cryptography and Network Security*.  )

---

## 10. Commit Log
(Tuliskan bukti commit Git yang relevan.  
Contoh:
```
commit abc12345
Author: Anjani rahmawati <anjanirahmawati1204@gmail.com>
Date:   2025-12-16

    week2-cryptosystem: implementasi Caesar Cipher dan laporan )
```
