# Laporan Praktikum Kriptografi
Minggu ke-: 3
Topik: [judul praktikum]  
Nama: [Anjani rahmawati]  
NIM: [230202734]  
Kelas: [5ikrb]  

---

## 1. Tujuan
Tujuan pembelajaran praktikum ini adalah agar mahasiswa memahami pentingnya konsep aritmetika modular sebagai dasar utama dalam berbagai algoritma kriptografi modern. Dengan mempelajari operasi modular, mahasiswa dapat memahami bagaimana proses enkripsi dan dekripsi dilakukan dalam sistem bilangan terbatas (finite field).

Selain itu, mahasiswa diharapkan mampu menerapkan operasi dasar seperti penjumlahan, pengurangan, perkalian, perpangkatan, serta menghitung bilangan prima dan GCD (Greatest Common Divisor) untuk mendukung pembentukan kunci pada algoritma seperti RSA dan Diffie-Hellman.

Melalui pemahaman terhadap logaritma diskrit, mahasiswa juga dilatih untuk memahami konsep kesulitan komputasi yang menjadi fondasi keamanan kriptografi modern, di mana menemukan eksponen dari operasi modular menjadi tantangan matematis yang sangat kompleks.

---

## 2. Dasar Teori
Aritmetika modular merupakan sistem perhitungan yang dilakukan dalam ruang bilangan terbatas, di mana hasil operasi dikembalikan ke dalam rentang 0 hingga n–1. Operasi ini menggunakan konsep “sisa pembagian”, misalnya 

17mod 5=2. Dalam kriptografi, operasi modular digunakan untuk memastikan hasil perhitungan tidak melebihi batas tertentu, menjaga efisiensi serta keamanan proses enkripsi dan dekripsi.
Bilangan prima menjadi elemen penting dalam kriptografi karena memiliki sifat unik yang sulit difaktorkan. Algoritma seperti RSA memanfaatkan dua bilangan prima besar untuk membentuk pasangan kunci publik dan privat. Selain itu, GCD (Greatest Common Divisor) atau faktor persekutuan terbesar digunakan untuk menentukan apakah dua bilangan saling relatif prima, yang menjadi syarat penting dalam pembentukan kunci enkripsi.
Logaritma diskrit adalah kebalikan dari operasi perpangkatan dalam sistem modular. Jika diketahui ax ≡b(modn),maka mencari nilai 
𝑥
x disebut masalah logaritma diskrit. Kesulitan dalam menyelesaikan logaritma diskrit pada bilangan besar inilah yang menjadikan banyak algoritma kriptografi modern seperti Diffie-Hellman Key Exchange dan ElGamal bersifat aman terhadap serangan brute-force

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
 

Hasil eksekusi program :

![Hasil Eksekusi](/praktikum/week3-modmath-gcd/screenshots/hasil.png)


---

## 7. Jawaban Pertanyaan
  1. Apa peran aritmetika modular dalam kriptografi modern?
Aritmetika modular berperan sebagai dasar dari hampir semua algoritma kriptografi modern.
Operasi seperti penjumlahan, perkalian, dan perpangkatan dilakukan dalam sistem bilangan terbatas (mod n), sehingga hasil perhitungan selalu berada dalam rentang tertentu dan mencegah overflow.
Dalam algoritma seperti RSA, Diffie-Hellman, dan ElGamal, operasi enkripsi dan dekripsi didasarkan pada konsep eksponensiasi modular.
Dengan kata lain, aritmetika modular memungkinkan data diubah secara terstruktur namun sulit dibalik tanpa kunci yang tepat.
2. Mengapa invers modular penting dalam algoritma kunci publik (misalnya RSA)?
Invers modular digunakan untuk menemukan kunci dekripsi dari kunci enkripsi pada sistem kunci publik.
Dalam RSA, Tanpa kemampuan menghitung invers modular, proses pembentukan pasangan kunci tidak akan berhasil, dan pesan yang dienkripsi tidak dapat didekripsi kembali.
Jadi, invers modular adalah elemen penting agar komunikasi dua arah dalam kriptografi dapat berlangsung dengan aman.
3. Apa tantangan utama dalam menyelesaikan logaritma diskrit untuk modulus besar?
Tantangan utamanya adalah kompleksitas komputasi yang sangat tinggi.
Untuk bilangan modulus yang besar (misalnya ratusan digit), tidak ada algoritma efisien yang mampu menemukan nilai eksponen x daari persamaan  ax = b (mod n ) Waktu komputasi yang dibutuhkan akan meningkat secara eksponensial terhadap ukuran modulus.
Kesulitan inilah yang menjadi dasar keamanan algoritma seperti Diffie-Hellman dan ElGamal, karena meskipun mudah menghitung ax = mod n hampir mustahil membalik prosesnya tanpa mengetahui kunci privat.

---

## 8. KesimpulMelalui praktikum ini, mahasiswa memahami bahwa aritmetika modular merupakan dasar dari sistem kriptografi modern yang digunakan dalam proses enkripsi dan dekripsi data.
Konsep seperti GCD dan invers modular sangat penting dalam pembentukan kunci publik dan privat, seperti pada algoritma RSA.
Selain itu, penerapan logaritma diskrit menunjukkan mengapa kriptografi modern aman — karena sulitnya menghitung nilai eksponen dalam sistem modular besar.
Secara keseluruhan, praktikum ini memberikan pemahaman mendalam tentang bagaimana prinsip-prinsip matematika sederhana dapat digunakan untuk menjaga keamanan data digital.

---

## 9. Daftar Pustaka


---

## 10. Commit Log
(Tuliskan bukti commit Git yang relevan.  
Contoh:
```
commit abc12345
Author: anjani rahmawati <anjanirahmawati1204@gmail.com>
Date:   2025-09-21

    week2-cryptosystem: implementasi Caesar Cipher dan laporan )
```
