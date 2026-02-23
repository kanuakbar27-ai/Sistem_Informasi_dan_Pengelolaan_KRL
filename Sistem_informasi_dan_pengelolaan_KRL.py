from tabulate import tabulate
import math

listRendah = [
    {"idPerjalanan": "P95AKBKA0PNP01", "id": "P95AKBKA0PNP", "nama": "Akbar Kanugraha", "tahunLahir": 1995, "jenisKelamin": "Pria", "stasiunKeberangkatan": "Bogor", "stasiunTujuan": "Depok"},
    {"idPerjalanan": "P90ANDPA00BL2", "id": "P90ANDPA00BL", "nama": "Andi Pratama", "tahunLahir": 1990, "jenisKelamin": "Pria", "stasiunKeberangkatan": "Cilebut", "stasiunTujuan": "Manggarai"},
    {"idPerjalanan": "W92SITAH0PNP3", "id": "W92SITAH0PNP", "nama": "Siti Aisyah", "tahunLahir": 1992, "jenisKelamin": "Wanita", "stasiunKeberangkatan": "Bekasi", "stasiunTujuan": "Sudirman"},
    {"idPerjalanan": "P88DEDKN0CLL4", "id": "P88DEDKN0CLL", "nama": "Dedi Kurniawan", "tahunLahir": 1988, "jenisKelamin": "Pria", "stasiunKeberangkatan": "Cikarang", "stasiunTujuan": "Tanah Abang"},
    {"idPerjalanan": "W95LINAI0PNP5", "id": "W95LINAI0PNP", "nama": "Linda Anggraini", "tahunLahir": 1995, "jenisKelamin": "Wanita", "stasiunKeberangkatan": "Ancol", "stasiunTujuan": "Jakarta Kota"},
    {"idPerjalanan": "P00RIZMA0PNP6", "id": "P00RIZMA0PNP", "nama": "Rizky Maulana", "tahunLahir": 2000, "jenisKelamin": "Pria", "stasiunKeberangkatan": "Tangerang", "stasiunTujuan": "Duri"},
    {"idPerjalanan": "W01RINLI0PNP7", "id": "W01RINLI0PNP", "nama": "Rina Lestari", "tahunLahir": 2001, "jenisKelamin": "Wanita", "stasiunKeberangkatan": "Serpong", "stasiunTujuan": "Tanah Abang"},
    {"idPerjalanan": "P97BUDSO0PNP8", "id": "P97BUDSO0PNP", "nama": "Budi Santoso", "tahunLahir": 1997, "jenisKelamin": "Pria", "stasiunKeberangkatan": "Parung Panjang", "stasiunTujuan": "Palmerah"},
    {"idPerjalanan": "W99AMIFN0PNP9", "id": "W99AMIFN0PNP", "nama": "Amira Fatin", "tahunLahir": 1999, "jenisKelamin": "Wanita", "stasiunKeberangkatan": "Tanjung Priok", "stasiunTujuan": "Kampung Bandan"},
    {"idPerjalanan": "P94FAZRN0PNP10", "id": "P94FAZRN0PNP", "nama": "Faza Ramadhan", "tahunLahir": 1994, "jenisKelamin": "Pria", "stasiunKeberangkatan": "Cawang", "stasiunTujuan": "Tebet"},
    {"idPerjalanan": "W96DEWAI0PNP11", "id": "W96DEWAI0PNP", "nama": "Dewi Anggraini", "tahunLahir": 1996, "jenisKelamin": "Wanita", "stasiunKeberangkatan": "Depok Baru", "stasiunTujuan": "Juanda"},
    {"idPerjalanan": "P93HERSN0PNP12", "id": "P93HERSN0PNP", "nama": "Hery Setiawan", "tahunLahir": 1993, "jenisKelamin": "Pria", "stasiunKeberangkatan": "Kranji", "stasiunTujuan": "Pasar Senen"},
    {"idPerjalanan": "W98MAYSR0PNP13", "id": "W98MAYSR0PNP", "nama": "Maya Sari", "tahunLahir": 1998, "jenisKelamin": "Wanita", "stasiunKeberangkatan": "Bojong Gede", "stasiunTujuan": "Gondangdia"},
    {"idPerjalanan": "P91ADISA0PNP14", "id": "P91ADISA0PNP", "nama": "Aditya Subagja", "tahunLahir": 1991, "jenisKelamin": "Pria", "stasiunKeberangkatan": "Jurang Mangu", "stasiunTujuan": "Kebayoran"},
    {"idPerjalanan": "W02ANINR0PNP15", "id": "W02ANINR0PNP", "nama": "Anisa Nur", "tahunLahir": 2002, "jenisKelamin": "Wanita", "stasiunKeberangkatan": "Batu Ceper", "stasiunTujuan": "Grogol"},
    {"idPerjalanan": "P93RIZKN0PNP16", "id": "P93RIZKN0PNP", "nama": "Rizky Kurniawan", "tahunLahir": 1993, "jenisKelamin": "Pria", "stasiunKeberangkatan": "Citayam", "stasiunTujuan": "Tebet"},
    {"idPerjalanan": "W97SASPI0PNP17", "id": "W97SASPI0PNP", "nama": "Saskia Putri", "tahunLahir": 1997, "jenisKelamin": "Wanita", "stasiunKeberangkatan": "Klender", "stasiunTujuan": "Jatinegara"},
    {"idPerjalanan": "P91HENSA0PNP18", "id": "P91HENSA0PNP", "nama": "Hendra Saputra", "tahunLahir": 1991, "jenisKelamin": "Pria", "stasiunKeberangkatan": "Maja", "stasiunTujuan": "Tanah Abang"},
    {"idPerjalanan": "W00NADIT0PNP19", "id": "W00NADIT0PNP", "nama": "Nadia Iffat", "tahunLahir": 2000, "jenisKelamin": "Wanita", "stasiunKeberangkatan": "Bojong Indah", "stasiunTujuan": "Duri"},
    {"idPerjalanan": "P85YUDWO0PNP20", "id": "P85YUDWO0PNP", "nama": "Yudha Wicaksono", "tahunLahir": 1985, "jenisKelamin": "Pria", "stasiunKeberangkatan": "Ancol", "stasiunTujuan": "Tanjung Priok"},
    {"idPerjalanan": "W94MEGRY0PNP21", "id": "W94MEGRY0PNP", "nama": "Mega Resky", "tahunLahir": 1994, "jenisKelamin": "Wanita", "stasiunKeberangkatan": "Sudimara", "stasiunTujuan": "Palmerah"},
    {"idPerjalanan": "P96BIMAA0PNP22", "id": "P96BIMAA0PNP", "nama": "Bima Antara", "tahunLahir": 1996, "jenisKelamin": "Pria", "stasiunKeberangkatan": "Cilebut", "stasiunTujuan": "Juanda"},
    {"idPerjalanan": "W99FARAH0PNP23", "id": "W99FARAH0PNP", "nama": "Farah Azizah", "tahunLahir": 1999, "jenisKelamin": "Wanita", "stasiunKeberangkatan": "Bekasi Timur", "stasiunTujuan": "Manggarai"},
    {"idPerjalanan": "P92DIMSA0PNP24", "id": "P92DIMSA0PNP", "nama": "Dimas Setia", "tahunLahir": 1992, "jenisKelamin": "Pria", "stasiunKeberangkatan": "Karet", "stasiunTujuan": "Tanah Abang"},
    {"idPerjalanan": "W98GITOA0PNP25", "id": "W98GITOA0PNP", "nama": "Gita Oktavia", "tahunLahir": 1998, "jenisKelamin": "Wanita", "stasiunKeberangkatan": "Poris", "stasiunTujuan": "Pesing"},
    {"idPerjalanan": "P90ERWRN0PNP26", "id": "P90ERWRN0PNP", "nama": "Erwin Rian", "tahunLahir": 1990, "jenisKelamin": "Pria", "stasiunKeberangkatan": "Pondok Cina", "stasiunTujuan": "Jakarta Kota"},
    {"idPerjalanan": "W03ZULAA0PNP27", "id": "W03ZULAA0PNP", "nama": "Zulfa Amira", "tahunLahir": 2003, "jenisKelamin": "Wanita", "stasiunKeberangkatan": "Cisauk", "stasiunTujuan": "Kebayoran"},
    {"idPerjalanan": "P89AGUHN0PNP28", "id": "P89AGUHN0PNP", "nama": "Agus Hermawan", "tahunLahir": 1989, "jenisKelamin": "Pria", "stasiunKeberangkatan": "Metland Telaga Murni", "stasiunTujuan": "Bekasi"},
    {"idPerjalanan": "W95PADMN0PNP29", "id": "W95PADMN0PNP", "nama": "Padli Min", "tahunLahir": 1995, "jenisKelamin": "Wanita", "stasiunKeberangkatan": "Pasang Minggu", "stasiunTujuan": "Gondangdia"},
    {"idPerjalanan": "P01KEVAS0PNP30", "id": "P01KEVAS0PNP", "nama": "Kevin Andreas", "tahunLahir": 2001, "jenisKelamin": "Pria", "stasiunKeberangkatan": "Tangerang", "stasiunTujuan": "Tanah Tinggi"},
    {"idPerjalanan": "P92ARIRN0PNP31", "id": "P92ARIRN0PNP", "nama": "Aris Ryan", "tahunLahir": 1992, "jenisKelamin": "Pria", "stasiunKeberangkatan": "Bojong Gede", "stasiunTujuan": "Cawang"},
    {"idPerjalanan": "W96FIDDN0PNP32", "id": "W96FIDDN0PNP", "nama": "Fidya Dian", "tahunLahir": 1996, "jenisKelamin": "Wanita", "stasiunKeberangkatan": "Klender Baru", "stasiunTujuan": "Bekasi"},
    {"idPerjalanan": "P87HERMA0PNP33", "id": "P87HERMA0PNP", "nama": "Herman Maulana", "tahunLahir": 1987, "jenisKelamin": "Pria", "stasiunKeberangkatan": "Parung Panjang", "stasiunTujuan": "Tanah Abang"},
    {"idPerjalanan": "W04LULAA0PNP34", "id": "W04LULAA0PNP", "nama": "Lulu Amalia", "tahunLahir": 2004, "jenisKelamin": "Wanita", "stasiunKeberangkatan": "Tanah Tinggi", "stasiunTujuan": "Batu Ceper"},
    {"idPerjalanan": "P90SYAAS0PNP35", "id": "P90SYAAS0PNP", "nama": "Syaiful Anas", "tahunLahir": 1990, "jenisKelamin": "Pria", "stasiunKeberangkatan": "Jakarta Kota", "stasiunTujuan": "Tanjung Priok"},
    {"idPerjalanan": "W91RATSI0PNP36", "id": "W91RATSI0PNP", "nama": "Ratna Sari", "tahunLahir": 1991, "jenisKelamin": "Wanita", "stasiunKeberangkatan": "Depok", "stasiunTujuan": "Manggarai"},
    {"idPerjalanan": "P95REZPA0PNP37", "id": "P95REZPA0PNP", "nama": "Rezzy Pratama", "tahunLahir": 1995, "jenisKelamin": "Pria", "stasiunKeberangkatan": "Tambun", "stasiunTujuan": "Jatinegara"},
    {"idPerjalanan": "W02CHIAA0PNP38", "id": "W02CHIAA0PNP", "nama": "Chika Amara", "tahunLahir": 2002, "jenisKelamin": "Wanita", "stasiunKeberangkatan": "Sudimara", "stasiunTujuan": "Kebayoran"},
    {"idPerjalanan": "P88BAMHU0PNP39", "id": "P88BAMHU0PNP", "nama": "Bambang Heru", "tahunLahir": 1988, "jenisKelamin": "Pria", "stasiunKeberangkatan": "Tangerang", "stasiunTujuan": "Duri"},
    {"idPerjalanan": "W93ELIPT0PNP40", "id": "W93ELIPT0PNP", "nama": "Elisa Putri", "tahunLahir": 1993, "jenisKelamin": "Wanita", "stasiunKeberangkatan": "Ancol", "stasiunTujuan": "Kampung Bandan"},
    {"idPerjalanan": "P99GILRN0PNP41", "id": "P99GILRN0PNP", "nama": "Gilang Ramadhan", "tahunLahir": 1999, "jenisKelamin": "Pria", "stasiunKeberangkatan": "Lenteng Agung", "stasiunTujuan": "Univ. Indonesia"},
    {"idPerjalanan": "W01AMACA0PNP42", "id": "W01AMACA0PNP", "nama": "Amara Cantika", "tahunLahir": 2001, "jenisKelamin": "Wanita", "stasiunKeberangkatan": "Cibitung", "stasiunTujuan": "Cikarang"},
    {"idPerjalanan": "P94ANDWA0PNP43", "id": "P94ANDWA0PNP", "nama": "Andre Wijaya", "tahunLahir": 1994, "jenisKelamin": "Pria", "stasiunKeberangkatan": "Rawa Buntu", "stasiunTujuan": "Palmerah"},
    {"idPerjalanan": "W98KANDI0PNP44", "id": "W98KANDI0PNP", "nama": "Kania Dewi", "tahunLahir": 1998, "jenisKelamin": "Wanita", "stasiunKeberangkatan": "Pesing", "stasiunTujuan": "Grogol"},
    {"idPerjalanan": "P86SUBAI0PNP45", "id": "P86SUBAI0PNP", "nama": "Subagja Adi", "tahunLahir": 1986, "jenisKelamin": "Pria", "stasiunKeberangkatan": "Sawah Besar", "stasiunTujuan": "Jayakarta"},
    {"idPerjalanan": "W00PUTUI0PNP46", "id": "W00PUTUI0PNP", "nama": "Putri Utami", "tahunLahir": 2000, "jenisKelamin": "Wanita", "stasiunKeberangkatan": "Matraman", "stasiunTujuan": "Sudirman"},
    {"idPerjalanan": "P92ILHJA0PNP47", "id": "P92ILHJA0PNP", "nama": "Ilham Jaya", "tahunLahir": 1992, "jenisKelamin": "Pria", "stasiunKeberangkatan": "Gang Sentiong", "stasiunTujuan": "Pasar Senen"},
    {"idPerjalanan": "W95SANMA0PNP48", "id": "W95SANMA0PNP", "nama": "Santi Maria", "tahunLahir": 1995, "jenisKelamin": "Wanita", "stasiunKeberangkatan": "Rangkasbitung", "stasiunTujuan": "Maja"},
    {"idPerjalanan": "P91HENKS0PNP49", "id": "P91HENKS0PNP", "nama": "Hendra Koes", "tahunLahir": 1991, "jenisKelamin": "Pria", "stasiunKeberangkatan": "Pondok Jati", "stasiunTujuan": "Kemayoran"},
    {"idPerjalanan": "W01AMACA0PNP50", "id": "W01AMACA0PNP", "nama": "Amara Cantika", "tahunLahir": 2001, "jenisKelamin": "Wanita", "stasiunKeberangkatan": "Poris", "stasiunTujuan": "Tanah Tinggi"}
]
listMenengah = [
    {
        "id": "P90ANDPA00BL",
        "nama": "Andi Pratama",
        "tahunLahir": 1990,
        "jenisKelamin": "Pria",
        "jabatan": "Kepala Cabang Bogor Line",
        "password": "bogor123",
        "region": "Bogor Line"
    },
    {
        "id": "W89SITAH00RL",
        "nama": "Siti Aisyah",
        "tahunLahir": 1989,
        "jenisKelamin": "Wanita",
        "jabatan": "Kepala Cabang Rangkasbitung Line",
        "password": "rangkasbitung123",
        "region": "Rangkasbitung Line"
    },
    {
        "id": "P87BUDSO0TPL",
        "nama": "Budi Santoso",
        "tahunLahir": 1987,
        "jenisKelamin": "Pria",
        "jabatan": "Kepala Cabang Tanjung Priok Line",
        "password": "tanjungpriok123",
        "region": "Tanjung Priok Line"
    },
    {
        "id": "W91RINLI00TL",
        "nama": "Rina Lestari",
        "tahunLahir": 1991,
        "jenisKelamin": "Wanita",
        "jabatan": "Kepala Cabang Tangerang Line",
        "password": "tangerang123",
        "region": "Tangerang Line"
    },
    {
        "id": "P88DEDKN0CLL",
        "nama": "Dedi Kurniawan",
        "tahunLahir": 1988,
        "jenisKelamin": "Pria",
        "jabatan": "Kepala Cabang Cikarang Line",
        "password": "cikarang123",
        "region": "Cikarang Loop Line"
    }
]
listTinggi = [
    {
        "id": "P01AKBKA00DO",
        "nama": "Akbar Kanugraha",
        "tahunLahir": 2001,
        "jenisKelamin": "Pria",
        "jabatan": "Direktur Operasional",
        "password": "direktur123",
        "region": "Indonesia"
    },
    {
        "id": "W73DEWAI0WDO",
        "nama": "Dewi Anggraini",
        "tahunLahir": 1973,
        "jenisKelamin": "Wanita",
        "jabatan": "Wakil Direktur Operasional",
        "password": "wakil123",
        "region" : "Indonesia"
    }
]
dataKrl = [
  {
    "id": "KRLLN1",
    "line": "Bogor Line",
    "stasiun": {
      1: { "nama": "Bogor", "status": "Aktif", "transit": "Tidak" },
      2: { "nama": "Cilebut", "status": "Aktif", "transit": "Tidak" },
      3: { "nama": "Bojong Gede", "status": "Aktif", "transit": "Tidak" },
      4: { "nama": "Citayam", "status": "Aktif", "transit": "Tidak" },
      5: { "nama": "Depok", "status": "Aktif", "transit": "Tidak" },
      6: { "nama": "Depok Baru", "status": "Aktif", "transit": "Tidak" },
      7: { "nama": "Pondok Cina", "status": "Aktif", "transit": "Tidak" },
      8: { "nama": "Univ. Indonesia", "status": "Aktif", "transit": "Tidak" },
      9: { "nama": "Univ. Pancasila", "status": "Aktif", "transit": "Tidak" },
      10: { "nama": "Lenteng Agung", "status": "Aktif", "transit": "Tidak" },
      11: { "nama": "Tanjung Barat", "status": "Aktif", "transit": "Tidak" },
      12: { "nama": "Pasang Minggu", "status": "Aktif", "transit": "Tidak" },
      13: { "nama": "Pasang Minggu Baru", "status": "Aktif", "transit": "Tidak" },
      14: { "nama": "Duren Kalibata", "status": "Aktif", "transit": "Tidak" },
      15: { "nama": "Cawang", "status": "Aktif", "transit": "Tidak" },
      16: { "nama": "Tebet", "status": "Aktif", "transit": "Tidak" },
      17: { "nama": "Manggarai", "status": "Aktif", "transit": "Termasuk" },
      18: { "nama": "Cikini", "status": "Aktif", "transit": "Tidak" },
      19: { "nama": "Gondangdia", "status": "Aktif", "transit": "Tidak" },
      20: { "nama": "Juanda", "status": "Aktif", "transit": "Tidak" },
      21: { "nama": "Sawah Besar", "status": "Aktif", "transit": "Tidak" },
      22: { "nama": "Mangga Besar", "status": "Aktif", "transit": "Tidak" },
      23: { "nama": "Jayakarta", "status": "Aktif", "transit": "Tidak" },
      24: { "nama": "Jakarta Kota", "status": "Aktif", "transit": "Tidak" }
    }
  },
  {
    "id": "KRLLN2",
    "line": "Cikarang Loop Line",
    "sub rute": {
      "cikarang utama": {
        1: { "nama": "Cikarang", "status": "Aktif", "transit": "Tidak" },
        2: { "nama": "Metland Telaga Murni", "status": "Aktif", "transit": "Tidak" },
        3: { "nama": "Cibitung", "status": "Aktif", "transit": "Tidak" },
        4: { "nama": "Tambun", "status": "Aktif", "transit": "Tidak" },
        5: { "nama": "Bekasi Timur", "status": "Aktif", "transit": "Tidak" },
        6: { "nama": "Bekasi", "status": "Aktif", "transit": "Tidak" },
        7: { "nama": "Kranji", "status": "Aktif", "transit": "Tidak" },
        8: { "nama": "Cakung", "status": "Aktif", "transit": "Tidak" },
        9: { "nama": "Klender Baru", "status": "Aktif", "transit": "Tidak" },
        10: { "nama": "Buaran", "status": "Aktif", "transit": "Tidak" },
        11: { "nama": "Klender", "status": "Aktif", "transit": "Tidak" },
        12: { "nama": "Jatinegara", "status": "Aktif", "transit": "Termasuk" }
      },
      "via manggarai": {
        1: { "nama": "Jatinegara", "status": "Aktif", "transit": "Termasuk" },
        2: { "nama": "Matraman", "status": "Aktif", "transit": "Tidak" },
        3: { "nama": "Manggarai", "status": "Aktif", "transit": "Termasuk" },
        4: { "nama": "Sudirman", "status": "Aktif", "transit": "Tidak" },
        5: { "nama": "BNI City", "status": "Aktif", "transit": "Tidak" },
        6: { "nama": "Karet", "status": "Aktif", "transit": "Tidak" },
        7: { "nama": "Tanah Abang", "status": "Aktif", "transit": "Termasuk" },
        8: { "nama": "Duri", "status": "Aktif", "transit": "Termasuk" },
        9: { "nama": "Angke", "status": "Aktif", "transit": "Tidak" },
        10: { "nama": "Kampung Bandan", "status": "Aktif", "transit": "Termasuk" }
      },
      "via pasar senen": {
        1: { "nama": "Jatinegara", "status": "Aktif", "transit": "Termasuk" },
        2: { "nama": "Pondok Jati", "status": "Aktif", "transit": "Tidak" },
        3: { "nama": "Kramat", "status": "Aktif", "transit": "Tidak" },
        4: { "nama": "Gang Sentiong", "status": "Aktif", "transit": "Tidak" },
        5: { "nama": "Pasar Senen", "status": "Aktif", "transit": "Tidak" },
        6: { "nama": "Kemayoran", "status": "Aktif", "transit": "Tidak" },
        7: { "nama": "Rajawali", "status": "Aktif", "transit": "Tidak" },
        8: { "nama": "Kampung Bandan", "status": "Aktif", "transit": "Termasuk" }
      }
    }
  },
  {
    "id": "KRLLN3",
    "line": "Rangkasbitung Line",
    "stasiun": {
      1: { "nama": "Rangkasbitung", "status": "Aktif", "transit": "Tidak" },
      2: { "nama": "Citeras", "status": "Aktif", "transit": "Tidak" },
      3: { "nama": "Maja", "status": "Aktif", "transit": "Tidak" },
      4: { "nama": "Cikoya", "status": "Aktif", "transit": "Tidak" },
      5: { "nama": "Tigaraksa", "status": "Aktif", "transit": "Tidak" },
      6: { "nama": "Tenjo", "status": "Aktif", "transit": "Tidak" },
      7: { "nama": "Daru", "status": "Aktif", "transit": "Tidak" },
      8: { "nama": "Cilejit", "status": "Aktif", "transit": "Tidak" },
      9: { "nama": "Parung Panjang", "status": "Aktif", "transit": "Tidak" },
      10: { "nama": "Jatake", "status": "Aktif", "transit": "Tidak" },
      11: { "nama": "Cicayur", "status": "Aktif", "transit": "Tidak" },
      12: { "nama": "Cisauk", "status": "Aktif", "transit": "Tidak" },
      13: { "nama": "Serpong", "status": "Aktif", "transit": "Tidak" },
      14: { "nama": "Rawa Buntu", "status": "Aktif", "transit": "Tidak" },
      15: { "nama": "Sudimara", "status": "Aktif", "transit": "Tidak" },
      16: { "nama": "Jurang Mangu", "status": "Aktif", "transit": "Tidak" },
      17: { "nama": "Pondok Ranji", "status": "Aktif", "transit": "Tidak" },
      18: { "nama": "Kebayoran", "status": "Aktif", "transit": "Tidak" },
      19: { "nama": "Palmerah", "status": "Aktif", "transit": "Tidak" },
      20: { "nama": "Tanah Abang", "status": "Aktif", "transit": "Termasuk" }
    }
  },
  {
    "id": "KRLLN4",
    "line": "Tangerang Line",
    "stasiun": {
      1: { "nama": "Tangerang", "status": "Aktif", "transit": "Tidak" },
      2: { "nama": "Tanah Tinggi", "status": "Aktif", "transit": "Tidak" },
      3: { "nama": "Batu Ceper", "status": "Aktif", "transit": "Tidak" },
      4: { "nama": "Poris", "status": "Aktif", "transit": "Tidak" },
      5: { "nama": "Kali Deres", "status": "Aktif", "transit": "Tidak" },
      6: { "nama": "Rawa Buaya", "status": "Aktif", "transit": "Tidak" },
      7: { "nama": "Bojong Indah", "status": "Aktif", "transit": "Tidak" },
      8: { "nama": "Taman Kota", "status": "Aktif", "transit": "Tidak" },
      9: { "nama": "Pesing", "status": "Aktif", "transit": "Tidak" },
      10: { "nama": "Grogol", "status": "Aktif", "transit": "Tidak" },
      11: { "nama": "Duri", "status": "Aktif", "transit": "Termasuk" }
    }
  },
  {
    "id": "KRLLN5",
    "line": "Tanjung Priok Line",
    "stasiun": {
      1: { "nama": "Tanjung Priok", "status": "Aktif", "transit": "Tidak" },
      2: { "nama": "Ancol", "status": "Aktif", "transit": "Tidak" },
      3: { "nama": "Kampung Bandan", "status": "Aktif", "transit": "Termasuk" },
      4: { "nama": "Jakarta Kota", "status": "Aktif", "transit": "Tidak" }
    }
  }
]

