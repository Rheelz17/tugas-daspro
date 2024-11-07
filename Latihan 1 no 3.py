# Nama: Rafli Ahmad Fauzi
# NIM: 2405815
# 1B RPl


def rata_rata(*angka):
    total = sum(angka)
    ratarata = total / len(angka)
    return total, ratarata

angka = []
while True:
    input_angka = int(input(f"Masukkan angka (Masukkan 0 untuk berhenti): "))
    if input_angka == 0:
        break
    angka.append(input_angka)

total, ratarata = rata_rata(*angka)
print(f"Total: {total}")
print(f"Rata-rata: {total}/{len(angka)} = {ratarata}")