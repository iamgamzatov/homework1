import random

player = {
    'name': '',
    'hp': 100,
    'inventory': [{'Пикуа': 0}, {'Калиниан': 0}, {'Рефрит': 0}, {'Кабула': 0}]
    }
problems = {'Ваши проблемы': ['Генератор, ', "ГБЦ, ", "Стартер"]}
print(problems['Ваши проблемы'])
print('\n=====🎮ДОБРО ПОЖАЛОВАТЬ В ТЕРМИНАЛ ИГРЫ!🎮=====\n')
player['name'] = input('🥷 Введите имя: ').capitalize()
print(f'\nИтак, {player['name']}, вы являетесь пилотом космического корабля🛸\n')
print('К сожалению, ваше судно было подбито и вы высадились на планету Z🌠. \n🚨Здесь много неизученных ресурсов и разных обитателей🧟‍♀️\
      \nВам предстоит изучить мир и починить корабль (реактор), чтобы вернуться на Землю🌍! \n🛑Будьте острожны🛑 и остерегайтесь\
 местных обитателей🫈 ! Удачи вам!🌞\n')

events = [
    {'desc': 'Вас заметили дикие звери!🪬', 'type': 'enemy', 'damage': 20},
    {'desc': 'Перед вами лежит Калиниан!🪬', 'type': 'kalinian', 'name': 'Калиниан'},
    {'desc': 'Вы наткнулись на Рефрит!🪬', 'type': 'ref', 'name': 'Рефрит'},
    {'desc': 'Перед вами растение Кабула!🪬', 'type': 'kabula', 'name': 'Кабула'},
    {'desc': 'Выкапайте землю перед вами! Видны черные следы Пикуи🪬', 'type': 'pikua', 'name': 'Пикуа'} ]


