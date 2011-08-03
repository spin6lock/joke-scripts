#encoding=utf8


price_list = [54.6, 19.3, 61.2, 44.5, 19.5,20.5,70.3,26.4,41.2,10.4,62.9
]

money_limit=200

value = [0 for i in range(len(price_list) + 1)]
choose = [0 for i in range(len(price_list) + 1)]
gap = [money_limit for i in range(len(price_list) + 1)]

for i in range(1, len(price_list)+1):
	value[i] = value[i-1]
	choose[i] = 'No'
	total_weight = value[i-1]
	gap[i] = gap[i-1]
	if abs(total_weight + price_list[i-1] - money_limit) < gap[i-1]:
		value[i] = value[i-1] + price_list[i-1]
		choose[i] = 'Yes'
		gap[i] = abs(total_weight + price_list[i-1] - money_limit)

print "value:", "%.2f, "*len(value[1:]) %tuple(value[1:])
print "choose:", choose[1:]
print "gap:", "%.2f, "*len(gap[1:]) %tuple(gap[1:])
print "sum:", 
sumup = 0
for index, value in enumerate(choose):
	if value == 'Yes':
		sumup += price_list[index - 1]
print sumup
