from random import *
def arvud_loendis():
    print("Данные:")
    n=abs(int(input("Сколько целых чисел генерируем в список? => ")))
    mini=int(input("Введите минимальное число диапазона => "))
    maxi=int(input("Введите максимальное число диапазона => "))
    if mini>=maxi:
        mini,maxi=vahetus(mini,maxi)
    s=[]
       generaator(n,s,mini,maxi)
    print()
    print("Результаты:")
    print("Полученный список от",mini,"до",maxi,s)
    s.sort()
    print("Отсортированный список",s)
    pos=neg=null=[]
    jagamine(s,pos,neg,nol)
    print("Список положительных элементов",pos)
    print("Список отрицательных элементов",neg)
    print("Список нулевых элементов",nol)
    kesk=keskmine(pos)
    lisamine(s,kesk)
    print("Среднее положительных:",kesk)
    kesk=keskmine(neg)
    lisamine(s,kesk)
    print("Среднее отрицательных:",kesk)
    print("Добавляем средние в изначалный массив:")
    s.sort()
    print(s)

def vahetus (a:int,b:int):
	"""Kui a<b vahetasid ära
	:param int a: arv suurem kui b
	:param int b: arv väiksem kui a
	:rtype:int
	"""
	abi=a
	a=b
	b=abi
	return a,b

def generaator (n:int,loend:list,a:int,b:int):
	"""Lisab loendisse n randomiseeritud vahemik a kuni b
	:param int n: kui palju arvu on
	:param list loend: loend
	:param int a: minimaalne väärtus
	:param int b: maksimaalne väärtus
	:rtype:int 
	"""
	for i in range (n):
			loend.append(randint(a,b))

def jagamine(loend:list,p:int,n:int,nol:int):
	"""Positiivse, negatiivse ja nulli lisamine loendisse
	:param list loend: loend
	:param p: positiivne lisamine
	:param n: negativne lisamine 
	:param nol: nulli lisamine
	:rtype:int
	"""
	for el in loend:
		if el>0:
			p.append(el)
		elif el<0:
			n.append(el)
		else:
			nol.append(el)

def keskmine(loend:list,n:float):
	"""Keskmise väärtuse arutlemine
	:param list loend: loend
	:param n: kui palju väärtuseid on lisatud
	:rtype:float
	"""
	n=len(loend)
	if n==0:
		kesk=0
	else:
		sum=0
		for i in loend:
			sum+=i
		kesk=round(sum/n,2)
	return kesk

def lisamine(loend:list,el:float):
	"""Lisakse keskmised väärtused loendisse
	:param list loend: loend
	:param el: väärtus, mis lisakse
	:rtype:float
	"""
	loend.append(el)
	loend.sort()