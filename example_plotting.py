#example_plotting.py

import random as rand
from matplotlib import pyplot as plt

data = range(6)

event_categories = ['event1', 'event2', 'event3', 'event4', 'event5', 'event6']
d = {el:0 for el in event_categories}
count = 0
xevents = range(1,len(event_categories)+1)
for i in d:
	
	data[count] = rand.randrange(10,100)
	d[i] = data[count]
	count += 1 




plt.bar(range(len(d)), d.values())
plt.xticks(range(len(d)), d.keys())
plt.title('Score')


plt.show()