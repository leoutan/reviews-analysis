data = []
count = 0
sum_len = 0
avr_sum = 0
with open('reviews.txt', 'r') as f:
	for line in f:
		data.append(line)
		count += 1
		if count % 1000 == 0:
			print(len(data))
for d in data:
	sum_len = sum_len + len(d)
print(sum_len)
avr_sum = sum_len / len(data)
print(avr_sum)

new = []
for d in data:
	if len(d) < 100:
		new.append(d)
print('一共有', len(new), '筆留言長度小於100')
sum1 = 0
avg_sum1 = 0
for n in new:
	sum1 = sum1 + len(n)
avg_sum1 = sum1 / len(new)

good = []
for b in data:
	if 'good' in b:
		good.append(b)
print('一共有', len(good), '筆留言裡面有good')
print(good[0])