def tabelKrlSebagian(line):
    header = ["No", "Stasiun", "Status"]
    header2 = ["No", "Stasiun", "Status", "Rute Via"]
    row = []
    stasiunTercatat = []
    nomor = 1

    print(f"\n============== Tabel KRL di {line} ==============")
    for i in dataKrl:
        if i["line"] == line:
            if "stasiun" in i:
                for st in i["stasiun"]:
                    tabelData = [st, i['stasiun'][st]['nama'], i['stasiun'][st]['status']]
                    row.append(tabelData)
                print(tabulate(row, headers = header, tablefmt = "double_outline"), "\n")
            elif "sub rute" in i:
                for via in i["sub rute"]:
                    print(f"Rute Via {via}:")
                    for st2 in i["sub rute"][via]:
                        if i['sub rute'][via][st2]['nama'] not in stasiunTercatat:
                            tabelData = [nomor, i['sub rute'][via][st2]['nama'] , i['sub rute'][via][st2]['status'], via]
                            row.append(tabelData)
                            stasiunTercatat.append(i['sub rute'][via][st2]['nama'])
                            nomor += 1
                print(tabulate(row, headers = header2, tablefmt = "double_outline"), "\n")
def tabelUser(listUser):
    header = ["ID Perjalanan", "ID", "Nama", "Tahun Lahir", "Jenis Kelamin", "Stasiun Keberangkatan", "Stasiun Tujuan"]
    header2 = ["ID", "Nama", "Tahun Lahir", "Jenis Kelamin", "Jabatan", "Region", "Password"]
    row =[]

    if listUser == listRendah:
        print("\n======================================= Berikut Merupakan Data Penumpang =======================================")
        for i in listUser:
            tabeldata = [i['idPerjalanan'],i['id'], i['nama'], i['tahunLahir'], i['jenisKelamin'], i['stasiunKeberangkatan'], i['stasiunTujuan']]
            row.append(tabeldata)
        print(tabulate(row, headers=header, tablefmt="double_outline"), "\n")
    elif listUser == listMenengah:    
        print("\n========================== Berikut Merupakan Data Kepala Cabang ==========================")
        for i in listUser:
            tabeldata = [i['id'], i['nama'], i['tahunLahir'], i['jenisKelamin'], i['jabatan'], i['region'], i['password']]
            row.append(tabeldata)
        print(tabulate(row, headers=header2, tablefmt="double_outline"), "\n")
