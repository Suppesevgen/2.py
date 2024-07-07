def printParams(a = 1, b = 'строка', c = True):
    print(a, b, c)

#print_params(b = 25) - не работает
# print_params(c = [1,2,3]) - не работает

valuesList = [12,'Строка', True] # - создание списка с тремя элементами разных типов
valuesDict = {'a': 11, 'b' : 22, 'c' : 'строка'} # - создание словаря с тремя ключами
valuesList_2 = [54.32, 'Строка']

#printParams() # - вывод без аргументов
#printParams(1,2) # - вывод с двумя аргументами
#printParams(valuesList) # - вывод со списком
#printParams(*valuesList) # - вывод c распакованным списком
#printParams(**valuesDict) # - вывод с распакованным словарем
printParams(*valuesList_2,42) # - работает