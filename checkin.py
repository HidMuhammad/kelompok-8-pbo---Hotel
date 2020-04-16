class Checkin:

    def __init__(self, nama, no_ktp, telp, tipe, tarif, no_reservasi, tgl_checkin, no_kamar, data_tamu, no_checkin):
        self.nama = nama
        self.__ktp = no_ktp
        self.__telp = telp
        self.__tipe = tipe
        self.__tarif = tarif
        self.__noreservasi = no_reservasi
        self.__tglcheckin = tgl_checkin
        self.__nokamar = no_kamar
        self.__datatamu = data_tamu
        self.__nocheckin = no_checkin
    @property
    def nama(self):
        return self.nama
    @property
    def no_ktp(self):
        return self.__ktp
    @property
    def telp(self):
        return self.__telp
    @property
    def tipe(self):
        return self.__tipe
    @property
    def tarif(self):
        return self.__tarif
    @property
    def no_reseverasi(self):
        return self.__noreservasi
    @property
    def no_kamar(self):
        return self.__nokamar

    @property
    def tgl_checkin(self):
        pass

    @tgl_checkin.getter
    def tgl_checkin(self):
        return self.__tglcheckin

    @tgl_checkin.setter
    def tgl_checkin(self, tgl_checkin):
        self.__tglcheckin = tgl_checkin

    @property
    def data_tamu(self):
        pass

    @data_tamu.getter
    def data_tamu(self):
        return self.__datatamu

    @data_tamu.setter
    def data_tamu(self, data_tamu):
        self.__datatamu = data_tamu

    @property
    def no_checkin(self):
        pass
    @no_checkin.getter
    def no_checkin(self):
        return self.__nocheckin
    @no_checkin.setter
    def no_checkin(self, no_checkin):
        self.__nocheckin = no_checkin


customer1 = Checkin("Rizki", 100198201, 6285230189101, "deluxe", 150000, 43, "15 April 2020", 21, "data tamuu", 137)
print("nama customer :", customer1.nama)
print("tgl checkin :", customer1.no_ktp)