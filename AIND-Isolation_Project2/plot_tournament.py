import pandas as pd 
import seaborn as sns
import matplotlib.pyplot as plt

# data={'ID_Improved':[17/20,16/20,13/20,12/20,13/20,12/20,9/20],
# 'Student1':[17/20,15/20,15/20,14/20,15/20,12/20,12/20],
# 'Student2a':[14/20,15/20,10/20,13/20,15/20,12/20,11/20],
# 'Student2b':[18/20,16/20,12/20,10/20,14/20,12/20,13/20],
# 'Student3a':[16/20,14/20,11/20,14/20,16/20,13/20,11/20],
# 'Student3b':[16/20,13/20,12/20,13/20,15/20,13/20,10/20],
# 'cat':['a','b','c','d','e','f','g']
# }

# data={'data':[17/20,16/20,13/20,12/20,13/20,12/20,9/20]+
# [17/20,15/20,15/20,14/20,15/20,12/20,12/20]+
# [14/20,15/20,10/20,13/20,15/20,12/20,11/20]+
# [18/20,16/20,12/20,10/20,14/20,12/20,13/20]+
# [16/20,14/20,11/20,14/20,16/20,13/20,11/20]+
# [16/20,13/20,12/20,13/20,15/20,13/20,10/20],
# '':['ID_Improved'*7]
# 'cat':['a','b','c','d','e','f','g']*7
# }

# pd_data=pd.DataFrame(data)

# ax = sns.barplot(x='cat',y='ID_Improved', hue='Student1',data=pd_data)

# # ax.show()
# plt.show()

# tips = sns.load_dataset("tips")
# print(tips)

"""
========
Barchart
========

A bar plot with errorbars and height labels on individual bars
"""
import numpy as np
import matplotlib.pyplot as plt

N = 7


a=np.array([17,16,13,12,13,12,9])+np.array([15,14,11,10,15,12,12])
b=np.array([17,15,15,14,15,12,12])+np.array([17,14,13,11,16,12,11])
c=np.array([14,15,10,13,15,12,11])+np.array([20,15,15,10,12,14,14])
d=np.array([18,16,12,10,14,12,13])+np.array([16,15,12,13,13,13,15])
e=np.array([16,14,11,14,16,13,11])+np.array([18,15,12,11,14,12,13])
f=np.array([16,13,12,13,15,13,10])+np.array([17,14,12,13,16,13,15])

a=a/40
b=b/40
c=c/40
d=d/40
e=e/40
f=f/40

total_score=[65.71+63.57, 71.43+67.14, 64.29+71.43, 67.86+69.29, 67.86+67.86, 65.71+71.43]
print(np.array(total_score)/2)

# men_means = (20, 35, 30, 35, 27)
# men_std = (2, 3, 4, 1, 2)

ind = np.arange(N)  # the x locations for the groups
width = 0.2      # the width of the bars

fig, ax = plt.subplots()
rects1 = ax.bar(ind, a, width, color='c')
rects2 = ax.bar(ind + width, b, width, color='y')
rects3 = ax.bar(ind + 2*width, d, width, color='g')
rects4 = ax.bar(ind + 3*width, f, width, color='b')

# add some text for labels, title and axes ticks
ax.set_ylabel('Winning ratio')
ax.set_xlabel('Agents played with')
ax.set_title('ID_Improved and Student agents vs other agents')
ax.set_ylim(0,1)
ax.set_xticks(ind + width / 2)
ax.set_xticklabels(('Random', 'MM_Null', 'MM_Open', 'MM_Improved', 'AB_Null','AB_Open','AB_Improved'))

ax.legend((rects1[0], rects2[0], rects3[0], rects4[0]), ('ID_Improved', 'Student H1', 'Student H2', 'Student H3'))


# def autolabel(rects):
#     """
#     Attach a text label above each bar displaying its height
#     """
#     for rect in rects:
#         height = rect.get_height()
#         ax.text(rect.get_x() + rect.get_width()/2., 1.05*height,
#                 '%d' % int(height),
#                 ha='center', va='bottom')

# autolabel(rects1)
# autolabel(rects2)
plt.tight_layout()

# plt.savefig('bar_student3agent.png',dpi=400)

plt.show()