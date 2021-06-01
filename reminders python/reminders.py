reminders = []
for line in open('reminders.txt'):
    reminders.append(line)

while True:
    answer = input('What do you want to do? (+, -, c, or s):')
    if answer == '+':
        _input = '-' + input('\tPut the reminder you want to add here: ')
        w = open('reminders.txt', mode='a')
        w.write(f'{_input}\n')
        w.close()
        reminders.append(_input)
        print(f"\tSuccessfully added '{_input}' to reminders.")
    elif answer == '-':
        _type = input('\tDo you want to say the line number of the unwanted reminder, or say the actual reminder? (d/r)')
        if _type == 'r':
            delLine = input('\t\tWrite the line: ')
            newRem = []
            for lin in reminders:
                if lin != '-' + delLine and lin != delLine:
                   newRem.append(reminders[num])
            reminders = newRem
            print('\tSuccessfully removed.')
        elif _type == 'd':
            linNum = int(input('\t\tPick which line: ')) - 1
            newRem = []
            for num in range(len(reminders)):
                if num != linNum:
                   newRem.append(reminders[num])
            reminders = newRem
            print('\tSuccessfully removed.')
    elif answer == 's':
        for elem in reminders:
            print('\t' + elem)
    elif answer == 'c':
        w = open('reminders.txt', mode='w')
        w.write('')
        w.close()
        reminders = []
        print('\tSuccessfully cleared!')