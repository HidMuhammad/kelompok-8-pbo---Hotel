class layanan:

    def __init__(self, id, tarif, tipe):
        self.__id = id
        self.__tarif = tarif
        self.__tipe = tipe

    @property
    def id(self):
        pass
    @id.getter
    def id(self):
        return self.__id
    @id.setter
    def id(self, id):
        self.__id = id

    @property
    def tarif(self):
        pass
    @tarif.getter
    def id(self):
        return self.__tarif
    @tarif.setter
    def tarif(self, tarif):
        self.__tarif = tarif

    @property
    def tipe(self):
        pass
    @tipe.getter
    def tipe(self):
        return self.__tipe
    @tipe.setter
    def tipe(self, tipe):
        self.__tipe = tipe

layanan1 = layanan(10297, 135000, "suite")
print("id layanan :", layanan1.id, "tarif layanan", layanan1.tarif, "tipenya", layanan1.tipe)



