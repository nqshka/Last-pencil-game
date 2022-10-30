def bot(sticks):
    x = 1
    if sticks % 4 == 0:
        x = 3
    elif sticks % 4 == 3:
        x = 2
    print(f"Jack's turn:\n{x}")
    return x

def player(sticks):
    x = input("John's turn:\n")
    while x not in ('1', '2', '3'):
        x = input("Possible values: '1', '2' or '3'\n")
    while sticks - int(x) < 0:
        x = input('Too many pencils were taken\n')
    return int(x)


while True:
    pencils = input('How many pencils would you like to use:\n')
    try:
        pencils = int(pencils)
        if pencils > 0:
            break
        else:
            raise ValueError
    except ValueError:
        print('The number of pencils should be positive' if pencils == 0
              else 'The number of pencils should be numeric')

name = input('Who will be the first (John, Jack):\n')
while name not in ('John', 'Jack'):
    name = input("Choose between 'John' and 'Jack'\n")

while pencils > 0:
    print('|' * pencils)
    pencils -= player(pencils) if name == 'John' else bot(pencils)
    name = 'Jack' if name == 'John' else 'John'
print(name, 'won!')