def tabelPenumpangSebagian(line):
    header = ["ID", "Nama", "Tahun Lahir", "Jenis Kelamin", "Stasiun Keberangkatan", "Stasiun Tujuan"]
    row = []

    print(f"\n========================================= Tabel Penumpang di {line} =======================================")
    for i in listRendah:
        if i["stasiunKeberangkatan"] in namaStasiun(line) or i["stasiunTujuan"] in namaStasiun(line):
            tabeldata = [i['id'], i['nama'], i['tahunLahir'], i['jenisKelamin'], i['stasiunKeberangkatan'], i['stasiunTujuan']]
            row.append(tabeldata)
    print(tabulate(row, headers=header, tablefmt="double_outline"), "\n")
def tabelBedasarkanID(listUser, ID=None):
    header = ["ID Perjalanan","ID", "Nama", "Tahun Lahir", "Jenis Kelamin", "Stasiun Keberangkatan", "Stasiun Tujuan"]
    header2 = ["ID", "Nama", "Tahun Lahir", "Jenis Kelamin", "Jabatan", "Region", "Password"]
    header3 = ["No", "Nama Stasiun", "Status"]
    header4 = ["No", "ID", "Nama Line"]
    row = []

    if listUser == listRendah:
        print(f"\n==================================== Tabel Penumpang dengan ID {ID} ===================================")
        for i in listUser:
            if i["id"] == ID:
                tabeldata = [i['idPerjalanan'], i['id'], i['nama'], i['tahunLahir'], i['jenisKelamin'], i['stasiunKeberangkatan'], i['stasiunTujuan']]
                row.append(tabeldata)
        print(tabulate(row, headers=header, tablefmt="double_outline"), "\n")
    elif listUser == listMenengah:
        print(f"\n===================================== Tabel Kepala Cabang dengan ID {ID} =====================================")
        for i in listUser:
            if i["id"] == ID:
                tabeldata = [i['id'], i['nama'], i['tahunLahir'], i['jenisKelamin'], i['jabatan'], i['region'], i['password']]
                row.append(tabeldata)
        print(tabulate(row, headers=header2, tablefmt="double_outline"), "\n")
    elif listUser == dataKrl:
        print(f"\n======= Tabel Tambah Stasiun ========")
        for i in dataKrl:
            tabeldata = [i['id'][-1] ,i['id'], i['line']]
            row.append(tabeldata)
        print(tabulate(row, headers=header4, tablefmt="double_outline"), "\n")
    elif type(listUser) == dict:        
        print(f"\n=== Tabel Tambah Stasiun ====") 
        tabeldata = [1, listUser['nama'], listUser['status']]
        row.append(tabeldata)
        print(tabulate(row, headers=header3, tablefmt="double_outline"), "\n")
    elif type(listUser) == list and listUser not in [listMenengah, listRendah, listTinggi]:
        print(f"\n======== Tabel Stasiun =========") 
        nomor = 1
        for i in listUser:
            tabeldata = [nomor, i['nama'], i['status']]
            row.append(tabeldata)
            nomor +=1
        print(tabulate(row, headers=header3, tablefmt="double_outline"), "\n")
        
        
