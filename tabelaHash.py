class Hash_table:

    def __init__(self,tamanho):
        self.tamanho = tamanho
        self.hash_table = [[] for _ in range(10)]
        self.sub_hash_table =  [[] for _ in range(10)]

    def __hash_str(self, key_str):
        num = 0
        for c in key_str:
            num += ord(c)
        return num

    def hash_code(self, key_str):
        key = self.__hash_str(key_str)
        hash_key = self.hash_key = key % 10
        return hash_key

    def sub_hash_code(self,key_str):
        key = self.__hash_str(key_str)
        hash_key = self.sub_hash_key = key % (self.tamanho // 10)
        return hash_key

    def inserir(self,key,valor):
        indice_1 = self.hash_code(key)
        if self.hash_table[indice_1] is None:
            self.hash_table[indice_1] = [None] * (self.tamanho//10)
        indice_2 =  self.sub_hash_code(key)
        if self.sub_hash_table[indice_2] is None:
            self.sub_hash_table[indice_2] = [None] * (self.tamanho//10)
        self.sub_hash_table[indice_2].append((key,valor))

    def buscar(self,key):
            indice_1 = self.hash_code(key)
            indice_2 = self.sub_hash_code(key)

            if (self.hash_table[indice_1] is not None and self.sub_hash_table[indice_2] is not None):
                for k,v in self.sub_hash_table[indice_2]:
                    if k == key:
                        return v
            return None



    def print(self):
            print("{")
            for i in range(len(self.sub_hash_table)):
                alunos = self.sub_hash_table[i]
                for aluno in alunos:
                    nome,matricula = aluno
                    print(nome + ": " + str(matricula))
            
            print("}")


                    
        