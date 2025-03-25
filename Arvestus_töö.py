from module1 import * 
# Напишите функцию kool(), при запуске которой происходит заполнение двух списков: opilased[], puudumised[].
# После заполнения списков появляется меню с выбором действий:
# • Узнать n лучших учеников;
# • Упорядочить список в порядке возрастания прогулов. отобразить прогулы вместе с фамилиями учеников;
# • Вывести список учеников отправленных на комиссию ( критерий придумать самостоятельно);
# • Отчислить(удалить из списка)  учеников, у которых прогулов больше чем 100;
# • Свой вариант.
# Для решения задачи используйте функции.

# Списки


print(kool(opilased, puudumised))


# После заполнения списков появляется меню с выбором действий
# Меню с выбором действий
print("\nMennu")
print("1. Leia välja n parimat õpilast")
print("2. Korraldage nimekiri puudumiste kasvavas järjekorras. kuvage puudumised koos õpilaste nimedega")
print("3. Prindi komisjonile saadetud õpilaste nimekiri („Koosta oma kriteeriumid")
print("4. Kandke välja (eemaldage nimekirjast) õpilased, kellel on üle 100 puudumise")
print("5. Teie enda variant")
print("6. Väljumine")
while True:
    try:
        valik=int(input("Valige tegevus: "))
    except:
        print("Vali tegevus numbritega 1-6")
    if valik==1:
        print(top_n(opilased))
    elif valik==2:
        print(sort(opilased, puudumised))
    elif valik==3:
        print(commission(opilased, puudumised))
    elif valik==4:
        print(exclude(opilased, puudumised))
    elif valik==5:
        
    elif valik==6:
        break
    else:
        print("Vali tegevus numbritega 1-6")