from templates.manterclienteui import ManterClienteUI
from templates.manterenderecoui import ManterEnderecoUI
from service import Service
import streamlit as st

class IndexUI:
    def main():
        Service.cliente_criar_admin()
        op = st.sidebar.selectbox("Menu", ["Clientes", "Endereços"])
        if op == "Clientes": ManterClienteUI.main()
        if op == "Endereços": ManterEnderecoUI.main()

IndexUI.main()