money = float (input("Введите сумму: "))

per_cent = {'ТКБ': 5.6, 'СКБ': 5.9, 'ВТБ': 4.28, 'СБЕР': 4.0}

per_cent['ТКБ'] = 5.6 * (money/100)
per_cent['СКБ'] = 5.9 * (money/100)
per_cent['ВТБ'] = 4.28 * (money/100)
per_cent['СБЕР'] = 4.0 * (money/100)

dp1 = per_cent['ТКБ']
dp2 = per_cent['СКБ']
dp3 = per_cent['ВТБ']
dp4 = per_cent['СБЕР']

deposite = [dp1, dp2, dp3, dp4]

print("ТКБ =", dp1, "СКБ =", dp2, "ВТБ", dp3, "СБЕР = ", dp4)
print("Максимальная сумма, которую вы можете заработать - ", max(deposite))