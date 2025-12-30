# Laporan Praktikum Kriptografi
Minggu ke-: 12  
Topik: [aplikasi_tls]  
Nama: [Anjani rahmawati]  
NIM: [230202734]  
Kelas: [5ikrb]  

---

## 1. Tujuan

---

1. Analisis penggunaan kriptografi pada email dan SSL/TLS

Kriptografi digunakan pada email untuk menjaga kerahasiaan, integritas, dan keaslian pesan. Mekanisme seperti enkripsi end-to-end (PGP/S-MIME) memastikan isi email hanya dapat dibaca oleh pengirim dan penerima yang sah, sedangkan digital signature menjamin bahwa pesan tidak diubah selama pengiriman.
Pada SSL/TLS, kriptografi digunakan untuk mengamankan komunikasi antara client dan server melalui handshake, pertukaran kunci, serta penggunaan sertifikat digital sehingga data yang dikirimkan terlindungi dari penyadapan dan serangan pihak tidak berwenang.

---

2. Penjelasan enkripsi dalam transaksi e-commerce

Dalam transaksi e-commerce, enkripsi berperan penting untuk melindungi data sensitif seperti informasi akun, password, dan data pembayaran. Protokol HTTPS (SSL/TLS) mengenkripsi data sebelum dikirim melalui jaringan, sehingga meskipun data disadap, isinya tidak dapat dibaca. Selain itu, penggunaan sertifikat digital membantu memastikan identitas situs e-commerce sehingga meningkatkan kepercayaan pengguna dalam melakukan transaksi online.

---

3. Evaluasi isu etika dan privasi dalam penggunaan kriptografi

Penggunaan kriptografi memiliki dampak positif terhadap perlindungan privasi dan keamanan data pribadi, namun juga menimbulkan isu etika seperti penyalahgunaan enkripsi untuk aktivitas ilegal. Oleh karena itu, diperlukan keseimbangan antara hak privasi pengguna dan kepentingan keamanan publik. Penggunaan kriptografi harus dilakukan secara bertanggung jawab, sesuai dengan hukum dan etika, agar keamanan data tetap terjaga tanpa melanggar hak pihak lain.

---

## 2. Dasar Teori
Kriptografi merupakan teknik pengamanan data yang bertujuan untuk menjaga kerahasiaan (confidentiality), keutuhan (integrity), dan keaslian (authentication) informasi. Dalam komunikasi digital, kriptografi digunakan untuk mengenkripsi data sehingga hanya pihak yang berwenang yang dapat membaca isi informasi tersebut. Algoritma kriptografi terbagi menjadi kriptografi simetris (menggunakan satu kunci yang sama) dan kriptografi asimetris (menggunakan pasangan kunci publik dan privat).

Protokol SSL/TLS (Secure Sockets Layer / Transport Layer Security) adalah standar keamanan yang digunakan untuk melindungi pertukaran data antara client dan server di jaringan internet. TLS bekerja melalui proses handshake yang melibatkan autentikasi server menggunakan sertifikat digital, pertukaran kunci secara aman, dan pembentukan saluran komunikasi terenkripsi. Penerapan TLS ditandai dengan penggunaan HTTPS, yang berfungsi mencegah serangan seperti penyadapan (eavesdropping) dan man-in-the-middle.

Dalam sistem e-commerce, kriptografi berperan penting dalam mengamankan transaksi elektronik, khususnya pada proses login, pemesanan, dan pembayaran online. Enkripsi melindungi data sensitif seperti identitas pengguna dan informasi kartu pembayaran, sementara mekanisme autentikasi dan sertifikat digital meningkatkan kepercayaan antara konsumen dan penyedia layanan. Dengan penerapan kriptografi yang tepat, transaksi e-commerce dapat dilakukan secara aman dan terpercaya.

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
1. Membuat file `aplikasi_tls` di folder `praktikum/week12-E-commerce/src/`.
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

![Hasil Eksekusi](screenshots/hasil.png)
)

---

## 7. Jawaban Pertanyaan
1. Apa perbedaan utama antara HTTP dan HTTPS?

Perbedaan utama antara HTTP dan HTTPS terletak pada aspek keamanannya. HTTP mengirimkan data dalam bentuk teks biasa (plain text) sehingga mudah disadap oleh pihak tidak berwenang. Sementara itu, HTTPS menggunakan SSL/TLS untuk mengenkripsi data yang dikirim antara client dan server, sehingga informasi menjadi lebih aman. Selain itu, HTTPS juga menyediakan autentikasi server melalui sertifikat digital, yang tidak dimiliki oleh HTTP.

---

2. Mengapa sertifikat digital menjadi penting dalam komunikasi TLS?

Sertifikat digital penting dalam komunikasi TLS karena berfungsi untuk memverifikasi identitas server yang diakses oleh pengguna. Sertifikat ini dikeluarkan oleh Certificate Authority (CA) yang terpercaya, sehingga pengguna dapat memastikan bahwa mereka terhubung ke server yang sah, bukan server palsu. Dengan adanya sertifikat digital, risiko serangan seperti man-in-the-middle dapat diminimalkan dan kepercayaan dalam komunikasi online dapat ditingkatkan.

---

3. Bagaimana kriptografi mendukung privasi dalam komunikasi digital, tetapi sekaligus menimbulkan tantangan hukum dan etika?

Kriptografi mendukung privasi dengan melindungi data pribadi melalui enkripsi, sehingga hanya pihak yang berwenang yang dapat mengakses informasi tersebut. Namun, penggunaan kriptografi juga menimbulkan tantangan hukum dan etika karena dapat disalahgunakan untuk menyembunyikan aktivitas ilegal. Oleh karena itu, diperlukan keseimbangan antara perlindungan privasi individu dan penegakan hukum, agar kriptografi digunakan secara bertanggung jawab dan sesuai dengan peraturan yang berlaku.

---

## 8. Kesimpulan
dapat disimpulkan bahwa kriptografi memiliki peran penting dalam mengamankan komunikasi digital. Penggunaan protokol TLS/SSL pada HTTPS mampu melindungi data dari penyadapan, menjaga integritas informasi, serta memastikan keaslian pihak yang berkomunikasi melalui sertifikat digital.

Selain itu, dalam sistem e-commerce, kriptografi memberikan perlindungan terhadap data sensitif pengguna seperti informasi akun dan transaksi pembayaran, sehingga meningkatkan kepercayaan konsumen dalam melakukan transaksi online. Meskipun kriptografi mendukung privasi dan keamanan data, penerapannya juga menimbulkan tantangan hukum dan etika, sehingga diperlukan penggunaan yang bertanggung jawab dan sesuai dengan peraturan yang berlaku.

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
Date:   2025-09-20

    week12-aplikasi_tls )
```
