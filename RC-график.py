import matplotlib.pyplot as plt
import numpy as np
with open("data.txt", "r") as dat:
    d=[float(i) for i in dat.read().split()]
with open("settings.txt","r") as settings:
    tmp=[float(i) for i in settings.read().split()]
data=np.array(d)
y_pred= data * (3.3 / 255)
nu= len(data) / tmp[0]
y= y_pred[7:333]
x = [(1 / nu * i) for i in range(len(y))]
total_time=len(y)*tmp[1]
charge=194*tmp[1]
text_x=float(np.percentile(x, 60))
text_y=float(np.percentile(y,20))
plt.text(text_x, text_y,
        f"Время заряда: {charge:.2f} с\nВремя разряда: {(total_time-charge):.2f} с",linespacing=6 ,fontsize=8)
plt.xlabel('Время, c', fontsize=12)
plt.ylabel('Напряжение, B',fontsize=12)
plt.plot(x, y,label='U(t)' ,color='blue', linewidth=1.5, marker='o', markersize=5, markevery=20, markerfacecolor='blue')
plt.title("Процесс заряда и разряда конденсатора в RC-цепи",fontsize=14, pad=15, wrap=True)
plt.grid(which='major', linestyle='-', linewidth=1, color='gray', alpha=0.6)
plt.grid(which='minor', linestyle='--', linewidth=0.5, color='gray', alpha=0.4)
plt.minorticks_on()
plt.xlim(0,11)
plt.ylim(0,2.6)
plt.legend(framealpha=1)
plt.savefig("get.svg", format='svg',bbox_inches='tight')
plt.show()