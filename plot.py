import matplotlib.pyplot as plt

s = [15, 32, 88, 59, 44,  -32, 16]
x = range(len(s))
ax = plt.gca()
ax.bar(x, s, align='edge') 
ax.set_xticks(x)
ax.set_xticklabels(('8:30', '9:00', '10:30', '12:00',  '14:30', '16:00', '17:30'))
plt.show()
