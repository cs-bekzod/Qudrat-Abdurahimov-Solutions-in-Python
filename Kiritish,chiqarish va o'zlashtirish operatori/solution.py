'''**************************************************************************************
    |   Author: Bekzod Abdukhalilov                              |
    |   Language: Python                                         |
    |   Sana: 03.31.2021                                         |
    |   Murojat va Takliflar uchun (Telegram account): @userr9   |
**************************************************************************************'''

'''***********************************************************
    **************************************************
    *      Kiritish va Chiqarish (40 exercises)      *
    **************************************************
***********************************************************'''
######################## 1-misol ############################
# a = float(input('a ni kiriting:'))
# P = 4 * a
# print('Result:',P)
######################## 2-misol ############################
# a = float(input('a ni kiriting:'))
# S = a ** 2
# print('Result:',S)
######################## 3-misol ############################
# a = float(input('a ni kiriting:'))
# b = float(input('b ni kiriting:'))
# S = a * b
# P = 2 * (a + b)
# print('Yuzasi:',S)
# print('Perimetri:',P)
######################## 4-misol ############################
# import math
# d = float(input('d ni kiriting:'))
# L = d * math.pi
# print('Uzunlik:',L)
######################## 5-misol ############################ 
# a = float(input('a ni kiriting:'))
# V = a ** 3
# S = 6 * (a ** 2)
# print('Hajmi:',V)
# print('To`la sirti:',S)
######################## 6-misol ############################
# a = float(input('a ni kiriting:'))
# b = float(input('b ni kiriting:'))
# c = float(input('c ni kiriting:'))
# V = a * b * c
# S = 2 * (a * b + a * c + b * c)
# print('Hajmi:',V)
# print('To`la sirti:',S)
######################## 7-misol ############################
# import math
# R = float(input('R ni kiriting:'))
# L = 2 * math.pi * R
# S = math.pi * ( R ** 2)
# print('Uzunligi:',L)
# print('Yuzasi:',S)
######################## 8-misol ############################
# a = float(input('a ni kiriting:'))
# b = float(input('b ni kiriting:'))
# result = (a + b) / 2
# print('O`rta arifmetik:',result)
######################## 9-misol ############################
# a = float(input('a ni kiriting:'))
# b = float(input('b ni kiriting:'))
# result = (a * b) ** 0.5
# print('O`rta geometrik:',result)
######################## 10-misol ###########################
# a = float(input('a ni kiriting:'))
# b = float(input('b ni kiriting:'))
# summ = a + b
# multiplication = a * b
# squareA = a ** 2
# squareB = b ** 2

# result = f'''Yeg'indisi:{summ}
# Ko'paytmasi:{multiplication}
# a ning kvadrati:{squareA}
# b ning kvadrati:{squareB}'''

# print(result)
######################## 11-misol ###########################
# a = float(input('a ni kiriting:'))
# b = float(input('b ni kiriting:'))
# summ = a + b
# multiplication = a * b
# modul_a = abs(a) #Izoh: abs() funksiyasi berilgan sonni musbat qiymatga aylantiradi.abs(-3) = 3, abs(-10.3) = 10.3 ......
# modul_b = abs(b)

# result = f'''Yeg'indisi:{summ}
# Ko'paytmasi:{multiplication}
# a ning moduli:{modul_a}
# b ning moduli:{modul_b}'''

