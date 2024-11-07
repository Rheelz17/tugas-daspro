# Nama: Rafli Ahmad Fauzi
# NIM: 2405815
# 1B RPL

def fibonacci(n):
    if n <= 0:
        return []
    elif n == 1:
        return [0]
    elif n == 2:
        return [0, 1]
    
    fib_sequence = [0, 1]
    for i in range(2, n):
        next_fib = fib_sequence[-1] + fib_sequence[-2]
        fib_sequence.append(next_fib)
    return fib_sequence

jumlah_elemen = int(input("Masukkan jumlah angka Fibonacci: "))
deret_fibonacci = fibonacci(jumlah_elemen)
print(f"Deret fibonacci ke-{jumlah_elemen}: {deret_fibonacci}")
    