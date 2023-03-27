class Komputer:

    def __init__(self, nama, merk, jenis, harga):
        self.nama = nama
        self.jenis = jenis
        self.harga = harga
        self.merk = merk


class Processor(Komputer):
    def __init__(self, nama, merk, jenis, harga, jumlah_core, kecepatan_processor):
        super().__init__(nama, merk, jenis, harga)
        self.jumlah_core = jumlah_core
        self.kecepatan_processor = kecepatan_processor


class RAM(Komputer):
    def __init__(self, nama, merk, jenis, harga, capacity):
        super().__init__(nama, merk, jenis, harga)
        self.capacity = capacity


class HDD(Komputer):
    def __init__(self, nama, merk, jenis, harga, capacity, RPM):
        super().__init__(nama, merk, jenis, harga)
        self.capacity = capacity
        self.RPM = RPM


class VGA(Komputer):
    def __init__(self, nama, merk, jenis, harga, capacity):
        super().__init__(nama, merk, jenis, harga)
        self.capacity = capacity


class PSU(Komputer):
    def __init__(self, nama, merk, jenis, harga, daya):
        super().__init__(nama, merk, jenis, harga)
        self.daya = daya


rakit = [[Processor('Processor', 'Intel', 'Core i7 7740X', 4350000, 4, '4.3GHz'),
          RAM('RAM', 'V-Gen', 'DDR4 SODimm PC19200/2400MHz', 328000, '4GB'),
          HDD('HDD', 'Seagate', 'HDD 2.5 inch', 295000, '500GB', 7200),
          VGA('VGA', 'Asus', 'VGA GTX 1050', 250000, '2GB'),
          PSU('PSU', 'Corsair', 'Corsair V550', 250000, '500W')],
         [Processor('Processor', 'AMD', 'Ryzen 5 3600', 250000, 4, '4.3GHz'),
          RAM('RAM', 'G.SKILL', 'DDR4 2400MHz', 328000, '4GB'),
          HDD('HDD', 'Seagate', 'HDD 2.5 inch', 295000, '1000GB', 7200),
          VGA('VGA', 'Asus', '1060Ti', 250000, '8GB'),
          PSU('PSU', 'Corsair', 'Corsair V550', 250000, '500W')]]

for i, Komputer in enumerate(rakit):
    print("Komputer", i + 1)
    for part in Komputer:
        print(f" {part.nama} {part.jenis} produksi {part.merk} ")
