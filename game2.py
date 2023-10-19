from ayoclass import*

a = Ayogame()
p = 0
h = -1

while True:
    a.game_loud(p)
    h = int(input('I choose hole number: '))
    if a.check_illegal(h):
        p = a.round(p, h)
        print('')
        print('')
    else:
        print('Illegal move!')
        print('')
