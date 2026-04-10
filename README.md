# 📺 Youtube Downloader with Python (BeeWare)

Aplikasi downloader sederhana yang memungkinkan pengguna untuk mengunduh video atau audio dari YouTube secara gratis tanpa memerlukan API Key. Dibangun menggunakan framework **BeeWare (Toga)** dan **yt-dlp**.

## ✨ Fitur Utama
* **Download Video:** Mengunduh video dengan kualitas terbaik yang tersedia.
* **Download Audio:** Mengonversi video YouTube langsung menjadi format audio (MP3).
* **Multi-Platform:** Dapat dikemas menjadi installer Windows (.msi) dan Android (.apk).
* **Tanpa API Key:** Menggunakan library `yt-dlp` sehingga tidak memerlukan pendaftaran Google Cloud.

---

## 💻 Panduan Instalasi (Windows)

Jika Anda mendapatkan file installer `.msi`, ikuti langkah-langkah berikut:

1. **Jalankan Installer**: Klik dua kali pada file `Downloader Youtube-0.0.1.msi`.
2. **Peringatan Keamanan**: Muncul kotak biru bertuliskan *"Windows protected your PC"*?
   * Klik tulisan **"More info"**.
   * Klik tombol **"Run anyway"**.
3. **Ikuti Wizard**: Klik **Next** > **Install**, dan tunggu hingga proses selesai.
4. **Selesai**: Aplikasi kini terpasang secara permanen di sistem Anda.

---

## 🚀 Cara Menggunakan

1. **Buka Aplikasi**: Klik tombol **Start**, ketik *"Downloader Youtube"*, dan jalankan aplikasinya.
2. **Salin Link**: Buka YouTube dan **Copy Link** video yang ingin Anda unduh.
3. **Tempel Link**: Masukkan link tersebut ke kotak input di aplikasi.
4. **Pilih Format**: Pilih opsi **Video** atau **Audio** pada menu yang tersedia.
5. **Download**: Klik tombol **Mulai Download**.
6. **Lokasi File**: Setelah muncul notifikasi **"Berhasil!"**, file Anda dapat ditemukan di folder **Downloads** komputer Anda.

---

## 🛠️ Pengembangan (Untuk Developer)

Jika Anda ingin menjalankan atau mengembangkan proyek ini dari source code:

1. **Clone Repositori**:
   ```bash
   git clone [https://github.com/daffaandhikapratama905-oss/youtube-downloader-python](https://github.com/daffaandhikapratama905-oss/youtube-downloader-python.git)
   cd youtube-downloader-python