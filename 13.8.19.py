age_list = list()
price = list()
q = int(input('Сколько вам билетов, сэр?\n'))
for i in range(1, q+1):
    age_list.append(int(input('Сколько лет? ')))
for p in age_list:
    if p < 18:
        price.append(0)
    elif 18 <= p <= 25:
        price.append(990)
    else:
        price.append((1390))
if q <= 3:
    print('C вас ', sum(price), 'рублей. Может приведете еше одного, тогда будет скидка?!')
else:
    print('С вас ', sum(price)*0.9, 'рублей, у вас 10% скидка, так как больше 3х человек.\nИначе бы было', sum(price), 'рублей')

