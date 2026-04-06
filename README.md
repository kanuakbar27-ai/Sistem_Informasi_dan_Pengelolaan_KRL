# 🚆 Sistem Manajemen Rute KRL Jabodetabek

Capstone Project Modul 1 - Data Science & Machine Learning Program\
**Institution:** Purwadhika Digital School

------------------------------------------------------------------------

## 📌 Project Overview

Proyek **Sistem Manajemen Rute KRL** bertujuan untuk mengembangkan
sistem pengelolaan data transportasi umum berbasis Python yang
terstruktur dalam pengelolaan jalur Kereta Rel Listrik (KRL),
stasiun, data penumpang, serta data petugas.

Sistem ini dirancang untuk membantu pengelolaan informasi transportasi
secara terorganisir, serta mendukung analisis statistik penumpang

Proyek ini menerapkan konsep **CRUD (Create, Read, Update, Delete)**,
validasi input pengguna, serta sistem otorisasi berbasis hierarki.

------------------------------------------------------------------------

## 🎯 Context, Problem, and User

### Context

Sistem transportasi KRL memiliki banyak jalur, stasiun, serta
percabangan rute yang membutuhkan struktur data jelas agar mudah
dikelola dan dianalisis.

### Problem

Pengelolaan data tanpa sistem terstruktur berisiko menyebabkan:

-   Data tidak konsisten\
-   Kesulitan pembaruan informasi stasiun\
-   Sulit melakukan analisis statistik penumpang\

### User

Sistem memiliki tiga kategori pengguna:

1.  **Otoritas Tinggi (Direktur/Wakil Direktur)**
    -   Akses penuh sistem
    -   Mengelola jalur KRL
    -   Mengelola data penumpang
2.  **Otoritas Menengah (Kepala Cabang)**
    -   Mengelola data stasiun cabang yang dikelola
    -   Melihat statistik penumpang cabang yang dikelola
3.  **Pengguna Umum**
    -   Mendapatkan rekomendasi perjalanan

------------------------------------------------------------------------

## ⚙️ Fitur Utama

### 1️⃣ Menampilkan Data (Read)

- Melihat Data Seluruh Penumpang.
- Melihat Data Penumpang Bedasarkan ID.
- Meliat Data dan Statistik Penumpang  Bedasarkan Line.
- Mencari Rekomendasi Rute yang Akan di Lalui.

**Akses:** Otoritas Rendah, Menengah, & Tinggi

### 2️⃣ Menambahkan Data (Create)
-   Menambahkan stasiun baru
-   Input data perjalanan penumpang

**Akses:** Otoritas Tinggi
### 3️⃣ Mengubah Data (Update)

-   Update status stasiun (aktif / nonaktif)
-   Update data kepala cabang (Otoritas)

**Akses:** Otoritas Menengah & Tinggi

### 4️⃣ Menghapus Data (Delete)

-   Menghapus data penumpang

**Akses:** Otoritas Tinggi
------------------------------------------------------------------------

## 🔐 Sistem Otorisasi (Hierarki)

    Otoritas Tinggi
          ↓
    Otoritas Menengah
          ↓
    Pengguna Umum

------------------------------------------------------------------------

## 🗂️ Struktur Data Sistem

Program menggunakan:

-   List
-   Dictionary
-   Nested Dictionary

Struktur utama:

    List Jalur KRL
        → Dictionary Line
            → Dictionary Stasiun
            → Dictionary Cabang (jika ada)

------------------------------------------------------------------------

## ▶️ Cara Menjalankan Program

Pastikan Python sudah terpasang:

    python --version

Jalankan program:

    python Sistem_informasi_dan_pengelolaan_KRL.py

------------------------------------------------------------------------

## 🧰 Teknologi yang Digunakan

-   Programming Language : Python 3
-   Libraries : Standard Python Library
-   Runtime Environment : Local Machine
-   Editor : Visual Studio Code

------------------------------------------------------------------------

## 👤 Creator

Nama: Akbar Kanugraha\
Program: Data Science & Machine Learning\
Institution: Purwadhika Digital School

------------------------------------------------------------------------

⭐ Project ini dibuat sebagai bagian dari Capstone Project Modul 1.