# print(result)
######################## 12-misol ###########################
# a = float(input('a ni kiriting:'))
# b = float(input('b ni kiriting:'))
# c = ((a ** 2) + (b ** 2)) ** 0.5
# P = a + b + c
# print('Gipotenuzasi:',c)
# print('Perimetri:',P)
######################## 13-misol ###########################
# import math
# # Izoh:(R1 > R2) shart bajarilishi kerak!
# R1 = float(input('R1 ni kiriting:')) 
# R2 = float(input('R2 ni kiriting:'))
# S1 , S2 = math.pi * R1 , math.pi * R2
# S3 = math.pi * (R1 - R2)
# print(f'S1:{S1} \nS2:{S2} \nS3:{S3}')
######################## 14-misol ###########################
# import math
# L = float(input('L ni kiriting:'))
# R = L / ( 2 * math.pi)
# S = math.pi * (R ** 2)
# print(f'Radiusi:{R} \nYuzasi:{S}')
######################## 15-misol ###########################
# import math
# S = float(input('S ni kiriting:'))
# R = (S / math.pi) ** 0.5
# d = R / 2 # Izoh: diametr radiusning yarmiga teng.
# print(f'Diametri:{d} \nRadiusi:{R}')
######################## 16-misol ###########################
# a = float(input('x1 ni kiriting:'))
# b = float(input('x2 ni kiriting:'))
# result = abs(a - b)
# print('x1 va x2 orasidagi masofa:',result)
######################## 17-misol ###########################
# a = float(input('A ni kiriting:'))
# b = float(input('B ni kiriting:'))
# c = float(input('C ni kiriting:'))
# AC , BC = abs(a - c) , abs(b - c)
# summ = AC + BC
# print('AC kesma uzunligi:',AC)
# print('BC kesma uzunligi:',BC)
# print('AC va BC kesma uzunliklari yeg`indisi:',summ)
######################## 18-misol ###########################
# a = float(input('A ni kiriting:'))
# b = float(input('B ni kiriting:'))
# c = float(input('C ni kiriting:'))
# multiplication = abs(a - c) * abs(b - c)
# print('AC va BC kesmalar uzunliklari ko`paytmasi:',multiplication)
######################## 19-misol ###########################
# '''         (a,b)__________________(c,b)             
#                 |                  |             IZOH: (a < c) va (e < b) shart bajarilishi kerak.
#                 |                  |                   Agar ushbu shart bajarilmasa natija xato chiqadi.
#            (a,e)|__________________|(c,e)
# '''
# a = float(input('a ni kiriting:'))
# b = float(input('b ni kiriting:'))
# c = float(input('c ni kiriting:'))
# e = float(input('e ni kiriting:'))
# perimetr = 2 * ((b - e) + (c - a))
# yuzasi = (b - e) * (c - a)
# print(f'Perimetri:{perimetr} \nYuzasi:{yuzasi}')
######################## 20-misol ###########################
# x1 = float(input('x1 ni kiriting:'))
# x2 = float(input('x2 ni kiriting:'))
# y1 = float(input('y1 ni kiriting:'))
# y2 = float(input('y2 ni kiriting:'))
# result = ((x2 -x1) ** 2 + (y2 - y1) ** 2) ** 0.5
######################## 21-misol ###########################
# x1 = float(input('x1 ni kiriting:'))
# y1 = float(input('y1 ni kiriting:'))
# x2 = float(input('x2 ni kiriting:'))
# y2 = float(input('y2 ni kiriting:'))
# x3 = float(input('x3 ni kiriting:'))
# y3 = float(input('y3 ni kiriting:'))
# a = ((x2 -x1) ** 2 + (y2 - y1) ** 2) ** 0.5
# b = ((x3 -x1) ** 2 + (y3 - y1) ** 2) ** 0.5
# c = ((x2 -x3) ** 2 + (y2 - y3) ** 2) ** 0.5
# p = (a + b + c) / 2
# S = (p * (p - a) * (p - b) * (p - c)) ** 0.5
# P = a + b + c
# print(f'Yuzasi:{S} \nPerimetri:{P}')
######################## 22-misol ###########################
# 1 - usul
# a = input('a ni kiriting:')
# b = input('b ni kiriting:')
# a,b = b,a
# print(a,b)

