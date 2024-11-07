# Nama: Rafli Ahmad Fauzi
# NIM: 2405815
# 1B RPL

def kesempatanlogin():
    login = 3
    print("Silakan login")

    while login > 0:
        username = input(f"Username : ")
        password = input(f"Password : ")
        if password == "latihan":
            print("Selamat anda telah berhasil login!")
            break
        else:
            login -= 1
            if login > 0:
                print(f"Login salah! Kesempatan Anda {login} x kali lagi")
            else:
                print("Anda telah melebihi batas percobaan login.")
kesempatanlogin()