class AkunBank:
    list_pelanggan = []

    def __init__(self, no_pelanggan, nama_pelanggan, jumlah_saldo):
        self.__no_pelanggan = no_pelanggan
        self.__nama_pelanggan = nama_pelanggan
        self.__jumlah_saldo = jumlah_saldo
        self.list_pelanggan.append(self)


    def lihat_menu(self):
      #menampilkan menu tanpa dipanggil 
        print(f"Halo {Akun1.__nama_pelanggan}, ingin melakukan apa?")
        print("1. Lihat saldo \n 2. Tarik tunai \n 3. Transfer Saldo \n 4. Keluar")

    def lihat_saldo(self):
      #fungsi untuk melihat saldo Akun1
        print("Radot memiliki saldo", Akun1.__jumlah_saldo)

    def tarik_tunai(self, jlhtarik):
      #fungsi tarik tunai 
        if jlhtarik > Akun1.__jumlah_saldo:
            print("Nominal saldo yang anda punya tidak cukup!")
        else:
            Akun1.__jumlah_saldo = Akun1.__jumlah_saldo - jlhtarik
            print("Saldo berhasil ditarik!")

    def transfer_otomatis (self,nominal,nopel):
      #fungsi transfer dengan pengecekan saldo Akun1
      if nominal < self.__jumlah_saldo: 
        #fungsi apabila saldo Akun1 cukup
        for pelanggan in self.list_pelanggan:
            if pelanggan.__no_pelanggan == nopel:
              pelanggan.__jumlah_saldo += nominal
              self.__jumlah_saldo -= nominal
              print (f"Transfer Rp. {nominal} ke {pelanggan.__nama_pelanggan} sukses!")

      else :
            print ("Saldo anda tidak mencukupi untuk melakukan transfer! \n Kembali Ke Menu Utama")
    


Akun1 = AkunBank("1234", "Radot", 5000000000)
Akun2 = AkunBank("2345", "Ukraina", 6666666666)
Akun3 = AkunBank("3456", "Elon Musk", 9999999999)

Loop = True
while Loop:
    print("Selamat datang di Bank Jago")
    Akun1.lihat_menu()
    akses_akun = (input("Masukkan nomor input : "))
    if akses_akun == '1':
        Akun1.lihat_saldo()
    elif akses_akun == '2':
        jlhtarik = int(input("Masukkan nominal yang ingin ditarik : "))
        Akun1.tarik_tunai(jlhtarik)
    elif akses_akun == '3':
        nominal_input = int(input("Masukkan nominal yang ingin di transfer : "))
        nopel_input = input("Masukkan no rekening tujuan : ")
        Akun1.transfer_otomatis(nominal_input, nopel_input)
    elif akses_akun == '4':
      Loop = False
      

