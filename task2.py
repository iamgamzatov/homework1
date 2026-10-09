contacts = [
    {'name': 'Geektech', 'phone': '0507052018'},
    {'name': 'Служба спасения', 'phone': '911'},
    {'name': 'Пожарная служба', 'phone': '101'},
]

def create(name, phone):
    contacts.append({'name': name, 'phone': phone})
    return contacts

def edit_name(name, phone, new_name, new_phone):
    for contact in contacts:
        if contact['name'] == name and contact['phone'] == phone:
            contact['name'] = new_name
            contact['phone'] = new_phone
            return contacts
    
def delete(name):
    contacts.remove({'name': name, 'phone': '0507052018'})
    return contacts



ten = [i for i in range(1, 11)]

evens = [i for i in ten if i % 2 == 0]
print([i ** 2 for i in evens])

def index_list(list, i):
    if 0 <= i < len(list):
        for j in range(len(list)):
            if j == i:
                return 'Полученное значение: ' + str(list[j])
    else:
        return '\nНет значения по данному индексу'
        
            
while 1:
    print('\nif you exit, press "11"\n')
    input_index = int(input('Enter index: '))
    print()
    if input_index == 11:
        break
    if input_index > 9 or input_index < 0:
        print('\nВведите индекс от 0 до 9')
    print(index_list(ten, input_index))