def validasiHurup(prompt, banyakDigit):
    while True:
        hasil = input(prompt).strip().title()
        if len(hasil) >= banyakDigit and hasil.replace(" ", "").isalpha():
            return hasil 
        else:
           print(f"Input Tidak Valid! Harap Masukkan Minimal {banyakDigit} Digit Huruf dan Berupa Huruf.\n")
def validasiAngka(prompt, pilihan, limit1, limit2, banyakDigit=4):
    while True:
        hasil = input(prompt).strip()
        if hasil.isdigit():
            if pilihan == "Pilihan": 
                if len(hasil) <= banyakDigit:
                    if limit1 <= int(hasil) <= limit2:
                        return int(hasil)
                    else:
                        print(f"Input Tidak Valid! Harap Masukkan Angka Sesuai Rentang {limit1} - {limit2}.\n")
                else:
                    print(f"Input Tidak Valid! Harap minmal {banyakDigit} Digit Angka")
            elif pilihan == "Tahun":  
                if len(hasil) == banyakDigit:
                    if limit1 <= int(hasil) <= limit2:
                        return int(hasil)
                    else:
                        print(f"Input Tidak Valid! Harap Masukkan Angka Sesuai Rentang {limit1} - {limit2}.\n")
                else:
                    print(f"Input Tidak Valid! Harap Masukkan {banyakDigit} Digit Angka")       
        else:
            print(f"Input Tidak Valid! Harap Masukkan Angka.\n")
def validasiDuaPilihan(prompt, pilihan1, pilihan2):
    while True:
        hasil = input(prompt).strip().title()
        if hasil in [pilihan1, pilihan2]:
            return hasil
        else:
            print(f"Input Tidak Valid! Harap Masukkan {pilihan1} atau {pilihan2}.\n")
def validasiPassword(prompt):
    while True:
        hasil = input(prompt).strip()
        if len(hasil) >= 8 and hasil.isalnum():
            return hasil
        else:
            print("Input Tidak Valid! Harap Masukkan Password Minimal 8 Karakter, Mengandung Huruf dan Angka.\n")
def validasAktifNonaktif(prompt):
    while True:
        hasil = input(prompt).strip().title()
        if hasil in ["Aktif", "Nonaktif"]:
            return hasil
        else:
            print("Input Tidak Valid! Harap Masukkan 'Aktif' atau 'Nonaktif'.\n")

def pembuatanIdRendah(nama, lahir, jenisKelamin):
    keyLahir = str(lahir)
    namaSplit = nama.split()
    namaId1 = namaSplit[0][0:3]
    if len(namaSplit) > 1:
        namaId2 = namaSplit[1][0] + namaSplit[1][-1]
    else :
        namaId2 = "NO"
    ID = f"{jenisKelamin[0]}{keyLahir[-2:]}{namaId1.upper()}{namaId2.upper()}{0}PNP"
    return ID
def pembuatanIdMenengah(nama, lahir, jenisKelamin, region):
    keyLahir = str(lahir)
    namaSplit = nama.split()
    namaId1 = namaSplit[0][0:3]
    if len(namaSplit) > 1:
        namaId2 = namaSplit[1][0] + namaSplit[1][-1]
    else :
        namaId2 = "NO"
    regionSplit = region.split()
    if len(regionSplit) > 2:
        regionID =  f"{regionSplit[0][0]}{regionSplit[1][0]}{regionSplit[2][0]}"
    else :
        regionID =  f"0{regionSplit[0][0]}{regionSplit[1][0]}"
    ID = f"{jenisKelamin[0]}{keyLahir[-2:]}{namaId1.upper()}{namaId2.upper()}{0}{regionID}"
    return ID

def kategoriUser(nama, tahunLahir, jenisKelamin):
    ditemukan = False
    for i in range(len(listTinggi)):
        if nama == listTinggi[i]["nama"] and tahunLahir == listTinggi[i]["tahunLahir"] and jenisKelamin == listTinggi[i]["jenisKelamin"]:
            ditemukan = True
            return "Tinggi", listTinggi[i]
    if ditemukan == False:
        for i in range(len(listMenengah)):
            if nama == listMenengah[i]["nama"] and tahunLahir == listMenengah[i]["tahunLahir"] and jenisKelamin == listMenengah[i]["jenisKelamin"]:
                ditemukan = True
                return "Menengah", listMenengah[i]
    if ditemukan == False:
        return "Rendah", None
