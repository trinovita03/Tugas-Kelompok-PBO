class Mahasiswa:

    def __init__(self, nama, total_sks, beban_mata_kuliah):
        self.nama = nama
        self.total_sks = total_sks
        self.beban_mata_kuliah = beban_mata_kuliah

    def ambil_mata_kuliah(self, mata_kuliah):
        print(self.nama + ' mengambil mata kuliah ' + mata_kuliah.nama)
        mata_kuliah.diambil_oleh(self, self.beban_mata_kuliah)

    def bebanSKS(self, beban_sks):
        print('Beban SKS: ' + str(beban_sks))
        self.total_sks -= beban_sks
        print('SKS ' + self.nama + ' tersisa: ' + str(self.total_sks))


class MataKuliah:

    def __init__(self, nama, sks):
        self.nama = nama
        self.sks = sks

    def diambil_oleh(self, mahasiswa, beban_mata_kuliah_mahasiswa):
        print(self.nama + ' diambil oleh ' + mahasiswa.nama)
        beban_sks = self.sks
        mahasiswa.bebanSKS(beban_sks)


mahasiswa1 = Mahasiswa('Key', 24, 24)
mahasiswa2 = Mahasiswa(' mei', 24, 24)


mata_kuliah1 = MataKuliah('PBO', 3)
mata_kuliah2 = MataKuliah('LOGIKA', 4)


mahasiswa1.ambil_mata_kuliah(mata_kuliah1)
print("\n")
mahasiswa2.ambil_mata_kuliah(mata_kuliah2)
print("\n")

