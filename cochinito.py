import random 

saving_days = 150
money_in_piggy = [
    4, 6, 7, 8, 9, 10, 12, 14, 15, 16,
    20, 22, 23, 26, 28, 30, 31, 35, 36,
     53, 
    60, 61, 65, 66, 69, 71, 73,
    84, 91, 94,
    100, 101, 109, 110, 113, 115, 117,
    120, 121, 131, 134, 
    140, 141, 142, 149, 150]
total_savings = saving_days * (saving_days + 1) //2
saving_days_now = len(money_in_piggy)
piggy_total = sum(money_in_piggy)


def get_cochinito_today_savings():
    while True:
        today_money = random.randint(1, 150)
        if today_money not in money_in_piggy:
            return today_money
res = saving_days - saving_days_now
today_money = get_cochinito_today_savings()
print("El numero de hoy es: ", today_money)
print("Total ahorrado: ", piggy_total)
print("Faltan ", res, "dias de ahorro")
