import streamlit as st
import pandas as pd
import time
from service import Service

class ManterServicoUI:
    def main():
        st.header("Cadastro de Serviços")
        tab1, tab2, tab3 = st.tabs([""])