def namaStasiun(line):
    namaStasiunLis = []
    for jalur in dataKrl:
        if jalur["line"] == line:
            if "stasiun" in jalur:
                for st in jalur["stasiun"]:
                    namaStasiunLis.append(jalur["stasiun"][st]["nama"])
            elif "sub rute" in jalur:
                for via in jalur["sub rute"]:
                    for st2 in jalur["sub rute"][via]:
                        namaStasiunLis.append(jalur["sub rute"][via][st2]["nama"])
    return namaStasiunLis 
def stasiunTransit():
    stTransit = []
    for i in dataKrl:
        if "stasiun" in i:
            for j in i["stasiun"]:
                if i["stasiun"][j]["transit"] == "Termasuk" and i["stasiun"][j]["nama"] not in stTransit:
                    stTransit.append(i["stasiun"][j]["nama"])
        elif "sub rute" in i:
            for j in i["sub rute"]:
                for k in i["sub rute"][j]:
                    if i["sub rute"][j][k]["transit"] == "Termasuk" and i["sub rute"][j][k]["nama"] not in stTransit:
                        stTransit.append(i["sub rute"][j][k]["nama"])
    return stTransit
def loginPass(listOtoritas, nama, lahir, jenisKelamin):
    for i in listOtoritas:
        if i["nama"] == nama and i["tahunLahir"] == lahir and i["jenisKelamin"] == jenisKelamin:
            percobaan =0
            while percobaan < 3 :
                password = input("Masukkan Password Anda: ")
                if i["password"] == password:
                    print( f"\nSelamat Datang di Panel Kendali Operasional, Bapak/Ibu {nama}, Anda masuk sebagai {i['jabatan']}")
                    break
                else :
                    print(f"Kata Sandi yang Anda Masukkan Salah, Silahkan Coba Kembali.\n")
                    percobaan +=1
            return percobaan

def ruteRekomendasi(nama,  lahir, jenisKelamin):
    listIdPj = []
    for i in listRendah:
        listIdPj.append(int(i["idPerjalanan"][12:]))
    if len(listIdPj) == 0:
        nomorTambahan = 1
    else:
        nomorTambahan = max(listIdPj) + 1
    CatUser, urutan = kategoriUser(nama, lahir, jenisKelamin)
    if CatUser == "Rendah":
        IDuser = pembuatanIdRendah(nama, lahir, jenisKelamin)
        IDpj = f"{IDuser}{nomorTambahan}"
    elif CatUser == "Menengah":
        IDuser = urutan["id"]
        IDpj = f"{IDuser}{nomorTambahan}"
    elif CatUser == "Tinggi":
        IDuser = urutan["id"]
        IDpj = f"{IDuser}{nomorTambahan}"
    
    naik = input("\nMasukkan Stasiun Keberangkatan: ").strip().title()
    turun = input("Masukkan Stasiun Tujuan: ").strip().title()
    listPenumpang = {
            "idPerjalanan": IDpj,
            "id": IDuser, 
            "nama": nama, 
            "tahunLahir": lahir, 
            "jenisKelamin": jenisKelamin,
            "stasiunKeberangkatan": naik,
            "stasiunTujuan": turun
            }  
    lineAsal = ""
    lineTujuan = ""
    for i in dataKrl:
        namaStasiunLine = namaStasiun(i["line"])
        if naik in namaStasiunLine and turun in namaStasiunLine:
            lineAsal = i["line"]
            lineTujuan = i["line"]
            break
        elif turun in namaStasiunLine and naik not in namaStasiunLine:
            lineTujuan = i["line"]
        elif turun not in namaStasiunLine and naik in namaStasiunLine:
            lineAsal = i["line"]

    if lineAsal == lineTujuan and lineAsal != "":
        print(f"""
Stasiun {naik} dan {turun} berada di jalur yang sama ({lineAsal})
Silakan naik kereta langsung tanpa transit.""")
        listRendah.append(listPenumpang)
    elif lineAsal == "" or lineTujuan == "":
        print("\nMaaf stasiun keberangkatan atau stasiun tujuan tidak ditemukan di sistem.")
    else :
        stTransit = ""
        titikTransit = stasiunTransit()
        namaStasiunLineAsal = namaStasiun(lineAsal)
        namaStasiunLineTujuan = namaStasiun(lineTujuan)
        for transit in titikTransit:
            if transit in namaStasiunLineAsal and transit in namaStasiunLineTujuan:
                stTransit = transit
                break
        status = cariStatusStasiun(lineAsal, stTransit)
        if stTransit != "" and status == "Aktif":
            print(f"""
Stasiun keberangkatan Anda ada di {lineAsal}, dan stasiun tujuan Anda ada di {lineTujuan}.
Silakan transit di stasiun {stTransit}.""")
        elif stTransit != "" and status == "Nonaktif":
            print(f"""
Mohon maaf, transit di {stTransit} tidak tersedia saat ini karena status stasiun sedang Nonaktif. 
Silakan hubungi petugas untuk rute alternatif.""")
        else :
            print(f"""
Rute ditemukan, namun memerlukan lebih dari satu kali transit atau rute khusus.
Silahkan bertanya ke petugas terdekat.""")
        listRendah.append(listPenumpang)  

def AvgLahir(listAvg):
    avg = sum(listAvg)/len(listAvg)
    return avg
def statistikPenumpang(listStasiun, line):
    listPenumpang = []
    listStBerangkat = []
    listStTurun = []
    lahirPria = []
    lahirWanita = []
    
    for j in listRendah:
        if j["stasiunKeberangkatan"] in listStasiun or j["stasiunTujuan"] in listStasiun:
            listPenumpang.append(j)
            if j["jenisKelamin"] == "Pria":
                lahirPria.append(j["tahunLahir"])
            else:
                lahirWanita.append(j["tahunLahir"])
        if j["stasiunTujuan"] in listStasiun:
            listStTurun.append(j)
        if j["stasiunKeberangkatan"] in listStasiun:
            listStBerangkat.append(j)
    tabelPenumpangSebagian(line)
    if len(listPenumpang) > 0:    
        if len(lahirPria) > 0:
            avgPria = AvgLahir(lahirPria)
        else:
            avgPria = 2026
        if  len(lahirWanita) > 0:
            avgWanita = AvgLahir(lahirWanita)
        else:
            avgWanita = 2026
        avgAll = (sum(lahirPria)+sum(lahirWanita))/(len(listPenumpang))
    else:
        avgPria = 2026
        avgWanita = 2026
        avgAll = 2026
    print(f"""Jumlah Penumpang yang Menggunakan Jalur Ini: {len(listPenumpang)} Orang.
Penumpang yang Berangkat dari Jalur Ini: {(len(listStBerangkat))} Orang.
Penumpang yang Turun dari Jalur Ini: {(len(listStTurun))} Orang.
Komposisi Gender Penumpang: Pria {len(lahirPria)} Orang, Wanita {len(lahirWanita)} Orang.
Rata-Rata Umur yang Menggunakan Jalur Ini: {math.floor(2026 - avgAll)}
dengan Rata-Rata Umur Pria {math.floor(2026- avgPria)} Tahun dan Rata-Rata Umur Wanita {math.floor(2026 - avgWanita)} Tahun
        """)
def melihatDataStatistikRendah(line, role):
    listStasiun = namaStasiun(line)
    if role == "Menengah":
        while True:
            print(f"""
========= Menu Melihat Data dan Statistik Penumpang di Line {line} =========
1. Melihat Data dan Statistik Penumpang.
2. Melihat Data Penumpang Bedasarkan ID.
3. Kembali ke Menu.""")
            userPilih = input("Masukkan Pilihan Anda Bedasarkan Nomor: ").strip()
            if userPilih == "1":
                statistikPenumpang(listStasiun, line)
            elif userPilih == "2":
                masukkanID = input("Masukkan ID Penumpang yang Ingin Dilihat Datanya: ").strip().upper()
                listID = []
                for p in listRendah:
                    if p["stasiunKeberangkatan"] in listStasiun or p["stasiunTujuan"] in listStasiun:
                        listID.append(p["id"])
                if masukkanID in listID:
                    tabelBedasarkanID(listRendah, masukkanID)
                else:
                    print("Maaf, ID yang Anda Masukkan Tidak Ditemukan.\n")
            elif userPilih == "3":
                break
            else:
                print("Maaf, Pilihan yang Anda Masukkan Tidak Valid.\n")
    elif role == "Tinggi":
        statistikPenumpang(listStasiun, line)

