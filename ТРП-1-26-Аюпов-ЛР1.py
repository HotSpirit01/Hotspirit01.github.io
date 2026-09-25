#n1
x=float(input('x='))
y=7*x+5
print('y=', y)
#1.2. Составить алгоритм вычисления длины окружности, если известен ее
#радиус, радиус окружности вводится пользователем.
Radius=int(input())
P=Radius*2*3.141592
print(P)
# Составить алгоритм вычисления периметра прямоугольного треугольника, если известны его катеты, катеты вводятся пользователем
a=float(input('first: '))
b=float(input('second: '))
f=a*a+b*b
c=pow(f, 0.5)
P=a+b+c
print('P=', P)
#1.3 Составить алгоритм вычисления периметра прямоугольного треугольника, если известны его катеты, катеты вводятся пользователем
a=float(input('first: '))
b=float(input('second: '))
f=a*a+b*b
c=pow(f, 0.5)
P=a+b+c
print('P=', P)
#1.4 Составить алгоритм вычисления периметра равнобедренной трапеции, если известны ее основания и высота, основания и высота вводятся пользователем.
ab=float(input('меньшая сторона:'))
cd=float(input('Большая сторона:'))
h=float(input('Высота:'))
if cd <= ab:
    print('err')
else:
    ost=cd-ab
    side=pow(h*h+ost*ost, 0.5)
    P=ab+cd+side*2
    print('Периметр равен: ', P)
#1.5 Найти расстояние между точками на плоскости с заданными координатами (x1, y1) и (x2, y2) (вычисляется через формулу гипотенузы прямоугольного треугольника). 
x1=float(input('x1: '))
x2=float(input('x2: '))
y1=float(input('y1: '))
y2=float(input('y2: '))
x=x2-x1
y=y2-y1
r=pow(x*x+y*y, 0.5)
print('r: ', r)
#2.1 Составить алгоритм решения задачи для определения большего из двух вещественных чисел (не используя функцию min или max).
x=float(input('x: '))
y=float(input('y: '))
if x > y:
    print(x, 'greater')
elif x < y:
    print(y, 'greater')
else:
    print('=')
#2.2 Составить алгоритм решения задачи для определения меньшего из трех целых чисел (не используя функцию min или max). 
a=float(input('a: '))
b=float(input('b: '))
c=float(input('c: '))
if a>b:
    if a > c:
        print(a, ' is greatest')
    elif a < c:
        print(c, ' is greatest')
    else:
        print(c, ' is greatest(a=c)')
elif a<b:
    if b > c:
            print(b, ' is greatest')
    elif b < c:
            print(c, ' is greatest')
    else:
            print(c, ' is greatest(b=c)')
else:
    if a>c:
            print(a, ' is greatest(a=b)')
    elif a<c:
          print(c, ' is greatest')
    else:
          print('a=b=c')
# 2.3 Вводятся три разных числа. Найти, какое из них является средним (больше одного, но меньше другого, не используя функцию min или max).
a=float(input('a: '))
b=float(input('b: '))
c=float(input('c: '))
if a>b:
    if a<c:
        print(a)
    elif a>c:
        if b>c:
            print(b)
        elif b<c:
            print(c)
        else:
            print(TypeError)
    else:
        print(TypeError)
elif a<b:
    if b<c:
            print(b)
    elif b>c:
        if a>c:
                print(a)
        elif a<c:
                print(a)
        else:
                print(TypeError)
    else:
            print(TypeError)
else:
     print(TypeError)
#2.4. Для данного x вычислить значение функции: 
x=float(input('x:'))
if x<=-1:
    y=1/(x*x)
elif x>-1 and x<=2:
    y=x*x
else:
    y=4
print(y)
#2.5. Даны действительные числа x, y вычислите где u=3z^2-2z+5
x=float(input('x: '))
y=float(input('y: '))
if x+y<2:
    z=pow(x*x+y*y, 0.5)
elif x+y==3 or x+y==8:
    z=2*x*y
elif x+y>=10:
    z=x-y
else:
    z=2*x+3*y
u=3*z*z-2*z+5
print(u)
#2.6 Определить четверть координатной плоскости, которой принадлежит точка. Координаты точки ввести с клавиатуры.
x=float(input('x: '))
y=float(input('y: '))
if x<0 and y>0:
    print('I')
elif x>0 and y>0:
    print('II')
elif x>0 and y<0:
    print('III')
else:
    print('IV')
#3.3. Составить алгоритм вывода таблицы перевода перевода 1, 2,... 20 долларов США в рубли по текущему курсу (значение курса вводится пользователем, ответ выдается столбцом, например, 1 $ = 65 руб.).
for i in range(21):
    dollar=84.40*i
    print(i,'$=',dollar, 'rub')
#3.4. Составить таблицу (для разделения строк таблицы использовать знак подчеркивания ‘_‘, а для разделения столбцов таблицы знак вертикальной полоски ‘|‘) вывода стоимости 2, 3, …, 10 кг конфет (цена 1 кг конфет вводится пользователем).
can=float(input('1 candy prise: '))
for i in range(2, 11):
    prise=can*i
    print('_________________________')
    print('| ', i, 'kg |', prise, ' rub |')
#3.5. Дано натуральное число n и k. Вычислите сумму:
k=1
S=0
n=int(input('n: '))
for k in range(1,n+1):
    S=S+1/(pow(k,5))
print(S)
#3.6. Дано натуральное число n и k. Вычислите сумму:
S=0
n=int(input('n: '))
for k in range(1,n+1):
    S=S+(2*k-1)/(k+1)
print(S)
#3.7. Дано натуральное число n и k. Вычислите произведение n множителей:
S=1
n=int(input('n: '))
for k in range(1,n+1):
    S=S*(1+1/k)
print(S)
#4.2. Даны два целых числа A и B (A < B). Составить алгоритм вывода всех целых чисел, расположенных между данными числами (не включая сами эти числа), в порядке их убывания.
A=int(input('A: '))
B=int(input('B (B>A): '))
if A>B:
    print('err')
i=A+1
while i>A and i<B:
    print(i)
    i=i+1
#4.3. Дано натуральное число N. Составить алгоритм получения всех чисел, меньше N.
N=int(input('N(N>0): '))
i=N-1
while i>0:
    print(i)
    i=i-1
#4.4. Дано число n. Составить алгоритм поиска первого натурального числа, квадрат которого больше n. 
n=float(input('n: '))
i=0
while i*i<=n:
    i=i+1
print(i)
#4.5. Определить сумму всех нечетных чисел от 1 до 99
S=0
i=1
while i<=99:
    if i%2==0:
        i=i+1
    else:
        S=S+i
        i=i+1
print(S)