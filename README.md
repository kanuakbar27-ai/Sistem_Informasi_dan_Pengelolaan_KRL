Sistem Manajemen Rute KRL Jabodetabek

Capstone Project Modul 1 - Data Science & Machine Learning Program

Institution: Purwadhika Digital School

Creator: (Isi Nama Kamu)

Project Overview

Proyek Sistem Manajemen Rute KRL bertujuan untuk mengembangkan sistem pengelolaan data transportasi umum berbasis Python yang terstruktur dalam mendokumentasikan jalur Kereta Rel Listrik (KRL), stasiun, percabangan rute, serta data penumpang. Sistem ini dirancang untuk membantu pengelolaan informasi transportasi secara terorganisir, mendukung analisis statistik penumpang, serta menyediakan simulasi pengambilan keputusan bagi otoritas transportasi.

Proyek ini menerapkan alur kerja pengelolaan data secara end-to-end menggunakan konsep CRUD (Create, Read, Update, Delete), validasi input pengguna, serta sistem otorisasi berbasis hierarki. Fokus utama diberikan pada menjaga konsistensi data rute, kemudahan pengelolaan stasiun, serta fleksibilitas sistem untuk pengembangan di masa mendatang.

Context, Problem, and User
Context

Sistem transportasi KRL memiliki banyak jalur, stasiun, serta percabangan rute yang membutuhkan struktur data yang jelas agar mudah dikelola dan dianalisis.

Problem

Pengelolaan data rute dan stasiun tanpa sistem terstruktur berisiko menyebabkan:

Data tidak konsisten

Kesulitan dalam pembaruan informasi stasiun

Sulit melakukan analisis statistik penumpang

Tidak adanya pembagian hak akses pengguna

User

Sistem memiliki tiga kategori pengguna berdasarkan tingkat otoritas:

Otoritas Tinggi
Memiliki akses penuh terhadap sistem termasuk pengelolaan jalur KRL.

Otoritas Menengah
Memiliki akses pengelolaan data stasiun dan statistik penumpang.

Pengguna Umum (Rendah)
Hanya dapat melihat rute dan mendapatkan rekomendasi perjalanan.

Fitur Utama
1. Menampilkan Data (Read)

Menampilkan seluruh jalur KRL dan daftar stasiun

Menampilkan rute perjalanan yang akan dilewati pengguna

Menampilkan data penumpang (akses otoritas)

Menampilkan statistik penumpang

2. Menambahkan Data (Create)

Input data perjalanan penumpang

Penyimpanan data untuk kebutuhan analisis statistik

Validasi input stasiun keberangkatan dan tujuan

3. Mengubah Data (Update)

Update nama stasiun

Update status stasiun (aktif / nonaktif)

Update jalur jika terjadi perubahan rute

(Akses: Otoritas Menengah dan Tinggi)

4. Menghapus Data (Delete)

Menghapus stasiun dari sistem (Otoritas Menengah)

Menghapus jalur KRL (Otoritas Tinggi)

Sistem Otorisasi (Hierarki Akses)

Sistem menggunakan konsep hierarki akses:

Otoritas Tinggi
      ↓
Otoritas Menengah
      ↓
Pengguna Umum

Otoritas tingkat lebih tinggi dapat mengakses fitur tingkat di bawahnya.

Struktur Data Sistem

Program menggunakan struktur data Python:

List

Dictionary

Nested Dictionary

Struktur utama:

List Jalur KRL
    → Dictionary Line
        → Dictionary Stasiun
        → Dictionary Cabang (jika ada)

Setiap stasiun memiliki atribut:

Kode stasiun

Nama stasiun

Status operasional

Penanganan Percabangan Rute

Beberapa jalur KRL memiliki percabangan, seperti pada Cikarang Line.
Sistem menangani percabangan dengan memisahkan:

Stasiun utama (jalur linear)

Cabang rute (jalur lanjutan)

Pendekatan ini memudahkan pengelolaan data dan pengembangan fitur rekomendasi perjalanan.

Alur Program

Pengguna masuk ke sistem

Sistem menentukan kategori pengguna berdasarkan data otoritas

Menu ditampilkan sesuai hak akses

Pengguna memilih fitur yang diinginkan

Sistem memproses data sesuai perintah CRUD

Cara Menjalankan Program

Pastikan Python sudah terpasang:

python --version

Jalankan program:

python capstone5.py

Program akan menampilkan menu interaktif pada terminal.

Teknologi yang Digunakan

Programming Language : Python 3
Libraries : Standard Python Library
Runtime Environment : Local Machine
Editor : Visual Studio Code

Tujuan Pembelajaran

Proyek ini bertujuan untuk melatih:

Pemahaman struktur data Python

Implementasi CRUD

Logika percabangan program

Validasi input

Perancangan sistem berbasis hierarki

Simulasi sistem dunia nyata

Pengembangan Lanjutan

Sistem dapat dikembangkan menjadi:

Integrasi database nyata (SQL / NoSQL)

Visualisasi rute transportasi

Analisis statistik penumpang

Sistem rekomendasi rute otomatis

Antarmuka grafis (GUI / Web)
