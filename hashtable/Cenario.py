import SimpleHashTable
# usando nossa hash table
# inicializacao da hash table
print("\nmostrando tabela vazia criada *****************************************************")
myHashTable = SimpleHashTable.HashTable(10)

# mostrando objetos instanciados
SimpleHashTable.HashTable.mostrar_tabela(myHashTable)

# instciando dados na nossa hash table
SimpleHashTable.HashTable.inserir(myHashTable, 1, 'ola')
SimpleHashTable.HashTable.inserir(myHashTable, 2, 'turma')
SimpleHashTable.HashTable.inserir(myHashTable, 3, 'essa')
SimpleHashTable.HashTable.inserir(myHashTable, 4, 'funcao')
SimpleHashTable.HashTable.inserir(myHashTable, 5, 'mostra')
SimpleHashTable.HashTable.inserir(myHashTable, 6, 'como')
SimpleHashTable.HashTable.inserir(myHashTable, 7, 'lidar')
SimpleHashTable.HashTable.inserir(myHashTable, 8, 'com')
SimpleHashTable.HashTable.inserir(myHashTable, 9, 'colisão 1')
SimpleHashTable.HashTable.inserir(myHashTable, 9, 'colisão 2')
SimpleHashTable.HashTable.inserir(myHashTable, 9, 'colisão 3')
SimpleHashTable.HashTable.inserir(myHashTable, 10, 'colisao 4')
SimpleHashTable.HashTable.inserir(myHashTable, 100, 'colisao 5')

# mostrando objetos instanciados
print("\nmostrando todos os elementos ******************************************************")
SimpleHashTable.HashTable.mostrar_tabela(myHashTable)

# tratando elemento
print("\ntratando um elemento **************************************************************")
SimpleHashTable.HashTable.tratamento(myHashTable, 10)

# mostrando os objetos apos o tratamento
print("\nmostrando novamente os elementos apos o tratamento ********************************")
SimpleHashTable.HashTable.mostrar_tabela(myHashTable)

# tratando elemento
print("\ntratando um elemento **************************************************************")
SimpleHashTable.HashTable.tratamento(myHashTable, 100)

# mostrando os objetos apos o tratamento
print("\nmostrando novamente os elementos apos o tratamento ********************************")
SimpleHashTable.HashTable.mostrar_tabela(myHashTable)