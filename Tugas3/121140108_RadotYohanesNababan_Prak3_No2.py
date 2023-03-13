class Karyawan:
    #atribut kelas menyimpan jumlah karyawan
    jumlah_karyawan = 0

    #initial
    def __init__(self, nama, gaji, jabatan):
        self.__nama = nama      #atribut private
        self.gaji = gaji        #atribut public
        self._jabatan = jabatan #atribut protected
        Karyawan.jumlah_karyawan += 1

    #fungsi menampilkan nama karyawan
    def tampil_nama(self):
        print(f"Nama : {self.__nama}")

    #fungsi menampilkan gaji karyawan   
    def tampil_gaji(self):
        print(f"Gaji : {self.gaji}")
    
    #fungsi menampilkan jabatan
    def tampil_jabatan(self):
        print(f"Jabatan = {self._jabatan}")
    
    #fungsi inputan mengubah jabatan
    def ubah_jabatan(self, jabatan_baru):
        self._jabatan = jabatan_baru
    
    #fungsi mengubah/update gaji sesuai jabatan
    def ubah_gaji (self):
      if (self._jabatan == "Manager"):
        self.gaji = 10000000
      elif (self._jabatan == "President" ):
        self.gaji = 15000000
      elif (self._jabatan == "Staf"):
        self.gaji = 5000000
    
    #fungsi menambah gaji
    def tambah_gaji (self,gajiplus):
      self.gaji += gajiplus
    

karyawan1 = Karyawan("Radot", 10000000, "Manager")
karyawan2 = Karyawan("Eko", 5000000, "Staf")
karyawan3 = Karyawan("Rafli", 15000000, "President")

karyawan1.tampil_nama() 
karyawan1.tampil_gaji() 
karyawan1.tampil_jabatan()
print("--------")

karyawan1.ubah_jabatan("President")
karyawan1.tampil_jabatan() 
karyawan1.ubah_gaji()
karyawan1.tampil_gaji()
print ("--------")
karyawan1.tambah_gaji(500000)
karyawan1.tampil_gaji()
print ("-------")

karyawan2.tampil_nama()
karyawan3.tampil_gaji()
print ("---------")
print (f"Jumlah Karyawan saat ini adalah : {Karyawan.jumlah_karyawan} orang")
