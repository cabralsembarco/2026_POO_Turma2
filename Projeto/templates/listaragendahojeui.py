import streamlit as st
import pandas as pd
from service import Service
import time
from datetime import datetime

class ListarAgendaHojeUI:
    def main():
        st.header("Lista de Horários de Clientes")
        tab1 = st.tabs(["Selecionar Cliente"])
        with tab1: ListarAgendaHojeUI.selecionar()

    def selecionar():
    horarios = Service.horario_listar_agenda()
    if len(horarios) == 0: st.write("Nenhum horário cadastrado")
    else:
        dic = []
        for obj in horarios:
            cliente = Service.cliente_listar_id(obj.get_id_cliente())
            servico = Service.servico_listar_id(obj.get_id_servico())
            profissional = Service.profissional_listar_id(obj.get_id_profissional())
            if cliente != None: cliente = cliente.get_nome()
            if servico != None: servico = servico.get_descricao()
            if profissional != None: profissional = profissional.get_nome()
            dic.append({"id" : obj.get_id(), "data" : obj.get_data(), "cliente" : cliente,
            "serviço" : servico, "profissional" : profissional})
        df = pd.DataFrame(dic)
        st.dataframe(df)