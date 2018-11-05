# Criando a tabela
class HashTable():

    def __init__(self, tamanho_tabela):
        self.tamanho_tabela = tamanho_tabela
        self.tabela = [[] for _ in range(tamanho_tabela)]

    def funcao_hashing(self, valor):
        return valor % self.tamanho_tabela

    def inserir(self, chave, valor):
        self.tabela[self.funcao_hashing(chave)].append(valor)

    def tratamento(self, chave):
        print("Foi tratado o elemento de chave: {} e valor: {} ".format(chave, self.tabela[self.funcao_hashing(chave)][0]))
        self.deletar_elemento(chave)

    def deletar_elemento(self, chave):
        if len(self.tabela[self.funcao_hashing(chave)]) > 0:
            self.tabela[self.funcao_hashing(chave)].pop(0)

    def mostrar_tabela(self):
        print(self.tabela)
