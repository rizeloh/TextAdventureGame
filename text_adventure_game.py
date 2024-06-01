def display_intro():
    """
    Введение в игру.
    """
    print("Вы находитесь в темной комнате в старом замке.")
    print("Перед вами две двери.")
    print("Вы должны выбрать одну из них, чтобы продолжить ваше приключение.")

def choose_door():
    """
    Выбор двери игроком.
    """
    door = ""
    while door != "1" and door != "2":
        print("Выберите дверь: 1 или 2?")
        door = input("> ")
    return door

def check_door(door_choice):
    """
    Проверка выбора двери и развитие сюжета.
    """
    print("Вы открываете дверь номер", door_choice)
    if door_choice == "1":
        print("Перед вами злобный дракон!")
        print("Дракон атакует и вы не успеваете увернуться. Вы проиграли!")
    elif door_choice == "2":
        print("Вы находите сундук с сокровищами!")
        print("Поздравляем! Вы победили и нашли сокровища!")

def play_game():
    """
    Основная функция игры.
    """
    display_intro()
    door_choice = choose_door()
    check_door(door_choice)

if __name__ == "__main__":
    play_game()
