import random

player = {'name':  '',
            'hp': 100,
            'gold': 0,
            'invertory': []


          }

events = [

      {'desc': 'Вы нашли заброшенный сундук.', 'type': 'chest', 'gold' : 50, 'item': 'Ржавый мечь'},
      {'desc': 'На вас напал дикий кабан', 'type': 'enemy', 'damage': 20, 'gold': 30},
      {'desc': 'Вы встретили продячего торговца', 'type': 'traider', 'cost': 40, 'item': 'Зелье лечения'},
      {'desc': 'Вы попали в ловушку со змеями', 'type': 'trap', 'damage': 15},
      {'desc': 'Вы вышли на дорогу, можете передохнуть', 'type': 'peace', 'hp_restore': 10},
]

print('===ДОБРО ПОЖАЛОВАТЬ В ТЕРМИНАЛ ИГРЫ===')
player['name'] = input('Введите имя: ')
print(f'\n{player['name'].capitalize()}, у вас есть 10 шагов\n')

for step in range(1, 11):
  if player['hp'] <= 0:
    print('Вы погибли от урона...')
    break 
  print(f'---Шаг {step}/10')
  print(f'Здоровье {player['hp']}, Золото {player['gold']}, Инвентарь {player['invertory']}')
  current_event = random.choice(events)

  print(f'событие : {current_event['desc']}')

  if current_event['type'] == 'chest':
    print('1. Открыть сундук')
    print('2. Пройти мимо')
    choice = input('Ваш выбор?(1/2)')

    if choice == '1':
      player['gold'] += current_event['gold']

      if current_event['item'] not in player['inventory']:
        player['inventory'].append(current_event['item'])
      print(f'Вы нашли {current_event['gold']} золота и предмет {current_event['item']}')
      
    else:
      print('Вы решили не рисковать')
  if current_event['type'] == 'enemy':
    print('1. Сражаться - потеря 20 hp, но получу золото')
    print('2. Убежать (50% шанс получить урон)')

    if choice == '1':
      if 'Ржавый меч' in player['inventory']:
        actual_damage = current_event['damage'] // 2
        print('Благодаря мечу вы получили на 50% урона ниже')
      else:
        actual_damage = current_event['damage']

      player['hp'] -= actual_damage
      player['gold'] += current_event['gold']
      print(f'Вы победили дикого кабана!')
    else:
      if random.random()<0.5:
        damage = current_event['damage'] // 2
        player['hp'] -= damage
        print('Вы попытались убежать, но кабан вас укусил')
      else:
        print('Вы убежали без урона')
  elif current_event['type'] == 'traider':
    print(f'1. Купить {current_event['item']} за {current_event['cost']} золото')
    print(f'2. Пройти мимо')
    choice = input('Ваш выбор? (1, 2): ')
    if choice == '1':
      if player['gold'] >= current_event['cost']:
        player['gold'] -= current_event['cost']
        player['inventory'].append(current_event['item'])
        print(f'Вы купили {current_event['item']}')
      else:
        print('У вас недостаточно золота!')
    else:
      print('Вы попрощались с торговцем! он пожелал удачной торговли!')
  elif current_event['type'] == 'trap':
    player['hp'] -= current_event['damage']
    print(f'Вы получили {current_event['damage']} урона от ловушки')
  elif current_event['type'] == 'peace':
    if 'Зелье лечения' in player['inventory']:
      print('У вас есть аптечка, хотите использовать?')
      print('1 - да (100%)\n2 - нет (+10%)')
      choice = input('Ваш выбор? (1, 2): ')

      if choice == '1':
        player['hp'] == 100
        player['inventory'].remove('Зелье лечения')
        print('Вы восстановили здоровье!')
        continue
    player['hp'] = min(100, player['hp'] + current_event['hp_restore'])
    print(f'Вы восстановили силы {current_event['hp_restore']}')


  if player['hp'] <= 0:
    print('Game Over')
  else:
    print('You win')
    print('Финальный счет - ')