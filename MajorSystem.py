import sqlite3
import pandas as pd
import numpy as np

#----------Definicije------------
def Vnos():
    sl_A = slovar.loc[int(V_st), 'A']
    sl_B = slovar.loc[int(V_st), 'B']
    sl_C = slovar.loc[int(V_st), 'C']
    sl_D = slovar.loc[int(V_st), 'D']
    sl_E = slovar.loc[int(V_st), 'E']
    sl_F = slovar.loc[int(V_st), 'F']
    sl_G = slovar.loc[int(V_st), 'G']
    sl_H = slovar.loc[int(V_st), 'H']

    if sl_A == prazno:
        slovar.loc[int(V_st), 'A'] = V_bes
    elif sl_B == prazno:
        slovar.loc[int(V_st), 'B'] = V_bes
    elif sl_C == prazno:
        slovar.loc[int(V_st), 'C'] = V_bes
    elif sl_D == prazno:
        slovar.loc[int(V_st), 'D'] = V_bes
    elif sl_E == prazno:
        slovar.loc[int(V_st), 'E'] = V_bes
    elif sl_F == prazno:
        slovar.loc[int(V_st), 'F'] = V_bes
    elif sl_G == prazno:
        slovar.loc[int(V_st), 'G'] = V_bes
    elif sl_H == prazno:
        slovar.loc[int(V_st), 'H'] = V_bes
    else:
        print('The dictionary already contains 8 words.')
#----------Podatki---------------
prazno = '----'

print('For help type:     manual')
while True:
    print(' ')
    test = input('What do you want do to? ')
    slovar = pd.read_csv('slovar.csv', names=['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H'])
    if test == 'input':
        while True:
            V_st = input('Input number:       ')
            if V_st != 'stop':
                V_bes = input('Input word: ')
                if V_bes == 'stop':
                    break
                else:
                    Vnos()
                    slovar.to_csv('slovar.csv', header=None)
            else:
                break

    elif test == 'output':
        while True:
            lokacija = input('Pick a number: ')
            if lokacija == 'stop':
                break
            elif int(lokacija) >= 10000:
                print('Too large number! Try again...')
                continue
            else:
                print(' ')
                print('Words for number ', lokacija, ':')
                print(slovar.loc[int(lokacija)])

    elif test == 'reset':
        test_1 = input('Which number do you want to reset? ')

        if test_1 == 'reset all':
            test_2 = input('Do you really wont to reset all? ')
            if test_2 == 'yes':
                N = 1000
                indeks = np.arange(0, N)
                slovar = pd.DataFrame('----', index=indeks, columns=list('ABCDEFGH'))
                slovar.to_csv('slovar.csv')
            else:
                continue

        elif test_1 == 'stop':
            continue

        else:
            slovar.loc[int(test_1)] = prazno
            slovar.to_csv('slovar.csv', header=None)

    elif str(test) == 'exit':
        break

    elif str(test) == 'print':
        print(slovar)

    elif str(test) == 'manual':
        print('-To input a number type:         input')
        print('-To browse for a number type:    output')
        print('-To stop the input/browse type:  stop')
        print('-To reset a dictionary type:     reset')
        print('-To stop the reset type:         stop')
        print('-To reset all type:              reset all')
        print('-To display the dictionary type: print')
        print('-To exit type:                   exit')




