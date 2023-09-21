def bnk():
    amt = 0
    print('Current amount in your account:',amt)
    print('Enter the opertation to be performed:\n\tW]Withdraw\n\tD]Deposit')
    l = 0
    while l <= 1:
        ch = input('Choice:')
        '''print('Old amount:',amt)'''
        if ch == 'W':
            w = int(input('Enter the your amount:\n\tW-'))
            if w >= amt:
                print('Insufficint amount in your account')
                break
            else:
                amt = amt-w
        elif ch == 'D':
            d = int(input('Enter the your amount:\n\tD-'))
            amt = d + amt
        print('New amount:',amt)
        c = input('Do you wish to continue(y/n):')
        if c == 'y':
            continue
        else:
            print('Final amount arter transaction:',amt)
            break

bnk()