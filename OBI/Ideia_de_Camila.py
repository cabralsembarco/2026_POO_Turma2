class idade:
    def __init__(self, cibele, camila, celeste):
        self.cibele = cibele
        self.camila = camila
        self.celeste = celeste
    def set_cibele(self, cibele):
        n = int(input())
        if n <= 5 or n >= 100