# 2 - usul
# a = input('a ni kiriting:')
# b = input('b ni kiriting:')
# c = a
# a = b
# b = c
# print(a,b)
######################## 23-misol ###########################
# 1-usul
# a = input('a ni kiriting:')
# b = input('b ni kiriting:')
# c = input('c ni kiriting:')
# a,b,c = b,c,a
# print(a,b,c)
# 2 - usul 
# a = input('a ni kiriting:')
# b = input('b ni kiriting:')
# c = input('c ni kiriting:')
# x = a
# a = b 
# b = c
# c = x
# print(a,b,c)
######################## 24-misol ###########################
# 1-usul
# a = input('a ni kiriting:')
# b = input('b ni kiriting:')
# c = input('c ni kiriting:')
# a,b,c = c,a,b
# print(a,b,c)
# 2 - usul
# a = input('a ni kiriting:')
# b = input('b ni kiriting:')
# c = input('c ni kiriting:') 
# x = a  
# a = c
# c = b
# b = x     
# print(a,b,c)       
######################## 25-misol ###########################
# x = float(input('x ni kiriting:'))
# y = 3 * (x ** 6) - 6 * (x ** 2) - 7 
# print('Funksiyaning qiymati:',y)
######################## 26-misol ###########################
# x = float(input('x ni kiriting:'))
# y = 4 * (x - 3) ** 6 - 7 * (x - 3) ** 3 + 2
# print('Funksiyaning qiymati:',y)
######################## 27-misol ###########################
# A = float(input('A ni kiriting:'))
# A2 = A ** 2
# A4 = A ** 4
# A8 = A ** 8
# print(f'A ning 2-darajasi:{A2} \nA ning 4-darajasi:{A4} \nA ning 8-darajasi:{A8}')
######################## 28-misol ###########################
# A = float(input('A ni kiriting:'))
# A2 = A ** 2
# A3 = A ** 3
# A5 = A ** 5
# A10 = A ** 10
# A15 = A ** 15
# result = f'''A ning 2-darajasi:{A2} 
# A ning 3-darajasi:{A3} 
# A ning 5-darajasi:{A5}
# A ning 10-darajasi:{A10}
# A ning 15-darajasi:{A15}'''
# print(result)
######################## 29-misol ###########################
# import math
# a = float(input('a ni kiriting (0 < a < 360):'))
# result = (a * math.pi) / 180
# print('a ning radiandagi qiymati:',result)
######################## 30-misol ###########################
# import math
# a = float(input('a ni kiriting (0 < a < 2pi):'))
# result = a * 180 / math.pi
# print('a ni gradusdagi ko`rinishi:',result)
######################## 31-misol ###########################
# t = float(input('Temperaturani kiriting:'))
# result = (t - 32) * 5 / 9
# print('Gradusdagi qiymati:',result)
######################## 32-misol ###########################
# t = float(input('Temperaturani kiriting:'))
# result = t * 9 / 5 * (t - 32)
# print('Farangeytdagi qiymati:',result)
######################## 33-misol ###########################
'''
         X kg ------ A so'm
                                ==>  demak 1 kg:  1 * A / X so'm turadi
         1 kg ------ ? 


         X kg ------ A so'm
                                ==>  demak Y kg: Y * A / X so'm turadi
         Y kg ------ ?       
'''
######################## 34-misol ###########################
'''
        Yuqoridagi misoldan malumki 1 kg shokolad narxi (1 * A / X) so'mga teng,
        1 kg konfet narxi esa (1 * B / Y) so'mga teng
        demak shokolad konfetdan qancha so'm qimmatligini aniqlash uchun narxlarini ayiramiz:
        Javob: (1 * A / X) - (1 * B / Y)
'''
######################## 35-misol ###########################
'''
Oqim bo'ylab bosib o'tgan yo'li: S1 = (V + U) * T1
Oqimga qarshi bosib o'tgan yo'li: S2 = (V - U) * T2
Umumiy masofa: S1 + S2

IZOH: Agar ushbu fo'rmulalarga tushunmagan bo'lsangiz xavotir olmang.Ushbu fo'rmulani tushunishingiz
uchun fizikadan boshlang'ich bilimingiz bo'lishi kerak :)
''' 
# v = float(input('V ni kiriting:'))
# u = float(input('U ni kiriting:'))
# T1 = float(input('T1 ni kiriting:'))
# T2 = float(input('T2 ni kiriting:'))
# S = (v + u) * T1 + (v - u) * T2
# print('Umumiy masofa:',S)
######################## 36-misol ###########################
'''
Fo'rmula: S + V1 * T + V2 * T
'''
# s = float(input('Boshlang`ich masofani kiriting (S):'))
# v1 = float(input('V1 ni kiriting:'))
# v2 = float(input('V2 ni kiriting:'))
# T = float(input('T ni kiriting:'))
# result = s + v1 * T + v2 * T
# print('T vaqtdan keyin mashinalar orasidagi masofa:',result)
######################## 37-misol ###########################
'''
Fo'rmula: |S - V1 * T - V2 * T| 
IZOH: | bu modul belgisi,agar natija manfiy chiqsa demak mashinalar uchrashib o'tib ketgan boladi,
lekin ular orasida masofa bo'ladi.
'''
# s = float(input('Boshlang`ich masofani kiriting (S):'))
# v1 = float(input('V1 ni kiriting:'))
# v2 = float(input('V2 ni kiriting:'))
# T = float(input('T ni kiriting:'))
# result = abs(s - v1 * T - v2 * T)
# print('T vaqtdan keyin mashinalar orasidagi masofa:',result)
######################## 38-misol ###########################
# a = float(input('A ni kiriting:'))
# b = float(input('B ni kiriting:'))
# try:
#     x = - b / a
#     print('x:',x)
# except:
#     print('Sonni 0 ga bo`lish mumkin emas! a ga noldan boshqa qiymat bering.')
######################## 39-misol ###########################
# A = float(input('A ni kiriting:'))
# B = float(input('B ni kiriting:'))
# C = float(input('C ni kiriting:'))
# Diskriminant = B ** 2 - 4 * A * C
# x1,x2 = (-B + (Diskriminant ** 0.5)) / 2 * A, (-B - (Diskriminant ** 0.5)) / 2 * A
# print('Tenglama ildizlari:',x1,x2)
######################## 40-misol ###########################
'''
{ A1 * x + B1 * y = C1
{ A2 * x + B2 * y = C2
''' 
# a1 = float(input('A1 koefitsentni kiriting:'))
# b1 = float(input('B1 koefitsentni kiriting:'))
# c1 = float(input('C1 koefitsentni kiriting:'))
# a2 = float(input('A2 koefitsentni kiriting:'))
# b2 = float(input('B2 koefitsentni kiriting:'))
# c2 = float(input('C2 koefitsentni kiriting:'))
# D = (a1 * b2 - a2 * b1)
# x = (c1 * b2 - c2 * b1) / D
# y = (a1 * c2 - a2 * c1) / D
# print('Tenglamalar sistemasining yechimlari:',x,y)
#-----------------------------------------------------------------------------------------------------------------> 