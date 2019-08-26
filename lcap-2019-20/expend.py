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

ls = ["Total Budgeted General\nFund Expenditures", "Total Budgeted\nExpenditures in LCAP"]
xs = np.arange(len(ls))
ys = [637297, 411900]

mean = sum(ys)/len(ys)
dollar = lambda x, p='': '\$'+format(int(x), ',')

#fig1 = plt.figure(1, figsize=(7,4))
#ax = fig1.add_subplot(1,1,1)
plt.bar(xs, ys, width=0.6, align='center', tick_label=ls, color=['blue','forestgreen'])
plt.xlim(-0.5,1.5)
for i, v in enumerate(ys):
    plt.gca().text(i, v+0.03*mean, dollar(v), color='black', ha='center')
plt.gca().get_yaxis().set_major_formatter(mlp.ticker.FuncFormatter(dollar))
plt.ylim([0, 700000])
plt.title('Budgeted Expenditures')

if svg:
	plt.savefig('expend.svg')
else:
	plt.savefig('expend.png')
	#plt.show()
