class reservasi:

    def __init__(self, noreservasi, datatamu, statuspemesanan, datakamar):
        self.__noreservasi = noreservasi
        self.__datatamu = datatamu
        self.__statuspemesanan = statuspemesanan
        self.__datakamar = datakamar
    @property
    def datatamu(self):
        pass
    @property
    def datakamar(self):
        pass
    @property
    def noreservasi(self):
        pass
    @noreservasi.getter
    def noreservasi(self):
        return self.__noreservasi
    @noreservasi.setter
    def noreservasi(self, noreservasi):
        self.__noreservasi = noreservasi

    @property
    def statuspemesanan(self):
        pass
    @statuspemesanan.getter
    def statuspemesanan(self):
        return self.__statuspemesanan
    @statuspemesanan.setter
    def statuspemesanan(self, statuspemesanan):
        self.__statuspemesanan = statuspemesanan

reservasi1 = reservasi(54, "data tamunya", "lunas", "tipenya deluxe")
print("nomor reservasi", reservasi1.noreservasi, "datatamu :", reservasi1.datatamu, "status", reservasi1.statuspemesanan, "tipe kamar :", reservasi1.datakamar)


