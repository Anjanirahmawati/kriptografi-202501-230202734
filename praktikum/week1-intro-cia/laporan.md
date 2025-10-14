# Laporan Praktikum Kriptografi
Minggu ke-: 1
Topik: [introcia]  
Nama: [Anjani Rahmawati]  
NIM: [230202734]  
Kelas: [5IKRB]  

---

## 1. Tujuan
Tujuan dari praktikum ini adalah untuk memahami konsep dasar keamanan informasi melalui tiga pilar utama CIA Triad (Confidentiality, Integrity, Availability). Selain itu, mahasiswa diharapkan dapat mengenali pentingnya penerapan prinsip CIA dalam sistem keamanan digital dan jaringan komputer.

---

## 2. Dasar Teori
Kriptografi merupakan ilmu yang mempelajari teknik untuk menjaga kerahasiaan dan keamanan informasi agar tidak dapat diakses oleh pihak yang tidak berwenang. Dalam dunia keamanan informasi, terdapat tiga komponen utama yang dikenal sebagai CIA Triad, yaitu Confidentiality, Integrity, dan Availability.  

Confidentiality (Kerahasiaan) memastikan bahwa data hanya dapat diakses oleh pihak yang berwenang melalui teknik seperti enkripsi.  
Integrity (Integritas) menjamin bahwa data tidak diubah tanpa izin, dengan cara verifikasi menggunakan hash atau tanda tangan digital.  
Availability (Ketersediaan)  memastikan bahwa sistem dan data selalu dapat diakses kapan pun dibutuhkan oleh pengguna yang berhak.

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
# contoh potongan kode
def encrypt(text, key):
    return ...
```
)

---

## 6. Hasil dan Pembahasan
(- Lampirkan screenshot hasil eksekusi program (taruh di folder `screenshots/`).  
- Berikan tabel atau ringkasan hasil uji jika diperlukan.  
- Jelaskan apakah hasil sesuai ekspektasi.  
- Bahas error (jika ada) dan solusinya. 

Hasil eksekusi program Caesar Cipher:

![Hasil Eksekusi](screenshots/output.png)
![Hasil Input](screenshots/input.png)
![Hasil Output](screenshots/output.png)
)

---

## 7. Jawaban Pertanyaan
(Jawab pertanyaan diskusi yang diberikan pada modul.  
- Pertanyaan 1: …  
- Pertanyaan 2: …  
)
---

## 8. Kesimpulan
(Tuliskan kesimpulan singkat (2–3 kalimat) berdasarkan percobaan.  )

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
Author: Nama Mahasiswa <email>
Date:   2025-09-20

    week2-cryptosystem: implementasi Caesar Cipher dan laporan )
```
### Langkah 4 — Quiz Singkat
Jawab pertanyaan berikut di laporan:  
1. Siapa tokoh yang dianggap sebagai bapak kriptografi modern?  
Tokoh yang dianggap sebagai bapak kriptografi modern adalah Claude E. Shannon.  
   Ia memperkenalkan dasar teori kriptografi modern melalui publikasinya berjudul *“Communication Theory of Secrecy Systems”* pada tahun 1949, yang menjelaskan konsep keamanan informasi secara matematis.
2. Sebutkan algoritma kunci publik yang populer digunakan saat ini.
Algoritma kunci publik yang paling populer digunakan adalah RSA (Rivest–Shamir–Adleman) dan Elliptic Curve Cryptography (ECC).  
   RSA banyak digunakan untuk enkripsi dan tanda tangan digital, sedangkan ECC digunakan karena tingkat keamanan tinggi dengan panjang kunci yang lebih pendek.  
3. Apa perbedaan utama antara kriptografi klasik dan kriptografi modern?  
Perbedaan utamanya terletak pada metode dan kompleksitas algoritma:
   - Kriptografi klasik menggunakan teknik sederhana seperti substitusi dan transposisi huruf (contoh: Caesar Cipher, Vigenère Cipher).  
   - Kriptografi modern menggunakan prinsip matematika dan komputasi kompleks, serta mendukung penggunaan kunci publik dan privat (contoh: AES, RSA, ECC).