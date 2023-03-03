def cekpass(uname, pasw):
    if uname == "informatika" and pasw == "12345678":
        print("Berhasil Login!")
        exit()
    else:
        print("Username atau password salah!")



for i in range(0, 3):
    username = input("Masukkan username anda : ")
    password = input("Masukkan password anda : ")
    cekpass(username, password)
print("Akun terblokir!")
