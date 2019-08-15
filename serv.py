#!/usr/bin/python

svg = False;

import numpy as np
import matplotlib as mlp
import matplotlib.pyplot as plt
import locale

if svg:
	mlp.use('svg')
mlp.rcParams['font.family'] = ['Computer Modern', 'DejaVu Sans']
plt.rc("text", usetex=True)
locale.setlocale(locale.LC_ALL, '')

ls = ["Estimated Actual Expenditures for High Needs Students in LCAP: \$45,495","Total Budgeted Expenditures for High Needs Students in the LCAP: \$53,579"]
xs = np.arange(len(ls))
ys = [45495,53579]

mean = sum(ys)/len(ys)
dollar = lambda x, p='': '\$'+format(int(x), ',')

#fig1 = plt.figure(1, figsize=(7,5))
#ax = fig1.add_subplot(1,1,1)
h = plt.barh(xs, ys, height=0.5, align='center', tick_label=['',''], color=['blue','forestgreen'])
plt.ylim(-1,1.5)
plt.gca().invert_yaxis()
plt.gcf().set_size_inches(7,4)
plt.tick_params(axis='y', which='both', bottom=False, top=False)
for i, v in enumerate(ys):
    plt.gca().text(i, v+0.03*mean, dollar(v), color='black', va='center')
plt.gca().set_xlim([0, 60000])
plt.gca().get_xaxis().set_major_formatter(mlp.ticker.FuncFormatter(dollar))
plt.title('Current Year Expenditures: Increased or Improved Services for High Needs Students')
plt.legend(h, ls, loc='upper right')

if svg:
	plt.savefig('serv.svg')
else:
	plt.savefig('serv.png')
	#plt.show()
