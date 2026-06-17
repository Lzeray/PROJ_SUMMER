s = {'2': 'привет', '1': 'Hello'}

h = list(s.items())
h.sort()

print(h)
h = dict(h)
print(h)