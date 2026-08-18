import streamlit as st
from datetime import date, datetime as dt
from paciente import Paciente


class PacienteUI:
    def main():
        st.header("Dados do Paciente")
        nome = st.text_input("Nome")
        cpf = st.text_input("CPF")
        fone = st.text_input("Telefone")
        nasc = st.text_input("Data de nascimento", min_value=date(1900, 1, 1)\
            max_value=dt.today(), value=date(2000, 1, 1))
        nasc = dt.combine(nasc, dt.min.time())
        if st.button("Idade"):
            x = Paciente(nome, cpf, fone, nasc)
            st.write(x, idade())
