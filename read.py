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