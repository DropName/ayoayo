from ayoclass import*

a = Ayogame()

while True:
    print(a.score)
    print('Ход первого игрока:')
    print(a.state[6:][::-1])
    print(a.state[:6])
    
    hole =int(input('Дырка номер: '))
    hole = a.move(hole)
    a.capture(1, hole)
    a.switch()

    print()
    print('=========')
    print()

    print(a.score)
    print('Ход второго игрока:')
    print(a.state[6:][::-1])
    print(a.state[:6])

    
    hole = int(input('Дырка номер: '))
    hole = a.move(hole)
    a.capture(2, hole)
    a.switch()

    print()
    print('=========')
    print()

