money = int(input('Введите вносимую сумму денег '))

per_cent = {'ТКБ': 5.6, 'СКБ': 5.9, 'ВТБ': 4.28, 'СБЕР': 4.0}
depo_TKB = per_cent['ТКБ'] * money *0.01
depo_CKB = per_cent['СКБ'] * money *0.01
depo_VTB = per_cent['ВТБ'] * money *0.01
depo_SBER = per_cent['СБЕР'] * money *0.01

deposit = {'Д_ткб': depo_TKB, 'Д_скб': depo_CKB, 'Д_втб': depo_VTB, 'Д_сбер': depo_SBER}
print(deposit)
print('Максимальная сумма, которую вы можете заработать - ', max(deposit.values()))
print('Так что несите деньги в', max(per_cent, key=per_cent.get))
print('Хотя с учетом нынешней инфляции, не думаю, что это хорошая идея :-(. До свидания!')
