my_dict = {'apple': 50, 'banana': 20, 'cherry': 30}

asc_sorted = dict(sorted(my_dict.items(), key=lambda item: item[1]))
print("Ascending:", asc_sorted)

desc_sorted = dict(sorted(my_dict.items(), key=lambda item: item[1], reverse=True))
print("Descending:", desc_sorted)
