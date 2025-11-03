# Laporan Praktikum Kriptografi
Minggu ke-: 4  
Topik: [entropy]  
Nama: [Anjani Rahmawati]  
NIM: [230202734]  
Kelas: [5ikrb]  

---

## 1. Tujuan
Setelah mengikuti praktikum ini, mahasiswa diharapkan mampu:

Menyelesaikan perhitungan sederhana terkait entropi kunci.
Menggunakan teorema Euler pada contoh perhitungan modular & invers.
Menghitung unicity distance untuk ciphertext tertentu.
Menganalisis kekuatan kunci berdasarkan entropi dan unicity distance.
Mengevaluasi potensi serangan brute force pada kriptosistem sederhana.


---

## 2. Dasar Teori
Entropy dalam kriptografi merupakan ukuran tingkat keacakan atau ketidakpastian dari suatu sistem kunci. Semakin tinggi nilai entropy, semakin besar pula jumlah kemungkinan kunci yang harus diuji, sehingga meningkatkan kekuatan keamanan terhadap serangan brute force. Entropy ideal tercapai ketika setiap simbol atau kunci memiliki probabilitas yang sama untuk muncul, menandakan sistem memiliki distribusi acak yang sempurna.

Unicity distance adalah panjang minimum ciphertext yang diperlukan agar kunci dapat diidentifikasi secara unik oleh penyerang. Konsep ini digunakan untuk mengevaluasi seberapa banyak data terenkripsi yang dibutuhkan agar analisis kriptografi bisa berhasil menemukan kunci sebenarnya. Semakin besar nilai unicity distance, semakin sulit sistem kriptografi dipecahkan dengan ciphertext terbatas.

Brute force sendiri merupakan metode serangan yang mencoba seluruh kemungkinan kunci hingga menemukan yang benar. Hubungan antara entropy, unicity distance, dan brute force menunjukkan bahwa semakin tinggi entropy dan unicity distance, semakin kuat sistem kriptografi terhadap serangan brute force, karena kompleksitas pencarian kunci meningkat secara eksponensial.

---

## 3. Alat dan Bahan
- Python 3.x  
- Visual Studio Code / editor lain  
- Git dan akun GitHub  
- Library tambahan (misalnya pycryptodome, jika diperlukan)  

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
1. Arti dari nilai entropy dalam konteks kekuatan kunci

Entropy menggambarkan tingkat ketidakpastian atau keacakan pada suatu kunci kriptografi.

Semakin tinggi nilai entropy, semakin sulit untuk menebak kunci karena kombinasi yang mungkin semakin banyak dan acak.

Sebaliknya, entropy rendah berarti pola kunci bisa ditebak lebih mudah.
2. Pentingnya unicity distance dalam menentukan keamanan cipher

Unicity distance (UD) adalah jumlah minimum ciphertext yang dibutuhkan agar bisa menentukan kunci secara unik, dengan asumsi penyerang tahu sebagian pola bahasa plaintext.

Jika panjang ciphertext < UD, maka banyak kemungkinan kunci masih valid → cipher masih aman.

Jika panjang ciphertext ≥ UD, penyerang dapat menemukan kunci yang benar dengan analisis statistik → cipher tidak aman.
3. Mengapa brute force masih menjadi ancaman meskipun algoritma sudah kuat

Walaupun algoritma modern seperti AES sangat kuat secara matematis, brute force tetap ancaman karena:

Komputer semakin cepat dan murah, termasuk penggunaan GPU dan komputasi paralel.

Kesalahan implementasi (panjang kunci kurang, penyimpanan kunci tidak aman, atau pemakaian ulang kunci) membuat brute force lebih mudah.

Serangan brute force tidak perlu tahu algoritma — hanya mencoba semua kemungkinan kunci sampai berhasil.
---

## 8. Kesimpulan
Dari hasil percobaan, diketahui bahwa algoritma Caesar Cipher memiliki entropy rendah karena ruang kuncinya hanya berjumlah 26, sehingga mudah dipecahkan dengan serangan brute force. Nilai unicity distance yang kecil menunjukkan cipher ini tidak cukup kuat untuk melindungi pesan dalam jumlah ciphertext besar. Sebaliknya, algoritma modern seperti AES-128 memiliki entropy dan waktu brute force yang sangat besar, menjadikannya jauh lebih aman untuk digunakan.

---



---

## 10. Commit Log
(Tuliskan bukti commit Git yang relevan.  
Contoh:
```
commit abc12345
Author: Anjani Rahmawati <anjanirahmawati1204@gmail.com>
Date:   2025-09-20

    week2-cryptosystem: implementasi Caesar Cipher dan laporan )
```
