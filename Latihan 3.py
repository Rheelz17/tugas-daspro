# Nama: Rafli Ahmad Fauzi
# NIM: 2405815
# 1B RPL

def selisih_waktu(jam_mulai, menit_mulai, detik_mulai, jam_selesai, menit_selesai, detik_selesai):
    # mengubah semua ke detik
    total_detik_mulai = jam_mulai * 3600 + menit_mulai * 60 + detik_mulai
    total_detik_selesai = jam_selesai * 3600 + menit_selesai * 60 + detik_selesai

    # menghitung selisih detik
    selisih_detik = total_detik_selesai - total_detik_mulai

    # mengubah kembali ke jam, menit, dan detik
    selisih_jam = selisih_detik // 3600
    selisih_detik %= 3600
    selisih_menit = selisih_detik // 60
    selisih_detik %= 60

    return selisih_jam, selisih_menit, selisih_detik

jam_mulai = int(input("Masukkan jam mulai: "))
menit_mulai = int(input("Masukkan menit mulai: "))
detik_mulai = int(input("Masukkan detik mulai: "))

jam_selesai = int(input("Masukkan jam selesai: "))
menit_selesai = int(input("Masukkan menit selesai: "))
detik_selesai = int(input("Masukkan detik selesai: "))

selisih_jam, selisih_menit, selisih_detik = selisih_waktu(jam_mulai, menit_mulai, detik_mulai, jam_selesai, menit_selesai, detik_selesai)
print(f"Selisih waktu: {selisih_jam} jam - {selisih_menit} menit - {selisih_detik} detik")