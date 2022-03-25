# Игра "крестики - нолики"
# автор: Кутепов Сергей
# группа FPW-65

field = [['-']*3 for _ in range(3)]
criss_count=0

def print_field(f):
    print('  0 1 2')
    for i in range(len(field)):
        print(str(i)+' '+' '.join(field[i]))
def user_input(f):
    while True:
        place=input('Введите 2 координаты цифрами через пробел: ').split()
        if len(place)!=2:
            continue
        if not(place[0].isdigit() and place[1].isdigit()):
            continue
        x,y = map(int, place)
        if not(x in [0, 1, 2] and y in [0, 1, 2]):
            continue
        if f[x][y]!='-':
            print('клетка занята')
            continue
        break
    return x,y

def check_win(smb):
    for n in range(3):
        if check_line(field[n][0], field[n][1], field[n][2], smb) or \
        check_line(field[0][n], field[1][n], field[2][n], smb):
            return True
    if check_line(field[0][0], field[1][1], field[2][2], smb) or \
    check_line(field[2][0], field[1][1], field[0][2], smb):
        return True
    else:
        return False

def check_line(a1,a2,a3,smb):
    if a1==smb and a2==smb and a3==smb:
        return True


while True:
    if criss_count%2==0:
        criss='X'
    else:
        criss='0'
    print_field(field)
    x,y=user_input(field)
    field[x][y]=criss
    if check_win(criss):
        print('Выиграл '+criss)
        print_field(field)
        break
    criss_count+=1
    if criss_count>8:
        print('Ничья')
        print_field(field)
        break

