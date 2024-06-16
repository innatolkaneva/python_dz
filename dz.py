def show_menu():
    print("\nВыберите необходимое действие:\n"
          "1. Отобразить весь справочник\n"
          "2. Найти абонента по фамилии\n"
          "3. Найти абонента по номеру телефона\n"
          "4. Изменить номер телефон по фамилии\n"
          "5. Удалить по фамилии\n"
          "6. Добавить нового абонента\n"
          "7. Скопировать данные по номеру строки в другой файл\n"
          "8. Завершить работу")
    choice = int(input())
    return choice

def work_with_phonebook():	

    choice=show_menu()

    phone_book=read_txt('phon.txt')

    while (choice!=8):

        if choice==1:
            print_result(phone_book)
        elif choice==2:
            last_name=input('Введите фамилию для поиска:\n').strip().capitalize()
            print(find_by_lastname(phone_book,last_name))
        elif choice==3:
            number=input('Введите номер телефона для поиска:\n').strip()
            print(find_by_number(phone_book,number))       	
        elif choice==4:
            last_name=input('Введите фамилию для поиска:\n').strip().capitalize()
            new_number=input('Введите новый номер абонента:\n').strip()
            print(change_number(phone_book,last_name,new_number))
        elif choice==5:
            lastname=input('Введите фамилию:\n').strip().capitalize()
            print(delete_by_lastname(phone_book,lastname))
        elif choice==6:
            user_data=input('Введите фамилию, имя, номер и описание через пробел:\n')
            print(add_user(phone_book,user_data))
        elif choice==7:
            number_str=int(input('Введите порядковый номер абонента:\n'))
            new_file=input('Введи название файла в который копировать абонента:\n')
            print(copy_data(phone_book, number_str, new_file))
            


        choice=show_menu()

def read_txt(filename): 

    phone_book=[]

    fields=['Фамилия', 'Имя', 'Телефон', 'Описание']
    i = 1
    with open(filename,'r',encoding='utf-8') as phb:

        for line in phb:
           if line != '\n':
            line = line.replace('\n','')
            record = dict(zip(fields, line.split(',')))
            record['Порядковый номер'] = i
            i += 1

	     
            phone_book.append(record)	

    return phone_book

def write_txt(filename , phone_book):
    with open(filename,'w',encoding='utf-8') as phoune:
        for i in range(len(phone_book)):
            s=''
            for v in phone_book[i].values():
                if isinstance(v, str):
                    s = s + v + ','
            phoune.write(f'{s[:-1]}\n')

def print_result(phone_book):
    for line in phone_book: 
        for key, values in line.items():
            print(f'{key} - {values}')
        print('-'*80)

def find_by_lastname(phone_book,last_name):
    for line in phone_book:
        if last_name in line.values():
            man = ''
            for key, values in line.items():
                man += (f'{key} - {values}\n')
            return man
            
    return 'Нет такой фамилии'


def find_by_number(phone_book,number):
    for line in phone_book:
        if number in line.values():
            man = ''
            for key, values in line.items():
                man += (f'{key} - {values}\n')
            return man
            
    return 'Нет такого номера'

def delete_by_lastname(phone_book,lastname):
    for line in phone_book:
        if lastname in line.values():
            phone_book.remove(line)
            print(phone_book)
            write_txt('phon.txt', phone_book)
            #чтобы порядковый номер сохранялся при дальнейшей работе с книгой
            i = 1
            for line in phone_book:
                line['Порядковый номер'] = i
                i += 1
            return f'{lastname} - удален'
    
    return 'Нет такой фамилии'

def change_number(phone_book,last_name,new_number):
    for line in phone_book:
        if last_name in line.values():
            line['Телефон'] = new_number
            write_txt('phon.txt', phone_book)
            man = ''
            for key, values in line.items():
                man += (f'{key} - {values}\n')
            return man           
    return 'Нет такой фамилии'

def add_user(phone_book,user_data):
    last_name, name, number, *discription = user_data.split()
    new_dict = {'Фамилия': last_name, 'Имя': name, 'Телефон': number, 'Описание': ' '.join(discription)}
    phone_book.append(new_dict)
    print(phone_book)
    write_txt('phon.txt', phone_book)
    i = 1
    for line in phone_book:
        line['Порядковый номер'] = i
        i += 1
    return f'{last_name} {name} добавлен в книжку'


def copy_data(phone_book,number_str, new_file):
    with open(new_file+'.txt','w',encoding='utf-8') as phoune:
        for line in phone_book:
            if line['Порядковый номер'] == number_str:
                s = ''
                for v in line.values():
                    if isinstance(v, str):
                        s = s + v + ','
                phoune.write(f'{s[:-1]}\n')
                return f"{line['Фамилия']} {line['Имя']} скопирован"
    
work_with_phonebook()


