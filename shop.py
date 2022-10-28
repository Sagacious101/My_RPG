def shop(player_name, player_money, player_xp, player_hp, player_mp, player_damage):
    os.system("cls")
    #печатаем персонажа
    print(f"Имя: {player_name}")
    print(f"Деньги: {player_money}")
    print(f"Опыт: {player_xp}")
    print(f"HP: {player_hp}")
    print(f"MP: {player_mp}")
    print(f"АТК: {player_damage}")
    print(F"Зелья: {player_potions}")

    #печатаем ситуацию
    print(f"{player_name} приехал в лавку снаряжения")

    #печатаем выборы
    print("1 - Купить зелье лечения за 3 монеты")
    print("2 - Выйти из лавки обратно в город")

    # проверяем выбор
    answer = input("Введите номер варианта и нажмите ENTER: ")
    if answer == "1":

    elif answer == "2":

    input("++++++++")
