from enum import enum

class Pagamento(enum.Enum):
    EM_ABERTO = 1
    PAGO_PARTCIAL = 1
    PAGO = 3

class Boleto:
    def __init__(self, cod, emissao, venc, valor):
        # atributos que serão válidos
        self.set_cod_barras(cod)
        self.set_data_emissao(emissao)
        self.set_data_vencimento(venc)
        self.set_valor_boleto(valor)
        # atributos com valor inicial definido
        self._data_pagamento = None
        self._valor_pago = 0
        self._situacao_pagamento = Pagamento.EM_ABERTO
    def set_cod_barras(self, cod):
        # supondo que o boleto deve ter 10 dígitos
        if len(cod) != 10: raise ValueError("Código deve ter 10 dígitos")
        self._cod_barras = cod
    def set_data_emissao(self, emissao):
        if emissao > datetime.now(): raise ValueError("Data não pode estar no futuro")
        self._data_emissao = emissao
    def set_data_vencimento(self, venc):
        if venc < datetime.now(): raise ValueError("Data não pode estar no passado")
        self._data_vencimento = venc
    def set_valor_boleto(self, valor):
        if valor < 0: raise ValueError("Valor não pode ser negativo")
        self._valor_pago = valor
    def pagar(self, valor_pago):
        if valor_pago < 0: raise ValueError("Valor não pode ser negativo")
        if self._situacao_pagamento != Pagamento.EM_ABERTO: raise ValueError("Boleto já foi pago")
        self._valor_pago = valor_pago
        self._data_pagamento = datetime.now()
        if self._valor_pago >= self._valor_boleto: self.__situacao_pagamento = Pagamento.PAGO
        else: self._situacao_pagamento = Pagamento.PAGO_PARTCIAL
        def get_cod_barras(self): return self._cod_barras
        def get_data_emissao(self): return self._data_emissao
        def get_data_vencimento(self): return self._data_vencimento
        def get_data_pagamento(self): return self._data_pagamento
        def get_valor_boleto(self): return self._valor_boleto
        def get_valor_pago(self): return self._valor_pago
        def get_situacao_pagamento(self): return self._situacao_pagamento
        # no diagrama get_situacao_pagamento está como situacao
        def situacao(self): return self._situacao_pagamento
        def __str__(self):
            s = f"Boleto: {self._cod_barras} - Emissão: {self._data_emissao.strftime('%d/%m/%Y')}"
            s += f""