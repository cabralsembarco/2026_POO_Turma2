from models.clientes import Cliente
from models.clientesDAO import ClienteDAO
from models.servico import Servico
from models.servicoDAO import ServicoDAO
from models.horario import Horario
from models.horarioDAO import HorarioDAO
from models.profissional import Profissional
from models.profissionalDAO import ProfissionalDAO
from models.endereco import Endereco
from models.enderecoDAO import EnderecoDAO

class Service:
    @staticmethod
    def cliente_inserir(id, nome, email, fone, senha):
        obj = Cliente(id, nome, email, fone, senha)
        ClienteDAO().inserir(obj)
    @staticmethod
    def cliente_listar():
        return ClienteDAO().listar()
    @staticmethod
    def cliente_listar_id(id):
        return ClienteDAO().listar_id(id)
    @staticmethod
    def cliente_atualizar(id, nome, email, fone, senha):
        obj = Cliente(id, nome, email, fone, senha)
        ClienteDAO().atualizar(obj)
    @staticmethod
    def cliente_excluir(id):
        ClienteDAO().excluir(id)
    @staticmethod
    def cliente_criar_admin():
        for c in Service.cliente_listar():
            if c.get_email() == "admin": return
        Service.cliente_listar("admin", "admin", "fone", "1234")
    @staticmethod
    def cliente_autenticar():
        for c in Service.cliente_listar():
            



    @staticmethod
    def servico_inserir(id, descricao, valor):
        obj = Servico(id, descricao, valor)
        ServicoDAO().inserir(obj)
    @staticmethod
    def servico_listar():
        return ServicoDAO().listar()
    @staticmethod
    def servico_listar_id(id):
        return ServicoDAO().listar_id(id)
    @staticmethod
    def servico_atualizar(id, descricao, valor):
        obj = Servico(id, descricao, valor)
        ServicoDAO().atualizar(obj)
    @staticmethod
    def servico_excluir(id):
        ServicoDAO().excluir(id)



    @staticmethod
    def endereco_inserir(id, nome, endereco, id_cliente):
        obj = Endereco(id, nome, endereco, id_cliente)
        EnderecoDAO().inserir(obj)
    @staticmethod
    def endereco_listar():
        EnderecoDAO().listar()
    @staticmethod
    def endereco_listar_id(id):
        EnderecoDAO().listar_id(id)
    @staticmethod
    def endereco_atualizar(id, nome, endereco, id_cliente):
        obj = Endereco(id, nome, endereco, id_cliente)
        EnderecoDAO().inserir(obj)
    @staticmethod
    def endereco_excluir(id):
        EnderecoDAO().excluir(id)
