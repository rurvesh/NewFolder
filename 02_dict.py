a = {'1' : 'z', '2': 'b', '3': 'a'}

var = dict(sorted(a.items(), key=lambda x:x[1]))
print(var)