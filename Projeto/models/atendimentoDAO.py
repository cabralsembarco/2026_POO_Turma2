from models.atendimento import Atendimento
from datetime import datetime as dt
import json

class AtendimentoDAO:
    def __init__(self):
        self.__arquivo = "atendimentos.json"
        self.__objetos = []
        self.__abrir()

    def inserir(self, obj):