def cariStatusStasiun(line,namaStasiun):
    for jalur in dataKrl:
        if jalur["line"] == line:
            if "stasiun" in jalur:
                for st in jalur["stasiun"]:
                    if jalur["stasiun"][st]["nama"] == namaStasiun:
                        namaSt = jalur["stasiun"][st]["nama"]
                        Stat = jalur["stasiun"][st]["status"]
                        return Stat 
            elif "sub rute" in jalur:
                for via in jalur["sub rute"]:
                    for st2 in jalur["sub rute"][via]:
                        if jalur["sub rute"][via][st2]["nama"] == namaStasiun:
                            namaSt = jalur["sub rute"][via][st2]["nama"]
                            Stat = jalur["sub rute"][via][st2]["status"]
                            return Stat 
def perubahanStatus (namaStasiun, statusSekarang, menjadiStatus):
    listStTransit = stasiunTransit()
    if namaStasiun in listStTransit:
        print(f"Stasiun {namaStasiun} Adalah Stasiun Transit")
        print(f"Jika Anda Men{(menjadiStatus).lower()}nya, Semua Stasiun {namaStasiun} Akan {(menjadiStatus).title()} di Semua Line")
        userUbahInput = validasiDuaPilihan(f"Apakah Anda Yakin men{(menjadiStatus).lower()}nya?(ya/tidak) ", "Ya", "Tidak").strip().title()
        if userUbahInput == "Ya":
            for jalur in dataKrl:
                if "stasiun" in jalur:
                    for st in jalur["stasiun"]:
                        if jalur["stasiun"][st]["nama"] == namaStasiun:
                            jalur["stasiun"][st]["status"] = menjadiStatus
                elif "sub rute" in jalur:
                    for via in jalur["sub rute"]:
                        for st2 in jalur["sub rute"][via]:
                            if jalur["sub rute"][via][st2]["nama"] == namaStasiun:
                                jalur["sub rute"][via][st2]["status"] = menjadiStatus
            print(f"\nBerhasil! Stasiun {namaStasiun} telah di{menjadiStatus}kan\n")
        elif userUbahInput == "Tidak":
            print(f"\nBaik, Stasiun {namaStasiun} akan tetap di{statusSekarang}kan\n")
    elif namaStasiun not in listStTransit:
        userUbahInput = validasiDuaPilihan(f"Apakah Anda Yakin men{(menjadiStatus).lower()}nya?(ya/tidak) ", "Ya", "Tidak").strip().title()
        if userUbahInput == "Ya":
            for jalur in dataKrl:
                if "stasiun" in jalur:
                    for st in jalur["stasiun"]:
                        if jalur["stasiun"][st]["nama"] == namaStasiun:
                            jalur["stasiun"][st]["status"] = menjadiStatus
                elif "sub rute" in jalur:
                    for via in jalur["sub rute"]:
                        for st2 in jalur["sub rute"][via]:
                            if jalur["sub rute"][via][st2]["nama"] == namaStasiun:
                                jalur["sub rute"][via][st2]["status"] = menjadiStatus
            print(f"\nBerhasil! Stasiun {namaStasiun} telah di{menjadiStatus}kan\n")
        elif userUbahInput == "Tidak":
            print(f"\nBaik, Stasiun {namaStasiun} akan tetap di{statusSekarang}kan\n")
def prosesUbahStatus (line):
    listStasiun = namaStasiun(line)
    while True:
        tabelKrlSebagian(line)
        stasiunUbahStatus = input("\nMasukkan Stasiun yang ingin diubah Statusnya: ").strip().title()
        if stasiunUbahStatus in listStasiun:
            status = cariStatusStasiun(line, stasiunUbahStatus)                        
            print(f"\nSaat Ini Stasiun {stasiunUbahStatus} memiliki status {status}\n")
            if status == "Aktif":
                perubahanStatus(stasiunUbahStatus,"Aktif", "Nonaktif")
                break
            else:
                perubahanStatus(stasiunUbahStatus,"Nonaktif", "Aktif")
                break
        else:
            print("Maaf, Stasiun yang Anda Masukkan Tidak Ditemukan di Line Ini\n")
def updateStatusStasiun (line, role):
    if role == "Menengah":
        while True:
            print(f"""
=== Mengubah Status Stasiun di {line} ====
1. Ubah Status Stasiun
2. Kembali ke Menu Utama""")
            userPilih = input("\nMasukkan Pilihan Anda Bedasarkan Nomor: ").strip()
            if userPilih == "1":
                prosesUbahStatus(line)
            elif userPilih == "2":
                break
    elif role == "Tinggi":
        prosesUbahStatus(line)

def gantiKepalaCabang(line):
        for i in listMenengah:
            if i["region"] == line:
                ID = i["id"]
                tabelBedasarkanID(listMenengah, ID)
                continueGanti = validasiDuaPilihan("Apakah Anda Yakin Ingin Mengganti Data Ini?(ya/tidak) ", "Ya", "Tidak")
                if continueGanti == "Ya":
                    sebagianSeluruhKolom = validasiDuaPilihan("Apakah Anda Ingin Mengganti Seluruh Kolom atau Sebagian Data Kepala Cabang Saja?(seluruh/sebagian) ", "Seluruh", "Sebagian")
                    if sebagianSeluruhKolom == "Seluruh":
                        namaGanti = validasiHurup("Masukkan Nama Pengganti: ",3)
                        tahunGanti = validasiAngka("Masukkan Tahun Lahir Pengganti: ", "Tahun", 1955, 2025, 4)
                        jenisKelaminGanti = validasiDuaPilihan("Masukkan Jenis Kelamin Pengganti (Pria/Wanita): ", "Pria", "Wanita")
                        passwordGanti = validasiPassword("Masukkan Password Pengganti: ")
                        apakahSave = validasiDuaPilihan("Apakah Anda Yakin untuk Menyimpan Perubahan Ini?(ya/tidak) ", "Ya", "Tidak")
                        if apakahSave == "Ya":
                            i["id"] = pembuatanIdMenengah(namaGanti, tahunGanti, jenisKelaminGanti, i["region"])
                            i["nama"] = namaGanti
                            i["tahunLahir"] = tahunGanti
                            i["jenisKelamin"] = jenisKelaminGanti
                            i["password"] = passwordGanti 
                            print("\nData Kepala Cabang Berhasil Diubah.\n")
                        elif apakahSave == "Tidak":
                            print("\nBaik, Data Kepala Cabang Tidak Akan Diubah.\n")
                    elif sebagianSeluruhKolom == "Sebagian":
                        while True:
                            kolomGanti = input("Masukkan Kolom yang Ingin Diubah (nama/tahun lahir/jenis kelamin/password): ").strip().lower()
                            if kolomGanti == "nama":
                                namaGanti = validasiHurup("Masukkan Nama Pengganti: ",3)
                                apakahSave = validasiDuaPilihan("Apakah Anda Yakin untuk Menyimpan Perubahan Ini?(ya/tidak) ", "Ya", "Tidak")
                                if apakahSave == "Ya":
                                    i["id"] = pembuatanIdMenengah(namaGanti, i["tahunLahir"], i["jenisKelamin"], i["region"])
                                    i["nama"] = namaGanti
                                    print("\nData Kepala Cabang Berhasil Diubah.\n")
                                    break
                                elif apakahSave == "Tidak":
                                    print("\nBaik, Data Kepala Cabang Tidak Akan Diubah.\n")
                                    break
                            elif kolomGanti == "tahun lahir":
                                tahunGanti = validasiAngka("Masukkan Tahun Lahir Pengganti: ", "Tahun", 1955, 2025, 4)
                                apakahSave = validasiDuaPilihan("Apakah Anda Yakin untuk Menyimpan Perubahan Ini?(ya/tidak) ", "Ya", "Tidak")
                                if apakahSave == "Ya":
                                    i["id"] = pembuatanIdMenengah(i["nama"], tahunGanti, i["jenisKelamin"], i["region"])
                                    i["tahunLahir"] = tahunGanti
                                    print("\nData Kepala Cabang Berhasil Diubah.\n")
                                    break
                                elif apakahSave == "Tidak":
                                    print("\nBaik, Data Kepala Cabang Tidak Akan Diubah.\n")
                                    break
                            elif kolomGanti == "jenis kelamin":
                                jenisKelaminGanti = validasiDuaPilihan("Masukkan Jenis Kelamin Pengganti (Pria/Wanita): ", "Pria", "Wanita")
                                apakahSave = validasiDuaPilihan("Apakah Anda Yakin untuk Menyimpan Perubahan Ini?(ya/tidak) ", "Ya", "Tidak")
                                if apakahSave == "Ya":
                                    i["id"] = pembuatanIdMenengah(i["nama"], i["tahunLahir"], jenisKelaminGanti, i["region"])
                                    i["jenisKelamin"] = jenisKelaminGanti
                                    print("\nData Kepala Cabang Berhasil Diubah.\n")
                                    break
                                elif apakahSave == "Tidak":
                                    print("\nBaik, Data Kepala Cabang Tidak Akan Diubah.\n")
                                    break
                            elif kolomGanti == "password":
                                passwordGanti = validasiPassword("Masukkan Password Pengganti: ")
                                apakahSave = validasiDuaPilihan("Apakah Anda Yakin untuk Menyimpan Perubahan Ini?(ya/tidak) ", "Ya", "Tidak")
                                if apakahSave == "Ya":
                                    i["password"] = passwordGanti 
                                    print("\nData Kepala Cabang Berhasil Diubah.\n")
                                    break
                                elif apakahSave == "Tidak":
                                    print("\nBaik, Data Kepala Cabang Tidak Akan Diubah.\n")
                                    break
                            else:
                                print("Kolom yang Anda Masukkan Tidak Valid, Silahkan Masukkan Sesuai Opsi yang Tersedia\n")
                elif continueGanti == "Tidak":
                    print("\nBaik, Data Kepala Cabang Tidak Akan Diubah.\n")

