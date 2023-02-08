import math
from numpy import random
import numpy
import numpy as np
import random
import matplotlib.pyplot as plt
import xlsxwriter
from os.path import exists
import time
import os

t1 = np.random.randint (17, size = (10))
t2 = np.random.randint (17, size = (10))
t3 = np.random.randint (17 , size = (10))
t4 = np.random.randint (17 , size = (10))
t5 = np.random.randint (17 , size = (10))
t6 = np.random.randint (17 , size = (10))
t7 = np.random.randint (17 , size = (10))
# t8 = np.random.randint (20, size = (10))
# t9 = np.random.randint (20, size = (10))
# t10 = np.random.randint (20 , size = (10))
# t11 = np.random.randint (20 , size = (10))
# t12 = np.random.randint (20 , size = (10))
# t13 = np.random.randint (20 , size = (10))
# t14 = np.random.randint (20 , size = (10))
# t15 = np.random.randint (20 , size = (10))
# t16 = np.random.randint (20 , size = (10))
# t17 = np.random.randint (20 , size = (10))
# t18 = np.random.randint (20 , size = (10))
# t19 = np.random.randint (20 , size = (10))
# t20 = np.random.randint (20 , size = (10))

r1 = random.randint(0,1)
r2 = random.randint(0,1)
r3 = random.randint(0,1)
r4 = random.randint(0,1)
r5 = random.randint(0,1)
e0 = random.randint(-1,1)

def HHO_pop (i):

    file_name_H = 'C:/Users/Naweed/PycharmProjects/IHHO/Initial population/list of initial population.txt'
    for pop in range (i):
        t1 = np.random.randint(15, size=(10))
        t2 = np.random.randint(15, size=(10))
        t3 = np.random.randint(15, size=(10))
        t4 = np.random.randint(15, size=(10))
        t5 = np.random.randint(15, size=(10))
        t6 = np.random.randint(15, size=(10))
        t7 = np.random.randint(15, size=(10))
        q = random.randint(0, 1)
        ms = sum(t3)
        ms2 = sum(t1)
        ms3 = sum(t2)
        target = min(ms, ms2, ms3)

        if target == ms:
            target = t3
        elif target == ms2:
            target = t1
        else:
            target = t2

        lb = 0
        ub = random.randint(1,4)
        total_tasks = [t3 , t2 ,t1]
        n = len(total_tasks)
        xm = np.floor(t4 / n)

        if q >= 0.5:
            initial_pop =(list(set(t3) - set(r1 * t2) - set(2*r2*t1))) + (list(set(r1 * t2) - set(t3) - set(2*r2*t1))) + (list(set(2*r2*t1) - set(r1 * t2) - set(t3)))
            len_init = len(initial_pop)
            # initial_pop = np.array(initial_pop)

            with open(file_name_H, 'a') as f:
                f.write('New Task if (q>0.5) :')
                f.write(str(initial_pop))
                f.write(' -> size =')
                f.write(str(len_init))
                f.write('\n-------------------------------------------------------------------')
                f.write('\n')


        else:
           a = (list(set(target) - set(xm)))
           b = r3 * (lb + r4 * (ub-lb))
           init_pop2 = abs(np.subtract(a, b))
           init_pop2 = list(init_pop2)
           len_init2 = len(init_pop2)

           with open (file_name_H, 'a') as f :
               f.write('New Task if (q<0.5) :')
               f.write(str(init_pop2))
               f.write(' -> size =')
               f.write(str(len_init2))
               f.write('\n-------------------------------------------------------------------')
               f.write('\n')


def Pop():
    try :
        file_P = 'C:/Users/Naweed/PycharmProjects/IHHO/Cuckoo/Cuckoo popualation.txt'
        file_P2 = 'C:/Users/Naweed/PycharmProjects/IHHO/Cuckoo/Cuckoo popualation.txt'
        file_P3 = 'C:/Users/Naweed/PycharmProjects/IHHO/Initial population/list of initial population.txt'
        with open (file_P3 , 'r') as f :
            print('                        \nHHO & IHHO :')
            print('\n',f.read())
            print('***********************************************************')
        with open(file_P, 'r') as f:
            print('                        \nCuckoo :')
            print('\n',f.read())


    except (FileNotFoundError) :
        print('*********************************')
        print('* no population generated yet ! *')
        print('*********************************')

def HHO(x=str, y=str):
    file_ph = 'C:/Users/Naweed/PycharmProjects/IHHO/HHO Solution/HHO Solution.txt'
    loip = np.array(x)
    loip2 = np.array(y)
    try:
        if len(loip) != len(loip2):
            print('-------------------------------------')
            print('*** Warning ***\n Arrays size must be equal\nfor a better IHHO performace!!!\n')
            print('-------------------------------------')
    except ValueError:
        print('Arrays size must be equal !!!')
    r = random.randint(0, 1)
    ms = sum(loip)
    ms2 = sum(loip2)
    tasks = [t1,t2,t3,t4,t5,t6,t7]
    total_tasks = len(tasks)
    t = random.randint (1,7)
    e = (2 * e0) * (1-(t/total_tasks))
    j = 2 * (1-r5)
    lb = 0
    ub = random.randint(1, 4)

    if ms > ms2 :
        makespan = loip2

        if r > 0.5 and e > 0.5:

            if len(makespan) and len(loip) == 7 or 8 or 9 or 10 or 11 or 12 or 13 or 14 or 15 or 16 or 17 or 18 or 19 or 20 or 21 or 22:
                segmention = np.array_split (makespan,(2,3))
                segmention2 = np.array_split(loip,(2,3))
                print('makespan segmention:' , segmention)
                print('Task segmention:' , segmention2)
                if j >= 2:
                    if sum(segmention2[2]) > sum(segmention[2]):
                        sub = np.subtract(segmention2[2], segmention[2])
                        segmention2[2] = segmention2[2] - sub
                        soft_besiege = list(segmention2[0]) + list(segmention2[1]) + list(segmention2[2])
                        soft_besiege = list(soft_besiege)
                        print('\n------------------------------')
                        print('*1st displacement*\n after soft besiege:',soft_besiege,'-->','new makespan of Task:',sum(soft_besiege))
                        # print('\n------------------------------')
                    if sum(segmention2[0]) > sum(segmention[0]):
                        sub = np.subtract(segmention2[0], segmention[0])
                        segmention2[0] = segmention2[0] - sub
                        print('our segmention is:', segmention2)
                        soft_besiege = list(segmention2[0]) + list(segmention2[1]) + list(segmention2[2])
                        soft_besiege = list(soft_besiege)
                        print('\n------------------------------')
                        print('*Final displacement*\n after soft besiege:', soft_besiege, '-->','new makespan of Task:',sum(soft_besiege))

                        with open (file_ph,'a') as f:
                            soft_besiege = str(soft_besiege)
                            f.write('\n')
                            f.write('Soft , j >=2 :')
                            f.write(soft_besiege)
                            # f.write('\n')
                            f.write('\n-----------------------------------------')
                else:
                    loip=list(loip)
                    print(' if j=0:',loip)

                    with open(file_ph, 'a') as f:
                        loip = list(loip)
                        # loip = str(loip)
                        f.write('\n')
                        f.write('Soft , j = 0 :')
                        f.write(str(loip))
                        f.write('\n-----------------------------------------')
    else:


        if r >= 0.5 and e >= 0.5:
            makespan = loip

            # print('\n------------------------------')
            if len(makespan) and len(loip2) == 7 or 8 or 9 or 10 or 11 or 12 or 13 or 14 or 15 or 16 or 17 or 18 or 19 or 20 or 21 or 22:
                segmention = np.array_split(makespan, (2, 3))
                segmention2 = np.array_split(loip2, (2, 3))
                print('makespan segmention:', segmention)
                print('Task segmention:', segmention2)

                if j >= 2:
                    if sum(segmention2[2]) > sum(segmention[2]):
                        sub = np.subtract (segmention2[2], segmention[2])
                        segmention2[2] = segmention2[2] - sub
                        soft_besiege = list(segmention2[0]) + list(segmention2[1]) + list(segmention2[2])
                        soft_besiege = list(soft_besiege)
                        print('\n------------------------------')
                        print('*1st displacement*\n after soft besiege:',soft_besiege,'-->','new makespan of Task:',sum(soft_besiege))

                    if sum(segmention2[0]) > sum(segmention[0]):
                        sub = np.subtract(segmention2[0], segmention[0])
                        segmention2[0] = segmention2[0] - sub
                        soft_besiege = list(segmention2[0]) + list(segmention2[1]) + list(segmention2[2])
                        soft_besiege = list(soft_besiege)
                        print('\n------------------------------')
                        print('*Final displacement*\n after soft besiege:',soft_besiege,'-->','new makespan of Task:',sum(soft_besiege))

                        with open (file_ph,'a') as f:
                            soft_besiege = str(soft_besiege)
                            f.write('\n')
                            f.write('Soft , j >=2 :')
                            f.write(soft_besiege)
                            # f.write('\n')
                            f.write('\n-----------------------------------------')
                else:
                    loip2=list(loip2)
                    print(' if j=0:',loip2)

                    with open(file_ph, 'a') as f:

                        f.write('\n')
                        f.write('Soft , j = 0 :')
                        f.write(str(loip2))
                        # f.write('\n')
                        f.write('\n-----------------------------------------')

            elif len(makespan) and len(loip2) == 4 or 5 or 6:
                if j >= 2:
                    if ms2 > ms:
                        makespan =loip
                        segmention = np.array_split(makespan, (1, 2))
                        segmention2 = np.array_split(loip2, (2, 3))
                        print('makespan segmention:', segmention)
                        print('Task segmention:', segmention2)
                    if sum(segmention2[2]) > sum(segmention[2]):
                        sub = np.subtract(segmention2[2], segmention[2])
                        segmention2[2] = segmention2[2] - sub
                        soft_besiege = list(segmention2[0]) + list(segmention2[1]) + list(segmention2[2])
                        soft_besiege = list(soft_besiege)

                        with open (file_ph,'a') as f:
                            soft_besiege = str(soft_besiege)
                            f.write('\n')
                            f.write('Soft , j >=2 :')
                            f.write(soft_besiege)
                            f.write('\n')
                            f.write('\n-----------------------------------------')
                else:
                    loip2=list(loip2)
                    print(' if j=0:',loip2)

                    with open(file_ph, 'a') as f:

                        f.write('\n')
                        f.write('Soft , j = 0 :')
                        f.write(str(loip2))
                        # f.write('\n')
                        f.write('\n-----------------------------------------')

            elif len(makespan) and len(loip2) == 4 or 5 or 6:
                if j >= 2:
                    if ms > ms2:
                        makespan = loip2
                        segmention = np.array_split(makespan, (1, 2))
                        segmention2 = np.array_split(loip, (2, 3))
                        print('makespan segmention:', segmention)
                        print('Task segmention:', segmention2)
                    if sum(segmention2[2]) > sum(segmention[2]):
                        sub = np.subtract(segmention2[2], segmention[2])
                        segmention2[2] = segmention2[2] - sub
                        soft_besiege = list(segmention2[0]) + list(segmention2[1]) + list(segmention2[2])
                        soft_besiege = list(soft_besiege)

                        with open (file_ph,'a') as f:
                            soft_besiege = str(soft_besiege)
                            f.write('\n')
                            f.write('Soft , j >=2 :')
                            f.write(soft_besiege)
                            # f.write('\n')
                            f.write('\n-----------------------------------------')
                else:
                    loip=list(loip)
                    print(' if j=0:',loip)

                    with open(file_ph, 'a') as f:

                        f.write('\n')
                        f.write('Soft , j >=2 :')
                        f.write(str(loip))
                        # f.write('\n')
                        f.write('\n-----------------------------------------')

    if ms > ms2:
        if r >=0.5 and e<0.5 :
            makespan = loip2
            delta_x = np.setdiff1d(makespan,loip)
            delta_x2= np.setdiff1d(loip,makespan)
            delta_x3=np.append(delta_x,delta_x2)
            hard_besiege = np.setdiff1d(makespan,(e*delta_x3))
            len_arr = len(loip2)
            hard_besiege = np.resize(hard_besiege, len_arr)
            hard_besiege = list(hard_besiege)
            print('after hard besiege:',hard_besiege,'new makespan is:',sum(hard_besiege))

            with open(file_ph, 'a') as f:
                hard_besiege = str(hard_besiege)
                f.write('\n')
                f.write('Hard :')
                f.write(hard_besiege)
                # f.write('\n')
                f.write('\n-----------------------------------------')
    else:
        makespan = loip
        if r >= 0.5 and e < 0.5:
            makespan = loip
            delta_x = np.setdiff1d(makespan,loip2)
            delta_x2 = np.setdiff1d(loip2, makespan)
            delta_x3 = np.append(delta_x, delta_x2)
            hard_besiege = np.setdiff1d(makespan, (e * delta_x3))
            len_arr = len(loip2)
            hard_besiege = np.resize(hard_besiege,len_arr)
            hard_besiege = list(hard_besiege)
            print('after hard besiege:', hard_besiege, 'new makespan is:', sum(hard_besiege))

            with open(file_ph, 'a') as f:
                hard_besiege = str(hard_besiege)
                f.write('\n')
                f.write('Hard :')
                f.write(hard_besiege)
                # f.write('\n')
                f.write('\n-----------------------------------------')

    if ms > ms2:

        makespan = loip2
        print('makespan is :', makespan, '-->', 'makespan of it :', sum(makespan))
        print('Task is :', loip, '-->', 'makespan of Task is :', sum(loip))
        print('\n------------------------------')
        if r < 0.5 and e >=0.5:
                makespan = loip2
                j = 2 * (1 - r5)
                # levy_flight
                # d = random.randint(0,1)
                # s=1*d
                # beta = 1.5
                # sigma = (math.gamma(1 + beta) * math.sin(math.pi * beta / 2) / (
                #             math.gamma((1 + beta) / 2) * beta * 2 ** ((beta - 1) / 2))) ** (1 / beta)
                # u = 0.01 * numpy.random.randn(d) * sigma
                # v = numpy.random.randn(d)
                # zz = numpy.power(numpy.absolute(v), (1 / beta))
                # levy_f = numpy.divide(u, zz)

                Y = np.setdiff1d(makespan,(e*j*makespan))
                Y = np.setdiff1d(Y,loip)
                Y2 = np.setdiff1d(loip,Y)
                Y3 = np.append(Y,Y2)
                len_arr = len(loip)
                Y3 = np.resize(Y3,len_arr)
                Y3 = list(Y3)
                print('after soft besiege with rapid dives :', Y3, 'new makespan is :', sum(Y3))

                with open(file_ph, 'a') as f:
                    Y3 = str(Y3)
                    f.write('\n')
                    f.write('Soft rapid :')
                    f.write(Y3)
                    # f.write('\n')
                    f.write('\n-----------------------------------------')
                # Z = Y2 * s * levy_f

    else:
        makespan = loip
        print('makespan is :', makespan, '-->', 'makespan of it :', sum(makespan))
        print('Task is :', loip2, '-->', 'makespan of Task is :', sum(loip2))
        print('\n------------------------------')
        if r < 0.5 and e >=0.5:
            makespan = loip

            # # levy_flight
            # d = random.randint(0, 1)
            # s = 1 * d
            # beta = 1.5
            # sigma = (math.gamma(1 + beta) * math.sin(math.pi * beta / 2) / (
            #         math.gamma((1 + beta) / 2) * beta * 2 ** ((beta - 1) / 2))) ** (1 / beta)
            # u = 0.01 * numpy.random.randn(d) * sigma
            # v = numpy.random.randn(d)
            # zz = numpy.power(numpy.absolute(v), (1 / beta))
            # levy_f = numpy.divide(u, zz)

            Y = np.setdiff1d(makespan, (e * j * makespan))
            Y = np.setdiff1d(Y, loip2)
            Y2 = np.setdiff1d(loip2, Y)
            Y3 = np.append(Y, Y2)
            len_arr = len(loip)
            Y3 = np.resize(Y3, len_arr)
            Y3 = np.resize(Y3,len_arr)
            Y3 = list(Y3)
            print('after soft besiege with rapid dives :', Y3, 'new makespan is :', sum(Y3))

            with open(file_ph, 'a') as f:
                Y3 = str(Y3)
                f.write('\n')
                f.write('Soft rapid :')
                f.write(Y3)
                # f.write('\n')
                f.write('\n-----------------------------------------')

            # Z = Y2 * s * levy_f


    if ms > ms2:
        j = 2 * (1 - r5)
        total_tasks = [loip,loip2]
        n = len(total_tasks)
        loip = np.array(loip)
        xm = np.floor(loip / n)
        makespan = loip2
        print('makespan is :', makespan, '-->', 'makespan of it :', sum(makespan))
        print('Task is :', loip, '-->', 'makespan of Task is :', sum(loip))
        print('\n------------------------------')
        if r < 0.5 and e < 0.5 :
            hbrd = np.setdiff1d( (e*j*makespan),xm)
            hbrd2 = np.setdiff1d (makespan,hbrd)
            hbrd2 = list(hbrd2)
            print('after hard besiege with rapid dives :', hbrd2, 'new makespan is :', sum(hbrd2))

            with open(file_ph, 'a') as f:
                hbrd2 = str(hbrd2)
                f.write('\n')
                f.write('Hard rapid :')
                f.write(hbrd2)
                # f.write('\n')
                f.write('\n-----------------------------------------')
    else:
        j = 2 * (1 - r5)
        total_tasks = [loip, loip2]
        n = len(total_tasks)
        loip2 = np.array(loip2)
        xm = np.floor(loip2 / n)
        makespan = loip
        print('makespan is :', makespan, '-->', 'makespan of it :', sum(makespan))
        print('Task is :', loip2, '-->', 'makespan of Task is :', sum(loip2))
        print('\n------------------------------')

        if r < 0.5 and e < 0.5:
            hbrd = np.setdiff1d((e * j * makespan), xm)
            hbrd2 = np.setdiff1d(makespan, hbrd)
            hbrd2 = list(hbrd2)
            print('after hard besiege with rapid dives :',hbrd2 ,'new makespan is :',sum(hbrd2))

            with open(file_ph, 'a') as f:
                hbrd2 = str(hbrd2)
                f.write('\n')
                f.write('Hard rapid :')
                f.write(hbrd2)
                # f.write('\n')
                f.write('\n-----------------------------------------')

def Genetic ():
    fn_fm = 'C:/Users/Naweed/PycharmProjects/IHHO/Genetic/Genetic Solutions.txt'
    t1 = np.random.randint(15, size=(10))
    t2 = np.random.randint(15, size=(10))
    pop1 = t1
    pop2 = t2
    Roulet_wheel = random.randint(0, 1)
    if Roulet_wheel == 0 :
        time.sleep(0.3)
        print('--> Cross',end='')
        time.sleep(0.3)
        print(' Over',end='')
        time.sleep(0.3)
        print(' .',end='')
        time.sleep(0.3)
        print('.', end='')
        time.sleep(0.3)
        print('.\n', end='')
        if sum(pop1)>sum(pop2) :
            makespan = pop2
            segmention = np.array_split(makespan, (2, random.randint(4,7)))
            segmention2 = np.array_split(pop1, (2, random.randint(4,7)))
            print('makespan segmention:' , segmention)
            print('Task segmention:' , segmention2)
            print('\n----------------------------------------------')
            print('* Makespan is :', makespan, 'Makespan :', sum(makespan))
            print('* Task is :', pop1, 'Makespan is :', sum(pop1))
            segmention2[0] = segmention[0]
            segmention2[2] = segmention[2]
            solution = list(segmention2[0]) + list(segmention2[1]) + list(segmention2[2])
            solution = list(solution)
            makespan = list(makespan)
            print('* New Task is :', list(solution), 'New Makespan is :', sum(solution))
            print('\n----------------------------------------------')

            with open(fn_fm, 'a') as f:
                f.write('\n')
                f.write('Cross Over :')
                f.write(str(solution))
                # f.write('\n')
                f.write('\n-----------------------------------------')
        else :
            makespan = pop1
            segmention = np.array_split(makespan, (2, random.randint(4,7)))
            segmention2 = np.array_split(pop2, (2,random.randint(4,7)))
            pop2 = list(pop2)
            print('\n----------------------------------------------')
            print('* Makespan is :', makespan, 'Makespan :', sum(makespan))
            print('* Task is :', pop2, 'Makespan is :', sum(pop2))
            makespan = list(makespan)
            segmention2[0] = segmention[0]
            segmention2[2] = segmention[2]
            solution = list(segmention2[0]) + list(segmention2[1]) + list(segmention2[2])
            solution = list(solution)
            print('* New Task is :', list(solution), 'New Makespan is :', sum(solution))
            print('\n----------------------------------------------')

            with open(fn_fm, 'a') as f:
                f.write('\n')
                f.write('Cross Over :')
                f.write(str(solution))
                # f.write('\n')
                f.write('\n-----------------------------------------')
    else :
        time.sleep(0.3)
        print('--> Muta', end='')
        time.sleep(0.3)
        print('tion',end='')
        time.sleep(0.3)
        print(' .', end='')
        time.sleep(0.3)
        print('.', end='')
        time.sleep(0.3)
        print('.\n', end='')
        if sum(pop1) > sum(pop2):
            makespan = pop2
            segmention = np.array_split(makespan, (2, random.randint(4, 7)))
            segmention2 = np.array_split(pop1, (2, random.randint(4, 7)))
            print('makespan segmention:', segmention)
            print('Task segmention:', segmention2)
            print('\n----------------------------------------------')
            print('* Makespan is :', makespan, 'Makespan :', sum(makespan))
            print('* Task is :', pop1, 'Makespan is :', sum(pop2))
            segmention2[random.randrange(0,2)][random.randrange(0,2)] = segmention[random.randrange(0,2)][random.randrange(0,1)]
            segmention2[random.randrange(0,1)][random.randrange(0,2)] = segmention[random.randrange(0,2)][random.randrange(0,1)]
            solution = list(segmention2[0]) + list(segmention2[1]) + list(segmention2[2])
            solution = list(solution)
            print('* New Task is :', list(solution), 'New Makespan is :', sum(solution))
            print('\n----------------------------------------------')

            with open(fn_fm, 'a') as f:
                f.write('\n')
                f.write('Mutation :')
                f.write(str(solution))
                # f.write('\n')
                f.write('\n-----------------------------------------')

        else :
            makespan = pop1
            segmention = np.array_split(makespan, (2, random.randint(4, 7)))
            segmention2 = np.array_split(pop2, (2, random.randint(4, 7)))
            print('makespan segmention:', segmention)
            print('Task segmention:', segmention2)
            print('\n----------------------------------------------')
            print('* Makespan is :', makespan, 'Makespan :', sum(makespan))
            print('* Task is :', pop2, 'Makespan is :', sum(pop2))
            segmention2[random.randrange(0, 2)][random.randrange(0, 1)] = segmention[random.randrange(0, 1)][
                random.randrange(0, 3)]
            segmention2[random.randrange(0, 1)][random.randrange(0, 1)] = segmention[random.randrange(0, 2)][
                random.randrange(0, 2)]
            solution = list(segmention2[0]) + list(segmention2[1]) + list(segmention2[2])
            solution = list(solution)
            print('* New Task is :', list(solution), 'New Makespan is :', sum(solution))
            print('\n----------------------------------------------')

        with open(fn_fm, 'a') as f:
            f.write('\n')
            f.write('Mutation :')
            f.write(str(solution))
            # f.write('\n')
            f.write('\n-----------------------------------------')

def Cuckoo_genetic ():
    fn_fn = 'C:/Users/Naweed/PycharmProjects/IHHO/Cuckoo Genetic/Cuckoo Genetic.txt'
    t1 = np.random.randint(13, size=(10))
    t2 = np.random.randint(13, size=(10))
    t3 = np.random.randint(13, size=(10))
    pop1 = t1
    pop2 = t2
    pop3 = t3
    Roulet_wheel = random.randint(0, 1)
    tasks = [t1, t2, t3, t4, t5, t6, t7]
    total_tasks = len(tasks)
    t = random.randint(1, 7)
    Var_high_Task = random.randint(5, 10)
    Var_Low_Task = 0
    MRN = np.floor(t / total_tasks) * (Var_high_Task - Var_Low_Task)
    MRN = np.sum(MRN)
    if Roulet_wheel == 0 :
        time.sleep(0.3)
        print('--> Cross',end='')
        time.sleep(0.3)
        print(' Over',end='')
        time.sleep(0.3)
        print(' .',end='')
        time.sleep(0.3)
        print('.', end='')
        time.sleep(0.3)
        print('.\n', end='')
        if sum(pop1)>sum(pop2) :
            makespan = pop2
            segmention = np.array_split(makespan, (2, random.randint(4,7)))
            segmention2 = np.array_split(pop1, (2, random.randint(4,7)))
            segmention2[0] = segmention[0]
            segmention2[2] = segmention[2]
            solution = list(segmention2[0]) + list(segmention2[1]) + list(segmention2[2])
            solution = list(solution)
            segmention = np.array_split(makespan, (2, random.randint(4, 7)))
            segmention2 = np.array_split(pop3, (2, random.randint(4, 7)))
            segmention2[0] = segmention[0]
            segmention2[2] = segmention[2]
            solution2 = list(segmention2[0]) + list(segmention2[1]) + list(segmention2[2])
            solution2 = list(solution2)
            makespan2 = list(makespan)
            loip = np.array(solution)
            loip2 = np.array(solution2)
            if len(loip) == len(loip2) :
                ms = sum (loip)
                ms2 = sum(loip2)
                if ms > ms2:
                    makespan = loip2
                    if (MRN) > 0:
                        print('               * Imigration is possible *')
                        print('\n')
                        segmention = np.array_split(makespan, (2, 3))
                        segmention2 = np.array_split(loip, (2, 3))
                        print('makespan segmention:', segmention)
                        print('Task segmention:', segmention2)

                        if sum(segmention2[2]) > sum(segmention[2]):
                            sub = np.subtract(segmention2[2], segmention[2])
                            segmention2[2] = segmention2[2] - sub
                            imigration = list(segmention2[0]) + list(segmention2[1]) + list(segmention2[2])
                            imigration = list(imigration)
                            imigration[len(imigration) - 1] = loip2[len(loip) - 1]
                            print('\n------------------------------')
                            print('*1st displacement*\n ', imigration, '-->', 'new makespan of Task:',
                                  sum(imigration))
                            # print('\n------------------------------')
                        if sum(segmention2[0]) > sum(segmention[0]):
                            sub = np.subtract(segmention2[0], segmention[0])
                            segmention2[0] = segmention2[0] - sub
                            print('our segmention is:', segmention2)
                            imigration = list(segmention2[0]) + list(segmention2[1]) + list(segmention2[2])
                            imigration = list(imigration)
                            imigration[len(imigration) - 1] = loip[len(loip) - 1]
                            print('\n------------------------------')
                            print('*Final displacement*\n ', imigration, '-->', 'new makespan of Task:',
                                  sum(imigration))
                            with open(fn_fn, 'a') as f:
                                imigration = str(imigration)
                                f.write('\n')
                                f.write('Imigration :')
                                f.write(imigration)
                                # f.write('\n')
                                f.write('\n-----------------------------------------')
                    else:
                        print('               * No need to imigrate *')
                        print('\n')
                        time.sleep(0.5)
                        print('Sorting Population', end='')
                        time.sleep(0.3)
                        print(' .', end='')
                        time.sleep(0.3)
                        print('.', end='')
                        time.sleep(0.3)
                        print('.')
                        time.sleep(0.1)
                        time.sleep(0.5)
                        print('Removing worst Fitnesses', end='')
                        time.sleep(0.3)
                        print(' .', end='')
                        time.sleep(0.3)
                        print('.', end='')
                        time.sleep(0.3)
                        print('.')
                        time.sleep(0.3)
                        print('\nDone !')
                        loip = list(loip)
                        print('No MRN : ,', loip)

                        with open(fn_fn, 'a') as f:

                            f.write('\n')
                            f.write('No imigration :')
                            f.write(str(loip))
                            # f.write('\n')
                            f.write('\n-----------------------------------------')

                elif ms2 > ms:
                    makespan = loip
                    if (MRN) > 0:
                        print('               * Imigration is possible *')
                        print('\n')
                        segmention = np.array_split(makespan, (2, 3))
                        segmention2 = np.array_split(loip2, (2, 3))
                        print('makespan segmention:', segmention)
                        print('Task segmention:', segmention2)

                        if sum(segmention2[2]) > sum(segmention[2]):
                            sub = np.subtract(segmention2[2], segmention[2])
                            segmention2[2] = segmention2[2] - sub
                            imigration = list(segmention2[0]) + list(segmention2[1]) + list(segmention2[2])
                            imigration = list(imigration)
                            imigration[len(imigration) - 1] = loip2[len(loip) - 1]
                            print('\n------------------------------')
                            print('*1st displacement*\n ', imigration, '-->', 'new makespan of Task:',
                                  sum(imigration))

                        if sum(segmention2[0]) > sum(segmention[0]):
                            sub = np.subtract(segmention2[0], segmention[0])
                            segmention2[0] = segmention2[0] - sub
                            imigration = list(segmention2[0]) + list(segmention2[1]) + list(segmention2[2])
                            imigration = list(imigration)
                            imigration[len(imigration) - 1] = loip2[len(loip) - 1]
                            print('\n------------------------------')
                            print('*Final displacement*\n ', imigration, '-->', 'new makespan of Task:',
                                  sum(imigration))
                            with open(fn_fn, 'a') as f:
                                imigration = str(imigration)
                                f.write('\n')
                                f.write('Imigration :')
                                f.write(imigration)
                                # f.write('\n')
                                f.write('\n-----------------------------------------')
                    else:
                        print('               * No need to imigrate *')
                        print('\n')
                        time.sleep(0.5)
                        print('Sorting Population', end='')
                        time.sleep(0.3)
                        print(' .', end='')
                        time.sleep(0.3)
                        print('.', end='')
                        time.sleep(0.3)
                        print('.')
                        time.sleep(0.1)
                        time.sleep(0.5)
                        print('Removing worst Fitnesses', end='')
                        time.sleep(0.3)
                        print(' .', end='')
                        time.sleep(0.3)
                        print('.', end='')
                        time.sleep(0.3)
                        print('.')
                        time.sleep(0.3)
                        print('\nDone !')
                        loip2 = list(loip2)
                        print('No MRN ,', loip2)

                        with open(fn_fn, 'a') as f:

                            f.write('\n')
                            f.write('No imigration :')
                            f.write(str(loip2))
                            # f.write('\n')
                            f.write('\n-----------------------------------------')
            else :
                print('               * No need to imigrate *')
                print('\n')
                time.sleep(0.5)
                print('Sorting Population', end='')
                time.sleep(0.3)
                print(' .', end='')
                time.sleep(0.3)
                print('.', end='')
                time.sleep(0.3)
                print('.')
                time.sleep(0.1)
                time.sleep(0.5)
                print('Removing worst Fitnesses', end='')
                time.sleep(0.3)
                print(' .', end='')
                time.sleep(0.3)
                print('.', end='')
                time.sleep(0.3)
                print('.')
                time.sleep(0.3)
                print('\nDone !')
                loip2 = list(loip2)
                print('No MRN ,', loip2)

                with open(fn_fn, 'a') as f:

                    f.write('\n')
                    f.write('No imigration :')
                    f.write(str(loip2))
                    # f.write('\n')
                    f.write('\n-----------------------------------------')
        else :
            makespan = pop1
            segmention = np.array_split(makespan, (2, random.randint(4,7)))
            segmention2 = np.array_split(pop2, (2,random.randint(4,7)))
            pop2 = list(pop2)
            makespan = list(makespan)
            segmention2[0] = segmention[0]
            segmention2[2] = segmention[2]
            solution = list(segmention2[0]) + list(segmention2[1]) + list(segmention2[2])
            solution = list(solution)
            segmention = np.array_split(makespan, (2, random.randint(4, 7)))
            segmention2 = np.array_split(pop3, (2, random.randint(4, 7)))
            segmention2[0] = segmention[0]
            segmention2[2] = segmention[2]
            solution2 = list(segmention2[0]) + list(segmention2[1]) + list(segmention2[2])
            solution2 = list(solution2)
            loip = np.array(solution)
            loip2 = np.array(solution2)
            if len(loip) == len(loip2) :
                ms = sum(loip)
                ms2 =sum(loip2)
                if ms > ms2:
                    makespan = loip2
                    if (MRN) > 0:
                        print('               * Imigration is possible *')
                        print('\n')
                        segmention = np.array_split(makespan, (2, 3))
                        segmention2 = np.array_split(loip, (2, 3))
                        print('makespan segmention:', segmention)
                        print('Task segmention:', segmention2)

                        if sum(segmention2[2]) > sum(segmention[2]):
                            sub = np.subtract(segmention2[2], segmention[2])
                            segmention2[2] = segmention2[2] - sub
                            imigration = list(segmention2[0]) + list(segmention2[1]) + list(segmention2[2])
                            imigration = list(imigration)
                            imigration[len(imigration) - 1] = loip2[len(loip) - 1]
                            print('\n------------------------------')
                            print('*1st displacement*\n ', imigration, '-->', 'new makespan of Task:',
                                  sum(imigration))
                            # print('\n------------------------------')
                        if sum(segmention2[0]) > sum(segmention[0]):
                            sub = np.subtract(segmention2[0], segmention[0])
                            segmention2[0] = segmention2[0] - sub
                            print('our segmention is:', segmention2)
                            imigration = list(segmention2[0]) + list(segmention2[1]) + list(segmention2[2])
                            imigration = list(imigration)
                            imigration[len(imigration) - 1] = loip[len(loip) - 1]
                            print('\n------------------------------')
                            print('*Final displacement*\n ', imigration, '-->', 'new makespan of Task:',
                                  sum(imigration))

                            with open(fn_fn, 'a') as f:
                                imigration = str(imigration)
                                f.write('\n')
                                f.write('Imigration :')
                                f.write(imigration)
                                # f.write('\n')
                                f.write('\n-----------------------------------------')
                    else:
                        print('               * No need to imigrate *')
                        print('\n')
                        time.sleep(0.5)
                        print('Sorting Population', end='')
                        time.sleep(0.3)
                        print(' .', end='')
                        time.sleep(0.3)
                        print('.', end='')
                        time.sleep(0.3)
                        print('.')
                        time.sleep(0.1)
                        time.sleep(0.5)
                        print('Removing worst Fitnesses', end='')
                        time.sleep(0.3)
                        print(' .', end='')
                        time.sleep(0.3)
                        print('.', end='')
                        time.sleep(0.3)
                        print('.')
                        time.sleep(0.3)
                        print('\nDone !')
                        loip = list(loip)
                        print('No MRN : ,', loip)

                        with open(fn_fn, 'a') as f:
                            loip = list(loip)
                            loip = str(loip)
                            f.write('\n')
                            f.write('No imigration:')
                            f.write(str(loip))
                            f.write('\n-----------------------------------------')
                elif ms2 > ms:
                    makespan = loip
                    if (MRN) > 0:
                        print('               * Imigration is possible *')
                        print('\n')
                        segmention = np.array_split(makespan, (2, 3))
                        segmention2 = np.array_split(loip2, (2, 3))
                        print('makespan segmention:', segmention)
                        print('Task segmention:', segmention2)

                        if sum(segmention2[2]) > sum(segmention[2]):
                            sub = np.subtract(segmention2[2], segmention[2])
                            segmention2[2] = segmention2[2] - sub
                            imigration = list(segmention2[0]) + list(segmention2[1]) + list(segmention2[2])
                            imigration = list(imigration)
                            imigration[len(imigration) - 1] = loip2[len(loip) - 1]
                            print('\n------------------------------')
                            print('*1st displacement*\n ', imigration, '-->', 'new makespan of Task:',
                                  sum(imigration))

                        if sum(segmention2[0]) > sum(segmention[0]):
                            sub = np.subtract(segmention2[0], segmention[0])
                            segmention2[0] = segmention2[0] - sub
                            imigration = list(segmention2[0]) + list(segmention2[1]) + list(segmention2[2])
                            imigration = list(imigration)
                            imigration[len(imigration) - 1] = loip2[len(loip) - 1]
                            print('\n------------------------------')
                            print('*Final displacement*\n ', imigration, '-->', 'new makespan of Task:',
                                  sum(imigration))

                            with open(fn_fn, 'a') as f:
                                imigration = str(imigration)
                                f.write('\n')
                                f.write('Imigration :')
                                f.write(imigration)
                                # f.write('\n')
                                f.write('\n-----------------------------------------')
                    else:
                        print('               * No need to imigrate *')
                        print('\n')
                        time.sleep(0.5)
                        print('Sorting Population', end='')
                        time.sleep(0.3)
                        print(' .', end='')
                        time.sleep(0.3)
                        print('.', end='')
                        time.sleep(0.3)
                        print('.')
                        time.sleep(0.1)
                        time.sleep(0.5)
                        print('Removing worst Fitnesses', end='')
                        time.sleep(0.3)
                        print(' .', end='')
                        time.sleep(0.3)
                        print('.', end='')
                        time.sleep(0.3)
                        print('.')
                        time.sleep(0.3)
                        print('\nDone !')
                        loip2 = list(loip2)
                        print('No MRN ,', loip2)

                        with open(fn_fn, 'a') as f:

                            f.write('\n')
                            f.write('No imigration :')
                            f.write(str(loip2))
                            # f.write('\n')
                            f.write('\n-----------------------------------------')
            else :
                print('               * No need to imigrate *')
                print('\n')
                time.sleep(0.5)
                print('Sorting Population', end='')
                time.sleep(0.3)
                print(' .', end='')
                time.sleep(0.3)
                print('.', end='')
                time.sleep(0.3)
                print('.')
                time.sleep(0.1)
                time.sleep(0.5)
                print('Removing worst Fitnesses', end='')
                time.sleep(0.3)
                print(' .', end='')
                time.sleep(0.3)
                print('.', end='')
                time.sleep(0.3)
                print('.')
                time.sleep(0.3)
                print('\nDone !')
                loip2 = list(loip2)
                print('No MRN ,', loip2)

                with open(fn_fn, 'a') as f:

                    f.write('\n')
                    f.write('No imigration :')
                    f.write(str(loip2))
                    # f.write('\n')
                    f.write('\n-----------------------------------------')
    else :
        time.sleep(0.3)
        print('--> Muta', end='')
        time.sleep(0.3)
        print('tion',end='')
        time.sleep(0.3)
        print(' .', end='')
        time.sleep(0.3)
        print('.', end='')
        time.sleep(0.3)
        print('.\n', end='')
        if sum(pop1) > sum(pop2):
            makespan = pop2
            segmention = np.array_split(makespan, (2, random.randint(4, 7)))
            segmention2 = np.array_split(pop1, (2, random.randint(4, 7)))
            segmention2[random.randrange(0,2)][random.randrange(0,2)] = segmention[random.randrange(0,2)][random.randrange(0,1)]
            segmention2[random.randrange(0,1)][random.randrange(0,2)] = segmention[random.randrange(0,2)][random.randrange(0,1)]
            solution = list(segmention2[0]) + list(segmention2[1]) + list(segmention2[2])
            solution = list(solution)
            segmention = np.array_split(makespan, (2, random.randint(4, 7)))
            segmention2 = np.array_split(pop3, (2, random.randint(4, 7)))
            segmention2[random.randrange(0, 2)][random.randrange(0, 2)] = segmention[random.randrange(0, 2)][
                random.randrange(0, 1)]
            segmention2[random.randrange(0, 1)][random.randrange(0, 2)] = segmention[random.randrange(0, 2)][
                random.randrange(0, 1)]
            solution2 = list(segmention2[0]) + list(segmention2[1]) + list(segmention2[2])
            solution2 = list(solution2)
            loip = np.array(solution)
            loip2 = np.array(solution2)
            loip = np.array(solution)
            loip2 = np.array(solution2)
            if len(loip) == len(loip2) :
                ms = sum(loip)
                ms2 = sum(loip2)
                if ms > ms2:
                    makespan = loip2
                    if (MRN) > 0:
                        print('               * Imigration is possible *')
                        print('\n')
                        segmention = np.array_split(makespan, (2, 3))
                        segmention2 = np.array_split(loip, (2, 3))
                        print('makespan segmention:', segmention)
                        print('Task segmention:', segmention2)

                        if sum(segmention2[2]) > sum(segmention[2]):
                            sub = np.subtract(segmention2[2], segmention[2])
                            segmention2[2] = segmention2[2] - sub
                            imigration = list(segmention2[0]) + list(segmention2[1]) + list(segmention2[2])
                            imigration = list(imigration)
                            imigration[len(imigration) - 1] = loip2[len(loip) - 1]
                            print('\n------------------------------')
                            print('*1st displacement*\n ', imigration, '-->', 'new makespan of Task:',
                                  sum(imigration))
                            # print('\n------------------------------')
                        if sum(segmention2[0]) > sum(segmention[0]):
                            sub = np.subtract(segmention2[0], segmention[0])
                            segmention2[0] = segmention2[0] - sub
                            print('our segmention is:', segmention2)
                            imigration = list(segmention2[0]) + list(segmention2[1]) + list(segmention2[2])
                            imigration = list(imigration)
                            imigration[len(imigration) - 1] = loip[len(loip) - 1]
                            print('\n------------------------------')
                            print('*Final displacement*\n ', imigration, '-->', 'new makespan of Task:',
                                  sum(imigration))

                            with open(fn_fn, 'a') as f:
                                imigration = str(imigration)
                                f.write('\n')
                                f.write('Imigration :')
                                f.write(imigration)
                                # f.write('\n')
                                f.write('\n-----------------------------------------')
                    else:
                        print('               * No need to imigrate *')
                        print('\n')
                        time.sleep(0.5)
                        print('Sorting Population', end='')
                        time.sleep(0.3)
                        print(' .', end='')
                        time.sleep(0.3)
                        print('.', end='')
                        time.sleep(0.3)
                        print('.')
                        time.sleep(0.1)
                        time.sleep(0.5)
                        print('Removing worst Fitnesses', end='')
                        time.sleep(0.3)
                        print(' .', end='')
                        time.sleep(0.3)
                        print('.', end='')
                        time.sleep(0.3)
                        print('.')
                        time.sleep(0.3)
                        print('\nDone !')
                        loip = list(loip)
                        print('No MRN : ,', loip)

                        with open(fn_fn, 'a') as f:
                            loip = list(loip)
                            # loip = str(loip)
                            f.write('\n')
                            f.write('No imigration:')
                            f.write(str(loip))
                            f.write('\n-----------------------------------------')
                elif ms2 > ms:
                    makespan = loip
                    if (MRN) > 0:
                        print('               * Imigration is possible *')
                        print('\n')
                        segmention = np.array_split(makespan, (2, 3))
                        segmention2 = np.array_split(loip2, (2, 3))
                        print('makespan segmention:', segmention)
                        print('Task segmention:', segmention2)

                        if sum(segmention2[2]) > sum(segmention[2]):
                            sub = np.subtract(segmention2[2], segmention[2])
                            segmention2[2] = segmention2[2] - sub
                            imigration = list(segmention2[0]) + list(segmention2[1]) + list(segmention2[2])
                            imigration = list(imigration)
                            imigration[len(imigration) - 1] = loip2[len(loip) - 1]
                            print('\n------------------------------')
                            print('*1st displacement*\n ', imigration, '-->', 'new makespan of Task:',
                                  sum(imigration))

                        if sum(segmention2[0]) > sum(segmention[0]):
                            sub = np.subtract(segmention2[0], segmention[0])
                            segmention2[0] = segmention2[0] - sub
                            imigration = list(segmention2[0]) + list(segmention2[1]) + list(segmention2[2])
                            imigration = list(imigration)
                            imigration[len(imigration) - 1] = loip2[len(loip) - 1]
                            print('\n------------------------------')
                            print('*Final displacement*\n ', imigration, '-->', 'new makespan of Task:',
                                  sum(imigration))

                            with open(fn_fn, 'a') as f:
                                imigration = str(imigration)
                                f.write('\n')
                                f.write('Imigration :')
                                f.write(imigration)
                                # f.write('\n')
                                f.write('\n-----------------------------------------')
                    else:
                        print('               * No need to imigrate *')
                        print('\n')
                        time.sleep(0.5)
                        print('Sorting Population', end='')
                        time.sleep(0.3)
                        print(' .', end='')
                        time.sleep(0.3)
                        print('.', end='')
                        time.sleep(0.3)
                        print('.')
                        time.sleep(0.1)
                        time.sleep(0.5)
                        print('Removing worst Fitnesses', end='')
                        time.sleep(0.3)
                        print(' .', end='')
                        time.sleep(0.3)
                        print('.', end='')
                        time.sleep(0.3)
                        print('.')
                        time.sleep(0.3)
                        print('\nDone !')
                        loip2 = list(loip2)
                        print('No MRN ,', loip2)

                        with open(fn_fn, 'a') as f:

                            f.write('\n')
                            f.write('No imigration :')
                            f.write(str(loip2))
                            # f.write('\n')
                            f.write('\n-----------------------------------------')
            else :
                print('               * No need to imigrate *')
                print('\n')
                time.sleep(0.5)
                print('Sorting Population', end='')
                time.sleep(0.3)
                print(' .', end='')
                time.sleep(0.3)
                print('.', end='')
                time.sleep(0.3)
                print('.')
                time.sleep(0.1)
                time.sleep(0.5)
                print('Removing worst Fitnesses', end='')
                time.sleep(0.3)
                print(' .', end='')
                time.sleep(0.3)
                print('.', end='')
                time.sleep(0.3)
                print('.')
                time.sleep(0.3)
                print('\nDone !')
                loip2 = list(loip2)
                print('No MRN ,', loip2)

                with open(fn_fn, 'a') as f:

                    f.write('\n')
                    f.write('No imigration :')
                    f.write(str(loip2))
                    # f.write('\n')
                    f.write('\n-----------------------------------------')

        else :
            makespan = pop1
            segmention = np.array_split(makespan, (2, random.randint(4, 7)))
            segmention2 = np.array_split(pop2, (2, random.randint(4, 7)))
            segmention2[random.randrange(0, 2)][random.randrange(0, 1)] = segmention[random.randrange(0, 1)][
                random.randrange(0, 2)]
            segmention2[random.randrange(0, 1)][random.randrange(0, 1)] = segmention[random.randrange(0, 2)][
                random.randrange(0, 2)]
            solution = list(segmention2[0]) + list(segmention2[1]) + list(segmention2[2])
            solution = list(solution)
            segmention = np.array_split(makespan, (2, random.randint(4, 7)))
            segmention2 = np.array_split(pop3, (2, random.randint(4, 7)))
            segmention2[random.randrange(0, 2)][random.randrange(0, 1)] = segmention[random.randrange(0, 1)][
                random.randrange(0, 2)]
            segmention2[random.randrange(0, 1)][random.randrange(0, 1)] = segmention[random.randrange(0, 2)][
                random.randrange(0, 2)]
            solution2 = list(segmention2[0]) + list(segmention2[1]) + list(segmention2[2])
            solution2 = list(solution2)
            loip = np.array(solution)
            loip2 = np.array(solution2)

            if len(loip) == len(loip2) :
                ms = sum(loip)
                ms2 = sum(loip2)
                if ms > ms2:
                    makespan = loip2
                    if (MRN) > 0:
                        print('               * Imigration is possible *')
                        print('\n')
                        segmention = np.array_split(makespan, (2, 3))
                        segmention2 = np.array_split(loip, (2, 3))
                        print('makespan segmention:', segmention)
                        print('Task segmention:', segmention2)

                        if sum(segmention2[2]) > sum(segmention[2]):
                            sub = np.subtract(segmention2[2], segmention[2])
                            segmention2[2] = segmention2[2] - sub
                            imigration = list(segmention2[0]) + list(segmention2[1]) + list(segmention2[2])
                            imigration = list(imigration)
                            imigration[len(imigration) - 1] = loip2[len(loip) - 1]
                            print('\n------------------------------')
                            print('*1st displacement*\n ', imigration, '-->', 'new makespan of Task:',
                                  sum(imigration))
                            # print('\n------------------------------')
                        if sum(segmention2[0]) > sum(segmention[0]):
                            sub = np.subtract(segmention2[0], segmention[0])
                            segmention2[0] = segmention2[0] - sub
                            print('our segmention is:', segmention2)
                            imigration = list(segmention2[0]) + list(segmention2[1]) + list(segmention2[2])
                            imigration = list(imigration)
                            imigration[len(imigration) - 1] = loip[len(loip) - 1]
                            print('\n------------------------------')
                            print('*Final displacement*\n ', imigration, '-->', 'new makespan of Task:',
                                  sum(imigration))

                            with open(fn_fn, 'a') as f:
                                imigration = str(imigration)
                                f.write('\n')
                                f.write('Imigration :')
                                f.write(imigration)
                                # f.write('\n')
                                f.write('\n-----------------------------------------')
                    else:
                        print('               * No need to imigrate *')
                        print('\n')
                        time.sleep(0.5)
                        print('Sorting Population', end='')
                        time.sleep(0.3)
                        print(' .', end='')
                        time.sleep(0.3)
                        print('.', end='')
                        time.sleep(0.3)
                        print('.')
                        time.sleep(0.1)
                        time.sleep(0.5)
                        print('Removing worst Fitnesses', end='')
                        time.sleep(0.3)
                        print(' .', end='')
                        time.sleep(0.3)
                        print('.', end='')
                        time.sleep(0.3)
                        print('.')
                        time.sleep(0.3)
                        print('\nDone !')
                        loip = list(loip)
                        print('No MRN : ,', loip)

                        with open(fn_fn, 'a') as f:
                            loip = list(loip)
                            # loip = str(loip)
                            f.write('\n')
                            f.write('No imigration:')
                            f.write(str(loip))
                            f.write('\n-----------------------------------------')
                elif ms2 > ms:
                    makespan = loip
                    if (MRN) > 0:
                        print('               * Imigration is possible *')
                        print('\n')
                        segmention = np.array_split(makespan, (2, 3))
                        segmention2 = np.array_split(loip2, (2, 3))
                        print('makespan segmention:', segmention)
                        print('Task segmention:', segmention2)

                        if sum(segmention2[2]) > sum(segmention[2]):
                            sub = np.subtract(segmention2[2], segmention[2])
                            segmention2[2] = segmention2[2] - sub
                            imigration = list(segmention2[0]) + list(segmention2[1]) + list(segmention2[2])
                            imigration = list(imigration)
                            imigration[len(imigration) - 1] = loip2[len(loip) - 1]
                            print('\n------------------------------')
                            print('*1st displacement*\n ', imigration, '-->', 'new makespan of Task:',
                                  sum(imigration))

                        if sum(segmention2[0]) > sum(segmention[0]):
                            sub = np.subtract(segmention2[0], segmention[0])
                            segmention2[0] = segmention2[0] - sub
                            imigration = list(segmention2[0]) + list(segmention2[1]) + list(segmention2[2])
                            imigration = list(imigration)
                            imigration[len(imigration) - 1] = loip2[len(loip) - 1]
                            print('\n------------------------------')
                            print('*Final displacement*\n ', imigration, '-->', 'new makespan of Task:',
                                  sum(imigration))

                            with open(fn_fn, 'a') as f:
                                imigration = str(imigration)
                                f.write('\n')
                                f.write('Imigration :')
                                f.write(imigration)
                                # f.write('\n')
                                f.write('\n-----------------------------------------')
                    else:
                        print('               * No need to imigrate *')
                        print('\n')
                        time.sleep(0.5)
                        print('Sorting Population', end='')
                        time.sleep(0.3)
                        print(' .', end='')
                        time.sleep(0.3)
                        print('.', end='')
                        time.sleep(0.3)
                        print('.')
                        time.sleep(0.1)
                        time.sleep(0.5)
                        print('Removing worst Fitnesses', end='')
                        time.sleep(0.3)
                        print(' .', end='')
                        time.sleep(0.3)
                        print('.', end='')
                        time.sleep(0.3)
                        print('.')
                        time.sleep(0.3)
                        print('\nDone !')
                        loip2 = list(loip2)
                        print('No MRN ,', loip2)

                        with open(fn_fn, 'a') as f:

                            f.write('\n')
                            f.write('No imigration :')
                            f.write(str(loip2))
                            # f.write('\n')
                            f.write('\n-----------------------------------------')
            else:
                print('               * No need to imigrate *')
                print('\n')
                time.sleep(0.5)
                print('Sorting Population', end='')
                time.sleep(0.3)
                print(' .', end='')
                time.sleep(0.3)
                print('.', end='')
                time.sleep(0.3)
                print('.')
                time.sleep(0.1)
                time.sleep(0.5)
                print('Removing worst Fitnesses', end='')
                time.sleep(0.3)
                print(' .', end='')
                time.sleep(0.3)
                print('.', end='')
                time.sleep(0.3)
                print('.')
                time.sleep(0.3)
                print('\nDone !')
                loip2 = list(loip2)
                print('No MRN ,', loip2)

                with open(fn_fn, 'a') as f:

                    f.write('\n')
                    f.write('No imigration :')
                    f.write(str(loip2))
                    # f.write('\n')
                    f.write('\n-----------------------------------------')


def IHHO(x=str, y=str):
    file_file = 'C:/Users/Naweed/PycharmProjects/IHHO/HHO Solution/IHHO Solution.txt'
    loip = np.array(x)
    loip2 = np.array(y)
    try:
        if len(loip) != len(loip2):
            print('-------------------------------------')
            print('*** Warning ***\n Arrays size must be equal\nfor a better IHHO performace!!!\n')
            print('-------------------------------------')
    except ValueError:
        print('Arrays size must be equal !!!')
    r = random.randint(0,1)
    ms = sum(loip)
    ms2 = sum(loip2)
    tasks = [t1,t2,t3,t4,t5,t6,t7]
    total_tasks = len(tasks)
    t = random.randint (1,7)
    e = (2 * e0) * (1-(t/total_tasks))
    j = 2 * (1-r5)
    lb = 0
    ub = random.randint(1, 4)

    if ms > ms2 :
        makespan = loip2
        if r > 0.5 and e > 0.5:
            if len(makespan) and len(loip) == 7 or 8 or 9 or 10 or 11 or 12 or 13 or 14 or 15 or 16 or 17 or 18 or 19 or 20 or 21 or 22:
                segmention = np.array_split (makespan,(2,3))
                segmention2 = np.array_split(loip,(2,3))
                print('makespan segmention:' , segmention)
                print('Task segmention:' , segmention2)
                if j >= 2:
                    if sum(segmention2[2]) > sum(segmention[2]):
                        sub = np.subtract(segmention2[2], segmention[2])
                        segmention2[2] = segmention2[2] - sub
                        soft_besiege = list(segmention2[0]) + list(segmention2[1]) + list(segmention2[2])
                        soft_besiege = list(soft_besiege)
                        print('\n------------------------------')
                        print('*1st displacement*\n after soft besiege:',soft_besiege,'-->','new makespan of Task:',sum(soft_besiege))
                        # print('\n------------------------------')
                    if sum(segmention2[0]) > sum(segmention[0]):
                        sub = np.subtract(segmention2[0], segmention[0])
                        segmention2[0] = segmention2[0] - sub
                        print('our segmention is:', segmention2)
                        soft_besiege = list(segmention2[0]) + list(segmention2[1]) + list(segmention2[2])
                        soft_besiege = list(soft_besiege)
                        print('\n------------------------------')
                        print('*Final displacement*\n after soft besiege:', soft_besiege, '-->','new makespan of Task:',sum(soft_besiege))
                        with open(file_file, 'a') as f:
                            soft_besiege = str(soft_besiege)
                            f.write('\n')
                            f.write('Soft , j >=2 :')
                            f.write(soft_besiege)
                            # f.write('\n')
                            f.write('\n-----------------------------------------')
                else :
                        loip = np.sort(loip)
                        loip = list(loip)
                        print('\n----------------------------------------------')
                        print('* Makespan is :', makespan, 'Makespan :', sum(makespan))
                        print('* Task is :', loip, 'Makespan is :', sum(loip))
                        makespan = np.sort(makespan)
                        loip = np.delete(loip, len(loip) - 1)
                        loip = np.append(loip, makespan[len(makespan) - 1])

                        makespan = list (makespan)
                        print('* New Task is :', list(loip), 'New Makespan is :', sum(loip))
                        print('\n----------------------------------------------')

                        with open(file_file, 'a') as f:
                            loip = list(loip)
                            f.write('\n')
                            f.write('Soft , j = 0 :')
                            f.write(str(loip))
                            # f.write('\n')
                            f.write('\n-----------------------------------------')
    else:
        makespan = loip
        if r >= 0.5 and e >= 0.5:
            makespan = loip
            if len(makespan) and len(loip2) == 7 or 8 or 9 or 10 or 11 or 12 or 13 or 14 or 15 or 16 or 17 or 18 or 19 or 20 or 21 or 22:
                segmention = np.array_split(makespan, (2, 3))
                segmention2 = np.array_split(loip2, (2, 3))
                print('makespan segmention:', segmention)
                print('Task segmention:', segmention2)

                if j >= 2:
                    if sum(segmention2[2]) > sum(segmention[2]):
                        sub = np.subtract (segmention2[2], segmention[2])
                        segmention2[2] = segmention2[2] - sub
                        soft_besiege = list(segmention2[0]) + list(segmention2[1]) + list(segmention2[2])
                        soft_besiege = list(soft_besiege)
                        print('\n------------------------------')
                        print('*1st displacement*\n after soft besiege:',soft_besiege,'-->','new makespan of Task:',sum(soft_besiege))
                        # print('\n------------------------------')

                    if sum(segmention2[0]) > sum(segmention[0]):
                        sub = np.subtract(segmention2[0], segmention[0])
                        segmention2[0] = segmention2[0] - sub
                        soft_besiege = list(segmention2[0]) + list(segmention2[1]) + list(segmention2[2])
                        soft_besiege = list(soft_besiege)
                        print('\n------------------------------')
                        print('*Final displacement*\n after soft besiege:',soft_besiege,'-->','new makespan of Task:',sum(soft_besiege))
                        with open(file_file, 'a') as f:
                            soft_besiege = str(soft_besiege)
                            f.write('\n')
                            f.write('Soft , j >=2 :')
                            f.write(soft_besiege)
                            # f.write('\n')
                            f.write('\n-----------------------------------------')
                else:
                    loip2 = np.sort(loip2)
                    makespan = np.sort(makespan)
                    loip2 = list(loip2)
                    print('\n----------------------------------------------')
                    print('* Makespan is :', makespan, 'Makespan :', sum(makespan))
                    print('* Task is :', loip2, 'Makespan is :', sum(loip2))
                    loip2 = np.delete(loip2, len(loip2) - 1)
                    loip2 = np.append(loip2, makespan[len(makespan) - 1])
                    makespan = list(makespan)
                    print('* New Task is :', list(loip2), 'New Makespan is :', sum(loip2))
                    print('\n----------------------------------------------')

                    with open(file_file, 'a') as f:
                        loip2 = list(loip2)

                        f.write('\n')
                        f.write('Soft , j = 0 :')
                        f.write(str(loip2))
                        # f.write('\n')
                        f.write('\n-----------------------------------------')

            elif len(makespan) and len(loip2) == 4 or 5 or 6:
                if j >= 2:
                    if ms2 > ms:
                        makespan =loip
                        segmention = np.array_split(makespan, (1, 2))
                        segmention2 = np.array_split(loip2, (2, 3))
                        print('makespan segmention:', segmention)
                        print('Task segmention:', segmention2)
                    if sum(segmention2[2]) > sum(segmention[2]):
                        sub = np.subtract(segmention2[2], segmention[2])
                        segmention2[2] = segmention2[2] - sub
                        soft_besiege = list(segmention2[0]) + list(segmention2[1]) + list(segmention2[2])
                        soft_besiege = list(soft_besiege)
                        with open(file_file, 'a') as f:
                            soft_besiege = str(soft_besiege)
                            f.write('\n')
                            f.write('Soft , j >=2 :')
                            f.write(soft_besiege)
                            # f.write('\n')
                            f.write('\n-----------------------------------------')
                else:
                    loip2 = np.sort(loip2)
                    makespan = np.sort(makespan)
                    loip2 = list(loip2)
                    print('\n----------------------------------------------')
                    print('* Makespan is :', makespan, 'Makespan :', sum(makespan))
                    print('* Task is :', loip2, 'Makespan is :', sum(loip2))
                    loip2 = np.delete(loip2, len(loip2) - 1)
                    loip2 = np.append(loip2, makespan[len(makespan) - 1])

                    makespan = list(makespan)

                    print('* New Task is :', list(loip2), 'New Makespan is :', sum(loip2))
                    print('\n----------------------------------------------')

                    with open(file_file, 'a') as f:
                        loip2 = list(loip2)

                        f.write('\n')
                        f.write('Soft , j >=2 :')
                        f.write(str(loip2))
                        # f.write('\n')
                        f.write('\n-----------------------------------------')


            elif len(makespan) and len(loip2) == 4 or 5 or 6:
                if j >= 2:
                    if ms > ms2:
                        makespan = loip2
                        segmention = np.array_split(makespan, (1, 2))
                        segmention2 = np.array_split(loip, (2, 3))
                        print('makespan segmention:', segmention)
                        print('Task segmention:', segmention2)
                    if sum(segmention2[2]) > sum(segmention[2]):
                        sub = np.subtract(segmention2[2], segmention[2])
                        segmention2[2] = segmention2[2] - sub
                        soft_besiege = list(segmention2[0]) + list(segmention2[1]) + list(segmention2[2])
                        soft_besiege = list(soft_besiege)
                        with open(file_file, 'a') as f:
                            soft_besiege = str(soft_besiege)
                            f.write('\n')
                            f.write('Soft , j >=2 :')
                            f.write(soft_besiege)
                            # f.write('\n')
                            f.write('\n-----------------------------------------')
                else:
                    loip = np.sort(loip)
                    makespan = np.sort(makespan)
                    loip = list(loip)
                    print('\n----------------------------------------------')
                    print('* Makespan is :', makespan, 'Makespan :', sum(makespan))
                    print('* Task is :', loip, 'Makespan is :', sum(loip))
                    loip = np.delete(loip, len(loip) - 1)
                    loip = np.append(loip, makespan[len(makespan) - 1])

                    makespan = list(makespan)

                    print('* New Task is :', list(loip), 'New Makespan is :', sum(loip))
                    print('\n----------------------------------------------')

                    with open(file_file, 'a') as f:
                        loip = list(loip)

                        f.write('\n')
                        f.write('Soft , j >=2 :')
                        f.write(str(loip))
                        # f.write('\n')
                        f.write('\n-----------------------------------------')
    if ms > ms2:
        if r >=0.5 and e<0.5 :
            makespan = loip2
            delta_x = np.setdiff1d(makespan,loip)
            delta_x2= np.setdiff1d(loip,makespan)
            delta_x3=np.append(delta_x,delta_x2)
            hard_besiege = np.setdiff1d(makespan,(e*delta_x3))
            len_arr = len(loip2)
            hard_besiege = np.resize(hard_besiege, len_arr)
            hard_besiege[1] = loip[2]
            hard_besiege[2] = loip[1]
            hard_besiege = list(hard_besiege)
            print('after hard besiege:',hard_besiege,'new makespan is:',sum(hard_besiege))
            with open(file_file, 'a') as f:
                hard_besiege = str(hard_besiege)
                f.write('\n')
                f.write('Hard :')

                f.write(hard_besiege)
                # f.write('\n')
                f.write('\n-----------------------------------------')
    else:
        makespan = loip
        if r >= 0.5 and e < 0.5:
            makespan = loip
            delta_x = np.setdiff1d(makespan,loip2)
            delta_x2 = np.setdiff1d(loip2, makespan)
            delta_x3 = np.append(delta_x, delta_x2)
            hard_besiege = np.setdiff1d(makespan, (e * delta_x3))
            len_arr = len(loip2)
            hard_besiege = np.resize(hard_besiege,len_arr)
            hard_besiege[1] = loip2[2]
            hard_besiege[2] = loip2[1]
            hard_besiege = list(hard_besiege)
            print('after hard besiege:', hard_besiege, 'new makespan is:', sum(hard_besiege))
            with open(file_file, 'a') as f:
                hard_besiege = str(hard_besiege)
                f.write('\n')
                f.write('Hard :')
                f.write(hard_besiege)
                # f.write('\n')
                f.write('\n-----------------------------------------')

    if ms > ms2:
        makespan = loip2
        print('makespan is :', makespan, '-->', 'makespan of it :', sum(makespan))
        print('Task is :', loip, '-->', 'makespan of Task is :', sum(loip))
        print('\n------------------------------')
        if r < 0.5 and e >=0.5:
                makespan = loip2
                j = 2 * (1 - r5)
                # levy_flight
                # d = random.randint(0,1)
                # s=1*d
                # beta = 1.5
                # sigma = (math.gamma(1 + beta) * math.sin(math.pi * beta / 2) / (
                #             math.gamma((1 + beta) / 2) * beta * 2 ** ((beta - 1) / 2))) ** (1 / beta)
                # u = 0.01 * numpy.random.randn(d) * sigma
                # v = numpy.random.randn(d)
                # zz = numpy.power(numpy.absolute(v), (1 / beta))
                # levy_f = numpy.divide(u, zz)

                Y = np.setdiff1d(makespan,(e*j*makespan))
                Y = np.setdiff1d(Y,loip)
                Y2 = np.setdiff1d(loip,Y)
                Y3 = np.append(Y,Y2)
                len_arr = len(loip)
                Y3 = np.resize(Y3,len_arr)
                Y3 = list(Y3)

                # Z = Y2 * s * levy_f
                print('after soft besiege with rapid dives :', Y3 , 'new makespan is :',sum(Y3))
                with open(file_file, 'a') as f:
                    Y3 = str(Y3)
                    f.write('\n')
                    f.write('Soft rapid :')
                    f.write(Y3)
                    # f.write('\n')
                    f.write('\n-----------------------------------------')
    else:
        makespan = loip
        print('makespan is :', makespan, '-->', 'makespan of it :', sum(makespan))
        print('Task is :', loip2, '-->', 'makespan of Task is :', sum(loip2))
        print('\n------------------------------')
        if r < 0.5 and e >=0.5:
            makespan = loip

            # # levy_flight
            # d = random.randint(0, 1)
            # s = 1 * d
            # beta = 1.5
            # sigma = (math.gamma(1 + beta) * math.sin(math.pi * beta / 2) / (
            #         math.gamma((1 + beta) / 2) * beta * 2 ** ((beta - 1) / 2))) ** (1 / beta)
            # u = 0.01 * numpy.random.randn(d) * sigma
            # v = numpy.random.randn(d)
            # zz = numpy.power(numpy.absolute(v), (1 / beta))
            # levy_f = numpy.divide(u, zz)

            Y = np.setdiff1d(makespan, (e * j * makespan))
            Y = np.setdiff1d(Y, loip2)
            Y2 = np.setdiff1d(loip2, Y)
            Y3 = np.append(Y, Y2)
            len_arr = len(loip)
            Y3 = np.resize(Y3, len_arr)
            Y3 = np.resize(Y3,len_arr)
            Y3 = list(Y3)

            # Z = Y2 * s * levy_f
            print('after soft besiege with rapid dives :', Y3 , 'new makespan is :',sum(Y3))
            with open(file_file, 'a') as f:
                Y3 = str(Y3)
                f.write('\n')
                f.write('Soft rapid :')
                f.write(Y3)
                # f.write('\n')
                f.write('\n-----------------------------------------')

    if ms > ms2:
        j = 2 * (1 - r5)
        total_tasks = [loip,loip2]
        n = len(total_tasks)
        loip = np.array(loip)
        xm = np.floor(loip / n)
        makespan = loip2
        print('makespan is :', makespan, '-->', 'makespan of it :', sum(makespan))
        print('Task is :', loip, '-->', 'makespan of Task is :', sum(loip))
        print('\n------------------------------')
        if r < 0.5 and e < 0.5 :
            hbrd = np.setdiff1d( (e*j*makespan),xm)
            hbrd2 = np.setdiff1d (makespan,hbrd)
            hbrd2 = list(hbrd2)
            print('after hard besiege with rapid dives :',hbrd2 ,'new makespan is :',sum(hbrd2))
            with open(file_file, 'a') as f:
                hbrd2 = str(hbrd2)
                f.write('\n')
                f.write('Hard rapid :')
                f.write(hbrd2)
                # f.write('\n')
                f.write('\n-----------------------------------------')
    else:
        j = 2 * (1 - r5)
        total_tasks = [loip, loip2]
        n = len(total_tasks)
        loip2 = np.array(loip2)
        xm = np.floor(loip2 / n)
        makespan = loip
        print('makespan is :', makespan, '-->', 'makespan of it :', sum(makespan))
        print('Task is :', loip2, '-->', 'makespan of Task is :', sum(loip2))
        print('\n------------------------------')

        if r < 0.5 and e < 0.5:
            hbrd = np.setdiff1d((e * j * makespan), xm)
            hbrd2 = np.setdiff1d(makespan, hbrd)
            hbrd2 = list(hbrd2)
            print('after hard besiege with rapid dives :',hbrd2 ,'new makespan is :',sum(hbrd2))
            with open(file_file, 'a') as f:
                hbrd2 = str(hbrd2)
                f.write('\n')
                f.write('Hard rapid :')
                f.write(hbrd2)
                # f.write('\n')
                f.write('\n-----------------------------------------')

def Cuckoo_pop (j):
    filete = 'C:/Users/Naweed/PycharmProjects/IHHO/Cuckoo/Cuckoo popualation.txt'

    for pop in range(j) :
        Max_NNS = random.randint(10,18)
        Min_NNS = random.randint(5,10)
        rand = random.randint(0,1)
        k = (Max_NNS - Min_NNS) * rand + Min_NNS
        task = np.random.randint(15, size=(k))
        task = list (task)
        length = len(task)

        with open(filete, 'a') as f:
            f.write(str(task))
            f.write(' -> size =')
            f.write(str(length))
            f.write('\n-------------------------------------------------------------------')
            f.write('\n')

def Cuckoo (x,y):
    file_pat = 'C:/Users/Naweed/PycharmProjects/IHHO/Cuckoo/Cuckoo Solutions.txt'
    loip = np.array(x)
    loip2 = np.array(y)
    try:
        if len(loip) != len(loip2):
            print('-------------------------------------')
            print('*** Warning ***\n Arrays size must be equal\nfor a better IHHO performace!!!\n')
            print('-------------------------------------')
    except ValueError:
        print('Arrays size must be equal !!!')

    ms = sum(loip)
    ms2 = sum(loip2)
    tasks = [t1, t2, t3, t4, t5, t6, t7]
    total_tasks = len(tasks)
    t = random.randint(1, 7)
    Var_high_Task = random.randint(5,10)
    Var_Low_Task  = 0
    MRN = np.floor(t / total_tasks) * (Var_high_Task - Var_Low_Task)
    MRN = np.sum(MRN)
    MRN = random.randint(0,1)

    if ms > ms2:
        makespan = loip2
        if  (MRN) > 0 :
            print('               * Imigration is possible *')
            print('\n')
            segmention = np.array_split(makespan, (2, 3))
            segmention2 = np.array_split(loip, (2, 3))
            print('makespan segmention:', segmention)
            print('Task segmention:', segmention2)

            if sum(segmention2[2]) > sum(segmention[2]):
                sub = np.subtract(segmention2[2], segmention[2])
                segmention2[2] = segmention2[2] - sub
                imigration = list(segmention2[0]) + list(segmention2[1]) + list(segmention2[2])
                imigration = list(imigration)
                imigration[len(imigration) - 1] = loip2[len(loip) - 1]
                print('\n------------------------------')
                print('*1st displacement*\n ', imigration, '-->', 'new makespan of Task:',
                      sum(imigration))
                # print('\n------------------------------')
            if sum(segmention2[0]) > sum(segmention[0]):
                sub = np.subtract(segmention2[0], segmention[0])
                segmention2[0] = segmention2[0] - sub
                print('our segmention is:', segmention2)
                imigration = list(segmention2[0]) + list(segmention2[1]) + list(segmention2[2])
                imigration = list(imigration)
                imigration[len(imigration)-1] = loip[len(loip)-1]
                print('\n------------------------------')
                print('*Final displacement*\n ', imigration, '-->', 'new makespan of Task:',
                      sum(imigration))

                with open(file_pat, 'a') as f:
                    imigration = str(imigration)
                    f.write('\n')
                    f.write('Imigration :')
                    f.write(imigration)
                    # f.write('\n')
                    f.write('\n-----------------------------------------')
        else:
            print('               * No need to imigrate *')
            print('\n')
            time.sleep(0.5)
            print('Sorting Population', end='')
            time.sleep(0.3)
            print(' .', end='')
            time.sleep(0.3)
            print('.', end='')
            time.sleep(0.3)
            print('.')
            time.sleep(0.1)
            time.sleep(0.5)
            print('Removing worst Fitnesses', end='')
            time.sleep(0.3)
            print(' .', end='')
            time.sleep(0.3)
            print('.', end='')
            time.sleep(0.3)
            print('.')
            time.sleep(0.3)
            print('\nDone !')
            loip = list(loip)
            print('No MRN : ,', loip)

            with open(file_pat, 'a') as f:
                loip = list(loip)
                # loip = str(loip)
                f.write('\n')
                f.write('No imigration:')
                f.write(str(loip))
                f.write('\n-----------------------------------------')
    elif ms2 > ms :
        makespan = loip
        if (MRN) > 0 :
            print('               * Imigration is possible *')
            print('\n')
            segmention = np.array_split(makespan, (2, 3))
            segmention2 = np.array_split(loip2, (2, 3))
            print('makespan segmention:', segmention)
            print('Task segmention:', segmention2)

            if sum(segmention2[2]) > sum(segmention[2]):
                sub = np.subtract(segmention2[2], segmention[2])
                segmention2[2] = segmention2[2] - sub
                imigration = list(segmention2[0]) + list(segmention2[1]) + list(segmention2[2])
                imigration = list(imigration)
                imigration[len(imigration) - 1] = loip2[len(loip) - 1]
                print('\n------------------------------')
                print('*1st displacement*\n ', imigration, '-->', 'new makespan of Task:',
                      sum(imigration))

            if sum(segmention2[0]) > sum(segmention[0]):
                sub = np.subtract(segmention2[0], segmention[0])
                segmention2[0] = segmention2[0] - sub
                imigration = list(segmention2[0]) + list(segmention2[1]) + list(segmention2[2])
                imigration = list(imigration)
                imigration[len(imigration) - 1] = loip2[len(loip) - 1]
                print('\n------------------------------')
                print('*Final displacement*\n ', imigration, '-->', 'new makespan of Task:',
                      sum(imigration))

                with open(file_pat, 'a') as f:
                    imigration = str(imigration)
                    f.write('\n')
                    f.write('Imigration :')
                    f.write(imigration)
                    # f.write('\n')
                    f.write('\n-----------------------------------------')
        else:
            print('               * No need to imigrate *')
            print('\n')
            time.sleep(0.5)
            print('Sorting Population', end='')
            time.sleep(0.3)
            print(' .',end='')
            time.sleep(0.3)
            print('.',end='')
            time.sleep(0.3)
            print('.')
            time.sleep(0.1)
            time.sleep(0.5)
            print('Removing worst Fitnesses', end='')
            time.sleep(0.3)
            print(' .',end='')
            time.sleep(0.3)
            print('.',end='')
            time.sleep(0.3)
            print('.')
            time.sleep(0.3)
            print('\nDone !')
            loip2 = list(loip2)
            print('No MRN ,', loip2)

            with open(file_pat, 'a') as f:

                f.write('\n')
                f.write('No imigration :')
                f.write(str(loip2))
                # f.write('\n')
                f.write('\n-----------------------------------------')


def Solutions () :
    fn2 = 'C:/Users/Naweed/PycharmProjects/IHHO/Cuckoo Genetic/Cuckoo Genetic.txt'
    fn = 'C:/Users/Naweed/PycharmProjects/IHHO/Genetic/Genetic Solutions.txt'
    file_path2 = 'C:/Users/Naweed/PycharmProjects/IHHO/HHO Solution/IHHO Solution.txt'
    file_path = 'C:/Users/Naweed/PycharmProjects/IHHO/HHO Solution/HHO Solution.txt'
    file_path3 = 'C:/Users/Naweed/PycharmProjects/IHHO/Cuckoo/Cuckoo Solutions.txt'

    with open (file_path,'r') as f :
        print('\n')
        print('        *** HHO Solutions *** ')
        print(f.read())

    with open (file_path2,'r') as f :
        print('\n')
        print('        *** IHHO Solutions *** ')
        print(f.read())

    with open(file_path3, 'r') as f:
        print('\n')
        print('        *** Cuckoo Solutions *** ')
        print(f.read())

    with open(fn, 'r') as f:
        print('\n')
        print('        *** Genetic Solutions *** ')
        print(f.read())

    with open(fn2, 'r') as f:
        print('\n')
        print('        *** Cuckoo Genetic Solutions *** ')
        print(f.read())

def Molecular (a=list , b =str):
    fm = 'C:/Users/Naweed/PycharmProjects/IHHO/Graphs/Molecular graph.txt'
    if len(a) > 19 or len(a) < 4:
        print('!! List lengh must be !! ', '\nhigher than 4 or equal 4 \nand lower than 19 or equal 19')
    else:
      if len (a) == 4 :
          root_node = a[0]
          a =[[root_node , a[1] , a[3]] , [root_node,a[2]]]

      elif len(a) == 5 :
          root_node = a[0]
          a = [[root_node, a[1], a[3]], [root_node, a[2]],
               [root_node,a[1],a[4]]]

      elif len(a) == 6 :
          root_node = a[0]
          a = [[root_node, a[1], a[3]], [root_node, a[2],a[5]],
               [root_node, a[1], a[4]]]

      elif len(a) == 7 :
          root_node = a[0]
          a = [[root_node, a[1], a[3]], [root_node, a[2], a[5]],
               [root_node, a[1], a[4]],[root_node,a[2],a[6]]]

      elif len(a) == 8 :
          root_node = a[0]
          a = [[root_node, a[1], a[3],a[7]], [root_node, a[2], a[5]],
               [root_node, a[1], a[4]],[root_node,a[2],a[6]]]

      elif len(a) == 9 :
          root_node = a[0]
          a = [[root_node, a[1], a[3],a[7]],[root_node, a[1], a[3],a[8]], [root_node, a[2], a[5]],
               [root_node, a[1], a[4]],[root_node,a[2],a[6]]]

      elif len(a) == 10 :
          root_node = a[0]
          a = [[root_node, a[1], a[3],a[7]],[root_node, a[1], a[3],a[8]], [root_node, a[2], a[5]],
               [root_node, a[1], a[4],a[9]],[root_node,a[2],a[6]]]

      elif len(a) == 11 :
          root_node = a[0]
          a = [[root_node, a[1], a[3],a[7]],[root_node, a[1], a[3],a[8]], [root_node, a[2], a[5]],
               [root_node, a[1], a[4],a[9]],[root_node, a[1], a[4],a[10]],[root_node,a[2],a[6]]]

      elif len(a) == 12 :
          root_node = a[0]
          a = [[root_node, a[1], a[3],a[7]],[root_node, a[1], a[3],a[8]], [root_node, a[2], a[5],a[11]],
               [root_node, a[1], a[4],a[9]],[root_node, a[1], a[4],a[10]],[root_node,a[2],a[6]]]

      elif len(a) == 13 :
          root_node = a[0]
          a = [[root_node, a[1], a[3],a[7]],[root_node, a[1], a[3],a[8]],
               [root_node, a[2], a[5],a[11]],
               [root_node, a[2], a[5], a[12]], [root_node, a[1], a[4],a[9]]
               ,[root_node, a[1], a[4],a[10]],[root_node,a[2],a[6]]]

      elif len(a) == 14 :
          root_node = a[0]
          a = [[root_node, a[1], a[3],a[7]],[root_node, a[1], a[3],a[8]],
               [root_node, a[2], a[5],a[11]],
               [root_node, a[2], a[5], a[12]], [root_node, a[1], a[4],a[9]]
               ,[root_node, a[1], a[4],a[10]],[root_node,a[2],a[6],a[13]]]

      elif len(a) == 15 :
          root_node = a[0]
          a = [[root_node, a[1], a[3],a[7]],[root_node, a[1], a[3],a[8]],
               [root_node, a[2], a[5],a[11]],
               [root_node, a[2], a[5], a[12]], [root_node, a[1], a[4],a[9]]
               ,[root_node, a[1], a[4],a[10]],[root_node,a[2],a[6],a[13]],[root_node,a[2],a[6],a[14]]]

      elif len(a) == 16 :
          root_node = a[0]
          a = [[root_node, a[1], a[3], a[7], a[15]], [root_node, a[1], a[3], a[8], a[15]],
               [root_node, a[1], a[3], a[8]], [root_node, a[2], a[5], a[11], a[16]],
               [root_node, a[2], a[5], a[12], a[16]], [root_node, a[1], a[4], a[9], a[16]]
              , [root_node, a[1], a[4], a[10], a[15]], [root_node, a[2], a[6], a[13]],
               [root_node, a[2], a[6], a[14]]]

      elif len(a) == 17 :
          root_node = a[0]
          a = [[root_node, a[1], a[3], a[7], a[15]], [root_node, a[1], a[3], a[8], a[15]],
               [root_node, a[1], a[3], a[8]], [root_node, a[2], a[5], a[11], a[16]],
               [root_node, a[2], a[5], a[12], a[16]], [root_node, a[1], a[4], a[9], a[16]]
              , [root_node, a[1], a[4], a[10], a[15]], [root_node, a[2], a[6], a[13]],
               [root_node, a[2], a[6], a[14]]]

      elif len(a) == 18 :
          root_node = a[0]
          a = [[root_node, a[1], a[3],a[7],a[15]],[root_node, a[1], a[3],a[8],a[15]],
               [root_node,a[1], a[3],a[8]],[root_node, a[2], a[5],a[11],a[16]],
               [root_node, a[2], a[5], a[12],a[16]], [root_node, a[1], a[4],a[9],a[16]]
               ,[root_node, a[1], a[4],a[10],a[15]],[root_node,a[2],a[6],a[13],a[17]],
               [root_node,a[2],a[6],a[14],a[17]]]

      elif len(a) == 19:
          root_node = a[0]
          a = [[root_node, a[1], a[3], a[7], a[15]], [root_node, a[1], a[3], a[8], a[15]],
               [root_node, a[1], a[3],a[18]],
               [root_node, a[1], a[3], a[8]], [root_node, a[2], a[5], a[11], a[16],a[18]],
               [root_node, a[2], a[5], a[12], a[16],a[18]], [root_node, a[1], a[4], a[9], a[16],a[18]]
              , [root_node, a[1], a[4], a[10], a[15]], [root_node, a[2], a[6], a[13], a[17]],
               [root_node, a[2], a[6], a[13], a[18]],[root_node, a[2], a[6], a[14], a[17]]]

    with open(fm, 'a') as f:
        f.write('Molecular graph :')
        f.write('-->')
        f.write(b)
        f.write('\n')
        f.write(str(a))
        f.write('\n-------------------------------------------------------------------')
        f.write('\n')

def Molecular_h ():
    t1 = np.random.randint(30, size=(10))
    a = t1
    fm = 'C:/Users/Naweed/PycharmProjects/IHHO/HEFT Metrics/Heft Cpop Molecular Graph.txt'
    if len(a) > 19 or len(a) < 4:
        print('!! List lengh must be !! ', '\nhigher than 4 or equal 4 \nand lower than 19 or equal 19')
    else:
      if len (a) == 4 :
          root_node = a[0]
          a =[[root_node , a[1] , a[3]] , [root_node,a[2]]]

      elif len(a) == 5 :
          root_node = a[0]
          a = [[root_node, a[1], a[3]], [root_node, a[2]],
               [root_node,a[1],a[4]]]

      elif len(a) == 6 :
          root_node = a[0]
          a = [[root_node, a[1], a[3]], [root_node, a[2],a[5]],
               [root_node, a[1], a[4]]]

      elif len(a) == 7 :
          root_node = a[0]
          a = [[root_node, a[1], a[3]], [root_node, a[2], a[5]],
               [root_node, a[1], a[4]],[root_node,a[2],a[6]]]

      elif len(a) == 8 :
          root_node = a[0]
          a = [[root_node, a[1], a[3],a[7]], [root_node, a[2], a[5]],
               [root_node, a[1], a[4]],[root_node,a[2],a[6]]]

      elif len(a) == 9 :
          root_node = a[0]
          a = [[root_node, a[1], a[3],a[7]],[root_node, a[1], a[3],a[8]], [root_node, a[2], a[5]],
               [root_node, a[1], a[4]],[root_node,a[2],a[6]]]

      elif len(a) == 10 :
          root_node = a[0]
          a = [[root_node, a[1], a[3],a[7]],[root_node, a[1], a[3],a[8]], [root_node, a[2], a[5]],
               [root_node, a[1], a[4],a[9]],[root_node,a[2],a[6]]]

      elif len(a) == 11 :
          root_node = a[0]
          a = [[root_node, a[1], a[3],a[7]],[root_node, a[1], a[3],a[8]], [root_node, a[2], a[5]],
               [root_node, a[1], a[4],a[9]],[root_node, a[1], a[4],a[10]],[root_node,a[2],a[6]]]

      elif len(a) == 12 :
          root_node = a[0]
          a = [[root_node, a[1], a[3],a[7]],[root_node, a[1], a[3],a[8]], [root_node, a[2], a[5],a[11]],
               [root_node, a[1], a[4],a[9]],[root_node, a[1], a[4],a[10]],[root_node,a[2],a[6]]]

      elif len(a) == 13 :
          root_node = a[0]
          a = [[root_node, a[1], a[3],a[7]],[root_node, a[1], a[3],a[8]],
               [root_node, a[2], a[5],a[11]],
               [root_node, a[2], a[5], a[12]], [root_node, a[1], a[4],a[9]]
               ,[root_node, a[1], a[4],a[10]],[root_node,a[2],a[6]]]

      elif len(a) == 14 :
          root_node = a[0]
          a = [[root_node, a[1], a[3],a[7]],[root_node, a[1], a[3],a[8]],
               [root_node, a[2], a[5],a[11]],
               [root_node, a[2], a[5], a[12]], [root_node, a[1], a[4],a[9]]
               ,[root_node, a[1], a[4],a[10]],[root_node,a[2],a[6],a[13]]]

      elif len(a) == 15 :
          root_node = a[0]
          a = [[root_node, a[1], a[3],a[7]],[root_node, a[1], a[3],a[8]],
               [root_node, a[2], a[5],a[11]],
               [root_node, a[2], a[5], a[12]], [root_node, a[1], a[4],a[9]]
               ,[root_node, a[1], a[4],a[10]],[root_node,a[2],a[6],a[13]],[root_node,a[2],a[6],a[14]]]

      elif len(a) == 16 :
          root_node = a[0]
          a = [[root_node, a[1], a[3], a[7], a[15]], [root_node, a[1], a[3], a[8], a[15]],
               [root_node, a[1], a[3], a[8]], [root_node, a[2], a[5], a[11], a[16]],
               [root_node, a[2], a[5], a[12], a[16]], [root_node, a[1], a[4], a[9], a[16]]
              , [root_node, a[1], a[4], a[10], a[15]], [root_node, a[2], a[6], a[13]],
               [root_node, a[2], a[6], a[14]]]

      elif len(a) == 17 :
          root_node = a[0]
          a = [[root_node, a[1], a[3], a[7], a[15]], [root_node, a[1], a[3], a[8], a[15]],
               [root_node, a[1], a[3], a[8]], [root_node, a[2], a[5], a[11], a[16]],
               [root_node, a[2], a[5], a[12], a[16]], [root_node, a[1], a[4], a[9], a[16]]
              , [root_node, a[1], a[4], a[10], a[15]], [root_node, a[2], a[6], a[13]],
               [root_node, a[2], a[6], a[14]]]

      elif len(a) == 18 :
          root_node = a[0]
          a = [[root_node, a[1], a[3],a[7],a[15]],[root_node, a[1], a[3],a[8],a[15]],
               [root_node,a[1], a[3],a[8]],[root_node, a[2], a[5],a[11],a[16]],
               [root_node, a[2], a[5], a[12],a[16]], [root_node, a[1], a[4],a[9],a[16]]
               ,[root_node, a[1], a[4],a[10],a[15]],[root_node,a[2],a[6],a[13],a[17]],
               [root_node,a[2],a[6],a[14],a[17]]]

      elif len(a) == 19:
          root_node = a[0]
          a = [[root_node, a[1], a[3], a[7], a[15]], [root_node, a[1], a[3], a[8], a[15]],
               [root_node, a[1], a[3],a[18]],
               [root_node, a[1], a[3], a[8]], [root_node, a[2], a[5], a[11], a[16],a[18]],
               [root_node, a[2], a[5], a[12], a[16],a[18]], [root_node, a[1], a[4], a[9], a[16],a[18]]
              , [root_node, a[1], a[4], a[10], a[15]], [root_node, a[2], a[6], a[13], a[17]],
               [root_node, a[2], a[6], a[13], a[18]],[root_node, a[2], a[6], a[14], a[17]]]

    with open(fm, 'a') as f:
        f.write('Molecular graph :')
        f.write('\n')
        f.write(str(a))
        f.write('\n-------------------------------------------------------------------')
        f.write('\n')

def Gaussian (a , b=str) :

  ff = 'C:/Users/Naweed/PycharmProjects/IHHO/Graphs/Gaussian graph.txt'

  if len (a) > 14 or len(a) < 4 :

      print('!! List lengh must be !! ', '\nhigher than 4 or equal 4 \nand lower than 14 or equal 14')
  else:
        if len(a) == 4 :
            root_node = a[0]
            a = [[root_node,a[1]],[root_node,a[2]],
                 [root_node,a[3]]]

        if len(a) == 5:
            root_node = a[0]
            a = [[root_node, a[1]], [root_node, a[2]],
                 [root_node, a[3]],[root_node,a[4]]]

        if len(a) == 6:
            root_node = a[0]
            a = [[root_node, a[1],a[5]], [root_node, a[2]],
                 [root_node, a[3]], [root_node, a[4]]]

        if len(a) == 7:
            root_node = a[0]
            a = [[root_node, a[1],a[5],a[6]], [root_node, a[2],a[6]],
                 [root_node, a[3]], [root_node, a[4]]]

        if len(a) == 8:
            root_node = a[0]
            a = [[root_node, a[1],a[5],a[6]],[root_node, a[1],a[5],a[7]],
                 [root_node, a[2],a[6]],[root_node, a[3],a[7]],
                 [root_node, a[4]]]

        if len(a) == 9:
            root_node = a[0]
            a = [[root_node, a[1], a[5], a[6]], [root_node, a[1], a[5], a[7]],
                 [root_node, a[1], a[5], a[8]],[root_node, a[2],a[6]],
                 [root_node, a[3],a[7]], [root_node, a[4],a[8]]]

        if len(a) == 10:
            root_node = a[0]
            a = [[root_node, a[1], a[5], a[6],a[9]], [root_node, a[1], a[5], a[7]],
                 [root_node, a[1], a[5], a[8]],[root_node, a[2],a[6],a[9]],
                 [root_node, a[3],a[7]], [root_node, a[4],a[8]]]

        if len(a) == 11:
            root_node = a[0]
            a = [[root_node, a[1], a[5], a[6],a[9],a[10]], [root_node, a[1], a[5], a[7]],
                 [root_node, a[1], a[5], a[8]],[root_node, a[2],a[6],a[9],a[10]],
                 [root_node, a[3],a[7],a[10]], [root_node, a[4],a[8]]]

        if len(a) == 12:
            root_node = a[0]
            a = [[root_node, a[1], a[5], a[6],a[9],a[10]],[root_node, a[1], a[5], a[6],a[9],a[11]],
                 [root_node, a[1], a[5], a[7]],
                 [root_node, a[1], a[5], a[8]],[root_node, a[2], a[6],a[9],a[10]],
                 [root_node, a[3],a[7],a[10]], [root_node, a[4],a[8],a[11]]]

        if len(a) == 13:
            root_node = a[0]
            a = [[root_node, a[1], a[5], a[6], a[9], a[10],a[12]],
                 [root_node, a[1], a[5], a[7]], [root_node, a[1], a[5], a[6], a[9], a[11]],
                 [root_node, a[1], a[5], a[8]], [root_node, a[2], a[6],a[9],a[10],a[12]],
                 [root_node, a[3], a[7], a[10],a[12]], [root_node, a[4], a[8], a[11]]]

        if len(a) == 14:
            root_node = a[0]
            a = [[root_node, a[1], a[5], a[6], a[9], a[10],a[12],a[13]],
                 [root_node, a[1], a[5], a[7]], [root_node, a[1], a[5], a[6], a[9], a[11]],
                 [root_node, a[1], a[5], a[8]], [root_node, a[2], a[6],a[9],a[10],a[12],a[13]],
                 [root_node, a[3], a[7], a[10],a[12],a[13]], [root_node, a[4], a[8], a[11],a[13]]]


  with open(ff, 'a') as f:
      f.write('Gaussian graph :')
      f.write('-->')
      f.write(b)
      f.write('\n')
      f.write(str(a))
      f.write('\n-------------------------------------------------------------------')
      f.write('\n')

def Gaussian_h () :
  t1 = np.random.randint(30, size=(10))
  a=t1
  ff = 'C:/Users/Naweed/PycharmProjects/IHHO/HEFT Metrics/Heft Cpop Gaussian graph.txt'

  if len (a) > 14 or len(a) < 4 :

      print('!! List lengh must be !! ', '\nhigher than 4 or equal 4 \nand lower than 14 or equal 14')
  else:
        if len(a) == 4 :
            root_node = a[0]
            a = [[root_node,a[1]],[root_node,a[2]],
                 [root_node,a[3]]]

        if len(a) == 5:
            root_node = a[0]
            a = [[root_node, a[1]], [root_node, a[2]],
                 [root_node, a[3]],[root_node,a[4]]]

        if len(a) == 6:
            root_node = a[0]
            a = [[root_node, a[1],a[5]], [root_node, a[2]],
                 [root_node, a[3]], [root_node, a[4]]]

        if len(a) == 7:
            root_node = a[0]
            a = [[root_node, a[1],a[5],a[6]], [root_node, a[2],a[6]],
                 [root_node, a[3]], [root_node, a[4]]]

        if len(a) == 8:
            root_node = a[0]
            a = [[root_node, a[1],a[5],a[6]],[root_node, a[1],a[5],a[7]],
                 [root_node, a[2],a[6]],[root_node, a[3],a[7]],
                 [root_node, a[4]]]

        if len(a) == 9:
            root_node = a[0]
            a = [[root_node, a[1], a[5], a[6]], [root_node, a[1], a[5], a[7]],
                 [root_node, a[1], a[5], a[8]],[root_node, a[2],a[6]],
                 [root_node, a[3],a[7]], [root_node, a[4],a[8]]]

        if len(a) == 10:
            root_node = a[0]
            a = [[root_node, a[1], a[5], a[6],a[9]], [root_node, a[1], a[5], a[7]],
                 [root_node, a[1], a[5], a[8]],[root_node, a[2],a[6],a[9]],
                 [root_node, a[3],a[7]], [root_node, a[4],a[8]]]

        if len(a) == 11:
            root_node = a[0]
            a = [[root_node, a[1], a[5], a[6],a[9],a[10]], [root_node, a[1], a[5], a[7]],
                 [root_node, a[1], a[5], a[8]],[root_node, a[2],a[6],a[9],a[10]],
                 [root_node, a[3],a[7],a[10]], [root_node, a[4],a[8]]]

        if len(a) == 12:
            root_node = a[0]
            a = [[root_node, a[1], a[5], a[6],a[9],a[10]],[root_node, a[1], a[5], a[6],a[9],a[11]],
                 [root_node, a[1], a[5], a[7]],
                 [root_node, a[1], a[5], a[8]],[root_node, a[2], a[6],a[9],a[10]],
                 [root_node, a[3],a[7],a[10]], [root_node, a[4],a[8],a[11]]]

        if len(a) == 13:
            root_node = a[0]
            a = [[root_node, a[1], a[5], a[6], a[9], a[10],a[12]],
                 [root_node, a[1], a[5], a[7]], [root_node, a[1], a[5], a[6], a[9], a[11]],
                 [root_node, a[1], a[5], a[8]], [root_node, a[2], a[6],a[9],a[10],a[12]],
                 [root_node, a[3], a[7], a[10],a[12]], [root_node, a[4], a[8], a[11]]]

        if len(a) == 14:
            root_node = a[0]
            a = [[root_node, a[1], a[5], a[6], a[9], a[10],a[12],a[13]],
                 [root_node, a[1], a[5], a[7]], [root_node, a[1], a[5], a[6], a[9], a[11]],
                 [root_node, a[1], a[5], a[8]], [root_node, a[2], a[6],a[9],a[10],a[12],a[13]],
                 [root_node, a[3], a[7], a[10],a[12],a[13]], [root_node, a[4], a[8], a[11],a[13]]]


  with open(ff, 'a') as f:
      f.write('Gaussian graph :')
      f.write('\n')
      f.write(str(a))
      f.write('\n-------------------------------------------------------------------')
      f.write('\n')


def FFT (a,b=str):

    fq = 'C:/Users/Naweed/PycharmProjects/IHHO/Graphs/FFT graph.txt'

    if len(a) > 15 or len(a) < 4:
        print('!! List lengh must be !! ', '\nhigher than 4 or equal 4 \nand lower than 15 or equal 15')
    else:

        if len(a) == 4 :
            root_node = a[0]
            a = [[root_node,a[1],a[3]],[root_node,a[2]]]

        elif len(a) == 5 :
            root_node = a[0]
            a = [[root_node, a[1], a[3]],[root_node, a[1], a[4]],
                 [root_node, a[2]]]

        elif len(a) == 6 :
            root_node = a[0]
            a = [[root_node, a[1], a[3]],[root_node, a[1], a[4]],
                 [root_node, a[2],a[5]]]

        elif len(a) == 7 :
            root_node = a[0]
            a = [[root_node, a[1], a[3]],[root_node, a[1], a[4]],
                 [root_node, a[2],a[5]],[root_node, a[2],a[6]]]

        elif len(a) == 8 :
            root_node = a[0]
            a = [[root_node, a[1], a[3],a[7]],[root_node, a[1], a[4],a[7]],
                 [root_node, a[2],a[5]],[root_node, a[2],a[6]]]

        elif len(a) == 9 :
            root_node = a[0]
            a = [[root_node, a[1], a[3],a[7]],[root_node, a[1], a[3],a[8]],
                 [root_node, a[1], a[4],a[7]],[root_node, a[1], a[4],a[8]],
                 [root_node, a[2],a[5]],[root_node, a[2],a[6]]]

        elif len(a) == 10 :
            root_node = a[0]
            a = [[root_node, a[1], a[3],a[7]],[root_node, a[1], a[3],a[8]],
                 [root_node, a[1], a[4],a[7]],[root_node, a[1], a[4],a[8]],
                 [root_node, a[2],a[5],a[9]],[root_node, a[2],a[6],a[9]]]

        elif len(a) == 11 :
            root_node = a[0]
            a = [[root_node, a[1], a[3],a[7]],[root_node, a[1], a[3],a[8]],
                 [root_node, a[1], a[4],a[7]],[root_node, a[1], a[4],a[8]],
                 [root_node, a[2],a[5],a[9]],[root_node, a[2],a[6],a[9]],
                 [root_node, a[2],a[6],a[10]],[root_node, a[2],a[5],a[10]]]

        elif len(a) == 12 :
            root_node = a[0]
            a = [[root_node, a[1], a[3],a[7],a[11]],[root_node, a[1], a[3],a[8]],
                 [root_node, a[1], a[4],a[7],a[11]],[root_node, a[1], a[4],a[8]],
                 [root_node, a[2],a[5],a[9],a[11]],[root_node, a[2],a[6],a[9],a[11]],
                 [root_node, a[2],a[6],a[10]],[root_node, a[2],a[5],a[10]]]

        elif len(a) == 13 :
            root_node = a[0]
            a = [[root_node, a[1], a[3], a[7], a[11]], [root_node, a[1], a[3], a[8],a[12]],
                 [root_node, a[1], a[4], a[7], a[11]], [root_node, a[1], a[4], a[8],a[12]],
                 [root_node, a[2], a[5], a[9], a[11]], [root_node, a[2], a[6], a[9], a[11]],
                 [root_node, a[2], a[6], a[10],a[12]], [root_node, a[2], a[5], a[10],a[12]]]

        elif len(a) == 14 :
            root_node = a[0]
            a = [[root_node, a[1], a[3], a[7], a[11]], [root_node, a[1], a[3], a[8],a[12]],
                 [root_node, a[1], a[4], a[7], a[11]], [root_node, a[1], a[4], a[8],a[12]],
                 [root_node, a[2], a[5], a[9], a[11]],[root_node, a[2], a[5], a[9], a[13]]
                , [root_node, a[2], a[6], a[9], a[11]],[root_node, a[2], a[6], a[9], a[13]],
                 [[root_node, a[1], a[3], a[7], a[13]],
                 [root_node, a[2], a[6], a[10],a[12]], [root_node, a[2], a[5], a[10],a[12]]]]

        elif len(a) == 15:
            root_node = a[0]
            a = [[root_node, a[1], a[3], a[7], a[11]], [root_node, a[1], a[3], a[8], a[12]],
                 [root_node, a[1], a[3], a[8], a[14]] , [root_node, a[1], a[4], a[8], a[14]],
                 [root_node, a[1], a[4], a[7], a[11]], [root_node, a[1], a[4], a[8], a[12]],
                 [root_node, a[2], a[5], a[9], a[11]], [root_node, a[2], a[5], a[9], a[13]]
                , [root_node, a[2], a[6], a[9], a[11]], [root_node, a[2], a[6], a[9], a[13]],
                 [[root_node, a[1], a[3], a[7], a[13]], root_node, a[2], a[6], a[10], a[14]],
                  [root_node, a[2], a[6], a[10], a[12]], [root_node, a[2], a[5], a[10], a[12]],
                 [root_node, a[2], a[5], a[10], a[14]]]

    with open(fq, 'a') as f:
        f.write('FFT graph :')
        f.write('-->')
        f.write(b)
        f.write('\n')
        f.write(str(a))
        f.write('\n-------------------------------------------------------------------')
        f.write('\n')

def FFT_h ():
    t1 = np.random.randint(30, size=(10))
    a=t1
    fq = 'C:/Users/Naweed/PycharmProjects/IHHO/HEFT Metrics/Heft Cpop FFT graph.txt'

    if len(a) > 15 or len(a) < 4:
        print('!! List lengh must be !! ', '\nhigher than 4 or equal 4 \nand lower than 15 or equal 15')
    else:

        if len(a) == 4 :
            root_node = a[0]
            a = [[root_node,a[1],a[3]],[root_node,a[2]]]

        elif len(a) == 5 :
            root_node = a[0]
            a = [[root_node, a[1], a[3]],[root_node, a[1], a[4]],
                 [root_node, a[2]]]

        elif len(a) == 6 :
            root_node = a[0]
            a = [[root_node, a[1], a[3]],[root_node, a[1], a[4]],
                 [root_node, a[2],a[5]]]

        elif len(a) == 7 :
            root_node = a[0]
            a = [[root_node, a[1], a[3]],[root_node, a[1], a[4]],
                 [root_node, a[2],a[5]],[root_node, a[2],a[6]]]

        elif len(a) == 8 :
            root_node = a[0]
            a = [[root_node, a[1], a[3],a[7]],[root_node, a[1], a[4],a[7]],
                 [root_node, a[2],a[5]],[root_node, a[2],a[6]]]

        elif len(a) == 9 :
            root_node = a[0]
            a = [[root_node, a[1], a[3],a[7]],[root_node, a[1], a[3],a[8]],
                 [root_node, a[1], a[4],a[7]],[root_node, a[1], a[4],a[8]],
                 [root_node, a[2],a[5]],[root_node, a[2],a[6]]]

        elif len(a) == 10 :
            root_node = a[0]
            a = [[root_node, a[1], a[3],a[7]],[root_node, a[1], a[3],a[8]],
                 [root_node, a[1], a[4],a[7]],[root_node, a[1], a[4],a[8]],
                 [root_node, a[2],a[5],a[9]],[root_node, a[2],a[6],a[9]]]

        elif len(a) == 11 :
            root_node = a[0]
            a = [[root_node, a[1], a[3],a[7]],[root_node, a[1], a[3],a[8]],
                 [root_node, a[1], a[4],a[7]],[root_node, a[1], a[4],a[8]],
                 [root_node, a[2],a[5],a[9]],[root_node, a[2],a[6],a[9]],
                 [root_node, a[2],a[6],a[10]],[root_node, a[2],a[5],a[10]]]

        elif len(a) == 12 :
            root_node = a[0]
            a = [[root_node, a[1], a[3],a[7],a[11]],[root_node, a[1], a[3],a[8]],
                 [root_node, a[1], a[4],a[7],a[11]],[root_node, a[1], a[4],a[8]],
                 [root_node, a[2],a[5],a[9],a[11]],[root_node, a[2],a[6],a[9],a[11]],
                 [root_node, a[2],a[6],a[10]],[root_node, a[2],a[5],a[10]]]

        elif len(a) == 13 :
            root_node = a[0]
            a = [[root_node, a[1], a[3], a[7], a[11]], [root_node, a[1], a[3], a[8],a[12]],
                 [root_node, a[1], a[4], a[7], a[11]], [root_node, a[1], a[4], a[8],a[12]],
                 [root_node, a[2], a[5], a[9], a[11]], [root_node, a[2], a[6], a[9], a[11]],
                 [root_node, a[2], a[6], a[10],a[12]], [root_node, a[2], a[5], a[10],a[12]]]

        elif len(a) == 14 :
            root_node = a[0]
            a = [[root_node, a[1], a[3], a[7], a[11]], [root_node, a[1], a[3], a[8],a[12]],
                 [root_node, a[1], a[4], a[7], a[11]], [root_node, a[1], a[4], a[8],a[12]],
                 [root_node, a[2], a[5], a[9], a[11]],[root_node, a[2], a[5], a[9], a[13]]
                , [root_node, a[2], a[6], a[9], a[11]],[root_node, a[2], a[6], a[9], a[13]],
                 [[root_node, a[1], a[3], a[7], a[13]],
                 [root_node, a[2], a[6], a[10],a[12]], [root_node, a[2], a[5], a[10],a[12]]]]

        elif len(a) == 15:
            root_node = a[0]
            a = [[root_node, a[1], a[3], a[7], a[11]], [root_node, a[1], a[3], a[8], a[12]],
                 [root_node, a[1], a[3], a[8], a[14]] , [root_node, a[1], a[4], a[8], a[14]],
                 [root_node, a[1], a[4], a[7], a[11]], [root_node, a[1], a[4], a[8], a[12]],
                 [root_node, a[2], a[5], a[9], a[11]], [root_node, a[2], a[5], a[9], a[13]]
                , [root_node, a[2], a[6], a[9], a[11]], [root_node, a[2], a[6], a[9], a[13]],
                 [[root_node, a[1], a[3], a[7], a[13]], root_node, a[2], a[6], a[10], a[14]],
                  [root_node, a[2], a[6], a[10], a[12]], [root_node, a[2], a[5], a[10], a[12]],
                 [root_node, a[2], a[5], a[10], a[14]]]

    with open(fq, 'a') as f:
        f.write('FFT graph :')
        f.write('\n')
        f.write(str(a))
        f.write('\n-------------------------------------------------------------------')
        f.write('\n')


def Graphs ():
    try :
        fq = 'C:/Users/Naweed/PycharmProjects/IHHO/HEFT Metrics/Heft Cpop FFT graph.txt'
        ff = 'C:/Users/Naweed/PycharmProjects/IHHO/HEFT Metrics/Heft Cpop Gaussian graph.txt'
        ft = 'C:/Users/Naweed/PycharmProjects/IHHO/Graphs/Molecular graph.txt'
        ft2 = 'C:/Users/Naweed/PycharmProjects/IHHO/Graphs/Gaussian graph.txt'
        ft3 = 'C:/Users/Naweed/PycharmProjects/IHHO/Graphs/FFT graph.txt'
        fm = 'C:/Users/Naweed/PycharmProjects/IHHO/HEFT Metrics/Heft Cpop Molecular Graph.txt'

        file_exists = exists(ft)
        file_exists2 = exists(ft2)
        file_exists3 = exists(ft3)

        with open(ft, 'r') as f:
            print(f.read())
        with open(ft2, 'r') as f:
            print(f.read())
        with open(ft3, 'r') as f:
            print(f.read())
        print('********** Heft-Cpop Graphs **********')
        with open(fm, 'r') as f:
            print(f.read())
        with open(ff, 'r') as f:
            print(f.read())
        with open(fq, 'r') as f:
            print(f.read())

    except FileNotFoundError :
            print('     *****************************************')
            print('     * At least 3 graphs must be generated ! *')
            print('     *****************************************')

def Metrics_cg (x=list) :
    try:
        if x[0:len(x)] == x[0:len(x)]:
            x[0].append(0)
        x = np.array(x,dtype=object)
        p = np.array([4,12,7])
        cpu_len = len(p)
        fastest_processor = max(p)
        MRP = random.randint(0,1)
        if MRP == 0:
            print('*** No need to Change CPU ***')
        else :
            print('*** CPU Changed ***')

        file_name = 'C:/Users/Naweed/PycharmProjects/IHHO/Cuckoo Genetic/Cuckoo Genetic Makespan.txt'
        file_name2 = 'C:/Users/Naweed/PycharmProjects/IHHO/Cuckoo Genetic/Cuckoo Genetic SLR.txt'
        file_name3 = 'C:/Users/Naweed/PycharmProjects/IHHO/Cuckoo Genetic/Cuckoo Genetic Speed up.txt'
        file_name4 = 'C:/Users/Naweed/PycharmProjects/IHHO/Cuckoo Genetic/Cuckoo Genetic CCR.txt'
        file_name5 = 'C:/Users/Naweed/PycharmProjects/IHHO/Cuckoo Genetic/Cuckoo Genetic Efficiency.txt'

        if len(x) == 3 :
            ms1 = np.round(x[0] / fastest_processor,2)
            ms2 = np.round(x[1] / fastest_processor,2)
            ms3 = np.round(x[2] / fastest_processor,2)
            run = [ms1,ms2,ms3]

            path = np.array([0.5, 0.1])
            path_sum = math.fsum(path)
            msm1 = np.round(x[0] / p[1], 2)
            msm2 = np.round(x[1] / p[1], 2)
            msm3 = np.round(x[2] / p[1], 2)

            task_min = [math.fsum(msm1), math.fsum(msm2),
                        math.fsum(msm3)]
            task_min = math.fsum(task_min)
            print('Tasks on fastest processor :', round(task_min, 2))
            cp_min = [max(msm1),max(msm2),max(msm3)]
            print('critical path on fastest cpu :',cp_min)
            cp_min = max(cp_min)
            print('makespan of cp on fastest cpu :',cp_min)
            cp = [max(ms1),max(ms2)+path[0],max(ms3)+path[1]]
            print('critical path :',cp)
            cp = max(cp)
            print('makespan of cp :', round(cp,2))
            print('\n----------------------------------')
            print('on p0=4:\n', ms1, '\non p1=12:\n', ms2, '\non p0=4:\n', ms3)
            print('\n----------------------------------------------------------------')
            makespan_cpus = [math.fsum(ms1),math.fsum(ms2)+path[0],
                             math.fsum(ms3)+path[1]]
            makespan = math.fsum(makespan_cpus)
            print('Makespan is :',round(makespan,2))

        if len(x) == 4 :
            ms1 = np.round(x[0] / fastest_processor,2)
            ms2 = np.round(x[1] / fastest_processor,2)
            ms3 = np.round(x[2] / fastest_processor,2)
            ms4 = np.round(x[3] / p[2],2)
            run = [ms1,ms2,ms3,ms4]

            path = np.array([0.5, 0.1, 1])
            path_sum = math.fsum(path)
            msm1 = np.round(x[0] / p[1], 2)
            msm2 = np.round(x[1] / p[1], 2)
            msm3 = np.round(x[2] / p[1], 2)
            msm4 = np.round(x[3] / p[1], 2)
            task_min = [math.fsum(msm1), math.fsum(msm2),
                        math.fsum(msm3), math.fsum(msm4)]
            task_min = math.fsum(task_min)
            print('Tasks on fastest processor :', round(task_min, 2))
            cp_min = [max(msm1),max(msm2),max(msm3),max(msm4)]
            print('critical path on fastest cpu :',cp_min)
            cp_min = max(cp_min)
            print('makespan of cp on fastest cpu :',cp_min)
            cp = [max(ms1),max(ms2)+path[0],max(ms3)+path[1],max(ms4)+path[2]]
            print('critical path :',cp)
            cp = max(cp)
            print('makespan of cp :', round(cp,2))
            print('\n----------------------------------')
            print('on p0=4:\n', ms1, '\non p1=12:\n', ms2, '\non p0=4:\n', ms3, '\non p2=7:\n', ms4)
            print('\n----------------------------------------------------------------')
            makespan_cpus = [math.fsum(ms1),math.fsum(ms2)+path[0],
                             math.fsum(ms3)+path[1],math.fsum(ms4)+path[2]]
            makespan = math.fsum(makespan_cpus)
            print('Makespan is :',round(makespan,2))

        elif len(x) == 5 :
            ms1 = np.round(x[0]/fastest_processor,2)
            ms2 = np.round(x[1] / p[1],2)
            ms3 = np.round(x[2] / fastest_processor,2)
            ms4 = np.round(x[3] / fastest_processor,2)
            ms5 = np.round(x[4] / p[1], 2)
            run = [ms1, ms2, ms3, ms4,ms5]
            path = np.array([0.5, 0.1, 1, 1.7])
            path_sum = math.fsum(path)
            msm1 = np.round(x[0] / p[1], 2)
            msm2 = np.round(x[1] / p[1], 2)
            msm3 = np.round(x[2] / p[1], 2)
            msm4 = np.round(x[3] / p[1], 2)
            msm5 = np.round(x[4] / p[1], 2)
            task_min = [math.fsum(msm1), math.fsum(msm2),
                        math.fsum(msm3), math.fsum(msm4), math.fsum(msm5)]
            task_min = math.fsum(task_min)
            print('Tasks on fastest processor :', round(task_min, 2))
            cp_min = [max(msm1), max(msm2), max(msm3), max(msm4),max(ms5)]
            print('critical path on fastest cpu :', cp_min)
            cp_min = max(cp_min)
            print('makespan of cp on fastest cpu :', cp_min)
            cp = [max(ms1),max(ms2)+path[0],max(ms3)+path[1],max(ms4)+path[2],max(ms5)+path[3]]
            print('critical path :', cp)
            cp = max(cp)
            print('makespan of cp :', round(cp,2))
            print('\n----------------------------------')
            print('on p0=4:\n', ms1, '\non p1=12:\n', ms2, '\non p0=4:\n', ms3, '\non p2=7:\n', ms4,'\non p1=12:\n', ms5)
            print('\n----------------------------------------------------------------')
            makespan_cpus = [math.fsum(ms1), math.fsum(ms2) + path[0],
                             math.fsum(ms3) + path[1], math.fsum(ms4) + path[2],math.fsum(ms5)+path[3]]
            makespan = math.fsum(makespan_cpus)
            print('Makespan is :',round(makespan,2))

        elif len(x) == 6:
            ms1 = np.round(x[0] / fastest_processor, 2)
            ms2 = np.round(x[1] / p[1], 2)
            ms3 = np.round(x[2] / fastest_processor, 2)
            ms4 = np.round(x[3] / fastest_processor, 2)
            ms5 = np.round(x[4] / p[1], 2)
            ms6 = np.round(x[5] / p[1], 2)
            run = [ms1, ms2, ms3, ms4, ms5,ms6]
            path = np.array([0.5, 0.1, 1, 1.7])
            path_sum = math.fsum(path)
            msm1 = np.round(x[0] / p[1], 2)
            msm2 = np.round(x[1] / p[1], 2)
            msm3 = np.round(x[2] / p[1], 2)
            msm4 = np.round(x[3] / p[1], 2)
            msm5 = np.round(x[4] / p[1], 2)
            msm6 = np.round(x[5] / p[1], 2)
            task_min = [math.fsum(msm1), math.fsum(msm2),
                        math.fsum(msm3), math.fsum(msm4), math.fsum(msm5), math.fsum(msm6)]
            task_min = math.fsum(task_min)
            print('Tasks on fastest processor :', round(task_min, 2))
            cp_min = [max(msm1), max(msm2), max(msm3), max(msm4), max(msm5),max(msm6)]
            print('critical path on fastest cpu :', cp_min)
            cp_min = max(cp_min)
            print('makespan of cp on fastest cpu :', cp_min)
            cp = [max(ms1), max(ms2) + path[0], max(ms3) + path[1],
                  max(ms4) + path[2], max(ms5) + path[3],max(ms6)]
            print('critical path :', cp)
            cp = max(cp)
            print('makespan of cp :', round(cp,2))
            print('\n----------------------------------')
            print('on p0=4:\n', ms1, '\non p1=12:\n', ms2, '\non p0=4:\n',
            ms3, '\non p2=7:\n', ms4, '\non p1=12:\n', ms5,'\non p1=12:\n', ms6)
            print('\n----------------------------------------------------------------')
            makespan_cpus = [math.fsum(ms1), math.fsum(ms2) + path[0],
                             math.fsum(ms3) + path[1], math.fsum(ms4) + path[2],
                             math.fsum(ms5) + path[3],math.fsum(ms6)]
            makespan = math.fsum(makespan_cpus)
            print('Makespan is :', round(makespan, 2))

        elif len(x) == 7:
            ms1 = np.round(x[0] / fastest_processor, 2)
            ms2 = np.round(x[1] / p[1], 2)
            ms3 = np.round(x[2] / fastest_processor, 2)
            ms4 = np.round(x[3] / fastest_processor, 2)
            ms5 = np.round(x[4] / p[1], 2)
            ms6 = np.round(x[5] / p[1], 2)
            ms7 = np.round(x[6] / fastest_processor, 2)
            run = [ms1, ms2, ms3, ms4, ms5, ms6,ms7]
            path = np.array([0.5, 0.1, 1, 1.7, 6.6])
            path_sum = math.fsum(path)
            msm1 = np.round(x[0] / p[1], 2)
            msm2 = np.round(x[1] / p[1], 2)
            msm3 = np.round(x[2] / p[1], 2)
            msm4 = np.round(x[3] / p[1], 2)
            msm5 = np.round(x[4] / p[1], 2)
            msm6 = np.round(x[5] / p[1], 2)
            msm7 = np.round(x[6] / p[1], 2)
            task_min = [math.fsum(msm1), math.fsum(msm2),
                        math.fsum(msm3), math.fsum(msm4), math.fsum(msm5), math.fsum(msm6), math.fsum(msm7)]
            task_min = math.fsum(task_min)
            print('Tasks on fastest processor :', round(task_min, 2))
            cp_min = [max(msm1), max(msm2), max(msm3), max(msm4), max(msm5), max(msm6),max(msm7)]
            print('critical path on fastest cpu :', cp_min)
            cp_min = max(cp_min)
            print('makespan of cp on fastest cpu :', cp_min)
            cp = [max(ms1), max(ms2) + path[0], max(ms3) + path[1],
                  max(ms4) + path[2], max(ms5) + path[3], max(ms6),max(ms7)+path[4]]
            print('critical path :', cp)
            cp = max(cp)
            print('makespan of cp :', round(cp,2))
            print('\n----------------------------------')
            print('on p0=4:\n', ms1, '\non p1=12:\n', ms2, '\non p0=4:\n',
            ms3, '\non p2=7:\n', ms4, '\non p1=12:\n', ms5,'\non p1=12:\n', ms6,'\non p1=12:\n', ms7)
            print('\n----------------------------------------------------------------')
            makespan_cpus = [math.fsum(ms1), math.fsum(ms2) + path[0],
                             math.fsum(ms3) + path[1], math.fsum(ms4) + path[2],
                             math.fsum(ms5) + path[3], math.fsum(ms6),math.fsum(ms7)+path[4]]
            makespan = math.fsum(makespan_cpus)
            print('Makespan is :', round(makespan, 2))

        elif len(x) == 8:
            ms1 = np.round(x[0] / fastest_processor, 2)
            ms2 = np.round(x[1] / p[1], 2)
            ms3 = np.round(x[2] / fastest_processor, 2)
            ms4 = np.round(x[3] / fastest_processor, 2)
            ms5 = np.round(x[4] / p[1], 2)
            ms6 = np.round(x[5] / p[1], 2)
            ms7 = np.round(x[6] / fastest_processor, 2)
            ms8 = np.round(x[7] / fastest_processor, 2)
            run = [ms1, ms2, ms3, ms4, ms5, ms6, ms7,ms8]
            path = np.array([0.5, 0.1, 1, 1.7, 6.6, 11.7])
            path_sum = math.fsum(path)
            msm1 = np.round(x[0] / p[1], 2)
            msm2 = np.round(x[1] / p[1], 2)
            msm3 = np.round(x[2] / p[1], 2)
            msm4 = np.round(x[3] / p[1], 2)
            msm5 = np.round(x[4] / p[1], 2)
            msm6 = np.round(x[5] / p[1], 2)
            msm7 = np.round(x[6] / p[1], 2)
            msm8 = np.round(x[7] / p[1], 2)
            task_min = [math.fsum(msm1), math.fsum(msm2),
                        math.fsum(msm3), math.fsum(msm4), math.fsum(msm5), math.fsum(msm6), math.fsum(msm7)
                , math.fsum(msm8)]
            task_min = math.fsum(task_min)
            print('Tasks on fastest processor :', round(task_min, 2))
            cp_min = [max(msm1), max(msm2), max(msm3), max(msm4), max(msm5), max(msm6), max(msm7),max(msm8)]
            print('critical path on fastest cpu :', cp_min)
            cp_min = max(cp_min)
            print('makespan of cp on fastest cpu :', cp_min)
            cp = [max(ms1), max(ms2) + path[0], max(ms3) + path[1],
                  max(ms4) + path[2], max(ms5) + path[3], max(ms6), max(ms7) + path[4],max(ms8)+path[5]]
            print('critical path :', cp)
            cp = max(cp)
            print('makespan of cp :', round(cp,2))
            print('\n----------------------------------')
            print('on p0=4:\n', ms1, '\non p1=12:\n', ms2, '\non p0=4:\n',
            ms3, '\non p2=7:\n', ms4, '\non p1=12:\n', ms5,'\non p1=12:\n', ms6,'\non p1=12:\n', ms7,
                  '\non p2=7:\n', ms8)
            print('\n----------------------------------------------------------------')
            makespan_cpus = [math.fsum(ms1), math.fsum(ms2) + path[0],
                             math.fsum(ms3) + path[1], math.fsum(ms4) + path[2],
                             math.fsum(ms5) + path[3], math.fsum(ms6), math.fsum(ms7) + path[4]
                ,math.fsum(ms8)+path[5]]
            makespan = math.fsum(makespan_cpus)
            print('Makespan is :', round(makespan, 2))

        elif len(x) == 9:
            ms1 = np.round(x[0] / fastest_processor, 2)
            ms2 = np.round(x[1] / fastest_processor, 2)
            ms3 = np.round(x[2] / fastest_processor, 2)
            ms4 = np.round(x[3] / fastest_processor, 2)
            ms5 = np.round(x[4] / p[1], 2)
            ms6 = np.round(x[5] / p[1], 2)
            ms7 = np.round(x[6] / fastest_processor, 2)
            ms8 = np.round(x[7] / p[2], 2)
            ms9 = np.round(x[8] / fastest_processor, 2)
            run = [ms1, ms2, ms3, ms4, ms5, ms6, ms7, ms8,ms9]
            path = np.array([0.5, 0.1, 1, 1.7, 6.6, 11.7, 13.3])
            path_sum = math.fsum(path)
            msm1 = np.round(x[0] / p[1], 2)
            msm2 = np.round(x[1] / p[1], 2)
            msm3 = np.round(x[2] / p[1], 2)
            msm4 = np.round(x[3] / p[1], 2)
            msm5 = np.round(x[4] / p[1], 2)
            msm6 = np.round(x[5] / p[1], 2)
            msm7 = np.round(x[6] / p[1], 2)
            msm8 = np.round(x[7] / p[1], 2)
            msm9 = np.round(x[8] / p[1], 2)
            task_min = [math.fsum(msm1), math.fsum(msm2),
                        math.fsum(msm3), math.fsum(msm4), math.fsum(msm5), math.fsum(msm6), math.fsum(msm7)
                , math.fsum(msm8), math.fsum(msm9)]
            task_min = math.fsum(task_min)
            print('Tasks on fastest processor :', round(task_min, 2))
            cp_min = [max(msm1), max(msm2), max(msm3), max(msm4), max(msm5),
                      max(msm6), max(msm7), max(msm8),max(msm9)]
            print('critical path on fastest cpu :', cp_min)
            cp_min = max(cp_min)
            print('makespan of cp on fastest cpu :', cp_min)
            cp = [max(ms1), max(ms2) + path[0], max(ms3) + path[1],
                  max(ms4) + path[2], max(ms5) + path[3], max(ms6),
                  max(ms7) + path[4], max(ms8) + path[5],max(ms9) + path[6]]
            print('critical path :', cp)
            cp = max(cp)
            print('makespan of cp :', round(cp,2))
            print('\n----------------------------------')
            print('on p0=4:\n', ms1, '\non p1=12:\n', ms2, '\non p0=4:\n',
                  ms3, '\non p2=7:\n', ms4, '\non p1=12:\n', ms5, '\non p1=12:\n', ms6, '\non p1=12:\n', ms7,
                  '\non p1=12:\n', ms8, '\non p1=12:\n', ms9)
            print('\n----------------------------------------------------------------')
            makespan_cpus = [math.fsum(ms1), math.fsum(ms2) + path[0],
                             math.fsum(ms3) + path[1], math.fsum(ms4) + path[2],
                             math.fsum(ms5) + path[3], math.fsum(ms6), math.fsum(ms7) + path[4]
                , math.fsum(ms8) + path[5], math.fsum(ms9)+path[6]]
            makespan = math.fsum(makespan_cpus)
            print('Makespan is :', round(makespan, 2))

        elif len(x) == 10:
            ms1 = np.round(x[0] / fastest_processor, 2)
            ms2 = np.round(x[1] / p[1], 2)
            ms3 = np.round(x[2] / fastest_processor, 2)
            ms4 = np.round(x[3] / fastest_processor, 2)
            ms5 = np.round(x[4] / p[1], 2)
            ms6 = np.round(x[5] / p[1], 2)
            ms7 = np.round(x[6] / fastest_processor, 2)
            ms8 = np.round(x[7] / p[2], 2)
            ms9 = np.round(x[8] / p[1], 2)
            ms10 = np.round(x[9] / fastest_processor, 2)
            run = [ms1, ms2, ms3, ms4, ms5, ms6, ms7, ms8, ms9,ms10]
            path = np.array([0.5, 0.1, 1, 1.7, 6.6, 11.7, 13.3, 14.79])
            path_sum = math.fsum(path)
            msm1 = np.round(x[0] / p[1], 2)
            msm2 = np.round(x[1] / p[1], 2)
            msm3 = np.round(x[2] / p[1], 2)
            msm4 = np.round(x[3] / p[1], 2)
            msm5 = np.round(x[4] / p[1], 2)
            msm6 = np.round(x[5] / p[1], 2)
            msm7 = np.round(x[6] / p[1], 2)
            msm8 = np.round(x[7] / p[1], 2)
            msm9 = np.round(x[8] / p[1], 2)
            msm10 = np.round(x[9] / p[1], 2)
            task_min = [math.fsum(msm1), math.fsum(msm2),
                        math.fsum(msm3), math.fsum(msm4), math.fsum(msm5), math.fsum(msm6), math.fsum(msm7)
                , math.fsum(msm8), math.fsum(msm9), math.fsum(msm10)]
            task_min = math.fsum(task_min)
            print('Tasks on fastest processor :', round(task_min, 2))
            cp_min = [max(msm1), max(msm2), max(msm3), max(msm4), max(msm5),
                      max(msm6), max(msm7), max(msm8), max(msm9),max(msm10)]
            print('critical path on fastest cpu :', cp_min)
            cp_min = max(cp_min)
            print('makespan of cp on fastest cpu :', cp_min)
            cp = [max(ms1), max(ms2) + path[0], max(ms3) + path[1],
                  max(ms4) + path[2], max(ms5) + path[3], max(ms6),
                  max(ms7) + path[4], max(ms8) + path[5], max(ms9) + path[6],max(ms10)+path[7]]
            print('critical path :', cp)
            cp = max(cp)
            print('makespan of cp :', round(cp,2))
            print('\n----------------------------------')
            print('on p0=4:\n', ms1, '\non p1=12:\n', ms2, '\non p0=4:\n',
                  ms3, '\non p2=7:\n', ms4, '\non p1=12:\n', ms5, '\non p1=12:\n', ms6, '\non p1=12:\n', ms7,
                  '\non p1=12:\n', ms8,'\non p1=12:\n', ms9,'\non p0=4:\n', ms10)
            print('\n----------------------------------------------------------------')
            makespan_cpus = [math.fsum(ms1), math.fsum(ms2) + path[0],
                             math.fsum(ms3) + path[1], math.fsum(ms4) + path[2],
                             math.fsum(ms5) + path[3], math.fsum(ms6), math.fsum(ms7) + path[4]
                , math.fsum(ms8) + path[5], math.fsum(ms9) + path[6], math.fsum(ms10)+path[7]]
            makespan = math.fsum(makespan_cpus)
            print('Makespan is :', round(makespan, 2))

        elif len(x) == 11:
            ms1 = np.round(x[0] / fastest_processor, 2)
            ms2 = np.round(x[1] / p[1], 2)
            ms3 = np.round(x[2] / fastest_processor, 2)
            ms4 = np.round(x[3] / fastest_processor, 2)
            ms5 = np.round(x[4] / p[1], 2)
            ms6 = np.round(x[5] / p[1], 2)
            ms7 = np.round(x[6] / fastest_processor, 2)
            ms8 = np.round(x[7] / fastest_processor, 2)
            ms9 = np.round(x[8] / p[1], 2)
            ms10 = np.round(x[9] / p[0], 2)
            ms11 = np.round(x[10] / fastest_processor, 2)
            run = [ms1, ms2, ms3, ms4, ms5, ms6, ms7, ms8, ms9, ms10,ms11]
            path = np.array([0.5, 0.1, 1, 1.7, 6.6, 11.7, 13.3, 14.79])
            path_sum = math.fsum(path)
            msm1 = np.round(x[0] / p[1], 2)
            msm2 = np.round(x[1] / p[1], 2)
            msm3 = np.round(x[2] / p[1], 2)
            msm4 = np.round(x[3] / p[1], 2)
            msm5 = np.round(x[4] / p[1], 2)
            msm6 = np.round(x[5] / p[1], 2)
            msm7 = np.round(x[6] / p[1], 2)
            msm8 = np.round(x[7] / p[1], 2)
            msm9 = np.round(x[8] / p[1], 2)
            msm10 = np.round(x[9] / p[1], 2)
            msm11 = np.round(x[10] / p[1], 2)
            task_min = [math.fsum(msm1), math.fsum(msm2),
                        math.fsum(msm3), math.fsum(msm4), math.fsum(msm5), math.fsum(msm6), math.fsum(msm7)
                , math.fsum(msm8), math.fsum(msm9), math.fsum(msm10), math.fsum(msm11)]
            task_min = math.fsum(task_min)
            print('Tasks on fastest processor :', round(task_min, 2))
            cp_min = [max(msm1), max(msm2), max(msm3), max(msm4), max(msm5),
                      max(msm6), max(msm7), max(msm8), max(msm9), max(msm10),max(msm11)]
            print('critical path on fastest cpu :', cp_min)
            cp_min = max(cp_min)
            print('makespan of cp on fastest cpu :', cp_min)
            cp = [max(ms1), max(ms2) + path[0], max(ms3) + path[1],
                  max(ms4) + path[2], max(ms5) + path[3], max(ms6),
                  max(ms7) + path[4], max(ms8) + path[5], max(ms9) + path[6], max(ms10) + path[7],max(ms11)]
            print('critical path :', cp)
            cp = max(cp)
            print('makespan of cp :', round(cp,2))
            print('\n----------------------------------')
            print('on p0=4:\n', ms1, '\non p1=12:\n', ms2, '\non p0=4:\n',
                  ms3, '\non p2=7:\n', ms4, '\non p1=12:\n', ms5, '\non p1=12:\n', ms6, '\non p1=12:\n', ms7,
                  '\non p1=12:\n', ms8,'\non p1=12:\n', ms9,'\non p0=4:\n', ms10,'\non p0=4:\n', ms11)
            print('\n----------------------------------------------------------------')
            makespan_cpus = [math.fsum(ms1), math.fsum(ms2) + path[0],
                             math.fsum(ms3) + path[1], math.fsum(ms4) + path[2],
                             math.fsum(ms5) + path[3], math.fsum(ms6), math.fsum(ms7) + path[4]
                , math.fsum(ms8) + path[5], math.fsum(ms9) + path[6],
                             math.fsum(ms10) + path[7], math.fsum(ms11)]
            makespan = math.fsum(makespan_cpus)
            print('Makespan is :', round(makespan, 2))

        elif len(x) == 12:
            ms1 = np.round(x[0] / fastest_processor, 2)
            ms2 = np.round(x[1] / fastest_processor, 2)
            ms3 = np.round(x[2] / fastest_processor, 2)
            ms4 = np.round(x[3] / fastest_processor, 2)
            ms5 = np.round(x[4] / p[1], 2)
            ms6 = np.round(x[5] / p[1], 2)
            ms7 = np.round(x[6] / fastest_processor, 2)
            ms8 = np.round(x[7] / fastest_processor, 2)
            ms9 = np.round(x[8] / p[1], 2)
            ms10 = np.round(x[9] / p[0], 2)
            ms11 = np.round(x[10] / fastest_processor, 2)
            ms12 = np.round(x[11] / p[1], 2)
            run = [ms1, ms2, ms3, ms4, ms5, ms6,
                   ms7, ms8, ms9, ms10, ms11,ms12]
            path = np.array([0.5, 0.1, 1, 1.7, 6.6, 11.7, 13.3, 14.79, 18.4])
            path_sum = math.fsum(path)
            msm1 = np.round(x[0] / p[1], 2)
            msm2 = np.round(x[1] / p[1], 2)
            msm3 = np.round(x[2] / p[1], 2)
            msm4 = np.round(x[3] / p[1], 2)
            msm5 = np.round(x[4] / p[1], 2)
            msm6 = np.round(x[5] / p[1], 2)
            msm7 = np.round(x[6] / p[1], 2)
            msm8 = np.round(x[7] / p[1], 2)
            msm9 = np.round(x[8] / p[1], 2)
            msm10 = np.round(x[9] / p[1], 2)
            msm11 = np.round(x[10] / p[1], 2)
            msm12 = np.round(x[11] / p[1], 2)
            task_min = [math.fsum(msm1), math.fsum(msm2),
                        math.fsum(msm3), math.fsum(msm4), math.fsum(msm5), math.fsum(msm6), math.fsum(msm7)
                , math.fsum(msm8), math.fsum(msm9), math.fsum(msm10), math.fsum(msm11),
                        math.fsum(msm12)]
            task_min = math.fsum(task_min)
            print('Tasks on fastest processor :', round(task_min, 2))
            cp_min = [max(msm1), max(msm2), max(msm3), max(msm4), max(msm5),
                      max(msm6), max(msm7), max(msm8), max(msm9), max(msm10), max(msm11),max(msm12)]
            print('critical path on fastest cpu :', cp_min)
            cp_min = max(cp_min)
            print('makespan of cp on fastest cpu :', cp_min)
            cp = [max(ms1), max(ms2) + path[0], max(ms3) + path[1],
                  max(ms4) + path[2], max(ms5) + path[3], max(ms6),
                  max(ms7) + path[4], max(ms8) + path[5], max(ms9) + path[6],
                  max(ms10) + path[7], max(ms11),max(ms12)+path[8]]
            print('critical path :', cp)
            cp = max(cp)
            print('makespan of cp :', round(cp,2))
            print('\n----------------------------------')
            print('on p0=4:\n', ms1, '\non p1=12:\n', ms2, '\non p0=4:\n',
                  ms3, '\non p2=7:\n', ms4, '\non p1=12:\n', ms5, '\non p1=12:\n', ms6, '\non p1=12:\n', ms7,
                  '\non p1=12:\n', ms8,'\non p1=12:\n', ms9,'\non p0=4:\n', ms10,'\non p0=4:\n',
                  ms11,'\non p1=12:\n', ms12)
            print('\n----------------------------------------------------------------')
            makespan_cpus = [math.fsum(ms1), math.fsum(ms2) + path[0],
                             math.fsum(ms3) + path[1], math.fsum(ms4) + path[2],
                             math.fsum(ms5) + path[3], math.fsum(ms6), math.fsum(ms7) + path[4]
                , math.fsum(ms8) + path[5], math.fsum(ms9) + path[6],
                             math.fsum(ms10) + path[7], math.fsum(ms12)+path[8]]
            makespan = math.fsum(makespan_cpus)
            print('Makespan is :', round(makespan, 2))

        elif len(x) == 13:
            ms1 = np.round(x[0] / fastest_processor, 2)
            ms2 = np.round(x[1] / p[1], 2)
            ms3 = np.round(x[2] / fastest_processor, 2)
            ms4 = np.round(x[3] / fastest_processor, 2)
            ms5 = np.round(x[4] / p[1], 2)
            ms6 = np.round(x[5] / p[1], 2)
            ms7 = np.round(x[6] / p[0], 2)
            ms8 = np.round(x[7] / fastest_processor, 2)
            ms9 = np.round(x[8] / p[1], 2)
            ms10 = np.round(x[9] / fastest_processor, 2)
            ms11 = np.round(x[10] / fastest_processor, 2)
            ms12 = np.round(x[11] / p[1], 2)
            ms13 = np.round(x[12] / p[1], 2)
            run = [ms1, ms2, ms3, ms4, ms5, ms6,
                   ms7, ms8, ms9, ms10, ms11, ms12,ms13]
            path = np.array([0.5, 0.1, 1, 1.7, 6.6, 11.7, 13.3, 14.79, 18.4])
            path_sum = math.fsum(path)
            msm1 = np.round(x[0] / p[1], 2)
            msm2 = np.round(x[1] / p[1], 2)
            msm3 = np.round(x[2] / p[1], 2)
            msm4 = np.round(x[3] / p[1], 2)
            msm5 = np.round(x[4] / p[1], 2)
            msm6 = np.round(x[5] / p[1], 2)
            msm7 = np.round(x[6] / p[1], 2)
            msm8 = np.round(x[7] / p[1], 2)
            msm9 = np.round(x[8] / p[1], 2)
            msm10 = np.round(x[9] / p[1], 2)
            msm11 = np.round(x[10] / p[1], 2)
            msm12 = np.round(x[11] / p[1], 2)
            msm13 = np.round(x[12] / p[1], 2)
            task_min = [math.fsum(msm1), math.fsum(msm2),
                        math.fsum(msm3), math.fsum(msm4), math.fsum(msm5), math.fsum(msm6), math.fsum(msm7)
                , math.fsum(msm8), math.fsum(msm9), math.fsum(msm10), math.fsum(msm11),
                        math.fsum(msm12), math.fsum(msm13)]
            task_min = math.fsum(task_min)
            print('Tasks on fastest processor :', round(task_min, 2))
            cp_min = [max(msm1), max(msm2), max(msm3), max(msm4), max(msm5),
                      max(msm6), max(msm7), max(msm8), max(msm9),
                      max(msm10), max(msm11), max(msm12),max(msm13)]
            print('critical path on fastest cpu :', cp_min)
            cp_min = max(cp_min)
            print('makespan of cp on fastest cpu :', cp_min)
            cp = [max(ms1), max(ms2) + path[0], max(ms3) + path[1],
                  max(ms4) + path[2], max(ms5) + path[3], max(ms6),
                  max(ms7) + path[4], max(ms8) + path[5], max(ms9) + path[6],
                  max(ms10) + path[7], max(ms11), max(ms12) + path[8],max(ms13)]
            print('critical path :', cp)
            cp = max(cp)
            print('makespan of cp :', round(cp,2))
            print('\n----------------------------------')
            print('on p0=4:\n', ms1, '\non p1=12:\n', ms2, '\non p0=4:\n',
                  ms3, '\non p2=7:\n', ms4, '\non p1=12:\n', ms5, '\non p1=12:\n', ms6, '\non p1=12:\n', ms7,
                  '\non p1=12:\n', ms8, '\non p1=12:\n', ms9, '\non p0=4:\n', ms10, '\non p0=4:\n',
                  ms11, '\non p0=4:\n', ms12, '\non p1=12:\n', ms13)
            print('\n----------------------------------------------------------------')
            makespan_cpus = [math.fsum(ms1), math.fsum(ms2) + path[0],
                             math.fsum(ms3) + path[1], math.fsum(ms4) + path[2],
                             math.fsum(ms5) + path[3], math.fsum(ms6), math.fsum(ms7) + path[4]
                , math.fsum(ms8) + path[5], math.fsum(ms9) + path[6],
                             math.fsum(ms10) + path[7],
                             math.fsum(ms12) + path[8], math.fsum(ms13)]
            makespan = math.fsum(makespan_cpus)
            print('Makespan is :', round(makespan, 2))

        elif len(x) == 14:
            ms1 = np.round(x[0] / fastest_processor, 2)
            ms2 = np.round(x[1] / p[1], 2)
            ms3 = np.round(x[2] / fastest_processor, 2)
            ms4 = np.round(x[3] / p[2], 2)
            ms5 = np.round(x[4] / p[1], 2)
            ms6 = np.round(x[5] / p[1], 2)
            ms7 = np.round(x[6] / fastest_processor, 2)
            ms8 = np.round(x[7] / fastest_processor, 2)
            ms9 = np.round(x[8] / fastest_processor, 2)
            ms10 = np.round(x[9] / fastest_processor, 2)
            ms11 = np.round(x[10] / fastest_processor, 2)
            ms12 = np.round(x[11] / p[1], 2)
            ms13 = np.round(x[12] / p[1], 2)
            ms14 = np.round(x[13] / fastest_processor, 2)
            run = [ms1, ms2, ms3, ms4, ms5, ms6,
                   ms7, ms8, ms9, ms10, ms11,
                   ms12, ms13,ms14]
            path = np.array([0.5, 0.1, 1, 1.7, 6.6, 11.7, 13.3, 14.79, 18.4, 19.9])
            path_sum = math.fsum(path)
            msm1 = np.round(x[0] / p[1], 2)
            msm2 = np.round(x[1] / p[1], 2)
            msm3 = np.round(x[2] / p[1], 2)
            msm4 = np.round(x[3] / p[1], 2)
            msm5 = np.round(x[4] / p[1], 2)
            msm6 = np.round(x[5] / p[1], 2)
            msm7 = np.round(x[6] / p[1], 2)
            msm8 = np.round(x[7] / p[1], 2)
            msm9 = np.round(x[8] / p[1], 2)
            msm10 = np.round(x[9] / p[1], 2)
            msm11 = np.round(x[10] / p[1], 2)
            msm12 = np.round(x[11] / p[1], 2)
            msm13 = np.round(x[12] / p[1], 2)
            msm14 = np.round(x[13] / p[1], 2)
            task_min = [math.fsum(msm1), math.fsum(msm2),
                        math.fsum(msm3), math.fsum(msm4), math.fsum(msm5), math.fsum(msm6), math.fsum(msm7)
                , math.fsum(msm8), math.fsum(msm9), math.fsum(msm10), math.fsum(msm11),
                        math.fsum(msm12), math.fsum(msm13), math.fsum(msm14)]
            task_min = math.fsum(task_min)
            print('Tasks on fastest processor :', round(task_min, 2))
            cp_min = [max(msm1), max(msm2), max(msm3), max(msm4), max(msm5),
                      max(msm6), max(msm7), max(msm8), max(msm9),
                      max(msm10), max(msm11), max(msm12), max(msm13),max(msm14)]
            print('critical path on fastest cpu :', cp_min)
            cp_min = max(cp_min)
            print('makespan of cp on fastest cpu :', cp_min)
            cp = [max(ms1), max(ms2) + path[0], max(ms3) + path[1],
                  max(ms4) + path[2], max(ms5) + path[3], max(ms6),
                  max(ms7) + path[4], max(ms8) + path[5], max(ms9) + path[6],
                  max(ms10) + path[7], max(ms11), max(ms12) + path[8], max(ms13),max(ms14)+path[9]]
            print('critical path :', cp)
            cp = max(cp)
            print('makespan of cp :', round(cp,2))
            print('\n----------------------------------')
            print('on p0=4:\n', ms1, '\non p1=12:\n', ms2, '\non p0=4:\n',
                  ms3, '\non p2=7:\n', ms4, '\non p1=12:\n', ms5, '\non p1=12:\n', ms6, '\non p1=12:\n', ms7,
                  '\non p1=12:\n', ms8, '\non p1=12:\n', ms9, '\non p0=4:\n', ms10, '\non p0=4:\n',
                  ms11, '\non p0=4:\n', ms12, '\non p1=12:\n', ms13, '\non p2=7:\n', ms14)
            print('\n----------------------------------------------------------------')
            makespan_cpus = [math.fsum(ms1), math.fsum(ms2) + path[0],
                             math.fsum(ms3) + path[1], math.fsum(ms4) + path[2],
                             math.fsum(ms5) + path[3], math.fsum(ms6), math.fsum(ms7) + path[4]
                , math.fsum(ms8) + path[5], math.fsum(ms9) + path[6],
                             math.fsum(ms10) + path[7],
                             math.fsum(ms12) + path[8],
                             math.fsum(ms13),math.fsum(ms14)+path[9]]
            makespan = math.fsum(makespan_cpus)
            print('Makespan is :', round(makespan, 2))

        elif len(x) == 15:
            ms1 = np.round(x[0] / fastest_processor, 2)
            ms2 = np.round(x[1] / p[1], 2)
            ms3 = np.round(x[2] / fastest_processor, 2)
            ms4 = np.round(x[3] / fastest_processor, 2)
            ms5 = np.round(x[4] / p[1], 2)
            ms6 = np.round(x[5] / p[1], 2)
            ms7 = np.round(x[6] / fastest_processor, 2)
            ms8 = np.round(x[7] / fastest_processor, 2)
            ms9 = np.round(x[8] / p[1], 2)
            ms10 = np.round(x[9] / p[0], 2)
            ms11 = np.round(x[10] / fastest_processor, 2)
            ms12 = np.round(x[11] / p[1], 2)
            ms13 = np.round(x[12] / p[1], 2)
            ms14 = np.round(x[13] / fastest_processor, 2)
            ms15 = np.round(x[14] / fastest_processor, 2)
            run = [ms1, ms2, ms3, ms4, ms5, ms6,
                   ms7, ms8, ms9, ms10, ms11,
                   ms12, ms13, ms14,ms15]
            path = np.array([0.5, 0.1, 1, 1.7, 6.6, 11.7, 13.3, 14.79, 18.4, 19.9])
            path_sum = math.fsum(path)
            msm1 = np.round(x[0] / p[1], 2)
            msm2 = np.round(x[1] / p[1], 2)
            msm3 = np.round(x[2] / p[1], 2)
            msm4 = np.round(x[3] / p[1], 2)
            msm5 = np.round(x[4] / p[1], 2)
            msm6 = np.round(x[5] / p[1], 2)
            msm7 = np.round(x[6] / p[1], 2)
            msm8 = np.round(x[7] / p[1], 2)
            msm9 = np.round(x[8] / p[1], 2)
            msm10 = np.round(x[9] / p[1], 2)
            msm11 = np.round(x[10] / p[1], 2)
            msm12 = np.round(x[11] / p[1], 2)
            msm13 = np.round(x[12] / p[1], 2)
            msm14 = np.round(x[13] / p[1], 2)
            msm15 = np.round(x[14] / p[1], 2)
            task_min = [math.fsum(msm1), math.fsum(msm2),
                        math.fsum(msm3), math.fsum(msm4), math.fsum(msm5), math.fsum(msm6), math.fsum(msm7)
                , math.fsum(msm8), math.fsum(msm9), math.fsum(msm10), math.fsum(msm11),
                        math.fsum(msm12), math.fsum(msm13), math.fsum(msm14), math.fsum(msm15)]
            task_min = math.fsum(task_min)
            print('Tasks on fastest processor :', round(task_min, 2))
            cp_min = [max(msm1), max(msm2), max(msm3), max(msm4), max(msm5),
                      max(msm6), max(msm7), max(msm8), max(msm9),
                      max(msm10), max(msm11), max(msm12), max(msm13), max(msm14), max(msm15)]
            print('critical path on fastest cpu :', cp_min)
            cp_min = max(cp_min)
            print('makespan of cp on fastest cpu :', cp_min)
            cp = [max(ms1), max(ms2) + path[0], max(ms3) + path[1],
                  max(ms4) + path[2], max(ms5) + path[3], max(ms6),
                  max(ms7) + path[4], max(ms8) + path[5], max(ms9) + path[6],
                  max(ms10) + path[7], max(ms11), max(ms12) + path[8],
                  max(ms13), max(ms14) + path[9], max(ms15)]
            print('critical path :', cp)
            cp = max(cp)
            print('makespan of cp :', round(cp,2))
            print('\n----------------------------------')
            print('on p0=4:\n', ms1, '\non p1=12:\n', ms2, '\non p0=4:\n',
                  ms3, '\non p2=7:\n', ms4, '\non p1=12:\n', ms5, '\non p1=12:\n', ms6, '\non p1=12:\n', ms7,
                  '\non p1=12:\n', ms8, '\non p1=12:\n', ms9, '\non p0=4:\n', ms10, '\non p0=4:\n',
                  ms11, '\non p0=4:\n', ms12, '\non p1=12:\n', ms13, '\non p2=7:\n', ms14,
                  '\non p2=7:\n', ms15)
            print('\n----------------------------------------------------------------')
            makespan_cpus = [math.fsum(ms1), math.fsum(ms2) + path[0],
                             math.fsum(ms3) + path[1], math.fsum(ms4) + path[2],
                             math.fsum(ms5) + path[3], math.fsum(ms6), math.fsum(ms7) + path[4]
                , math.fsum(ms8) + path[5], math.fsum(ms9) + path[6],
                             math.fsum(ms10) + path[7],
                             math.fsum(ms12) + path[8],
                             math.fsum(ms13), math.fsum(ms14) + path[9], math.fsum(ms15)]
            makespan = math.fsum(makespan_cpus)
            print('Makespan is :', round(makespan, 2))

        elif len(x) == 16:
            ms1 = np.round(x[0] / fastest_processor, 2)
            ms2 = np.round(x[1] / p[1], 2)
            ms3 = np.round(x[2] / fastest_processor, 2)
            ms4 = np.round(x[3] / p[2], 2)
            ms5 = np.round(x[4] / p[1], 2)
            ms6 = np.round(x[5] / p[1], 2)
            ms7 = np.round(x[6] / fastest_processor, 2)
            ms8 = np.round(x[7] / fastest_processor, 2)
            ms9 = np.round(x[8] / p[1], 2)
            ms10 = np.round(x[9] / fastest_processor, 2)
            ms11 = np.round(x[10] / fastest_processor, 2)
            ms12 = np.round(x[11] / fastest_processor, 2)
            ms13 = np.round(x[12] / p[1], 2)
            ms14 = np.round(x[13] / fastest_processor, 2)
            ms15 = np.round(x[14] / fastest_processor, 2)
            ms16 = np.round(x[15] / p[1], 2)
            run = [ms1, ms2, ms3, ms4, ms5, ms6,
                   ms7, ms8, ms9, ms10, ms11,
                   ms12, ms13, ms14, ms15,ms16]
            path = np.array([0.5, 0.1, 1, 1.7, 6.6, 11.7, 13.3, 14.79, 18.4, 19.9, 19.5, 13.6])
            path_sum = math.fsum(path)
            msm1 = np.round(x[0] / p[1], 2)
            msm2 = np.round(x[1] / p[1], 2)
            msm3 = np.round(x[2] / p[1], 2)
            msm4 = np.round(x[3] / p[1], 2)
            msm5 = np.round(x[4] / p[1], 2)
            msm6 = np.round(x[5] / p[1], 2)
            msm7 = np.round(x[6] / p[1], 2)
            msm8 = np.round(x[7] / p[1], 2)
            msm9 = np.round(x[8] / p[1], 2)
            msm10 = np.round(x[9] / p[1], 2)
            msm11 = np.round(x[10] / p[1], 2)
            msm12 = np.round(x[11] / p[1], 2)
            msm13 = np.round(x[12] / p[1], 2)
            msm14 = np.round(x[13] / p[1], 2)
            msm15 = np.round(x[14] / p[1], 2)
            msm16 = np.round(x[15] / p[1], 2)
            task_min = [math.fsum(msm1), math.fsum(msm2),
                        math.fsum(msm3), math.fsum(msm4), math.fsum(msm5), math.fsum(msm6), math.fsum(msm7)
                , math.fsum(msm8), math.fsum(msm9), math.fsum(msm10), math.fsum(msm11),
                        math.fsum(msm12), math.fsum(msm13), math.fsum(msm14), math.fsum(msm15),
                        math.fsum(msm16)]
            task_min = math.fsum(task_min)
            print('Tasks on fastest processor :', round(task_min, 2))
            cp_min = [max(msm1), max(msm2), max(msm3), max(msm4), max(msm5),
                      max(msm6), max(msm7), max(msm8), max(msm9),
                      max(msm10), max(msm11), max(msm12), max(msm13), max(msm14),max(msm15),max(msm16)]
            print('critical path on fastest cpu :', cp_min)
            cp_min = max(cp_min)
            print('makespan of cp on fastest cpu :', cp_min)
            cp = [max(ms1), max(ms2) + path[0], max(ms3) + path[1],
                  max(ms4) + path[2], max(ms5) + path[3], max(ms6),
                  max(ms7) + path[4], max(ms8) + path[5], max(ms9) + path[6],
                  max(ms10) + path[7], max(ms11), max(ms12) + path[8],
                  max(ms13), max(ms14) + path[9],max(ms15)+path[10],max(ms16)+path[11]]
            print('critical path :', cp)
            cp = max(cp)
            print('makespan of cp :', round(cp,2))
            print('\n----------------------------------')
            print('on p0=4:\n', ms1, '\non p1=12:\n', ms2, '\non p0=4:\n',
                  ms3, '\non p2=7:\n', ms4, '\non p1=12:\n', ms5, '\non p1=12:\n', ms6, '\non p1=12:\n', ms7,
                  '\non p1=12:\n', ms8, '\non p1=12:\n', ms9, '\non p0=4:\n', ms10, '\non p0=4:\n',
                  ms11, '\non p0=4:\n', ms12, '\non p1=12:\n', ms13, '\non p2=7:\n', ms14,
                  '\non p2=7:\n', ms15, '\non p1=12:\n', ms16)
            print('\n----------------------------------------------------------------')
            makespan_cpus = [math.fsum(ms1), math.fsum(ms2) + path[0],
                             math.fsum(ms3) + path[1], math.fsum(ms4) + path[2],
                             math.fsum(ms5) + path[3], math.fsum(ms6), math.fsum(ms7) + path[4]
                , math.fsum(ms8) + path[5], math.fsum(ms9) + path[6],
                             math.fsum(ms10) + path[7],
                             math.fsum(ms12) + path[8],
                             math.fsum(ms13), math.fsum(ms14) + path[9],
                             math.fsum(ms15), math.fsum(ms16)+path[11]]
            makespan = math.fsum(makespan_cpus)
            print('Makespan is :', round(makespan, 2))

        elif len(x) == 17:
            ms1 = np.round(x[0] / fastest_processor, 2)
            ms2 = np.round(x[1] / p[1], 2)
            ms3 = np.round(x[2] / fastest_processor, 2)
            ms4 = np.round(x[3] / p[2], 2)
            ms5 = np.round(x[4] / p[1], 2)
            ms6 = np.round(x[5] / p[1], 2)
            ms7 = np.round(x[6] / fastest_processor, 2)
            ms8 = np.round(x[7] / fastest_processor, 2)
            ms9 = np.round(x[8] / p[1], 2)
            ms10 = np.round(x[9] / fastest_processor, 2)
            ms11 = np.round(x[10] / fastest_processor, 2)
            ms12 = np.round(x[11] / p[1], 2)
            ms13 = np.round(x[12] / p[1], 2)
            ms14 = np.round(x[13] / fastest_processor, 2)
            ms15 = np.round(x[14] / fastest_processor, 2)
            ms16 = np.round(x[15] / p[1], 2)
            ms17 = np.round(x[16] / p[1], 2)
            run = [ms1, ms2, ms3, ms4, ms5, ms6,
                   ms7, ms8, ms9, ms10, ms11, ms12,
                   ms13, ms14, ms15, ms16,ms17]
            path = np.array([0.5, 0.1, 1, 1.7, 6.6, 11.7, 13.3, 14.79, 18.4, 19.9, 19.5, 13.6])
            path_sum = math.fsum(path)
            msm1 = np.round(x[0] / p[1], 2)
            msm2 = np.round(x[1] / p[1], 2)
            msm3 = np.round(x[2] / p[1], 2)
            msm4 = np.round(x[3] / p[1], 2)
            msm5 = np.round(x[4] / p[1], 2)
            msm6 = np.round(x[5] / p[1], 2)
            msm7 = np.round(x[6] / p[1], 2)
            msm8 = np.round(x[7] / p[1], 2)
            msm9 = np.round(x[8] / p[1], 2)
            msm10 = np.round(x[9] / p[1], 2)
            msm11 = np.round(x[10] / p[1], 2)
            msm12 = np.round(x[11] / p[1], 2)
            msm13 = np.round(x[12] / p[1], 2)
            msm14 = np.round(x[13] / p[1], 2)
            msm15 = np.round(x[14] / p[1], 2)
            msm16 = np.round(x[15] / p[1], 2)
            msm17 = np.round(x[16] / p[1], 2)
            task_min = [math.fsum(msm1), math.fsum(msm2),
                        math.fsum(msm3), math.fsum(msm4), math.fsum(msm5), math.fsum(msm6), math.fsum(msm7)
                , math.fsum(msm8), math.fsum(msm9), math.fsum(msm10), math.fsum(msm11),
                        math.fsum(msm12), math.fsum(msm13), math.fsum(msm14), math.fsum(msm15),
                        math.fsum(msm16), math.fsum(msm17)]
            task_min = math.fsum(task_min)
            print('Tasks on fastest processor :', round(task_min, 2))
            cp_min = [max(msm1), max(msm2), max(msm3), max(msm4), max(msm5),
                      max(msm6), max(msm7), max(msm8), max(msm9),
                      max(msm10), max(msm11), max(msm12),
                      max(msm13), max(msm14), max(msm15),max(msm16),max(msm17)]
            print('critical path on fastest cpu :', cp_min)
            cp_min = max(cp_min)
            print('makespan of cp on fastest cpu :', cp_min)
            cp = [max(ms1), max(ms2) + path[0], max(ms3) + path[1],
                  max(ms4) + path[2], max(ms5) + path[3], max(ms6),
                  max(ms7) + path[4], max(ms8) + path[5], max(ms9) + path[6],
                  max(ms10) + path[7], max(ms11), max(ms12) + path[8],
                  max(ms13), max(ms14) + path[9], max(ms15) + path[10],max(ms16)+path[11],max(ms17)]
            print('critical path :', cp)
            cp = max(cp)
            print('makespan of cp :', round(cp,2))
            print('\n----------------------------------')
            print('on p0=4:\n', ms1, '\non p1=12:\n', ms2, '\non p0=4:\n',
                  ms3, '\non p2=7:\n', ms4, '\non p1=12:\n', ms5, '\non p1=12:\n', ms6, '\non p1=12:\n', ms7,
                  '\non p1=12:\n', ms8, '\non p1=12:\n', ms9, '\non p0=4:\n', ms10, '\non p0=4:\n',
                  ms11, '\non p0=4:\n', ms12, '\non p1=12:\n', ms13, '\non p2=7:\n', ms14,
                  '\non p2=7:\n', ms15, '\non p1=12:\n', ms16, '\non p1=12:\n', ms17)
            print('\n----------------------------------------------------------------')
            makespan_cpus = [math.fsum(ms1), math.fsum(ms2) + path[0],
                             math.fsum(ms3) + path[1], math.fsum(ms4) + path[2],
                             math.fsum(ms5) + path[3], math.fsum(ms6), math.fsum(ms7) + path[4]
                , math.fsum(ms8) + path[5], math.fsum(ms9) + path[6],
                             math.fsum(ms10) + path[7],
                             math.fsum(ms12) + path[8],
                             math.fsum(ms13), math.fsum(ms14) + path[9],
                             math.fsum(ms15), math.fsum(ms16) + path[11],math.fsum(ms17)]
            makespan = math.fsum(makespan_cpus)
            print('Makespan is :', round(makespan, 2))

        elif len(x) == 18:
            ms1 = np.round(x[0] / fastest_processor, 2)
            ms2 = np.round(x[1] / p[1], 2)
            ms3 = np.round(x[2] / fastest_processor, 2)
            ms4 = np.round(x[3] / fastest_processor, 2)
            ms5 = np.round(x[4] / p[1], 2)
            ms6 = np.round(x[5] / p[1], 2)
            ms7 = np.round(x[6] / fastest_processor, 2)
            ms8 = np.round(x[7] / fastest_processor, 2)
            ms9 = np.round(x[8] / p[1], 2)
            ms10 = np.round(x[9] / p[0], 2)
            ms11 = np.round(x[10] / fastest_processor, 2)
            ms12 = np.round(x[11] / p[1], 2)
            ms13 = np.round(x[12] / p[1], 2)
            ms14 = np.round(x[13] / fastest_processor, 2)
            ms15 = np.round(x[14] / fastest_processor, 2)
            ms16 = np.round(x[15] / p[1], 2)
            ms17 = np.round(x[16] / p[1], 2)
            ms18 = np.round(x[17] / fastest_processor, 2)
            run = [ms1, ms2, ms3, ms4, ms5, ms6,
                   ms7, ms8, ms9, ms10, ms11, ms12,
                   ms13, ms14, ms15, ms16, ms17,ms18]
            path = np.array([0.5, 0.1, 1, 1.7, 6.6, 11.7, 13.3, 14.79, 18.4, 19.9, 19.5, 13.6, 17.7])
            path_sum = math.fsum(path)
            msm1 = np.round(x[0] / p[1], 2)
            msm2 = np.round(x[1] / p[1], 2)
            msm3 = np.round(x[2] / p[1], 2)
            msm4 = np.round(x[3] / p[1], 2)
            msm5 = np.round(x[4] / p[1], 2)
            msm6 = np.round(x[5] / p[1], 2)
            msm7 = np.round(x[6] / p[1], 2)
            msm8 = np.round(x[7] / p[1], 2)
            msm9 = np.round(x[8] / p[1], 2)
            msm10 = np.round(x[9] / p[1], 2)
            msm11 = np.round(x[10] / p[1], 2)
            msm12 = np.round(x[11] / p[1], 2)
            msm13 = np.round(x[12] / p[1], 2)
            msm14 = np.round(x[13] / p[1], 2)
            msm15 = np.round(x[14] / p[1], 2)
            msm16 = np.round(x[15] / p[1], 2)
            msm17 = np.round(x[16] / p[1], 2)
            msm18 = np.round(x[17] / p[1], 2)
            task_min = [math.fsum(msm1), math.fsum(msm2),
                        math.fsum(msm3), math.fsum(msm4), math.fsum(msm5), math.fsum(msm6), math.fsum(msm7)
                , math.fsum(msm8), math.fsum(msm9), math.fsum(msm10), math.fsum(msm11),
                        math.fsum(msm12), math.fsum(msm13), math.fsum(msm14), math.fsum(msm15),
                        math.fsum(msm16), math.fsum(msm17), math.fsum(msm18)]
            task_min = math.fsum(task_min)
            print('Tasks on fastest processor :', round(task_min, 2))
            cp_min = [max(msm1), max(msm2), max(msm3), max(msm4), max(msm5),
                      max(msm6), max(msm7), max(msm8), max(msm9),
                      max(msm10), max(msm11), max(msm12),
                      max(msm13), max(msm14), max(msm15), max(msm16), max(msm17),max(msm18)]
            print('critical path on fastest cpu :', cp_min)
            cp_min = max(cp_min)
            print('makespan of cp on fastest cpu :', cp_min)
            cp = [max(ms1), max(ms2) + path[0], max(ms3) + path[1],
                  max(ms4) + path[2], max(ms5) + path[3], max(ms6),
                  max(ms7) + path[4], max(ms8) + path[5], max(ms9) + path[6],
                  max(ms10) + path[7], max(ms11), max(ms12) + path[8],
                  max(ms13), max(ms14) + path[9], max(ms15) + path[10], max(ms16), max(ms17),max(ms18)+path[12]]
            print('critical path :', cp)
            cp = max(cp)
            print('makespan of cp :', round(cp,2))
            print('\n----------------------------------')
            print('on p0=4:\n', ms1, '\non p1=12:\n', ms2, '\non p0=4:\n',
                  ms3, '\non p2=7:\n', ms4, '\non p1=12:\n', ms5, '\non p1=12:\n', ms6, '\non p1=12:\n', ms7,
                  '\non p1=12:\n', ms8, '\non p1=12:\n', ms9, '\non p0=4:\n', ms10, '\non p0=4:\n',
                  ms11, '\non p0=4:\n', ms12, '\non p1=12:\n', ms13, '\non p2=7:\n', ms14,
                  '\non p2=7:\n', ms15, '\non p1=12:\n', ms16, '\non p1=12:\n', ms17, '\non p1=12:\n', ms18)
            print('\n----------------------------------------------------------------')
            makespan_cpus = [math.fsum(ms1), math.fsum(ms2) + path[0],
                             math.fsum(ms3) + path[1], math.fsum(ms4) + path[2],
                             math.fsum(ms5) + path[3], math.fsum(ms6), math.fsum(ms7) + path[4]
                , math.fsum(ms8) + path[5], math.fsum(ms9) + path[6],
                             math.fsum(ms10) + path[7],
                             math.fsum(ms12) + path[8],
                             math.fsum(ms13), math.fsum(ms14) + path[9],
                             math.fsum(ms15), math.fsum(ms16) + path[11],
                             math.fsum(ms17),math.fsum(ms18)+path[12]]
            makespan = math.fsum(makespan_cpus)
            print('Makespan is :', round(makespan, 2))

        elif len(x) == 19:
            ms1 = np.round(x[0] / fastest_processor, 2)
            ms2 = np.round(x[1] / p[1], 2)
            ms3 = np.round(x[2] / p[0], 2)
            ms4 = np.round(x[3] / p[2], 2)
            ms5 = np.round(x[4] / p[1], 2)
            ms6 = np.round(x[5] / p[1], 2)
            ms7 = np.round(x[6] / fastest_processor, 2)
            ms8 = np.round(x[7] / fastest_processor, 2)
            ms9 = np.round(x[8] / fastest_processor, 2)
            ms10 = np.round(x[9] / p[0], 2)
            ms11 = np.round(x[10] / fastest_processor, 2)
            ms12 = np.round(x[11] / p[1], 2)
            ms13 = np.round(x[12] / p[1], 2)
            ms14 = np.round(x[13] / fastest_processor, 2)
            ms15 = np.round(x[14] / fastest_processor, 2)
            ms16 = np.round(x[15] / p[1], 2)
            ms17 = np.round(x[16] / p[1], 2)
            ms18 = np.round(x[17] / fastest_processor, 2)
            ms19 = np.round(x[18] / fastest_processor, 2)
            run = [ms1, ms2, ms3, ms4, ms5, ms6,
                   ms7, ms8, ms9, ms10, ms11, ms12,
                   ms13, ms14, ms15, ms16, ms17, ms18,ms19]
            path = np.array([0.5, 0.1, 1, 1.7, 6.6, 11.7, 13.3, 14.79, 18.4, 19.9, 19.5, 13.6, 17.7])
            path_sum = math.fsum(path)
            msm1 = np.round(x[0] / p[1], 2)
            msm2 = np.round(x[1] / p[1], 2)
            msm3 = np.round(x[2] / p[1], 2)
            msm4 = np.round(x[3] / p[1], 2)
            msm5 = np.round(x[4] / p[1], 2)
            msm6 = np.round(x[5] / p[1], 2)
            msm7 = np.round(x[6] / p[1], 2)
            msm8 = np.round(x[7] / p[1], 2)
            msm9 = np.round(x[8] / p[1], 2)
            msm10 = np.round(x[9] / p[1], 2)
            msm11 = np.round(x[10] / p[1], 2)
            msm12 = np.round(x[11] / p[1], 2)
            msm13 = np.round(x[12] / p[1], 2)
            msm14 = np.round(x[13] / p[1], 2)
            msm15 = np.round(x[14] / p[1], 2)
            msm16 = np.round(x[15] / p[1], 2)
            msm17 = np.round(x[16] / p[1], 2)
            msm18 = np.round(x[17] / p[1], 2)
            msm19 = np.round(x[18] / p[1], 2)
            task_min = [math.fsum(msm1), math.fsum(msm2),
                        math.fsum(msm3), math.fsum(msm4), math.fsum(msm5), math.fsum(msm6), math.fsum(msm7)
                , math.fsum(msm8), math.fsum(msm9), math.fsum(msm10), math.fsum(msm11),
                        math.fsum(msm12), math.fsum(msm13), math.fsum(msm14), math.fsum(msm15),
                        math.fsum(msm16), math.fsum(msm17), math.fsum(msm18), math.fsum(msm19)]
            task_min = math.fsum(task_min)
            print('Tasks on fastest processor :', round(task_min,2))
            cp_min = [max(msm1), max(msm2), max(msm3), max(msm4), max(msm5),
                      max(msm6), max(msm7), max(msm8), max(msm9),
                      max(msm10), max(msm11), max(msm12),
                      max(msm13), max(msm14), max(msm15), max(msm16), max(msm17), max(msm18),max(msm19)]
            print('critical path on fastest cpu :', cp_min)
            cp_min = max(cp_min)
            print('makespan of cp on fastest cpu :', cp_min)
            cp = [max(ms1), max(ms2) + path[0], max(ms3) + path[1],
                  max(ms4) + path[2], max(ms5) + path[3], max(ms6),
                  max(ms7) + path[4], max(ms8) + path[5], max(ms9) + path[6],
                  max(ms10) + path[7], max(ms11), max(ms12) + path[8],
                  max(ms13), max(ms14) + path[9], max(ms15) + path[10],
                  max(ms16), max(ms17),max(ms18)+path[12],max(ms19)]
            print('critical path :', cp)
            cp = max(cp)
            print('makespan of cp :', round(cp,2))
            print('\n----------------------------------')
            print('on p0=4:\n', ms1, '\non p1=12:\n', ms2, '\non p0=4:\n',
                  ms3, '\non p2=7:\n', ms4, '\non p1=12:\n', ms5, '\non p1=12:\n', ms6, '\non p1=12:\n', ms7,
                  '\non p1=12:\n', ms8, '\non p1=12:\n', ms9, '\non p0=4:\n', ms10, '\non p0=4:\n',
                  ms11, '\non p0=4:\n', ms12, '\non p1=12:\n', ms13, '\non p2=7:\n', ms14,
                  '\non p2=7:\n', ms15, '\non p1=12:\n', ms16, '\non p1=12:\n', ms17,
                  '\non p1=12:\n', ms18, '\non p0=4:\n', ms19)
            print('\n----------------------------------------------------------------')
            makespan_cpus = [math.fsum(ms1), math.fsum(ms2) + path[0],
                             math.fsum(ms3) + path[1], math.fsum(ms4) + path[2],
                             math.fsum(ms5) + path[3], math.fsum(ms6), math.fsum(ms7) + path[4]
                , math.fsum(ms8) + path[5], math.fsum(ms9) + path[6],
                             math.fsum(ms10) + path[7],
                             math.fsum(ms12) + path[8],
                             math.fsum(ms13), math.fsum(ms14) + path[9],
                             math.fsum(ms15), math.fsum(ms16) + path[11],
                             math.fsum(ms17), math.fsum(ms18) + path[12], math.fsum(ms19)]
            makespan = round(math.fsum(makespan_cpus),2)
            print('Makespan is :', makespan)

        SLR = round(makespan/cp_min,2)
        print('-> SLR is :',SLR)

        Speedup = round(task_min/makespan,2)
        print('-> Speed up is :',Speedup)

        Efficiency = round(Speedup/cpu_len,2)
        print('-> Efficiency is :',Efficiency)
        print('running on CPUS :' , run)
        print('makespan cpus :',makespan_cpus)

        CCR = round(path_sum/makespan,1)
        print('CCR :' ,CCR)

        with open (file_name,'a') as f :
            makespan = round(makespan,2)
            f.write(str(makespan))
            f.write(',')
        with open(file_name2, 'a') as f:
            f.write(str(SLR))
            f.write(',')
        with open(file_name3, 'a') as f:
            f.write(str(Speedup))
            f.write(',')
        with open(file_name4, 'a') as f:
            f.write(str(CCR))
            f.write(',')
        with open(file_name5, 'a') as f:
            f.write(str(Efficiency))
            f.write(',')

    except TypeError:
        print('\n')
        print('     *************************************************')
        print('     *  Size of input Graph arrays must not be equal *')
        print('     *              Try another Graph !              *')
        print('     *************************************************')

def Metrics_c (x=list) :
    try:
        if x[0:len(x)] == x[0:len(x)]:
            x[0].append(0)
        x = np.array(x,dtype=object)
        p = np.array([4,12,7])
        cpu_len = len(p)

        file_name = 'C:/Users/Naweed/PycharmProjects/IHHO/Metrics Cuckoo/Makespan data set.txt'
        file_name2 = 'C:/Users/Naweed/PycharmProjects/IHHO/Metrics Cuckoo/SLR data set.txt'
        file_name3 = 'C:/Users/Naweed/PycharmProjects/IHHO/Metrics Cuckoo/Speed up data set.txt'
        file_name4 = 'C:/Users/Naweed/PycharmProjects/IHHO/Metrics Cuckoo/CCR data set.txt'
        file_name5 = 'C:/Users/Naweed/PycharmProjects/IHHO/Metrics Cuckoo/Efficiency data set.txt'

        if len(x) == 3 :
            ms1 = np.round(x[0] / p[0],2)
            ms2 = np.round(x[1] / p[1],2)
            ms3 = np.round(x[2] / p[0],2)
            run = [ms1,ms2,ms3]

            path = np.array([0.5, 0.1])
            path_sum = math.fsum(path)
            msm1 = np.round(x[0] / p[1], 2)
            msm2 = np.round(x[1] / p[1], 2)
            msm3 = np.round(x[2] / p[1], 2)

            task_min = [math.fsum(msm1), math.fsum(msm2),
                        math.fsum(msm3)]
            task_min = math.fsum(task_min)
            print('Tasks on fastest processor :', round(task_min, 2))
            cp_min = [max(msm1),max(msm2),max(msm3)]
            print('critical path on fastest cpu :',cp_min)
            cp_min = max(cp_min)
            print('makespan of cp on fastest cpu :',cp_min)
            cp = [max(ms1),max(ms2)+path[0],max(ms3)+path[1]]
            print('critical path :',cp)
            cp = max(cp)
            print('makespan of cp :', round(cp,2))
            print('\n----------------------------------')
            print('on p0=4:\n', ms1, '\non p1=12:\n', ms2, '\non p0=4:\n', ms3)
            print('\n----------------------------------------------------------------')
            makespan_cpus = [math.fsum(ms1),math.fsum(ms2)+path[0],
                             math.fsum(ms3)+path[1]]
            makespan = math.fsum(makespan_cpus)
            print('Makespan is :',round(makespan,2))

        if len(x) == 4 :
            ms1 = np.round(x[0] / p[0],2)
            ms2 = np.round(x[1] / p[1],2)
            ms3 = np.round(x[2] / p[0],2)
            ms4 = np.round(x[3] / p[2],2)
            run = [ms1,ms2,ms3,ms4]

            path = np.array([0.5, 0.1, 1])
            path_sum = math.fsum(path)
            msm1 = np.round(x[0] / p[1], 2)
            msm2 = np.round(x[1] / p[1], 2)
            msm3 = np.round(x[2] / p[1], 2)
            msm4 = np.round(x[3] / p[1], 2)
            task_min = [math.fsum(msm1), math.fsum(msm2),
                        math.fsum(msm3), math.fsum(msm4)]
            task_min = math.fsum(task_min)
            print('Tasks on fastest processor :', round(task_min, 2))
            cp_min = [max(msm1),max(msm2),max(msm3),max(msm4)]
            print('critical path on fastest cpu :',cp_min)
            cp_min = max(cp_min)
            print('makespan of cp on fastest cpu :',cp_min)
            cp = [max(ms1),max(ms2)+path[0],max(ms3)+path[1],max(ms4)+path[2]]
            print('critical path :',cp)
            cp = max(cp)
            print('makespan of cp :', round(cp,2))
            print('\n----------------------------------')
            print('on p0=4:\n', ms1, '\non p1=12:\n', ms2, '\non p0=4:\n', ms3, '\non p2=7:\n', ms4)
            print('\n----------------------------------------------------------------')
            makespan_cpus = [math.fsum(ms1),math.fsum(ms2)+path[0],
                             math.fsum(ms3)+path[1],math.fsum(ms4)+path[2]]
            makespan = math.fsum(makespan_cpus)
            print('Makespan is :',round(makespan,2))

        elif len(x) == 5 :
            ms1 = np.round(x[0]/p[0],2)
            ms2 = np.round(x[1] / p[1],2)
            ms3 = np.round(x[2] / p[0],2)
            ms4 = np.round(x[3] / p[2],2)
            ms5 = np.round(x[4] / p[1], 2)
            run = [ms1, ms2, ms3, ms4,ms5]
            path = np.array([0.5, 0.1, 1, 1.7])
            path_sum = math.fsum(path)
            msm1 = np.round(x[0] / p[1], 2)
            msm2 = np.round(x[1] / p[1], 2)
            msm3 = np.round(x[2] / p[1], 2)
            msm4 = np.round(x[3] / p[1], 2)
            msm5 = np.round(x[4] / p[1], 2)
            task_min = [math.fsum(msm1), math.fsum(msm2),
                        math.fsum(msm3), math.fsum(msm4), math.fsum(msm5)]
            task_min = math.fsum(task_min)
            print('Tasks on fastest processor :', round(task_min, 2))
            cp_min = [max(msm1), max(msm2), max(msm3), max(msm4),max(ms5)]
            print('critical path on fastest cpu :', cp_min)
            cp_min = max(cp_min)
            print('makespan of cp on fastest cpu :', cp_min)
            cp = [max(ms1),max(ms2)+path[0],max(ms3)+path[1],max(ms4)+path[2],max(ms5)+path[3]]
            print('critical path :', cp)
            cp = max(cp)
            print('makespan of cp :', round(cp,2))
            print('\n----------------------------------')
            print('on p0=4:\n', ms1, '\non p1=12:\n', ms2, '\non p0=4:\n', ms3, '\non p2=7:\n', ms4,'\non p1=12:\n', ms5)
            print('\n----------------------------------------------------------------')
            makespan_cpus = [math.fsum(ms1), math.fsum(ms2) + path[0],
                             math.fsum(ms3) + path[1], math.fsum(ms4) + path[2],math.fsum(ms5)+path[3]]
            makespan = math.fsum(makespan_cpus)
            print('Makespan is :',round(makespan,2))

        elif len(x) == 6:
            ms1 = np.round(x[0] / p[0], 2)
            ms2 = np.round(x[1] / p[1], 2)
            ms3 = np.round(x[2] / p[0], 2)
            ms4 = np.round(x[3] / p[2], 2)
            ms5 = np.round(x[4] / p[1], 2)
            ms6 = np.round(x[5] / p[1], 2)
            run = [ms1, ms2, ms3, ms4, ms5,ms6]
            path = np.array([0.5, 0.1, 1, 1.7])
            path_sum = math.fsum(path)
            msm1 = np.round(x[0] / p[1], 2)
            msm2 = np.round(x[1] / p[1], 2)
            msm3 = np.round(x[2] / p[1], 2)
            msm4 = np.round(x[3] / p[1], 2)
            msm5 = np.round(x[4] / p[1], 2)
            msm6 = np.round(x[5] / p[1], 2)
            task_min = [math.fsum(msm1), math.fsum(msm2),
                        math.fsum(msm3), math.fsum(msm4), math.fsum(msm5), math.fsum(msm6)]
            task_min = math.fsum(task_min)
            print('Tasks on fastest processor :', round(task_min, 2))
            cp_min = [max(msm1), max(msm2), max(msm3), max(msm4), max(msm5),max(msm6)]
            print('critical path on fastest cpu :', cp_min)
            cp_min = max(cp_min)
            print('makespan of cp on fastest cpu :', cp_min)
            cp = [max(ms1), max(ms2) + path[0], max(ms3) + path[1],
                  max(ms4) + path[2], max(ms5) + path[3],max(ms6)]
            print('critical path :', cp)
            cp = max(cp)
            print('makespan of cp :', round(cp,2))
            print('\n----------------------------------')
            print('on p0=4:\n', ms1, '\non p1=12:\n', ms2, '\non p0=4:\n',
            ms3, '\non p2=7:\n', ms4, '\non p1=12:\n', ms5,'\non p1=12:\n', ms6)
            print('\n----------------------------------------------------------------')
            makespan_cpus = [math.fsum(ms1), math.fsum(ms2) + path[0],
                             math.fsum(ms3) + path[1], math.fsum(ms4) + path[2],
                             math.fsum(ms5) + path[3],math.fsum(ms6)]
            makespan = math.fsum(makespan_cpus)
            print('Makespan is :', round(makespan, 2))

        elif len(x) == 7:
            ms1 = np.round(x[0] / p[0], 2)
            ms2 = np.round(x[1] / p[1], 2)
            ms3 = np.round(x[2] / p[0], 2)
            ms4 = np.round(x[3] / p[2], 2)
            ms5 = np.round(x[4] / p[1], 2)
            ms6 = np.round(x[5] / p[1], 2)
            ms7 = np.round(x[6] / p[0], 2)
            run = [ms1, ms2, ms3, ms4, ms5, ms6,ms7]
            path = np.array([0.5, 0.1, 1, 1.7, 6.6])
            path_sum = math.fsum(path)
            msm1 = np.round(x[0] / p[1], 2)
            msm2 = np.round(x[1] / p[1], 2)
            msm3 = np.round(x[2] / p[1], 2)
            msm4 = np.round(x[3] / p[1], 2)
            msm5 = np.round(x[4] / p[1], 2)
            msm6 = np.round(x[5] / p[1], 2)
            msm7 = np.round(x[6] / p[1], 2)
            task_min = [math.fsum(msm1), math.fsum(msm2),
                        math.fsum(msm3), math.fsum(msm4), math.fsum(msm5), math.fsum(msm6), math.fsum(msm7)]
            task_min = math.fsum(task_min)
            print('Tasks on fastest processor :', round(task_min, 2))
            cp_min = [max(msm1), max(msm2), max(msm3), max(msm4), max(msm5), max(msm6),max(msm7)]
            print('critical path on fastest cpu :', cp_min)
            cp_min = max(cp_min)
            print('makespan of cp on fastest cpu :', cp_min)
            cp = [max(ms1), max(ms2) + path[0], max(ms3) + path[1],
                  max(ms4) + path[2], max(ms5) + path[3], max(ms6),max(ms7)+path[4]]
            print('critical path :', cp)
            cp = max(cp)
            print('makespan of cp :', round(cp,2))
            print('\n----------------------------------')
            print('on p0=4:\n', ms1, '\non p1=12:\n', ms2, '\non p0=4:\n',
            ms3, '\non p2=7:\n', ms4, '\non p1=12:\n', ms5,'\non p1=12:\n', ms6,'\non p1=12:\n', ms7)
            print('\n----------------------------------------------------------------')
            makespan_cpus = [math.fsum(ms1), math.fsum(ms2) + path[0],
                             math.fsum(ms3) + path[1], math.fsum(ms4) + path[2],
                             math.fsum(ms5) + path[3], math.fsum(ms6),math.fsum(ms7)+path[4]]
            makespan = math.fsum(makespan_cpus)
            print('Makespan is :', round(makespan, 2))

        elif len(x) == 8:
            ms1 = np.round(x[0] / p[0], 2)
            ms2 = np.round(x[1] / p[1], 2)
            ms3 = np.round(x[2] / p[0], 2)
            ms4 = np.round(x[3] / p[2], 2)
            ms5 = np.round(x[4] / p[1], 2)
            ms6 = np.round(x[5] / p[1], 2)
            ms7 = np.round(x[6] / p[0], 2)
            ms8 = np.round(x[7] / p[2], 2)
            run = [ms1, ms2, ms3, ms4, ms5, ms6, ms7,ms8]
            path = np.array([0.5, 0.1, 1, 1.7, 6.6, 11.7])
            path_sum = math.fsum(path)
            msm1 = np.round(x[0] / p[1], 2)
            msm2 = np.round(x[1] / p[1], 2)
            msm3 = np.round(x[2] / p[1], 2)
            msm4 = np.round(x[3] / p[1], 2)
            msm5 = np.round(x[4] / p[1], 2)
            msm6 = np.round(x[5] / p[1], 2)
            msm7 = np.round(x[6] / p[1], 2)
            msm8 = np.round(x[7] / p[1], 2)
            task_min = [math.fsum(msm1), math.fsum(msm2),
                        math.fsum(msm3), math.fsum(msm4), math.fsum(msm5), math.fsum(msm6), math.fsum(msm7)
                , math.fsum(msm8)]
            task_min = math.fsum(task_min)
            print('Tasks on fastest processor :', round(task_min, 2))
            cp_min = [max(msm1), max(msm2), max(msm3), max(msm4), max(msm5), max(msm6), max(msm7),max(msm8)]
            print('critical path on fastest cpu :', cp_min)
            cp_min = max(cp_min)
            print('makespan of cp on fastest cpu :', cp_min)
            cp = [max(ms1), max(ms2) + path[0], max(ms3) + path[1],
                  max(ms4) + path[2], max(ms5) + path[3], max(ms6), max(ms7) + path[4],max(ms8)+path[5]]
            print('critical path :', cp)
            cp = max(cp)
            print('makespan of cp :', round(cp,2))
            print('\n----------------------------------')
            print('on p0=4:\n', ms1, '\non p1=12:\n', ms2, '\non p0=4:\n',
            ms3, '\non p2=7:\n', ms4, '\non p1=12:\n', ms5,'\non p1=12:\n', ms6,'\non p1=12:\n', ms7,
                  '\non p2=7:\n', ms8)
            print('\n----------------------------------------------------------------')
            makespan_cpus = [math.fsum(ms1), math.fsum(ms2) + path[0],
                             math.fsum(ms3) + path[1], math.fsum(ms4) + path[2],
                             math.fsum(ms5) + path[3], math.fsum(ms6), math.fsum(ms7) + path[4]
                ,math.fsum(ms8)+path[5]]
            makespan = math.fsum(makespan_cpus)
            print('Makespan is :', round(makespan, 2))

        elif len(x) == 9:
            ms1 = np.round(x[0] / p[0], 2)
            ms2 = np.round(x[1] / p[1], 2)
            ms3 = np.round(x[2] / p[0], 2)
            ms4 = np.round(x[3] / p[2], 2)
            ms5 = np.round(x[4] / p[1], 2)
            ms6 = np.round(x[5] / p[1], 2)
            ms7 = np.round(x[6] / p[0], 2)
            ms8 = np.round(x[7] / p[2], 2)
            ms9 = np.round(x[8] / p[1], 2)
            run = [ms1, ms2, ms3, ms4, ms5, ms6, ms7, ms8,ms9]
            path = np.array([0.5, 0.1, 1, 1.7, 6.6, 11.7, 13.3])
            path_sum = math.fsum(path)
            msm1 = np.round(x[0] / p[1], 2)
            msm2 = np.round(x[1] / p[1], 2)
            msm3 = np.round(x[2] / p[1], 2)
            msm4 = np.round(x[3] / p[1], 2)
            msm5 = np.round(x[4] / p[1], 2)
            msm6 = np.round(x[5] / p[1], 2)
            msm7 = np.round(x[6] / p[1], 2)
            msm8 = np.round(x[7] / p[1], 2)
            msm9 = np.round(x[8] / p[1], 2)
            task_min = [math.fsum(msm1), math.fsum(msm2),
                        math.fsum(msm3), math.fsum(msm4), math.fsum(msm5), math.fsum(msm6), math.fsum(msm7)
                , math.fsum(msm8), math.fsum(msm9)]
            task_min = math.fsum(task_min)
            print('Tasks on fastest processor :', round(task_min, 2))
            cp_min = [max(msm1), max(msm2), max(msm3), max(msm4), max(msm5),
                      max(msm6), max(msm7), max(msm8),max(msm9)]
            print('critical path on fastest cpu :', cp_min)
            cp_min = max(cp_min)
            print('makespan of cp on fastest cpu :', cp_min)
            cp = [max(ms1), max(ms2) + path[0], max(ms3) + path[1],
                  max(ms4) + path[2], max(ms5) + path[3], max(ms6),
                  max(ms7) + path[4], max(ms8) + path[5],max(ms9) + path[6]]
            print('critical path :', cp)
            cp = max(cp)
            print('makespan of cp :', round(cp,2))
            print('\n----------------------------------')
            print('on p0=4:\n', ms1, '\non p1=12:\n', ms2, '\non p0=4:\n',
                  ms3, '\non p2=7:\n', ms4, '\non p1=12:\n', ms5, '\non p1=12:\n', ms6, '\non p1=12:\n', ms7,
                  '\non p1=12:\n', ms8, '\non p1=12:\n', ms9)
            print('\n----------------------------------------------------------------')
            makespan_cpus = [math.fsum(ms1), math.fsum(ms2) + path[0],
                             math.fsum(ms3) + path[1], math.fsum(ms4) + path[2],
                             math.fsum(ms5) + path[3], math.fsum(ms6), math.fsum(ms7) + path[4]
                , math.fsum(ms8) + path[5], math.fsum(ms9)+path[6]]
            makespan = math.fsum(makespan_cpus)
            print('Makespan is :', round(makespan, 2))

        elif len(x) == 10:
            ms1 = np.round(x[0] / p[0], 2)
            ms2 = np.round(x[1] / p[1], 2)
            ms3 = np.round(x[2] / p[0], 2)
            ms4 = np.round(x[3] / p[2], 2)
            ms5 = np.round(x[4] / p[1], 2)
            ms6 = np.round(x[5] / p[1], 2)
            ms7 = np.round(x[6] / p[0], 2)
            ms8 = np.round(x[7] / p[2], 2)
            ms9 = np.round(x[8] / p[1], 2)
            ms10 = np.round(x[9] / p[0], 2)
            run = [ms1, ms2, ms3, ms4, ms5, ms6, ms7, ms8, ms9,ms10]
            path = np.array([0.5, 0.1, 1, 1.7, 6.6, 11.7, 13.3, 14.79])
            path_sum = math.fsum(path)
            msm1 = np.round(x[0] / p[1], 2)
            msm2 = np.round(x[1] / p[1], 2)
            msm3 = np.round(x[2] / p[1], 2)
            msm4 = np.round(x[3] / p[1], 2)
            msm5 = np.round(x[4] / p[1], 2)
            msm6 = np.round(x[5] / p[1], 2)
            msm7 = np.round(x[6] / p[1], 2)
            msm8 = np.round(x[7] / p[1], 2)
            msm9 = np.round(x[8] / p[1], 2)
            msm10 = np.round(x[9] / p[1], 2)
            task_min = [math.fsum(msm1), math.fsum(msm2),
                        math.fsum(msm3), math.fsum(msm4), math.fsum(msm5), math.fsum(msm6), math.fsum(msm7)
                , math.fsum(msm8), math.fsum(msm9), math.fsum(msm10)]
            task_min = math.fsum(task_min)
            print('Tasks on fastest processor :', round(task_min, 2))
            cp_min = [max(msm1), max(msm2), max(msm3), max(msm4), max(msm5),
                      max(msm6), max(msm7), max(msm8), max(msm9),max(msm10)]
            print('critical path on fastest cpu :', cp_min)
            cp_min = max(cp_min)
            print('makespan of cp on fastest cpu :', cp_min)
            cp = [max(ms1), max(ms2) + path[0], max(ms3) + path[1],
                  max(ms4) + path[2], max(ms5) + path[3], max(ms6),
                  max(ms7) + path[4], max(ms8) + path[5], max(ms9) + path[6],max(ms10)+path[7]]
            print('critical path :', cp)
            cp = max(cp)
            print('makespan of cp :', round(cp,2))
            print('\n----------------------------------')
            print('on p0=4:\n', ms1, '\non p1=12:\n', ms2, '\non p0=4:\n',
                  ms3, '\non p2=7:\n', ms4, '\non p1=12:\n', ms5, '\non p1=12:\n', ms6, '\non p1=12:\n', ms7,
                  '\non p1=12:\n', ms8,'\non p1=12:\n', ms9,'\non p0=4:\n', ms10)
            print('\n----------------------------------------------------------------')
            makespan_cpus = [math.fsum(ms1), math.fsum(ms2) + path[0],
                             math.fsum(ms3) + path[1], math.fsum(ms4) + path[2],
                             math.fsum(ms5) + path[3], math.fsum(ms6), math.fsum(ms7) + path[4]
                , math.fsum(ms8) + path[5], math.fsum(ms9) + path[6], math.fsum(ms10)+path[7]]
            makespan = math.fsum(makespan_cpus)
            print('Makespan is :', round(makespan, 2))

        elif len(x) == 11:
            ms1 = np.round(x[0] / p[0], 2)
            ms2 = np.round(x[1] / p[1], 2)
            ms3 = np.round(x[2] / p[0], 2)
            ms4 = np.round(x[3] / p[2], 2)
            ms5 = np.round(x[4] / p[1], 2)
            ms6 = np.round(x[5] / p[1], 2)
            ms7 = np.round(x[6] / p[0], 2)
            ms8 = np.round(x[7] / p[2], 2)
            ms9 = np.round(x[8] / p[1], 2)
            ms10 = np.round(x[9] / p[0], 2)
            ms11 = np.round(x[10] / p[0], 2)
            run = [ms1, ms2, ms3, ms4, ms5, ms6, ms7, ms8, ms9, ms10,ms11]
            path = np.array([0.5, 0.1, 1, 1.7, 6.6, 11.7, 13.3, 14.79])
            path_sum = math.fsum(path)
            msm1 = np.round(x[0] / p[1], 2)
            msm2 = np.round(x[1] / p[1], 2)
            msm3 = np.round(x[2] / p[1], 2)
            msm4 = np.round(x[3] / p[1], 2)
            msm5 = np.round(x[4] / p[1], 2)
            msm6 = np.round(x[5] / p[1], 2)
            msm7 = np.round(x[6] / p[1], 2)
            msm8 = np.round(x[7] / p[1], 2)
            msm9 = np.round(x[8] / p[1], 2)
            msm10 = np.round(x[9] / p[1], 2)
            msm11 = np.round(x[10] / p[1], 2)
            task_min = [math.fsum(msm1), math.fsum(msm2),
                        math.fsum(msm3), math.fsum(msm4), math.fsum(msm5), math.fsum(msm6), math.fsum(msm7)
                , math.fsum(msm8), math.fsum(msm9), math.fsum(msm10), math.fsum(msm11)]
            task_min = math.fsum(task_min)
            print('Tasks on fastest processor :', round(task_min, 2))
            cp_min = [max(msm1), max(msm2), max(msm3), max(msm4), max(msm5),
                      max(msm6), max(msm7), max(msm8), max(msm9), max(msm10),max(msm11)]
            print('critical path on fastest cpu :', cp_min)
            cp_min = max(cp_min)
            print('makespan of cp on fastest cpu :', cp_min)
            cp = [max(ms1), max(ms2) + path[0], max(ms3) + path[1],
                  max(ms4) + path[2], max(ms5) + path[3], max(ms6),
                  max(ms7) + path[4], max(ms8) + path[5], max(ms9) + path[6], max(ms10) + path[7],max(ms11)]
            print('critical path :', cp)
            cp = max(cp)
            print('makespan of cp :', round(cp,2))
            print('\n----------------------------------')
            print('on p0=4:\n', ms1, '\non p1=12:\n', ms2, '\non p0=4:\n',
                  ms3, '\non p2=7:\n', ms4, '\non p1=12:\n', ms5, '\non p1=12:\n', ms6, '\non p1=12:\n', ms7,
                  '\non p1=12:\n', ms8,'\non p1=12:\n', ms9,'\non p0=4:\n', ms10,'\non p0=4:\n', ms11)
            print('\n----------------------------------------------------------------')
            makespan_cpus = [math.fsum(ms1), math.fsum(ms2) + path[0],
                             math.fsum(ms3) + path[1], math.fsum(ms4) + path[2],
                             math.fsum(ms5) + path[3], math.fsum(ms6), math.fsum(ms7) + path[4]
                , math.fsum(ms8) + path[5], math.fsum(ms9) + path[6],
                             math.fsum(ms10) + path[7], math.fsum(ms11)]
            makespan = math.fsum(makespan_cpus)
            print('Makespan is :', round(makespan, 2))

        elif len(x) == 12:
            ms1 = np.round(x[0] / p[0], 2)
            ms2 = np.round(x[1] / p[1], 2)
            ms3 = np.round(x[2] / p[0], 2)
            ms4 = np.round(x[3] / p[2], 2)
            ms5 = np.round(x[4] / p[1], 2)
            ms6 = np.round(x[5] / p[1], 2)
            ms7 = np.round(x[6] / p[0], 2)
            ms8 = np.round(x[7] / p[2], 2)
            ms9 = np.round(x[8] / p[1], 2)
            ms10 = np.round(x[9] / p[0], 2)
            ms11 = np.round(x[10] / p[0], 2)
            ms12 = np.round(x[11] / p[1], 2)
            run = [ms1, ms2, ms3, ms4, ms5, ms6,
                   ms7, ms8, ms9, ms10, ms11,ms12]
            path = np.array([0.5, 0.1, 1, 1.7, 6.6, 11.7, 13.3, 14.79, 18.4])
            path_sum = math.fsum(path)
            msm1 = np.round(x[0] / p[1], 2)
            msm2 = np.round(x[1] / p[1], 2)
            msm3 = np.round(x[2] / p[1], 2)
            msm4 = np.round(x[3] / p[1], 2)
            msm5 = np.round(x[4] / p[1], 2)
            msm6 = np.round(x[5] / p[1], 2)
            msm7 = np.round(x[6] / p[1], 2)
            msm8 = np.round(x[7] / p[1], 2)
            msm9 = np.round(x[8] / p[1], 2)
            msm10 = np.round(x[9] / p[1], 2)
            msm11 = np.round(x[10] / p[1], 2)
            msm12 = np.round(x[11] / p[1], 2)
            task_min = [math.fsum(msm1), math.fsum(msm2),
                        math.fsum(msm3), math.fsum(msm4), math.fsum(msm5), math.fsum(msm6), math.fsum(msm7)
                , math.fsum(msm8), math.fsum(msm9), math.fsum(msm10), math.fsum(msm11),
                        math.fsum(msm12)]
            task_min = math.fsum(task_min)
            print('Tasks on fastest processor :', round(task_min, 2))
            cp_min = [max(msm1), max(msm2), max(msm3), max(msm4), max(msm5),
                      max(msm6), max(msm7), max(msm8), max(msm9), max(msm10), max(msm11),max(msm12)]
            print('critical path on fastest cpu :', cp_min)
            cp_min = max(cp_min)
            print('makespan of cp on fastest cpu :', cp_min)
            cp = [max(ms1), max(ms2) + path[0], max(ms3) + path[1],
                  max(ms4) + path[2], max(ms5) + path[3], max(ms6),
                  max(ms7) + path[4], max(ms8) + path[5], max(ms9) + path[6],
                  max(ms10) + path[7], max(ms11),max(ms12)+path[8]]
            print('critical path :', cp)
            cp = max(cp)
            print('makespan of cp :', round(cp,2))
            print('\n----------------------------------')
            print('on p0=4:\n', ms1, '\non p1=12:\n', ms2, '\non p0=4:\n',
                  ms3, '\non p2=7:\n', ms4, '\non p1=12:\n', ms5, '\non p1=12:\n', ms6, '\non p1=12:\n', ms7,
                  '\non p1=12:\n', ms8,'\non p1=12:\n', ms9,'\non p0=4:\n', ms10,'\non p0=4:\n',
                  ms11,'\non p1=12:\n', ms12)
            print('\n----------------------------------------------------------------')
            makespan_cpus = [math.fsum(ms1), math.fsum(ms2) + path[0],
                             math.fsum(ms3) + path[1], math.fsum(ms4) + path[2],
                             math.fsum(ms5) + path[3], math.fsum(ms6), math.fsum(ms7) + path[4]
                , math.fsum(ms8) + path[5], math.fsum(ms9) + path[6],
                             math.fsum(ms10) + path[7], math.fsum(ms12)+path[8]]
            makespan = math.fsum(makespan_cpus)
            print('Makespan is :', round(makespan, 2))

        elif len(x) == 13:
            ms1 = np.round(x[0] / p[0], 2)
            ms2 = np.round(x[1] / p[1], 2)
            ms3 = np.round(x[2] / p[0], 2)
            ms4 = np.round(x[3] / p[2], 2)
            ms5 = np.round(x[4] / p[1], 2)
            ms6 = np.round(x[5] / p[1], 2)
            ms7 = np.round(x[6] / p[0], 2)
            ms8 = np.round(x[7] / p[2], 2)
            ms9 = np.round(x[8] / p[1], 2)
            ms10 = np.round(x[9] / p[0], 2)
            ms11 = np.round(x[10] / p[0], 2)
            ms12 = np.round(x[11] / p[1], 2)
            ms13 = np.round(x[12] / p[1], 2)
            run = [ms1, ms2, ms3, ms4, ms5, ms6,
                   ms7, ms8, ms9, ms10, ms11, ms12,ms13]
            path = np.array([0.5, 0.1, 1, 1.7, 6.6, 11.7, 13.3, 14.79, 18.4])
            path_sum = math.fsum(path)
            msm1 = np.round(x[0] / p[1], 2)
            msm2 = np.round(x[1] / p[1], 2)
            msm3 = np.round(x[2] / p[1], 2)
            msm4 = np.round(x[3] / p[1], 2)
            msm5 = np.round(x[4] / p[1], 2)
            msm6 = np.round(x[5] / p[1], 2)
            msm7 = np.round(x[6] / p[1], 2)
            msm8 = np.round(x[7] / p[1], 2)
            msm9 = np.round(x[8] / p[1], 2)
            msm10 = np.round(x[9] / p[1], 2)
            msm11 = np.round(x[10] / p[1], 2)
            msm12 = np.round(x[11] / p[1], 2)
            msm13 = np.round(x[12] / p[1], 2)
            task_min = [math.fsum(msm1), math.fsum(msm2),
                        math.fsum(msm3), math.fsum(msm4), math.fsum(msm5), math.fsum(msm6), math.fsum(msm7)
                , math.fsum(msm8), math.fsum(msm9), math.fsum(msm10), math.fsum(msm11),
                        math.fsum(msm12), math.fsum(msm13)]
            task_min = math.fsum(task_min)
            print('Tasks on fastest processor :', round(task_min, 2))
            cp_min = [max(msm1), max(msm2), max(msm3), max(msm4), max(msm5),
                      max(msm6), max(msm7), max(msm8), max(msm9),
                      max(msm10), max(msm11), max(msm12),max(msm13)]
            print('critical path on fastest cpu :', cp_min)
            cp_min = max(cp_min)
            print('makespan of cp on fastest cpu :', cp_min)
            cp = [max(ms1), max(ms2) + path[0], max(ms3) + path[1],
                  max(ms4) + path[2], max(ms5) + path[3], max(ms6),
                  max(ms7) + path[4], max(ms8) + path[5], max(ms9) + path[6],
                  max(ms10) + path[7], max(ms11), max(ms12) + path[8],max(ms13)]
            print('critical path :', cp)
            cp = max(cp)
            print('makespan of cp :', round(cp,2))
            print('\n----------------------------------')
            print('on p0=4:\n', ms1, '\non p1=12:\n', ms2, '\non p0=4:\n',
                  ms3, '\non p2=7:\n', ms4, '\non p1=12:\n', ms5, '\non p1=12:\n', ms6, '\non p1=12:\n', ms7,
                  '\non p1=12:\n', ms8, '\non p1=12:\n', ms9, '\non p0=4:\n', ms10, '\non p0=4:\n',
                  ms11, '\non p0=4:\n', ms12, '\non p1=12:\n', ms13)
            print('\n----------------------------------------------------------------')
            makespan_cpus = [math.fsum(ms1), math.fsum(ms2) + path[0],
                             math.fsum(ms3) + path[1], math.fsum(ms4) + path[2],
                             math.fsum(ms5) + path[3], math.fsum(ms6), math.fsum(ms7) + path[4]
                , math.fsum(ms8) + path[5], math.fsum(ms9) + path[6],
                             math.fsum(ms10) + path[7],
                             math.fsum(ms12) + path[8], math.fsum(ms13)]
            makespan = math.fsum(makespan_cpus)
            print('Makespan is :', round(makespan, 2))

        elif len(x) == 14:
            ms1 = np.round(x[0] / p[0], 2)
            ms2 = np.round(x[1] / p[1], 2)
            ms3 = np.round(x[2] / p[0], 2)
            ms4 = np.round(x[3] / p[2], 2)
            ms5 = np.round(x[4] / p[1], 2)
            ms6 = np.round(x[5] / p[1], 2)
            ms7 = np.round(x[6] / p[0], 2)
            ms8 = np.round(x[7] / p[2], 2)
            ms9 = np.round(x[8] / p[1], 2)
            ms10 = np.round(x[9] / p[0], 2)
            ms11 = np.round(x[10] / p[0], 2)
            ms12 = np.round(x[11] / p[1], 2)
            ms13 = np.round(x[12] / p[1], 2)
            ms14 = np.round(x[13] / p[2], 2)
            run = [ms1, ms2, ms3, ms4, ms5, ms6,
                   ms7, ms8, ms9, ms10, ms11,
                   ms12, ms13,ms14]
            path = np.array([0.5, 0.1, 1, 1.7, 6.6, 11.7, 13.3, 14.79, 18.4, 19.9])
            path_sum = math.fsum(path)
            msm1 = np.round(x[0] / p[1], 2)
            msm2 = np.round(x[1] / p[1], 2)
            msm3 = np.round(x[2] / p[1], 2)
            msm4 = np.round(x[3] / p[1], 2)
            msm5 = np.round(x[4] / p[1], 2)
            msm6 = np.round(x[5] / p[1], 2)
            msm7 = np.round(x[6] / p[1], 2)
            msm8 = np.round(x[7] / p[1], 2)
            msm9 = np.round(x[8] / p[1], 2)
            msm10 = np.round(x[9] / p[1], 2)
            msm11 = np.round(x[10] / p[1], 2)
            msm12 = np.round(x[11] / p[1], 2)
            msm13 = np.round(x[12] / p[1], 2)
            msm14 = np.round(x[13] / p[1], 2)
            task_min = [math.fsum(msm1), math.fsum(msm2),
                        math.fsum(msm3), math.fsum(msm4), math.fsum(msm5), math.fsum(msm6), math.fsum(msm7)
                , math.fsum(msm8), math.fsum(msm9), math.fsum(msm10), math.fsum(msm11),
                        math.fsum(msm12), math.fsum(msm13), math.fsum(msm14)]
            task_min = math.fsum(task_min)
            print('Tasks on fastest processor :', round(task_min, 2))
            cp_min = [max(msm1), max(msm2), max(msm3), max(msm4), max(msm5),
                      max(msm6), max(msm7), max(msm8), max(msm9),
                      max(msm10), max(msm11), max(msm12), max(msm13),max(msm14)]
            print('critical path on fastest cpu :', cp_min)
            cp_min = max(cp_min)
            print('makespan of cp on fastest cpu :', cp_min)
            cp = [max(ms1), max(ms2) + path[0], max(ms3) + path[1],
                  max(ms4) + path[2], max(ms5) + path[3], max(ms6),
                  max(ms7) + path[4], max(ms8) + path[5], max(ms9) + path[6],
                  max(ms10) + path[7], max(ms11), max(ms12) + path[8], max(ms13),max(ms14)+path[9]]
            print('critical path :', cp)
            cp = max(cp)
            print('makespan of cp :', round(cp,2))
            print('\n----------------------------------')
            print('on p0=4:\n', ms1, '\non p1=12:\n', ms2, '\non p0=4:\n',
                  ms3, '\non p2=7:\n', ms4, '\non p1=12:\n', ms5, '\non p1=12:\n', ms6, '\non p1=12:\n', ms7,
                  '\non p1=12:\n', ms8, '\non p1=12:\n', ms9, '\non p0=4:\n', ms10, '\non p0=4:\n',
                  ms11, '\non p0=4:\n', ms12, '\non p1=12:\n', ms13, '\non p2=7:\n', ms14)
            print('\n----------------------------------------------------------------')
            makespan_cpus = [math.fsum(ms1), math.fsum(ms2) + path[0],
                             math.fsum(ms3) + path[1], math.fsum(ms4) + path[2],
                             math.fsum(ms5) + path[3], math.fsum(ms6), math.fsum(ms7) + path[4]
                , math.fsum(ms8) + path[5], math.fsum(ms9) + path[6],
                             math.fsum(ms10) + path[7],
                             math.fsum(ms12) + path[8],
                             math.fsum(ms13),math.fsum(ms14)+path[9]]
            makespan = math.fsum(makespan_cpus)
            print('Makespan is :', round(makespan, 2))

        elif len(x) == 15:
            ms1 = np.round(x[0] / p[0], 2)
            ms2 = np.round(x[1] / p[1], 2)
            ms3 = np.round(x[2] / p[0], 2)
            ms4 = np.round(x[3] / p[2], 2)
            ms5 = np.round(x[4] / p[1], 2)
            ms6 = np.round(x[5] / p[1], 2)
            ms7 = np.round(x[6] / p[0], 2)
            ms8 = np.round(x[7] / p[2], 2)
            ms9 = np.round(x[8] / p[1], 2)
            ms10 = np.round(x[9] / p[0], 2)
            ms11 = np.round(x[10] / p[0], 2)
            ms12 = np.round(x[11] / p[1], 2)
            ms13 = np.round(x[12] / p[1], 2)
            ms14 = np.round(x[13] / p[2], 2)
            ms15 = np.round(x[14] / p[2], 2)
            run = [ms1, ms2, ms3, ms4, ms5, ms6,
                   ms7, ms8, ms9, ms10, ms11,
                   ms12, ms13, ms14,ms15]
            path = np.array([0.5, 0.1, 1, 1.7, 6.6, 11.7, 13.3, 14.79, 18.4, 19.9])
            path_sum = math.fsum(path)
            msm1 = np.round(x[0] / p[1], 2)
            msm2 = np.round(x[1] / p[1], 2)
            msm3 = np.round(x[2] / p[1], 2)
            msm4 = np.round(x[3] / p[1], 2)
            msm5 = np.round(x[4] / p[1], 2)
            msm6 = np.round(x[5] / p[1], 2)
            msm7 = np.round(x[6] / p[1], 2)
            msm8 = np.round(x[7] / p[1], 2)
            msm9 = np.round(x[8] / p[1], 2)
            msm10 = np.round(x[9] / p[1], 2)
            msm11 = np.round(x[10] / p[1], 2)
            msm12 = np.round(x[11] / p[1], 2)
            msm13 = np.round(x[12] / p[1], 2)
            msm14 = np.round(x[13] / p[1], 2)
            msm15 = np.round(x[14] / p[1], 2)
            task_min = [math.fsum(msm1), math.fsum(msm2),
                        math.fsum(msm3), math.fsum(msm4), math.fsum(msm5), math.fsum(msm6), math.fsum(msm7)
                , math.fsum(msm8), math.fsum(msm9), math.fsum(msm10), math.fsum(msm11),
                        math.fsum(msm12), math.fsum(msm13), math.fsum(msm14), math.fsum(msm15)]
            task_min = math.fsum(task_min)
            print('Tasks on fastest processor :', round(task_min, 2))
            cp_min = [max(msm1), max(msm2), max(msm3), max(msm4), max(msm5),
                      max(msm6), max(msm7), max(msm8), max(msm9),
                      max(msm10), max(msm11), max(msm12), max(msm13), max(msm14), max(msm15)]
            print('critical path on fastest cpu :', cp_min)
            cp_min = max(cp_min)
            print('makespan of cp on fastest cpu :', cp_min)
            cp = [max(ms1), max(ms2) + path[0], max(ms3) + path[1],
                  max(ms4) + path[2], max(ms5) + path[3], max(ms6),
                  max(ms7) + path[4], max(ms8) + path[5], max(ms9) + path[6],
                  max(ms10) + path[7], max(ms11), max(ms12) + path[8],
                  max(ms13), max(ms14) + path[9], max(ms15)]
            print('critical path :', cp)
            cp = max(cp)
            print('makespan of cp :', round(cp,2))
            print('\n----------------------------------')
            print('on p0=4:\n', ms1, '\non p1=12:\n', ms2, '\non p0=4:\n',
                  ms3, '\non p2=7:\n', ms4, '\non p1=12:\n', ms5, '\non p1=12:\n', ms6, '\non p1=12:\n', ms7,
                  '\non p1=12:\n', ms8, '\non p1=12:\n', ms9, '\non p0=4:\n', ms10, '\non p0=4:\n',
                  ms11, '\non p0=4:\n', ms12, '\non p1=12:\n', ms13, '\non p2=7:\n', ms14,
                  '\non p2=7:\n', ms15)
            print('\n----------------------------------------------------------------')
            makespan_cpus = [math.fsum(ms1), math.fsum(ms2) + path[0],
                             math.fsum(ms3) + path[1], math.fsum(ms4) + path[2],
                             math.fsum(ms5) + path[3], math.fsum(ms6), math.fsum(ms7) + path[4]
                , math.fsum(ms8) + path[5], math.fsum(ms9) + path[6],
                             math.fsum(ms10) + path[7],
                             math.fsum(ms12) + path[8],
                             math.fsum(ms13), math.fsum(ms14) + path[9], math.fsum(ms15)]
            makespan = math.fsum(makespan_cpus)
            print('Makespan is :', round(makespan, 2))

        elif len(x) == 16:
            ms1 = np.round(x[0] / p[0], 2)
            ms2 = np.round(x[1] / p[1], 2)
            ms3 = np.round(x[2] / p[0], 2)
            ms4 = np.round(x[3] / p[2], 2)
            ms5 = np.round(x[4] / p[1], 2)
            ms6 = np.round(x[5] / p[1], 2)
            ms7 = np.round(x[6] / p[0], 2)
            ms8 = np.round(x[7] / p[2], 2)
            ms9 = np.round(x[8] / p[1], 2)
            ms10 = np.round(x[9] / p[0], 2)
            ms11 = np.round(x[10] / p[0], 2)
            ms12 = np.round(x[11] / p[1], 2)
            ms13 = np.round(x[12] / p[1], 2)
            ms14 = np.round(x[13] / p[2], 2)
            ms15 = np.round(x[14] / p[2], 2)
            ms16 = np.round(x[15] / p[1], 2)
            run = [ms1, ms2, ms3, ms4, ms5, ms6,
                   ms7, ms8, ms9, ms10, ms11,
                   ms12, ms13, ms14, ms15,ms16]
            path = np.array([0.5, 0.1, 1, 1.7, 6.6, 11.7, 13.3, 14.79, 18.4, 19.9, 19.5, 13.6])
            path_sum = math.fsum(path)
            msm1 = np.round(x[0] / p[1], 2)
            msm2 = np.round(x[1] / p[1], 2)
            msm3 = np.round(x[2] / p[1], 2)
            msm4 = np.round(x[3] / p[1], 2)
            msm5 = np.round(x[4] / p[1], 2)
            msm6 = np.round(x[5] / p[1], 2)
            msm7 = np.round(x[6] / p[1], 2)
            msm8 = np.round(x[7] / p[1], 2)
            msm9 = np.round(x[8] / p[1], 2)
            msm10 = np.round(x[9] / p[1], 2)
            msm11 = np.round(x[10] / p[1], 2)
            msm12 = np.round(x[11] / p[1], 2)
            msm13 = np.round(x[12] / p[1], 2)
            msm14 = np.round(x[13] / p[1], 2)
            msm15 = np.round(x[14] / p[1], 2)
            msm16 = np.round(x[15] / p[1], 2)
            task_min = [math.fsum(msm1), math.fsum(msm2),
                        math.fsum(msm3), math.fsum(msm4), math.fsum(msm5), math.fsum(msm6), math.fsum(msm7)
                , math.fsum(msm8), math.fsum(msm9), math.fsum(msm10), math.fsum(msm11),
                        math.fsum(msm12), math.fsum(msm13), math.fsum(msm14), math.fsum(msm15),
                        math.fsum(msm16)]
            task_min = math.fsum(task_min)
            print('Tasks on fastest processor :', round(task_min, 2))
            cp_min = [max(msm1), max(msm2), max(msm3), max(msm4), max(msm5),
                      max(msm6), max(msm7), max(msm8), max(msm9),
                      max(msm10), max(msm11), max(msm12), max(msm13), max(msm14),max(msm15),max(msm16)]
            print('critical path on fastest cpu :', cp_min)
            cp_min = max(cp_min)
            print('makespan of cp on fastest cpu :', cp_min)
            cp = [max(ms1), max(ms2) + path[0], max(ms3) + path[1],
                  max(ms4) + path[2], max(ms5) + path[3], max(ms6),
                  max(ms7) + path[4], max(ms8) + path[5], max(ms9) + path[6],
                  max(ms10) + path[7], max(ms11), max(ms12) + path[8],
                  max(ms13), max(ms14) + path[9],max(ms15)+path[10],max(ms16)+path[11]]
            print('critical path :', cp)
            cp = max(cp)
            print('makespan of cp :', round(cp,2))
            print('\n----------------------------------')
            print('on p0=4:\n', ms1, '\non p1=12:\n', ms2, '\non p0=4:\n',
                  ms3, '\non p2=7:\n', ms4, '\non p1=12:\n', ms5, '\non p1=12:\n', ms6, '\non p1=12:\n', ms7,
                  '\non p1=12:\n', ms8, '\non p1=12:\n', ms9, '\non p0=4:\n', ms10, '\non p0=4:\n',
                  ms11, '\non p0=4:\n', ms12, '\non p1=12:\n', ms13, '\non p2=7:\n', ms14,
                  '\non p2=7:\n', ms15, '\non p1=12:\n', ms16)
            print('\n----------------------------------------------------------------')
            makespan_cpus = [math.fsum(ms1), math.fsum(ms2) + path[0],
                             math.fsum(ms3) + path[1], math.fsum(ms4) + path[2],
                             math.fsum(ms5) + path[3], math.fsum(ms6), math.fsum(ms7) + path[4]
                , math.fsum(ms8) + path[5], math.fsum(ms9) + path[6],
                             math.fsum(ms10) + path[7],
                             math.fsum(ms12) + path[8],
                             math.fsum(ms13), math.fsum(ms14) + path[9],
                             math.fsum(ms15), math.fsum(ms16)+path[11]]
            makespan = math.fsum(makespan_cpus)
            print('Makespan is :', round(makespan, 2))

        elif len(x) == 17:
            ms1 = np.round(x[0] / p[0], 2)
            ms2 = np.round(x[1] / p[1], 2)
            ms3 = np.round(x[2] / p[0], 2)
            ms4 = np.round(x[3] / p[2], 2)
            ms5 = np.round(x[4] / p[1], 2)
            ms6 = np.round(x[5] / p[1], 2)
            ms7 = np.round(x[6] / p[0], 2)
            ms8 = np.round(x[7] / p[2], 2)
            ms9 = np.round(x[8] / p[1], 2)
            ms10 = np.round(x[9] / p[0], 2)
            ms11 = np.round(x[10] / p[0], 2)
            ms12 = np.round(x[11] / p[1], 2)
            ms13 = np.round(x[12] / p[1], 2)
            ms14 = np.round(x[13] / p[2], 2)
            ms15 = np.round(x[14] / p[2], 2)
            ms16 = np.round(x[15] / p[1], 2)
            ms17 = np.round(x[16] / p[1], 2)
            run = [ms1, ms2, ms3, ms4, ms5, ms6,
                   ms7, ms8, ms9, ms10, ms11, ms12,
                   ms13, ms14, ms15, ms16,ms17]
            path = np.array([0.5, 0.1, 1, 1.7, 6.6, 11.7, 13.3, 14.79, 18.4, 19.9, 19.5, 13.6])
            path_sum = math.fsum(path)
            msm1 = np.round(x[0] / p[1], 2)
            msm2 = np.round(x[1] / p[1], 2)
            msm3 = np.round(x[2] / p[1], 2)
            msm4 = np.round(x[3] / p[1], 2)
            msm5 = np.round(x[4] / p[1], 2)
            msm6 = np.round(x[5] / p[1], 2)
            msm7 = np.round(x[6] / p[1], 2)
            msm8 = np.round(x[7] / p[1], 2)
            msm9 = np.round(x[8] / p[1], 2)
            msm10 = np.round(x[9] / p[1], 2)
            msm11 = np.round(x[10] / p[1], 2)
            msm12 = np.round(x[11] / p[1], 2)
            msm13 = np.round(x[12] / p[1], 2)
            msm14 = np.round(x[13] / p[1], 2)
            msm15 = np.round(x[14] / p[1], 2)
            msm16 = np.round(x[15] / p[1], 2)
            msm17 = np.round(x[16] / p[1], 2)
            task_min = [math.fsum(msm1), math.fsum(msm2),
                        math.fsum(msm3), math.fsum(msm4), math.fsum(msm5), math.fsum(msm6), math.fsum(msm7)
                , math.fsum(msm8), math.fsum(msm9), math.fsum(msm10), math.fsum(msm11),
                        math.fsum(msm12), math.fsum(msm13), math.fsum(msm14), math.fsum(msm15),
                        math.fsum(msm16), math.fsum(msm17)]
            task_min = math.fsum(task_min)
            print('Tasks on fastest processor :', round(task_min, 2))
            cp_min = [max(msm1), max(msm2), max(msm3), max(msm4), max(msm5),
                      max(msm6), max(msm7), max(msm8), max(msm9),
                      max(msm10), max(msm11), max(msm12),
                      max(msm13), max(msm14), max(msm15),max(msm16),max(msm17)]
            print('critical path on fastest cpu :', cp_min)
            cp_min = max(cp_min)
            print('makespan of cp on fastest cpu :', cp_min)
            cp = [max(ms1), max(ms2) + path[0], max(ms3) + path[1],
                  max(ms4) + path[2], max(ms5) + path[3], max(ms6),
                  max(ms7) + path[4], max(ms8) + path[5], max(ms9) + path[6],
                  max(ms10) + path[7], max(ms11), max(ms12) + path[8],
                  max(ms13), max(ms14) + path[9], max(ms15) + path[10],max(ms16)+path[11],max(ms17)]
            print('critical path :', cp)
            cp = max(cp)
            print('makespan of cp :', round(cp,2))
            print('\n----------------------------------')
            print('on p0=4:\n', ms1, '\non p1=12:\n', ms2, '\non p0=4:\n',
                  ms3, '\non p2=7:\n', ms4, '\non p1=12:\n', ms5, '\non p1=12:\n', ms6, '\non p1=12:\n', ms7,
                  '\non p1=12:\n', ms8, '\non p1=12:\n', ms9, '\non p0=4:\n', ms10, '\non p0=4:\n',
                  ms11, '\non p0=4:\n', ms12, '\non p1=12:\n', ms13, '\non p2=7:\n', ms14,
                  '\non p2=7:\n', ms15, '\non p1=12:\n', ms16, '\non p1=12:\n', ms17)
            print('\n----------------------------------------------------------------')
            makespan_cpus = [math.fsum(ms1), math.fsum(ms2) + path[0],
                             math.fsum(ms3) + path[1], math.fsum(ms4) + path[2],
                             math.fsum(ms5) + path[3], math.fsum(ms6), math.fsum(ms7) + path[4]
                , math.fsum(ms8) + path[5], math.fsum(ms9) + path[6],
                             math.fsum(ms10) + path[7],
                             math.fsum(ms12) + path[8],
                             math.fsum(ms13), math.fsum(ms14) + path[9],
                             math.fsum(ms15), math.fsum(ms16) + path[11],math.fsum(ms17)]
            makespan = math.fsum(makespan_cpus)
            print('Makespan is :', round(makespan, 2))

        elif len(x) == 18:
            ms1 = np.round(x[0] / p[0], 2)
            ms2 = np.round(x[1] / p[1], 2)
            ms3 = np.round(x[2] / p[0], 2)
            ms4 = np.round(x[3] / p[2], 2)
            ms5 = np.round(x[4] / p[1], 2)
            ms6 = np.round(x[5] / p[1], 2)
            ms7 = np.round(x[6] / p[0], 2)
            ms8 = np.round(x[7] / p[2], 2)
            ms9 = np.round(x[8] / p[1], 2)
            ms10 = np.round(x[9] / p[0], 2)
            ms11 = np.round(x[10] / p[0], 2)
            ms12 = np.round(x[11] / p[1], 2)
            ms13 = np.round(x[12] / p[1], 2)
            ms14 = np.round(x[13] / p[2], 2)
            ms15 = np.round(x[14] / p[2], 2)
            ms16 = np.round(x[15] / p[1], 2)
            ms17 = np.round(x[16] / p[1], 2)
            ms18 = np.round(x[17] / p[0], 2)
            run = [ms1, ms2, ms3, ms4, ms5, ms6,
                   ms7, ms8, ms9, ms10, ms11, ms12,
                   ms13, ms14, ms15, ms16, ms17,ms18]
            path = np.array([0.5, 0.1, 1, 1.7, 6.6, 11.7, 13.3, 14.79, 18.4, 19.9, 19.5, 13.6, 17.7])
            path_sum = math.fsum(path)
            msm1 = np.round(x[0] / p[1], 2)
            msm2 = np.round(x[1] / p[1], 2)
            msm3 = np.round(x[2] / p[1], 2)
            msm4 = np.round(x[3] / p[1], 2)
            msm5 = np.round(x[4] / p[1], 2)
            msm6 = np.round(x[5] / p[1], 2)
            msm7 = np.round(x[6] / p[1], 2)
            msm8 = np.round(x[7] / p[1], 2)
            msm9 = np.round(x[8] / p[1], 2)
            msm10 = np.round(x[9] / p[1], 2)
            msm11 = np.round(x[10] / p[1], 2)
            msm12 = np.round(x[11] / p[1], 2)
            msm13 = np.round(x[12] / p[1], 2)
            msm14 = np.round(x[13] / p[1], 2)
            msm15 = np.round(x[14] / p[1], 2)
            msm16 = np.round(x[15] / p[1], 2)
            msm17 = np.round(x[16] / p[1], 2)
            msm18 = np.round(x[17] / p[1], 2)
            task_min = [math.fsum(msm1), math.fsum(msm2),
                        math.fsum(msm3), math.fsum(msm4), math.fsum(msm5), math.fsum(msm6), math.fsum(msm7)
                , math.fsum(msm8), math.fsum(msm9), math.fsum(msm10), math.fsum(msm11),
                        math.fsum(msm12), math.fsum(msm13), math.fsum(msm14), math.fsum(msm15),
                        math.fsum(msm16), math.fsum(msm17), math.fsum(msm18)]
            task_min = math.fsum(task_min)
            print('Tasks on fastest processor :', round(task_min, 2))
            cp_min = [max(msm1), max(msm2), max(msm3), max(msm4), max(msm5),
                      max(msm6), max(msm7), max(msm8), max(msm9),
                      max(msm10), max(msm11), max(msm12),
                      max(msm13), max(msm14), max(msm15), max(msm16), max(msm17),max(msm18)]
            print('critical path on fastest cpu :', cp_min)
            cp_min = max(cp_min)
            print('makespan of cp on fastest cpu :', cp_min)
            cp = [max(ms1), max(ms2) + path[0], max(ms3) + path[1],
                  max(ms4) + path[2], max(ms5) + path[3], max(ms6),
                  max(ms7) + path[4], max(ms8) + path[5], max(ms9) + path[6],
                  max(ms10) + path[7], max(ms11), max(ms12) + path[8],
                  max(ms13), max(ms14) + path[9], max(ms15) + path[10], max(ms16), max(ms17),max(ms18)+path[12]]
            print('critical path :', cp)
            cp = max(cp)
            print('makespan of cp :', round(cp,2))
            print('\n----------------------------------')
            print('on p0=4:\n', ms1, '\non p1=12:\n', ms2, '\non p0=4:\n',
                  ms3, '\non p2=7:\n', ms4, '\non p1=12:\n', ms5, '\non p1=12:\n', ms6, '\non p1=12:\n', ms7,
                  '\non p1=12:\n', ms8, '\non p1=12:\n', ms9, '\non p0=4:\n', ms10, '\non p0=4:\n',
                  ms11, '\non p0=4:\n', ms12, '\non p1=12:\n', ms13, '\non p2=7:\n', ms14,
                  '\non p2=7:\n', ms15, '\non p1=12:\n', ms16, '\non p1=12:\n', ms17, '\non p1=12:\n', ms18)
            print('\n----------------------------------------------------------------')
            makespan_cpus = [math.fsum(ms1), math.fsum(ms2) + path[0],
                             math.fsum(ms3) + path[1], math.fsum(ms4) + path[2],
                             math.fsum(ms5) + path[3], math.fsum(ms6), math.fsum(ms7) + path[4]
                , math.fsum(ms8) + path[5], math.fsum(ms9) + path[6],
                             math.fsum(ms10) + path[7],
                             math.fsum(ms12) + path[8],
                             math.fsum(ms13), math.fsum(ms14) + path[9],
                             math.fsum(ms15), math.fsum(ms16) + path[11],
                             math.fsum(ms17),math.fsum(ms18)+path[12]]
            makespan = math.fsum(makespan_cpus)
            print('Makespan is :', round(makespan, 2))

        elif len(x) == 19:
            ms1 = np.round(x[0] / p[0], 2)
            ms2 = np.round(x[1] / p[1], 2)
            ms3 = np.round(x[2] / p[0], 2)
            ms4 = np.round(x[3] / p[2], 2)
            ms5 = np.round(x[4] / p[1], 2)
            ms6 = np.round(x[5] / p[1], 2)
            ms7 = np.round(x[6] / p[0], 2)
            ms8 = np.round(x[7] / p[2], 2)
            ms9 = np.round(x[8] / p[1], 2)
            ms10 = np.round(x[9] / p[0], 2)
            ms11 = np.round(x[10] / p[0], 2)
            ms12 = np.round(x[11] / p[1], 2)
            ms13 = np.round(x[12] / p[1], 2)
            ms14 = np.round(x[13] / p[2], 2)
            ms15 = np.round(x[14] / p[2], 2)
            ms16 = np.round(x[15] / p[1], 2)
            ms17 = np.round(x[16] / p[1], 2)
            ms18 = np.round(x[17] / p[0], 2)
            ms19 = np.round(x[18] / p[0], 2)
            run = [ms1, ms2, ms3, ms4, ms5, ms6,
                   ms7, ms8, ms9, ms10, ms11, ms12,
                   ms13, ms14, ms15, ms16, ms17, ms18,ms19]
            path = np.array([0.5, 0.1, 1, 1.7, 6.6, 11.7, 13.3, 14.79, 18.4, 19.9, 19.5, 13.6, 17.7])
            path_sum = math.fsum(path)
            msm1 = np.round(x[0] / p[1], 2)
            msm2 = np.round(x[1] / p[1], 2)
            msm3 = np.round(x[2] / p[1], 2)
            msm4 = np.round(x[3] / p[1], 2)
            msm5 = np.round(x[4] / p[1], 2)
            msm6 = np.round(x[5] / p[1], 2)
            msm7 = np.round(x[6] / p[1], 2)
            msm8 = np.round(x[7] / p[1], 2)
            msm9 = np.round(x[8] / p[1], 2)
            msm10 = np.round(x[9] / p[1], 2)
            msm11 = np.round(x[10] / p[1], 2)
            msm12 = np.round(x[11] / p[1], 2)
            msm13 = np.round(x[12] / p[1], 2)
            msm14 = np.round(x[13] / p[1], 2)
            msm15 = np.round(x[14] / p[1], 2)
            msm16 = np.round(x[15] / p[1], 2)
            msm17 = np.round(x[16] / p[1], 2)
            msm18 = np.round(x[17] / p[1], 2)
            msm19 = np.round(x[18] / p[1], 2)
            task_min = [math.fsum(msm1), math.fsum(msm2),
                        math.fsum(msm3), math.fsum(msm4), math.fsum(msm5), math.fsum(msm6), math.fsum(msm7)
                , math.fsum(msm8), math.fsum(msm9), math.fsum(msm10), math.fsum(msm11),
                        math.fsum(msm12), math.fsum(msm13), math.fsum(msm14), math.fsum(msm15),
                        math.fsum(msm16), math.fsum(msm17), math.fsum(msm18), math.fsum(msm19)]
            task_min = math.fsum(task_min)
            print('Tasks on fastest processor :', round(task_min,2))
            cp_min = [max(msm1), max(msm2), max(msm3), max(msm4), max(msm5),
                      max(msm6), max(msm7), max(msm8), max(msm9),
                      max(msm10), max(msm11), max(msm12),
                      max(msm13), max(msm14), max(msm15), max(msm16), max(msm17), max(msm18),max(msm19)]
            print('critical path on fastest cpu :', cp_min)
            cp_min = max(cp_min)
            print('makespan of cp on fastest cpu :', cp_min)
            cp = [max(ms1), max(ms2) + path[0], max(ms3) + path[1],
                  max(ms4) + path[2], max(ms5) + path[3], max(ms6),
                  max(ms7) + path[4], max(ms8) + path[5], max(ms9) + path[6],
                  max(ms10) + path[7], max(ms11), max(ms12) + path[8],
                  max(ms13), max(ms14) + path[9], max(ms15) + path[10],
                  max(ms16), max(ms17),max(ms18)+path[12],max(ms19)]
            print('critical path :', cp)
            cp = max(cp)
            print('makespan of cp :', round(cp,2))
            print('\n----------------------------------')
            print('on p0=4:\n', ms1, '\non p1=12:\n', ms2, '\non p0=4:\n',
                  ms3, '\non p2=7:\n', ms4, '\non p1=12:\n', ms5, '\non p1=12:\n', ms6, '\non p1=12:\n', ms7,
                  '\non p1=12:\n', ms8, '\non p1=12:\n', ms9, '\non p0=4:\n', ms10, '\non p0=4:\n',
                  ms11, '\non p0=4:\n', ms12, '\non p1=12:\n', ms13, '\non p2=7:\n', ms14,
                  '\non p2=7:\n', ms15, '\non p1=12:\n', ms16, '\non p1=12:\n', ms17,
                  '\non p1=12:\n', ms18, '\non p0=4:\n', ms19)
            print('\n----------------------------------------------------------------')
            makespan_cpus = [math.fsum(ms1), math.fsum(ms2) + path[0],
                             math.fsum(ms3) + path[1], math.fsum(ms4) + path[2],
                             math.fsum(ms5) + path[3], math.fsum(ms6), math.fsum(ms7) + path[4]
                , math.fsum(ms8) + path[5], math.fsum(ms9) + path[6],
                             math.fsum(ms10) + path[7],
                             math.fsum(ms12) + path[8],
                             math.fsum(ms13), math.fsum(ms14) + path[9],
                             math.fsum(ms15), math.fsum(ms16) + path[11],
                             math.fsum(ms17), math.fsum(ms18) + path[12], math.fsum(ms19)]
            makespan = round(math.fsum(makespan_cpus),2)
            print('Makespan is :', makespan)

        SLR = round(makespan/cp_min,2)
        print('-> SLR is :',SLR)

        Speedup = round(task_min/makespan,2)
        print('-> Speed up is :',Speedup)

        Efficiency = round(Speedup/cpu_len,2)
        print('-> Efficiency is :',Efficiency)
        print('running on CPUS :' , run)
        print('makespan cpus :',makespan_cpus)

        CCR = round(path_sum/makespan,1)
        print('CCR :' ,CCR)

        with open (file_name,'a') as f :
            f.write(str(makespan))
            f.write(',')
        with open(file_name2, 'a') as f:
            f.write(str(SLR))
            f.write(',')
        with open(file_name3, 'a') as f:
            f.write(str(Speedup))
            f.write(',')
        with open(file_name4, 'a') as f:
            f.write(str(CCR))
            f.write(',')
        with open(file_name5, 'a') as f:
            f.write(str(Efficiency))
            f.write(',')
    except TypeError:
        print('\n')
        print('     *************************************************')
        print('     *  Size of input Graph arrays must not be equal *')
        print('     *              Try another Graph !              *')
        print('     *************************************************')

def Metrics (x=list) :
    try:
        if x[0:len(x)] == x[0:len(x)]:
            x[0].append(0)
        x = np.array(x,dtype=object)
        p = np.array([4,12,7])
        cpu_len = len(p)

        file_name = 'C:/Users/Naweed/PycharmProjects/IHHO/Metrics/Makespan data set.txt'
        file_name2 = 'C:/Users/Naweed/PycharmProjects/IHHO/Metrics/SLR data set.txt'
        file_name3 = 'C:/Users/Naweed/PycharmProjects/IHHO/Metrics/Speed up data set.txt'
        file_name4 = 'C:/Users/Naweed/PycharmProjects/IHHO/Metrics/CCR data set.txt'
        file_name5 = 'C:/Users/Naweed/PycharmProjects/IHHO/Metrics/Efficiency data set.txt'

        if len(x) == 3 :
            ms1 = np.round(x[0] / p[0],2)
            ms2 = np.round(x[1] / p[1],2)
            ms3 = np.round(x[2] / p[0],2)
            run = [ms1,ms2,ms3]

            path = np.array([0.5, 0.1])
            path_sum = math.fsum(path)
            msm1 = np.round(x[0] / p[1], 2)
            msm2 = np.round(x[1] / p[1], 2)
            msm3 = np.round(x[2] / p[1], 2)

            task_min = [math.fsum(msm1), math.fsum(msm2),
                        math.fsum(msm3)]
            task_min = math.fsum(task_min)
            print('Tasks on fastest processor :', round(task_min, 2))
            cp_min = [max(msm1),max(msm2),max(msm3)]
            print('critical path on fastest cpu :',cp_min)
            cp_min = max(cp_min)
            print('makespan of cp on fastest cpu :',cp_min)
            cp = [max(ms1),max(ms2)+path[0],max(ms3)+path[1]]
            print('critical path :',cp)
            cp = max(cp)
            print('makespan of cp :', round(cp,2))
            print('\n----------------------------------')
            print('on p0=4:\n', ms1, '\non p1=12:\n', ms2, '\non p0=4:\n', ms3)
            print('\n----------------------------------------------------------------')
            makespan_cpus = [math.fsum(ms1),math.fsum(ms2)+path[0],
                             math.fsum(ms3)+path[1]]
            makespan = math.fsum(makespan_cpus)
            print('Makespan is :',round(makespan,2))

        if len(x) == 4 :
            ms1 = np.round(x[0] / p[0],2)
            ms2 = np.round(x[1] / p[1],2)
            ms3 = np.round(x[2] / p[0],2)
            ms4 = np.round(x[3] / p[2],2)
            run = [ms1,ms2,ms3,ms4]

            path = np.array([0.5, 0.1, 1])
            path_sum = math.fsum(path)
            msm1 = np.round(x[0] / p[1], 2)
            msm2 = np.round(x[1] / p[1], 2)
            msm3 = np.round(x[2] / p[1], 2)
            msm4 = np.round(x[3] / p[1], 2)
            task_min = [math.fsum(msm1), math.fsum(msm2),
                        math.fsum(msm3), math.fsum(msm4)]
            task_min = math.fsum(task_min)
            print('Tasks on fastest processor :', round(task_min, 2))
            cp_min = [max(msm1),max(msm2),max(msm3),max(msm4)]
            print('critical path on fastest cpu :',cp_min)
            cp_min = max(cp_min)
            print('makespan of cp on fastest cpu :',cp_min)
            cp = [max(ms1),max(ms2)+path[0],max(ms3)+path[1],max(ms4)+path[2]]
            print('critical path :',cp)
            cp = max(cp)
            print('makespan of cp :', round(cp,2))
            print('\n----------------------------------')
            print('on p0=4:\n', ms1, '\non p1=12:\n', ms2, '\non p0=4:\n', ms3, '\non p2=7:\n', ms4)
            print('\n----------------------------------------------------------------')
            makespan_cpus = [math.fsum(ms1),math.fsum(ms2)+path[0],
                             math.fsum(ms3)+path[1],math.fsum(ms4)+path[2]]
            makespan = math.fsum(makespan_cpus)
            print('Makespan is :',round(makespan,2))

        elif len(x) == 5 :
            ms1 = np.round(x[0]/p[0],2)
            ms2 = np.round(x[1] / p[1],2)
            ms3 = np.round(x[2] / p[0],2)
            ms4 = np.round(x[3] / p[2],2)
            ms5 = np.round(x[4] / p[1], 2)
            run = [ms1, ms2, ms3, ms4,ms5]
            path = np.array([0.5, 0.1, 1, 1.7])
            path_sum = math.fsum(path)
            msm1 = np.round(x[0] / p[1], 2)
            msm2 = np.round(x[1] / p[1], 2)
            msm3 = np.round(x[2] / p[1], 2)
            msm4 = np.round(x[3] / p[1], 2)
            msm5 = np.round(x[4] / p[1], 2)
            task_min = [math.fsum(msm1), math.fsum(msm2),
                        math.fsum(msm3), math.fsum(msm4), math.fsum(msm5)]
            task_min = math.fsum(task_min)
            print('Tasks on fastest processor :', round(task_min, 2))
            cp_min = [max(msm1), max(msm2), max(msm3), max(msm4),max(ms5)]
            print('critical path on fastest cpu :', cp_min)
            cp_min = max(cp_min)
            print('makespan of cp on fastest cpu :', cp_min)
            cp = [max(ms1),max(ms2)+path[0],max(ms3)+path[1],max(ms4)+path[2],max(ms5)+path[3]]
            print('critical path :', cp)
            cp = max(cp)
            print('makespan of cp :', round(cp,2))
            print('\n----------------------------------')
            print('on p0=4:\n', ms1, '\non p1=12:\n', ms2, '\non p0=4:\n', ms3, '\non p2=7:\n', ms4,'\non p1=12:\n', ms5)
            print('\n----------------------------------------------------------------')
            makespan_cpus = [math.fsum(ms1), math.fsum(ms2) + path[0],
                             math.fsum(ms3) + path[1], math.fsum(ms4) + path[2],math.fsum(ms5)+path[3]]
            makespan = math.fsum(makespan_cpus)
            print('Makespan is :',round(makespan,2))

        elif len(x) == 6:
            ms1 = np.round(x[0] / p[0], 2)
            ms2 = np.round(x[1] / p[1], 2)
            ms3 = np.round(x[2] / p[0], 2)
            ms4 = np.round(x[3] / p[2], 2)
            ms5 = np.round(x[4] / p[1], 2)
            ms6 = np.round(x[5] / p[1], 2)
            run = [ms1, ms2, ms3, ms4, ms5,ms6]
            path = np.array([0.5, 0.1, 1, 1.7])
            path_sum = math.fsum(path)
            msm1 = np.round(x[0] / p[1], 2)
            msm2 = np.round(x[1] / p[1], 2)
            msm3 = np.round(x[2] / p[1], 2)
            msm4 = np.round(x[3] / p[1], 2)
            msm5 = np.round(x[4] / p[1], 2)
            msm6 = np.round(x[5] / p[1], 2)
            task_min = [math.fsum(msm1), math.fsum(msm2),
                        math.fsum(msm3), math.fsum(msm4), math.fsum(msm5), math.fsum(msm6)]
            task_min = math.fsum(task_min)
            print('Tasks on fastest processor :', round(task_min, 2))
            cp_min = [max(msm1), max(msm2), max(msm3), max(msm4), max(msm5),max(msm6)]
            print('critical path on fastest cpu :', cp_min)
            cp_min = max(cp_min)
            print('makespan of cp on fastest cpu :', cp_min)
            cp = [max(ms1), max(ms2) + path[0], max(ms3) + path[1],
                  max(ms4) + path[2], max(ms5) + path[3],max(ms6)]
            print('critical path :', cp)
            cp = max(cp)
            print('makespan of cp :', round(cp,2))
            print('\n----------------------------------')
            print('on p0=4:\n', ms1, '\non p1=12:\n', ms2, '\non p0=4:\n',
            ms3, '\non p2=7:\n', ms4, '\non p1=12:\n', ms5,'\non p1=12:\n', ms6)
            print('\n----------------------------------------------------------------')
            makespan_cpus = [math.fsum(ms1), math.fsum(ms2) + path[0],
                             math.fsum(ms3) + path[1], math.fsum(ms4) + path[2],
                             math.fsum(ms5) + path[3],math.fsum(ms6)]
            makespan = math.fsum(makespan_cpus)
            print('Makespan is :', round(makespan, 2))

        elif len(x) == 7:
            ms1 = np.round(x[0] / p[0], 2)
            ms2 = np.round(x[1] / p[1], 2)
            ms3 = np.round(x[2] / p[0], 2)
            ms4 = np.round(x[3] / p[2], 2)
            ms5 = np.round(x[4] / p[1], 2)
            ms6 = np.round(x[5] / p[1], 2)
            ms7 = np.round(x[6] / p[0], 2)
            run = [ms1, ms2, ms3, ms4, ms5, ms6,ms7]
            path = np.array([0.5, 0.1, 1, 1.7, 6.6])
            path_sum = math.fsum(path)
            msm1 = np.round(x[0] / p[1], 2)
            msm2 = np.round(x[1] / p[1], 2)
            msm3 = np.round(x[2] / p[1], 2)
            msm4 = np.round(x[3] / p[1], 2)
            msm5 = np.round(x[4] / p[1], 2)
            msm6 = np.round(x[5] / p[1], 2)
            msm7 = np.round(x[6] / p[1], 2)
            task_min = [math.fsum(msm1), math.fsum(msm2),
                        math.fsum(msm3), math.fsum(msm4), math.fsum(msm5), math.fsum(msm6), math.fsum(msm7)]
            task_min = math.fsum(task_min)
            print('Tasks on fastest processor :', round(task_min, 2))
            cp_min = [max(msm1), max(msm2), max(msm3), max(msm4), max(msm5), max(msm6),max(msm7)]
            print('critical path on fastest cpu :', cp_min)
            cp_min = max(cp_min)
            print('makespan of cp on fastest cpu :', cp_min)
            cp = [max(ms1), max(ms2) + path[0], max(ms3) + path[1],
                  max(ms4) + path[2], max(ms5) + path[3], max(ms6),max(ms7)+path[4]]
            print('critical path :', cp)
            cp = max(cp)
            print('makespan of cp :', round(cp,2))
            print('\n----------------------------------')
            print('on p0=4:\n', ms1, '\non p1=12:\n', ms2, '\non p0=4:\n',
            ms3, '\non p2=7:\n', ms4, '\non p1=12:\n', ms5,'\non p1=12:\n', ms6,'\non p1=12:\n', ms7)
            print('\n----------------------------------------------------------------')
            makespan_cpus = [math.fsum(ms1), math.fsum(ms2) + path[0],
                             math.fsum(ms3) + path[1], math.fsum(ms4) + path[2],
                             math.fsum(ms5) + path[3], math.fsum(ms6),math.fsum(ms7)+path[4]]
            makespan = math.fsum(makespan_cpus)
            print('Makespan is :', round(makespan, 2))

        elif len(x) == 8:
            ms1 = np.round(x[0] / p[0], 2)
            ms2 = np.round(x[1] / p[1], 2)
            ms3 = np.round(x[2] / p[0], 2)
            ms4 = np.round(x[3] / p[2], 2)
            ms5 = np.round(x[4] / p[1], 2)
            ms6 = np.round(x[5] / p[1], 2)
            ms7 = np.round(x[6] / p[0], 2)
            ms8 = np.round(x[7] / p[2], 2)
            run = [ms1, ms2, ms3, ms4, ms5, ms6, ms7,ms8]
            path = np.array([0.5, 0.1, 1, 1.7, 6.6, 11.7])
            path_sum = math.fsum(path)
            msm1 = np.round(x[0] / p[1], 2)
            msm2 = np.round(x[1] / p[1], 2)
            msm3 = np.round(x[2] / p[1], 2)
            msm4 = np.round(x[3] / p[1], 2)
            msm5 = np.round(x[4] / p[1], 2)
            msm6 = np.round(x[5] / p[1], 2)
            msm7 = np.round(x[6] / p[1], 2)
            msm8 = np.round(x[7] / p[1], 2)
            task_min = [math.fsum(msm1), math.fsum(msm2),
                        math.fsum(msm3), math.fsum(msm4), math.fsum(msm5), math.fsum(msm6), math.fsum(msm7)
                , math.fsum(msm8)]
            task_min = math.fsum(task_min)
            print('Tasks on fastest processor :', round(task_min, 2))
            cp_min = [max(msm1), max(msm2), max(msm3), max(msm4), max(msm5), max(msm6), max(msm7),max(msm8)]
            print('critical path on fastest cpu :', cp_min)
            cp_min = max(cp_min)
            print('makespan of cp on fastest cpu :', cp_min)
            cp = [max(ms1), max(ms2) + path[0], max(ms3) + path[1],
                  max(ms4) + path[2], max(ms5) + path[3], max(ms6), max(ms7) + path[4],max(ms8)+path[5]]
            print('critical path :', cp)
            cp = max(cp)
            print('makespan of cp :', round(cp,2))
            print('\n----------------------------------')
            print('on p0=4:\n', ms1, '\non p1=12:\n', ms2, '\non p0=4:\n',
            ms3, '\non p2=7:\n', ms4, '\non p1=12:\n', ms5,'\non p1=12:\n', ms6,'\non p1=12:\n', ms7,
                  '\non p2=7:\n', ms8)
            print('\n----------------------------------------------------------------')
            makespan_cpus = [math.fsum(ms1), math.fsum(ms2) + path[0],
                             math.fsum(ms3) + path[1], math.fsum(ms4) + path[2],
                             math.fsum(ms5) + path[3], math.fsum(ms6), math.fsum(ms7) + path[4]
                ,math.fsum(ms8)+path[5]]
            makespan = math.fsum(makespan_cpus)
            print('Makespan is :', round(makespan, 2))

        elif len(x) == 9:
            ms1 = np.round(x[0] / p[0], 2)
            ms2 = np.round(x[1] / p[1], 2)
            ms3 = np.round(x[2] / p[0], 2)
            ms4 = np.round(x[3] / p[2], 2)
            ms5 = np.round(x[4] / p[1], 2)
            ms6 = np.round(x[5] / p[1], 2)
            ms7 = np.round(x[6] / p[0], 2)
            ms8 = np.round(x[7] / p[2], 2)
            ms9 = np.round(x[8] / p[1], 2)
            run = [ms1, ms2, ms3, ms4, ms5, ms6, ms7, ms8,ms9]
            path = np.array([0.5, 0.1, 1, 1.7, 6.6, 11.7, 13.3])
            path_sum = math.fsum(path)
            msm1 = np.round(x[0] / p[1], 2)
            msm2 = np.round(x[1] / p[1], 2)
            msm3 = np.round(x[2] / p[1], 2)
            msm4 = np.round(x[3] / p[1], 2)
            msm5 = np.round(x[4] / p[1], 2)
            msm6 = np.round(x[5] / p[1], 2)
            msm7 = np.round(x[6] / p[1], 2)
            msm8 = np.round(x[7] / p[1], 2)
            msm9 = np.round(x[8] / p[1], 2)
            task_min = [math.fsum(msm1), math.fsum(msm2),
                        math.fsum(msm3), math.fsum(msm4), math.fsum(msm5), math.fsum(msm6), math.fsum(msm7)
                , math.fsum(msm8), math.fsum(msm9)]
            task_min = math.fsum(task_min)
            print('Tasks on fastest processor :', round(task_min, 2))
            cp_min = [max(msm1), max(msm2), max(msm3), max(msm4), max(msm5),
                      max(msm6), max(msm7), max(msm8),max(msm9)]
            print('critical path on fastest cpu :', cp_min)
            cp_min = max(cp_min)
            print('makespan of cp on fastest cpu :', cp_min)
            cp = [max(ms1), max(ms2) + path[0], max(ms3) + path[1],
                  max(ms4) + path[2], max(ms5) + path[3], max(ms6),
                  max(ms7) + path[4], max(ms8) + path[5],max(ms9) + path[6]]
            print('critical path :', cp)
            cp = max(cp)
            print('makespan of cp :', round(cp,2))
            print('\n----------------------------------')
            print('on p0=4:\n', ms1, '\non p1=12:\n', ms2, '\non p0=4:\n',
                  ms3, '\non p2=7:\n', ms4, '\non p1=12:\n', ms5, '\non p1=12:\n', ms6, '\non p1=12:\n', ms7,
                  '\non p1=12:\n', ms8, '\non p1=12:\n', ms9)
            print('\n----------------------------------------------------------------')
            makespan_cpus = [math.fsum(ms1), math.fsum(ms2) + path[0],
                             math.fsum(ms3) + path[1], math.fsum(ms4) + path[2],
                             math.fsum(ms5) + path[3], math.fsum(ms6), math.fsum(ms7) + path[4]
                , math.fsum(ms8) + path[5], math.fsum(ms9)+path[6]]
            makespan = math.fsum(makespan_cpus)
            print('Makespan is :', round(makespan, 2))

        elif len(x) == 10:
            ms1 = np.round(x[0] / p[0], 2)
            ms2 = np.round(x[1] / p[1], 2)
            ms3 = np.round(x[2] / p[0], 2)
            ms4 = np.round(x[3] / p[2], 2)
            ms5 = np.round(x[4] / p[1], 2)
            ms6 = np.round(x[5] / p[1], 2)
            ms7 = np.round(x[6] / p[0], 2)
            ms8 = np.round(x[7] / p[2], 2)
            ms9 = np.round(x[8] / p[1], 2)
            ms10 = np.round(x[9] / p[0], 2)
            run = [ms1, ms2, ms3, ms4, ms5, ms6, ms7, ms8, ms9,ms10]
            path = np.array([0.5, 0.1, 1, 1.7, 6.6, 11.7, 13.3, 14.79])
            path_sum = math.fsum(path)
            msm1 = np.round(x[0] / p[1], 2)
            msm2 = np.round(x[1] / p[1], 2)
            msm3 = np.round(x[2] / p[1], 2)
            msm4 = np.round(x[3] / p[1], 2)
            msm5 = np.round(x[4] / p[1], 2)
            msm6 = np.round(x[5] / p[1], 2)
            msm7 = np.round(x[6] / p[1], 2)
            msm8 = np.round(x[7] / p[1], 2)
            msm9 = np.round(x[8] / p[1], 2)
            msm10 = np.round(x[9] / p[1], 2)
            task_min = [math.fsum(msm1), math.fsum(msm2),
                        math.fsum(msm3), math.fsum(msm4), math.fsum(msm5), math.fsum(msm6), math.fsum(msm7)
                , math.fsum(msm8), math.fsum(msm9), math.fsum(msm10)]
            task_min = math.fsum(task_min)
            print('Tasks on fastest processor :', round(task_min, 2))
            cp_min = [max(msm1), max(msm2), max(msm3), max(msm4), max(msm5),
                      max(msm6), max(msm7), max(msm8), max(msm9),max(msm10)]
            print('critical path on fastest cpu :', cp_min)
            cp_min = max(cp_min)
            print('makespan of cp on fastest cpu :', cp_min)
            cp = [max(ms1), max(ms2) + path[0], max(ms3) + path[1],
                  max(ms4) + path[2], max(ms5) + path[3], max(ms6),
                  max(ms7) + path[4], max(ms8) + path[5], max(ms9) + path[6],max(ms10)+path[7]]
            print('critical path :', cp)
            cp = max(cp)
            print('makespan of cp :', round(cp,2))
            print('\n----------------------------------')
            print('on p0=4:\n', ms1, '\non p1=12:\n', ms2, '\non p0=4:\n',
                  ms3, '\non p2=7:\n', ms4, '\non p1=12:\n', ms5, '\non p1=12:\n', ms6, '\non p1=12:\n', ms7,
                  '\non p1=12:\n', ms8,'\non p1=12:\n', ms9,'\non p0=4:\n', ms10)
            print('\n----------------------------------------------------------------')
            makespan_cpus = [math.fsum(ms1), math.fsum(ms2) + path[0],
                             math.fsum(ms3) + path[1], math.fsum(ms4) + path[2],
                             math.fsum(ms5) + path[3], math.fsum(ms6), math.fsum(ms7) + path[4]
                , math.fsum(ms8) + path[5], math.fsum(ms9) + path[6], math.fsum(ms10)+path[7]]
            makespan = math.fsum(makespan_cpus)
            print('Makespan is :', round(makespan, 2))

        elif len(x) == 11:
            ms1 = np.round(x[0] / p[0], 2)
            ms2 = np.round(x[1] / p[1], 2)
            ms3 = np.round(x[2] / p[0], 2)
            ms4 = np.round(x[3] / p[2], 2)
            ms5 = np.round(x[4] / p[1], 2)
            ms6 = np.round(x[5] / p[1], 2)
            ms7 = np.round(x[6] / p[0], 2)
            ms8 = np.round(x[7] / p[2], 2)
            ms9 = np.round(x[8] / p[1], 2)
            ms10 = np.round(x[9] / p[0], 2)
            ms11 = np.round(x[10] / p[0], 2)
            run = [ms1, ms2, ms3, ms4, ms5, ms6, ms7, ms8, ms9, ms10,ms11]
            path = np.array([0.5, 0.1, 1, 1.7, 6.6, 11.7, 13.3, 14.79])
            path_sum = math.fsum(path)
            msm1 = np.round(x[0] / p[1], 2)
            msm2 = np.round(x[1] / p[1], 2)
            msm3 = np.round(x[2] / p[1], 2)
            msm4 = np.round(x[3] / p[1], 2)
            msm5 = np.round(x[4] / p[1], 2)
            msm6 = np.round(x[5] / p[1], 2)
            msm7 = np.round(x[6] / p[1], 2)
            msm8 = np.round(x[7] / p[1], 2)
            msm9 = np.round(x[8] / p[1], 2)
            msm10 = np.round(x[9] / p[1], 2)
            msm11 = np.round(x[10] / p[1], 2)
            task_min = [math.fsum(msm1), math.fsum(msm2),
                        math.fsum(msm3), math.fsum(msm4), math.fsum(msm5), math.fsum(msm6), math.fsum(msm7)
                , math.fsum(msm8), math.fsum(msm9), math.fsum(msm10), math.fsum(msm11)]
            task_min = math.fsum(task_min)
            print('Tasks on fastest processor :', round(task_min, 2))
            cp_min = [max(msm1), max(msm2), max(msm3), max(msm4), max(msm5),
                      max(msm6), max(msm7), max(msm8), max(msm9), max(msm10),max(msm11)]
            print('critical path on fastest cpu :', cp_min)
            cp_min = max(cp_min)
            print('makespan of cp on fastest cpu :', cp_min)
            cp = [max(ms1), max(ms2) + path[0], max(ms3) + path[1],
                  max(ms4) + path[2], max(ms5) + path[3], max(ms6),
                  max(ms7) + path[4], max(ms8) + path[5], max(ms9) + path[6], max(ms10) + path[7],max(ms11)]
            print('critical path :', cp)
            cp = max(cp)
            print('makespan of cp :', round(cp,2))
            print('\n----------------------------------')
            print('on p0=4:\n', ms1, '\non p1=12:\n', ms2, '\non p0=4:\n',
                  ms3, '\non p2=7:\n', ms4, '\non p1=12:\n', ms5, '\non p1=12:\n', ms6, '\non p1=12:\n', ms7,
                  '\non p1=12:\n', ms8,'\non p1=12:\n', ms9,'\non p0=4:\n', ms10,'\non p0=4:\n', ms11)
            print('\n----------------------------------------------------------------')
            makespan_cpus = [math.fsum(ms1), math.fsum(ms2) + path[0],
                             math.fsum(ms3) + path[1], math.fsum(ms4) + path[2],
                             math.fsum(ms5) + path[3], math.fsum(ms6), math.fsum(ms7) + path[4]
                , math.fsum(ms8) + path[5], math.fsum(ms9) + path[6],
                             math.fsum(ms10) + path[7], math.fsum(ms11)]
            makespan = math.fsum(makespan_cpus)
            print('Makespan is :', round(makespan, 2))

        elif len(x) == 12:
            ms1 = np.round(x[0] / p[0], 2)
            ms2 = np.round(x[1] / p[1], 2)
            ms3 = np.round(x[2] / p[0], 2)
            ms4 = np.round(x[3] / p[2], 2)
            ms5 = np.round(x[4] / p[1], 2)
            ms6 = np.round(x[5] / p[1], 2)
            ms7 = np.round(x[6] / p[0], 2)
            ms8 = np.round(x[7] / p[2], 2)
            ms9 = np.round(x[8] / p[1], 2)
            ms10 = np.round(x[9] / p[0], 2)
            ms11 = np.round(x[10] / p[0], 2)
            ms12 = np.round(x[11] / p[1], 2)
            run = [ms1, ms2, ms3, ms4, ms5, ms6,
                   ms7, ms8, ms9, ms10, ms11,ms12]
            path = np.array([0.5, 0.1, 1, 1.7, 6.6, 11.7, 13.3, 14.79, 18.4])
            path_sum = math.fsum(path)
            msm1 = np.round(x[0] / p[1], 2)
            msm2 = np.round(x[1] / p[1], 2)
            msm3 = np.round(x[2] / p[1], 2)
            msm4 = np.round(x[3] / p[1], 2)
            msm5 = np.round(x[4] / p[1], 2)
            msm6 = np.round(x[5] / p[1], 2)
            msm7 = np.round(x[6] / p[1], 2)
            msm8 = np.round(x[7] / p[1], 2)
            msm9 = np.round(x[8] / p[1], 2)
            msm10 = np.round(x[9] / p[1], 2)
            msm11 = np.round(x[10] / p[1], 2)
            msm12 = np.round(x[11] / p[1], 2)
            task_min = [math.fsum(msm1), math.fsum(msm2),
                        math.fsum(msm3), math.fsum(msm4), math.fsum(msm5), math.fsum(msm6), math.fsum(msm7)
                , math.fsum(msm8), math.fsum(msm9), math.fsum(msm10), math.fsum(msm11),
                        math.fsum(msm12)]
            task_min = math.fsum(task_min)
            print('Tasks on fastest processor :', round(task_min, 2))
            cp_min = [max(msm1), max(msm2), max(msm3), max(msm4), max(msm5),
                      max(msm6), max(msm7), max(msm8), max(msm9), max(msm10), max(msm11),max(msm12)]
            print('critical path on fastest cpu :', cp_min)
            cp_min = max(cp_min)
            print('makespan of cp on fastest cpu :', cp_min)
            cp = [max(ms1), max(ms2) + path[0], max(ms3) + path[1],
                  max(ms4) + path[2], max(ms5) + path[3], max(ms6),
                  max(ms7) + path[4], max(ms8) + path[5], max(ms9) + path[6],
                  max(ms10) + path[7], max(ms11),max(ms12)+path[8]]
            print('critical path :', cp)
            cp = max(cp)
            print('makespan of cp :', round(cp,2))
            print('\n----------------------------------')
            print('on p0=4:\n', ms1, '\non p1=12:\n', ms2, '\non p0=4:\n',
                  ms3, '\non p2=7:\n', ms4, '\non p1=12:\n', ms5, '\non p1=12:\n', ms6, '\non p1=12:\n', ms7,
                  '\non p1=12:\n', ms8,'\non p1=12:\n', ms9,'\non p0=4:\n', ms10,'\non p0=4:\n',
                  ms11,'\non p1=12:\n', ms12)
            print('\n----------------------------------------------------------------')
            makespan_cpus = [math.fsum(ms1), math.fsum(ms2) + path[0],
                             math.fsum(ms3) + path[1], math.fsum(ms4) + path[2],
                             math.fsum(ms5) + path[3], math.fsum(ms6), math.fsum(ms7) + path[4]
                , math.fsum(ms8) + path[5], math.fsum(ms9) + path[6],
                             math.fsum(ms10) + path[7], math.fsum(ms12)+path[8]]
            makespan = math.fsum(makespan_cpus)
            print('Makespan is :', round(makespan, 2))

        elif len(x) == 13:
            ms1 = np.round(x[0] / p[0], 2)
            ms2 = np.round(x[1] / p[1], 2)
            ms3 = np.round(x[2] / p[0], 2)
            ms4 = np.round(x[3] / p[2], 2)
            ms5 = np.round(x[4] / p[1], 2)
            ms6 = np.round(x[5] / p[1], 2)
            ms7 = np.round(x[6] / p[0], 2)
            ms8 = np.round(x[7] / p[2], 2)
            ms9 = np.round(x[8] / p[1], 2)
            ms10 = np.round(x[9] / p[0], 2)
            ms11 = np.round(x[10] / p[0], 2)
            ms12 = np.round(x[11] / p[1], 2)
            ms13 = np.round(x[12] / p[1], 2)
            run = [ms1, ms2, ms3, ms4, ms5, ms6,
                   ms7, ms8, ms9, ms10, ms11, ms12,ms13]
            path = np.array([0.5, 0.1, 1, 1.7, 6.6, 11.7, 13.3, 14.79, 18.4])
            path_sum = math.fsum(path)
            msm1 = np.round(x[0] / p[1], 2)
            msm2 = np.round(x[1] / p[1], 2)
            msm3 = np.round(x[2] / p[1], 2)
            msm4 = np.round(x[3] / p[1], 2)
            msm5 = np.round(x[4] / p[1], 2)
            msm6 = np.round(x[5] / p[1], 2)
            msm7 = np.round(x[6] / p[1], 2)
            msm8 = np.round(x[7] / p[1], 2)
            msm9 = np.round(x[8] / p[1], 2)
            msm10 = np.round(x[9] / p[1], 2)
            msm11 = np.round(x[10] / p[1], 2)
            msm12 = np.round(x[11] / p[1], 2)
            msm13 = np.round(x[12] / p[1], 2)
            task_min = [math.fsum(msm1), math.fsum(msm2),
                        math.fsum(msm3), math.fsum(msm4), math.fsum(msm5), math.fsum(msm6), math.fsum(msm7)
                , math.fsum(msm8), math.fsum(msm9), math.fsum(msm10), math.fsum(msm11),
                        math.fsum(msm12), math.fsum(msm13)]
            task_min = math.fsum(task_min)
            print('Tasks on fastest processor :', round(task_min, 2))
            cp_min = [max(msm1), max(msm2), max(msm3), max(msm4), max(msm5),
                      max(msm6), max(msm7), max(msm8), max(msm9),
                      max(msm10), max(msm11), max(msm12),max(msm13)]
            print('critical path on fastest cpu :', cp_min)
            cp_min = max(cp_min)
            print('makespan of cp on fastest cpu :', cp_min)
            cp = [max(ms1), max(ms2) + path[0], max(ms3) + path[1],
                  max(ms4) + path[2], max(ms5) + path[3], max(ms6),
                  max(ms7) + path[4], max(ms8) + path[5], max(ms9) + path[6],
                  max(ms10) + path[7], max(ms11), max(ms12) + path[8],max(ms13)]
            print('critical path :', cp)
            cp = max(cp)
            print('makespan of cp :', round(cp,2))
            print('\n----------------------------------')
            print('on p0=4:\n', ms1, '\non p1=12:\n', ms2, '\non p0=4:\n',
                  ms3, '\non p2=7:\n', ms4, '\non p1=12:\n', ms5, '\non p1=12:\n', ms6, '\non p1=12:\n', ms7,
                  '\non p1=12:\n', ms8, '\non p1=12:\n', ms9, '\non p0=4:\n', ms10, '\non p0=4:\n',
                  ms11, '\non p0=4:\n', ms12, '\non p1=12:\n', ms13)
            print('\n----------------------------------------------------------------')
            makespan_cpus = [math.fsum(ms1), math.fsum(ms2) + path[0],
                             math.fsum(ms3) + path[1], math.fsum(ms4) + path[2],
                             math.fsum(ms5) + path[3], math.fsum(ms6), math.fsum(ms7) + path[4]
                , math.fsum(ms8) + path[5], math.fsum(ms9) + path[6],
                             math.fsum(ms10) + path[7],
                             math.fsum(ms12) + path[8], math.fsum(ms13)]
            makespan = math.fsum(makespan_cpus)
            print('Makespan is :', round(makespan, 2))

        elif len(x) == 14:
            ms1 = np.round(x[0] / p[0], 2)
            ms2 = np.round(x[1] / p[1], 2)
            ms3 = np.round(x[2] / p[0], 2)
            ms4 = np.round(x[3] / p[2], 2)
            ms5 = np.round(x[4] / p[1], 2)
            ms6 = np.round(x[5] / p[1], 2)
            ms7 = np.round(x[6] / p[0], 2)
            ms8 = np.round(x[7] / p[2], 2)
            ms9 = np.round(x[8] / p[1], 2)
            ms10 = np.round(x[9] / p[0], 2)
            ms11 = np.round(x[10] / p[0], 2)
            ms12 = np.round(x[11] / p[1], 2)
            ms13 = np.round(x[12] / p[1], 2)
            ms14 = np.round(x[13] / p[2], 2)
            run = [ms1, ms2, ms3, ms4, ms5, ms6,
                   ms7, ms8, ms9, ms10, ms11,
                   ms12, ms13,ms14]
            path = np.array([0.5, 0.1, 1, 1.7, 6.6, 11.7, 13.3, 14.79, 18.4, 19.9])
            path_sum = math.fsum(path)
            msm1 = np.round(x[0] / p[1], 2)
            msm2 = np.round(x[1] / p[1], 2)
            msm3 = np.round(x[2] / p[1], 2)
            msm4 = np.round(x[3] / p[1], 2)
            msm5 = np.round(x[4] / p[1], 2)
            msm6 = np.round(x[5] / p[1], 2)
            msm7 = np.round(x[6] / p[1], 2)
            msm8 = np.round(x[7] / p[1], 2)
            msm9 = np.round(x[8] / p[1], 2)
            msm10 = np.round(x[9] / p[1], 2)
            msm11 = np.round(x[10] / p[1], 2)
            msm12 = np.round(x[11] / p[1], 2)
            msm13 = np.round(x[12] / p[1], 2)
            msm14 = np.round(x[13] / p[1], 2)
            task_min = [math.fsum(msm1), math.fsum(msm2),
                        math.fsum(msm3), math.fsum(msm4), math.fsum(msm5), math.fsum(msm6), math.fsum(msm7)
                , math.fsum(msm8), math.fsum(msm9), math.fsum(msm10), math.fsum(msm11),
                        math.fsum(msm12), math.fsum(msm13), math.fsum(msm14)]
            task_min = math.fsum(task_min)
            print('Tasks on fastest processor :', round(task_min, 2))
            cp_min = [max(msm1), max(msm2), max(msm3), max(msm4), max(msm5),
                      max(msm6), max(msm7), max(msm8), max(msm9),
                      max(msm10), max(msm11), max(msm12), max(msm13),max(msm14)]
            print('critical path on fastest cpu :', cp_min)
            cp_min = max(cp_min)
            print('makespan of cp on fastest cpu :', cp_min)
            cp = [max(ms1), max(ms2) + path[0], max(ms3) + path[1],
                  max(ms4) + path[2], max(ms5) + path[3], max(ms6),
                  max(ms7) + path[4], max(ms8) + path[5], max(ms9) + path[6],
                  max(ms10) + path[7], max(ms11), max(ms12) + path[8], max(ms13),max(ms14)+path[9]]
            print('critical path :', cp)
            cp = max(cp)
            print('makespan of cp :', round(cp,2))
            print('\n----------------------------------')
            print('on p0=4:\n', ms1, '\non p1=12:\n', ms2, '\non p0=4:\n',
                  ms3, '\non p2=7:\n', ms4, '\non p1=12:\n', ms5, '\non p1=12:\n', ms6, '\non p1=12:\n', ms7,
                  '\non p1=12:\n', ms8, '\non p1=12:\n', ms9, '\non p0=4:\n', ms10, '\non p0=4:\n',
                  ms11, '\non p0=4:\n', ms12, '\non p1=12:\n', ms13, '\non p2=7:\n', ms14)
            print('\n----------------------------------------------------------------')
            makespan_cpus = [math.fsum(ms1), math.fsum(ms2) + path[0],
                             math.fsum(ms3) + path[1], math.fsum(ms4) + path[2],
                             math.fsum(ms5) + path[3], math.fsum(ms6), math.fsum(ms7) + path[4]
                , math.fsum(ms8) + path[5], math.fsum(ms9) + path[6],
                             math.fsum(ms10) + path[7],
                             math.fsum(ms12) + path[8],
                             math.fsum(ms13),math.fsum(ms14)+path[9]]
            makespan = math.fsum(makespan_cpus)
            print('Makespan is :', round(makespan, 2))

        elif len(x) == 15:
            ms1 = np.round(x[0] / p[0], 2)
            ms2 = np.round(x[1] / p[1], 2)
            ms3 = np.round(x[2] / p[0], 2)
            ms4 = np.round(x[3] / p[2], 2)
            ms5 = np.round(x[4] / p[1], 2)
            ms6 = np.round(x[5] / p[1], 2)
            ms7 = np.round(x[6] / p[0], 2)
            ms8 = np.round(x[7] / p[2], 2)
            ms9 = np.round(x[8] / p[1], 2)
            ms10 = np.round(x[9] / p[0], 2)
            ms11 = np.round(x[10] / p[0], 2)
            ms12 = np.round(x[11] / p[1], 2)
            ms13 = np.round(x[12] / p[1], 2)
            ms14 = np.round(x[13] / p[2], 2)
            ms15 = np.round(x[14] / p[2], 2)
            run = [ms1, ms2, ms3, ms4, ms5, ms6,
                   ms7, ms8, ms9, ms10, ms11,
                   ms12, ms13, ms14,ms15]
            path = np.array([0.5, 0.1, 1, 1.7, 6.6, 11.7, 13.3, 14.79, 18.4, 19.9])
            path_sum = math.fsum(path)
            msm1 = np.round(x[0] / p[1], 2)
            msm2 = np.round(x[1] / p[1], 2)
            msm3 = np.round(x[2] / p[1], 2)
            msm4 = np.round(x[3] / p[1], 2)
            msm5 = np.round(x[4] / p[1], 2)
            msm6 = np.round(x[5] / p[1], 2)
            msm7 = np.round(x[6] / p[1], 2)
            msm8 = np.round(x[7] / p[1], 2)
            msm9 = np.round(x[8] / p[1], 2)
            msm10 = np.round(x[9] / p[1], 2)
            msm11 = np.round(x[10] / p[1], 2)
            msm12 = np.round(x[11] / p[1], 2)
            msm13 = np.round(x[12] / p[1], 2)
            msm14 = np.round(x[13] / p[1], 2)
            msm15 = np.round(x[14] / p[1], 2)
            task_min = [math.fsum(msm1), math.fsum(msm2),
                        math.fsum(msm3), math.fsum(msm4), math.fsum(msm5), math.fsum(msm6), math.fsum(msm7)
                , math.fsum(msm8), math.fsum(msm9), math.fsum(msm10), math.fsum(msm11),
                        math.fsum(msm12), math.fsum(msm13), math.fsum(msm14), math.fsum(msm15)]
            task_min = math.fsum(task_min)
            print('Tasks on fastest processor :', round(task_min, 2))
            cp_min = [max(msm1), max(msm2), max(msm3), max(msm4), max(msm5),
                      max(msm6), max(msm7), max(msm8), max(msm9),
                      max(msm10), max(msm11), max(msm12), max(msm13), max(msm14), max(msm15)]
            print('critical path on fastest cpu :', cp_min)
            cp_min = max(cp_min)
            print('makespan of cp on fastest cpu :', cp_min)
            cp = [max(ms1), max(ms2) + path[0], max(ms3) + path[1],
                  max(ms4) + path[2], max(ms5) + path[3], max(ms6),
                  max(ms7) + path[4], max(ms8) + path[5], max(ms9) + path[6],
                  max(ms10) + path[7], max(ms11), max(ms12) + path[8],
                  max(ms13), max(ms14) + path[9], max(ms15)]
            print('critical path :', cp)
            cp = max(cp)
            print('makespan of cp :', round(cp,2))
            print('\n----------------------------------')
            print('on p0=4:\n', ms1, '\non p1=12:\n', ms2, '\non p0=4:\n',
                  ms3, '\non p2=7:\n', ms4, '\non p1=12:\n', ms5, '\non p1=12:\n', ms6, '\non p1=12:\n', ms7,
                  '\non p1=12:\n', ms8, '\non p1=12:\n', ms9, '\non p0=4:\n', ms10, '\non p0=4:\n',
                  ms11, '\non p0=4:\n', ms12, '\non p1=12:\n', ms13, '\non p2=7:\n', ms14,
                  '\non p2=7:\n', ms15)
            print('\n----------------------------------------------------------------')
            makespan_cpus = [math.fsum(ms1), math.fsum(ms2) + path[0],
                             math.fsum(ms3) + path[1], math.fsum(ms4) + path[2],
                             math.fsum(ms5) + path[3], math.fsum(ms6), math.fsum(ms7) + path[4]
                , math.fsum(ms8) + path[5], math.fsum(ms9) + path[6],
                             math.fsum(ms10) + path[7],
                             math.fsum(ms12) + path[8],
                             math.fsum(ms13), math.fsum(ms14) + path[9], math.fsum(ms15)]
            makespan = math.fsum(makespan_cpus)
            print('Makespan is :', round(makespan, 2))

        elif len(x) == 16:
            ms1 = np.round(x[0] / p[0], 2)
            ms2 = np.round(x[1] / p[1], 2)
            ms3 = np.round(x[2] / p[0], 2)
            ms4 = np.round(x[3] / p[2], 2)
            ms5 = np.round(x[4] / p[1], 2)
            ms6 = np.round(x[5] / p[1], 2)
            ms7 = np.round(x[6] / p[0], 2)
            ms8 = np.round(x[7] / p[2], 2)
            ms9 = np.round(x[8] / p[1], 2)
            ms10 = np.round(x[9] / p[0], 2)
            ms11 = np.round(x[10] / p[0], 2)
            ms12 = np.round(x[11] / p[1], 2)
            ms13 = np.round(x[12] / p[1], 2)
            ms14 = np.round(x[13] / p[2], 2)
            ms15 = np.round(x[14] / p[2], 2)
            ms16 = np.round(x[15] / p[1], 2)
            run = [ms1, ms2, ms3, ms4, ms5, ms6,
                   ms7, ms8, ms9, ms10, ms11,
                   ms12, ms13, ms14, ms15,ms16]
            path = np.array([0.5, 0.1, 1, 1.7, 6.6, 11.7, 13.3, 14.79, 18.4, 19.9, 19.5, 13.6])
            path_sum = math.fsum(path)
            msm1 = np.round(x[0] / p[1], 2)
            msm2 = np.round(x[1] / p[1], 2)
            msm3 = np.round(x[2] / p[1], 2)
            msm4 = np.round(x[3] / p[1], 2)
            msm5 = np.round(x[4] / p[1], 2)
            msm6 = np.round(x[5] / p[1], 2)
            msm7 = np.round(x[6] / p[1], 2)
            msm8 = np.round(x[7] / p[1], 2)
            msm9 = np.round(x[8] / p[1], 2)
            msm10 = np.round(x[9] / p[1], 2)
            msm11 = np.round(x[10] / p[1], 2)
            msm12 = np.round(x[11] / p[1], 2)
            msm13 = np.round(x[12] / p[1], 2)
            msm14 = np.round(x[13] / p[1], 2)
            msm15 = np.round(x[14] / p[1], 2)
            msm16 = np.round(x[15] / p[1], 2)
            task_min = [math.fsum(msm1), math.fsum(msm2),
                        math.fsum(msm3), math.fsum(msm4), math.fsum(msm5), math.fsum(msm6), math.fsum(msm7)
                , math.fsum(msm8), math.fsum(msm9), math.fsum(msm10), math.fsum(msm11),
                        math.fsum(msm12), math.fsum(msm13), math.fsum(msm14), math.fsum(msm15),
                        math.fsum(msm16)]
            task_min = math.fsum(task_min)
            print('Tasks on fastest processor :', round(task_min, 2))
            cp_min = [max(msm1), max(msm2), max(msm3), max(msm4), max(msm5),
                      max(msm6), max(msm7), max(msm8), max(msm9),
                      max(msm10), max(msm11), max(msm12), max(msm13), max(msm14),max(msm15),max(msm16)]
            print('critical path on fastest cpu :', cp_min)
            cp_min = max(cp_min)
            print('makespan of cp on fastest cpu :', cp_min)
            cp = [max(ms1), max(ms2) + path[0], max(ms3) + path[1],
                  max(ms4) + path[2], max(ms5) + path[3], max(ms6),
                  max(ms7) + path[4], max(ms8) + path[5], max(ms9) + path[6],
                  max(ms10) + path[7], max(ms11), max(ms12) + path[8],
                  max(ms13), max(ms14) + path[9],max(ms15)+path[10],max(ms16)+path[11]]
            print('critical path :', cp)
            cp = max(cp)
            print('makespan of cp :', round(cp,2))
            print('\n----------------------------------')
            print('on p0=4:\n', ms1, '\non p1=12:\n', ms2, '\non p0=4:\n',
                  ms3, '\non p2=7:\n', ms4, '\non p1=12:\n', ms5, '\non p1=12:\n', ms6, '\non p1=12:\n', ms7,
                  '\non p1=12:\n', ms8, '\non p1=12:\n', ms9, '\non p0=4:\n', ms10, '\non p0=4:\n',
                  ms11, '\non p0=4:\n', ms12, '\non p1=12:\n', ms13, '\non p2=7:\n', ms14,
                  '\non p2=7:\n', ms15, '\non p1=12:\n', ms16)
            print('\n----------------------------------------------------------------')
            makespan_cpus = [math.fsum(ms1), math.fsum(ms2) + path[0],
                             math.fsum(ms3) + path[1], math.fsum(ms4) + path[2],
                             math.fsum(ms5) + path[3], math.fsum(ms6), math.fsum(ms7) + path[4]
                , math.fsum(ms8) + path[5], math.fsum(ms9) + path[6],
                             math.fsum(ms10) + path[7],
                             math.fsum(ms12) + path[8],
                             math.fsum(ms13), math.fsum(ms14) + path[9],
                             math.fsum(ms15), math.fsum(ms16)+path[11]]
            makespan = math.fsum(makespan_cpus)
            print('Makespan is :', round(makespan, 2))

        elif len(x) == 17:
            ms1 = np.round(x[0] / p[0], 2)
            ms2 = np.round(x[1] / p[1], 2)
            ms3 = np.round(x[2] / p[0], 2)
            ms4 = np.round(x[3] / p[2], 2)
            ms5 = np.round(x[4] / p[1], 2)
            ms6 = np.round(x[5] / p[1], 2)
            ms7 = np.round(x[6] / p[0], 2)
            ms8 = np.round(x[7] / p[2], 2)
            ms9 = np.round(x[8] / p[1], 2)
            ms10 = np.round(x[9] / p[0], 2)
            ms11 = np.round(x[10] / p[0], 2)
            ms12 = np.round(x[11] / p[1], 2)
            ms13 = np.round(x[12] / p[1], 2)
            ms14 = np.round(x[13] / p[2], 2)
            ms15 = np.round(x[14] / p[2], 2)
            ms16 = np.round(x[15] / p[1], 2)
            ms17 = np.round(x[16] / p[1], 2)
            run = [ms1, ms2, ms3, ms4, ms5, ms6,
                   ms7, ms8, ms9, ms10, ms11, ms12,
                   ms13, ms14, ms15, ms16,ms17]
            path = np.array([0.5, 0.1, 1, 1.7, 6.6, 11.7, 13.3, 14.79, 18.4, 19.9, 19.5, 13.6])
            path_sum = math.fsum(path)
            msm1 = np.round(x[0] / p[1], 2)
            msm2 = np.round(x[1] / p[1], 2)
            msm3 = np.round(x[2] / p[1], 2)
            msm4 = np.round(x[3] / p[1], 2)
            msm5 = np.round(x[4] / p[1], 2)
            msm6 = np.round(x[5] / p[1], 2)
            msm7 = np.round(x[6] / p[1], 2)
            msm8 = np.round(x[7] / p[1], 2)
            msm9 = np.round(x[8] / p[1], 2)
            msm10 = np.round(x[9] / p[1], 2)
            msm11 = np.round(x[10] / p[1], 2)
            msm12 = np.round(x[11] / p[1], 2)
            msm13 = np.round(x[12] / p[1], 2)
            msm14 = np.round(x[13] / p[1], 2)
            msm15 = np.round(x[14] / p[1], 2)
            msm16 = np.round(x[15] / p[1], 2)
            msm17 = np.round(x[16] / p[1], 2)
            task_min = [math.fsum(msm1), math.fsum(msm2),
                        math.fsum(msm3), math.fsum(msm4), math.fsum(msm5), math.fsum(msm6), math.fsum(msm7)
                , math.fsum(msm8), math.fsum(msm9), math.fsum(msm10), math.fsum(msm11),
                        math.fsum(msm12), math.fsum(msm13), math.fsum(msm14), math.fsum(msm15),
                        math.fsum(msm16), math.fsum(msm17)]
            task_min = math.fsum(task_min)
            print('Tasks on fastest processor :', round(task_min, 2))
            cp_min = [max(msm1), max(msm2), max(msm3), max(msm4), max(msm5),
                      max(msm6), max(msm7), max(msm8), max(msm9),
                      max(msm10), max(msm11), max(msm12),
                      max(msm13), max(msm14), max(msm15),max(msm16),max(msm17)]
            print('critical path on fastest cpu :', cp_min)
            cp_min = max(cp_min)
            print('makespan of cp on fastest cpu :', cp_min)
            cp = [max(ms1), max(ms2) + path[0], max(ms3) + path[1],
                  max(ms4) + path[2], max(ms5) + path[3], max(ms6),
                  max(ms7) + path[4], max(ms8) + path[5], max(ms9) + path[6],
                  max(ms10) + path[7], max(ms11), max(ms12) + path[8],
                  max(ms13), max(ms14) + path[9], max(ms15) + path[10],max(ms16)+path[11],max(ms17)]
            print('critical path :', cp)
            cp = max(cp)
            print('makespan of cp :', round(cp,2))
            print('\n----------------------------------')
            print('on p0=4:\n', ms1, '\non p1=12:\n', ms2, '\non p0=4:\n',
                  ms3, '\non p2=7:\n', ms4, '\non p1=12:\n', ms5, '\non p1=12:\n', ms6, '\non p1=12:\n', ms7,
                  '\non p1=12:\n', ms8, '\non p1=12:\n', ms9, '\non p0=4:\n', ms10, '\non p0=4:\n',
                  ms11, '\non p0=4:\n', ms12, '\non p1=12:\n', ms13, '\non p2=7:\n', ms14,
                  '\non p2=7:\n', ms15, '\non p1=12:\n', ms16, '\non p1=12:\n', ms17)
            print('\n----------------------------------------------------------------')
            makespan_cpus = [math.fsum(ms1), math.fsum(ms2) + path[0],
                             math.fsum(ms3) + path[1], math.fsum(ms4) + path[2],
                             math.fsum(ms5) + path[3], math.fsum(ms6), math.fsum(ms7) + path[4]
                , math.fsum(ms8) + path[5], math.fsum(ms9) + path[6],
                             math.fsum(ms10) + path[7],
                             math.fsum(ms12) + path[8],
                             math.fsum(ms13), math.fsum(ms14) + path[9],
                             math.fsum(ms15), math.fsum(ms16) + path[11],math.fsum(ms17)]
            makespan = math.fsum(makespan_cpus)
            print('Makespan is :', round(makespan, 2))

        elif len(x) == 18:
            ms1 = np.round(x[0] / p[0], 2)
            ms2 = np.round(x[1] / p[1], 2)
            ms3 = np.round(x[2] / p[0], 2)
            ms4 = np.round(x[3] / p[2], 2)
            ms5 = np.round(x[4] / p[1], 2)
            ms6 = np.round(x[5] / p[1], 2)
            ms7 = np.round(x[6] / p[0], 2)
            ms8 = np.round(x[7] / p[2], 2)
            ms9 = np.round(x[8] / p[1], 2)
            ms10 = np.round(x[9] / p[0], 2)
            ms11 = np.round(x[10] / p[0], 2)
            ms12 = np.round(x[11] / p[1], 2)
            ms13 = np.round(x[12] / p[1], 2)
            ms14 = np.round(x[13] / p[2], 2)
            ms15 = np.round(x[14] / p[2], 2)
            ms16 = np.round(x[15] / p[1], 2)
            ms17 = np.round(x[16] / p[1], 2)
            ms18 = np.round(x[17] / p[0], 2)
            run = [ms1, ms2, ms3, ms4, ms5, ms6,
                   ms7, ms8, ms9, ms10, ms11, ms12,
                   ms13, ms14, ms15, ms16, ms17,ms18]
            path = np.array([0.5, 0.1, 1, 1.7, 6.6, 11.7, 13.3, 14.79, 18.4, 19.9, 19.5, 13.6, 17.7])
            path_sum = math.fsum(path)
            msm1 = np.round(x[0] / p[1], 2)
            msm2 = np.round(x[1] / p[1], 2)
            msm3 = np.round(x[2] / p[1], 2)
            msm4 = np.round(x[3] / p[1], 2)
            msm5 = np.round(x[4] / p[1], 2)
            msm6 = np.round(x[5] / p[1], 2)
            msm7 = np.round(x[6] / p[1], 2)
            msm8 = np.round(x[7] / p[1], 2)
            msm9 = np.round(x[8] / p[1], 2)
            msm10 = np.round(x[9] / p[1], 2)
            msm11 = np.round(x[10] / p[1], 2)
            msm12 = np.round(x[11] / p[1], 2)
            msm13 = np.round(x[12] / p[1], 2)
            msm14 = np.round(x[13] / p[1], 2)
            msm15 = np.round(x[14] / p[1], 2)
            msm16 = np.round(x[15] / p[1], 2)
            msm17 = np.round(x[16] / p[1], 2)
            msm18 = np.round(x[17] / p[1], 2)
            task_min = [math.fsum(msm1), math.fsum(msm2),
                        math.fsum(msm3), math.fsum(msm4), math.fsum(msm5), math.fsum(msm6), math.fsum(msm7)
                , math.fsum(msm8), math.fsum(msm9), math.fsum(msm10), math.fsum(msm11),
                        math.fsum(msm12), math.fsum(msm13), math.fsum(msm14), math.fsum(msm15),
                        math.fsum(msm16), math.fsum(msm17), math.fsum(msm18)]
            task_min = math.fsum(task_min)
            print('Tasks on fastest processor :', round(task_min, 2))
            cp_min = [max(msm1), max(msm2), max(msm3), max(msm4), max(msm5),
                      max(msm6), max(msm7), max(msm8), max(msm9),
                      max(msm10), max(msm11), max(msm12),
                      max(msm13), max(msm14), max(msm15), max(msm16), max(msm17),max(msm18)]
            print('critical path on fastest cpu :', cp_min)
            cp_min = max(cp_min)
            print('makespan of cp on fastest cpu :', cp_min)
            cp = [max(ms1), max(ms2) + path[0], max(ms3) + path[1],
                  max(ms4) + path[2], max(ms5) + path[3], max(ms6),
                  max(ms7) + path[4], max(ms8) + path[5], max(ms9) + path[6],
                  max(ms10) + path[7], max(ms11), max(ms12) + path[8],
                  max(ms13), max(ms14) + path[9], max(ms15) + path[10], max(ms16), max(ms17),max(ms18)+path[12]]
            print('critical path :', cp)
            cp = max(cp)
            print('makespan of cp :', round(cp,2))
            print('\n----------------------------------')
            print('on p0=4:\n', ms1, '\non p1=12:\n', ms2, '\non p0=4:\n',
                  ms3, '\non p2=7:\n', ms4, '\non p1=12:\n', ms5, '\non p1=12:\n', ms6, '\non p1=12:\n', ms7,
                  '\non p1=12:\n', ms8, '\non p1=12:\n', ms9, '\non p0=4:\n', ms10, '\non p0=4:\n',
                  ms11, '\non p0=4:\n', ms12, '\non p1=12:\n', ms13, '\non p2=7:\n', ms14,
                  '\non p2=7:\n', ms15, '\non p1=12:\n', ms16, '\non p1=12:\n', ms17, '\non p1=12:\n', ms18)
            print('\n----------------------------------------------------------------')
            makespan_cpus = [math.fsum(ms1), math.fsum(ms2) + path[0],
                             math.fsum(ms3) + path[1], math.fsum(ms4) + path[2],
                             math.fsum(ms5) + path[3], math.fsum(ms6), math.fsum(ms7) + path[4]
                , math.fsum(ms8) + path[5], math.fsum(ms9) + path[6],
                             math.fsum(ms10) + path[7],
                             math.fsum(ms12) + path[8],
                             math.fsum(ms13), math.fsum(ms14) + path[9],
                             math.fsum(ms15), math.fsum(ms16) + path[11],
                             math.fsum(ms17),math.fsum(ms18)+path[12]]
            makespan = math.fsum(makespan_cpus)
            print('Makespan is :', round(makespan, 2))

        elif len(x) == 19:
            ms1 = np.round(x[0] / p[0], 2)
            ms2 = np.round(x[1] / p[1], 2)
            ms3 = np.round(x[2] / p[0], 2)
            ms4 = np.round(x[3] / p[2], 2)
            ms5 = np.round(x[4] / p[1], 2)
            ms6 = np.round(x[5] / p[1], 2)
            ms7 = np.round(x[6] / p[0], 2)
            ms8 = np.round(x[7] / p[2], 2)
            ms9 = np.round(x[8] / p[1], 2)
            ms10 = np.round(x[9] / p[0], 2)
            ms11 = np.round(x[10] / p[0], 2)
            ms12 = np.round(x[11] / p[1], 2)
            ms13 = np.round(x[12] / p[1], 2)
            ms14 = np.round(x[13] / p[2], 2)
            ms15 = np.round(x[14] / p[2], 2)
            ms16 = np.round(x[15] / p[1], 2)
            ms17 = np.round(x[16] / p[1], 2)
            ms18 = np.round(x[17] / p[0], 2)
            ms19 = np.round(x[18] / p[0], 2)
            run = [ms1, ms2, ms3, ms4, ms5, ms6,
                   ms7, ms8, ms9, ms10, ms11, ms12,
                   ms13, ms14, ms15, ms16, ms17, ms18,ms19]
            path = np.array([0.5, 0.1, 1, 1.7, 6.6, 11.7, 13.3, 14.79, 18.4, 19.9, 19.5, 13.6, 17.7])
            path_sum = math.fsum(path)
            msm1 = np.round(x[0] / p[1], 2)
            msm2 = np.round(x[1] / p[1], 2)
            msm3 = np.round(x[2] / p[1], 2)
            msm4 = np.round(x[3] / p[1], 2)
            msm5 = np.round(x[4] / p[1], 2)
            msm6 = np.round(x[5] / p[1], 2)
            msm7 = np.round(x[6] / p[1], 2)
            msm8 = np.round(x[7] / p[1], 2)
            msm9 = np.round(x[8] / p[1], 2)
            msm10 = np.round(x[9] / p[1], 2)
            msm11 = np.round(x[10] / p[1], 2)
            msm12 = np.round(x[11] / p[1], 2)
            msm13 = np.round(x[12] / p[1], 2)
            msm14 = np.round(x[13] / p[1], 2)
            msm15 = np.round(x[14] / p[1], 2)
            msm16 = np.round(x[15] / p[1], 2)
            msm17 = np.round(x[16] / p[1], 2)
            msm18 = np.round(x[17] / p[1], 2)
            msm19 = np.round(x[18] / p[1], 2)
            task_min = [math.fsum(msm1), math.fsum(msm2),
                        math.fsum(msm3), math.fsum(msm4), math.fsum(msm5), math.fsum(msm6), math.fsum(msm7)
                , math.fsum(msm8), math.fsum(msm9), math.fsum(msm10), math.fsum(msm11),
                        math.fsum(msm12), math.fsum(msm13), math.fsum(msm14), math.fsum(msm15),
                        math.fsum(msm16), math.fsum(msm17), math.fsum(msm18), math.fsum(msm19)]
            task_min = math.fsum(task_min)
            print('Tasks on fastest processor :', round(task_min,2))
            cp_min = [max(msm1), max(msm2), max(msm3), max(msm4), max(msm5),
                      max(msm6), max(msm7), max(msm8), max(msm9),
                      max(msm10), max(msm11), max(msm12),
                      max(msm13), max(msm14), max(msm15), max(msm16), max(msm17), max(msm18),max(msm19)]
            print('critical path on fastest cpu :', cp_min)
            cp_min = max(cp_min)
            print('makespan of cp on fastest cpu :', cp_min)
            cp = [max(ms1), max(ms2) + path[0], max(ms3) + path[1],
                  max(ms4) + path[2], max(ms5) + path[3], max(ms6),
                  max(ms7) + path[4], max(ms8) + path[5], max(ms9) + path[6],
                  max(ms10) + path[7], max(ms11), max(ms12) + path[8],
                  max(ms13), max(ms14) + path[9], max(ms15) + path[10],
                  max(ms16), max(ms17),max(ms18)+path[12],max(ms19)]
            print('critical path :', cp)
            cp = max(cp)
            print('makespan of cp :', round(cp,2))
            print('\n----------------------------------')
            print('on p0=4:\n', ms1, '\non p1=12:\n', ms2, '\non p0=4:\n',
                  ms3, '\non p2=7:\n', ms4, '\non p1=12:\n', ms5, '\non p1=12:\n', ms6, '\non p1=12:\n', ms7,
                  '\non p1=12:\n', ms8, '\non p1=12:\n', ms9, '\non p0=4:\n', ms10, '\non p0=4:\n',
                  ms11, '\non p0=4:\n', ms12, '\non p1=12:\n', ms13, '\non p2=7:\n', ms14,
                  '\non p2=7:\n', ms15, '\non p1=12:\n', ms16, '\non p1=12:\n', ms17,
                  '\non p1=12:\n', ms18, '\non p0=4:\n', ms19)
            print('\n----------------------------------------------------------------')
            makespan_cpus = [math.fsum(ms1), math.fsum(ms2) + path[0],
                             math.fsum(ms3) + path[1], math.fsum(ms4) + path[2],
                             math.fsum(ms5) + path[3], math.fsum(ms6), math.fsum(ms7) + path[4]
                , math.fsum(ms8) + path[5], math.fsum(ms9) + path[6],
                             math.fsum(ms10) + path[7],
                             math.fsum(ms12) + path[8],
                             math.fsum(ms13), math.fsum(ms14) + path[9],
                             math.fsum(ms15), math.fsum(ms16) + path[11],
                             math.fsum(ms17), math.fsum(ms18) + path[12], math.fsum(ms19)]
            makespan = round(math.fsum(makespan_cpus),2)
            print('Makespan is :', makespan)

        SLR = round(makespan/cp_min,2)
        print('-> SLR is :',SLR)

        Speedup = round(task_min/makespan,2)
        print('-> Speed up is :',Speedup)

        Efficiency = round(Speedup/cpu_len,2)
        print('-> Efficiency is :',Efficiency)
        print('running on CPUS :' , run)
        print('makespan cpus :',makespan_cpus)

        CCR = round(path_sum/makespan,1)
        print('CCR :' ,CCR)

        with open (file_name,'a') as f :
            f.write(str(makespan))
            f.write(',')
        with open(file_name2, 'a') as f:
            f.write(str(SLR))
            f.write(',')
        with open(file_name3, 'a') as f:
            f.write(str(Speedup))
            f.write(',')
        with open(file_name4, 'a') as f:
            f.write(str(CCR))
            f.write(',')
        with open(file_name5, 'a') as f:
            f.write(str(Efficiency))
            f.write(',')
            if len(run) == 3 :
                fn = 'C:/Users/Naweed/PycharmProjects/IHHO/HHO Dataset/IHHO run1.xlsx'
                with xlsxwriter.Workbook(fn) as workbook:
                    worksheet = workbook.add_worksheet('run')
                    worksheet.write(0, 0, 'Makespan:')
                    worksheet.write(0, 1, makespan)
                    worksheet.write(1, 0, 'SLR:')
                    worksheet.write(1, 1, SLR)
                    worksheet.write(2, 0, 'Speedup:')
                    worksheet.write(2, 1, Speedup)
                    worksheet.write(3, 0, 'Efficiency:')
                    worksheet.write(3, 1, Efficiency)
                    worksheet.write(4, 0, 'CCR:')
                    worksheet.write(4, 1, CCR)
                    worksheet.write(0, 2, '      ***')
                    worksheet.write(1, 2, '      ***')
                    worksheet.write(2, 2, '      ***')
                    worksheet.write(3, 2, '      ***')
                    worksheet.write(4, 2, '      ***')
                    worksheet.write(0, 3, 'p0:')
                    worksheet.write(1, 3, 'p1:')
                    worksheet.write(2, 3, 'p0:')

                    for row_num, data in enumerate(run):
                        worksheet.write_row(row_num, 4, data)

        if len(run) == 4:
            fn = 'C:/Users/Naweed/PycharmProjects/IHHO/HHO Dataset/IHHO run2.xlsx'
            with xlsxwriter.Workbook(fn) as workbook:
                worksheet = workbook.add_worksheet('run')
                worksheet.write(0, 0, 'Makespan:')
                worksheet.write(0, 1, makespan)
                worksheet.write(1, 0, 'SLR:')
                worksheet.write(1, 1, SLR)
                worksheet.write(2, 0, 'Speedup:')
                worksheet.write(2, 1, Speedup)
                worksheet.write(3, 0, 'Efficiency:')
                worksheet.write(3, 1, Efficiency)
                worksheet.write(4, 0, 'CCR:')
                worksheet.write(4, 1, CCR)
                worksheet.write(0, 2, '      ***')
                worksheet.write(1, 2, '      ***')
                worksheet.write(2, 2, '      ***')
                worksheet.write(3, 2, '      ***')
                worksheet.write(4, 2, '      ***')
                worksheet.write(0, 3, 'p0:')
                worksheet.write(1, 3, 'p1:')
                worksheet.write(2, 3, 'p0:')
                worksheet.write(3, 3, 'p2:')

                for row_num, data in enumerate(run):
                    worksheet.write_row(row_num, 4, data)

        elif len (run) == 5 :
            fn = 'C:/Users/Naweed/PycharmProjects/IHHO/HHO Dataset/IHHO run3.xlsx'
            with xlsxwriter.Workbook(fn) as workbook:
                worksheet = workbook.add_worksheet('run')
                worksheet.write(0, 0, 'Makespan:')
                worksheet.write(0, 1, makespan)
                worksheet.write(1, 0, 'SLR:')
                worksheet.write(1, 1, SLR)
                worksheet.write(2, 0, 'Speedup:')
                worksheet.write(2, 1, Speedup)
                worksheet.write(3, 0, 'Efficiency:')
                worksheet.write(3, 1, Efficiency)
                worksheet.write(4, 0, 'CCR:')
                worksheet.write(4, 1, CCR)
                worksheet.write(0, 2, '      ***')
                worksheet.write(1, 2, '      ***')
                worksheet.write(2, 2, '      ***')
                worksheet.write(3, 2, '      ***')
                worksheet.write(4, 2, '      ***')
                worksheet.write(0, 3, 'p0:')
                worksheet.write(1, 3, 'p1:')
                worksheet.write(2, 3, 'p0:')
                worksheet.write(3, 3, 'p2:')
                worksheet.write(4, 3, 'p1:')

                for row_num, data in enumerate(run):
                    worksheet.write_row(row_num, 4, data)

        elif len (run) == 6 :
            fn = 'C:/Users/Naweed/PycharmProjects/IHHO/HHO Dataset/IHHO run4.xlsx'
            with xlsxwriter.Workbook(fn) as workbook:
                worksheet = workbook.add_worksheet('run')
                worksheet.write(0, 0, 'Makespan:')
                worksheet.write(0, 1, makespan)
                worksheet.write(1, 0, 'SLR:')
                worksheet.write(1, 1, SLR)
                worksheet.write(2, 0, 'Speedup:')
                worksheet.write(2, 1, Speedup)
                worksheet.write(3, 0, 'Efficiency:')
                worksheet.write(3, 1, Efficiency)
                worksheet.write(4, 0, 'CCR:')
                worksheet.write(4, 1, CCR)
                worksheet.write(0, 2, '      ***')
                worksheet.write(1, 2, '      ***')
                worksheet.write(2, 2, '      ***')
                worksheet.write(3, 2, '      ***')
                worksheet.write(4, 2, '      ***')
                worksheet.write(0, 3, 'p0:')
                worksheet.write(1, 3, 'p1:')
                worksheet.write(2, 3, 'p0:')
                worksheet.write(3, 3, 'p2:')
                worksheet.write(4, 3, 'p1:')
                worksheet.write(5, 3, 'p1:')

                for row_num, data in enumerate(run):
                    worksheet.write_row(row_num, 4, data)

        elif len (run) == 7 :
            fn = 'C:/Users/Naweed/PycharmProjects/IHHO/HHO Dataset/IHHO run5.xlsx'
            with xlsxwriter.Workbook(fn) as workbook:
                worksheet = workbook.add_worksheet('run')
                worksheet.write(0, 0, 'Makespan:')
                worksheet.write(0, 1, makespan)
                worksheet.write(1, 0, 'SLR:')
                worksheet.write(1, 1, SLR)
                worksheet.write(2, 0, 'Speedup:')
                worksheet.write(2, 1, Speedup)
                worksheet.write(3, 0, 'Efficiency:')
                worksheet.write(3, 1, Efficiency)
                worksheet.write(4, 0, 'CCR:')
                worksheet.write(4, 1, CCR)
                worksheet.write(0, 2, '      ***')
                worksheet.write(1, 2, '      ***')
                worksheet.write(2, 2, '      ***')
                worksheet.write(3, 2, '      ***')
                worksheet.write(4, 2, '      ***')
                worksheet.write(0, 3, 'p0:')
                worksheet.write(1, 3, 'p1:')
                worksheet.write(2, 3, 'p0:')
                worksheet.write(3, 3, 'p2:')
                worksheet.write(4, 3, 'p1:')
                worksheet.write(5, 3, 'p1:')
                worksheet.write(6, 3, 'p1:')

                for row_num, data in enumerate(run):
                    worksheet.write_row(row_num, 4, data)

        elif len(run) == 8:
            fn = 'C:/Users/Naweed/PycharmProjects/IHHO/HHO Dataset/IHHO run6.xlsx'
            with xlsxwriter.Workbook(fn) as workbook:
                worksheet = workbook.add_worksheet('run')
                worksheet.write(0, 0, 'Makespan:')
                worksheet.write(0, 1, makespan)
                worksheet.write(1, 0, 'SLR:')
                worksheet.write(1, 1, SLR)
                worksheet.write(2, 0, 'Speedup:')
                worksheet.write(2, 1, Speedup)
                worksheet.write(3, 0, 'Efficiency:')
                worksheet.write(3, 1, Efficiency)
                worksheet.write(4, 0, 'CCR:')
                worksheet.write(4, 1, CCR)
                worksheet.write(0, 2, '      ***')
                worksheet.write(1, 2, '      ***')
                worksheet.write(2, 2, '      ***')
                worksheet.write(3, 2, '      ***')
                worksheet.write(4, 2, '      ***')
                worksheet.write(0, 3, 'p0:')
                worksheet.write(1, 3, 'p1:')
                worksheet.write(2, 3, 'p0:')
                worksheet.write(3, 3, 'p2:')
                worksheet.write(4, 3, 'p1:')
                worksheet.write(5, 3, 'p1:')
                worksheet.write(6, 3, 'p1:')
                worksheet.write(7, 3, 'p2:')

                for row_num, data in enumerate(run):
                    worksheet.write_row(row_num, 4, data)

        elif len(run) == 9:
            fn = 'C:/Users/Naweed/PycharmProjects/IHHO/HHO Dataset/IHHO run7.xlsx'
            with xlsxwriter.Workbook(fn) as workbook:
                worksheet = workbook.add_worksheet('run')
                worksheet.write(0, 0, 'Makespan:')
                worksheet.write(0, 1, makespan)
                worksheet.write(1, 0, 'SLR:')
                worksheet.write(1, 1, SLR)
                worksheet.write(2, 0, 'Speedup:')
                worksheet.write(2, 1, Speedup)
                worksheet.write(3, 0, 'Efficiency:')
                worksheet.write(3, 1, Efficiency)
                worksheet.write(4, 0, 'CCR:')
                worksheet.write(4, 1, CCR)
                worksheet.write(0, 2, '      ***')
                worksheet.write(1, 2, '      ***')
                worksheet.write(2, 2, '      ***')
                worksheet.write(3, 2, '      ***')
                worksheet.write(4, 2, '      ***')
                worksheet.write(0, 3, 'p0:')
                worksheet.write(1, 3, 'p1:')
                worksheet.write(2, 3, 'p0:')
                worksheet.write(3, 3, 'p2:')
                worksheet.write(4, 3, 'p1:')
                worksheet.write(5, 3, 'p1:')
                worksheet.write(6, 3, 'p1:')
                worksheet.write(8, 3, 'p2:')
                worksheet.write(7, 3, 'p1:')

                for row_num, data in enumerate(run):
                    worksheet.write_row(row_num, 4, data)

        elif len(run) == 10:
            fn = 'C:/Users/Naweed/PycharmProjects/IHHO/HHO Dataset/IHHO run8.xlsx'
            with xlsxwriter.Workbook(fn) as workbook:
                worksheet = workbook.add_worksheet('run')
                worksheet.write(0, 0, 'Makespan:')
                worksheet.write(0, 1, makespan)
                worksheet.write(1, 0, 'SLR:')
                worksheet.write(1, 1, SLR)
                worksheet.write(2, 0, 'Speedup:')
                worksheet.write(2, 1, Speedup)
                worksheet.write(3, 0, 'Efficiency:')
                worksheet.write(3, 1, Efficiency)
                worksheet.write(4, 0, 'CCR:')
                worksheet.write(4, 1, CCR)
                worksheet.write(0, 2, '      ***')
                worksheet.write(1, 2, '      ***')
                worksheet.write(2, 2, '      ***')
                worksheet.write(3, 2, '      ***')
                worksheet.write(4, 2, '      ***')
                worksheet.write(0, 3, 'p0:')
                worksheet.write(1, 3, 'p1:')
                worksheet.write(2, 3, 'p0:')
                worksheet.write(3, 3, 'p2:')
                worksheet.write(4, 3, 'p1:')
                worksheet.write(5, 3, 'p1:')
                worksheet.write(6, 3, 'p1:')
                worksheet.write(7, 3, 'p2:')
                worksheet.write(8, 3, 'p1:')
                worksheet.write(9, 3, 'p1:')

                for row_num, data in enumerate(run):
                    worksheet.write_row(row_num, 4, data)

        elif len(run) == 11:
            fn = 'C:/Users/Naweed/PycharmProjects/IHHO/HHO Dataset/IHHO run9.xlsx'
            with xlsxwriter.Workbook(fn) as workbook:
                worksheet = workbook.add_worksheet('run')
                worksheet.write(0, 0, 'Makespan:')
                worksheet.write(0, 1, makespan)
                worksheet.write(1, 0, 'SLR:')
                worksheet.write(1, 1, SLR)
                worksheet.write(2, 0, 'Speedup:')
                worksheet.write(2, 1, Speedup)
                worksheet.write(3, 0, 'Efficiency:')
                worksheet.write(3, 1, Efficiency)
                worksheet.write(4, 0, 'CCR:')
                worksheet.write(4, 1, CCR)
                worksheet.write(0, 2, '      ***')
                worksheet.write(1, 2, '      ***')
                worksheet.write(2, 2, '      ***')
                worksheet.write(3, 2, '      ***')
                worksheet.write(4, 2, '      ***')
                worksheet.write(0, 3, 'p0:')
                worksheet.write(1, 3, 'p1:')
                worksheet.write(2, 3, 'p0:')
                worksheet.write(3, 3, 'p2:')
                worksheet.write(4, 3, 'p1:')
                worksheet.write(5, 3, 'p1:')
                worksheet.write(6, 3, 'p1:')
                worksheet.write(7, 3, 'p2:')
                worksheet.write(8, 3, 'p1:')
                worksheet.write(9, 3, 'p1:')
                worksheet.write(10, 3, 'p0:')

                for row_num, data in enumerate(run):
                    worksheet.write_row(row_num, 4, data)

        elif len(run) == 12:
            fn = 'C:/Users/Naweed/PycharmProjects/IHHO/HHO Dataset/IHHO run10.xlsx'
            with xlsxwriter.Workbook(fn) as workbook:
                worksheet = workbook.add_worksheet('run')
                worksheet.write(0, 0, 'Makespan:')
                worksheet.write(0, 1, makespan)
                worksheet.write(1, 0, 'SLR:')
                worksheet.write(1, 1, SLR)
                worksheet.write(2, 0, 'Speedup:')
                worksheet.write(2, 1, Speedup)
                worksheet.write(3, 0, 'Efficiency:')
                worksheet.write(3, 1, Efficiency)
                worksheet.write(4, 0, 'CCR:')
                worksheet.write(4, 1, CCR)
                worksheet.write(0, 2, '      ***')
                worksheet.write(1, 2, '      ***')
                worksheet.write(2, 2, '      ***')
                worksheet.write(3, 2, '      ***')
                worksheet.write(4, 2, '      ***')
                worksheet.write(0, 3, 'p0:')
                worksheet.write(1, 3, 'p1:')
                worksheet.write(2, 3, 'p0:')
                worksheet.write(3, 3, 'p2:')
                worksheet.write(4, 3, 'p1:')
                worksheet.write(5, 3, 'p1:')
                worksheet.write(6, 3, 'p1:')
                worksheet.write(7, 3, 'p2:')
                worksheet.write(8, 3, 'p1:')
                worksheet.write(9, 3, 'p1:')
                worksheet.write(10, 3, 'p0:')
                worksheet.write(11, 3, 'p1:')

                for row_num, data in enumerate(run):
                    worksheet.write_row(row_num, 4, data)

        elif len(run) == 13:
            fn = 'C:/Users/Naweed/PycharmProjects/IHHO/HHO Dataset/IHHO run11.xlsx'
            with xlsxwriter.Workbook(fn) as workbook:
                worksheet = workbook.add_worksheet('run')
                worksheet.write(0, 0, 'Makespan:')
                worksheet.write(0, 1, makespan)
                worksheet.write(1, 0, 'SLR:')
                worksheet.write(1, 1, SLR)
                worksheet.write(2, 0, 'Speedup:')
                worksheet.write(2, 1, Speedup)
                worksheet.write(3, 0, 'Efficiency:')
                worksheet.write(3, 1, Efficiency)
                worksheet.write(4, 0, 'CCR:')
                worksheet.write(4, 1, CCR)
                worksheet.write(0, 2, '      ***')
                worksheet.write(1, 2, '      ***')
                worksheet.write(2, 2, '      ***')
                worksheet.write(3, 2, '      ***')
                worksheet.write(4, 2, '      ***')
                worksheet.write(0, 3, 'p0:')
                worksheet.write(1, 3, 'p1:')
                worksheet.write(2, 3, 'p0:')
                worksheet.write(3, 3, 'p2:')
                worksheet.write(4, 3, 'p1:')
                worksheet.write(5, 3, 'p1:')
                worksheet.write(6, 3, 'p1:')
                worksheet.write(7, 3, 'p2:')
                worksheet.write(8, 3, 'p1:')
                worksheet.write(9, 3, 'p1:')
                worksheet.write(10, 3, 'p0:')
                worksheet.write(11, 3, 'p1:')
                worksheet.write(12, 3, 'p1:')

                for row_num, data in enumerate(run):
                    worksheet.write_row(row_num, 4, data)

        elif len(run) == 14:
            fn = 'C:/Users/Naweed/PycharmProjects/IHHO/HHO Dataset/IHHO run12.xlsx'
            with xlsxwriter.Workbook(fn) as workbook:
                worksheet = workbook.add_worksheet('run')
                worksheet.write(0, 0, 'Makespan:')
                worksheet.write(0, 1, makespan)
                worksheet.write(1, 0, 'SLR:')
                worksheet.write(1, 1, SLR)
                worksheet.write(2, 0, 'Speedup:')
                worksheet.write(2, 1, Speedup)
                worksheet.write(3, 0, 'Efficiency:')
                worksheet.write(3, 1, Efficiency)
                worksheet.write(4, 0, 'CCR:')
                worksheet.write(4, 1, CCR)
                worksheet.write(0, 2, '      ***')
                worksheet.write(1, 2, '      ***')
                worksheet.write(2, 2, '      ***')
                worksheet.write(3, 2, '      ***')
                worksheet.write(4, 2, '      ***')
                worksheet.write(0, 3, 'p0:')
                worksheet.write(1, 3, 'p1:')
                worksheet.write(2, 3, 'p0:')
                worksheet.write(3, 3, 'p2:')
                worksheet.write(4, 3, 'p1:')
                worksheet.write(5, 3, 'p1:')
                worksheet.write(6, 3, 'p1:')
                worksheet.write(7, 3, 'p2:')
                worksheet.write(8, 3, 'p1:')
                worksheet.write(9, 3, 'p1:')
                worksheet.write(10, 3, 'p0:')
                worksheet.write(11, 3, 'p1:')
                worksheet.write(12, 3, 'p1:')
                worksheet.write(13, 3, 'p2:')

                for row_num, data in enumerate(run):
                    worksheet.write_row(row_num, 4, data)

        elif len(run) == 15:
            fn = 'C:/Users/Naweed/PycharmProjects/IHHO/HHO Dataset/IHHO run13.xlsx'
            with xlsxwriter.Workbook(fn) as workbook:
                worksheet = workbook.add_worksheet('run')
                worksheet.write(0, 0, 'Makespan:')
                worksheet.write(0, 1, makespan)
                worksheet.write(1, 0, 'SLR:')
                worksheet.write(1, 1, SLR)
                worksheet.write(2, 0, 'Speedup:')
                worksheet.write(2, 1, Speedup)
                worksheet.write(3, 0, 'Efficiency:')
                worksheet.write(3, 1, Efficiency)
                worksheet.write(4, 0, 'CCR:')
                worksheet.write(4, 1, CCR)
                worksheet.write(0, 2, '      ***')
                worksheet.write(1, 2, '      ***')
                worksheet.write(2, 2, '      ***')
                worksheet.write(3, 2, '      ***')
                worksheet.write(4, 2, '      ***')
                worksheet.write(0, 3, 'p0:')
                worksheet.write(1, 3, 'p1:')
                worksheet.write(2, 3, 'p0:')
                worksheet.write(3, 3, 'p2:')
                worksheet.write(4, 3, 'p1:')
                worksheet.write(5, 3, 'p1:')
                worksheet.write(6, 3, 'p1:')
                worksheet.write(7, 3, 'p2:')
                worksheet.write(8, 3, 'p1:')
                worksheet.write(9, 3, 'p1:')
                worksheet.write(10, 3, 'p0:')
                worksheet.write(11, 3, 'p1:')
                worksheet.write(12, 3, 'p1:')
                worksheet.write(13, 3, 'p2:')
                worksheet.write(14, 3, 'p2:')

                for row_num, data in enumerate(run):
                    worksheet.write_row(row_num, 4, data)

        elif len(run) == 16:
            fn = 'C:/Users/Naweed/PycharmProjects/IHHO/HHO Dataset/IHHO run14.xlsx'
            with xlsxwriter.Workbook(fn) as workbook:
                worksheet = workbook.add_worksheet('run')
                worksheet.write(0, 0, 'Makespan:')
                worksheet.write(0, 1, makespan)
                worksheet.write(1, 0, 'SLR:')
                worksheet.write(1, 1, SLR)
                worksheet.write(2, 0, 'Speedup:')
                worksheet.write(2, 1, Speedup)
                worksheet.write(3, 0, 'Efficiency:')
                worksheet.write(3, 1, Efficiency)
                worksheet.write(4, 0, 'CCR:')
                worksheet.write(4, 1, CCR)
                worksheet.write(0, 2, '      ***')
                worksheet.write(1, 2, '      ***')
                worksheet.write(2, 2, '      ***')
                worksheet.write(3, 2, '      ***')
                worksheet.write(4, 2, '      ***')
                worksheet.write(0, 3, 'p0:')
                worksheet.write(1, 3, 'p1:')
                worksheet.write(2, 3, 'p0:')
                worksheet.write(3, 3, 'p2:')
                worksheet.write(4, 3, 'p1:')
                worksheet.write(5, 3, 'p1:')
                worksheet.write(6, 3, 'p1:')
                worksheet.write(7, 3, 'p2:')
                worksheet.write(8, 3, 'p1:')
                worksheet.write(9, 3, 'p1:')
                worksheet.write(10, 3, 'p0:')
                worksheet.write(11, 3, 'p1:')
                worksheet.write(12, 3, 'p1:')
                worksheet.write(13, 3, 'p2:')
                worksheet.write(14, 3, 'p2:')
                worksheet.write(15, 3, 'p1:')

                for row_num, data in enumerate(run):
                    worksheet.write_row(row_num, 4, data)

        elif len(run) == 17:
            fn = 'C:/Users/Naweed/PycharmProjects/IHHO/HHO Dataset/IHHO run15.xlsx'
            with xlsxwriter.Workbook(fn) as workbook:
                worksheet = workbook.add_worksheet('run')
                worksheet.write(0, 0, 'Makespan:')
                worksheet.write(0, 1, makespan)
                worksheet.write(1, 0, 'SLR:')
                worksheet.write(1, 1, SLR)
                worksheet.write(2, 0, 'Speedup:')
                worksheet.write(2, 1, Speedup)
                worksheet.write(3, 0, 'Efficiency:')
                worksheet.write(3, 1, Efficiency)
                worksheet.write(4, 0, 'CCR:')
                worksheet.write(4, 1, CCR)
                worksheet.write(0, 2, '      ***')
                worksheet.write(1, 2, '      ***')
                worksheet.write(2, 2, '      ***')
                worksheet.write(3, 2, '      ***')
                worksheet.write(4, 2, '      ***')
                worksheet.write(0, 3, 'p0:')
                worksheet.write(1, 3, 'p1:')
                worksheet.write(2, 3, 'p0:')
                worksheet.write(3, 3, 'p2:')
                worksheet.write(4, 3, 'p1:')
                worksheet.write(5, 3, 'p1:')
                worksheet.write(6, 3, 'p1:')
                worksheet.write(7, 3, 'p2:')
                worksheet.write(8, 3, 'p1:')
                worksheet.write(9, 3, 'p1:')
                worksheet.write(10, 3, 'p0:')
                worksheet.write(11, 3, 'p1:')
                worksheet.write(12, 3, 'p1:')
                worksheet.write(13, 3, 'p2:')
                worksheet.write(14, 3, 'p2:')
                worksheet.write(15, 3, 'p1:')
                worksheet.write(16, 3, 'p1:')

                for row_num, data in enumerate(run):
                    worksheet.write_row(row_num, 4, data)

        elif len(run) == 18:
            fn = 'C:/Users/Naweed/PycharmProjects/IHHO/HHO Dataset/IHHO run16.xlsx'
            with xlsxwriter.Workbook(fn) as workbook:
                worksheet = workbook.add_worksheet('run')
                worksheet.write(0, 0, 'Makespan:')
                worksheet.write(0, 1, makespan)
                worksheet.write(1, 0, 'SLR:')
                worksheet.write(1, 1, SLR)
                worksheet.write(2, 0, 'Speedup:')
                worksheet.write(2, 1, Speedup)
                worksheet.write(3, 0, 'Efficiency:')
                worksheet.write(3, 1, Efficiency)
                worksheet.write(4, 0, 'CCR:')
                worksheet.write(4, 1, CCR)
                worksheet.write(0, 2, '      ***')
                worksheet.write(1, 2, '      ***')
                worksheet.write(2, 2, '      ***')
                worksheet.write(3, 2, '      ***')
                worksheet.write(4, 2, '      ***')
                worksheet.write(0, 3, 'p0:')
                worksheet.write(1, 3, 'p1:')
                worksheet.write(2, 3, 'p0:')
                worksheet.write(3, 3, 'p2:')
                worksheet.write(4, 3, 'p1:')
                worksheet.write(5, 3, 'p1:')
                worksheet.write(6, 3, 'p1:')
                worksheet.write(7, 3, 'p2:')
                worksheet.write(8, 3, 'p1:')
                worksheet.write(9, 3, 'p1:')
                worksheet.write(10, 3, 'p0:')
                worksheet.write(11, 3, 'p1:')
                worksheet.write(12, 3, 'p1:')
                worksheet.write(13, 3, 'p2:')
                worksheet.write(14, 3, 'p2:')
                worksheet.write(15, 3, 'p1:')
                worksheet.write(16, 3, 'p1:')
                worksheet.write(17, 3, 'p1:')

                for row_num, data in enumerate(run):
                    worksheet.write_row(row_num, 4, data)

        elif len(run) == 19:
            fn = 'C:/Users/Naweed/PycharmProjects/IHHO/HHO Dataset/IHHO run17.xlsx'
            with xlsxwriter.Workbook(fn) as workbook:
                worksheet = workbook.add_worksheet('run')
                worksheet.write(0, 0, 'Makespan:')
                worksheet.write(0, 1, makespan)
                worksheet.write(1, 0, 'SLR:')
                worksheet.write(1, 1, SLR)
                worksheet.write(2, 0, 'Speedup:')
                worksheet.write(2, 1, Speedup)
                worksheet.write(3, 0, 'Efficiency:')
                worksheet.write(3, 1, Efficiency)
                worksheet.write(4, 0, 'CCR:')
                worksheet.write(4, 1, CCR)
                worksheet.write(0, 2, '      ***')
                worksheet.write(1, 2, '      ***')
                worksheet.write(2, 2, '      ***')
                worksheet.write(3, 2, '      ***')
                worksheet.write(4, 2, '      ***')
                worksheet.write(0, 3, 'p0:')
                worksheet.write(1, 3, 'p1:')
                worksheet.write(2, 3, 'p0:')
                worksheet.write(3, 3, 'p2:')
                worksheet.write(4, 3, 'p1:')
                worksheet.write(5, 3, 'p1:')
                worksheet.write(6, 3, 'p1:')
                worksheet.write(7, 3, 'p2:')
                worksheet.write(8, 3, 'p1:')
                worksheet.write(9, 3, 'p1:')
                worksheet.write(10, 3, 'p0:')
                worksheet.write(11, 3, 'p1:')
                worksheet.write(12, 3, 'p1:')
                worksheet.write(13, 3, 'p2:')
                worksheet.write(14, 3, 'p2:')
                worksheet.write(15, 3, 'p1:')
                worksheet.write(16, 3, 'p1:')
                worksheet.write(17, 3, 'p1:')
                worksheet.write(18, 3, 'p0:')

                for row_num, data in enumerate(run):
                    worksheet.write_row(row_num, 4, data)
    except TypeError:
        print('\n')
        print('     *************************************************')
        print('     *  Size of input Graph arrays must not be equal *')
        print('     *              Try another Graph !              *')
        print('     *************************************************')
def Metrics_g (x=list) :
    try:
        if x[0:len(x)] == x[0:len(x)]:
            x[0].append(0)
        x = np.array(x,dtype=object)
        p = np.array([4,12,7])
        cpu_len = len(p)

        file_name = 'C:/Users/Naweed/PycharmProjects/IHHO/Genetic/Makespan data set.txt'
        file_name2 = 'C:/Users/Naweed/PycharmProjects/IHHO/Genetic/SLR data set.txt'
        file_name3 = 'C:/Users/Naweed/PycharmProjects/IHHO/Genetic/Speed up data set.txt'
        file_name4 = 'C:/Users/Naweed/PycharmProjects/IHHO/Genetic/CCR data set.txt'
        file_name5 = 'C:/Users/Naweed/PycharmProjects/IHHO/Genetic/Efficiency data set.txt'

        if len(x) == 3 :
            ms1 = np.round(x[0] / p[0],2)
            ms2 = np.round(x[1] / p[1],2)
            ms3 = np.round(x[2] / p[0],2)
            run = [ms1,ms2,ms3]

            path = np.array([0.5, 0.1])
            path_sum = math.fsum(path)
            msm1 = np.round(x[0] / p[1], 2)
            msm2 = np.round(x[1] / p[1], 2)
            msm3 = np.round(x[2] / p[1], 2)

            task_min = [math.fsum(msm1), math.fsum(msm2),
                        math.fsum(msm3)]
            task_min = math.fsum(task_min)
            print('Tasks on fastest processor :', round(task_min, 2))
            cp_min = [max(msm1),max(msm2),max(msm3)]
            print('critical path on fastest cpu :',cp_min)
            cp_min = max(cp_min)
            print('makespan of cp on fastest cpu :',cp_min)
            cp = [max(ms1),max(ms2)+path[0],max(ms3)+path[1]]
            print('critical path :',cp)
            cp = max(cp)
            print('makespan of cp :', round(cp,2))
            print('\n----------------------------------')
            print('on p0=4:\n', ms1, '\non p1=12:\n', ms2, '\non p0=4:\n', ms3)
            print('\n----------------------------------------------------------------')
            makespan_cpus = [math.fsum(ms1),math.fsum(ms2)+path[0],
                             math.fsum(ms3)+path[1]]
            makespan = math.fsum(makespan_cpus)
            print('Makespan is :',round(makespan,2))

        if len(x) == 4 :
            ms1 = np.round(x[0] / p[0],2)
            ms2 = np.round(x[1] / p[1],2)
            ms3 = np.round(x[2] / p[0],2)
            ms4 = np.round(x[3] / p[2],2)
            run = [ms1,ms2,ms3,ms4]

            path = np.array([0.5, 0.1, 1])
            path_sum = math.fsum(path)
            msm1 = np.round(x[0] / p[1], 2)
            msm2 = np.round(x[1] / p[1], 2)
            msm3 = np.round(x[2] / p[1], 2)
            msm4 = np.round(x[3] / p[1], 2)
            task_min = [math.fsum(msm1), math.fsum(msm2),
                        math.fsum(msm3), math.fsum(msm4)]
            task_min = math.fsum(task_min)
            print('Tasks on fastest processor :', round(task_min, 2))
            cp_min = [max(msm1),max(msm2),max(msm3),max(msm4)]
            print('critical path on fastest cpu :',cp_min)
            cp_min = max(cp_min)
            print('makespan of cp on fastest cpu :',cp_min)
            cp = [max(ms1),max(ms2)+path[0],max(ms3)+path[1],max(ms4)+path[2]]
            print('critical path :',cp)
            cp = max(cp)
            print('makespan of cp :', round(cp,2))
            print('\n----------------------------------')
            print('on p0=4:\n', ms1, '\non p1=12:\n', ms2, '\non p0=4:\n', ms3, '\non p2=7:\n', ms4)
            print('\n----------------------------------------------------------------')
            makespan_cpus = [math.fsum(ms1),math.fsum(ms2)+path[0],
                             math.fsum(ms3)+path[1],math.fsum(ms4)+path[2]]
            makespan = math.fsum(makespan_cpus)
            print('Makespan is :',round(makespan,2))

        elif len(x) == 5 :
            ms1 = np.round(x[0]/p[0],2)
            ms2 = np.round(x[1] / p[1],2)
            ms3 = np.round(x[2] / p[0],2)
            ms4 = np.round(x[3] / p[2],2)
            ms5 = np.round(x[4] / p[1], 2)
            run = [ms1, ms2, ms3, ms4,ms5]
            path = np.array([0.5, 0.1, 1, 1.7])
            path_sum = math.fsum(path)
            msm1 = np.round(x[0] / p[1], 2)
            msm2 = np.round(x[1] / p[1], 2)
            msm3 = np.round(x[2] / p[1], 2)
            msm4 = np.round(x[3] / p[1], 2)
            msm5 = np.round(x[4] / p[1], 2)
            task_min = [math.fsum(msm1), math.fsum(msm2),
                        math.fsum(msm3), math.fsum(msm4), math.fsum(msm5)]
            task_min = math.fsum(task_min)
            print('Tasks on fastest processor :', round(task_min, 2))
            cp_min = [max(msm1), max(msm2), max(msm3), max(msm4),max(ms5)]
            print('critical path on fastest cpu :', cp_min)
            cp_min = max(cp_min)
            print('makespan of cp on fastest cpu :', cp_min)
            cp = [max(ms1),max(ms2)+path[0],max(ms3)+path[1],max(ms4)+path[2],max(ms5)+path[3]]
            print('critical path :', cp)
            cp = max(cp)
            print('makespan of cp :', round(cp,2))
            print('\n----------------------------------')
            print('on p0=4:\n', ms1, '\non p1=12:\n', ms2, '\non p0=4:\n', ms3, '\non p2=7:\n', ms4,'\non p1=12:\n', ms5)
            print('\n----------------------------------------------------------------')
            makespan_cpus = [math.fsum(ms1), math.fsum(ms2) + path[0],
                             math.fsum(ms3) + path[1], math.fsum(ms4) + path[2],math.fsum(ms5)+path[3]]
            makespan = math.fsum(makespan_cpus)
            print('Makespan is :',round(makespan,2))

        elif len(x) == 6:
            ms1 = np.round(x[0] / p[0], 2)
            ms2 = np.round(x[1] / p[1], 2)
            ms3 = np.round(x[2] / p[0], 2)
            ms4 = np.round(x[3] / p[2], 2)
            ms5 = np.round(x[4] / p[1], 2)
            ms6 = np.round(x[5] / p[1], 2)
            run = [ms1, ms2, ms3, ms4, ms5,ms6]
            path = np.array([0.5, 0.1, 1, 1.7])
            path_sum = math.fsum(path)
            msm1 = np.round(x[0] / p[1], 2)
            msm2 = np.round(x[1] / p[1], 2)
            msm3 = np.round(x[2] / p[1], 2)
            msm4 = np.round(x[3] / p[1], 2)
            msm5 = np.round(x[4] / p[1], 2)
            msm6 = np.round(x[5] / p[1], 2)
            task_min = [math.fsum(msm1), math.fsum(msm2),
                        math.fsum(msm3), math.fsum(msm4), math.fsum(msm5), math.fsum(msm6)]
            task_min = math.fsum(task_min)
            print('Tasks on fastest processor :', round(task_min, 2))
            cp_min = [max(msm1), max(msm2), max(msm3), max(msm4), max(msm5),max(msm6)]
            print('critical path on fastest cpu :', cp_min)
            cp_min = max(cp_min)
            print('makespan of cp on fastest cpu :', cp_min)
            cp = [max(ms1), max(ms2) + path[0], max(ms3) + path[1],
                  max(ms4) + path[2], max(ms5) + path[3],max(ms6)]
            print('critical path :', cp)
            cp = max(cp)
            print('makespan of cp :', round(cp,2))
            print('\n----------------------------------')
            print('on p0=4:\n', ms1, '\non p1=12:\n', ms2, '\non p0=4:\n',
            ms3, '\non p2=7:\n', ms4, '\non p1=12:\n', ms5,'\non p1=12:\n', ms6)
            print('\n----------------------------------------------------------------')
            makespan_cpus = [math.fsum(ms1), math.fsum(ms2) + path[0],
                             math.fsum(ms3) + path[1], math.fsum(ms4) + path[2],
                             math.fsum(ms5) + path[3],math.fsum(ms6)]
            makespan = math.fsum(makespan_cpus)
            print('Makespan is :', round(makespan, 2))

        elif len(x) == 7:
            ms1 = np.round(x[0] / p[0], 2)
            ms2 = np.round(x[1] / p[1], 2)
            ms3 = np.round(x[2] / p[0], 2)
            ms4 = np.round(x[3] / p[2], 2)
            ms5 = np.round(x[4] / p[1], 2)
            ms6 = np.round(x[5] / p[1], 2)
            ms7 = np.round(x[6] / p[0], 2)
            run = [ms1, ms2, ms3, ms4, ms5, ms6,ms7]
            path = np.array([0.5, 0.1, 1, 1.7, 6.6])
            path_sum = math.fsum(path)
            msm1 = np.round(x[0] / p[1], 2)
            msm2 = np.round(x[1] / p[1], 2)
            msm3 = np.round(x[2] / p[1], 2)
            msm4 = np.round(x[3] / p[1], 2)
            msm5 = np.round(x[4] / p[1], 2)
            msm6 = np.round(x[5] / p[1], 2)
            msm7 = np.round(x[6] / p[1], 2)
            task_min = [math.fsum(msm1), math.fsum(msm2),
                        math.fsum(msm3), math.fsum(msm4), math.fsum(msm5), math.fsum(msm6), math.fsum(msm7)]
            task_min = math.fsum(task_min)
            print('Tasks on fastest processor :', round(task_min, 2))
            cp_min = [max(msm1), max(msm2), max(msm3), max(msm4), max(msm5), max(msm6),max(msm7)]
            print('critical path on fastest cpu :', cp_min)
            cp_min = max(cp_min)
            print('makespan of cp on fastest cpu :', cp_min)
            cp = [max(ms1), max(ms2) + path[0], max(ms3) + path[1],
                  max(ms4) + path[2], max(ms5) + path[3], max(ms6),max(ms7)+path[4]]
            print('critical path :', cp)
            cp = max(cp)
            print('makespan of cp :', round(cp,2))
            print('\n----------------------------------')
            print('on p0=4:\n', ms1, '\non p1=12:\n', ms2, '\non p0=4:\n',
            ms3, '\non p2=7:\n', ms4, '\non p1=12:\n', ms5,'\non p1=12:\n', ms6,'\non p1=12:\n', ms7)
            print('\n----------------------------------------------------------------')
            makespan_cpus = [math.fsum(ms1), math.fsum(ms2) + path[0],
                             math.fsum(ms3) + path[1], math.fsum(ms4) + path[2],
                             math.fsum(ms5) + path[3], math.fsum(ms6),math.fsum(ms7)+path[4]]
            makespan = math.fsum(makespan_cpus)
            print('Makespan is :', round(makespan, 2))

        elif len(x) == 8:
            ms1 = np.round(x[0] / p[0], 2)
            ms2 = np.round(x[1] / p[1], 2)
            ms3 = np.round(x[2] / p[0], 2)
            ms4 = np.round(x[3] / p[2], 2)
            ms5 = np.round(x[4] / p[1], 2)
            ms6 = np.round(x[5] / p[1], 2)
            ms7 = np.round(x[6] / p[0], 2)
            ms8 = np.round(x[7] / p[2], 2)
            run = [ms1, ms2, ms3, ms4, ms5, ms6, ms7,ms8]
            path = np.array([0.5, 0.1, 1, 1.7, 6.6, 11.7])
            path_sum = math.fsum(path)
            msm1 = np.round(x[0] / p[1], 2)
            msm2 = np.round(x[1] / p[1], 2)
            msm3 = np.round(x[2] / p[1], 2)
            msm4 = np.round(x[3] / p[1], 2)
            msm5 = np.round(x[4] / p[1], 2)
            msm6 = np.round(x[5] / p[1], 2)
            msm7 = np.round(x[6] / p[1], 2)
            msm8 = np.round(x[7] / p[1], 2)
            task_min = [math.fsum(msm1), math.fsum(msm2),
                        math.fsum(msm3), math.fsum(msm4), math.fsum(msm5), math.fsum(msm6), math.fsum(msm7)
                , math.fsum(msm8)]
            task_min = math.fsum(task_min)
            print('Tasks on fastest processor :', round(task_min, 2))
            cp_min = [max(msm1), max(msm2), max(msm3), max(msm4), max(msm5), max(msm6), max(msm7),max(msm8)]
            print('critical path on fastest cpu :', cp_min)
            cp_min = max(cp_min)
            print('makespan of cp on fastest cpu :', cp_min)
            cp = [max(ms1), max(ms2) + path[0], max(ms3) + path[1],
                  max(ms4) + path[2], max(ms5) + path[3], max(ms6), max(ms7) + path[4],max(ms8)+path[5]]
            print('critical path :', cp)
            cp = max(cp)
            print('makespan of cp :', round(cp,2))
            print('\n----------------------------------')
            print('on p0=4:\n', ms1, '\non p1=12:\n', ms2, '\non p0=4:\n',
            ms3, '\non p2=7:\n', ms4, '\non p1=12:\n', ms5,'\non p1=12:\n', ms6,'\non p1=12:\n', ms7,
                  '\non p2=7:\n', ms8)
            print('\n----------------------------------------------------------------')
            makespan_cpus = [math.fsum(ms1), math.fsum(ms2) + path[0],
                             math.fsum(ms3) + path[1], math.fsum(ms4) + path[2],
                             math.fsum(ms5) + path[3], math.fsum(ms6), math.fsum(ms7) + path[4]
                ,math.fsum(ms8)+path[5]]
            makespan = math.fsum(makespan_cpus)
            print('Makespan is :', round(makespan, 2))

        elif len(x) == 9:
            ms1 = np.round(x[0] / p[0], 2)
            ms2 = np.round(x[1] / p[1], 2)
            ms3 = np.round(x[2] / p[0], 2)
            ms4 = np.round(x[3] / p[2], 2)
            ms5 = np.round(x[4] / p[1], 2)
            ms6 = np.round(x[5] / p[1], 2)
            ms7 = np.round(x[6] / p[0], 2)
            ms8 = np.round(x[7] / p[2], 2)
            ms9 = np.round(x[8] / p[1], 2)
            run = [ms1, ms2, ms3, ms4, ms5, ms6, ms7, ms8,ms9]
            path = np.array([0.5, 0.1, 1, 1.7, 6.6, 11.7, 13.3])
            path_sum = math.fsum(path)
            msm1 = np.round(x[0] / p[1], 2)
            msm2 = np.round(x[1] / p[1], 2)
            msm3 = np.round(x[2] / p[1], 2)
            msm4 = np.round(x[3] / p[1], 2)
            msm5 = np.round(x[4] / p[1], 2)
            msm6 = np.round(x[5] / p[1], 2)
            msm7 = np.round(x[6] / p[1], 2)
            msm8 = np.round(x[7] / p[1], 2)
            msm9 = np.round(x[8] / p[1], 2)
            task_min = [math.fsum(msm1), math.fsum(msm2),
                        math.fsum(msm3), math.fsum(msm4), math.fsum(msm5), math.fsum(msm6), math.fsum(msm7)
                , math.fsum(msm8), math.fsum(msm9)]
            task_min = math.fsum(task_min)
            print('Tasks on fastest processor :', round(task_min, 2))
            cp_min = [max(msm1), max(msm2), max(msm3), max(msm4), max(msm5),
                      max(msm6), max(msm7), max(msm8),max(msm9)]
            print('critical path on fastest cpu :', cp_min)
            cp_min = max(cp_min)
            print('makespan of cp on fastest cpu :', cp_min)
            cp = [max(ms1), max(ms2) + path[0], max(ms3) + path[1],
                  max(ms4) + path[2], max(ms5) + path[3], max(ms6),
                  max(ms7) + path[4], max(ms8) + path[5],max(ms9) + path[6]]
            print('critical path :', cp)
            cp = max(cp)
            print('makespan of cp :', round(cp,2))
            print('\n----------------------------------')
            print('on p0=4:\n', ms1, '\non p1=12:\n', ms2, '\non p0=4:\n',
                  ms3, '\non p2=7:\n', ms4, '\non p1=12:\n', ms5, '\non p1=12:\n', ms6, '\non p1=12:\n', ms7,
                  '\non p1=12:\n', ms8, '\non p1=12:\n', ms9)
            print('\n----------------------------------------------------------------')
            makespan_cpus = [math.fsum(ms1), math.fsum(ms2) + path[0],
                             math.fsum(ms3) + path[1], math.fsum(ms4) + path[2],
                             math.fsum(ms5) + path[3], math.fsum(ms6), math.fsum(ms7) + path[4]
                , math.fsum(ms8) + path[5], math.fsum(ms9)+path[6]]
            makespan = math.fsum(makespan_cpus)
            print('Makespan is :', round(makespan, 2))

        elif len(x) == 10:
            ms1 = np.round(x[0] / p[0], 2)
            ms2 = np.round(x[1] / p[1], 2)
            ms3 = np.round(x[2] / p[0], 2)
            ms4 = np.round(x[3] / p[2], 2)
            ms5 = np.round(x[4] / p[1], 2)
            ms6 = np.round(x[5] / p[1], 2)
            ms7 = np.round(x[6] / p[0], 2)
            ms8 = np.round(x[7] / p[2], 2)
            ms9 = np.round(x[8] / p[1], 2)
            ms10 = np.round(x[9] / p[0], 2)
            run = [ms1, ms2, ms3, ms4, ms5, ms6, ms7, ms8, ms9,ms10]
            path = np.array([0.5, 0.1, 1, 1.7, 6.6, 11.7, 13.3, 14.79])
            path_sum = math.fsum(path)
            msm1 = np.round(x[0] / p[1], 2)
            msm2 = np.round(x[1] / p[1], 2)
            msm3 = np.round(x[2] / p[1], 2)
            msm4 = np.round(x[3] / p[1], 2)
            msm5 = np.round(x[4] / p[1], 2)
            msm6 = np.round(x[5] / p[1], 2)
            msm7 = np.round(x[6] / p[1], 2)
            msm8 = np.round(x[7] / p[1], 2)
            msm9 = np.round(x[8] / p[1], 2)
            msm10 = np.round(x[9] / p[1], 2)
            task_min = [math.fsum(msm1), math.fsum(msm2),
                        math.fsum(msm3), math.fsum(msm4), math.fsum(msm5), math.fsum(msm6), math.fsum(msm7)
                , math.fsum(msm8), math.fsum(msm9), math.fsum(msm10)]
            task_min = math.fsum(task_min)
            print('Tasks on fastest processor :', round(task_min, 2))
            cp_min = [max(msm1), max(msm2), max(msm3), max(msm4), max(msm5),
                      max(msm6), max(msm7), max(msm8), max(msm9),max(msm10)]
            print('critical path on fastest cpu :', cp_min)
            cp_min = max(cp_min)
            print('makespan of cp on fastest cpu :', cp_min)
            cp = [max(ms1), max(ms2) + path[0], max(ms3) + path[1],
                  max(ms4) + path[2], max(ms5) + path[3], max(ms6),
                  max(ms7) + path[4], max(ms8) + path[5], max(ms9) + path[6],max(ms10)+path[7]]
            print('critical path :', cp)
            cp = max(cp)
            print('makespan of cp :', round(cp,2))
            print('\n----------------------------------')
            print('on p0=4:\n', ms1, '\non p1=12:\n', ms2, '\non p0=4:\n',
                  ms3, '\non p2=7:\n', ms4, '\non p1=12:\n', ms5, '\non p1=12:\n', ms6, '\non p1=12:\n', ms7,
                  '\non p1=12:\n', ms8,'\non p1=12:\n', ms9,'\non p0=4:\n', ms10)
            print('\n----------------------------------------------------------------')
            makespan_cpus = [math.fsum(ms1), math.fsum(ms2) + path[0],
                             math.fsum(ms3) + path[1], math.fsum(ms4) + path[2],
                             math.fsum(ms5) + path[3], math.fsum(ms6), math.fsum(ms7) + path[4]
                , math.fsum(ms8) + path[5], math.fsum(ms9) + path[6], math.fsum(ms10)+path[7]]
            makespan = math.fsum(makespan_cpus)
            print('Makespan is :', round(makespan, 2))

        elif len(x) == 11:
            ms1 = np.round(x[0] / p[0], 2)
            ms2 = np.round(x[1] / p[1], 2)
            ms3 = np.round(x[2] / p[0], 2)
            ms4 = np.round(x[3] / p[2], 2)
            ms5 = np.round(x[4] / p[1], 2)
            ms6 = np.round(x[5] / p[1], 2)
            ms7 = np.round(x[6] / p[0], 2)
            ms8 = np.round(x[7] / p[2], 2)
            ms9 = np.round(x[8] / p[1], 2)
            ms10 = np.round(x[9] / p[0], 2)
            ms11 = np.round(x[10] / p[0], 2)
            run = [ms1, ms2, ms3, ms4, ms5, ms6, ms7, ms8, ms9, ms10,ms11]
            path = np.array([0.5, 0.1, 1, 1.7, 6.6, 11.7, 13.3, 14.79])
            path_sum = math.fsum(path)
            msm1 = np.round(x[0] / p[1], 2)
            msm2 = np.round(x[1] / p[1], 2)
            msm3 = np.round(x[2] / p[1], 2)
            msm4 = np.round(x[3] / p[1], 2)
            msm5 = np.round(x[4] / p[1], 2)
            msm6 = np.round(x[5] / p[1], 2)
            msm7 = np.round(x[6] / p[1], 2)
            msm8 = np.round(x[7] / p[1], 2)
            msm9 = np.round(x[8] / p[1], 2)
            msm10 = np.round(x[9] / p[1], 2)
            msm11 = np.round(x[10] / p[1], 2)
            task_min = [math.fsum(msm1), math.fsum(msm2),
                        math.fsum(msm3), math.fsum(msm4), math.fsum(msm5), math.fsum(msm6), math.fsum(msm7)
                , math.fsum(msm8), math.fsum(msm9), math.fsum(msm10), math.fsum(msm11)]
            task_min = math.fsum(task_min)
            print('Tasks on fastest processor :', round(task_min, 2))
            cp_min = [max(msm1), max(msm2), max(msm3), max(msm4), max(msm5),
                      max(msm6), max(msm7), max(msm8), max(msm9), max(msm10),max(msm11)]
            print('critical path on fastest cpu :', cp_min)
            cp_min = max(cp_min)
            print('makespan of cp on fastest cpu :', cp_min)
            cp = [max(ms1), max(ms2) + path[0], max(ms3) + path[1],
                  max(ms4) + path[2], max(ms5) + path[3], max(ms6),
                  max(ms7) + path[4], max(ms8) + path[5], max(ms9) + path[6], max(ms10) + path[7],max(ms11)]
            print('critical path :', cp)
            cp = max(cp)
            print('makespan of cp :', round(cp,2))
            print('\n----------------------------------')
            print('on p0=4:\n', ms1, '\non p1=12:\n', ms2, '\non p0=4:\n',
                  ms3, '\non p2=7:\n', ms4, '\non p1=12:\n', ms5, '\non p1=12:\n', ms6, '\non p1=12:\n', ms7,
                  '\non p1=12:\n', ms8,'\non p1=12:\n', ms9,'\non p0=4:\n', ms10,'\non p0=4:\n', ms11)
            print('\n----------------------------------------------------------------')
            makespan_cpus = [math.fsum(ms1), math.fsum(ms2) + path[0],
                             math.fsum(ms3) + path[1], math.fsum(ms4) + path[2],
                             math.fsum(ms5) + path[3], math.fsum(ms6), math.fsum(ms7) + path[4]
                , math.fsum(ms8) + path[5], math.fsum(ms9) + path[6],
                             math.fsum(ms10) + path[7], math.fsum(ms11)]
            makespan = math.fsum(makespan_cpus)
            print('Makespan is :', round(makespan, 2))

        elif len(x) == 12:
            ms1 = np.round(x[0] / p[0], 2)
            ms2 = np.round(x[1] / p[1], 2)
            ms3 = np.round(x[2] / p[0], 2)
            ms4 = np.round(x[3] / p[2], 2)
            ms5 = np.round(x[4] / p[1], 2)
            ms6 = np.round(x[5] / p[1], 2)
            ms7 = np.round(x[6] / p[0], 2)
            ms8 = np.round(x[7] / p[2], 2)
            ms9 = np.round(x[8] / p[1], 2)
            ms10 = np.round(x[9] / p[0], 2)
            ms11 = np.round(x[10] / p[0], 2)
            ms12 = np.round(x[11] / p[1], 2)
            run = [ms1, ms2, ms3, ms4, ms5, ms6,
                   ms7, ms8, ms9, ms10, ms11,ms12]
            path = np.array([0.5, 0.1, 1, 1.7, 6.6, 11.7, 13.3, 14.79, 18.4])
            path_sum = math.fsum(path)
            msm1 = np.round(x[0] / p[1], 2)
            msm2 = np.round(x[1] / p[1], 2)
            msm3 = np.round(x[2] / p[1], 2)
            msm4 = np.round(x[3] / p[1], 2)
            msm5 = np.round(x[4] / p[1], 2)
            msm6 = np.round(x[5] / p[1], 2)
            msm7 = np.round(x[6] / p[1], 2)
            msm8 = np.round(x[7] / p[1], 2)
            msm9 = np.round(x[8] / p[1], 2)
            msm10 = np.round(x[9] / p[1], 2)
            msm11 = np.round(x[10] / p[1], 2)
            msm12 = np.round(x[11] / p[1], 2)
            task_min = [math.fsum(msm1), math.fsum(msm2),
                        math.fsum(msm3), math.fsum(msm4), math.fsum(msm5), math.fsum(msm6), math.fsum(msm7)
                , math.fsum(msm8), math.fsum(msm9), math.fsum(msm10), math.fsum(msm11),
                        math.fsum(msm12)]
            task_min = math.fsum(task_min)
            print('Tasks on fastest processor :', round(task_min, 2))
            cp_min = [max(msm1), max(msm2), max(msm3), max(msm4), max(msm5),
                      max(msm6), max(msm7), max(msm8), max(msm9), max(msm10), max(msm11),max(msm12)]
            print('critical path on fastest cpu :', cp_min)
            cp_min = max(cp_min)
            print('makespan of cp on fastest cpu :', cp_min)
            cp = [max(ms1), max(ms2) + path[0], max(ms3) + path[1],
                  max(ms4) + path[2], max(ms5) + path[3], max(ms6),
                  max(ms7) + path[4], max(ms8) + path[5], max(ms9) + path[6],
                  max(ms10) + path[7], max(ms11),max(ms12)+path[8]]
            print('critical path :', cp)
            cp = max(cp)
            print('makespan of cp :', round(cp,2))
            print('\n----------------------------------')
            print('on p0=4:\n', ms1, '\non p1=12:\n', ms2, '\non p0=4:\n',
                  ms3, '\non p2=7:\n', ms4, '\non p1=12:\n', ms5, '\non p1=12:\n', ms6, '\non p1=12:\n', ms7,
                  '\non p1=12:\n', ms8,'\non p1=12:\n', ms9,'\non p0=4:\n', ms10,'\non p0=4:\n',
                  ms11,'\non p1=12:\n', ms12)
            print('\n----------------------------------------------------------------')
            makespan_cpus = [math.fsum(ms1), math.fsum(ms2) + path[0],
                             math.fsum(ms3) + path[1], math.fsum(ms4) + path[2],
                             math.fsum(ms5) + path[3], math.fsum(ms6), math.fsum(ms7) + path[4]
                , math.fsum(ms8) + path[5], math.fsum(ms9) + path[6],
                             math.fsum(ms10) + path[7], math.fsum(ms12)+path[8]]
            makespan = math.fsum(makespan_cpus)
            print('Makespan is :', round(makespan, 2))

        elif len(x) == 13:
            ms1 = np.round(x[0] / p[0], 2)
            ms2 = np.round(x[1] / p[1], 2)
            ms3 = np.round(x[2] / p[0], 2)
            ms4 = np.round(x[3] / p[2], 2)
            ms5 = np.round(x[4] / p[1], 2)
            ms6 = np.round(x[5] / p[1], 2)
            ms7 = np.round(x[6] / p[0], 2)
            ms8 = np.round(x[7] / p[2], 2)
            ms9 = np.round(x[8] / p[1], 2)
            ms10 = np.round(x[9] / p[0], 2)
            ms11 = np.round(x[10] / p[0], 2)
            ms12 = np.round(x[11] / p[1], 2)
            ms13 = np.round(x[12] / p[1], 2)
            run = [ms1, ms2, ms3, ms4, ms5, ms6,
                   ms7, ms8, ms9, ms10, ms11, ms12,ms13]
            path = np.array([0.5, 0.1, 1, 1.7, 6.6, 11.7, 13.3, 14.79, 18.4])
            path_sum = math.fsum(path)
            msm1 = np.round(x[0] / p[1], 2)
            msm2 = np.round(x[1] / p[1], 2)
            msm3 = np.round(x[2] / p[1], 2)
            msm4 = np.round(x[3] / p[1], 2)
            msm5 = np.round(x[4] / p[1], 2)
            msm6 = np.round(x[5] / p[1], 2)
            msm7 = np.round(x[6] / p[1], 2)
            msm8 = np.round(x[7] / p[1], 2)
            msm9 = np.round(x[8] / p[1], 2)
            msm10 = np.round(x[9] / p[1], 2)
            msm11 = np.round(x[10] / p[1], 2)
            msm12 = np.round(x[11] / p[1], 2)
            msm13 = np.round(x[12] / p[1], 2)
            task_min = [math.fsum(msm1), math.fsum(msm2),
                        math.fsum(msm3), math.fsum(msm4), math.fsum(msm5), math.fsum(msm6), math.fsum(msm7)
                , math.fsum(msm8), math.fsum(msm9), math.fsum(msm10), math.fsum(msm11),
                        math.fsum(msm12), math.fsum(msm13)]
            task_min = math.fsum(task_min)
            print('Tasks on fastest processor :', round(task_min, 2))
            cp_min = [max(msm1), max(msm2), max(msm3), max(msm4), max(msm5),
                      max(msm6), max(msm7), max(msm8), max(msm9),
                      max(msm10), max(msm11), max(msm12),max(msm13)]
            print('critical path on fastest cpu :', cp_min)
            cp_min = max(cp_min)
            print('makespan of cp on fastest cpu :', cp_min)
            cp = [max(ms1), max(ms2) + path[0], max(ms3) + path[1],
                  max(ms4) + path[2], max(ms5) + path[3], max(ms6),
                  max(ms7) + path[4], max(ms8) + path[5], max(ms9) + path[6],
                  max(ms10) + path[7], max(ms11), max(ms12) + path[8],max(ms13)]
            print('critical path :', cp)
            cp = max(cp)
            print('makespan of cp :', round(cp,2))
            print('\n----------------------------------')
            print('on p0=4:\n', ms1, '\non p1=12:\n', ms2, '\non p0=4:\n',
                  ms3, '\non p2=7:\n', ms4, '\non p1=12:\n', ms5, '\non p1=12:\n', ms6, '\non p1=12:\n', ms7,
                  '\non p1=12:\n', ms8, '\non p1=12:\n', ms9, '\non p0=4:\n', ms10, '\non p0=4:\n',
                  ms11, '\non p0=4:\n', ms12, '\non p1=12:\n', ms13)
            print('\n----------------------------------------------------------------')
            makespan_cpus = [math.fsum(ms1), math.fsum(ms2) + path[0],
                             math.fsum(ms3) + path[1], math.fsum(ms4) + path[2],
                             math.fsum(ms5) + path[3], math.fsum(ms6), math.fsum(ms7) + path[4]
                , math.fsum(ms8) + path[5], math.fsum(ms9) + path[6],
                             math.fsum(ms10) + path[7],
                             math.fsum(ms12) + path[8], math.fsum(ms13)]
            makespan = math.fsum(makespan_cpus)
            print('Makespan is :', round(makespan, 2))

        elif len(x) == 14:
            ms1 = np.round(x[0] / p[0], 2)
            ms2 = np.round(x[1] / p[1], 2)
            ms3 = np.round(x[2] / p[0], 2)
            ms4 = np.round(x[3] / p[2], 2)
            ms5 = np.round(x[4] / p[1], 2)
            ms6 = np.round(x[5] / p[1], 2)
            ms7 = np.round(x[6] / p[0], 2)
            ms8 = np.round(x[7] / p[2], 2)
            ms9 = np.round(x[8] / p[1], 2)
            ms10 = np.round(x[9] / p[0], 2)
            ms11 = np.round(x[10] / p[0], 2)
            ms12 = np.round(x[11] / p[1], 2)
            ms13 = np.round(x[12] / p[1], 2)
            ms14 = np.round(x[13] / p[2], 2)
            run = [ms1, ms2, ms3, ms4, ms5, ms6,
                   ms7, ms8, ms9, ms10, ms11,
                   ms12, ms13,ms14]
            path = np.array([0.5, 0.1, 1, 1.7, 6.6, 11.7, 13.3, 14.79, 18.4, 19.9])
            path_sum = math.fsum(path)
            msm1 = np.round(x[0] / p[1], 2)
            msm2 = np.round(x[1] / p[1], 2)
            msm3 = np.round(x[2] / p[1], 2)
            msm4 = np.round(x[3] / p[1], 2)
            msm5 = np.round(x[4] / p[1], 2)
            msm6 = np.round(x[5] / p[1], 2)
            msm7 = np.round(x[6] / p[1], 2)
            msm8 = np.round(x[7] / p[1], 2)
            msm9 = np.round(x[8] / p[1], 2)
            msm10 = np.round(x[9] / p[1], 2)
            msm11 = np.round(x[10] / p[1], 2)
            msm12 = np.round(x[11] / p[1], 2)
            msm13 = np.round(x[12] / p[1], 2)
            msm14 = np.round(x[13] / p[1], 2)
            task_min = [math.fsum(msm1), math.fsum(msm2),
                        math.fsum(msm3), math.fsum(msm4), math.fsum(msm5), math.fsum(msm6), math.fsum(msm7)
                , math.fsum(msm8), math.fsum(msm9), math.fsum(msm10), math.fsum(msm11),
                        math.fsum(msm12), math.fsum(msm13), math.fsum(msm14)]
            task_min = math.fsum(task_min)
            print('Tasks on fastest processor :', round(task_min, 2))
            cp_min = [max(msm1), max(msm2), max(msm3), max(msm4), max(msm5),
                      max(msm6), max(msm7), max(msm8), max(msm9),
                      max(msm10), max(msm11), max(msm12), max(msm13),max(msm14)]
            print('critical path on fastest cpu :', cp_min)
            cp_min = max(cp_min)
            print('makespan of cp on fastest cpu :', cp_min)
            cp = [max(ms1), max(ms2) + path[0], max(ms3) + path[1],
                  max(ms4) + path[2], max(ms5) + path[3], max(ms6),
                  max(ms7) + path[4], max(ms8) + path[5], max(ms9) + path[6],
                  max(ms10) + path[7], max(ms11), max(ms12) + path[8], max(ms13),max(ms14)+path[9]]
            print('critical path :', cp)
            cp = max(cp)
            print('makespan of cp :', round(cp,2))
            print('\n----------------------------------')
            print('on p0=4:\n', ms1, '\non p1=12:\n', ms2, '\non p0=4:\n',
                  ms3, '\non p2=7:\n', ms4, '\non p1=12:\n', ms5, '\non p1=12:\n', ms6, '\non p1=12:\n', ms7,
                  '\non p1=12:\n', ms8, '\non p1=12:\n', ms9, '\non p0=4:\n', ms10, '\non p0=4:\n',
                  ms11, '\non p0=4:\n', ms12, '\non p1=12:\n', ms13, '\non p2=7:\n', ms14)
            print('\n----------------------------------------------------------------')
            makespan_cpus = [math.fsum(ms1), math.fsum(ms2) + path[0],
                             math.fsum(ms3) + path[1], math.fsum(ms4) + path[2],
                             math.fsum(ms5) + path[3], math.fsum(ms6), math.fsum(ms7) + path[4]
                , math.fsum(ms8) + path[5], math.fsum(ms9) + path[6],
                             math.fsum(ms10) + path[7],
                             math.fsum(ms12) + path[8],
                             math.fsum(ms13),math.fsum(ms14)+path[9]]
            makespan = math.fsum(makespan_cpus)
            print('Makespan is :', round(makespan, 2))

        elif len(x) == 15:
            ms1 = np.round(x[0] / p[0], 2)
            ms2 = np.round(x[1] / p[1], 2)
            ms3 = np.round(x[2] / p[0], 2)
            ms4 = np.round(x[3] / p[2], 2)
            ms5 = np.round(x[4] / p[1], 2)
            ms6 = np.round(x[5] / p[1], 2)
            ms7 = np.round(x[6] / p[0], 2)
            ms8 = np.round(x[7] / p[2], 2)
            ms9 = np.round(x[8] / p[1], 2)
            ms10 = np.round(x[9] / p[0], 2)
            ms11 = np.round(x[10] / p[0], 2)
            ms12 = np.round(x[11] / p[1], 2)
            ms13 = np.round(x[12] / p[1], 2)
            ms14 = np.round(x[13] / p[2], 2)
            ms15 = np.round(x[14] / p[2], 2)
            run = [ms1, ms2, ms3, ms4, ms5, ms6,
                   ms7, ms8, ms9, ms10, ms11,
                   ms12, ms13, ms14,ms15]
            path = np.array([0.5, 0.1, 1, 1.7, 6.6, 11.7, 13.3, 14.79, 18.4, 19.9])
            path_sum = math.fsum(path)
            msm1 = np.round(x[0] / p[1], 2)
            msm2 = np.round(x[1] / p[1], 2)
            msm3 = np.round(x[2] / p[1], 2)
            msm4 = np.round(x[3] / p[1], 2)
            msm5 = np.round(x[4] / p[1], 2)
            msm6 = np.round(x[5] / p[1], 2)
            msm7 = np.round(x[6] / p[1], 2)
            msm8 = np.round(x[7] / p[1], 2)
            msm9 = np.round(x[8] / p[1], 2)
            msm10 = np.round(x[9] / p[1], 2)
            msm11 = np.round(x[10] / p[1], 2)
            msm12 = np.round(x[11] / p[1], 2)
            msm13 = np.round(x[12] / p[1], 2)
            msm14 = np.round(x[13] / p[1], 2)
            msm15 = np.round(x[14] / p[1], 2)
            task_min = [math.fsum(msm1), math.fsum(msm2),
                        math.fsum(msm3), math.fsum(msm4), math.fsum(msm5), math.fsum(msm6), math.fsum(msm7)
                , math.fsum(msm8), math.fsum(msm9), math.fsum(msm10), math.fsum(msm11),
                        math.fsum(msm12), math.fsum(msm13), math.fsum(msm14), math.fsum(msm15)]
            task_min = math.fsum(task_min)
            print('Tasks on fastest processor :', round(task_min, 2))
            cp_min = [max(msm1), max(msm2), max(msm3), max(msm4), max(msm5),
                      max(msm6), max(msm7), max(msm8), max(msm9),
                      max(msm10), max(msm11), max(msm12), max(msm13), max(msm14), max(msm15)]
            print('critical path on fastest cpu :', cp_min)
            cp_min = max(cp_min)
            print('makespan of cp on fastest cpu :', cp_min)
            cp = [max(ms1), max(ms2) + path[0], max(ms3) + path[1],
                  max(ms4) + path[2], max(ms5) + path[3], max(ms6),
                  max(ms7) + path[4], max(ms8) + path[5], max(ms9) + path[6],
                  max(ms10) + path[7], max(ms11), max(ms12) + path[8],
                  max(ms13), max(ms14) + path[9], max(ms15)]
            print('critical path :', cp)
            cp = max(cp)
            print('makespan of cp :', round(cp,2))
            print('\n----------------------------------')
            print('on p0=4:\n', ms1, '\non p1=12:\n', ms2, '\non p0=4:\n',
                  ms3, '\non p2=7:\n', ms4, '\non p1=12:\n', ms5, '\non p1=12:\n', ms6, '\non p1=12:\n', ms7,
                  '\non p1=12:\n', ms8, '\non p1=12:\n', ms9, '\non p0=4:\n', ms10, '\non p0=4:\n',
                  ms11, '\non p0=4:\n', ms12, '\non p1=12:\n', ms13, '\non p2=7:\n', ms14,
                  '\non p2=7:\n', ms15)
            print('\n----------------------------------------------------------------')
            makespan_cpus = [math.fsum(ms1), math.fsum(ms2) + path[0],
                             math.fsum(ms3) + path[1], math.fsum(ms4) + path[2],
                             math.fsum(ms5) + path[3], math.fsum(ms6), math.fsum(ms7) + path[4]
                , math.fsum(ms8) + path[5], math.fsum(ms9) + path[6],
                             math.fsum(ms10) + path[7],
                             math.fsum(ms12) + path[8],
                             math.fsum(ms13), math.fsum(ms14) + path[9], math.fsum(ms15)]
            makespan = math.fsum(makespan_cpus)
            print('Makespan is :', round(makespan, 2))

        elif len(x) == 16:
            ms1 = np.round(x[0] / p[0], 2)
            ms2 = np.round(x[1] / p[1], 2)
            ms3 = np.round(x[2] / p[0], 2)
            ms4 = np.round(x[3] / p[2], 2)
            ms5 = np.round(x[4] / p[1], 2)
            ms6 = np.round(x[5] / p[1], 2)
            ms7 = np.round(x[6] / p[0], 2)
            ms8 = np.round(x[7] / p[2], 2)
            ms9 = np.round(x[8] / p[1], 2)
            ms10 = np.round(x[9] / p[0], 2)
            ms11 = np.round(x[10] / p[0], 2)
            ms12 = np.round(x[11] / p[1], 2)
            ms13 = np.round(x[12] / p[1], 2)
            ms14 = np.round(x[13] / p[2], 2)
            ms15 = np.round(x[14] / p[2], 2)
            ms16 = np.round(x[15] / p[1], 2)
            run = [ms1, ms2, ms3, ms4, ms5, ms6,
                   ms7, ms8, ms9, ms10, ms11,
                   ms12, ms13, ms14, ms15,ms16]
            path = np.array([0.5, 0.1, 1, 1.7, 6.6, 11.7, 13.3, 14.79, 18.4, 19.9, 19.5, 13.6])
            path_sum = math.fsum(path)
            msm1 = np.round(x[0] / p[1], 2)
            msm2 = np.round(x[1] / p[1], 2)
            msm3 = np.round(x[2] / p[1], 2)
            msm4 = np.round(x[3] / p[1], 2)
            msm5 = np.round(x[4] / p[1], 2)
            msm6 = np.round(x[5] / p[1], 2)
            msm7 = np.round(x[6] / p[1], 2)
            msm8 = np.round(x[7] / p[1], 2)
            msm9 = np.round(x[8] / p[1], 2)
            msm10 = np.round(x[9] / p[1], 2)
            msm11 = np.round(x[10] / p[1], 2)
            msm12 = np.round(x[11] / p[1], 2)
            msm13 = np.round(x[12] / p[1], 2)
            msm14 = np.round(x[13] / p[1], 2)
            msm15 = np.round(x[14] / p[1], 2)
            msm16 = np.round(x[15] / p[1], 2)
            task_min = [math.fsum(msm1), math.fsum(msm2),
                        math.fsum(msm3), math.fsum(msm4), math.fsum(msm5), math.fsum(msm6), math.fsum(msm7)
                , math.fsum(msm8), math.fsum(msm9), math.fsum(msm10), math.fsum(msm11),
                        math.fsum(msm12), math.fsum(msm13), math.fsum(msm14), math.fsum(msm15),
                        math.fsum(msm16)]
            task_min = math.fsum(task_min)
            print('Tasks on fastest processor :', round(task_min, 2))
            cp_min = [max(msm1), max(msm2), max(msm3), max(msm4), max(msm5),
                      max(msm6), max(msm7), max(msm8), max(msm9),
                      max(msm10), max(msm11), max(msm12), max(msm13), max(msm14),max(msm15),max(msm16)]
            print('critical path on fastest cpu :', cp_min)
            cp_min = max(cp_min)
            print('makespan of cp on fastest cpu :', cp_min)
            cp = [max(ms1), max(ms2) + path[0], max(ms3) + path[1],
                  max(ms4) + path[2], max(ms5) + path[3], max(ms6),
                  max(ms7) + path[4], max(ms8) + path[5], max(ms9) + path[6],
                  max(ms10) + path[7], max(ms11), max(ms12) + path[8],
                  max(ms13), max(ms14) + path[9],max(ms15)+path[10],max(ms16)+path[11]]
            print('critical path :', cp)
            cp = max(cp)
            print('makespan of cp :', round(cp,2))
            print('\n----------------------------------')
            print('on p0=4:\n', ms1, '\non p1=12:\n', ms2, '\non p0=4:\n',
                  ms3, '\non p2=7:\n', ms4, '\non p1=12:\n', ms5, '\non p1=12:\n', ms6, '\non p1=12:\n', ms7,
                  '\non p1=12:\n', ms8, '\non p1=12:\n', ms9, '\non p0=4:\n', ms10, '\non p0=4:\n',
                  ms11, '\non p0=4:\n', ms12, '\non p1=12:\n', ms13, '\non p2=7:\n', ms14,
                  '\non p2=7:\n', ms15, '\non p1=12:\n', ms16)
            print('\n----------------------------------------------------------------')
            makespan_cpus = [math.fsum(ms1), math.fsum(ms2) + path[0],
                             math.fsum(ms3) + path[1], math.fsum(ms4) + path[2],
                             math.fsum(ms5) + path[3], math.fsum(ms6), math.fsum(ms7) + path[4]
                , math.fsum(ms8) + path[5], math.fsum(ms9) + path[6],
                             math.fsum(ms10) + path[7],
                             math.fsum(ms12) + path[8],
                             math.fsum(ms13), math.fsum(ms14) + path[9],
                             math.fsum(ms15), math.fsum(ms16)+path[11]]
            makespan = math.fsum(makespan_cpus)
            print('Makespan is :', round(makespan, 2))

        elif len(x) == 17:
            ms1 = np.round(x[0] / p[0], 2)
            ms2 = np.round(x[1] / p[1], 2)
            ms3 = np.round(x[2] / p[0], 2)
            ms4 = np.round(x[3] / p[2], 2)
            ms5 = np.round(x[4] / p[1], 2)
            ms6 = np.round(x[5] / p[1], 2)
            ms7 = np.round(x[6] / p[0], 2)
            ms8 = np.round(x[7] / p[2], 2)
            ms9 = np.round(x[8] / p[1], 2)
            ms10 = np.round(x[9] / p[0], 2)
            ms11 = np.round(x[10] / p[0], 2)
            ms12 = np.round(x[11] / p[1], 2)
            ms13 = np.round(x[12] / p[1], 2)
            ms14 = np.round(x[13] / p[2], 2)
            ms15 = np.round(x[14] / p[2], 2)
            ms16 = np.round(x[15] / p[1], 2)
            ms17 = np.round(x[16] / p[1], 2)
            run = [ms1, ms2, ms3, ms4, ms5, ms6,
                   ms7, ms8, ms9, ms10, ms11, ms12,
                   ms13, ms14, ms15, ms16,ms17]
            path = np.array([0.5, 0.1, 1, 1.7, 6.6, 11.7, 13.3, 14.79, 18.4, 19.9, 19.5, 13.6])
            path_sum = math.fsum(path)
            msm1 = np.round(x[0] / p[1], 2)
            msm2 = np.round(x[1] / p[1], 2)
            msm3 = np.round(x[2] / p[1], 2)
            msm4 = np.round(x[3] / p[1], 2)
            msm5 = np.round(x[4] / p[1], 2)
            msm6 = np.round(x[5] / p[1], 2)
            msm7 = np.round(x[6] / p[1], 2)
            msm8 = np.round(x[7] / p[1], 2)
            msm9 = np.round(x[8] / p[1], 2)
            msm10 = np.round(x[9] / p[1], 2)
            msm11 = np.round(x[10] / p[1], 2)
            msm12 = np.round(x[11] / p[1], 2)
            msm13 = np.round(x[12] / p[1], 2)
            msm14 = np.round(x[13] / p[1], 2)
            msm15 = np.round(x[14] / p[1], 2)
            msm16 = np.round(x[15] / p[1], 2)
            msm17 = np.round(x[16] / p[1], 2)
            task_min = [math.fsum(msm1), math.fsum(msm2),
                        math.fsum(msm3), math.fsum(msm4), math.fsum(msm5), math.fsum(msm6), math.fsum(msm7)
                , math.fsum(msm8), math.fsum(msm9), math.fsum(msm10), math.fsum(msm11),
                        math.fsum(msm12), math.fsum(msm13), math.fsum(msm14), math.fsum(msm15),
                        math.fsum(msm16), math.fsum(msm17)]
            task_min = math.fsum(task_min)
            print('Tasks on fastest processor :', round(task_min, 2))
            cp_min = [max(msm1), max(msm2), max(msm3), max(msm4), max(msm5),
                      max(msm6), max(msm7), max(msm8), max(msm9),
                      max(msm10), max(msm11), max(msm12),
                      max(msm13), max(msm14), max(msm15),max(msm16),max(msm17)]
            print('critical path on fastest cpu :', cp_min)
            cp_min = max(cp_min)
            print('makespan of cp on fastest cpu :', cp_min)
            cp = [max(ms1), max(ms2) + path[0], max(ms3) + path[1],
                  max(ms4) + path[2], max(ms5) + path[3], max(ms6),
                  max(ms7) + path[4], max(ms8) + path[5], max(ms9) + path[6],
                  max(ms10) + path[7], max(ms11), max(ms12) + path[8],
                  max(ms13), max(ms14) + path[9], max(ms15) + path[10],max(ms16)+path[11],max(ms17)]
            print('critical path :', cp)
            cp = max(cp)
            print('makespan of cp :', round(cp,2))
            print('\n----------------------------------')
            print('on p0=4:\n', ms1, '\non p1=12:\n', ms2, '\non p0=4:\n',
                  ms3, '\non p2=7:\n', ms4, '\non p1=12:\n', ms5, '\non p1=12:\n', ms6, '\non p1=12:\n', ms7,
                  '\non p1=12:\n', ms8, '\non p1=12:\n', ms9, '\non p0=4:\n', ms10, '\non p0=4:\n',
                  ms11, '\non p0=4:\n', ms12, '\non p1=12:\n', ms13, '\non p2=7:\n', ms14,
                  '\non p2=7:\n', ms15, '\non p1=12:\n', ms16, '\non p1=12:\n', ms17)
            print('\n----------------------------------------------------------------')
            makespan_cpus = [math.fsum(ms1), math.fsum(ms2) + path[0],
                             math.fsum(ms3) + path[1], math.fsum(ms4) + path[2],
                             math.fsum(ms5) + path[3], math.fsum(ms6), math.fsum(ms7) + path[4]
                , math.fsum(ms8) + path[5], math.fsum(ms9) + path[6],
                             math.fsum(ms10) + path[7],
                             math.fsum(ms12) + path[8],
                             math.fsum(ms13), math.fsum(ms14) + path[9],
                             math.fsum(ms15), math.fsum(ms16) + path[11],math.fsum(ms17)]
            makespan = math.fsum(makespan_cpus)
            print('Makespan is :', round(makespan, 2))

        elif len(x) == 18:
            ms1 = np.round(x[0] / p[0], 2)
            ms2 = np.round(x[1] / p[1], 2)
            ms3 = np.round(x[2] / p[0], 2)
            ms4 = np.round(x[3] / p[2], 2)
            ms5 = np.round(x[4] / p[1], 2)
            ms6 = np.round(x[5] / p[1], 2)
            ms7 = np.round(x[6] / p[0], 2)
            ms8 = np.round(x[7] / p[2], 2)
            ms9 = np.round(x[8] / p[1], 2)
            ms10 = np.round(x[9] / p[0], 2)
            ms11 = np.round(x[10] / p[0], 2)
            ms12 = np.round(x[11] / p[1], 2)
            ms13 = np.round(x[12] / p[1], 2)
            ms14 = np.round(x[13] / p[2], 2)
            ms15 = np.round(x[14] / p[2], 2)
            ms16 = np.round(x[15] / p[1], 2)
            ms17 = np.round(x[16] / p[1], 2)
            ms18 = np.round(x[17] / p[0], 2)
            run = [ms1, ms2, ms3, ms4, ms5, ms6,
                   ms7, ms8, ms9, ms10, ms11, ms12,
                   ms13, ms14, ms15, ms16, ms17,ms18]
            path = np.array([0.5, 0.1, 1, 1.7, 6.6, 11.7, 13.3, 14.79, 18.4, 19.9, 19.5, 13.6, 17.7])
            path_sum = math.fsum(path)
            msm1 = np.round(x[0] / p[1], 2)
            msm2 = np.round(x[1] / p[1], 2)
            msm3 = np.round(x[2] / p[1], 2)
            msm4 = np.round(x[3] / p[1], 2)
            msm5 = np.round(x[4] / p[1], 2)
            msm6 = np.round(x[5] / p[1], 2)
            msm7 = np.round(x[6] / p[1], 2)
            msm8 = np.round(x[7] / p[1], 2)
            msm9 = np.round(x[8] / p[1], 2)
            msm10 = np.round(x[9] / p[1], 2)
            msm11 = np.round(x[10] / p[1], 2)
            msm12 = np.round(x[11] / p[1], 2)
            msm13 = np.round(x[12] / p[1], 2)
            msm14 = np.round(x[13] / p[1], 2)
            msm15 = np.round(x[14] / p[1], 2)
            msm16 = np.round(x[15] / p[1], 2)
            msm17 = np.round(x[16] / p[1], 2)
            msm18 = np.round(x[17] / p[1], 2)
            task_min = [math.fsum(msm1), math.fsum(msm2),
                        math.fsum(msm3), math.fsum(msm4), math.fsum(msm5), math.fsum(msm6), math.fsum(msm7)
                , math.fsum(msm8), math.fsum(msm9), math.fsum(msm10), math.fsum(msm11),
                        math.fsum(msm12), math.fsum(msm13), math.fsum(msm14), math.fsum(msm15),
                        math.fsum(msm16), math.fsum(msm17), math.fsum(msm18)]
            task_min = math.fsum(task_min)
            print('Tasks on fastest processor :', round(task_min, 2))
            cp_min = [max(msm1), max(msm2), max(msm3), max(msm4), max(msm5),
                      max(msm6), max(msm7), max(msm8), max(msm9),
                      max(msm10), max(msm11), max(msm12),
                      max(msm13), max(msm14), max(msm15), max(msm16), max(msm17),max(msm18)]
            print('critical path on fastest cpu :', cp_min)
            cp_min = max(cp_min)
            print('makespan of cp on fastest cpu :', cp_min)
            cp = [max(ms1), max(ms2) + path[0], max(ms3) + path[1],
                  max(ms4) + path[2], max(ms5) + path[3], max(ms6),
                  max(ms7) + path[4], max(ms8) + path[5], max(ms9) + path[6],
                  max(ms10) + path[7], max(ms11), max(ms12) + path[8],
                  max(ms13), max(ms14) + path[9], max(ms15) + path[10], max(ms16), max(ms17),max(ms18)+path[12]]
            print('critical path :', cp)
            cp = max(cp)
            print('makespan of cp :', round(cp,2))
            print('\n----------------------------------')
            print('on p0=4:\n', ms1, '\non p1=12:\n', ms2, '\non p0=4:\n',
                  ms3, '\non p2=7:\n', ms4, '\non p1=12:\n', ms5, '\non p1=12:\n', ms6, '\non p1=12:\n', ms7,
                  '\non p1=12:\n', ms8, '\non p1=12:\n', ms9, '\non p0=4:\n', ms10, '\non p0=4:\n',
                  ms11, '\non p0=4:\n', ms12, '\non p1=12:\n', ms13, '\non p2=7:\n', ms14,
                  '\non p2=7:\n', ms15, '\non p1=12:\n', ms16, '\non p1=12:\n', ms17, '\non p1=12:\n', ms18)
            print('\n----------------------------------------------------------------')
            makespan_cpus = [math.fsum(ms1), math.fsum(ms2) + path[0],
                             math.fsum(ms3) + path[1], math.fsum(ms4) + path[2],
                             math.fsum(ms5) + path[3], math.fsum(ms6), math.fsum(ms7) + path[4]
                , math.fsum(ms8) + path[5], math.fsum(ms9) + path[6],
                             math.fsum(ms10) + path[7],
                             math.fsum(ms12) + path[8],
                             math.fsum(ms13), math.fsum(ms14) + path[9],
                             math.fsum(ms15), math.fsum(ms16) + path[11],
                             math.fsum(ms17),math.fsum(ms18)+path[12]]
            makespan = math.fsum(makespan_cpus)
            print('Makespan is :', round(makespan, 2))

        elif len(x) == 19:
            ms1 = np.round(x[0] / p[0], 2)
            ms2 = np.round(x[1] / p[1], 2)
            ms3 = np.round(x[2] / p[0], 2)
            ms4 = np.round(x[3] / p[2], 2)
            ms5 = np.round(x[4] / p[1], 2)
            ms6 = np.round(x[5] / p[1], 2)
            ms7 = np.round(x[6] / p[0], 2)
            ms8 = np.round(x[7] / p[2], 2)
            ms9 = np.round(x[8] / p[1], 2)
            ms10 = np.round(x[9] / p[0], 2)
            ms11 = np.round(x[10] / p[0], 2)
            ms12 = np.round(x[11] / p[1], 2)
            ms13 = np.round(x[12] / p[1], 2)
            ms14 = np.round(x[13] / p[2], 2)
            ms15 = np.round(x[14] / p[2], 2)
            ms16 = np.round(x[15] / p[1], 2)
            ms17 = np.round(x[16] / p[1], 2)
            ms18 = np.round(x[17] / p[0], 2)
            ms19 = np.round(x[18] / p[0], 2)
            run = [ms1, ms2, ms3, ms4, ms5, ms6,
                   ms7, ms8, ms9, ms10, ms11, ms12,
                   ms13, ms14, ms15, ms16, ms17, ms18,ms19]
            path = np.array([0.5, 0.1, 1, 1.7, 6.6, 11.7, 13.3, 14.79, 18.4, 19.9, 19.5, 13.6, 17.7])
            path_sum = math.fsum(path)
            msm1 = np.round(x[0] / p[1], 2)
            msm2 = np.round(x[1] / p[1], 2)
            msm3 = np.round(x[2] / p[1], 2)
            msm4 = np.round(x[3] / p[1], 2)
            msm5 = np.round(x[4] / p[1], 2)
            msm6 = np.round(x[5] / p[1], 2)
            msm7 = np.round(x[6] / p[1], 2)
            msm8 = np.round(x[7] / p[1], 2)
            msm9 = np.round(x[8] / p[1], 2)
            msm10 = np.round(x[9] / p[1], 2)
            msm11 = np.round(x[10] / p[1], 2)
            msm12 = np.round(x[11] / p[1], 2)
            msm13 = np.round(x[12] / p[1], 2)
            msm14 = np.round(x[13] / p[1], 2)
            msm15 = np.round(x[14] / p[1], 2)
            msm16 = np.round(x[15] / p[1], 2)
            msm17 = np.round(x[16] / p[1], 2)
            msm18 = np.round(x[17] / p[1], 2)
            msm19 = np.round(x[18] / p[1], 2)
            task_min = [math.fsum(msm1), math.fsum(msm2),
                        math.fsum(msm3), math.fsum(msm4), math.fsum(msm5), math.fsum(msm6), math.fsum(msm7)
                , math.fsum(msm8), math.fsum(msm9), math.fsum(msm10), math.fsum(msm11),
                        math.fsum(msm12), math.fsum(msm13), math.fsum(msm14), math.fsum(msm15),
                        math.fsum(msm16), math.fsum(msm17), math.fsum(msm18), math.fsum(msm19)]
            task_min = math.fsum(task_min)
            print('Tasks on fastest processor :', round(task_min,2))
            cp_min = [max(msm1), max(msm2), max(msm3), max(msm4), max(msm5),
                      max(msm6), max(msm7), max(msm8), max(msm9),
                      max(msm10), max(msm11), max(msm12),
                      max(msm13), max(msm14), max(msm15), max(msm16), max(msm17), max(msm18),max(msm19)]
            print('critical path on fastest cpu :', cp_min)
            cp_min = max(cp_min)
            print('makespan of cp on fastest cpu :', cp_min)
            cp = [max(ms1), max(ms2) + path[0], max(ms3) + path[1],
                  max(ms4) + path[2], max(ms5) + path[3], max(ms6),
                  max(ms7) + path[4], max(ms8) + path[5], max(ms9) + path[6],
                  max(ms10) + path[7], max(ms11), max(ms12) + path[8],
                  max(ms13), max(ms14) + path[9], max(ms15) + path[10],
                  max(ms16), max(ms17),max(ms18)+path[12],max(ms19)]
            print('critical path :', cp)
            cp = max(cp)
            print('makespan of cp :', round(cp,2))
            print('\n----------------------------------')
            print('on p0=4:\n', ms1, '\non p1=12:\n', ms2, '\non p0=4:\n',
                  ms3, '\non p2=7:\n', ms4, '\non p1=12:\n', ms5, '\non p1=12:\n', ms6, '\non p1=12:\n', ms7,
                  '\non p1=12:\n', ms8, '\non p1=12:\n', ms9, '\non p0=4:\n', ms10, '\non p0=4:\n',
                  ms11, '\non p0=4:\n', ms12, '\non p1=12:\n', ms13, '\non p2=7:\n', ms14,
                  '\non p2=7:\n', ms15, '\non p1=12:\n', ms16, '\non p1=12:\n', ms17,
                  '\non p1=12:\n', ms18, '\non p0=4:\n', ms19)
            print('\n----------------------------------------------------------------')
            makespan_cpus = [math.fsum(ms1), math.fsum(ms2) + path[0],
                             math.fsum(ms3) + path[1], math.fsum(ms4) + path[2],
                             math.fsum(ms5) + path[3], math.fsum(ms6), math.fsum(ms7) + path[4]
                , math.fsum(ms8) + path[5], math.fsum(ms9) + path[6],
                             math.fsum(ms10) + path[7],
                             math.fsum(ms12) + path[8],
                             math.fsum(ms13), math.fsum(ms14) + path[9],
                             math.fsum(ms15), math.fsum(ms16) + path[11],
                             math.fsum(ms17), math.fsum(ms18) + path[12], math.fsum(ms19)]
            makespan = round(math.fsum(makespan_cpus),2)
            print('Makespan is :', makespan)

        SLR = round(makespan/cp_min,2)
        print('-> SLR is :',SLR)

        Speedup = round(task_min/makespan,2)
        print('-> Speed up is :',Speedup)

        Efficiency = round(Speedup/cpu_len,2)
        print('-> Efficiency is :',Efficiency)
        print('running on CPUS :' , run)
        print('makespan cpus :',makespan_cpus)

        CCR = round(path_sum/makespan,1)
        print('CCR :' ,CCR)

        with open (file_name,'a') as f :
            f.write(str(makespan))
            f.write(',')
        with open(file_name2, 'a') as f:
            f.write(str(SLR))
            f.write(',')
        with open(file_name3, 'a') as f:
            f.write(str(Speedup))
            f.write(',')
        with open(file_name4, 'a') as f:
            f.write(str(CCR))
            f.write(',')
        with open(file_name5, 'a') as f:
            f.write(str(Efficiency))
            f.write(',')
    except TypeError:
        print('\n')
        print('     *************************************************')
        print('     *  Size of input Graph arrays must not be equal *')
        print('     *              Try another Graph !              *')
        print('     *************************************************')

def Metrics_plus (x=list) :
    print('\n Looking for fastest CPUs possible')
    print('         Please Wait ' ,end='')
    time.sleep(0.5)
    print('.',end='')
    time.sleep(0.5)
    print('.',end='')
    time.sleep(0.5)
    print('.')
    time.sleep(0.25)
    print('           % 1', end='')
    time.sleep(1)
    print('0', end='')
    time.sleep(2)
    print('0 Done !', end='')
    time.sleep(0.3)
    print('\n')
    try:
        if x[0:len(x)] == x[0:len(x)]:
            x[0].append(0)
        x = np.array(x,dtype=object)
        p = np.array([4,12,7])
        cpu_len = len(p)
        fastest_processor = max(p)

        file_name = 'C:/Users/Naweed/PycharmProjects/IHHO/Metrics +/Makespan data set.txt'
        file_name2 = 'C:/Users/Naweed/PycharmProjects/IHHO/Metrics +/SLR data set.txt'
        file_name3 = 'C:/Users/Naweed/PycharmProjects/IHHO/Metrics +/Speed up data set.txt'
        file_name4 = 'C:/Users/Naweed/PycharmProjects/IHHO/Metrics +/CCR data set.txt'
        file_name5 = 'C:/Users/Naweed/PycharmProjects/IHHO/Metrics +/Efficiency data set.txt'

        if len(x) == 3 :
            ms1 = np.round(x[0] / fastest_processor,2)
            ms2 = np.round(x[1] / fastest_processor,2)
            ms3 = np.round(x[2] / fastest_processor,2)
            run = [ms1,ms2,ms3]

            path = np.array([0.5, 0.1])
            path_sum = math.fsum(path)
            msm1 = np.round(x[0] / p[1], 2)
            msm2 = np.round(x[1] / p[1], 2)
            msm3 = np.round(x[2] / p[1], 2)

            task_min = [math.fsum(msm1), math.fsum(msm2),
                        math.fsum(msm3)]
            task_min = math.fsum(task_min)
            print('Tasks on fastest processor :', round(task_min, 2))
            cp_min = [max(msm1),max(msm2),max(msm3)]
            print('critical path on fastest cpu :',cp_min)
            cp_min = max(cp_min)
            print('makespan of cp on fastest cpu :',cp_min)
            cp = [max(ms1),max(ms2)+path[0],max(ms3)+path[1]]
            print('critical path :',cp)
            cp = max(cp)
            print('makespan of cp :', round(cp,2))
            print('\n----------------------------------')
            print('on p0=4:\n', ms1, '\non p1=12:\n', ms2, '\non p0=4:\n', ms3)
            print('\n----------------------------------------------------------------')
            makespan_cpus = [math.fsum(ms1),math.fsum(ms2)+path[0],
                             math.fsum(ms3)+path[1]]
            makespan = math.fsum(makespan_cpus)
            print('Makespan is :',round(makespan,2))

        if len(x) == 4 :
            ms1 = np.round(x[0] / fastest_processor,2)
            ms2 = np.round(x[1] / fastest_processor,2)
            ms3 = np.round(x[2] / fastest_processor,2)
            ms4 = np.round(x[3] / fastest_processor,2)
            run = [ms1,ms2,ms3,ms4]

            path = np.array([0.5, 0.1, 1])
            path_sum = math.fsum(path)
            msm1 = np.round(x[0] / p[1], 2)
            msm2 = np.round(x[1] / p[1], 2)
            msm3 = np.round(x[2] / p[1], 2)
            msm4 = np.round(x[3] / p[1], 2)
            task_min = [math.fsum(msm1), math.fsum(msm2),
                        math.fsum(msm3), math.fsum(msm4)]
            task_min = math.fsum(task_min)
            print('Tasks on fastest processor :', round(task_min, 2))
            cp_min = [max(msm1),max(msm2),max(msm3),max(msm4)]
            print('critical path on fastest cpu :',cp_min)
            cp_min = max(cp_min)
            print('makespan of cp on fastest cpu :',cp_min)
            cp = [max(ms1),max(ms2)+path[0],max(ms3)+path[1],max(ms4)+path[2]]
            print('critical path :',cp)
            cp = max(cp)
            print('makespan of cp :', round(cp,2))
            print('\n----------------------------------')
            print('on p0=4:\n', ms1, '\non p1=12:\n', ms2, '\non p0=4:\n', ms3, '\non p2=7:\n', ms4)
            print('\n----------------------------------------------------------------')
            makespan_cpus = [math.fsum(ms1),math.fsum(ms2)+path[0],
                             math.fsum(ms3)+path[1],math.fsum(ms4)+path[2]]
            makespan = math.fsum(makespan_cpus)
            print('Makespan is :',round(makespan,2))

        elif len(x) == 5 :
            ms1 = np.round(x[0]/fastest_processor,2)
            ms2 = np.round(x[1] / fastest_processor,2)
            ms3 = np.round(x[2] / fastest_processor,2)
            ms4 = np.round(x[3] / fastest_processor,2)
            ms5 = np.round(x[4] / fastest_processor, 2)
            run = [ms1, ms2, ms3, ms4,ms5]
            path = np.array([0.5, 0.1, 1, 1.7])
            path_sum = math.fsum(path)
            msm1 = np.round(x[0] / p[1], 2)
            msm2 = np.round(x[1] / p[1], 2)
            msm3 = np.round(x[2] / p[1], 2)
            msm4 = np.round(x[3] / p[1], 2)
            msm5 = np.round(x[4] / p[1], 2)
            task_min = [math.fsum(msm1), math.fsum(msm2),
                        math.fsum(msm3), math.fsum(msm4), math.fsum(msm5)]
            task_min = math.fsum(task_min)
            print('Tasks on fastest processor :', round(task_min, 2))
            cp_min = [max(msm1), max(msm2), max(msm3), max(msm4),max(ms5)]
            print('critical path on fastest cpu :', cp_min)
            cp_min = max(cp_min)
            print('makespan of cp on fastest cpu :', cp_min)
            cp = [max(ms1),max(ms2)+path[0],max(ms3)+path[1],max(ms4)+path[2],max(ms5)+path[3]]
            print('critical path :', cp)
            cp = max(cp)
            print('makespan of cp :', round(cp,2))
            print('\n----------------------------------')
            print('on p0=4:\n', ms1, '\non p1=12:\n', ms2, '\non p0=4:\n', ms3, '\non p2=7:\n', ms4,'\non p1=12:\n', ms5)
            print('\n----------------------------------------------------------------')
            makespan_cpus = [math.fsum(ms1), math.fsum(ms2) + path[0],
                             math.fsum(ms3) + path[1], math.fsum(ms4) + path[2],math.fsum(ms5)+path[3]]
            makespan = math.fsum(makespan_cpus)
            print('Makespan is :',round(makespan,2))

        elif len(x) == 6:
            ms1 = np.round(x[0] / fastest_processor, 2)
            ms2 = np.round(x[1] / fastest_processor, 2)
            ms3 = np.round(x[2] / fastest_processor, 2)
            ms4 = np.round(x[3] / fastest_processor, 2)
            ms5 = np.round(x[4] / fastest_processor, 2)
            ms6 = np.round(x[5] / fastest_processor, 2)
            run = [ms1, ms2, ms3, ms4, ms5,ms6]
            path = np.array([0.5, 0.1, 1, 1.7])
            path_sum = math.fsum(path)
            msm1 = np.round(x[0] / p[1], 2)
            msm2 = np.round(x[1] / p[1], 2)
            msm3 = np.round(x[2] / p[1], 2)
            msm4 = np.round(x[3] / p[1], 2)
            msm5 = np.round(x[4] / p[1], 2)
            msm6 = np.round(x[5] / p[1], 2)
            task_min = [math.fsum(msm1), math.fsum(msm2),
                        math.fsum(msm3), math.fsum(msm4), math.fsum(msm5), math.fsum(msm6)]
            task_min = math.fsum(task_min)
            print('Tasks on fastest processor :', round(task_min, 2))
            cp_min = [max(msm1), max(msm2), max(msm3), max(msm4), max(msm5),max(msm6)]
            print('critical path on fastest cpu :', cp_min)
            cp_min = max(cp_min)
            print('makespan of cp on fastest cpu :', cp_min)
            cp = [max(ms1), max(ms2) + path[0], max(ms3) + path[1],
                  max(ms4) + path[2], max(ms5) + path[3],max(ms6)]
            print('critical path :', cp)
            cp = max(cp)
            print('makespan of cp :', round(cp,2))
            print('\n----------------------------------')
            print('on p0=4:\n', ms1, '\non p1=12:\n', ms2, '\non p0=4:\n',
            ms3, '\non p2=7:\n', ms4, '\non p1=12:\n', ms5,'\non p1=12:\n', ms6)
            print('\n----------------------------------------------------------------')
            makespan_cpus = [math.fsum(ms1), math.fsum(ms2) + path[0],
                             math.fsum(ms3) + path[1], math.fsum(ms4) + path[2],
                             math.fsum(ms5) + path[3],math.fsum(ms6)]
            makespan = math.fsum(makespan_cpus)
            print('Makespan is :', round(makespan, 2))

        elif len(x) == 7:
            ms1 = np.round(x[0] / fastest_processor, 2)
            ms2 = np.round(x[1] / fastest_processor, 2)
            ms3 = np.round(x[2] / fastest_processor, 2)
            ms4 = np.round(x[3] / fastest_processor, 2)
            ms5 = np.round(x[4] / fastest_processor, 2)
            ms6 = np.round(x[5] / fastest_processor, 2)
            ms7 = np.round(x[6] / fastest_processor, 2)
            run = [ms1, ms2, ms3, ms4, ms5, ms6,ms7]
            path = np.array([0.5, 0.1, 1, 1.7, 6.6])
            path_sum = math.fsum(path)
            msm1 = np.round(x[0] / p[1], 2)
            msm2 = np.round(x[1] / p[1], 2)
            msm3 = np.round(x[2] / p[1], 2)
            msm4 = np.round(x[3] / p[1], 2)
            msm5 = np.round(x[4] / p[1], 2)
            msm6 = np.round(x[5] / p[1], 2)
            msm7 = np.round(x[6] / p[1], 2)
            task_min = [math.fsum(msm1), math.fsum(msm2),
                        math.fsum(msm3), math.fsum(msm4), math.fsum(msm5), math.fsum(msm6), math.fsum(msm7)]
            task_min = math.fsum(task_min)
            print('Tasks on fastest processor :', round(task_min, 2))
            cp_min = [max(msm1), max(msm2), max(msm3), max(msm4), max(msm5), max(msm6),max(msm7)]
            print('critical path on fastest cpu :', cp_min)
            cp_min = max(cp_min)
            print('makespan of cp on fastest cpu :', cp_min)
            cp = [max(ms1), max(ms2) + path[0], max(ms3) + path[1],
                  max(ms4) + path[2], max(ms5) + path[3], max(ms6),max(ms7)+path[4]]
            print('critical path :', cp)
            cp = max(cp)
            print('makespan of cp :', round(cp,2))
            print('\n----------------------------------')
            print('on p0=4:\n', ms1, '\non p1=12:\n', ms2, '\non p0=4:\n',
            ms3, '\non p2=7:\n', ms4, '\non p1=12:\n', ms5,'\non p1=12:\n', ms6,'\non p1=12:\n', ms7)
            print('\n----------------------------------------------------------------')
            makespan_cpus = [math.fsum(ms1), math.fsum(ms2) + path[0],
                             math.fsum(ms3) + path[1], math.fsum(ms4) + path[2],
                             math.fsum(ms5) + path[3], math.fsum(ms6),math.fsum(ms7)+path[4]]
            makespan = math.fsum(makespan_cpus)
            print('Makespan is :', round(makespan, 2))

        elif len(x) == 8:
            ms1 = np.round(x[0] / fastest_processor, 2)
            ms2 = np.round(x[1] / fastest_processor, 2)
            ms3 = np.round(x[2] / fastest_processor, 2)
            ms4 = np.round(x[3] / fastest_processor, 2)
            ms5 = np.round(x[4] / fastest_processor, 2)
            ms6 = np.round(x[5] / fastest_processor, 2)
            ms7 = np.round(x[6] / fastest_processor, 2)
            ms8 = np.round(x[7] / fastest_processor, 2)
            run = [ms1, ms2, ms3, ms4, ms5, ms6, ms7,ms8]
            path = np.array([0.5, 0.1, 1, 1.7, 6.6, 11.7])
            path_sum = math.fsum(path)
            msm1 = np.round(x[0] / p[1], 2)
            msm2 = np.round(x[1] / p[1], 2)
            msm3 = np.round(x[2] / p[1], 2)
            msm4 = np.round(x[3] / p[1], 2)
            msm5 = np.round(x[4] / p[1], 2)
            msm6 = np.round(x[5] / p[1], 2)
            msm7 = np.round(x[6] / p[1], 2)
            msm8 = np.round(x[7] / p[1], 2)
            task_min = [math.fsum(msm1), math.fsum(msm2),
                        math.fsum(msm3), math.fsum(msm4), math.fsum(msm5), math.fsum(msm6), math.fsum(msm7)
                , math.fsum(msm8)]
            task_min = math.fsum(task_min)
            print('Tasks on fastest processor :', round(task_min, 2))
            cp_min = [max(msm1), max(msm2), max(msm3), max(msm4), max(msm5), max(msm6), max(msm7),max(msm8)]
            print('critical path on fastest cpu :', cp_min)
            cp_min = max(cp_min)
            print('makespan of cp on fastest cpu :', cp_min)
            cp = [max(ms1), max(ms2) + path[0], max(ms3) + path[1],
                  max(ms4) + path[2], max(ms5) + path[3], max(ms6), max(ms7) + path[4],max(ms8)+path[5]]
            print('critical path :', cp)
            cp = max(cp)
            print('makespan of cp :', round(cp,2))
            print('\n----------------------------------')
            print('on p0=4:\n', ms1, '\non p1=12:\n', ms2, '\non p0=4:\n',
            ms3, '\non p2=7:\n', ms4, '\non p1=12:\n', ms5,'\non p1=12:\n', ms6,'\non p1=12:\n', ms7,
                  '\non p2=7:\n', ms8)
            print('\n----------------------------------------------------------------')
            makespan_cpus = [math.fsum(ms1), math.fsum(ms2) + path[0],
                             math.fsum(ms3) + path[1], math.fsum(ms4) + path[2],
                             math.fsum(ms5) + path[3], math.fsum(ms6), math.fsum(ms7) + path[4]
                ,math.fsum(ms8)+path[5]]
            makespan = math.fsum(makespan_cpus)
            print('Makespan is :', round(makespan, 2))

        elif len(x) == 9:
            ms1 = np.round(x[0] / fastest_processor, 2)
            ms2 = np.round(x[1] / fastest_processor, 2)
            ms3 = np.round(x[2] / fastest_processor, 2)
            ms4 = np.round(x[3] / fastest_processor, 2)
            ms5 = np.round(x[4] / fastest_processor, 2)
            ms6 = np.round(x[5] / fastest_processor, 2)
            ms7 = np.round(x[6] / fastest_processor, 2)
            ms8 = np.round(x[7] / fastest_processor, 2)
            ms9 = np.round(x[8] / fastest_processor, 2)
            run = [ms1, ms2, ms3, ms4, ms5, ms6, ms7, ms8,ms9]
            path = np.array([0.5, 0.1, 1, 1.7, 6.6, 11.7, 13.3])
            path_sum = math.fsum(path)
            msm1 = np.round(x[0] / p[1], 2)
            msm2 = np.round(x[1] / p[1], 2)
            msm3 = np.round(x[2] / p[1], 2)
            msm4 = np.round(x[3] / p[1], 2)
            msm5 = np.round(x[4] / p[1], 2)
            msm6 = np.round(x[5] / p[1], 2)
            msm7 = np.round(x[6] / p[1], 2)
            msm8 = np.round(x[7] / p[1], 2)
            msm9 = np.round(x[8] / p[1], 2)
            task_min = [math.fsum(msm1), math.fsum(msm2),
                        math.fsum(msm3), math.fsum(msm4), math.fsum(msm5), math.fsum(msm6), math.fsum(msm7)
                , math.fsum(msm8), math.fsum(msm9)]
            task_min = math.fsum(task_min)
            print('Tasks on fastest processor :', round(task_min, 2))
            cp_min = [max(msm1), max(msm2), max(msm3), max(msm4), max(msm5),
                      max(msm6), max(msm7), max(msm8),max(msm9)]
            print('critical path on fastest cpu :', cp_min)
            cp_min = max(cp_min)
            print('makespan of cp on fastest cpu :', cp_min)
            cp = [max(ms1), max(ms2) + path[0], max(ms3) + path[1],
                  max(ms4) + path[2], max(ms5) + path[3], max(ms6),
                  max(ms7) + path[4], max(ms8) + path[5],max(ms9) + path[6]]
            print('critical path :', cp)
            cp = max(cp)
            print('makespan of cp :', round(cp,2))
            print('\n----------------------------------')
            print('on p0=4:\n', ms1, '\non p1=12:\n', ms2, '\non p0=4:\n',
                  ms3, '\non p2=7:\n', ms4, '\non p1=12:\n', ms5, '\non p1=12:\n', ms6, '\non p1=12:\n', ms7,
                  '\non p1=12:\n', ms8, '\non p1=12:\n', ms9)
            print('\n----------------------------------------------------------------')
            makespan_cpus = [math.fsum(ms1), math.fsum(ms2) + path[0],
                             math.fsum(ms3) + path[1], math.fsum(ms4) + path[2],
                             math.fsum(ms5) + path[3], math.fsum(ms6), math.fsum(ms7) + path[4]
                , math.fsum(ms8) + path[5], math.fsum(ms9)+path[6]]
            makespan = math.fsum(makespan_cpus)
            print('Makespan is :', round(makespan, 2))

        elif len(x) == 10:
            ms1 = np.round(x[0] / fastest_processor, 2)
            ms2 = np.round(x[1] / fastest_processor, 2)
            ms3 = np.round(x[2] / fastest_processor, 2)
            ms4 = np.round(x[3] / fastest_processor, 2)
            ms5 = np.round(x[4] / fastest_processor, 2)
            ms6 = np.round(x[5] / fastest_processor, 2)
            ms7 = np.round(x[6] / fastest_processor, 2)
            ms8 = np.round(x[7] / fastest_processor, 2)
            ms9 = np.round(x[8] / fastest_processor, 2)
            ms10 = np.round(x[9] / fastest_processor, 2)
            run = [ms1, ms2, ms3, ms4, ms5, ms6, ms7, ms8, ms9,ms10]
            path = np.array([0.5, 0.1, 1, 1.7, 6.6, 11.7, 13.3, 14.79])
            path_sum = math.fsum(path)
            msm1 = np.round(x[0] / p[1], 2)
            msm2 = np.round(x[1] / p[1], 2)
            msm3 = np.round(x[2] / p[1], 2)
            msm4 = np.round(x[3] / p[1], 2)
            msm5 = np.round(x[4] / p[1], 2)
            msm6 = np.round(x[5] / p[1], 2)
            msm7 = np.round(x[6] / p[1], 2)
            msm8 = np.round(x[7] / p[1], 2)
            msm9 = np.round(x[8] / p[1], 2)
            msm10 = np.round(x[9] / p[1], 2)
            task_min = [math.fsum(msm1), math.fsum(msm2),
                        math.fsum(msm3), math.fsum(msm4), math.fsum(msm5), math.fsum(msm6), math.fsum(msm7)
                , math.fsum(msm8), math.fsum(msm9), math.fsum(msm10)]
            task_min = math.fsum(task_min)
            print('Tasks on fastest processor :', round(task_min, 2))
            cp_min = [max(msm1), max(msm2), max(msm3), max(msm4), max(msm5),
                      max(msm6), max(msm7), max(msm8), max(msm9),max(msm10)]
            print('critical path on fastest cpu :', cp_min)
            cp_min = max(cp_min)
            print('makespan of cp on fastest cpu :', cp_min)
            cp = [max(ms1), max(ms2) + path[0], max(ms3) + path[1],
                  max(ms4) + path[2], max(ms5) + path[3], max(ms6),
                  max(ms7) + path[4], max(ms8) + path[5], max(ms9) + path[6],max(ms10)+path[7]]
            print('critical path :', cp)
            cp = max(cp)
            print('makespan of cp :', round(cp,2))
            print('\n----------------------------------')
            print('on p0=4:\n', ms1, '\non p1=12:\n', ms2, '\non p0=4:\n',
                  ms3, '\non p2=7:\n', ms4, '\non p1=12:\n', ms5, '\non p1=12:\n', ms6, '\non p1=12:\n', ms7,
                  '\non p1=12:\n', ms8,'\non p1=12:\n', ms9,'\non p0=4:\n', ms10)
            print('\n----------------------------------------------------------------')
            makespan_cpus = [math.fsum(ms1), math.fsum(ms2) + path[0],
                             math.fsum(ms3) + path[1], math.fsum(ms4) + path[2],
                             math.fsum(ms5) + path[3], math.fsum(ms6), math.fsum(ms7) + path[4]
                , math.fsum(ms8) + path[5], math.fsum(ms9) + path[6], math.fsum(ms10)+path[7]]
            makespan = math.fsum(makespan_cpus)
            print('Makespan is :', round(makespan, 2))

        elif len(x) == 11:
            ms1 = np.round(x[0] / fastest_processor, 2)
            ms2 = np.round(x[1] / fastest_processor, 2)
            ms3 = np.round(x[2] / fastest_processor, 2)
            ms4 = np.round(x[3] / fastest_processor, 2)
            ms5 = np.round(x[4] / fastest_processor, 2)
            ms6 = np.round(x[5] / fastest_processor, 2)
            ms7 = np.round(x[6] / fastest_processor, 2)
            ms8 = np.round(x[7] / fastest_processor, 2)
            ms9 = np.round(x[8] / fastest_processor, 2)
            ms10 = np.round(x[9] / fastest_processor, 2)
            ms11 = np.round(x[10] / fastest_processor, 2)
            run = [ms1, ms2, ms3, ms4, ms5, ms6, ms7, ms8, ms9, ms10,ms11]
            path = np.array([0.5, 0.1, 1, 1.7, 6.6, 11.7, 13.3, 14.79])
            path_sum = math.fsum(path)
            msm1 = np.round(x[0] / p[1], 2)
            msm2 = np.round(x[1] / p[1], 2)
            msm3 = np.round(x[2] / p[1], 2)
            msm4 = np.round(x[3] / p[1], 2)
            msm5 = np.round(x[4] / p[1], 2)
            msm6 = np.round(x[5] / p[1], 2)
            msm7 = np.round(x[6] / p[1], 2)
            msm8 = np.round(x[7] / p[1], 2)
            msm9 = np.round(x[8] / p[1], 2)
            msm10 = np.round(x[9] / p[1], 2)
            msm11 = np.round(x[10] / p[1], 2)
            task_min = [math.fsum(msm1), math.fsum(msm2),
                        math.fsum(msm3), math.fsum(msm4), math.fsum(msm5), math.fsum(msm6), math.fsum(msm7)
                , math.fsum(msm8), math.fsum(msm9), math.fsum(msm10), math.fsum(msm11)]
            task_min = math.fsum(task_min)
            print('Tasks on fastest processor :', round(task_min, 2))
            cp_min = [max(msm1), max(msm2), max(msm3), max(msm4), max(msm5),
                      max(msm6), max(msm7), max(msm8), max(msm9), max(msm10),max(msm11)]
            print('critical path on fastest cpu :', cp_min)
            cp_min = max(cp_min)
            print('makespan of cp on fastest cpu :', cp_min)
            cp = [max(ms1), max(ms2) + path[0], max(ms3) + path[1],
                  max(ms4) + path[2], max(ms5) + path[3], max(ms6),
                  max(ms7) + path[4], max(ms8) + path[5], max(ms9) + path[6], max(ms10) + path[7],max(ms11)]
            print('critical path :', cp)
            cp = max(cp)
            print('makespan of cp :', round(cp,2))
            print('\n----------------------------------')
            print('on p0=4:\n', ms1, '\non p1=12:\n', ms2, '\non p0=4:\n',
                  ms3, '\non p2=7:\n', ms4, '\non p1=12:\n', ms5, '\non p1=12:\n', ms6, '\non p1=12:\n', ms7,
                  '\non p1=12:\n', ms8,'\non p1=12:\n', ms9,'\non p0=4:\n', ms10,'\non p0=4:\n', ms11)
            print('\n----------------------------------------------------------------')
            makespan_cpus = [math.fsum(ms1), math.fsum(ms2) + path[0],
                             math.fsum(ms3) + path[1], math.fsum(ms4) + path[2],
                             math.fsum(ms5) + path[3], math.fsum(ms6), math.fsum(ms7) + path[4]
                , math.fsum(ms8) + path[5], math.fsum(ms9) + path[6],
                             math.fsum(ms10) + path[7], math.fsum(ms11)]
            makespan = math.fsum(makespan_cpus)
            print('Makespan is :', round(makespan, 2))

        elif len(x) == 12:
            ms1 = np.round(x[0] / fastest_processor, 2)
            ms2 = np.round(x[1] / fastest_processor, 2)
            ms3 = np.round(x[2] / fastest_processor, 2)
            ms4 = np.round(x[3] / fastest_processor, 2)
            ms5 = np.round(x[4] / fastest_processor, 2)
            ms6 = np.round(x[5] / fastest_processor, 2)
            ms7 = np.round(x[6] / fastest_processor, 2)
            ms8 = np.round(x[7] / fastest_processor, 2)
            ms9 = np.round(x[8] / fastest_processor, 2)
            ms10 = np.round(x[9] / fastest_processor, 2)
            ms11 = np.round(x[10] / fastest_processor, 2)
            ms12 = np.round(x[11] / fastest_processor, 2)
            run = [ms1, ms2, ms3, ms4, ms5, ms6,
                   ms7, ms8, ms9, ms10, ms11,ms12]
            path = np.array([0.5, 0.1, 1, 1.7, 6.6, 11.7, 13.3, 14.79, 18.4])
            path_sum = math.fsum(path)
            msm1 = np.round(x[0] / p[1], 2)
            msm2 = np.round(x[1] / p[1], 2)
            msm3 = np.round(x[2] / p[1], 2)
            msm4 = np.round(x[3] / p[1], 2)
            msm5 = np.round(x[4] / p[1], 2)
            msm6 = np.round(x[5] / p[1], 2)
            msm7 = np.round(x[6] / p[1], 2)
            msm8 = np.round(x[7] / p[1], 2)
            msm9 = np.round(x[8] / p[1], 2)
            msm10 = np.round(x[9] / p[1], 2)
            msm11 = np.round(x[10] / p[1], 2)
            msm12 = np.round(x[11] / p[1], 2)
            task_min = [math.fsum(msm1), math.fsum(msm2),
                        math.fsum(msm3), math.fsum(msm4), math.fsum(msm5), math.fsum(msm6), math.fsum(msm7)
                , math.fsum(msm8), math.fsum(msm9), math.fsum(msm10), math.fsum(msm11),
                        math.fsum(msm12)]
            task_min = math.fsum(task_min)
            print('Tasks on fastest processor :', round(task_min, 2))
            cp_min = [max(msm1), max(msm2), max(msm3), max(msm4), max(msm5),
                      max(msm6), max(msm7), max(msm8), max(msm9), max(msm10), max(msm11),max(msm12)]
            print('critical path on fastest cpu :', cp_min)
            cp_min = max(cp_min)
            print('makespan of cp on fastest cpu :', cp_min)
            cp = [max(ms1), max(ms2) + path[0], max(ms3) + path[1],
                  max(ms4) + path[2], max(ms5) + path[3], max(ms6),
                  max(ms7) + path[4], max(ms8) + path[5], max(ms9) + path[6],
                  max(ms10) + path[7], max(ms11),max(ms12)+path[8]]
            print('critical path :', cp)
            cp = max(cp)
            print('makespan of cp :', round(cp,2))
            print('\n----------------------------------')
            print('on p0=4:\n', ms1, '\non p1=12:\n', ms2, '\non p0=4:\n',
                  ms3, '\non p2=7:\n', ms4, '\non p1=12:\n', ms5, '\non p1=12:\n', ms6, '\non p1=12:\n', ms7,
                  '\non p1=12:\n', ms8,'\non p1=12:\n', ms9,'\non p0=4:\n', ms10,'\non p0=4:\n',
                  ms11,'\non p1=12:\n', ms12)
            print('\n----------------------------------------------------------------')
            makespan_cpus = [math.fsum(ms1), math.fsum(ms2) + path[0],
                             math.fsum(ms3) + path[1], math.fsum(ms4) + path[2],
                             math.fsum(ms5) + path[3], math.fsum(ms6), math.fsum(ms7) + path[4]
                , math.fsum(ms8) + path[5], math.fsum(ms9) + path[6],
                             math.fsum(ms10) + path[7], math.fsum(ms12)+path[8]]
            makespan = math.fsum(makespan_cpus)
            print('Makespan is :', round(makespan, 2))

        elif len(x) == 13:
            ms1 = np.round(x[0] / fastest_processor, 2)
            ms2 = np.round(x[1] / fastest_processor, 2)
            ms3 = np.round(x[2] / fastest_processor, 2)
            ms4 = np.round(x[3] / fastest_processor, 2)
            ms5 = np.round(x[4] / fastest_processor, 2)
            ms6 = np.round(x[5] / fastest_processor, 2)
            ms7 = np.round(x[6] / fastest_processor, 2)
            ms8 = np.round(x[7] / fastest_processor, 2)
            ms9 = np.round(x[8] / fastest_processor, 2)
            ms10 = np.round(x[9] / fastest_processor, 2)
            ms11 = np.round(x[10] / fastest_processor, 2)
            ms12 = np.round(x[11] / fastest_processor, 2)
            ms13 = np.round(x[12] / fastest_processor, 2)
            run = [ms1, ms2, ms3, ms4, ms5, ms6,
                   ms7, ms8, ms9, ms10, ms11, ms12,ms13]
            path = np.array([0.5, 0.1, 1, 1.7, 6.6, 11.7, 13.3, 14.79, 18.4])
            path_sum = math.fsum(path)
            msm1 = np.round(x[0] / p[1], 2)
            msm2 = np.round(x[1] / p[1], 2)
            msm3 = np.round(x[2] / p[1], 2)
            msm4 = np.round(x[3] / p[1], 2)
            msm5 = np.round(x[4] / p[1], 2)
            msm6 = np.round(x[5] / p[1], 2)
            msm7 = np.round(x[6] / p[1], 2)
            msm8 = np.round(x[7] / p[1], 2)
            msm9 = np.round(x[8] / p[1], 2)
            msm10 = np.round(x[9] / p[1], 2)
            msm11 = np.round(x[10] / p[1], 2)
            msm12 = np.round(x[11] / p[1], 2)
            msm13 = np.round(x[12] / p[1], 2)
            task_min = [math.fsum(msm1), math.fsum(msm2),
                        math.fsum(msm3), math.fsum(msm4), math.fsum(msm5), math.fsum(msm6), math.fsum(msm7)
                , math.fsum(msm8), math.fsum(msm9), math.fsum(msm10), math.fsum(msm11),
                        math.fsum(msm12), math.fsum(msm13)]
            task_min = math.fsum(task_min)
            print('Tasks on fastest processor :', round(task_min, 2))
            cp_min = [max(msm1), max(msm2), max(msm3), max(msm4), max(msm5),
                      max(msm6), max(msm7), max(msm8), max(msm9),
                      max(msm10), max(msm11), max(msm12),max(msm13)]
            print('critical path on fastest cpu :', cp_min)
            cp_min = max(cp_min)
            print('makespan of cp on fastest cpu :', cp_min)
            cp = [max(ms1), max(ms2) + path[0], max(ms3) + path[1],
                  max(ms4) + path[2], max(ms5) + path[3], max(ms6),
                  max(ms7) + path[4], max(ms8) + path[5], max(ms9) + path[6],
                  max(ms10) + path[7], max(ms11), max(ms12) + path[8],max(ms13)]
            print('critical path :', cp)
            cp = max(cp)
            print('makespan of cp :', round(cp,2))
            print('\n----------------------------------')
            print('on p0=4:\n', ms1, '\non p1=12:\n', ms2, '\non p0=4:\n',
                  ms3, '\non p2=7:\n', ms4, '\non p1=12:\n', ms5, '\non p1=12:\n', ms6, '\non p1=12:\n', ms7,
                  '\non p1=12:\n', ms8, '\non p1=12:\n', ms9, '\non p0=4:\n', ms10, '\non p0=4:\n',
                  ms11, '\non p0=4:\n', ms12, '\non p1=12:\n', ms13)
            print('\n----------------------------------------------------------------')
            makespan_cpus = [math.fsum(ms1), math.fsum(ms2) + path[0],
                             math.fsum(ms3) + path[1], math.fsum(ms4) + path[2],
                             math.fsum(ms5) + path[3], math.fsum(ms6), math.fsum(ms7) + path[4]
                , math.fsum(ms8) + path[5], math.fsum(ms9) + path[6],
                             math.fsum(ms10) + path[7],
                             math.fsum(ms12) + path[8], math.fsum(ms13)]
            makespan = math.fsum(makespan_cpus)
            print('Makespan is :', round(makespan, 2))

        elif len(x) == 14:
            ms1 = np.round(x[0] / fastest_processor, 2)
            ms2 = np.round(x[1] / fastest_processor, 2)
            ms3 = np.round(x[2] / fastest_processor, 2)
            ms4 = np.round(x[3] / fastest_processor, 2)
            ms5 = np.round(x[4] / fastest_processor, 2)
            ms6 = np.round(x[5] / fastest_processor, 2)
            ms7 = np.round(x[6] / fastest_processor, 2)
            ms8 = np.round(x[7] / fastest_processor, 2)
            ms9 = np.round(x[8] / fastest_processor, 2)
            ms10 = np.round(x[9] / fastest_processor, 2)
            ms11 = np.round(x[10] / fastest_processor, 2)
            ms12 = np.round(x[11] / fastest_processor, 2)
            ms13 = np.round(x[12] / fastest_processor, 2)
            ms14 = np.round(x[13] / fastest_processor, 2)
            run = [ms1, ms2, ms3, ms4, ms5, ms6,
                   ms7, ms8, ms9, ms10, ms11,
                   ms12, ms13,ms14]
            path = np.array([0.5, 0.1, 1, 1.7, 6.6, 11.7, 13.3, 14.79, 18.4, 19.9])
            path_sum = math.fsum(path)
            msm1 = np.round(x[0] / p[1], 2)
            msm2 = np.round(x[1] / p[1], 2)
            msm3 = np.round(x[2] / p[1], 2)
            msm4 = np.round(x[3] / p[1], 2)
            msm5 = np.round(x[4] / p[1], 2)
            msm6 = np.round(x[5] / p[1], 2)
            msm7 = np.round(x[6] / p[1], 2)
            msm8 = np.round(x[7] / p[1], 2)
            msm9 = np.round(x[8] / p[1], 2)
            msm10 = np.round(x[9] / p[1], 2)
            msm11 = np.round(x[10] / p[1], 2)
            msm12 = np.round(x[11] / p[1], 2)
            msm13 = np.round(x[12] / p[1], 2)
            msm14 = np.round(x[13] / p[1], 2)
            task_min = [math.fsum(msm1), math.fsum(msm2),
                        math.fsum(msm3), math.fsum(msm4), math.fsum(msm5), math.fsum(msm6), math.fsum(msm7)
                , math.fsum(msm8), math.fsum(msm9), math.fsum(msm10), math.fsum(msm11),
                        math.fsum(msm12), math.fsum(msm13), math.fsum(msm14)]
            task_min = math.fsum(task_min)
            print('Tasks on fastest processor :', round(task_min, 2))
            cp_min = [max(msm1), max(msm2), max(msm3), max(msm4), max(msm5),
                      max(msm6), max(msm7), max(msm8), max(msm9),
                      max(msm10), max(msm11), max(msm12), max(msm13),max(msm14)]
            print('critical path on fastest cpu :', cp_min)
            cp_min = max(cp_min)
            print('makespan of cp on fastest cpu :', cp_min)
            cp = [max(ms1), max(ms2) + path[0], max(ms3) + path[1],
                  max(ms4) + path[2], max(ms5) + path[3], max(ms6),
                  max(ms7) + path[4], max(ms8) + path[5], max(ms9) + path[6],
                  max(ms10) + path[7], max(ms11), max(ms12) + path[8], max(ms13),max(ms14)+path[9]]
            print('critical path :', cp)
            cp = max(cp)
            print('makespan of cp :', round(cp,2))
            print('\n----------------------------------')
            print('on p0=4:\n', ms1, '\non p1=12:\n', ms2, '\non p0=4:\n',
                  ms3, '\non p2=7:\n', ms4, '\non p1=12:\n', ms5, '\non p1=12:\n', ms6, '\non p1=12:\n', ms7,
                  '\non p1=12:\n', ms8, '\non p1=12:\n', ms9, '\non p0=4:\n', ms10, '\non p0=4:\n',
                  ms11, '\non p0=4:\n', ms12, '\non p1=12:\n', ms13, '\non p2=7:\n', ms14)
            print('\n----------------------------------------------------------------')
            makespan_cpus = [math.fsum(ms1), math.fsum(ms2) + path[0],
                             math.fsum(ms3) + path[1], math.fsum(ms4) + path[2],
                             math.fsum(ms5) + path[3], math.fsum(ms6), math.fsum(ms7) + path[4]
                , math.fsum(ms8) + path[5], math.fsum(ms9) + path[6],
                             math.fsum(ms10) + path[7],
                             math.fsum(ms12) + path[8],
                             math.fsum(ms13),math.fsum(ms14)+path[9]]
            makespan = math.fsum(makespan_cpus)
            print('Makespan is :', round(makespan, 2))

        elif len(x) == 15:
            ms1 = np.round(x[0] / fastest_processor, 2)
            ms2 = np.round(x[1] / fastest_processor, 2)
            ms3 = np.round(x[2] / fastest_processor, 2)
            ms4 = np.round(x[3] / fastest_processor, 2)
            ms5 = np.round(x[4] / fastest_processor, 2)
            ms6 = np.round(x[5] / fastest_processor, 2)
            ms7 = np.round(x[6] / fastest_processor, 2)
            ms8 = np.round(x[7] / fastest_processor, 2)
            ms9 = np.round(x[8] / fastest_processor, 2)
            ms10 = np.round(x[9] / fastest_processor, 2)
            ms11 = np.round(x[10] / fastest_processor, 2)
            ms12 = np.round(x[11] / fastest_processor, 2)
            ms13 = np.round(x[12] / fastest_processor, 2)
            ms14 = np.round(x[13] / fastest_processor, 2)
            ms15 = np.round(x[14] / fastest_processor, 2)
            run = [ms1, ms2, ms3, ms4, ms5, ms6,
                   ms7, ms8, ms9, ms10, ms11,
                   ms12, ms13, ms14,ms15]
            path = np.array([0.5, 0.1, 1, 1.7, 6.6, 11.7, 13.3, 14.79, 18.4, 19.9])
            path_sum = math.fsum(path)
            msm1 = np.round(x[0] / p[1], 2)
            msm2 = np.round(x[1] / p[1], 2)
            msm3 = np.round(x[2] / p[1], 2)
            msm4 = np.round(x[3] / p[1], 2)
            msm5 = np.round(x[4] / p[1], 2)
            msm6 = np.round(x[5] / p[1], 2)
            msm7 = np.round(x[6] / p[1], 2)
            msm8 = np.round(x[7] / p[1], 2)
            msm9 = np.round(x[8] / p[1], 2)
            msm10 = np.round(x[9] / p[1], 2)
            msm11 = np.round(x[10] / p[1], 2)
            msm12 = np.round(x[11] / p[1], 2)
            msm13 = np.round(x[12] / p[1], 2)
            msm14 = np.round(x[13] / p[1], 2)
            msm15 = np.round(x[14] / p[1], 2)
            task_min = [math.fsum(msm1), math.fsum(msm2),
                        math.fsum(msm3), math.fsum(msm4), math.fsum(msm5), math.fsum(msm6), math.fsum(msm7)
                , math.fsum(msm8), math.fsum(msm9), math.fsum(msm10), math.fsum(msm11),
                        math.fsum(msm12), math.fsum(msm13), math.fsum(msm14), math.fsum(msm15)]
            task_min = math.fsum(task_min)
            print('Tasks on fastest processor :', round(task_min, 2))
            cp_min = [max(msm1), max(msm2), max(msm3), max(msm4), max(msm5),
                      max(msm6), max(msm7), max(msm8), max(msm9),
                      max(msm10), max(msm11), max(msm12), max(msm13), max(msm14), max(msm15)]
            print('critical path on fastest cpu :', cp_min)
            cp_min = max(cp_min)
            print('makespan of cp on fastest cpu :', cp_min)
            cp = [max(ms1), max(ms2) + path[0], max(ms3) + path[1],
                  max(ms4) + path[2], max(ms5) + path[3], max(ms6),
                  max(ms7) + path[4], max(ms8) + path[5], max(ms9) + path[6],
                  max(ms10) + path[7], max(ms11), max(ms12) + path[8],
                  max(ms13), max(ms14) + path[9], max(ms15)]
            print('critical path :', cp)
            cp = max(cp)
            print('makespan of cp :', round(cp,2))
            print('\n----------------------------------')
            print('on p0=4:\n', ms1, '\non p1=12:\n', ms2, '\non p0=4:\n',
                  ms3, '\non p2=7:\n', ms4, '\non p1=12:\n', ms5, '\non p1=12:\n', ms6, '\non p1=12:\n', ms7,
                  '\non p1=12:\n', ms8, '\non p1=12:\n', ms9, '\non p0=4:\n', ms10, '\non p0=4:\n',
                  ms11, '\non p0=4:\n', ms12, '\non p1=12:\n', ms13, '\non p2=7:\n', ms14,
                  '\non p2=7:\n', ms15)
            print('\n----------------------------------------------------------------')
            makespan_cpus = [math.fsum(ms1), math.fsum(ms2) + path[0],
                             math.fsum(ms3) + path[1], math.fsum(ms4) + path[2],
                             math.fsum(ms5) + path[3], math.fsum(ms6), math.fsum(ms7) + path[4]
                , math.fsum(ms8) + path[5], math.fsum(ms9) + path[6],
                             math.fsum(ms10) + path[7],
                             math.fsum(ms12) + path[8],
                             math.fsum(ms13), math.fsum(ms14) + path[9], math.fsum(ms15)]
            makespan = math.fsum(makespan_cpus)
            print('Makespan is :', round(makespan, 2))

        elif len(x) == 16:
            ms1 = np.round(x[0] / fastest_processor, 2)
            ms2 = np.round(x[1] / fastest_processor, 2)
            ms3 = np.round(x[2] / fastest_processor, 2)
            ms4 = np.round(x[3] / fastest_processor, 2)
            ms5 = np.round(x[4] / fastest_processor, 2)
            ms6 = np.round(x[5] / fastest_processor, 2)
            ms7 = np.round(x[6] / fastest_processor, 2)
            ms8 = np.round(x[7] / fastest_processor, 2)
            ms9 = np.round(x[8] / fastest_processor, 2)
            ms10 = np.round(x[9] / fastest_processor, 2)
            ms11 = np.round(x[10] / fastest_processor, 2)
            ms12 = np.round(x[11] / fastest_processor, 2)
            ms13 = np.round(x[12] / fastest_processor, 2)
            ms14 = np.round(x[13] / fastest_processor, 2)
            ms15 = np.round(x[14] / fastest_processor, 2)
            ms16 = np.round(x[15] / fastest_processor, 2)
            run = [ms1, ms2, ms3, ms4, ms5, ms6,
                   ms7, ms8, ms9, ms10, ms11,
                   ms12, ms13, ms14, ms15,ms16]
            path = np.array([0.5, 0.1, 1, 1.7, 6.6, 11.7, 13.3, 14.79, 18.4, 19.9, 19.5, 13.6])
            path_sum = math.fsum(path)
            msm1 = np.round(x[0] / p[1], 2)
            msm2 = np.round(x[1] / p[1], 2)
            msm3 = np.round(x[2] / p[1], 2)
            msm4 = np.round(x[3] / p[1], 2)
            msm5 = np.round(x[4] / p[1], 2)
            msm6 = np.round(x[5] / p[1], 2)
            msm7 = np.round(x[6] / p[1], 2)
            msm8 = np.round(x[7] / p[1], 2)
            msm9 = np.round(x[8] / p[1], 2)
            msm10 = np.round(x[9] / p[1], 2)
            msm11 = np.round(x[10] / p[1], 2)
            msm12 = np.round(x[11] / p[1], 2)
            msm13 = np.round(x[12] / p[1], 2)
            msm14 = np.round(x[13] / p[1], 2)
            msm15 = np.round(x[14] / p[1], 2)
            msm16 = np.round(x[15] / p[1], 2)
            task_min = [math.fsum(msm1), math.fsum(msm2),
                        math.fsum(msm3), math.fsum(msm4), math.fsum(msm5), math.fsum(msm6), math.fsum(msm7)
                , math.fsum(msm8), math.fsum(msm9), math.fsum(msm10), math.fsum(msm11),
                        math.fsum(msm12), math.fsum(msm13), math.fsum(msm14), math.fsum(msm15),
                        math.fsum(msm16)]
            task_min = math.fsum(task_min)
            print('Tasks on fastest processor :', round(task_min, 2))
            cp_min = [max(msm1), max(msm2), max(msm3), max(msm4), max(msm5),
                      max(msm6), max(msm7), max(msm8), max(msm9),
                      max(msm10), max(msm11), max(msm12), max(msm13), max(msm14),max(msm15),max(msm16)]
            print('critical path on fastest cpu :', cp_min)
            cp_min = max(cp_min)
            print('makespan of cp on fastest cpu :', cp_min)
            cp = [max(ms1), max(ms2) + path[0], max(ms3) + path[1],
                  max(ms4) + path[2], max(ms5) + path[3], max(ms6),
                  max(ms7) + path[4], max(ms8) + path[5], max(ms9) + path[6],
                  max(ms10) + path[7], max(ms11), max(ms12) + path[8],
                  max(ms13), max(ms14) + path[9],max(ms15)+path[10],max(ms16)+path[11]]
            print('critical path :', cp)
            cp = max(cp)
            print('makespan of cp :', round(cp,2))
            print('\n----------------------------------')
            print('on p0=4:\n', ms1, '\non p1=12:\n', ms2, '\non p0=4:\n',
                  ms3, '\non p2=7:\n', ms4, '\non p1=12:\n', ms5, '\non p1=12:\n', ms6, '\non p1=12:\n', ms7,
                  '\non p1=12:\n', ms8, '\non p1=12:\n', ms9, '\non p0=4:\n', ms10, '\non p0=4:\n',
                  ms11, '\non p0=4:\n', ms12, '\non p1=12:\n', ms13, '\non p2=7:\n', ms14,
                  '\non p2=7:\n', ms15, '\non p1=12:\n', ms16)
            print('\n----------------------------------------------------------------')
            makespan_cpus = [math.fsum(ms1), math.fsum(ms2) + path[0],
                             math.fsum(ms3) + path[1], math.fsum(ms4) + path[2],
                             math.fsum(ms5) + path[3], math.fsum(ms6), math.fsum(ms7) + path[4]
                , math.fsum(ms8) + path[5], math.fsum(ms9) + path[6],
                             math.fsum(ms10) + path[7],
                             math.fsum(ms12) + path[8],
                             math.fsum(ms13), math.fsum(ms14) + path[9],
                             math.fsum(ms15), math.fsum(ms16)+path[11]]
            makespan = math.fsum(makespan_cpus)
            print('Makespan is :', round(makespan, 2))

        elif len(x) == 17:
            ms1 = np.round(x[0] / fastest_processor, 2)
            ms2 = np.round(x[1] / fastest_processor, 2)
            ms3 = np.round(x[2] / fastest_processor, 2)
            ms4 = np.round(x[3] / fastest_processor, 2)
            ms5 = np.round(x[4] / fastest_processor, 2)
            ms6 = np.round(x[5] / fastest_processor, 2)
            ms7 = np.round(x[6] / fastest_processor, 2)
            ms8 = np.round(x[7] / fastest_processor, 2)
            ms9 = np.round(x[8] / fastest_processor, 2)
            ms10 = np.round(x[9] / fastest_processor, 2)
            ms11 = np.round(x[10] / fastest_processor, 2)
            ms12 = np.round(x[11] / fastest_processor, 2)
            ms13 = np.round(x[12] / fastest_processor, 2)
            ms14 = np.round(x[13] / fastest_processor, 2)
            ms15 = np.round(x[14] / fastest_processor, 2)
            ms16 = np.round(x[15] / fastest_processor, 2)
            ms17 = np.round(x[16] / fastest_processor, 2)
            run = [ms1, ms2, ms3, ms4, ms5, ms6,
                   ms7, ms8, ms9, ms10, ms11, ms12,
                   ms13, ms14, ms15, ms16,ms17]
            path = np.array([0.5, 0.1, 1, 1.7, 6.6, 11.7, 13.3, 14.79, 18.4, 19.9, 19.5, 13.6])
            path_sum = math.fsum(path)
            msm1 = np.round(x[0] / p[1], 2)
            msm2 = np.round(x[1] / p[1], 2)
            msm3 = np.round(x[2] / p[1], 2)
            msm4 = np.round(x[3] / p[1], 2)
            msm5 = np.round(x[4] / p[1], 2)
            msm6 = np.round(x[5] / p[1], 2)
            msm7 = np.round(x[6] / p[1], 2)
            msm8 = np.round(x[7] / p[1], 2)
            msm9 = np.round(x[8] / p[1], 2)
            msm10 = np.round(x[9] / p[1], 2)
            msm11 = np.round(x[10] / p[1], 2)
            msm12 = np.round(x[11] / p[1], 2)
            msm13 = np.round(x[12] / p[1], 2)
            msm14 = np.round(x[13] / p[1], 2)
            msm15 = np.round(x[14] / p[1], 2)
            msm16 = np.round(x[15] / p[1], 2)
            msm17 = np.round(x[16] / p[1], 2)
            task_min = [math.fsum(msm1), math.fsum(msm2),
                        math.fsum(msm3), math.fsum(msm4), math.fsum(msm5), math.fsum(msm6), math.fsum(msm7)
                , math.fsum(msm8), math.fsum(msm9), math.fsum(msm10), math.fsum(msm11),
                        math.fsum(msm12), math.fsum(msm13), math.fsum(msm14), math.fsum(msm15),
                        math.fsum(msm16), math.fsum(msm17)]
            task_min = math.fsum(task_min)
            print('Tasks on fastest processor :', round(task_min, 2))
            cp_min = [max(msm1), max(msm2), max(msm3), max(msm4), max(msm5),
                      max(msm6), max(msm7), max(msm8), max(msm9),
                      max(msm10), max(msm11), max(msm12),
                      max(msm13), max(msm14), max(msm15),max(msm16),max(msm17)]
            print('critical path on fastest cpu :', cp_min)
            cp_min = max(cp_min)
            print('makespan of cp on fastest cpu :', cp_min)
            cp = [max(ms1), max(ms2) + path[0], max(ms3) + path[1],
                  max(ms4) + path[2], max(ms5) + path[3], max(ms6),
                  max(ms7) + path[4], max(ms8) + path[5], max(ms9) + path[6],
                  max(ms10) + path[7], max(ms11), max(ms12) + path[8],
                  max(ms13), max(ms14) + path[9], max(ms15) + path[10],max(ms16)+path[11],max(ms17)]
            print('critical path :', cp)
            cp = max(cp)
            print('makespan of cp :', round(cp,2))
            print('\n----------------------------------')
            print('on p0=4:\n', ms1, '\non p1=12:\n', ms2, '\non p0=4:\n',
                  ms3, '\non p2=7:\n', ms4, '\non p1=12:\n', ms5, '\non p1=12:\n', ms6, '\non p1=12:\n', ms7,
                  '\non p1=12:\n', ms8, '\non p1=12:\n', ms9, '\non p0=4:\n', ms10, '\non p0=4:\n',
                  ms11, '\non p0=4:\n', ms12, '\non p1=12:\n', ms13, '\non p2=7:\n', ms14,
                  '\non p2=7:\n', ms15, '\non p1=12:\n', ms16, '\non p1=12:\n', ms17)
            print('\n----------------------------------------------------------------')
            makespan_cpus = [math.fsum(ms1), math.fsum(ms2) + path[0],
                             math.fsum(ms3) + path[1], math.fsum(ms4) + path[2],
                             math.fsum(ms5) + path[3], math.fsum(ms6), math.fsum(ms7) + path[4]
                , math.fsum(ms8) + path[5], math.fsum(ms9) + path[6],
                             math.fsum(ms10) + path[7],
                             math.fsum(ms12) + path[8],
                             math.fsum(ms13), math.fsum(ms14) + path[9],
                             math.fsum(ms15), math.fsum(ms16) + path[11],math.fsum(ms17)]
            makespan = math.fsum(makespan_cpus)
            print('Makespan is :', round(makespan, 2))

        elif len(x) == 18:
            ms1 = np.round(x[0] / fastest_processor, 2)
            ms2 = np.round(x[1] / fastest_processor, 2)
            ms3 = np.round(x[2] / fastest_processor, 2)
            ms4 = np.round(x[3] / fastest_processor, 2)
            ms5 = np.round(x[4] / fastest_processor, 2)
            ms6 = np.round(x[5] / fastest_processor, 2)
            ms7 = np.round(x[6] / fastest_processor, 2)
            ms8 = np.round(x[7] / fastest_processor, 2)
            ms9 = np.round(x[8] / fastest_processor, 2)
            ms10 = np.round(x[9] / fastest_processor, 2)
            ms11 = np.round(x[10] / fastest_processor, 2)
            ms12 = np.round(x[11] / fastest_processor, 2)
            ms13 = np.round(x[12] / fastest_processor, 2)
            ms14 = np.round(x[13] / fastest_processor, 2)
            ms15 = np.round(x[14] / fastest_processor, 2)
            ms16 = np.round(x[15] / fastest_processor, 2)
            ms17 = np.round(x[16] / fastest_processor, 2)
            ms18 = np.round(x[17] / fastest_processor, 2)
            run = [ms1, ms2, ms3, ms4, ms5, ms6,
                   ms7, ms8, ms9, ms10, ms11, ms12,
                   ms13, ms14, ms15, ms16, ms17,ms18]
            path = np.array([0.5, 0.1, 1, 1.7, 6.6, 11.7, 13.3, 14.79, 18.4, 19.9, 19.5, 13.6, 17.7])
            path_sum = math.fsum(path)
            msm1 = np.round(x[0] / p[1], 2)
            msm2 = np.round(x[1] / p[1], 2)
            msm3 = np.round(x[2] / p[1], 2)
            msm4 = np.round(x[3] / p[1], 2)
            msm5 = np.round(x[4] / p[1], 2)
            msm6 = np.round(x[5] / p[1], 2)
            msm7 = np.round(x[6] / p[1], 2)
            msm8 = np.round(x[7] / p[1], 2)
            msm9 = np.round(x[8] / p[1], 2)
            msm10 = np.round(x[9] / p[1], 2)
            msm11 = np.round(x[10] / p[1], 2)
            msm12 = np.round(x[11] / p[1], 2)
            msm13 = np.round(x[12] / p[1], 2)
            msm14 = np.round(x[13] / p[1], 2)
            msm15 = np.round(x[14] / p[1], 2)
            msm16 = np.round(x[15] / p[1], 2)
            msm17 = np.round(x[16] / p[1], 2)
            msm18 = np.round(x[17] / p[1], 2)
            task_min = [math.fsum(msm1), math.fsum(msm2),
                        math.fsum(msm3), math.fsum(msm4), math.fsum(msm5), math.fsum(msm6), math.fsum(msm7)
                , math.fsum(msm8), math.fsum(msm9), math.fsum(msm10), math.fsum(msm11),
                        math.fsum(msm12), math.fsum(msm13), math.fsum(msm14), math.fsum(msm15),
                        math.fsum(msm16), math.fsum(msm17), math.fsum(msm18)]
            task_min = math.fsum(task_min)
            print('Tasks on fastest processor :', round(task_min, 2))
            cp_min = [max(msm1), max(msm2), max(msm3), max(msm4), max(msm5),
                      max(msm6), max(msm7), max(msm8), max(msm9),
                      max(msm10), max(msm11), max(msm12),
                      max(msm13), max(msm14), max(msm15), max(msm16), max(msm17),max(msm18)]
            print('critical path on fastest cpu :', cp_min)
            cp_min = max(cp_min)
            print('makespan of cp on fastest cpu :', cp_min)
            cp = [max(ms1), max(ms2) + path[0], max(ms3) + path[1],
                  max(ms4) + path[2], max(ms5) + path[3], max(ms6),
                  max(ms7) + path[4], max(ms8) + path[5], max(ms9) + path[6],
                  max(ms10) + path[7], max(ms11), max(ms12) + path[8],
                  max(ms13), max(ms14) + path[9], max(ms15) + path[10], max(ms16), max(ms17),max(ms18)+path[12]]
            print('critical path :', cp)
            cp = max(cp)
            print('makespan of cp :', round(cp,2))
            print('\n----------------------------------')
            print('on p0=4:\n', ms1, '\non p1=12:\n', ms2, '\non p0=4:\n',
                  ms3, '\non p2=7:\n', ms4, '\non p1=12:\n', ms5, '\non p1=12:\n', ms6, '\non p1=12:\n', ms7,
                  '\non p1=12:\n', ms8, '\non p1=12:\n', ms9, '\non p0=4:\n', ms10, '\non p0=4:\n',
                  ms11, '\non p0=4:\n', ms12, '\non p1=12:\n', ms13, '\non p2=7:\n', ms14,
                  '\non p2=7:\n', ms15, '\non p1=12:\n', ms16, '\non p1=12:\n', ms17, '\non p1=12:\n', ms18)
            print('\n----------------------------------------------------------------')
            makespan_cpus = [math.fsum(ms1), math.fsum(ms2) + path[0],
                             math.fsum(ms3) + path[1], math.fsum(ms4) + path[2],
                             math.fsum(ms5) + path[3], math.fsum(ms6), math.fsum(ms7) + path[4]
                , math.fsum(ms8) + path[5], math.fsum(ms9) + path[6],
                             math.fsum(ms10) + path[7],
                             math.fsum(ms12) + path[8],
                             math.fsum(ms13), math.fsum(ms14) + path[9],
                             math.fsum(ms15), math.fsum(ms16) + path[11],
                             math.fsum(ms17),math.fsum(ms18)+path[12]]
            makespan = math.fsum(makespan_cpus)
            print('Makespan is :', round(makespan, 2))

        elif len(x) == 19:
            ms1 = np.round(x[0] / fastest_processor, 2)
            ms2 = np.round(x[1] / fastest_processor, 2)
            ms3 = np.round(x[2] / fastest_processor, 2)
            ms4 = np.round(x[3] / fastest_processor, 2)
            ms5 = np.round(x[4] / fastest_processor, 2)
            ms6 = np.round(x[5] / fastest_processor, 2)
            ms7 = np.round(x[6] / fastest_processor, 2)
            ms8 = np.round(x[7] / fastest_processor, 2)
            ms9 = np.round(x[8] / fastest_processor, 2)
            ms10 = np.round(x[9] / fastest_processor, 2)
            ms11 = np.round(x[10] / fastest_processor, 2)
            ms12 = np.round(x[11] / fastest_processor, 2)
            ms13 = np.round(x[12] / fastest_processor, 2)
            ms14 = np.round(x[13] / fastest_processor, 2)
            ms15 = np.round(x[14] / fastest_processor, 2)
            ms16 = np.round(x[15] / fastest_processor, 2)
            ms17 = np.round(x[16] / fastest_processor, 2)
            ms18 = np.round(x[17] / fastest_processor, 2)
            ms19 = np.round(x[18] / fastest_processor, 2)
            run = [ms1, ms2, ms3, ms4, ms5, ms6,
                   ms7, ms8, ms9, ms10, ms11, ms12,
                   ms13, ms14, ms15, ms16, ms17, ms18,ms19]
            path = np.array([0.5, 0.1, 1, 1.7, 6.6, 11.7, 13.3, 14.79, 18.4, 19.9, 19.5, 13.6, 17.7])
            path_sum = math.fsum(path)
            msm1 = np.round(x[0] / p[1], 2)
            msm2 = np.round(x[1] / p[1], 2)
            msm3 = np.round(x[2] / p[1], 2)
            msm4 = np.round(x[3] / p[1], 2)
            msm5 = np.round(x[4] / p[1], 2)
            msm6 = np.round(x[5] / p[1], 2)
            msm7 = np.round(x[6] / p[1], 2)
            msm8 = np.round(x[7] / p[1], 2)
            msm9 = np.round(x[8] / p[1], 2)
            msm10 = np.round(x[9] / p[1], 2)
            msm11 = np.round(x[10] / p[1], 2)
            msm12 = np.round(x[11] / p[1], 2)
            msm13 = np.round(x[12] / p[1], 2)
            msm14 = np.round(x[13] / p[1], 2)
            msm15 = np.round(x[14] / p[1], 2)
            msm16 = np.round(x[15] / p[1], 2)
            msm17 = np.round(x[16] / p[1], 2)
            msm18 = np.round(x[17] / p[1], 2)
            msm19 = np.round(x[18] / p[1], 2)
            task_min = [math.fsum(msm1), math.fsum(msm2),
                        math.fsum(msm3), math.fsum(msm4), math.fsum(msm5), math.fsum(msm6), math.fsum(msm7)
                , math.fsum(msm8), math.fsum(msm9), math.fsum(msm10), math.fsum(msm11),
                        math.fsum(msm12), math.fsum(msm13), math.fsum(msm14), math.fsum(msm15),
                        math.fsum(msm16), math.fsum(msm17), math.fsum(msm18), math.fsum(msm19)]
            task_min = math.fsum(task_min)
            print('Tasks on fastest processor :', round(task_min,2))
            cp_min = [max(msm1), max(msm2), max(msm3), max(msm4), max(msm5),
                      max(msm6), max(msm7), max(msm8), max(msm9),
                      max(msm10), max(msm11), max(msm12),
                      max(msm13), max(msm14), max(msm15), max(msm16), max(msm17), max(msm18),max(msm19)]
            print('critical path on fastest cpu :', cp_min)
            cp_min = max(cp_min)
            print('makespan of cp on fastest cpu :', cp_min)
            cp = [max(ms1), max(ms2) + path[0], max(ms3) + path[1],
                  max(ms4) + path[2], max(ms5) + path[3], max(ms6),
                  max(ms7) + path[4], max(ms8) + path[5], max(ms9) + path[6],
                  max(ms10) + path[7], max(ms11), max(ms12) + path[8],
                  max(ms13), max(ms14) + path[9], max(ms15) + path[10],
                  max(ms16), max(ms17),max(ms18)+path[12],max(ms19)]
            print('critical path :', cp)
            cp = max(cp)
            print('makespan of cp :', round(cp,2))
            print('\n----------------------------------')
            print('on p0=4:\n', ms1, '\non p1=12:\n', ms2, '\non p0=4:\n',
                  ms3, '\non p2=7:\n', ms4, '\non p1=12:\n', ms5, '\non p1=12:\n', ms6, '\non p1=12:\n', ms7,
                  '\non p1=12:\n', ms8, '\non p1=12:\n', ms9, '\non p0=4:\n', ms10, '\non p0=4:\n',
                  ms11, '\non p0=4:\n', ms12, '\non p1=12:\n', ms13, '\non p2=7:\n', ms14,
                  '\non p2=7:\n', ms15, '\non p1=12:\n', ms16, '\non p1=12:\n', ms17,
                  '\non p1=12:\n', ms18, '\non p0=4:\n', ms19)
            print('\n----------------------------------------------------------------')
            makespan_cpus = [math.fsum(ms1), math.fsum(ms2) + path[0],
                             math.fsum(ms3) + path[1], math.fsum(ms4) + path[2],
                             math.fsum(ms5) + path[3], math.fsum(ms6), math.fsum(ms7) + path[4]
                , math.fsum(ms8) + path[5], math.fsum(ms9) + path[6],
                             math.fsum(ms10) + path[7],
                             math.fsum(ms12) + path[8],
                             math.fsum(ms13), math.fsum(ms14) + path[9],
                             math.fsum(ms15), math.fsum(ms16) + path[11],
                             math.fsum(ms17), math.fsum(ms18) + path[12], math.fsum(ms19)]
            makespan = round(math.fsum(makespan_cpus),2)
            print('Makespan is :', makespan)

        SLR = round(makespan/cp_min,2)
        print('-> SLR is :',SLR)

        Speedup = round(task_min/makespan,2)
        print('-> Speed up is :',Speedup)

        Efficiency = round(Speedup/cpu_len,2)
        print('-> Efficiency is :',Efficiency)
        print('running on CPUS :' , run)
        print('makespan cpus :',makespan_cpus)

        CCR = round(path_sum/makespan,1)
        print('CCR :' ,CCR)

        with open (file_name,'a') as f :
            f.write(str(makespan))
            f.write(',')
        with open(file_name2, 'a') as f:
            f.write(str(SLR))
            f.write(',')
        with open(file_name3, 'a') as f:
            f.write(str(Speedup))
            f.write(',')
        with open(file_name4, 'a') as f:
            f.write(str(CCR))
            f.write(',')
        with open(file_name5, 'a') as f:
            f.write(str(Efficiency))
            f.write(',')

            if len(run) == 3 :
                fn = 'C:/Users/Naweed/PycharmProjects/IHHO/IHHO Dataset/IHHO run1.xlsx'
                with xlsxwriter.Workbook(fn) as workbook:
                    worksheet = workbook.add_worksheet('run')
                    worksheet.write(0, 0, 'Makespan:')
                    worksheet.write(0, 1, makespan)
                    worksheet.write(1, 0, 'SLR:')
                    worksheet.write(1, 1, SLR)
                    worksheet.write(2, 0, 'Speedup:')
                    worksheet.write(2, 1, Speedup)
                    worksheet.write(3, 0, 'Efficiency:')
                    worksheet.write(3, 1, Efficiency)
                    worksheet.write(4, 0, 'CCR:')
                    worksheet.write(4, 1, CCR)
                    worksheet.write(0, 2, '      ***')
                    worksheet.write(1, 2, '      ***')
                    worksheet.write(2, 2, '      ***')
                    worksheet.write(3, 2, '      ***')
                    worksheet.write(4, 2, '      ***')
                    worksheet.write(0, 3, 'p0:')
                    worksheet.write(1, 3, 'p1:')
                    worksheet.write(2, 3, 'p0:')

                    for row_num, data in enumerate(run):
                        worksheet.write_row(row_num, 4, data)

        if len(run) == 4:
            fn = 'C:/Users/Naweed/PycharmProjects/IHHO/IHHO Dataset/IHHO run2.xlsx'
            with xlsxwriter.Workbook(fn) as workbook:
                worksheet = workbook.add_worksheet('run')
                worksheet.write(0, 0, 'Makespan:')
                worksheet.write(0, 1, makespan)
                worksheet.write(1, 0, 'SLR:')
                worksheet.write(1, 1, SLR)
                worksheet.write(2, 0, 'Speedup:')
                worksheet.write(2, 1, Speedup)
                worksheet.write(3, 0, 'Efficiency:')
                worksheet.write(3, 1, Efficiency)
                worksheet.write(4, 0, 'CCR:')
                worksheet.write(4, 1, CCR)
                worksheet.write(0, 2, '      ***')
                worksheet.write(1, 2, '      ***')
                worksheet.write(2, 2, '      ***')
                worksheet.write(3, 2, '      ***')
                worksheet.write(4, 2, '      ***')
                worksheet.write(0, 3, 'p0:')
                worksheet.write(1, 3, 'p1:')
                worksheet.write(2, 3, 'p0:')
                worksheet.write(3, 3, 'p2:')

                for row_num, data in enumerate(run):
                    worksheet.write_row(row_num, 4, data)

        elif len (run) == 5 :
            fn = 'C:/Users/Naweed/PycharmProjects/IHHO/IHHO Dataset/IHHO run3.xlsx'
            with xlsxwriter.Workbook(fn) as workbook:
                worksheet = workbook.add_worksheet('run')
                worksheet.write(0, 0, 'Makespan:')
                worksheet.write(0, 1, makespan)
                worksheet.write(1, 0, 'SLR:')
                worksheet.write(1, 1, SLR)
                worksheet.write(2, 0, 'Speedup:')
                worksheet.write(2, 1, Speedup)
                worksheet.write(3, 0, 'Efficiency:')
                worksheet.write(3, 1, Efficiency)
                worksheet.write(4, 0, 'CCR:')
                worksheet.write(4, 1, CCR)
                worksheet.write(0, 2, '      ***')
                worksheet.write(1, 2, '      ***')
                worksheet.write(2, 2, '      ***')
                worksheet.write(3, 2, '      ***')
                worksheet.write(4, 2, '      ***')
                worksheet.write(0, 3, 'p0:')
                worksheet.write(1, 3, 'p1:')
                worksheet.write(2, 3, 'p0:')
                worksheet.write(3, 3, 'p2:')
                worksheet.write(4, 3, 'p1:')

                for row_num, data in enumerate(run):
                    worksheet.write_row(row_num, 4, data)

        elif len (run) == 6 :
            fn = 'C:/Users/Naweed/PycharmProjects/IHHO/IHHO Dataset/IHHO run4.xlsx'
            with xlsxwriter.Workbook(fn) as workbook:
                worksheet = workbook.add_worksheet('run')
                worksheet.write(0, 0, 'Makespan:')
                worksheet.write(0, 1, makespan)
                worksheet.write(1, 0, 'SLR:')
                worksheet.write(1, 1, SLR)
                worksheet.write(2, 0, 'Speedup:')
                worksheet.write(2, 1, Speedup)
                worksheet.write(3, 0, 'Efficiency:')
                worksheet.write(3, 1, Efficiency)
                worksheet.write(4, 0, 'CCR:')
                worksheet.write(4, 1, CCR)
                worksheet.write(0, 2, '      ***')
                worksheet.write(1, 2, '      ***')
                worksheet.write(2, 2, '      ***')
                worksheet.write(3, 2, '      ***')
                worksheet.write(4, 2, '      ***')
                worksheet.write(0, 3, 'p0:')
                worksheet.write(1, 3, 'p1:')
                worksheet.write(2, 3, 'p0:')
                worksheet.write(3, 3, 'p2:')
                worksheet.write(4, 3, 'p1:')
                worksheet.write(5, 3, 'p1:')

                for row_num, data in enumerate(run):
                    worksheet.write_row(row_num, 4, data)

        elif len (run) == 7 :
            fn = 'C:/Users/Naweed/PycharmProjects/IHHO/IHHO Dataset/IHHO run5.xlsx'
            with xlsxwriter.Workbook(fn) as workbook:
                worksheet = workbook.add_worksheet('run')
                worksheet.write(0, 0, 'Makespan:')
                worksheet.write(0, 1, makespan)
                worksheet.write(1, 0, 'SLR:')
                worksheet.write(1, 1, SLR)
                worksheet.write(2, 0, 'Speedup:')
                worksheet.write(2, 1, Speedup)
                worksheet.write(3, 0, 'Efficiency:')
                worksheet.write(3, 1, Efficiency)
                worksheet.write(4, 0, 'CCR:')
                worksheet.write(4, 1, CCR)
                worksheet.write(0, 2, '      ***')
                worksheet.write(1, 2, '      ***')
                worksheet.write(2, 2, '      ***')
                worksheet.write(3, 2, '      ***')
                worksheet.write(4, 2, '      ***')
                worksheet.write(0, 3, 'p0:')
                worksheet.write(1, 3, 'p1:')
                worksheet.write(2, 3, 'p0:')
                worksheet.write(3, 3, 'p2:')
                worksheet.write(4, 3, 'p1:')
                worksheet.write(5, 3, 'p1:')
                worksheet.write(6, 3, 'p1:')

                for row_num, data in enumerate(run):
                    worksheet.write_row(row_num, 4, data)

        elif len(run) == 8:
            fn = 'C:/Users/Naweed/PycharmProjects/IHHO/IHHO Dataset/IHHO run6.xlsx'
            with xlsxwriter.Workbook(fn) as workbook:
                worksheet = workbook.add_worksheet('run')
                worksheet.write(0, 0, 'Makespan:')
                worksheet.write(0, 1, makespan)
                worksheet.write(1, 0, 'SLR:')
                worksheet.write(1, 1, SLR)
                worksheet.write(2, 0, 'Speedup:')
                worksheet.write(2, 1, Speedup)
                worksheet.write(3, 0, 'Efficiency:')
                worksheet.write(3, 1, Efficiency)
                worksheet.write(4, 0, 'CCR:')
                worksheet.write(4, 1, CCR)
                worksheet.write(0, 2, '      ***')
                worksheet.write(1, 2, '      ***')
                worksheet.write(2, 2, '      ***')
                worksheet.write(3, 2, '      ***')
                worksheet.write(4, 2, '      ***')
                worksheet.write(0, 3, 'p0:')
                worksheet.write(1, 3, 'p1:')
                worksheet.write(2, 3, 'p0:')
                worksheet.write(3, 3, 'p2:')
                worksheet.write(4, 3, 'p1:')
                worksheet.write(5, 3, 'p1:')
                worksheet.write(6, 3, 'p1:')
                worksheet.write(7, 3, 'p2:')

                for row_num, data in enumerate(run):
                    worksheet.write_row(row_num, 4, data)

        elif len(run) == 9:
            fn = 'C:/Users/Naweed/PycharmProjects/IHHO/IHHO Dataset/IHHO run7.xlsx'
            with xlsxwriter.Workbook(fn) as workbook:
                worksheet = workbook.add_worksheet('run')
                worksheet.write(0, 0, 'Makespan:')
                worksheet.write(0, 1, makespan)
                worksheet.write(1, 0, 'SLR:')
                worksheet.write(1, 1, SLR)
                worksheet.write(2, 0, 'Speedup:')
                worksheet.write(2, 1, Speedup)
                worksheet.write(3, 0, 'Efficiency:')
                worksheet.write(3, 1, Efficiency)
                worksheet.write(4, 0, 'CCR:')
                worksheet.write(4, 1, CCR)
                worksheet.write(0, 2, '      ***')
                worksheet.write(1, 2, '      ***')
                worksheet.write(2, 2, '      ***')
                worksheet.write(3, 2, '      ***')
                worksheet.write(4, 2, '      ***')
                worksheet.write(0, 3, 'p0:')
                worksheet.write(1, 3, 'p1:')
                worksheet.write(2, 3, 'p0:')
                worksheet.write(3, 3, 'p2:')
                worksheet.write(4, 3, 'p1:')
                worksheet.write(5, 3, 'p1:')
                worksheet.write(6, 3, 'p1:')
                worksheet.write(8, 3, 'p2:')
                worksheet.write(7, 3, 'p1:')

                for row_num, data in enumerate(run):
                    worksheet.write_row(row_num, 4, data)

        elif len(run) == 10:
            fn = 'C:/Users/Naweed/PycharmProjects/IHHO/IHHO Dataset/IHHO run8.xlsx'
            with xlsxwriter.Workbook(fn) as workbook:
                worksheet = workbook.add_worksheet('run')
                worksheet.write(0, 0, 'Makespan:')
                worksheet.write(0, 1, makespan)
                worksheet.write(1, 0, 'SLR:')
                worksheet.write(1, 1, SLR)
                worksheet.write(2, 0, 'Speedup:')
                worksheet.write(2, 1, Speedup)
                worksheet.write(3, 0, 'Efficiency:')
                worksheet.write(3, 1, Efficiency)
                worksheet.write(4, 0, 'CCR:')
                worksheet.write(4, 1, CCR)
                worksheet.write(0, 2, '      ***')
                worksheet.write(1, 2, '      ***')
                worksheet.write(2, 2, '      ***')
                worksheet.write(3, 2, '      ***')
                worksheet.write(4, 2, '      ***')
                worksheet.write(0, 3, 'p0:')
                worksheet.write(1, 3, 'p1:')
                worksheet.write(2, 3, 'p0:')
                worksheet.write(3, 3, 'p2:')
                worksheet.write(4, 3, 'p1:')
                worksheet.write(5, 3, 'p1:')
                worksheet.write(6, 3, 'p1:')
                worksheet.write(7, 3, 'p2:')
                worksheet.write(8, 3, 'p1:')
                worksheet.write(9, 3, 'p1:')

                for row_num, data in enumerate(run):
                    worksheet.write_row(row_num, 4, data)

        elif len(run) == 11:
            fn = 'C:/Users/Naweed/PycharmProjects/IHHO/IHHO Dataset/IHHO run9.xlsx'
            with xlsxwriter.Workbook(fn) as workbook:
                worksheet = workbook.add_worksheet('run')
                worksheet.write(0, 0, 'Makespan:')
                worksheet.write(0, 1, makespan)
                worksheet.write(1, 0, 'SLR:')
                worksheet.write(1, 1, SLR)
                worksheet.write(2, 0, 'Speedup:')
                worksheet.write(2, 1, Speedup)
                worksheet.write(3, 0, 'Efficiency:')
                worksheet.write(3, 1, Efficiency)
                worksheet.write(4, 0, 'CCR:')
                worksheet.write(4, 1, CCR)
                worksheet.write(0, 2, '      ***')
                worksheet.write(1, 2, '      ***')
                worksheet.write(2, 2, '      ***')
                worksheet.write(3, 2, '      ***')
                worksheet.write(4, 2, '      ***')
                worksheet.write(0, 3, 'p0:')
                worksheet.write(1, 3, 'p1:')
                worksheet.write(2, 3, 'p0:')
                worksheet.write(3, 3, 'p2:')
                worksheet.write(4, 3, 'p1:')
                worksheet.write(5, 3, 'p1:')
                worksheet.write(6, 3, 'p1:')
                worksheet.write(7, 3, 'p2:')
                worksheet.write(8, 3, 'p1:')
                worksheet.write(9, 3, 'p1:')
                worksheet.write(10, 3, 'p0:')

                for row_num, data in enumerate(run):
                    worksheet.write_row(row_num, 4, data)

        elif len(run) == 12:
            fn = 'C:/Users/Naweed/PycharmProjects/IHHO/IHHO Dataset/IHHO run10.xlsx'
            with xlsxwriter.Workbook(fn) as workbook:
                worksheet = workbook.add_worksheet('run')
                worksheet.write(0, 0, 'Makespan:')
                worksheet.write(0, 1, makespan)
                worksheet.write(1, 0, 'SLR:')
                worksheet.write(1, 1, SLR)
                worksheet.write(2, 0, 'Speedup:')
                worksheet.write(2, 1, Speedup)
                worksheet.write(3, 0, 'Efficiency:')
                worksheet.write(3, 1, Efficiency)
                worksheet.write(4, 0, 'CCR:')
                worksheet.write(4, 1, CCR)
                worksheet.write(0, 2, '      ***')
                worksheet.write(1, 2, '      ***')
                worksheet.write(2, 2, '      ***')
                worksheet.write(3, 2, '      ***')
                worksheet.write(4, 2, '      ***')
                worksheet.write(0, 3, 'p0:')
                worksheet.write(1, 3, 'p1:')
                worksheet.write(2, 3, 'p0:')
                worksheet.write(3, 3, 'p2:')
                worksheet.write(4, 3, 'p1:')
                worksheet.write(5, 3, 'p1:')
                worksheet.write(6, 3, 'p1:')
                worksheet.write(7, 3, 'p2:')
                worksheet.write(8, 3, 'p1:')
                worksheet.write(9, 3, 'p1:')
                worksheet.write(10, 3, 'p0:')
                worksheet.write(11, 3, 'p1:')

                for row_num, data in enumerate(run):
                    worksheet.write_row(row_num, 4, data)

        elif len(run) == 13:
            fn = 'C:/Users/Naweed/PycharmProjects/IHHO/IHHO Dataset/IHHO run11.xlsx'
            with xlsxwriter.Workbook(fn) as workbook:
                worksheet = workbook.add_worksheet('run')
                worksheet.write(0, 0, 'Makespan:')
                worksheet.write(0, 1, makespan)
                worksheet.write(1, 0, 'SLR:')
                worksheet.write(1, 1, SLR)
                worksheet.write(2, 0, 'Speedup:')
                worksheet.write(2, 1, Speedup)
                worksheet.write(3, 0, 'Efficiency:')
                worksheet.write(3, 1, Efficiency)
                worksheet.write(4, 0, 'CCR:')
                worksheet.write(4, 1, CCR)
                worksheet.write(0, 2, '      ***')
                worksheet.write(1, 2, '      ***')
                worksheet.write(2, 2, '      ***')
                worksheet.write(3, 2, '      ***')
                worksheet.write(4, 2, '      ***')
                worksheet.write(0, 3, 'p0:')
                worksheet.write(1, 3, 'p1:')
                worksheet.write(2, 3, 'p0:')
                worksheet.write(3, 3, 'p2:')
                worksheet.write(4, 3, 'p1:')
                worksheet.write(5, 3, 'p1:')
                worksheet.write(6, 3, 'p1:')
                worksheet.write(7, 3, 'p2:')
                worksheet.write(8, 3, 'p1:')
                worksheet.write(9, 3, 'p1:')
                worksheet.write(10, 3, 'p0:')
                worksheet.write(11, 3, 'p1:')
                worksheet.write(12, 3, 'p1:')

                for row_num, data in enumerate(run):
                    worksheet.write_row(row_num, 4, data)

        elif len(run) == 14:
            fn = 'C:/Users/Naweed/PycharmProjects/IHHO/IHHO Dataset/IHHO run12.xlsx'
            with xlsxwriter.Workbook(fn) as workbook:
                worksheet = workbook.add_worksheet('run')
                worksheet.write(0, 0, 'Makespan:')
                worksheet.write(0, 1, makespan)
                worksheet.write(1, 0, 'SLR:')
                worksheet.write(1, 1, SLR)
                worksheet.write(2, 0, 'Speedup:')
                worksheet.write(2, 1, Speedup)
                worksheet.write(3, 0, 'Efficiency:')
                worksheet.write(3, 1, Efficiency)
                worksheet.write(4, 0, 'CCR:')
                worksheet.write(4, 1, CCR)
                worksheet.write(0, 2, '      ***')
                worksheet.write(1, 2, '      ***')
                worksheet.write(2, 2, '      ***')
                worksheet.write(3, 2, '      ***')
                worksheet.write(4, 2, '      ***')
                worksheet.write(0, 3, 'p0:')
                worksheet.write(1, 3, 'p1:')
                worksheet.write(2, 3, 'p0:')
                worksheet.write(3, 3, 'p2:')
                worksheet.write(4, 3, 'p1:')
                worksheet.write(5, 3, 'p1:')
                worksheet.write(6, 3, 'p1:')
                worksheet.write(7, 3, 'p2:')
                worksheet.write(8, 3, 'p1:')
                worksheet.write(9, 3, 'p1:')
                worksheet.write(10, 3, 'p0:')
                worksheet.write(11, 3, 'p1:')
                worksheet.write(12, 3, 'p1:')
                worksheet.write(13, 3, 'p2:')

                for row_num, data in enumerate(run):
                    worksheet.write_row(row_num, 4, data)

        elif len(run) == 15:
            fn = 'C:/Users/Naweed/PycharmProjects/IHHO/IHHO Dataset/IHHO run13.xlsx'
            with xlsxwriter.Workbook(fn) as workbook:
                worksheet = workbook.add_worksheet('run')
                worksheet.write(0, 0, 'Makespan:')
                worksheet.write(0, 1, makespan)
                worksheet.write(1, 0, 'SLR:')
                worksheet.write(1, 1, SLR)
                worksheet.write(2, 0, 'Speedup:')
                worksheet.write(2, 1, Speedup)
                worksheet.write(3, 0, 'Efficiency:')
                worksheet.write(3, 1, Efficiency)
                worksheet.write(4, 0, 'CCR:')
                worksheet.write(4, 1, CCR)
                worksheet.write(0, 2, '      ***')
                worksheet.write(1, 2, '      ***')
                worksheet.write(2, 2, '      ***')
                worksheet.write(3, 2, '      ***')
                worksheet.write(4, 2, '      ***')
                worksheet.write(0, 3, 'p0:')
                worksheet.write(1, 3, 'p1:')
                worksheet.write(2, 3, 'p0:')
                worksheet.write(3, 3, 'p2:')
                worksheet.write(4, 3, 'p1:')
                worksheet.write(5, 3, 'p1:')
                worksheet.write(6, 3, 'p1:')
                worksheet.write(7, 3, 'p2:')
                worksheet.write(8, 3, 'p1:')
                worksheet.write(9, 3, 'p1:')
                worksheet.write(10, 3, 'p0:')
                worksheet.write(11, 3, 'p1:')
                worksheet.write(12, 3, 'p1:')
                worksheet.write(13, 3, 'p2:')
                worksheet.write(14, 3, 'p2:')

                for row_num, data in enumerate(run):
                    worksheet.write_row(row_num, 4, data)

        elif len(run) == 16:
            fn = 'C:/Users/Naweed/PycharmProjects/IHHO/IHHO Dataset/IHHO run14.xlsx'
            with xlsxwriter.Workbook(fn) as workbook:
                worksheet = workbook.add_worksheet('run')
                worksheet.write(0, 0, 'Makespan:')
                worksheet.write(0, 1, makespan)
                worksheet.write(1, 0, 'SLR:')
                worksheet.write(1, 1, SLR)
                worksheet.write(2, 0, 'Speedup:')
                worksheet.write(2, 1, Speedup)
                worksheet.write(3, 0, 'Efficiency:')
                worksheet.write(3, 1, Efficiency)
                worksheet.write(4, 0, 'CCR:')
                worksheet.write(4, 1, CCR)
                worksheet.write(0, 2, '      ***')
                worksheet.write(1, 2, '      ***')
                worksheet.write(2, 2, '      ***')
                worksheet.write(3, 2, '      ***')
                worksheet.write(4, 2, '      ***')
                worksheet.write(0, 3, 'p0:')
                worksheet.write(1, 3, 'p1:')
                worksheet.write(2, 3, 'p0:')
                worksheet.write(3, 3, 'p2:')
                worksheet.write(4, 3, 'p1:')
                worksheet.write(5, 3, 'p1:')
                worksheet.write(6, 3, 'p1:')
                worksheet.write(7, 3, 'p2:')
                worksheet.write(8, 3, 'p1:')
                worksheet.write(9, 3, 'p1:')
                worksheet.write(10, 3, 'p0:')
                worksheet.write(11, 3, 'p1:')
                worksheet.write(12, 3, 'p1:')
                worksheet.write(13, 3, 'p2:')
                worksheet.write(14, 3, 'p2:')
                worksheet.write(15, 3, 'p1:')

                for row_num, data in enumerate(run):
                    worksheet.write_row(row_num, 4, data)

        elif len(run) == 17:
            fn = 'C:/Users/Naweed/PycharmProjects/IHHO/IHHO Dataset/IHHO run15.xlsx'
            with xlsxwriter.Workbook(fn) as workbook:
                worksheet = workbook.add_worksheet('run')
                worksheet.write(0, 0, 'Makespan:')
                worksheet.write(0, 1, makespan)
                worksheet.write(1, 0, 'SLR:')
                worksheet.write(1, 1, SLR)
                worksheet.write(2, 0, 'Speedup:')
                worksheet.write(2, 1, Speedup)
                worksheet.write(3, 0, 'Efficiency:')
                worksheet.write(3, 1, Efficiency)
                worksheet.write(4, 0, 'CCR:')
                worksheet.write(4, 1, CCR)
                worksheet.write(0, 2, '      ***')
                worksheet.write(1, 2, '      ***')
                worksheet.write(2, 2, '      ***')
                worksheet.write(3, 2, '      ***')
                worksheet.write(4, 2, '      ***')
                worksheet.write(0, 3, 'p0:')
                worksheet.write(1, 3, 'p1:')
                worksheet.write(2, 3, 'p0:')
                worksheet.write(3, 3, 'p2:')
                worksheet.write(4, 3, 'p1:')
                worksheet.write(5, 3, 'p1:')
                worksheet.write(6, 3, 'p1:')
                worksheet.write(7, 3, 'p2:')
                worksheet.write(8, 3, 'p1:')
                worksheet.write(9, 3, 'p1:')
                worksheet.write(10, 3, 'p0:')
                worksheet.write(11, 3, 'p1:')
                worksheet.write(12, 3, 'p1:')
                worksheet.write(13, 3, 'p2:')
                worksheet.write(14, 3, 'p2:')
                worksheet.write(15, 3, 'p1:')
                worksheet.write(16, 3, 'p1:')

                for row_num, data in enumerate(run):
                    worksheet.write_row(row_num, 4, data)

        elif len(run) == 18:
            fn = 'C:/Users/Naweed/PycharmProjects/IHHO/IHHO Dataset/IHHO run16.xlsx'
            with xlsxwriter.Workbook(fn) as workbook:
                worksheet = workbook.add_worksheet('run')
                worksheet.write(0, 0, 'Makespan:')
                worksheet.write(0, 1, makespan)
                worksheet.write(1, 0, 'SLR:')
                worksheet.write(1, 1, SLR)
                worksheet.write(2, 0, 'Speedup:')
                worksheet.write(2, 1, Speedup)
                worksheet.write(3, 0, 'Efficiency:')
                worksheet.write(3, 1, Efficiency)
                worksheet.write(4, 0, 'CCR:')
                worksheet.write(4, 1, CCR)
                worksheet.write(0, 2, '      ***')
                worksheet.write(1, 2, '      ***')
                worksheet.write(2, 2, '      ***')
                worksheet.write(3, 2, '      ***')
                worksheet.write(4, 2, '      ***')
                worksheet.write(0, 3, 'p0:')
                worksheet.write(1, 3, 'p1:')
                worksheet.write(2, 3, 'p0:')
                worksheet.write(3, 3, 'p2:')
                worksheet.write(4, 3, 'p1:')
                worksheet.write(5, 3, 'p1:')
                worksheet.write(6, 3, 'p1:')
                worksheet.write(7, 3, 'p2:')
                worksheet.write(8, 3, 'p1:')
                worksheet.write(9, 3, 'p1:')
                worksheet.write(10, 3, 'p0:')
                worksheet.write(11, 3, 'p1:')
                worksheet.write(12, 3, 'p1:')
                worksheet.write(13, 3, 'p2:')
                worksheet.write(14, 3, 'p2:')
                worksheet.write(15, 3, 'p1:')
                worksheet.write(16, 3, 'p1:')
                worksheet.write(17, 3, 'p1:')

                for row_num, data in enumerate(run):
                    worksheet.write_row(row_num, 4, data)

        elif len(run) == 19:
            fn = 'C:/Users/Naweed/PycharmProjects/IHHO/IHHO Dataset/IHHO run17.xlsx'
            with xlsxwriter.Workbook(fn) as workbook:
                worksheet = workbook.add_worksheet('run')
                worksheet.write(0, 0, 'Makespan:')
                worksheet.write(0, 1, makespan)
                worksheet.write(1, 0, 'SLR:')
                worksheet.write(1, 1, SLR)
                worksheet.write(2, 0, 'Speedup:')
                worksheet.write(2, 1, Speedup)
                worksheet.write(3, 0, 'Efficiency:')
                worksheet.write(3, 1, Efficiency)
                worksheet.write(4, 0, 'CCR:')
                worksheet.write(4, 1, CCR)
                worksheet.write(0, 2, '      ***')
                worksheet.write(1, 2, '      ***')
                worksheet.write(2, 2, '      ***')
                worksheet.write(3, 2, '      ***')
                worksheet.write(4, 2, '      ***')
                worksheet.write(0, 3, 'p0:')
                worksheet.write(1, 3, 'p1:')
                worksheet.write(2, 3, 'p0:')
                worksheet.write(3, 3, 'p2:')
                worksheet.write(4, 3, 'p1:')
                worksheet.write(5, 3, 'p1:')
                worksheet.write(6, 3, 'p1:')
                worksheet.write(7, 3, 'p2:')
                worksheet.write(8, 3, 'p1:')
                worksheet.write(9, 3, 'p1:')
                worksheet.write(10, 3, 'p0:')
                worksheet.write(11, 3, 'p1:')
                worksheet.write(12, 3, 'p1:')
                worksheet.write(13, 3, 'p2:')
                worksheet.write(14, 3, 'p2:')
                worksheet.write(15, 3, 'p1:')
                worksheet.write(16, 3, 'p1:')
                worksheet.write(17, 3, 'p1:')
                worksheet.write(18, 3, 'p0:')

                for row_num, data in enumerate(run):
                    worksheet.write_row(row_num, 4, data)
    except TypeError:
        print('\n')
        print('     *************************************************')
        print('     *  Size of input Graph arrays must not be equal *')
        print('     *              Try another Graph !              *')
        print('     *************************************************')


def Heft_Cpop (t) :
    p = np.array([4, 12, 7])
    fastes_processor = np.max(p)
    t = list(t)
    if t[0:len(t)] == t[0:len(t)]:
        t[0].append(0)
    t = np.array(t,dtype=object)
    if len(t) == 3 :
        t = np.sort(t)
        msm1 = np.round(t[0] / p[1], 2)
        msm2 = np.round(t[1] / p[1], 2)
        msm3 = np.round(t[2] / p[1], 2)
        task_min = [math.fsum(msm1), math.fsum(msm2),
                    math.fsum(msm3)]
        task_min = math.fsum(task_min)
        print('Tasks on fastest processor :', round(task_min, 2))
        cp_min = [max(msm1), max(msm2), max(msm3)]
        print('critical path on fastest cpu :', cp_min)
        cp_min = max(cp_min)
        print('makespan of cp on fastest cpu :', cp_min)
        blevel = np.amax(t)
        t = np.delete(t,len(t)-1)
        ms1 = np.round(t[0] / p[0],2)
        ms2 = np.round(t[1] / p[1],2)
        ms3 = np.round (blevel / fastes_processor,2)
        run = [ms1,ms2,ms3]
        run_c = [ms1, msm2, ms3]

        path = np.array([0.5, 0.1])
        path_sum = math.fsum(path)
        print(run)
        makespan = [math.fsum(ms1) , math.fsum(ms2)+path[0] , math.fsum(ms3)+path[1]]
        makespan = math.fsum(makespan)
        # print('HEFT Makespan is :' , round(makespan,2))

        makespan_c = [math.fsum(ms1), math.fsum(msm2) + path[0], math.fsum(ms3) + path[1]]
        makespan_c = math.fsum(makespan_c)

    elif len(t) == 4:
        t = np.sort(t)
        msm1 = np.round(t[0] / p[1], 2)
        msm2 = np.round(t[1] / p[1], 2)
        msm3 = np.round(t[2] / p[1], 2)
        msm4 = np.round(t[3] / p[1], 2)
        task_min = [math.fsum(msm1), math.fsum(msm2),
                    math.fsum(msm3), math.fsum(msm4)]
        task_min = math.fsum(task_min)
        print('Tasks on fastest processor :', round(task_min, 2))
        cp_min = [max(msm1), max(msm2), max(msm3), max(msm4)]
        print('critical path on fastest cpu :', cp_min)
        cp_min = max(cp_min)
        print('makespan of cp on fastest cpu :', cp_min)
        blevel = np.amax(t)
        t = np.delete(t, len(t) - 1)
        ms1 = np.round(t[0] / p[0], 2)
        ms2 = np.round(t[1] / p[1], 2)
        ms3 = np.round(t[2] / p[0], 2)
        ms4 = np.round(blevel / fastes_processor, 2)
        run = [ms1, ms2, ms3, ms4]
        run_c = [msm1, msm2, ms3, ms4]

        path = np.array([0.5, 0.1, 1])
        path_sum = math.fsum(path)
        print(run)
        makespan = [math.fsum(ms1), math.fsum(ms2) + path[0], math.fsum(ms3) + path[1],
                    math.fsum(ms4)+path[2]]
        makespan = round(math.fsum(makespan), 2)
        # print('HEFT Makespan is :', makespan)

        makespan_c = [math.fsum(msm1), math.fsum(msm2) + path[0], math.fsum(ms3) + path[1],
                    math.fsum(ms4) + path[2]]
        makespan_c = round(math.fsum(makespan_c), 2)

    elif len(t) == 5:
        t = np.sort(t)
        msm1 = np.round(t[0] / p[1], 2)
        msm2 = np.round(t[1] / p[1], 2)
        msm3 = np.round(t[2] / p[1], 2)
        msm4 = np.round(t[3] / p[1], 2)
        msm5 = np.round(t[4] / p[1], 2)
        task_min = [math.fsum(msm1), math.fsum(msm2),
                    math.fsum(msm3), math.fsum(msm4), math.fsum(msm5)]
        task_min = math.fsum(task_min)
        print('Tasks on fastest processor :', round(task_min, 2))
        cp_min = [max(msm1), max(msm2), max(msm3), max(msm4), max(msm5)]
        print('critical path on fastest cpu :', cp_min)
        cp_min = max(cp_min)
        print('makespan of cp on fastest cpu :', cp_min)
        blevel = np.amax(t)
        t = np.delete(t, len(t) - 1)
        ms1 = np.round(t[0] / p[0], 2)
        ms2 = np.round(t[1] / p[1], 2)
        ms3 = np.round(t[2] / p[0], 2)
        ms4 = np.round(t[3] / p[2] , 2)
        ms5 = np.round(blevel / fastes_processor, 2)
        run = [ms1, ms2, ms3, ms4, ms5]
        run_c = [msm1, msm2, ms3, ms4, ms5]

        path = np.array([0.5, 0.1, 1 , 1.7])
        path_sum = math.fsum(path)
        print(run)
        makespan = [math.fsum(ms1), math.fsum(ms2) + path[0], math.fsum(ms3) + path[1],
                    math.fsum(ms4) + path[2],math.fsum(ms5)+path[3]]
        makespan = round(math.fsum(makespan), 2)
        # print('HEFT Makespan is :', makespan)

        makespan_c = [math.fsum(msm1), math.fsum(msm2) + path[0], math.fsum(ms3) + path[1],
                    math.fsum(ms4) + path[2], math.fsum(ms5) + path[3]]
        makespan_c = round(math.fsum(makespan_c), 2)

    elif len(t) == 6:
        t = np.sort(t)
        msm1 = np.round(t[0] / p[1], 2)
        msm2 = np.round(t[1] / p[1], 2)
        msm3 = np.round(t[2] / p[1], 2)
        msm4 = np.round(t[3] / p[1], 2)
        msm5 = np.round(t[4] / p[1], 2)
        msm6 = np.round(t[5] / p[1], 2)
        task_min = [math.fsum(msm1), math.fsum(msm2),
                    math.fsum(msm3), math.fsum(msm4), math.fsum(msm5), math.fsum(msm6)]
        task_min = math.fsum(task_min)
        print('Tasks on fastest processor :', round(task_min, 2))
        cp_min = [max(msm1), max(msm2), max(msm3), max(msm4), max(msm5),
                  max(msm6)]
        print('critical path on fastest cpu :', cp_min)
        cp_min = max(cp_min)
        print('makespan of cp on fastest cpu :', cp_min)
        blevel = np.amax(t)
        t = np.delete(t, len(t) - 1)
        ms1 = np.round(t[0] / p[0], 2)
        ms2 = np.round(t[1] / p[1], 2)
        ms3 = np.round(t[2] / p[0], 2)
        ms4 = np.round(t[3] / p[2], 2)
        ms5 = np.round(t[4] / p[1], 2)
        ms6 = np.round(blevel / fastes_processor, 2)
        run = [ms1, ms2, ms3, ms4, ms5, ms6]
        run_c = [ms1, msm2, ms3, msm4, msm5, ms6]

        path = np.array([0.5, 0.1, 1, 1.7])
        path_sum = math.fsum(path)
        print(run)
        makespan = [math.fsum(ms1), math.fsum(ms2) + path[0], math.fsum(ms3) + path[1],
                    math.fsum(ms4) + path[2], math.fsum(ms5) + path[3] , math.fsum(ms6)]
        makespan = round(math.fsum(makespan), 2)
        # print('HEFT Makespan is :', makespan)

        makespan_c = [math.fsum(ms1), math.fsum(msm2) + path[0], math.fsum(ms3) + path[1],
                    math.fsum(msm4) + path[2], math.fsum(msm5) + path[3], math.fsum(ms6)]
        makespan_c = round(math.fsum(makespan_c), 2)

    elif len(t) == 7:
        t = np.sort(t)
        msm1 = np.round(t[0] / p[1], 2)
        msm2 = np.round(t[1] / p[1], 2)
        msm3 = np.round(t[2] / p[1], 2)
        msm4 = np.round(t[3] / p[1], 2)
        msm5 = np.round(t[4] / p[1], 2)
        msm6 = np.round(t[5] / p[1], 2)
        msm7 = np.round(t[6] / p[1], 2)
        task_min = [math.fsum(msm1), math.fsum(msm2),
                    math.fsum(msm3), math.fsum(msm4), math.fsum(msm5), math.fsum(msm6), math.fsum(msm7)]
        task_min = math.fsum(task_min)
        print('Tasks on fastest processor :', round(task_min, 2))
        cp_min = [max(msm1), max(msm2), max(msm3), max(msm4), max(msm5),
                  max(msm6), max(msm7)]
        print('critical path on fastest cpu :', cp_min)
        cp_min = max(cp_min)
        print('makespan of cp on fastest cpu :', cp_min)
        blevel = np.amax(t)
        t = np.delete(t, len(t) - 1)
        ms1 = np.round(t[0] / p[0], 2)
        ms2 = np.round(t[1] / p[1], 2)
        ms3 = np.round(t[2] / p[0], 2)
        ms4 = np.round(t[3] / p[2], 2)
        ms5 = np.round(t[4] / p[1], 2)
        ms6 = np.round(t[5] / p[1], 2)
        ms7 = np.round(blevel / fastes_processor, 2)
        run = [ms1, ms2, ms3, ms4, ms5, ms6, ms7]
        run_c = [msm1, ms2, ms3, msm4, ms5, ms6, ms7]

        path = np.array([0.5, 0.1, 1, 1.7 , 6.6])
        path_sum = math.fsum(path)
        print(run)
        makespan = [math.fsum(ms1), math.fsum(ms2) + path[0], math.fsum(ms3) + path[1],
                    math.fsum(ms4) + path[2], math.fsum(ms5) + path[3],
                    math.fsum(ms6) , math.fsum(ms7)+path[4]]
        makespan = round(math.fsum(makespan), 2)
        # print('HEFT Makespan is :', makespan)

        makespan_c = [math.fsum(msm1), math.fsum(ms2) + path[0], math.fsum(ms3) + path[1],
                    math.fsum(msm4) + path[2], math.fsum(ms5) + path[3],
                    math.fsum(ms6), math.fsum(ms7) + path[4]]
        makespan_c = round(math.fsum(makespan_c), 2)

    elif len(t) == 8:
        t = np.sort(t)
        msm1 = np.round(t[0] / p[1], 2)
        msm2 = np.round(t[1] / p[1], 2)
        msm3 = np.round(t[2] / p[1], 2)
        msm4 = np.round(t[3] / p[1], 2)
        msm5 = np.round(t[4] / p[1], 2)
        msm6 = np.round(t[5] / p[1], 2)
        msm7 = np.round(t[6] / p[1], 2)
        msm8 = np.round(t[7] / p[1], 2)
        task_min = [math.fsum(msm1), math.fsum(msm2),
                    math.fsum(msm3), math.fsum(msm4), math.fsum(msm5), math.fsum(msm6), math.fsum(msm7)
            , math.fsum(msm8)]
        task_min = math.fsum(task_min)
        print('Tasks on fastest processor :', round(task_min, 2))
        cp_min = [max(msm1), max(msm2), max(msm3), max(msm4), max(msm5),
                  max(msm6), max(msm7), max(msm8)]
        print('critical path on fastest cpu :', cp_min)
        cp_min = max(cp_min)
        print('makespan of cp on fastest cpu :', cp_min)
        blevel = np.amax(t)
        t = np.delete(t, len(t) - 1)
        ms1 = np.round(t[0] / p[0], 2)
        ms2 = np.round(t[1] / p[1], 2)
        ms3 = np.round(t[2] / p[0], 2)
        ms4 = np.round(t[3] / p[2], 2)
        ms5 = np.round(t[4] / p[1], 2)
        ms6 = np.round(t[5] / p[1], 2)
        ms7 = np.round(t[6] / p[0], 2)
        ms8 = np.round(blevel / fastes_processor, 2)
        run = [ms1, ms2, ms3, ms4, ms5, ms6, ms7, ms8]
        run_c = [msm1, msm2, msm3, ms4, ms5, ms6, ms7, ms8]

        path = np.array([0.5, 0.1, 1, 1.7 , 6.6, 11.7])
        path_sum = math.fsum(path)
        print(run)
        makespan = [math.fsum(ms1), math.fsum(ms2) + path[0], math.fsum(ms3) + path[1],
                    math.fsum(ms4) + path[2], math.fsum(ms5) + path[3],
                    math.fsum(ms6) , math.fsum(ms7)+path[4],math.fsum(ms8)+path[5]]
        makespan = round(math.fsum(makespan), 2)
        # print('HEFT Makespan is :', makespan)

        makespan_c = [math.fsum(msm1), math.fsum(msm2) + path[0], math.fsum(msm3) + path[1],
                    math.fsum(ms4) + path[2], math.fsum(ms5) + path[3],
                    math.fsum(ms6), math.fsum(ms7) + path[4], math.fsum(ms8) + path[5]]
        makespan_c = round(math.fsum(makespan_c), 2)

    elif len(t) == 9:
        t = np.sort(t)
        msm1 = np.round(t[0] / p[1], 2)
        msm2 = np.round(t[1] / p[1], 2)
        msm3 = np.round(t[2] / p[1], 2)
        msm4 = np.round(t[3] / p[1], 2)
        msm5 = np.round(t[4] / p[1], 2)
        msm6 = np.round(t[5] / p[1], 2)
        msm7 = np.round(t[6] / p[1], 2)
        msm8 = np.round(t[7] / p[1], 2)
        msm9 = np.round(t[8] / p[1], 2)
        task_min = [math.fsum(msm1), math.fsum(msm2),
                    math.fsum(msm3), math.fsum(msm4), math.fsum(msm5), math.fsum(msm6), math.fsum(msm7)
            , math.fsum(msm8), math.fsum(msm9)]
        task_min = math.fsum(task_min)
        print('Tasks on fastest processor :', round(task_min, 2))
        cp_min = [max(msm1), max(msm2), max(msm3), max(msm4), max(msm5),
                  max(msm6), max(msm7), max(msm8), max(msm9)]
        print('critical path on fastest cpu :', cp_min)
        cp_min = max(cp_min)
        print('makespan of cp on fastest cpu :', cp_min)
        blevel = np.amax(t)
        t = np.delete(t, len(t) - 1)
        ms1 = np.round(t[0] / p[0], 2)
        ms2 = np.round(t[1] / p[1], 2)
        ms3 = np.round(t[2] / p[0], 2)
        ms4 = np.round(t[3] / p[2], 2)
        ms5 = np.round(t[4] / p[1], 2)
        ms6 = np.round(t[5] / p[1], 2)
        ms7 = np.round(t[6] / p[0], 2)
        ms8 = np.round(t[7] / p[2], 2)
        ms9 = np.round(blevel / fastes_processor, 2)
        run = [ms1, ms2, ms3, ms4, ms5, ms6, ms7, ms8
            , ms9]
        run_c = [ms1, msm2, msm3, ms4, ms5, ms6, ms7, ms8
            , ms9]

        path = np.array([0.5, 0.1, 1, 1.7, 6.6, 11.7,13.3])
        path_sum = math.fsum(path)
        print(run)
        makespan = [math.fsum(ms1), math.fsum(ms2) + path[0], math.fsum(ms3) + path[1],
                    math.fsum(ms4) + path[2], math.fsum(ms5) + path[3],
                    math.fsum(ms6), math.fsum(ms7) + path[4],
                    math.fsum(ms8) + path[5],math.fsum(ms9)+path[6]]
        makespan = round(math.fsum(makespan), 2)
        # print('HEFT Makespan is :', makespan)

        makespan_c = [math.fsum(ms1), math.fsum(msm2) + path[0], math.fsum(msm3) + path[1],
                    math.fsum(ms4) + path[2], math.fsum(ms5) + path[3],
                    math.fsum(ms6), math.fsum(ms7) + path[4],
                    math.fsum(ms8) + path[5], math.fsum(ms9) + path[6]]
        makespan_c = round(math.fsum(makespan_c), 2)

    elif len(t) == 10:
        t = np.sort(t)
        msm1 = np.round(t[0] / p[1], 2)
        msm2 = np.round(t[1] / p[1], 2)
        msm3 = np.round(t[2] / p[1], 2)
        msm4 = np.round(t[3] / p[1], 2)
        msm5 = np.round(t[4] / p[1], 2)
        msm6 = np.round(t[5] / p[1], 2)
        msm7 = np.round(t[6] / p[1], 2)
        msm8 = np.round(t[7] / p[1], 2)
        msm9 = np.round(t[8] / p[1], 2)
        msm10 = np.round(t[9] / p[1], 2)
        task_min = [math.fsum(msm1), math.fsum(msm2),
                    math.fsum(msm3), math.fsum(msm4), math.fsum(msm5), math.fsum(msm6), math.fsum(msm7)
            , math.fsum(msm8), math.fsum(msm9), math.fsum(msm10)]
        task_min = math.fsum(task_min)
        print('Tasks on fastest processor :', round(task_min, 2))
        cp_min = [max(msm1), max(msm2), max(msm3), max(msm4), max(msm5),
                  max(msm6), max(msm7), max(msm8), max(msm9),
                  max(msm10)]
        print('critical path on fastest cpu :', cp_min)
        cp_min = max(cp_min)
        print('makespan of cp on fastest cpu :', cp_min)
        blevel = np.amax(t)
        t = np.delete(t, len(t) - 1)
        ms1 = np.round(t[0] / p[0], 2)
        ms2 = np.round(t[1] / p[1], 2)
        ms3 = np.round(t[2] / p[0], 2)
        ms4 = np.round(t[3] / p[2], 2)
        ms5 = np.round(t[4] / p[1], 2)
        ms6 = np.round(t[5] / p[1], 2)
        ms7 = np.round(t[6] / p[0], 2)
        ms8 = np.round(t[7] / p[2], 2)
        ms9 = np.round(t[8] / p[1], 2)
        ms10 = np.round(blevel / fastes_processor, 2)
        run = [ms1, ms2, ms3, ms4, ms5, ms6, ms7, ms8
            , ms9, ms10]
        run_c = [ms1, msm2, msm3, ms4, msm5, ms6, ms7, ms8
            , msm9, ms10]

        path = np.array([0.5, 0.1, 1, 1.7, 6.6, 11.7,13.3, 14.79])
        path_sum = math.fsum(path)
        print(run)
        makespan = [math.fsum(ms1), math.fsum(ms2) + path[0], math.fsum(ms3) + path[1],
                    math.fsum(ms4) + path[2], math.fsum(ms5) + path[3],
                    math.fsum(ms6), math.fsum(ms7) + path[4],
                    math.fsum(ms8) + path[5],math.fsum(ms9)+path[6],math.fsum(ms10)+path[7]]
        makespan = round(math.fsum(makespan), 2)
        # print('HEFT Makespan is :', makespan)

        makespan_c = [math.fsum(ms1), math.fsum(msm2) + path[0], math.fsum(msm3) + path[1],
                    math.fsum(ms4) + path[2], math.fsum(msm5) + path[3],
                    math.fsum(ms6), math.fsum(ms7) + path[4],
                    math.fsum(ms8) + path[5], math.fsum(msm9) + path[6], math.fsum(ms10) + path[7]]
        makespan_c = round(math.fsum(makespan_c), 2)

    elif len(t) == 11:
        t = np.sort(t)
        msm1 = np.round(t[0] / p[1], 2)
        msm2 = np.round(t[1] / p[1], 2)
        msm3 = np.round(t[2] / p[1], 2)
        msm4 = np.round(t[3] / p[1], 2)
        msm5 = np.round(t[4] / p[1], 2)
        msm6 = np.round(t[5] / p[1], 2)
        msm7 = np.round(t[6] / p[1], 2)
        msm8 = np.round(t[7] / p[1], 2)
        msm9 = np.round(t[8] / p[1], 2)
        msm10 = np.round(t[9] / p[1], 2)
        msm11 = np.round(t[10] / p[1], 2)
        task_min = [math.fsum(msm1), math.fsum(msm2),
                    math.fsum(msm3), math.fsum(msm4), math.fsum(msm5), math.fsum(msm6), math.fsum(msm7)
            , math.fsum(msm8), math.fsum(msm9), math.fsum(msm10), math.fsum(msm11)]
        task_min = math.fsum(task_min)
        print('Tasks on fastest processor :', round(task_min, 2))
        cp_min = [max(msm1), max(msm2), max(msm3), max(msm4), max(msm5),
                  max(msm6), max(msm7), max(msm8), max(msm9),
                  max(msm10), max(msm11)]
        print('critical path on fastest cpu :', cp_min)
        cp_min = max(cp_min)
        print('makespan of cp on fastest cpu :', cp_min)
        blevel = np.amax(t)
        t = np.delete(t, len(t) - 1)
        ms1 = np.round(t[0] / p[0], 2)
        ms2 = np.round(t[1] / p[1], 2)
        ms3 = np.round(t[2] / p[0], 2)
        ms4 = np.round(t[3] / p[2], 2)
        ms5 = np.round(t[4] / p[1], 2)
        ms6 = np.round(t[5] / p[1], 2)
        ms7 = np.round(t[6] / p[0], 2)
        ms8 = np.round(t[7] / p[2], 2)
        ms9 = np.round(t[8] / p[1], 2)
        ms10 = np.round(t[9] / p[0], 2)
        ms11 = np.round(blevel / fastes_processor, 2)
        run = [ms1, ms2, ms3, ms4, ms5, ms6, ms7, ms8
            , ms9, ms10, ms11]
        run_c = [ms1, msm2, msm3, ms4, msm5, ms6, msm7, ms8
            , ms9, ms10, ms11]

        path = np.array([0.5, 0.1, 1, 1.7, 6.6, 11.7,13.3, 14.79])
        path_sum = math.fsum(path)
        print(run)
        makespan = [math.fsum(ms1), math.fsum(ms2) + path[0], math.fsum(ms3) + path[1],
                    math.fsum(ms4) + path[2], math.fsum(ms5) + path[3],
                    math.fsum(ms6), math.fsum(ms7) + path[4],
                    math.fsum(ms8) + path[5],math.fsum(ms9)+path[6],
                    math.fsum(ms10)+path[7] , math.fsum(ms11)]
        makespan = round(math.fsum(makespan), 2)
        # print('HEFT Makespan is :', makespan)

        makespan_c = [math.fsum(ms1), math.fsum(msm2) + path[0], math.fsum(msm3) + path[1],
                    math.fsum(ms4) + path[2], math.fsum(msm5) + path[3],
                    math.fsum(ms6), math.fsum(msm7) + path[4],
                    math.fsum(ms8) + path[5], math.fsum(ms9) + path[6],
                    math.fsum(ms10) + path[7], math.fsum(ms11)]
        makespan_c = round(math.fsum(makespan_c), 2)

    elif len(t) == 12:
        t = np.sort(t)
        msm1 = np.round(t[0] / p[1], 2)
        msm2 = np.round(t[1] / p[1], 2)
        msm3 = np.round(t[2] / p[1], 2)
        msm4 = np.round(t[3] / p[1], 2)
        msm5 = np.round(t[4] / p[1], 2)
        msm6 = np.round(t[5] / p[1], 2)
        msm7 = np.round(t[6] / p[1], 2)
        msm8 = np.round(t[7] / p[1], 2)
        msm9 = np.round(t[8] / p[1], 2)
        msm10 = np.round(t[9] / p[1], 2)
        msm11 = np.round(t[10] / p[1], 2)
        msm12 = np.round(t[11] / p[1], 2)
        task_min = [math.fsum(msm1), math.fsum(msm2),
                    math.fsum(msm3), math.fsum(msm4), math.fsum(msm5), math.fsum(msm6), math.fsum(msm7)
            , math.fsum(msm8), math.fsum(msm9), math.fsum(msm10), math.fsum(msm11),
                    math.fsum(msm12)]
        task_min = math.fsum(task_min)
        print('Tasks on fastest processor :', round(task_min, 2))
        cp_min = [max(msm1), max(msm2), max(msm3), max(msm4), max(msm5),
                  max(msm6), max(msm7), max(msm8), max(msm9),
                  max(msm10), max(msm11), max(msm12)]
        print('critical path on fastest cpu :', cp_min)
        cp_min = max(cp_min)
        print('makespan of cp on fastest cpu :', cp_min)
        blevel = np.amax(t)
        t = np.delete(t, len(t) - 1)
        ms1 = np.round(t[0] / p[0], 2)
        ms2 = np.round(t[1] / p[1], 2)
        ms3 = np.round(t[2] / p[0], 2)
        ms4 = np.round(t[3] / p[2], 2)
        ms5 = np.round(t[4] / p[1], 2)
        ms6 = np.round(t[5] / p[1], 2)
        ms7 = np.round(t[6] / p[0], 2)
        ms8 = np.round(t[7] / p[2], 2)
        ms9 = np.round(t[8] / p[1], 2)
        ms10 = np.round(t[9] / p[0], 2)
        ms11 = np.round(t[10] / p[0], 2)
        ms12 = np.round(blevel / fastes_processor, 2)
        run = [ms1, ms2, ms3, ms4, ms5, ms6, ms7, ms8
            , ms9, ms10, ms11, ms12]
        run_c = [msm1, msm2, ms3, ms4, ms5, ms6, ms7, msm8
            , ms9, ms10, ms11, ms12]

        path = np.array([0.5, 0.1, 1, 1.7, 6.6, 11.7,13.3, 14.79 , 18.4])
        path_sum = math.fsum(path)
        print(run)
        makespan = [math.fsum(ms1), math.fsum(ms2) + path[0], math.fsum(ms3) + path[1],
                    math.fsum(ms4) + path[2], math.fsum(ms5) + path[3],
                    math.fsum(ms6), math.fsum(ms7) + path[4],
                    math.fsum(ms8) + path[5],math.fsum(ms9)+path[6],
                    math.fsum(ms10)+path[7] , math.fsum(ms11) , math.fsum(ms12)+path[8]]
        makespan = round(math.fsum(makespan), 2)
        # print('HEFT Makespan is :', makespan)

        makespan_c = [math.fsum(msm1), math.fsum(msm2) + path[0], math.fsum(ms3) + path[1],
                    math.fsum(ms4) + path[2], math.fsum(ms5) + path[3],
                    math.fsum(ms6), math.fsum(ms7) + path[4],
                    math.fsum(msm8) + path[5], math.fsum(ms9) + path[6],
                    math.fsum(ms10) + path[7], math.fsum(ms11), math.fsum(ms12) + path[8]]
        makespan_c = round(math.fsum(makespan_c), 2)

    elif len(t) == 13:
        t = np.sort(t)
        msm1 = np.round(t[0] / p[1], 2)
        msm2 = np.round(t[1] / p[1], 2)
        msm3 = np.round(t[2] / p[1], 2)
        msm4 = np.round(t[3] / p[1], 2)
        msm5 = np.round(t[4] / p[1], 2)
        msm6 = np.round(t[5] / p[1], 2)
        msm7 = np.round(t[6] / p[1], 2)
        msm8 = np.round(t[7] / p[1], 2)
        msm9 = np.round(t[8] / p[1], 2)
        msm10 = np.round(t[9] / p[1], 2)
        msm11 = np.round(t[10] / p[1], 2)
        msm12 = np.round(t[11] / p[1], 2)
        msm13 = np.round(t[12] / p[1], 2)
        task_min = [math.fsum(msm1), math.fsum(msm2),
                    math.fsum(msm3), math.fsum(msm4), math.fsum(msm5), math.fsum(msm6), math.fsum(msm7)
            , math.fsum(msm8), math.fsum(msm9), math.fsum(msm10), math.fsum(msm11),
                    math.fsum(msm12), math.fsum(msm13)]
        task_min = math.fsum(task_min)
        print('Tasks on fastest processor :', round(task_min, 2))
        cp_min = [max(msm1), max(msm2), max(msm3), max(msm4), max(msm5),
                  max(msm6), max(msm7), max(msm8), max(msm9),
                  max(msm10), max(msm11), max(msm12),
                  max(msm13)]
        print('critical path on fastest cpu :', cp_min)
        cp_min = max(cp_min)
        print('makespan of cp on fastest cpu :', cp_min)
        blevel = np.amax(t)
        t = np.delete(t, len(t) - 1)
        ms1 = np.round(t[0] / p[0], 2)
        ms2 = np.round(t[1] / p[1], 2)
        ms3 = np.round(t[2] / p[0], 2)
        ms4 = np.round(t[3] / p[2], 2)
        ms5 = np.round(t[4] / p[1], 2)
        ms6 = np.round(t[5] / p[1], 2)
        ms7 = np.round(t[6] / p[0], 2)
        ms8 = np.round(t[7] / p[2], 2)
        ms9 = np.round(t[8] / p[1], 2)
        ms10 = np.round(t[9] / p[0], 2)
        ms11 = np.round(t[10] / p[0], 2)
        ms12 = np.round(t[11] / p[1], 2)
        ms13 = np.round(blevel / fastes_processor, 2)
        run = [ms1, ms2, ms3, ms4, ms5, ms6, ms7, ms8
            , ms9, ms10, ms11, ms12, ms13]
        run_c = [msm1, ms2, ms3, msm4, ms5, msm6, ms7, ms8
            , ms9, ms10, ms11, msm12, ms13]

        path = np.array([0.5, 0.1, 1, 1.7, 6.6, 11.7,13.3, 14.79 , 18.4])
        path_sum = math.fsum(path)
        print(run)
        makespan = [math.fsum(ms1), math.fsum(ms2) + path[0], math.fsum(ms3) + path[1],
                    math.fsum(ms4) + path[2], math.fsum(ms5) + path[3],
                    math.fsum(ms6), math.fsum(ms7) + path[4],
                    math.fsum(ms8) + path[5],math.fsum(ms9)+path[6],
                    math.fsum(ms10)+path[7] , math.fsum(ms11) ,
                    math.fsum(ms12)+path[8] , math.fsum(ms13)]
        makespan = round(math.fsum(makespan), 2)
        # print('HEFT Makespan is :', makespan)

        makespan_c = [math.fsum(msm1), math.fsum(ms2) + path[0], math.fsum(ms3) + path[1],
                    math.fsum(msm4) + path[2], math.fsum(ms5) + path[3],
                    math.fsum(msm6), math.fsum(ms7) + path[4],
                    math.fsum(ms8) + path[5], math.fsum(ms9) + path[6],
                    math.fsum(ms10) + path[7], math.fsum(ms11),
                    math.fsum(msm12) + path[8], math.fsum(ms13)]
        makespan_c = round(math.fsum(makespan_c), 2)

    elif len(t) == 14:
        t = np.sort(t)
        msm1 = np.round(t[0] / p[1], 2)
        msm2 = np.round(t[1] / p[1], 2)
        msm3 = np.round(t[2] / p[1], 2)
        msm4 = np.round(t[3] / p[1], 2)
        msm5 = np.round(t[4] / p[1], 2)
        msm6 = np.round(t[5] / p[1], 2)
        msm7 = np.round(t[6] / p[1], 2)
        msm8 = np.round(t[7] / p[1], 2)
        msm9 = np.round(t[8] / p[1], 2)
        msm10 = np.round(t[9] / p[1], 2)
        msm11 = np.round(t[10] / p[1], 2)
        msm12 = np.round(t[11] / p[1], 2)
        msm13 = np.round(t[12] / p[1], 2)
        msm14 = np.round(t[13] / p[1], 2)
        task_min = [math.fsum(msm1), math.fsum(msm2),
                    math.fsum(msm3), math.fsum(msm4), math.fsum(msm5), math.fsum(msm6), math.fsum(msm7)
            , math.fsum(msm8), math.fsum(msm9), math.fsum(msm10), math.fsum(msm11),
                    math.fsum(msm12), math.fsum(msm13), math.fsum(msm14)]
        task_min = math.fsum(task_min)
        print('Tasks on fastest processor :', round(task_min, 2))
        cp_min = [max(msm1), max(msm2), max(msm3), max(msm4), max(msm5),
                  max(msm6), max(msm7), max(msm8), max(msm9),
                  max(msm10), max(msm11), max(msm12),
                  max(msm13), max(msm14)]
        print('critical path on fastest cpu :', cp_min)
        cp_min = max(cp_min)
        print('makespan of cp on fastest cpu :', cp_min)
        blevel = np.amax(t)
        t = np.delete(t, len(t) - 1)
        ms1 = np.round(t[0] / p[0], 2)
        ms2 = np.round(t[1] / p[1], 2)
        ms3 = np.round(t[2] / p[0], 2)
        ms4 = np.round(t[3] / p[2], 2)
        ms5 = np.round(t[4] / p[1], 2)
        ms6 = np.round(t[5] / p[1], 2)
        ms7 = np.round(t[6] / p[0], 2)
        ms8 = np.round(t[7] / p[2], 2)
        ms9 = np.round(t[8] / p[1], 2)
        ms10 = np.round(t[9] / p[0], 2)
        ms11 = np.round(t[10] / p[0], 2)
        ms12 = np.round(t[11] / p[1], 2)
        ms13 = np.round(t[12] / p[1], 2)
        ms14 = np.round(blevel / fastes_processor, 2)
        run = [ms1, ms2, ms3, ms4, ms5, ms6, ms7, ms8
            , ms9, ms10, ms11, ms12, ms13, ms14]
        run_c = [ms1, ms2, ms3, msm4, ms5, ms6, ms7, ms8
            , msm9, ms10, ms11, ms12, msm13, ms14]

        path = np.array([0.5, 0.1, 1, 1.7, 6.6, 11.7, 13.3, 14.79, 18.4,19.9])
        path_sum = math.fsum(path)
        print(run)
        makespan = [math.fsum(ms1), math.fsum(ms2) + path[0], math.fsum(ms3) + path[1],
                    math.fsum(ms4) + path[2], math.fsum(ms5) + path[3],
                    math.fsum(ms6), math.fsum(ms7) + path[4],
                    math.fsum(ms8) + path[5], math.fsum(ms9) + path[6],
                    math.fsum(ms10) + path[7], math.fsum(ms11),
                    math.fsum(ms12) + path[8], math.fsum(ms13),math.fsum(ms14)+path[9]]
        makespan = round(math.fsum(makespan), 2)
        # print('HEFT Makespan is :', makespan)

        makespan_c = [math.fsum(ms1), math.fsum(ms2) + path[0], math.fsum(ms3) + path[1],
                    math.fsum(msm4) + path[2], math.fsum(ms5) + path[3],
                    math.fsum(ms6), math.fsum(ms7) + path[4],
                    math.fsum(ms8) + path[5], math.fsum(msm9) + path[6],
                    math.fsum(ms10) + path[7], math.fsum(ms11),
                    math.fsum(ms12) + path[8], math.fsum(msm13), math.fsum(ms14) + path[9]]
        makespan_c = round(math.fsum(makespan_c), 2)

    elif len(t) == 15:
        t = np.sort(t)
        msm1 = np.round(t[0] / p[1], 2)
        msm2 = np.round(t[1] / p[1], 2)
        msm3 = np.round(t[2] / p[1], 2)
        msm4 = np.round(t[3] / p[1], 2)
        msm5 = np.round(t[4] / p[1], 2)
        msm6 = np.round(t[5] / p[1], 2)
        msm7 = np.round(t[6] / p[1], 2)
        msm8 = np.round(t[7] / p[1], 2)
        msm9 = np.round(t[8] / p[1], 2)
        msm10 = np.round(t[9] / p[1], 2)
        msm11 = np.round(t[10] / p[1], 2)
        msm12 = np.round(t[11] / p[1], 2)
        msm13 = np.round(t[12] / p[1], 2)
        msm14 = np.round(t[13] / p[1], 2)
        msm15 = np.round(t[14] / p[1], 2)
        task_min = [math.fsum(msm1), math.fsum(msm2),
                    math.fsum(msm3), math.fsum(msm4), math.fsum(msm5), math.fsum(msm6), math.fsum(msm7)
            , math.fsum(msm8), math.fsum(msm9), math.fsum(msm10), math.fsum(msm11),
                    math.fsum(msm12), math.fsum(msm13), math.fsum(msm14), math.fsum(msm15)]
        task_min = math.fsum(task_min)
        print('Tasks on fastest processor :', round(task_min, 2))
        cp_min = [max(msm1), max(msm2), max(msm3), max(msm4), max(msm5),
                  max(msm6), max(msm7), max(msm8), max(msm9),
                  max(msm10), max(msm11), max(msm12),
                  max(msm13), max(msm14), max(msm15)]
        print('critical path on fastest cpu :', cp_min)
        cp_min = max(cp_min)
        print('makespan of cp on fastest cpu :', cp_min)
        blevel = np.amax(t)
        t = np.delete(t, len(t) - 1)
        ms1 = np.round(t[0] / p[0], 2)
        ms2 = np.round(t[1] / p[1], 2)
        ms3 = np.round(t[2] / p[0], 2)
        ms4 = np.round(t[3] / p[2], 2)
        ms5 = np.round(t[4] / p[1], 2)
        ms6 = np.round(t[5] / p[1], 2)
        ms7 = np.round(t[6] / p[0], 2)
        ms8 = np.round(t[7] / p[2], 2)
        ms9 = np.round(t[8] / p[1], 2)
        ms10 = np.round(t[9] / p[0], 2)
        ms11 = np.round(t[10] / p[0], 2)
        ms12 = np.round(t[11] / p[1], 2)
        ms13 = np.round(t[12] / p[1], 2)
        ms14 = np.round(t[13] / p[2], 2)
        ms15 = np.round(blevel / fastes_processor, 2)
        run = [ms1, ms2, ms3, ms4, ms5, ms6, ms7, ms8
            , ms9, ms10, ms11, ms12, ms13, ms14, ms15]
        run_c = [msm1, ms2, ms3, msm4, ms5, ms6, ms7, ms8
            , ms9, msm10, ms11, ms12, ms13, ms14, ms15]

        path = np.array([0.5, 0.1, 1, 1.7, 6.6, 11.7, 13.3, 14.79, 18.4, 19.9])
        path_sum = math.fsum(path)
        print(run)
        makespan = [math.fsum(ms1), math.fsum(ms2) + path[0], math.fsum(ms3) + path[1],
                    math.fsum(ms4) + path[2], math.fsum(ms5) + path[3],
                    math.fsum(ms6), math.fsum(ms7) + path[4],
                    math.fsum(ms8) + path[5], math.fsum(ms9) + path[6],
                    math.fsum(ms10) + path[7], math.fsum(ms11),
                    math.fsum(ms12) + path[8], math.fsum(ms13),
                    math.fsum(ms14) + path[9] , math.fsum(ms15)]
        makespan = round(math.fsum(makespan), 2)
        # print('HEFT Makespan is :', makespan)

        makespan_c = [math.fsum(msm1), math.fsum(ms2) + path[0], math.fsum(ms3) + path[1],
                    math.fsum(msm4) + path[2], math.fsum(ms5) + path[3],
                    math.fsum(ms6), math.fsum(ms7) + path[4],
                    math.fsum(ms8) + path[5], math.fsum(ms9) + path[6],
                    math.fsum(msm10) + path[7], math.fsum(ms11),
                    math.fsum(ms12) + path[8], math.fsum(ms13),
                    math.fsum(ms14) + path[9], math.fsum(ms15)]
        makespan_c = round(math.fsum(makespan_c), 2)

    elif len(t) == 16:
        t = np.sort(t)
        msm1 = np.round(t[0] / p[1], 2)
        msm2 = np.round(t[1] / p[1], 2)
        msm3 = np.round(t[2] / p[1], 2)
        msm4 = np.round(t[3] / p[1], 2)
        msm5 = np.round(t[4] / p[1], 2)
        msm6 = np.round(t[5] / p[1], 2)
        msm7 = np.round(t[6] / p[1], 2)
        msm8 = np.round(t[7] / p[1], 2)
        msm9 = np.round(t[8] / p[1], 2)
        msm10 = np.round(t[9] / p[1], 2)
        msm11 = np.round(t[10] / p[1], 2)
        msm12 = np.round(t[11] / p[1], 2)
        msm13 = np.round(t[12] / p[1], 2)
        msm14 = np.round(t[13] / p[1], 2)
        msm15 = np.round(t[14] / p[1], 2)
        msm16 = np.round(t[15] / p[1], 2)
        task_min = [math.fsum(msm1), math.fsum(msm2),
                    math.fsum(msm3), math.fsum(msm4), math.fsum(msm5), math.fsum(msm6), math.fsum(msm7)
            , math.fsum(msm8), math.fsum(msm9), math.fsum(msm10), math.fsum(msm11),
                    math.fsum(msm12), math.fsum(msm13), math.fsum(msm14), math.fsum(msm15),
                    math.fsum(msm16)]
        task_min = math.fsum(task_min)
        print('Tasks on fastest processor :', round(task_min, 2))
        cp_min = [max(msm1), max(msm2), max(msm3), max(msm4), max(msm5),
                  max(msm6), max(msm7), max(msm8), max(msm9),
                  max(msm10), max(msm11), max(msm12),
                  max(msm13), max(msm14), max(msm15), max(msm16)]
        print('critical path on fastest cpu :', cp_min)
        cp_min = max(cp_min)
        print('makespan of cp on fastest cpu :', cp_min)

        blevel = np.amax(t)
        t = np.delete(t, len(t) - 1)
        ms1 = np.round(t[0] / p[0], 2)
        ms2 = np.round(t[1] / p[1], 2)
        ms3 = np.round(t[2] / p[0], 2)
        ms4 = np.round(t[3] / p[2], 2)
        ms5 = np.round(t[4] / p[1], 2)
        ms6 = np.round(t[5] / p[1], 2)
        ms7 = np.round(t[6] / p[0], 2)
        ms8 = np.round(t[7] / p[2], 2)
        ms9 = np.round(t[8] / p[1], 2)
        ms10 = np.round(t[9] / p[0], 2)
        ms11 = np.round(t[10] / p[0], 2)
        ms12 = np.round(t[11] / p[1], 2)
        ms13 = np.round(t[12] / p[1], 2)
        ms14 = np.round(t[13] / p[2], 2)
        ms15 = np.round(t[14] / p[2], 2)
        ms16 = np.round(blevel / fastes_processor, 2)
        run = [ms1, ms2, ms3, ms4, ms5, ms6, ms7, ms8
            , ms9, ms10, ms11, ms12, ms13, ms14, ms15,
               ms16]
        run_c = [msm1, ms2, ms3, ms4, ms5, msm6, ms7, ms8
            , ms9, ms10, ms11, msm12, ms13, ms14, ms15,
               ms16]
        path = np.array([0.5, 0.1, 1, 1.7, 6.6, 11.7, 13.3, 14.79, 18.4, 19.9, 19.5])
        path_sum = math.fsum(path)
        print(run)
        makespan = [math.fsum(ms1), math.fsum(ms2) + path[0], math.fsum(ms3) + path[1],
                    math.fsum(ms4) + path[2], math.fsum(ms5) + path[3],
                    math.fsum(ms6), math.fsum(ms7) + path[4],
                    math.fsum(ms8) + path[5], math.fsum(ms9) + path[6],
                    math.fsum(ms10) + path[7], math.fsum(ms11),
                    math.fsum(ms12) + path[8], math.fsum(ms13),
                    math.fsum(ms14) + path[9] , math.fsum(ms15), math.fsum(ms16)+path[10]]
        makespan = round(math.fsum(makespan), 2)
        # print('HEFT Makespan is :', makespan)

        makespan_c = [math.fsum(msm1), math.fsum(ms2) + path[0], math.fsum(ms3) + path[1],
                    math.fsum(ms4) + path[2], math.fsum(ms5) + path[3],
                    math.fsum(msm6), math.fsum(ms7) + path[4],
                    math.fsum(ms8) + path[5], math.fsum(ms9) + path[6],
                    math.fsum(ms10) + path[7], math.fsum(ms11),
                    math.fsum(msm12) + path[8], math.fsum(ms13),
                    math.fsum(ms14) + path[9], math.fsum(ms15), math.fsum(ms16) + path[10]]
        makespan_c = round(math.fsum(makespan_c), 2)

    elif len(t) == 17:
        t = np.sort(t)
        msm1 = np.round(t[0] / p[1], 2)
        msm2 = np.round(t[1] / p[1], 2)
        msm3 = np.round(t[2] / p[1], 2)
        msm4 = np.round(t[3] / p[1], 2)
        msm5 = np.round(t[4] / p[1], 2)
        msm6 = np.round(t[5] / p[1], 2)
        msm7 = np.round(t[6] / p[1], 2)
        msm8 = np.round(t[7] / p[1], 2)
        msm9 = np.round(t[8] / p[1], 2)
        msm10 = np.round(t[9] / p[1], 2)
        msm11 = np.round(t[10] / p[1], 2)
        msm12 = np.round(t[11] / p[1], 2)
        msm13 = np.round(t[12] / p[1], 2)
        msm14 = np.round(t[13] / p[1], 2)
        msm15 = np.round(t[14] / p[1], 2)
        msm16 = np.round(t[15] / p[1], 2)
        msm17 = np.round(t[16] / p[1], 2)
        task_min = [math.fsum(msm1), math.fsum(msm2),
                    math.fsum(msm3), math.fsum(msm4), math.fsum(msm5), math.fsum(msm6), math.fsum(msm7)
            , math.fsum(msm8), math.fsum(msm9), math.fsum(msm10), math.fsum(msm11),
                    math.fsum(msm12), math.fsum(msm13), math.fsum(msm14), math.fsum(msm15),
                    math.fsum(msm16), math.fsum(msm17)]
        task_min = math.fsum(task_min)
        print('Tasks on fastest processor :', round(task_min, 2))
        cp_min = [max(msm1), max(msm2), max(msm3), max(msm4), max(msm5),
                  max(msm6), max(msm7), max(msm8), max(msm9),
                  max(msm10), max(msm11), max(msm12),
                  max(msm13), max(msm14), max(msm15), max(msm16), max(msm17)]
        print('critical path on fastest cpu :', cp_min)
        cp_min = max(cp_min)
        print('makespan of cp on fastest cpu :', cp_min)
        blevel = np.amax(t)
        t = np.delete(t, len(t) - 1)
        ms1 = np.round(t[0] / p[0], 2)
        ms2 = np.round(t[1] / p[1], 2)
        ms3 = np.round(t[2] / p[0], 2)
        ms4 = np.round(t[3] / p[2], 2)
        ms5 = np.round(t[4] / p[1], 2)
        ms6 = np.round(t[5] / p[1], 2)
        ms7 = np.round(t[6] / p[0], 2)
        ms8 = np.round(t[7] / p[2], 2)
        ms9 = np.round(t[8] / p[1], 2)
        ms10 = np.round(t[9] / p[0], 2)
        ms11 = np.round(t[10] / p[0], 2)
        ms12 = np.round(t[11] / p[1], 2)
        ms13 = np.round(t[12] / p[1], 2)
        ms14 = np.round(t[13] / p[2], 2)
        ms15 = np.round(t[14] / p[2], 2)
        ms16 = np.round(t[15] / p[2], 2)
        ms17 = np.round(blevel / fastes_processor, 2)
        run = [ms1, ms2, ms3, ms4, ms5, ms6, ms7, ms8
            , ms9, ms10, ms11, ms12, ms13, ms14, ms15,
               ms16, ms17]
        run_c = [ms1, ms2, ms3, ms4, msm5, ms6, ms7, msm8
            , msm9, ms10, ms11, ms12, ms13, ms14, ms15,
               ms16, msm17]

        path = np.array([0.5, 0.1, 1, 1.7, 6.6, 11.7, 13.3, 14.79, 18.4, 19.9, 19.5 ,13.6])
        path_sum = math.fsum(path)
        print(run)
        makespan = [math.fsum(ms1), math.fsum(ms2) + path[0], math.fsum(ms3) + path[1],
                    math.fsum(ms4) + path[2], math.fsum(ms5) + path[3],
                    math.fsum(ms6), math.fsum(ms7) + path[4],
                    math.fsum(ms8) + path[5], math.fsum(ms9) + path[6],
                    math.fsum(ms10) + path[7], math.fsum(ms11),
                    math.fsum(ms12) + path[8], math.fsum(ms13),
                    math.fsum(ms14) + path[9] , math.fsum(ms15),
                    math.fsum(ms16)+path[10] , math.fsum(ms17)+path[11]]
        makespan = round(math.fsum(makespan), 2)
        # print('HEFT Makespan is :', makespan)

        makespan_c = [math.fsum(ms1), math.fsum(msm2) + path[0], math.fsum(ms3) + path[1],
                    math.fsum(ms4) + path[2], math.fsum(msm5) + path[3],
                    math.fsum(ms6), math.fsum(ms7) + path[4],
                    math.fsum(msm8) + path[5], math.fsum(msm9) + path[6],
                    math.fsum(ms10) + path[7], math.fsum(ms11),
                    math.fsum(ms12) + path[8], math.fsum(ms13),
                    math.fsum(ms14) + path[9], math.fsum(ms15),
                    math.fsum(ms16) + path[10], math.fsum(msm17) + path[11]]
        makespan_c = round(math.fsum(makespan_c), 2)

    elif len(t) == 18:
        t = np.sort(t)
        msm1 = np.round(t[0] / p[1], 2)
        msm2 = np.round(t[1] / p[1], 2)
        msm3 = np.round(t[2] / p[1], 2)
        msm4 = np.round(t[3] / p[1], 2)
        msm5 = np.round(t[4] / p[1], 2)
        msm6 = np.round(t[5] / p[1], 2)
        msm7 = np.round(t[6] / p[1], 2)
        msm8 = np.round(t[7] / p[1], 2)
        msm9 = np.round(t[8] / p[1], 2)
        msm10 = np.round(t[9] / p[1], 2)
        msm11 = np.round(t[10] / p[1], 2)
        msm12 = np.round(t[11] / p[1], 2)
        msm13 = np.round(t[12] / p[1], 2)
        msm14 = np.round(t[13] / p[1], 2)
        msm15 = np.round(t[14] / p[1], 2)
        msm16 = np.round(t[15] / p[1], 2)
        msm17 = np.round(t[16] / p[1], 2)
        msm18 = np.round(t[17] / p[1], 2)
        task_min = [math.fsum(msm1), math.fsum(msm2),
                    math.fsum(msm3), math.fsum(msm4), math.fsum(msm5), math.fsum(msm6), math.fsum(msm7)
            , math.fsum(msm8), math.fsum(msm9), math.fsum(msm10), math.fsum(msm11),
                    math.fsum(msm12), math.fsum(msm13), math.fsum(msm14), math.fsum(msm15),
                    math.fsum(msm16), math.fsum(msm17), math.fsum(msm18)]
        task_min = math.fsum(task_min)
        print('Tasks on fastest processor :', round(task_min, 2))
        cp_min = [max(msm1), max(msm2), max(msm3), max(msm4), max(msm5),
                  max(msm6), max(msm7), max(msm8), max(msm9),
                  max(msm10), max(msm11), max(msm12),
                  max(msm13), max(msm14), max(msm15), max(msm16), max(msm17), max(msm18)]
        print('critical path on fastest cpu :', cp_min)
        cp_min = max(cp_min)
        print('makespan of cp on fastest cpu :', cp_min)
        blevel = np.amax(t)
        t = np.delete(t, len(t) - 1)
        ms1 = np.round(t[0] / p[0], 2)
        ms2 = np.round(t[1] / p[1], 2)
        ms3 = np.round(t[2] / p[0], 2)
        ms4 = np.round(t[3] / p[2], 2)
        ms5 = np.round(t[4] / p[1], 2)
        ms6 = np.round(t[5] / p[1], 2)
        ms7 = np.round(t[6] / p[0], 2)
        ms8 = np.round(t[7] / p[2], 2)
        ms9 = np.round(t[8] / p[1], 2)
        ms10 = np.round(t[9] / p[0], 2)
        ms11 = np.round(t[10] / p[0], 2)
        ms12 = np.round(t[11] / p[1], 2)
        ms13 = np.round(t[12] / p[1], 2)
        ms14 = np.round(t[13] / p[2], 2)
        ms15 = np.round(t[14] / p[2], 2)
        ms16 = np.round(t[15] / p[2], 2)
        ms17 = np.round(t[16] / p[1], 2)
        ms18 = np.round(blevel / fastes_processor, 2)
        run = [ms1, ms2, ms3, ms4, ms5, ms6, ms7, ms8
            , ms9, ms10, ms11, ms12, ms13, ms14, ms15,
               ms16, ms17, ms18]
        run_c = [msm1, msm2, ms3, ms4, msm5, ms6, ms7, ms8
            , ms9, ms10, msm11, ms12, ms13, ms14, ms15,
               msm16, ms17, ms18]
        path = np.array([0.5, 0.1, 1, 1.7, 6.6, 11.7, 13.3, 14.79, 18.4, 19.9, 19.5,13.6 , 17.7])
        path_sum = math.fsum(path)
        print(run)
        makespan = [math.fsum(ms1), math.fsum(ms2) + path[0], math.fsum(ms3) + path[1],
                    math.fsum(ms4) + path[2], math.fsum(ms5) + path[3],
                    math.fsum(ms6), math.fsum(ms7) + path[4],
                    math.fsum(ms8) + path[5], math.fsum(ms9) + path[6],
                    math.fsum(ms10) + path[7], math.fsum(ms11),
                    math.fsum(ms12) + path[8], math.fsum(ms13),
                    math.fsum(ms14) + path[9] , math.fsum(ms15),
                    math.fsum(ms16)+path[10] , math.fsum(ms17)+path[11] ,
                    math.fsum(ms18) + path[12]]
        makespan = round(math.fsum(makespan), 2)
        # print('HEFT Makespan is :', makespan)

        makespan_c = [math.fsum(msm1), math.fsum(msm2) + path[0], math.fsum(ms3) + path[1],
                    math.fsum(ms4) + path[2], math.fsum(msm5) + path[3],
                    math.fsum(ms6), math.fsum(ms7) + path[4],
                    math.fsum(ms8) + path[5], math.fsum(ms9) + path[6],
                    math.fsum(ms10) + path[7], math.fsum(msm11),
                    math.fsum(ms12) + path[8], math.fsum(ms13),
                    math.fsum(ms14) + path[9], math.fsum(ms15),
                    math.fsum(msm16) + path[10], math.fsum(ms17) + path[11],
                    math.fsum(ms18) + path[12]]
        makespan_c = round(math.fsum(makespan_c), 2)

    elif len(t) == 19:
        t = np.sort(t)
        msm1 = np.round(t[0] / p[1], 2)
        msm2 = np.round(t[1] / p[1], 2)
        msm3 = np.round(t[2] / p[1], 2)
        msm4 = np.round(t[3] / p[1], 2)
        msm5 = np.round(t[4] / p[1], 2)
        msm6 = np.round(t[5] / p[1], 2)
        msm7 = np.round(t[6] / p[1], 2)
        msm8 = np.round(t[7] / p[1], 2)
        msm9 = np.round(t[8] / p[1], 2)
        msm10 = np.round(t[9] / p[1], 2)
        msm11 = np.round(t[10] / p[1], 2)
        msm12 = np.round(t[11] / p[1], 2)
        msm13 = np.round(t[12] / p[1], 2)
        msm14 = np.round(t[13] / p[1], 2)
        msm15 = np.round(t[14] / p[1], 2)
        msm16 = np.round(t[15] / p[1], 2)
        msm17 = np.round(t[16] / p[1], 2)
        msm18 = np.round(t[17] / p[1], 2)
        msm19 = np.round(t[18] / p[1], 2)
        task_min = [math.fsum(msm1), math.fsum(msm2),
                    math.fsum(msm3), math.fsum(msm4), math.fsum(msm5), math.fsum(msm6), math.fsum(msm7)
            , math.fsum(msm8), math.fsum(msm9), math.fsum(msm10), math.fsum(msm11),
                    math.fsum(msm12), math.fsum(msm13), math.fsum(msm14), math.fsum(msm15),
                    math.fsum(msm16), math.fsum(msm17), math.fsum(msm18), math.fsum(msm19)]
        task_min = math.fsum(task_min)
        print('Tasks on fastest processor :', round(task_min, 2))
        cp_min = [max(msm1), max(msm2), max(msm3), max(msm4), max(msm5),
                  max(msm6), max(msm7), max(msm8), max(msm9),
                  max(msm10), max(msm11), max(msm12),
                  max(msm13), max(msm14), max(msm15), max(msm16), max(msm17), max(msm18), max(msm19)]
        print('critical path on fastest cpu :', cp_min)
        cp_min = max(cp_min)
        print('makespan of cp on fastest cpu :', cp_min)
        blevel = np.amax(t)
        t = np.delete(t, len(t) - 1)
        ms1 = np.round(t[0] / p[0], 2)
        ms2 = np.round(t[1] / p[1], 2)
        ms3 = np.round(t[2] / p[0], 2)
        ms4 = np.round(t[3] / p[2], 2)
        ms5 = np.round(t[4] / p[1], 2)
        ms6 = np.round(t[5] / p[1], 2)
        ms7 = np.round(t[6] / p[0], 2)
        ms8 = np.round(t[7] / p[2], 2)
        ms9 = np.round(t[8] / p[1], 2)
        ms10 = np.round(t[9] / p[0], 2)
        ms11 = np.round(t[10] / p[0], 2)
        ms12 = np.round(t[11] / p[1], 2)
        ms13 = np.round(t[12] / p[1], 2)
        ms14 = np.round(t[13] / p[2], 2)
        ms15 = np.round(t[14] / p[2], 2)
        ms16 = np.round(t[15] / p[2], 2)
        ms17 = np.round(t[16] / p[1], 2)
        ms18 = np.round(t[17] / p[0], 2)
        ms19 = np.round(blevel / fastes_processor, 2)
        run = [ms1, ms2, ms3 , ms4 ,ms5 ,ms6 ,ms7 ,ms8
            ,ms9 ,ms10 ,ms11 ,ms12 ,ms13 ,ms14,ms15 ,
               ms16 , ms17 ,ms18 ,ms19]
        run_c = [ms1, msm2, ms3, ms4, ms5, ms6, msm7, ms8
            , ms9, ms10, ms11, ms12, ms13, ms14, ms15,
               ms16, ms17, msm18, ms19]

        path = np.array([0.5, 0.1, 1, 1.7, 6.6, 11.7, 13.3, 14.79, 18.4, 19.9, 19.5, 13.6, 17.7])
        path_sum = math.fsum(path)
        print(run)
        makespan = [math.fsum(ms1), math.fsum(ms2) + path[0], math.fsum(ms3) + path[1],
                    math.fsum(ms4) + path[2], math.fsum(ms5) + path[3],
                    math.fsum(ms6), math.fsum(ms7) + path[4],
                    math.fsum(ms8) + path[5], math.fsum(ms9) + path[6],
                    math.fsum(ms10) + path[7], math.fsum(ms11),
                    math.fsum(ms12) + path[8], math.fsum(ms13),
                    math.fsum(ms14) + path[9], math.fsum(ms15),
                    math.fsum(ms16) + path[10], math.fsum(ms17) + path[11],
                    math.fsum(ms18) + path[12] , math.fsum(ms19)]
        makespan = round(math.fsum(makespan), 2)
        # print('HEFT Makespan is :', makespan)

        makespan_c = [math.fsum(ms1), math.fsum(msm2) + path[0], math.fsum(ms3) + path[1],
                    math.fsum(ms4) + path[2], math.fsum(ms5) + path[3],
                    math.fsum(ms6), math.fsum(msm7) + path[4],
                    math.fsum(ms8) + path[5], math.fsum(ms9) + path[6],
                    math.fsum(ms10) + path[7], math.fsum(ms11),
                    math.fsum(ms12) + path[8], math.fsum(ms13),
                    math.fsum(ms14) + path[9], math.fsum(ms15),
                    math.fsum(ms16) + path[10], math.fsum(ms17) + path[11],
                    math.fsum(msm18) + path[12], math.fsum(ms19)]
        makespan_c = round(math.fsum(makespan_c), 2)

    file_name11 = 'C:/Users/Naweed/PycharmProjects/IHHO/HEFT Metrics/HEFT SLR.txt'
    file_name12 = 'C:/Users/Naweed/PycharmProjects/IHHO/HEFT Metrics/HEFT Speed up.txt'
    file_name13 = 'C:/Users/Naweed/PycharmProjects/IHHO/HEFT Metrics/HEFT Efficiency.txt'
    file_name14 = 'C:/Users/Naweed/PycharmProjects/IHHO/HEFT Metrics/HEFT CCR.txt'
    file_name15 = 'C:/Users/Naweed/PycharmProjects/IHHO/HEFT Metrics/HEFT Makespan.txt'
    file_name6 = 'C:/Users/Naweed/PycharmProjects/IHHO/HEFT Metrics/CPOP Makespan.txt'
    file_name7 = 'C:/Users/Naweed/PycharmProjects/IHHO/HEFT Metrics/CPOP Efficiency.txt'
    file_name8 = 'C:/Users/Naweed/PycharmProjects/IHHO/HEFT Metrics/CPOP CCR.txt'
    file_name9 = 'C:/Users/Naweed/PycharmProjects/IHHO/HEFT Metrics/CPOP Speed up.txt'
    file_name10 = 'C:/Users/Naweed/PycharmProjects/IHHO/HEFT Metrics/CPOP SLR.txt'

    cpu_len = len(p)

    print('HEFT Makespan is :', makespan_c)
    SLR_c = round(makespan_c / cp_min, 2)
    print('-> SLR is :', SLR_c)

    Speedup_c = round(task_min / makespan_c, 2)
    print('-> Speed up is :', Speedup_c)

    Efficiency_c = round(Speedup_c / cpu_len, 2)
    print('-> Efficiency is :', Efficiency_c)
    print('running on CPUS :', run_c)

    CCR_c = round(path_sum / makespan_c, 1)
    print('CCR :', CCR_c)

    print('\n------------- CPOP Metrics ---------------')

    print('CPOP makespan is :', makespan)

    SLR = round(makespan / cp_min, 2)
    print('-> SLR is :', SLR)

    Speedup = round(task_min / makespan, 2)
    print('-> Speed up is :', Speedup)

    Efficiency = round(Speedup / cpu_len, 2)
    print('-> Efficiency is :', Efficiency)
    print('running on CPUS :', run)

    CCR = round(path_sum / makespan, 1)
    print('CCR :', CCR)

    with open(file_name15, 'a') as f:
        f.write(str(makespan_c))
        f.write(',')
    with open(file_name6, 'a') as f:
        f.write(str(makespan))
        f.write(',')
    with open(file_name11, 'a') as f:
        f.write(str(SLR_c))
        f.write(',')
    with open(file_name10, 'a') as f:
        f.write(str(SLR))
        f.write(',')
    with open(file_name12, 'a') as f:
        f.write(str(Speedup_c))
        f.write(',')
    with open(file_name9, 'a') as f:
        f.write(str(Speedup))
        f.write(',')
    with open(file_name14, 'a') as f:
        f.write(str(CCR_c))
        f.write(',')
    with open(file_name8, 'a') as f:
        f.write(str(CCR))
        f.write(',')
    with open(file_name13, 'a') as f:
        f.write(str(Efficiency_c))
        f.write(',')
    with open(file_name7, 'a') as f:
        f.write(str(Efficiency))
        f.write(',')

def Dataset():

    file_name = 'C:/Users/Naweed/PycharmProjects/IHHO/Metrics/Makespan data set.txt'
    file_name2 = 'C:/Users/Naweed/PycharmProjects/IHHO/Metrics/SLR data set.txt'
    file_name3 = 'C:/Users/Naweed/PycharmProjects/IHHO/Metrics/Speed up data set.txt'
    file_name4 = 'C:/Users/Naweed/PycharmProjects/IHHO/Metrics/CCR data set.txt'
    file_name5 = 'C:/Users/Naweed/PycharmProjects/IHHO/Metrics/Efficiency data set.txt'
    file_name11 = 'C:/Users/Naweed/PycharmProjects/IHHO/HEFT Metrics/HEFT SLR.txt'
    file_name12 = 'C:/Users/Naweed/PycharmProjects/IHHO/HEFT Metrics/HEFT Speed up.txt'
    file_name13 = 'C:/Users/Naweed/PycharmProjects/IHHO/HEFT Metrics/HEFT Efficiency.txt'
    file_name14 = 'C:/Users/Naweed/PycharmProjects/IHHO/HEFT Metrics/HEFT CCR.txt'
    file_name15 = 'C:/Users/Naweed/PycharmProjects/IHHO/HEFT Metrics/HEFT Makespan.txt'
    file_name6 = 'C:/Users/Naweed/PycharmProjects/IHHO/HEFT Metrics/CPOP Makespan.txt'
    file_name7 = 'C:/Users/Naweed/PycharmProjects/IHHO/HEFT Metrics/CPOP Efficiency.txt'
    file_name8 = 'C:/Users/Naweed/PycharmProjects/IHHO/HEFT Metrics/CPOP CCR.txt'
    file_name9 = 'C:/Users/Naweed/PycharmProjects/IHHO/HEFT Metrics/CPOP Speed up.txt'
    file_name10 = 'C:/Users/Naweed/PycharmProjects/IHHO/HEFT Metrics/CPOP SLR.txt'
    file_name16 = 'C:/Users/Naweed/PycharmProjects/IHHO/Metrics +/Makespan data set.txt'
    file_name17 = 'C:/Users/Naweed/PycharmProjects/IHHO/Metrics +/Efficiency data set.txt'
    file_name18 = 'C:/Users/Naweed/PycharmProjects/IHHO/Metrics +/CCR data set.txt'
    file_name19 = 'C:/Users/Naweed/PycharmProjects/IHHO/Metrics +/Speed up data set.txt'
    file_name20 = 'C:/Users/Naweed/PycharmProjects/IHHO/Metrics +/SLR data set.txt'
    file_name21 = 'C:/Users/Naweed/PycharmProjects/IHHO/Metrics Cuckoo/Makespan data set.txt'
    file_name22 = 'C:/Users/Naweed/PycharmProjects/IHHO/Metrics Cuckoo/SLR data set.txt'
    file_name23 = 'C:/Users/Naweed/PycharmProjects/IHHO/Metrics Cuckoo/Speed up data set.txt'
    file_name24 = 'C:/Users/Naweed/PycharmProjects/IHHO/Metrics Cuckoo/CCR data set.txt'
    file_name25 = 'C:/Users/Naweed/PycharmProjects/IHHO/Metrics Cuckoo/Efficiency data set.txt'
    file_name26 = 'C:/Users/Naweed/PycharmProjects/IHHO/Genetic/Makespan data set.txt'
    file_name27 = 'C:/Users/Naweed/PycharmProjects/IHHO/Genetic/SLR data set.txt'
    file_name28 = 'C:/Users/Naweed/PycharmProjects/IHHO/Genetic/Speed up data set.txt'
    file_name29 = 'C:/Users/Naweed/PycharmProjects/IHHO/Genetic/CCR data set.txt'
    file_name30 = 'C:/Users/Naweed/PycharmProjects/IHHO/Genetic/Efficiency data set.txt'
    file_name31 = 'C:/Users/Naweed/PycharmProjects/IHHO/Cuckoo Genetic/Cuckoo Genetic Makespan.txt'
    file_name32 = 'C:/Users/Naweed/PycharmProjects/IHHO/Cuckoo Genetic/Cuckoo Genetic SLR.txt'
    file_name33 = 'C:/Users/Naweed/PycharmProjects/IHHO/Cuckoo Genetic/Cuckoo Genetic Speed up.txt'
    file_name34 = 'C:/Users/Naweed/PycharmProjects/IHHO/Cuckoo Genetic/Cuckoo Genetic CCR.txt'
    file_name35 = 'C:/Users/Naweed/PycharmProjects/IHHO/Cuckoo Genetic/Cuckoo Genetic Efficiency.txt'

    try :
        print('----- HHO Metrics -----')
        with open (file_name,'r') as f:
            print('makespans :','[',f.read(),']')

        with open (file_name4,'r') as f:
            print('CCR :','[',f.read(),']')

        with open (file_name5,'r') as f:
            print('Efficiency :','[',f.read(),']')

        with open (file_name3,'r') as f:
            print('Speed up :','[',f.read(),']')

        with open (file_name2,'r') as f:
            print('SLR :','[',f.read(),']')

        print('----- IHHO Metrics -----')

        with open(file_name16, 'r') as f:
            print('makespans :', '[', f.read(), ']')

        with open(file_name18, 'r') as f:
            print('CCR :', '[', f.read(), ']')

        with open(file_name17, 'r') as f:
            print('Efficiency :', '[', f.read(), ']')

        with open(file_name19, 'r') as f:
            print('Speed up :', '[', f.read(), ']')

        with open(file_name20, 'r') as f:
            print('SLR :', '[', f.read(), ']')

        print('----- HEFT Metrics ------')

        with open(file_name15, 'r') as f:
            print('Makespan :', '[', f.read(), ']')

        with open(file_name11, 'r') as f:
            print('SLR :', '[', f.read(), ']')

        with open(file_name14, 'r') as f:
            print('CCR :', '[', f.read(), ']')

        with open(file_name13, 'r') as f:
            print('Efficiency :', '[', f.read(), ']')

        with open(file_name12, 'r') as f:
            print('Speed up :', '[', f.read(), ']')

        with open(file_name11, 'r') as f:
            print('SLR :', '[', f.read(), ']')

        print('----- CPOP Metrics -----')

        with open(file_name6, 'r') as f:
            print('makespans :', '[', f.read(), ']')

        with open(file_name8, 'r') as f:
            print('CCR :', '[', f.read(), ']')

        with open(file_name7, 'r') as f:
            print('Efficiency :', '[', f.read(), ']')

        with open(file_name9, 'r') as f:
            print('Speed up :', '[', f.read(), ']')

        with open(file_name10, 'r') as f:
            print('SLR :', '[', f.read(), ']')


        print('----- Cuckoo Metrics ------')

        with open(file_name21, 'r') as f:
            print('makespans :', '[', f.read(), ']')

        with open(file_name22, 'r') as f:
            print('SLR :', '[', f.read(), ']')

        with open (file_name23,'r') as f:
            print('Speed up :','[',f.read(),']')

        with open(file_name24, 'r') as f:
            print('CCR :', '[', f.read(), ']')

        with open(file_name25, 'r') as f:
            print('Efficiency :', '[', f.read(), ']')

        print('----- Genetic Metrics ------')

        with open(file_name26, 'r') as f:
            print('makespans :', '[', f.read(), ']')

        with open(file_name27, 'r') as f:
            print('SLR :', '[', f.read(), ']')

        with open(file_name28, 'r') as f:
            print('Speed up :', '[', f.read(), ']')

        with open(file_name29, 'r') as f:
            print('CCR :', '[', f.read(), ']')

        with open(file_name30, 'r') as f:
            print('Efficiency :', '[', f.read(), ']')

        print('----- Cuckoo Genetic Metrics ------')

        with open(file_name31, 'r') as f:
            print('makespans :', '[', f.read(), ']')

        with open(file_name32, 'r') as f:
            print('SLR :', '[', f.read(), ']')

        with open(file_name33, 'r') as f:
            print('Speed up :', '[', f.read(), ']')

        with open(file_name34, 'r') as f:
            print('CCR :', '[', f.read(), ']')

        with open(file_name35, 'r') as f:
            print('Efficiency :', '[', f.read(), ']')

    except (FileNotFoundError) :
        print('*****************************************')
        print('*          You must Generate :          *')
        print('*       HHO | IHHO | HEFT | CPOP |      *')
        print('*   Genetic | Cuckoo | Cuckoo Genetic   *')
        print('* All Solutions must be generated first *')
        print('*****************************************')

def Reset ():
    try:
        print('         \nClearing Database ', end='')
        time.sleep(0.5)
        print('.', end='')
        time.sleep(0.5)
        print('.', end='')
        time.sleep(0.5)
        print('.')
        ff = 'C:/Users/Naweed/PycharmProjects/IHHO/Graphs/Gaussian graph.txt'
        fq = 'C:/Users/Naweed/PycharmProjects/IHHO/Graphs/FFT graph.txt'
        fm = 'C:/Users/Naweed/PycharmProjects/IHHO/Graphs/Molecular graph.txt'
        file_name = 'C:/Users/Naweed/PycharmProjects/IHHO/Metrics/Makespan data set.txt'
        file_name2 = 'C:/Users/Naweed/PycharmProjects/IHHO/Metrics/SLR data set.txt'
        file_name3 = 'C:/Users/Naweed/PycharmProjects/IHHO/Metrics/Speed up data set.txt'
        file_name4 = 'C:/Users/Naweed/PycharmProjects/IHHO/Metrics/CCR data set.txt'
        file_name5 = 'C:/Users/Naweed/PycharmProjects/IHHO/Metrics/Efficiency data set.txt'
        file_name11 = 'C:/Users/Naweed/PycharmProjects/IHHO/HEFT Metrics/HEFT SLR.txt'
        file_name12 = 'C:/Users/Naweed/PycharmProjects/IHHO/HEFT Metrics/HEFT Speed up.txt'
        file_name13 = 'C:/Users/Naweed/PycharmProjects/IHHO/HEFT Metrics/HEFT Efficiency.txt'
        file_name14 = 'C:/Users/Naweed/PycharmProjects/IHHO/HEFT Metrics/HEFT CCR.txt'
        file_name15 = 'C:/Users/Naweed/PycharmProjects/IHHO/HEFT Metrics/HEFT Makespan.txt'
        file_name6 = 'C:/Users/Naweed/PycharmProjects/IHHO/HEFT Metrics/CPOP Makespan.txt'
        file_name7 = 'C:/Users/Naweed/PycharmProjects/IHHO/HEFT Metrics/CPOP Efficiency.txt'
        file_name8 = 'C:/Users/Naweed/PycharmProjects/IHHO/HEFT Metrics/CPOP CCR.txt'
        file_name9 = 'C:/Users/Naweed/PycharmProjects/IHHO/HEFT Metrics/CPOP Speed up.txt'
        file_name10 = 'C:/Users/Naweed/PycharmProjects/IHHO/HEFT Metrics/CPOP SLR.txt'
        file_name16 = 'C:/Users/Naweed/PycharmProjects/IHHO/Metrics +/Makespan data set.txt'
        file_name17 = 'C:/Users/Naweed/PycharmProjects/IHHO/Metrics +/Efficiency data set.txt'
        file_name18 = 'C:/Users/Naweed/PycharmProjects/IHHO/Metrics +/CCR data set.txt'
        file_name19 = 'C:/Users/Naweed/PycharmProjects/IHHO/Metrics +/Speed up data set.txt'
        file_name20 = 'C:/Users/Naweed/PycharmProjects/IHHO/Metrics +/SLR data set.txt'
        file_name21 = 'C:/Users/Naweed/PycharmProjects/IHHO/Metrics Cuckoo/Makespan data set.txt'
        file_name22 = 'C:/Users/Naweed/PycharmProjects/IHHO/Metrics Cuckoo/SLR data set.txt'
        file_name23 = 'C:/Users/Naweed/PycharmProjects/IHHO/Metrics Cuckoo/Speed up data set.txt'
        file_name24 = 'C:/Users/Naweed/PycharmProjects/IHHO/Metrics Cuckoo/CCR data set.txt'
        file_name25 = 'C:/Users/Naweed/PycharmProjects/IHHO/Metrics Cuckoo/Efficiency data set.txt'
        file_name26 = 'C:/Users/Naweed/PycharmProjects/IHHO/Genetic/Makespan data set.txt'
        file_name27 = 'C:/Users/Naweed/PycharmProjects/IHHO/Genetic/SLR data set.txt'
        file_name28 = 'C:/Users/Naweed/PycharmProjects/IHHO/Genetic/Speed up data set.txt'
        file_name29 = 'C:/Users/Naweed/PycharmProjects/IHHO/Genetic/CCR data set.txt'
        file_name30 = 'C:/Users/Naweed/PycharmProjects/IHHO/Genetic/Efficiency data set.txt'
        file_name31 = 'C:/Users/Naweed/PycharmProjects/IHHO/Cuckoo Genetic/Cuckoo Genetic Makespan.txt'
        file_name32 = 'C:/Users/Naweed/PycharmProjects/IHHO/Cuckoo Genetic/Cuckoo Genetic SLR.txt'
        file_name33 = 'C:/Users/Naweed/PycharmProjects/IHHO/Cuckoo Genetic/Cuckoo Genetic Speed up.txt'
        file_name34 = 'C:/Users/Naweed/PycharmProjects/IHHO/Cuckoo Genetic/Cuckoo Genetic CCR.txt'
        file_name35 = 'C:/Users/Naweed/PycharmProjects/IHHO/Cuckoo Genetic/Cuckoo Genetic Efficiency.txt'
        fn2 = 'C:/Users/Naweed/PycharmProjects/IHHO/Cuckoo Genetic/Cuckoo Genetic.txt'
        fn = 'C:/Users/Naweed/PycharmProjects/IHHO/Genetic/Genetic Solutions.txt'
        file_path2 = 'C:/Users/Naweed/PycharmProjects/IHHO/HHO Solution/IHHO Solution.txt'
        file_path = 'C:/Users/Naweed/PycharmProjects/IHHO/HHO Solution/HHO Solution.txt'
        file_path3 = 'C:/Users/Naweed/PycharmProjects/IHHO/Cuckoo/Cuckoo Solutions.txt'
        file = 'C:/Users/Naweed/PycharmProjects/IHHO/Cuckoo/Cuckoo popualation.txt'
        file_n = 'C:/Users/Naweed/PycharmProjects/IHHO/Initial population/list of initial population.txt'

        Dataset_list = [file_name,file_name2,file_name3,file_name4,file_name5,file_name6,
                        file_name7,file_name8,file_name9,file_name10,file_name11,file_name12,file_name13,
                        file_name14,file_name15,file_name16,file_name17,file_name18,file_name19,file_name20,
                        file_name21,file_name22,file_name23,file_name24,file_name25,file_name26,file_name27,
                        file_name28,file_name29,file_name30,file_name31,file_name32,file_name33,file_name34,
                        file_name35,fn,fn2,file_path,file_path2,file_path3,file,file_n,fm,ff,fq]

        for files in Dataset_list :
            os.remove(files)
        time.sleep(0.25)
        print('           \n% 1', end='')
        time.sleep(1)
        print('0', end='')
        time.sleep(2)
        print('0')
        print('\n            Done !')
    except (FileNotFoundError) :
        print('**********************************')
        print('*  Database still has free space *')
        print('*       No need to clear it !    *')
        print('**********************************')

def Histogram(a,b,c,d,e,f,g) :
    # a = input('HHO Metrics :')
    # b = input('CPOP Metrics :')
    # c = input('HEFT Metrics :')
    a = np.sort(np.array(a))
    # a = a[::-1]
    b = np.sort(np.array(b))
    # b = b[::-1]
    c = np.sort(np.array(c))
    # c = c[::-1]
    d = np.sort(np.array(d))
    # d = d[::-1]
    e = np.sort(np.array(e))
    # e = e[::-1]
    f = np.sort(np.array(f))
    # f = f[::-1]
    g = np.sort(np.array(g))
    # g = g[::-1]
    num = 1
    if len(a) == 1:
        labels = [num]

    elif len(a) == 2:
        labels = [num, num+6]

    elif len (a) == 3 :
        labels = [num, num+6, num+6+6]

    elif len (a ) == 4 :
        labels = [num, num+2, num+2+2+2, 16]

    # elif len(a ) == 5:
    #     labels = [num, num+2,num*8,
    #               num*16 , num*32]

    # elif len(a ) == 5:
    #     labels = [10, 20,50,
    #               100 , 200]

    elif len(a) == 5:
        labels = [0.1, 0.5, 5,
                  10, 15]

    elif len(a ) == 6:
        labels = [num, num+2, num+2+2+2, num*8,
                  num*16 , num*32]

    elif len(a) == 7:
        labels = [num, num+6, num+6+6, num+6+6+6+6, num+6+6+6+6+6, num+6+6+6+6+6+6, num+6+6+6+6+6+6+6]

    elif len(a) == 8:
        labels = [num, num+6, num+6+6, num+6+6+6+6,
                  num+6+6+6+6+6, num+6+6+6+6+6+6, num+6+6+6+6+6+6+6, num+6+6+6+6+6+6+6+6]

    elif len(a) == 9:
        labels = [num, num+6, num+6+6, num+6+6+6+6,
                  num+6+6+6+6+6, num+6+6+6+6+6+6, num+6+6+6+6+6+6+6,
                  num+6+6+6+6+6+6+6+6, num+6+6+6+6+6+6+6+6+6]

    elif len(a) == 10:
        labels = [num, num+6, num+6+6, num+6+6+6+6,
                  num+6+6+6+6+6, num+6+6+6+6+6+6, num+6+6+6+6+6+6+6,
                  num+6+6+6+6+6+6+6+6, num+6+6+6+6+6+6+6+6+6, num+6+6+6+6+6+6+6+6+6+6]

    elif len(a) == 11:
        labels = [num, num+6, num+6+6, num+6+6+6+6,
                  num+6+6+6+6+6, num+6+6+6+6+6+6, num+6+6+6+6+6+6+6,
                  num+6+6+6+6+6+6+6+6, num+6+6+6+6+6+6+6+6+6,
                  num+6+6+6+6+6+6+6+6+6+6, num+6+6+6+6+6+6+6+6+6+6+6]

    elif len(a) == 12:
        labels = [num, num+6, num+6+6, num+6+6+6+6,
                  num+6+6+6+6+6, num+6+6+6+6+6+6, num+6+6+6+6+6+6+6,
                  num+6+6+6+6+6+6+6+6, num+6+6+6+6+6+6+6+6+6,
                  num+6+6+6+6+6+6+6+6+6+6, num+6+6+6+6+6+6+6+6+6+6+6, num+6+6+6+6+6+6+6+6+6+6+6+6,
                  num + 6 + 6 + 6 + 6 + 6 + 6 + 6 + 6 + 6 + 6 + 6 + 6+6 ,num + 6 + 6 + 6 + 6 + 6 + 6 + 6 + 6 + 6 + 6 + 6 + 6+6+6
                  ,num + 6 + 6 + 6 + 6 + 6 + 6 + 6 + 6 + 6 + 6 + 6 + 6+6+6+6]

    elif len(a) == 13:
        labels = [num, num+6, num+6+6, num+6+6+6+6,
                  num+6+6+6+6+6, num+6+6+6+6+6+6, num+6+6+6+6+6+6+6,
                  num+6+6+6+6+6+6+6+6, num+6+6+6+6+6+6+6+6+6,
                  num+6+6+6+6+6+6+6+6+6+6, num+6+6+6+6+6+6+6+6+6+6+6, num+6+6+6+6+6+6+6+6+6+6+6+6,
                  num + 6 + 6 + 6 + 6 + 6 + 6 + 6 + 6 + 6 + 6 + 6 + 6+6 ]

    elif len(a) == 14:
        labels = [num, num+6, num+6+6, num+6+6+6+6,
                  num+6+6+6+6+6, num+6+6+6+6+6+6, num+6+6+6+6+6+6+6,
                  num+6+6+6+6+6+6+6+6, num+6+6+6+6+6+6+6+6+6,
                  num+6+6+6+6+6+6+6+6+6+6, num+6+6+6+6+6+6+6+6+6+6+6, num+6+6+6+6+6+6+6+6+6+6+6+6,
                  num + 6 + 6 + 6 + 6 + 6 + 6 + 6 + 6 + 6 + 6 + 6 + 6+6 ,num + 6 + 6 + 6 + 6 + 6 + 6 + 6 + 6 + 6 + 6 + 6 + 6+6+6 ]

    elif len(a) == 15:
        labels = [num, num+2, num+2+2, num+2+2+2,
                  num+2+2+2+2]

    elif len(a) == 16:
        labels = [num, num+6, num+6+6, num+6+6+6+6,
                  num+6+6+6+6+6, num+6+6+6+6+6+6, num+6+6+6+6+6+6+6,
                  num+6+6+6+6+6+6+6+6, num+6+6+6+6+6+6+6+6+6,
                  num+6+6+6+6+6+6+6+6+6+6, num+6+6+6+6+6+6+6+6+6+6+6, num+6+6+6+6+6+6+6+6+6+6+6+6,
                  num + 6 + 6 + 6 + 6 + 6 + 6 + 6 + 6 + 6 + 6 + 6 + 6+6 ,num + 6 + 6 + 6 + 6 + 6 + 6 + 6 + 6 + 6 + 6 + 6 + 6+6+6
                  ,num + 6 + 6 + 6 + 6 + 6 + 6 + 6 + 6 + 6 + 6 + 6 + 6+6+6+6
                  ,num + 6 + 6 + 6 + 6 + 6 + 6 + 6 + 6 + 6 + 6 + 6 + 6+6+6+6+6]

    elif len(a) == 17:
        labels = ['run1', 'run2', 'run3', 'run4', 'run5', 'run6',
                  'run7', 'run8', 'run9', 'run10', 'run11',
                  'run12', 'run13', 'run14', 'run15', 'run16', 'run17']

    elif len(a) == 18:
        labels = ['run1', 'run2', 'run3', 'run4', 'run5', 'run6',
                  'run7', 'run8', 'run9', 'run10', 'run11',
                  'run12', 'run13', 'run14', 'run15',
                  'run16', 'run17', 'run18']

    elif len(a) == 19:
        labels = ['run1', 'run2', 'run3', 'run4', 'run5', 'run6',
                  'run7', 'run8', 'run9', 'run10', 'run11',
                  'run12', 'run13', 'run14', 'run15',
                  'run16', 'run17', 'run18', 'run19']

    HHO = a
    IHHO = b
    CPOP = c
    HEFT = d
    Cuckoo = e
    Genetic = f
    Cuckoo_genetic = g

    x = np.arange(len(labels))
    width = 0.15
    fig, ax = plt.subplots()
    rects1 = ax.bar(x + 0.4/ 1, HHO, width, label='HHO')
    rects2 = ax.bar(x + 0.5/ 1, IHHO, width, label='IHHO')
    rects3 = ax.bar(x + 0.10 / 1, HEFT, width, label='HEFT')
    rects4 = ax.bar(x - 0.10 / 2, CPOP, width, label='CPOP')
    rects5 = ax.bar(x + 0.25 / 1, Cuckoo, width, label='MOSCOA')
    rects6 = ax.bar(x - 0.30 / 2, Genetic, width, label='Genetic')
    rects7 = ax.bar(x - 0.56 / 2, Cuckoo_genetic, width, label='HACG-TS')

    ax.set_ylabel('Average Makespan')
    ax.set_title('Number Of Generations')
    ax.set_xticks(x, labels)
    ax.legend(loc='upper left')

    # ax.bar_label(rects1, padding=3)
    # ax.bar_label(rects2, padding=5)
    # ax.bar_label(rects3, padding=3)
    # ax.bar_label(rects4, padding=5)
    # ax.bar_label(rects5, padding=20)
    # ax.bar_label(rects6, padding=3)
    # ax.bar_label(rects7, padding=1)

    fig.tight_layout()

    plt.show()


