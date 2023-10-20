# -*- coding: utf-8 -*-
from tabelaHash import Hash_table

class Aluno:
    def __init__(self, nome, matricula):
        self.nome = nome
        self.matricula = matricula

a1 = Aluno("Maria", 12)
a2 = Aluno("João", 6)
a3 = Aluno("José", 24)
a4 = Aluno("Lucas", 36)
a5 = Aluno("Matheus", 3)
a6 = Aluno("Simão", 7)


hash_table = Hash_table(10)
hash_table.inserir(a1.nome, a1.matricula)
hash_table.inserir(a2.nome, a2.matricula)
hash_table.inserir(a3.nome, a3.matricula)
hash_table.inserir(a4.nome, a4.matricula)
hash_table.inserir(a5.nome, a5.matricula)
hash_table.inserir(a6.nome, a6.matricula)


hash_table.print()
print("-------------")
print( hash_table.buscar("José"))
print( hash_table.buscar("Maria"))
print( hash_table.buscar("Lucas"))
print( hash_table.buscar("Matheus"))

