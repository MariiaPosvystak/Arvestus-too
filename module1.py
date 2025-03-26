# Напишите функцию kool(), при запуске которой происходит заполнение двух списков: opilased[], puudumised[].
# После заполнения списков появляется меню с выбором действий:
# • Узнать n лучших учеников;
# • Упорядочить список в порядке возрастания прогулов. отобразить прогулы вместе с фамилиями учеников;
# • Вывести список учеников отправленных на комиссию ( критерий придумать самостоятельно);
# • Отчислить(удалить из списка)  учеников, у которых прогулов больше чем 100;
# • Свой вариант.
# Для решения задачи используйте функции.

opilased=[]
puudumised=[]
# Заполнение списков
def kool(opilane: str, puudub:int)->any:
    """ Järjestab õpilased ja nende puudumised kaheks eraldi listiks
    :param opilane: õpilase nimi
    :param puudub: õpilase puudumise arv
    :return: õpilased ja nende puud
    """
    while True:
        opilane=str(input("Sisestage õpilase nimi "))
        if opilane.lower()=="stop":
            print(opilased, puudumised)
            break
        puudub=int(input("Sisestage, mitu puudub tal on "))
        opilased.append(opilane)
        puudumised.append(puudub)
        

# Узнать n лучших учеников
def top_n(n: int)->any:
    """ Välistab n parimat õpilast, kellel on kõige vähem puudumisi
    :param n: õpilaste arv
    :return: n parimat õpilast
    """
    n=int(input("Sisestage tippõpilaste arv, mida soovite näha"))
    sort_opilased=sorted(zip(opilased, puudumised))
    k=sort_opilased[:n]
    return k

# Упорядочить список в порядке возрастания прогулов. отобразить прогулы вместе с фамилиями учеников;
def sort()->any:
    """ Sorteerib õpilased ja nende puudumised vastavalt puudumiste arvule
    :return: sorteeritud õpilased ja nende puudumised
    """
    sort_puudumised=sorted(zip(opilased, puudumised))
    return sort_puudumised

# Вывести список учеников отправленных на комиссию ( критерий придумать самостоятельно)
def commission()->any:
    """ Õpilased, kellel on puudumised rohkem kui 50, saadetakse komisjoni
    :return: õpilased ja nende puudumised, kes saadetakse komisjoni
    """
    l=zip(opilased, puudumised)
    for opilased, puudumised in l:
        if puudumised>50: 
            return opilased, puudumised

# Отчислить(удалить из списка)  учеников, у которых прогулов больше чем 100
def exclude()->any:
    """ Õpilased, kellel on puudumised rohkem kui 100, eemaldatakse
    :return: õpilased ja nende puudumised, kes eemaldatakse
    """
    l=zip(opilased, puudumised)
    for opilased, puudumised in l:
        if puudumised>100:
            opilased.remove()
            puudumised.remove()
            return opilased, puudumised

# Свой вариант