cnt = 0
for step in range(1, 100):
    print("Проблемы: ", *problems['Ваши проблемы'])
    if player['hp'] == 0:
        break
    print(f'\nШаг: {step}')
    print(f'❤️ Health: {player['hp']} || 🎁Inventory: {player['inventory']} || 🧯\
My problems: {len(problems['Ваши проблемы'])}\n')
    choice = random.choice(events)
    if choice['type'] == 'enemy':
        print(choice['desc'])
        print('1. Сражаться?\n2. Убежать?')
        vybor = input()
        if vybor == "1":
            if 'Ефритовый меч' in player['inventory']:
                player['hp'] = player['hp'] - 3
                print(f"Вы сразились с монстром!\nОднако получили урон: 3")
            else:
                player['hp'] = player['hp'] - 6
                print(f'У вас нет орудия, лучше вам убежать! Однако на вас подействовала радиация\nВаше здоровье = {player['hp']}')
        else:
            print('Вы убежали и сохранили здоровье!')
    if choice['type'] == 'kalinian':
        print(f"{choice['desc']}\n1. Взять?\n2. Пройти мимо?")
        vybor = input()
        if vybor == '1':
            print('Вы подобрали: ', choice['name'] )
            player['inventory'][1]['Калиниан'] += 1

    if choice['type'] == 'ref':
        print(f"{choice['desc']}\n1. Взять?\n2. Пройти мимо?")
        vybor = input()
        if vybor == '1':
            print('Вы подобрали: ', choice['name'] )
            player['inventory'][2]['Рефрит'] += 1
    if choice['type'] == 'pikua':
            print(f"{choice['desc']}\n1. Взять?\n2. Пройти мимо?")
            vybor = input()
            if vybor == '1':
                print('Вы подобрали: ', choice['name'] )
                player['inventory'][0]['Пикуа'] += 1
    if choice['type'] == 'kabula':
                print(f"{choice['desc']}\n1. Взять?\n2. Пройти мимо?")
                vybor = input()
                if vybor == '1':
                    print('Вы подобрали: ', choice['name'] )
                    player['inventory'][3]['Кабула'] += 1
    if 'Ефритовый меч' not in player['inventory'] or 'Генератор, ' in problems['Ваши проблемы']:     
        if player['inventory'][0]['Пикуа'] >= 1 and player['inventory'][1]['Калиниан'] >= 1 and player['inventory'][2]['Рефрит'] >= 1:
            print(f'\n❤️ Health: {player['hp']} || 🎁Inventory: {player['inventory']} || 🧯\
    My problems: {len(problems['Ваши проблемы'])}\n')
            print('Вы можете скрести из предметов в инвентаре меч - 1 или\
 сделать статор дле генератора - 2 | Ваш выбор(1?2?)')
            vybor = input('')

            if vybor == '1':
                    if 'Ефритовый меч' not in player['inventory']:
                        player['inventory'].append('Ефритовый меч')
                        print('Вы скрестили: ', player['inventory'])
                        player['inventory'][0]['Пикуа'] -= 1
                        player['inventory'][1]['Калиниан'] -= 1
                        player['inventory'][2]['Рефрит'] -= 1
                    else:
                        print('Меч уже есть! Нyжно потратить ресурсы на починку Генератора')
            else:
                if 'Генератор, ' in problems['Ваши проблемы']:
                    problems['Ваши проблемы'].remove("Генератор, ")
                    player['inventory'][0]['Пикуа'] -= 1
                    player['inventory'][1]['Калиниан'] -= 1
                    player['inventory'][2]['Рефрит'] -= 1
                    print(f'Вы сделали деталь для генератора и починили его! Поздравляю\
 вас!')
                else:
                     print('Генератор уже починен! Вы можете сделать меч!')
    if 'ГБЦ, ' in problems['Ваши проблемы']:
        if player['inventory'][3]['Кабула'] >= 1 and player['inventory'][1]['Калиниан'] >= 2:
                print(f'\n❤️ Health: {player['hp']} || 🎁Inventory: {player['inventory']} || 🧯\
        My problems: {len(problems['Ваши проблемы'])}\n')
                print('Вы можете скрести из них распредвал для ГБЦ - 1 или\
 пройти мимо - 2 | Ваш выбор(1?2?)')
                vybor = input('')
                player['inventory'][3]['Кабула'] -= 1
                player['inventory'][1]['Калиниан'] -= 2
        
                if vybor == '1':
                    problems['Ваши проблемы'].remove("ГБЦ, ")
                    print(f'Вы сделали распредвал для ГБЦ и починили его! Поздравляю\
 вас!')
                else:
                    print('Вы отказалси что-либо делать!')
    if 'Стартер' in problems['Ваши проблемы']:
            if player['inventory'][0]['Пикуа'] >= 1 and player['inventory'][2]['Рефрит'] >= 1:
                    print(f'\n❤️ Health: {player['hp']} || 🎁Inventory: {player['inventory']} || 🧯\
            My problems: {len(problems['Ваши проблемы'])}\n')
                    print('Вы можете скрести из них обмотку для стартера - 1 или\
 пройти мимо - 2 | Ваш выбор(1?2?)')
                    vybor = input('')
                    player['inventory'][0]['Пикуа'] -= 1
                    player['inventory'][2]['Рефрит'] -= 1
            
                    if vybor == '1':
                        problems['Ваши проблемы'].remove("Стартер")
                        print('Вы сделали обмотку для стартера и починили его! Поздравляю\
 вас!')
                    else:
                        print('Вы отказалси что-либо делать!')
    if not(problems['Ваши проблемы']):
        print("\n🎉УРАААА!!!🎉 Все проблемы решены, осталось завести реактор!\n\
 1. Ехали домой!\n 2. Остаться с монстрами")
        home = input()
        if home == '1':
            cnt = 100000000
            
            print('🚨Попытка завести двигатель.................🚨')
            while cnt >= 0:

                cnt -= 1
                if cnt == 100000000 // 3:
                    print('ГГГГГГМММММ....')
                elif cnt == 100000000 // 2:
                    print('ГГГГГГМММММ....')
            
            
            print('\n\n\nДвигатель запущен!🚀\nОтправляемся домой!!!...........🌍\nДа - 1\nНет - 2')
            itog = input('')
            if itog == '1':
                cnt_end = 100000
                while cnt_end >= 0:
                    cnt_end -= 1
                    print('...........................................🚀')
                print('\nThe End\nРеквизиты для доната и поддержки проекта........💎')
                break
            else:
                print('Похожу ещё с монстрами, можест сдружусь, женюсь......')
                 
        else:
            print('Похожу ещё с монстрами, можест сдружусь, женюсь......')