def createCikarangVia(via):
    while True:   
        namaStasiunBaru = validasiHurup("Masukkan Nama Stasiun yang Ingin Ditambahkan: ", 3)
        listStasiun = namaStasiun("Cikarang Loop Line")
        if namaStasiunBaru in listStasiun:
            print("\nStasiun Sudah Terdaftar Sebelumnya\n")
            return
        else:
            listDictBaru = []
            for i in dataKrl:
                if i["line"] == "Cikarang Loop Line":
                    for j in i["sub rute"]:
                        if j == via:
                            for k in i["sub rute"][j]:
                                listDictBaru.append(i["sub rute"][via][k])
                    statusStasiunBaru = validasAktifNonaktif("Masukkan Status Stasiun (Aktif/Nonaktif): ")
                    dictStasiunBaru = {"nama": namaStasiunBaru, "status": statusStasiunBaru}
                    tabelBedasarkanID(dictStasiunBaru, namaStasiunBaru)
                    apakahBenar = validasiDuaPilihan("Apakah Sudah Benar Data Stasiun yang Ingin di Tambah?(sudah/belum) ", "Sudah", "Belum")
                    if apakahBenar == "Sudah":
                        tabelBedasarkanID(listDictBaru)
                        posisiStasiun = validasiAngka("Pilih Nomor Urut Posisi Stasiun (Stasiun Lama Akan Bergeser ke Bawah): ", "Pilihan", 1, len(listDictBaru), 2)
                        apakahSave = validasiDuaPilihan(f"Apakah Anda Yakin Untuk Menambah Stasiun {namaStasiunBaru} di Urutan ke-{posisiStasiun}?(ya/tidak) ", "Ya", "Tidak")
                        if apakahSave == "Ya":    
                            listDictBaru.insert(posisiStasiun-1, dictStasiunBaru)
                            for l in range(len(listDictBaru)):
                                i["sub rute"][via][l+1] = listDictBaru[l]
                            print(f"\nData Stasiun Baru Telah Ditambagkan di Cikarang Loop Line ({(via).title()}).")
                            return
                        elif apakahSave == "Tidak":
                            print("\nBaik, Data Stasiun Baru Tidak Akan Disimpan.")
                            return    
                    elif apakahBenar == "Belum":
                        print("\nJika Belum, Silahkan Isi Ulang Data.")
def createSelainCikarang(line):
    while True:
        namaStasiunBaru = validasiHurup("Masukkan Nama Stasiun yang Ingin Ditambahkan: ", 3)
        listStasiun = namaStasiun(line)
        if namaStasiunBaru in listStasiun:
            print("\nStasiun Sudah Terdaftar Sebelumnya\n")
            return
        else:
            listDictBaru = []
            for i in dataKrl:
                if i["line"] == line:
                    if "stasiun" in i:
                        for j in i["stasiun"]:
                            listDictBaru.append(i["stasiun"][j])
                    statusStasiunBaru = validasAktifNonaktif("Masukkan Status Stasiun (Aktif/Nonaktif): ")
                    dictStasiunBaru = {"nama": namaStasiunBaru, "status": statusStasiunBaru}    
                    tabelBedasarkanID(dictStasiunBaru)
                    apakahBenar = validasiDuaPilihan("Apakah Sudah Benar Data Stasiun yang Ingin di Tambah?(sudah/belum) ", "Sudah", "Belum")
                    if apakahBenar == "Sudah":
                        tabelBedasarkanID(listDictBaru)
                        posisiStasiun = validasiAngka("Pilih Nomor Urut Posisi Stasiun (Stasiun Lama Akan Bergeser ke Bawah): ", "Pilihan", 0, len(listDictBaru), 2)
                        apakahSave = validasiDuaPilihan(f"Apakah Anda Yakin Untuk Menambah Stasiun {namaStasiunBaru} di Urutan ke-{posisiStasiun}?(ya/tidak) ", "Ya", "Tidak")
                        if apakahSave == "Ya":
                            listDictBaru.insert(posisiStasiun-1, dictStasiunBaru)
                            for k in range(len(listDictBaru)):
                                i["stasiun"][k+1] = listDictBaru[k]
                            print(f"\nData Stasiun Baru Telah Ditambahkan di {line}.\n")
                            return
                        elif apakahSave == "Tidak":
                            print("\nBaik, Data Stasiun Baru Tidak Akan Disimpan.\n")
                            return
                    elif apakahBenar == "Belum":
                        print("\nJika Belum, Silahkan Isi Ulang Data.")      

