# KeyBloom ESP32-C3 BLE Prototype

Prototype ini menguji komunikasi BLE antara ESP32-C3 dan Windows 11 tanpa mengubah aplikasi atau firmware utama KeyBloom.

## Arsitektur

- Nama BLE: `KeyBloom-C3`
- Service UUID: `7c3a0001-8f6e-4d4b-a8f3-6f8f9c1b0001`
- Event characteristic UUID: `7c3a0002-8f6e-4d4b-a8f3-6f8f9c1b0001`
- Transport: custom BLE GATT notification
- Pairing tidak diperlukan untuk prototype ini

Format event sengaja sama dengan firmware serial utama:

```text
BUTTON 1 PRESSED
ENC1 RIGHT
ENC1 LEFT
ENC1 BUTTON PRESSED
ENC2 RIGHT
ENC2 LEFT
ENC2 BUTTON PRESSED
```

## 1. Siapkan Arduino IDE

1. Pastikan board package `esp32 by Espressif Systems` sudah terpasang.
2. Pilih board ESP32-C3 yang sesuai dengan hardware.
3. Buka `ESP32C3_BLE_Test/ESP32C3_BLE_Test.ino`.
4. Install library `NimBLE-Arduino` versi 2.x melalui Library Manager.
5. Upload firmware ke ESP32-C3.
6. Buka Serial Monitor dengan baud `115200`.

Output awal yang diharapkan:

```text
[BLE] Advertising as KeyBloom-C3
START
```

## 2. Siapkan Python

Dari root repository:

```powershell
python -m venv bluetooth_test\.venv
bluetooth_test\.venv\Scripts\python.exe -m pip install -r bluetooth_test\requirements.txt
```

## 3. Scan Perangkat

Pastikan Bluetooth Windows 11 aktif, lalu jalankan:

```powershell
bluetooth_test\.venv\Scripts\python.exe bluetooth_test\bluetooth_test.py --scan-only
```

Cari perangkat bernama `KeyBloom-C3` atau baris yang memiliki marker `<KeyBloom>`.

## 4. Connect dan Dengarkan Event

```powershell
bluetooth_test\.venv\Scripts\python.exe bluetooth_test\bluetooth_test.py
```

Tekan tombol dan putar encoder. Contoh output:

```text
[BLE] Connected: True
[14:20:30.804] [EVENT] START
[BLE] Listening for events. Press Ctrl+C to stop.
[14:20:31.125] [EVENT] BUTTON 1 PRESSED
[14:20:33.421] [EVENT] ENC1 RIGHT
```

Klien otomatis melakukan scan dan reconnect ketika ESP32 dimatikan atau koneksi terputus.

Jika pencarian berdasarkan nama gagal tetapi alamat terlihat saat scan, gunakan:

```powershell
bluetooth_test\.venv\Scripts\python.exe bluetooth_test\bluetooth_test.py --address "ALAMAT_DARI_HASIL_SCAN"
```

Pada Windows, address dari Bleak dapat berupa UUID dan bukan MAC address. Gunakan nilai persis seperti hasil scan.

## Checklist Pengujian

- ESP32 muncul sebagai `KeyBloom-C3`.
- Python dapat connect tanpa pairing manual.
- Semua enam tombol menghasilkan event yang benar.
- Kedua encoder menghasilkan arah dan event tombol yang benar.
- Tidak ada event ganda untuk satu detent encoder.
- Python mendeteksi disconnect ketika ESP32 dimatikan.
- Python reconnect setelah ESP32 dinyalakan kembali.
- Koneksi tetap stabil setidaknya 30 menit.

## Catatan

- ESP32-C3 mendukung BLE, bukan Bluetooth Classic SPP.
- Firmware ini tetap mencetak semua event ke serial untuk membantu debugging.
- Jangan mengganti firmware utama sebelum prototype ini lolos pengujian.
