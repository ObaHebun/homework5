immutable_var = 1, 6, 4, 'Kira', False, 1.5, [3, 5]
print(immutable_var)
  #  immutable_var[3] = 3 - изменить невозможно тк кортежи не поддерживают обращение к конкретному элементу
mutable_list = [1, 7, 8, False, 'Gamer', 4.5]
print(mutable_list)
mutable_list[0] = 1.5
mutable_list.append(44)
mutable_list.extend(['thats it folks'])
mutable_list.remove(8)
print(mutable_list)