while True:
    print("""
================= Selamat Datang di ====================
===== Sistem Informasi dan Manajemen KRL Commuter ======
1. Login sebagai Petugas
2. Masuk sebagai Penumpang (User)
          """)
    userInput = validasiAngka("Pilih Akses Anda:(1/2) ", "Pilihan", 1, 2, 1)
    if userInput == 1:
        nama = validasiHurup("Masukkan Nama Lengkap Anda? ", 3)
        lahir = validasiAngka("Masukkan Tahun Lahir Anda: ", "Tahun", 1955, 2025, 4)
        jenisKelamin = validasiDuaPilihan("Masukkan Jenis Kelamin Anda?(Pria/Wanita ) ", "Pria", "Wanita")
        catUser , iterasi = kategoriUser(nama, lahir, jenisKelamin)
        if catUser == "Menengah": 
            userPercobaan = loginPass (listMenengah, nama, lahir, jenisKelamin)
            if userPercobaan == 3:
                print("Anda Sudah Melebihi Batas Coba, Silahkan Coba Beberapa Saat Lagi")
                continue
            else:
                while True:
                    print(f"""
Saat ini Anda memiliki akses penuh untuk:
1. Mencari Rekomendasi Rute yang Akan di Lalui 
2. Melihat Data dan Statistik Penumpang di Seluruh Stasiun dalam {iterasi["region"]}.
3. Mengganti Status Operasional Stasiun (Aktif/Nonaktif) dalam {iterasi["region"]}.
4. Keluar Dari Menu.""")   
                    fiturAkses = input("Masukkan Nomer Fitur Akses yang Ingin Digunakan: ").strip()
                    if fiturAkses == "1":
                        ruteRekomendasi(nama, lahir, jenisKelamin)
                    elif fiturAkses == "2":
                        melihatDataStatistikRendah(iterasi["region"], catUser)
                    elif fiturAkses == "3":
                        updateStatusStasiun(iterasi["region"], catUser)
                    elif fiturAkses == "4":
                        break
                    else:
                        print("Opsi yang Anda Masukkan Tidak Valid\n")
        elif catUser == "Tinggi":
            userPercobaan = loginPass(listTinggi, nama, lahir, jenisKelamin)
            if userPercobaan == 3:
                print("Anda Sudah Melebihi Batas Coba, Silahkan Coba Beberapa Saat Lagi\n")
                continue
            else:
                while True:
                    print(f"""
Saat ini Anda memiliki akses penuh untuk: 
1. Melihat Data Penumpang.
2. Mengganti Status Data di Suatu Line.
3. Menghapus Data Orang Dalam Penumpang Bedasarkan ID.
4. Manambahkan Stasiun Baru.
5. Keluar Dari Menu.
6. Matikan Sistem.""")
                    fiturAkses = input("\nMasukkan Nomer Fitur Akses yang Ingin Digunakan Bedasarkan Nomor: ").strip()
                    if fiturAkses == "1":
                        while True:
                            print("""
============= Menu Melihat Data Penumpang =============
1. Melihat Data Seluruh Penumpang.
2. Melihat Data Penumpang Bedasarkan ID.
3. Melihat Data dan Statistik Penumpang  Bedasarkan Line.
4. Mencari Rekomendasi Rute yang Akan di Lalui.
5. Kembali ke Menu Utama""")
                            userPilih = input("\nMasukkan Pilihan Anda Bedasarkan Nomor: ").strip()
                            if userPilih == "1":
                                tabelUser(listRendah)
                            elif userPilih == "2":
                                masukkanID = input("\nMasukkan ID Penumpang yang Ingin Dilihat Datanya: ").strip().upper()
                                listID = []
                                for p in listRendah:
                                    listID.append(p["id"])
                                if masukkanID in listID:
                                    tabelBedasarkanID(listRendah, masukkanID)      
                                else:
                                    print("Maaf, ID yang Anda Masukkan Tidak Ditemukan.\n")
                            elif userPilih == "3":
                                while True:
                                    print("Daftar Line di KRL")
                                    nomor = 1
                                    for i in dataKrl:
                                        print(f"{nomor}. {i["line"]}")
                                        nomor += 1
                                    pilihLine = input("\nMasukkan Line yang Ingin Dipilih Bedasarkan Nomor: ").strip().title()
                                    if pilihLine in ["1", "2", "3", "4", "5"]:
                                        melihatDataStatistikRendah(dataKrl[int(pilihLine)-1]["line"], catUser)
                                        break
                                    else:
                                        print("Input yang Anda Masukkan Tidak Valid\n")
                            elif userPilih == "4":
                                ruteRekomendasi(nama, lahir, jenisKelamin)
                            elif userPilih == "5":
                                break
                            else:
                                print("Opsi yang Anda Masukkan Tidak Valid\n")
                    elif fiturAkses == "2":
                        while True:
                            listID = []
                            tabelBedasarkanID(dataKrl)
                            for i in dataKrl:
                                listID.append(i["id"])
                            pilihID = input("\nMasukkan Line yang Ingin Dipilih Bedasarkan ID: ").strip().upper()
                            if pilihID in listID:
                                for i in dataKrl:
                                    if i["id"] == pilihID:
                                        line = i["line"]
                                while True:
                                    print(f"""
============= Menu Update Data {line} =============
1. Mengganti Data Kepala Cabang.
2. Mengganti Status Operasional Stasiun (Aktif/Nonaktif).
3. Kembali ke Menu Utama.""")
                                    userPilihSubMenu = input("\nMasukkan Pilihan Anda Bedasarkan Nomor: ").strip()        
                                    if userPilihSubMenu == "1":
                                        gantiKepalaCabang(line)
                                    elif userPilihSubMenu == "2":
                                        updateStatusStasiun(line, catUser)
                                    elif userPilihSubMenu == "3":
                                        break
                                    else:
                                        print("Input yang Anda Masukkan Tidak Valid!")
                                break
                            else:
                                print("Input yang Anda Masukkan Tidak Valid!")
                    elif fiturAkses == "3":
                        if len(listRendah) == 0:
                            print("Tidak Ada Data Penumpang yang Dapat Diproses untuk Penghapusan")
                        else:
                            while True:
                                print("""
========= Menu Hapus Data Penumpang =========
1. Hapus Data Penumpang.
2. Kembali ke Menu Utama.""")
                                userPilih = input("\nMasukkan Pilihan Anda Bedasarkan Nomor: ").strip()
                                if userPilih == "1":
                                    tabelUser(listRendah)
                                    pilihIdRendah = input("Masukkan ID Pengguna yang ingin di hapus: ").strip().upper()
                                    listID = []
                                    for p in listRendah:
                                        listID.append(p["id"])

                                    if pilihIdRendah in listID:
                                        listIndex=[]
                                        for p in range(len(listRendah)):
                                            if listRendah[p]["id"] == pilihIdRendah:
                                                listIndex.append(p)
                                        tabelBedasarkanID(listRendah, pilihIdRendah)
                                        if len(listIndex) > 1:
                                            apakahHapus = validasiDuaPilihan("Apakah Anda Yakin untuk Menghapus Data Ini?(ya/tidak) ", "Ya", "Tidak")
                                            if apakahHapus == "Ya":
                                                apakahHapusSemua = validasiDuaPilihan("Mau Hapus Sekaligus atau Sebagian:(sekaligus/sebagian) ", "Sekaligus", "Sebagian")
                                                if apakahHapusSemua == "Sekaligus":
                                                    for i in sorted(listIndex, reverse = True):
                                                        dataDihapus = listRendah.pop(i)
                                                    print(f"\nData {dataDihapus['nama']} dengan ID {dataDihapus['id']} berhasil dihapus.\n")
                                                elif apakahHapusSemua == "Sebagian":
                                                    listIdPerjalanan = []
                                                    for i in listRendah:
                                                        if i["id"] == pilihIdRendah:
                                                            listIdPerjalanan.append(i["idPerjalanan"])
                                                    pilihIDpj = input("Masukkan ID Perjalanan yang ingin Anda Hapus: ").strip().upper()
                                                    if pilihIDpj in listIdPerjalanan:
                                                        for i in range(len(listRendah)):
                                                            if listRendah[i]["idPerjalanan"] == pilihIDpj:
                                                                dataDihapus = listRendah.pop(i)
                                                                break
                                                        print(f"\nData {dataDihapus['nama']} dengan ID Perjalanan {dataDihapus['idPerjalanan']} berhasil dihapus.\n")
                                                    else:
                                                        print("ID Perjalanan yang Anda Masukkan Tidak Terdaftar")
                                            elif apakahHapus == "Tidak":
                                                print("\nBaik, Data Tidak Akan Dihapus.\n")
                                        elif len(listIndex) == 1:    
                                            apakahHapus = validasiDuaPilihan("Apakah Anda Yakin untuk Menghapus Data Ini?(ya/tidak) ", "Ya", "Tidak")
                                            if apakahHapus == "Ya":
                                                dataDihapus = listRendah.pop(listIndex[0])
                                                print(f"\nData {dataDihapus['nama']} dengan ID {dataDihapus['id']} berhasil dihapus.\n")
                                            elif apakahHapus == "Tidak":
                                                print("\nBaik, Data Tidak Akan Dihapus.\n")
                                    else:
                                        print("ID yang Anda Masukkan Tidak Terdaftar.\n")
                                elif userPilih == "2":
                                    break
                    elif fiturAkses == "4":
                        while True:
                            print("""
====Manambahkan Stasiun Baru=====
1. Tambah Stasiun.
2. Kembali ke Menu Utama""")
                            userPilih = input("\nMasukkan Pilihan Anda Sesuai Angka: ").strip()
                            if userPilih == "1":
                                while True:
                                    print("Daftar Line di KRL")
                                    nomor = 1
                                    for i in dataKrl:
                                        print(f"{nomor}. {i["line"]}")
                                        nomor += 1
                                    pilihLine = input("\nMasukkan Line yang Ingin Dipilih untuk Ditambahkan Stasiun: ").strip()
                                    if pilihLine == "2":
                                        while True:
                                            print("""
=====Daftar Jalur di Cikarang Loop Line===
1. Cikarang Utama
2. Via Manggarai
3. Via Pasar Senen""")
                                            viaMana = input("\nPilih Daerah Jalur Mana untuk Ditambahkan: ").strip().lower()
                                            if viaMana == "1":
                                                createCikarangVia("cikarang utama")
                                                break
                                            elif viaMana == "2":
                                                createCikarangVia("via manggarai")
                                                break
                                            elif viaMana == "3":
                                                createCikarangVia("via pasar senen")
                                                break
                                            else:
                                                print("Opsi yang Anda Masukkan Tidak Valid, Silahkan Masukkan Sesuai Opsi yang Tersedia\n")
                                        break
                                    elif pilihLine in ["1", "3", "4", "5"]:
                                        createSelainCikarang(dataKrl[int(pilihLine)-1]["line"])
                                        break              
                                    else:
                                        print("Pilhan Anda Tidak Valid, Silahkan Coba Kembali\n")
                            elif userPilih == "2":
                                    break   
                            else:
                                print("Opsi yang Anda Masukkan Tidak Valid, Silahkan Masukkan Sesuai Opsi yang Tersedia")                    
                    elif fiturAkses == "5":   
                            break
                    elif fiturAkses == "6":
                        yaTidak = validasiDuaPilihan("Apakah Anda Yakin Ingin Mematikan Sistem?(ya/tidak) ", "Ya", "Tidak")
                        if yaTidak == "Tidak":
                            continue    
                        elif yaTidak == "Ya":
                            print("Terima Kasih Telah Menggunakan Sistem Informasi dan Manajemen KRL Commuter, Sampai Jumpa!")
                            exit()
                    else:
                        print("Opsi yang Anda Masukkan Tidak Valid")
        else :
            print("\nData yang Anda Masukkan Tidak Terdaftar sebagai Petugas.")
    elif userInput == 2:
        nama = validasiHurup("Masukkan Nama Lengkap Anda? ", 3)
        lahir = validasiAngka("Masukkan Tahun Lahir Anda: ", "Tahun", 1955, 2025, 4)
        jenisKelamin = validasiDuaPilihan("Masukkan Jenis Kelamin Anda?(Pria/Wanita ) ", "Pria", "Wanita")
        if jenisKelamin == "Pria":
            print(f"\nSelamat Datang di Sistem Informasi Layanan KRL Commuter, Bapak {nama}\nSaat ini Anda dapat Menggunakan Fitur Rekomendasi Rute")
        elif jenisKelamin == "Wanita":
            print(f"\nSelamat Datang di Sistem Informasi Layanan KRL Commuter, Ibu {nama}\nSaat ini Anda dapat Menggunakan Fitur Rekomendasi Rute")
        ruteRekomendasi(nama, lahir, jenisKelamin)
