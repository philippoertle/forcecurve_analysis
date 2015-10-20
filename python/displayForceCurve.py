__author__ = 'Philipp Oertle'

import csv
import numpy as np
import tkinter as tk
from tkinter import filedialog
import matplotlib.pyplot as plt

root = tk.Tk()
root.withdraw()
#file = filedialog.askopenfilenames()
file = 'D:\\Software\\forcecurve_analysis\\forcecurves\\connective_tissue\\map-data-2011.04.19-13.41.43-0273.out'
print(file)
fileLength = 0

#-------------------------------------------------------Process the height file-------------------------------------------------------

fileHeader = []
fwdData = []
bwdData = []
fwd = True
with open(file, newline='') as csvfile:
	filderContent = csv.reader(csvfile, delimiter=':')
	for row in filderContent:
		if len(row) > 1:
			fileHeader.append(row)
		if len(row) == 1 and len(fileHeader) < 50 and row != '#\r\n':
			fwdData.append(row[0])
		if len(row) == 1 and len(fileHeader) > 50 and row != '#\r\n':
			bwdData.append(row[0])
fwdData.pop(0)
fwdData.pop(0)

fwdData_np = np.zeros(shape=(len(fwdData),7))
for index in range(len(fwdData)):
	fwdData_np[index] = np.fromstring(fwdData[index],sep=' ')


vDeflection = fwdData_np[:,1]
hDeflection = fwdData_np[0:,4]
height_measured = fwdData_np[:,2]
print(len(vDeflection), len(height_measured))
fig, ax1 = plt.subplots()
ax1.plot(height_measured, vDeflection, 'b-')
ax1.set_xlabel('piezo extension [m]')
ax1.set_ylabel('vertical deflection [N]', color='b')

ax2 = ax1.twinx()
ax2.plot(height_measured, hDeflection, 'r.')
ax2.set_ylabel('horizontal deflection [V]', color='r')

plt.show()
