from pulp import LpMaximize, LpProblem, LpVariable

# Ініціалізуємо проблему як максимізацію
prob = LpProblem("Виробництво напоїв", LpMaximize)

# Визначаємо змінні рішення
limonad = LpVariable("Лимонад", lowBound=0, cat='Integer')  # Кількість одиниць лимонаду
sik = LpVariable("Фруктовий сік", lowBound=0, cat='Integer')  # Кількість одиниць фруктового соку

# Обмеження ресурсів
prob += 2 * limonad + sik <= 100  # Вода
prob += limonad <= 50  # Цукор
prob += limonad <= 30  # Лимонний сік
prob += 2 * sik <= 40  # Фруктове пюре

# Цільова функція - максимізація виробництва
prob += limonad + sik

# Розв'язуємо проблему
prob.solve()

# Виводимо результат
print("Кількість одиниць Лимонаду:", int(limonad.varValue))
print("Кількість одиниць Фруктового соку:", int(sik.varValue))
