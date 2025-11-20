# Laporan Praktikum Kriptografi
Minggu ke-: 7
Topik: [diffie-hellman]  
Nama: [Anjani rahmawati]  
NIM: [230202734]  
Kelas: [5ikrb]  

---

## 1. Tujuan
Tujuan pembelajaran ketiga adalah agar mahasiswa mampu secara mendalam menganalisis potensi serangan yang dapat terjadi pada protokol Diffie-Hellman, khususnya serangan Man-in-the-Middle (MITM), dengan memahami bagaimana penyerang dapat memotong jalur komunikasi antara dua pihak, menyamar sebagai masing-masing pihak, lalu mengirimkan kunci publik palsu sehingga kedua pihak tidak pernah benar-benar berbagi kunci yang sama; mahasiswa diharapkan dapat menjelaskan langkah-langkah teknik serangan tersebut, seperti manipulasi nilai publik bagaimana penyerang menghasilkan dua kunci rahasia berbeda untuk mengawasi dan memodifikasi pesan, serta mampu menguraikan konsekuensinya terhadap kerahasiaan dan integritas data; selain itu, mahasiswa juga harus memahami alasan protokol ini rentan tanpa mekanisme autentikasi, dan mampu menjelaskan strategi pencegahan seperti penggunaan digital signature, sertifikat, autentikasi dua arah, atau integrasi protokol Diffie-Hellman ke dalam protokol komunikasi aman seperti TLS/HTTPS.  

---

## 2. Dasar Teori
Protokol Diffie–Hellman adalah metode pertukaran kunci yang memungkinkan dua pihak menghasilkan sebuah kunci rahasia bersama meskipun berkomunikasi melalui jaringan yang tidak aman. Protokol ini memanfaatkan bilangan prima besar p dan generator g di mana masing-masing pihak memilih kunci privat secara acak dan menghitung kunci publik menggunakan operasi eksponensial modulo. Nilai publik itu dipertukarkan, dan kedua pihak dapat menghitung kunci rahasia yang sama melalui sifat matematika gb mod p yang kemudian digunakan untuk komunikasi terenkripsi.
Keamanan Diffie–Hellman didasarkan pada sulitnya memecahkan masalah logaritma diskrit, yaitu mencari nilai eksponen dari persamaan gx mod p Masalah ini sangat sulit diselesaikan jika bilangan yang digunakan berukuran besar, sehingga pihak ketiga tidak dapat mengetahui kunci rahasia hanya dari nilai publik. Meski demikian, Diffie–Hellman tidak memiliki mekanisme autentikasi bawaan yang memastikan identitas pihak yang terlibat dalam pertukaran kunci.
Tanpa autentikasi, protokol ini rentan terhadap serangan Man-in-the-Middle (MITM), di mana penyerang dapat memotong dan menggantikan nilai publik untuk menciptakan dua kunci rahasia berbeda dan memantau seluruh komunikasi. Oleh karena itu, implementasi modern biasanya menggabungkan Diffie–Hellman dengan autentikasi seperti tanda tangan digital atau sertifikat, atau menggunakannya dalam protokol yang lebih aman seperti TLS/HTTPS agar proses pertukaran kunci lebih terjamin dan tidak dapat disusupi.

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
import random

# parameter umum (disepakati publik)
p = 23  # bilangan prima
g = 5   # generator

# private key masing-masing pihak
a = random.randint(1, p-1)  # secret Alice
b = random.randint(1, p-1)  # secret Bob

# public key
A = pow(g, a, p)
B = pow(g, b, p)

# exchange public key
shared_secret_A = pow(B, a, p)
shared_secret_B = pow(A, b, p)

print("Kunci bersama Alice :", shared_secret_A)
print("Kunci bersama Bob   :", shared_secret_B)


---

## 6. Hasil dan Pembahasan
- Lampirkan screenshot hasil eksekusi program (taruh di folder `screenshots/`).  
- Berikan tabel atau ringkasan hasil uji jika diperlukan.  
- Jelaskan apakah hasil sesuai ekspektasi.  
- Bahas error (jika ada) dan solusinya. 

Hasil eksekusi program Caesar Cipher:

![Hasil Eksekusi](/praktikum/week7-diffie-hellman/screenshots.py/Hasil_Eksekusi.png)


---

## 7. Jawaban Pertanyaan
1. Mengapa Diffie-Hellman memungkinkan pertukaran kunci di saluran publik?

Karena Diffie-Hellman menggunakan operasi eksponensial modulo dengan bilangan prima besar, sehingga meskipun nilai publik dipertukarkan secara terbuka, pihak ketiga tidak dapat menghitung kunci rahasia. Hal ini disebabkan oleh sulitnya memecahkan logaritma diskrit, sehingga hanya kedua pihak yang memiliki kunci privat masing-masing yang dapat menghasilkan kunci rahasia yang sama.

---

2. Apa kelemahan utama protokol Diffie-Hellman murni?

Kelemahan utamanya adalah tidak adanya autentikasi. Protokol ini tidak dapat memastikan apakah pihak yang bertukar kunci adalah pihak yang sebenarnya, sehingga membuka peluang terjadinya serangan Man-in-the-Middle (MITM). Selain itu, nilai publik yang dipertukarkan dapat dimanipulasi oleh penyerang tanpa terdeteksi.

---
3. Bagaimana cara mencegah serangan MITM pada protokol ini?

Serangan MITM dapat dicegah dengan menambahkan mekanisme autentikasi, seperti tanda tangan digital, sertifikat digital (SSL/TLS), autentikasi dua arah, atau mengintegrasikan Diffie-Hellman ke dalam protokol yang aman seperti HTTPS. Dengan autentikasi, pihak yang terlibat dapat memverifikasi identitas lawan komunikasi sehingga penyerang tidak dapat menyamar di tengah proses pertukaran kunci.

---

## 8. Kesimpulan
Protokol Diffie–Hellman merupakan metode pertukaran kunci yang aman karena memanfaatkan operasi matematika yang sulit dipecahkan, yaitu logaritma diskrit, sehingga memungkinkan dua pihak membentuk kunci rahasia bersama meskipun berkomunikasi melalui saluran publik. Namun, protokol ini memiliki kelemahan penting, yaitu tidak adanya mekanisme autentikasi sehingga rentan terhadap serangan Man-in-the-Middle (MITM). Untuk memastikan keamanan pertukaran kunci, Diffie–Hellman harus dilengkapi dengan autentikasi seperti tanda tangan digital, sertifikat, atau digunakan dalam protokol komunikasi yang aman seperti TLS/HTTPS. Dengan kombinasi ini, proses pertukaran kunci menjadi lebih kuat, terlindungi, dan dapat digunakan secara aman dalam berbagai sistem keamanan modern.

---

## 9. Daftar Pustaka
(Cantumkan referensi yang digunakan.  
Contoh:  
- Katz, J., & Lindell, Y. *Introduction to Modern Cryptography*.  
- Stallings, W. *Cryptography and Network Security*.  )

---

## 10. Commit Log
Tuliskan bukti commit Git yang relevan.  
Contoh:
```
commit e3dfd9082d913a300c8e7c2ff5fed37b3c35fc10
Author: Anjani rahmawati <anjanirahmawati1204@gmail.com>
Date:   2025-11-20

    week7-diffie-hellman
```
