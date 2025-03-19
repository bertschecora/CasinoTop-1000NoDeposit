import random

print("1000 за регистрацию без депозита - Демо!")
spins = 5
while spins > 0:
    spins -= 1
    result = random.choice(["Джекпот!", "Фриспин!", "Ещё спин!"])
    print(f"Спин {5 - spins}: {result}")
    if spins > 0:
        input("Нажми Enter для нового шанса...")
print("Бери 1000 и крути в топ-казино!")
