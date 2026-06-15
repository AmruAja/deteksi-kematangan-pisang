# Deteksi Kematangan Pisang

Aplikasi desktop berbasis **Python** yang digunakan untuk mendeteksi tingkat kematangan buah pisang melalui pengolahan citra digital. Sistem akan menganalisis warna kulit pisang menggunakan metode **HSV (Hue, Saturation, Value)** dan mengklasifikasikan kondisi pisang menjadi **Mentah**, **Matang**, atau **Terlalu Matang**.

---

## Fitur

- Upload gambar pisang
- Deteksi warna menggunakan metode HSV
- Klasifikasi tingkat kematangan pisang
- Menampilkan nilai Hue dan Saturation
- Antarmuka GUI menggunakan Tkinter
- Pengolahan citra menggunakan OpenCV

---

## Teknologi yang Digunakan

- Python
- OpenCV
- NumPy
- Pillow (PIL)
- Tkinter

---

## Struktur Project

```text
Deteksi-Kematangan-Pisang/
│
├── deteksikematanganpisang.py
├── requirements.txt
├── README.md
└── test pisang/
```

---

## Menjalankan Project

### 1. Membuat Virtual Environment

```bash
python -m venv venv
```

Aktifkan virtual environment:

Windows

```bash
venv\Scripts\activate
```

Linux / MacOS

```bash
source venv/bin/activate
```

---

### 2. Install Dependency

```bash
pip install -r requirements.txt
```

atau

```bash
pip install opencv-python pillow numpy
```

---

### 3. Menjalankan Aplikasi

```bash
python deteksikematanganpisang.py
```

Jika berhasil maka akan muncul tampilan aplikasi:

- Tombol **Masukkan Gambar**
- Preview gambar pisang
- Hasil klasifikasi kematangan
- Nilai Hue dan Saturation

---

## Cara Penggunaan

### 1. Pilih Gambar

Klik tombol:

```text
Masukkan Gambar
```

Kemudian pilih gambar pisang yang ingin dianalisis.

---

### 2. Proses Analisis

Sistem akan:

- Membaca gambar
- Melakukan segmentasi objek pisang
- Menghitung rata-rata warna HSV
- Menentukan tingkat kematangan

---

### 3. Hasil Deteksi

Contoh hasil:

```text
Hasil : Mentah
Hue : 86.82
Saturasi : 0.31
```

---

## Kategori Kematangan

### Pisang Mentah

Karakteristik:

- Warna hijau dominan
- Nilai Hue tinggi

Output:

```text
Mentah
```

---

### Pisang Matang

Karakteristik:

- Warna kuning dominan
- Hue berada pada rentang kuning

Output:

```text
Matang
```

---

### Pisang Terlalu Matang

Karakteristik:

- Banyak bercak coklat atau hitam
- Saturasi menurun

Output:

```text
Terlalu Matang
```

---

## Dataset Pengujian

Gunakan gambar dengan:

- Format JPG atau PNG
- Objek pisang terlihat jelas
- Latar belakang tidak terlalu kompleks
- Pencahayaan cukup

---

## Troubleshooting

### Module Not Found

Install kembali dependency:

```bash
pip install opencv-python pillow numpy
```

---

### OpenCV Tidak Terdeteksi

```bash
pip install opencv-python
```

Cek instalasi:

```bash
pip show opencv-python
```

---

### Gambar Tidak Muncul

Pastikan:

- Format JPG atau PNG
- File tidak rusak
- Lokasi file dapat diakses

---

## Hasil Penelitian

Metode HSV digunakan karena mampu membedakan perubahan warna kulit pisang selama proses pematangan sehingga tingkat kematangan dapat diidentifikasi secara otomatis berdasarkan karakteristik warna objek.

---

## Developer

Aplikasi Deteksi Kematangan Pisang merupakan implementasi pengolahan citra digital menggunakan Python untuk membantu identifikasi tingkat kematangan buah pisang secara otomatis berdasarkan analisis warna HSV.
