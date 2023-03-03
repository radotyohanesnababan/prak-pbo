class Biodata:
  def __init__ (self,nama,NIM,kelasPBO,jumlahSKS, IPK):
    self.nama = nama
    self.NIM = NIM
    self.kelasPBO = kelasPBO
    self.jumlahSKS = jumlahSKS
    self.IPK =IPK
  def cetak (self):  
    print(f"Nama : {self.nama}, dengan NIM {self.NIM}, di kelas PBO {self.kelasPBO}. Jumlah SKS yang diambil adalah {self.jumlahSKS}")

  def cekSKS_nextsemester (self,IPK):
    if (self.IPK >= 3):
      print("Semester selanjutnya bisa mengambil 24 SKS")
    else:
      print ("Semester selanjutnya tidak bisa mengambil 24 SKS")
    
ipk = int(input("Masukkan IPK :"))
bio1 = Biodata("Radot", 121140108, "RB", 22, ipk)
bio1.cetak()
bio1.cekSKS_nextsemester(ipk)

