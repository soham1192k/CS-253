from matplotlib import pyplot as plt  
import numpy as np
from matplotlib import rc
import csv
with open('data.csv', newline='') as csvfile:
    data_list=list(csv.reader(csvfile, delimiter=','))

#Number of matches 
format=['Tests','ODIs','T20Is','First-Class','List A','T20s']
data=list(map(int,data_list[0]))
explode= (0.2,0.1,0,0,0,0)
fig1, ax1 = plt.subplots()
ax1.pie(data, explode=explode, labels=format, autopct='%1.1f%%',
        shadow=True, startangle=90)
ax1.axis('equal') 
plt.savefig('1.png')
plt.show()

#Number of centuries and half centuries
centuries=list(map(int,data_list[1]))
half_centuries=list(map(int,data_list[2]))
x = np.arange(len(format))  # the label locations
width = 0.35
fig, ax = plt.subplots()
rects1 = ax.bar(x - width/2, centuries, width, label='Centuries')
rects2 = ax.bar(x + width/2, half_centuries, width, label='Half Centuries')
ax.set_xticks(x)
ax.set_xticklabels(format)
ax.legend()
def autolabel(rects):
    for rect in rects:
        height = rect.get_height()
        ax.annotate('{}'.format(height),
                    xy=(rect.get_x() + rect.get_width() / 2, height),
                    xytext=(0, 3),  # 3 points vertical offset
                    textcoords="offset points",
                    ha='center', va='bottom')
autolabel(rects1)
autolabel(rects2)
fig.tight_layout()
plt.grid(color='b',linestyle='-',linewidth=1)
plt.title("Rohit Sharma:Count of Centuries and Half Centuries across formats")
plt.savefig('2.png')
plt.show()

#Average
fig = plt.figure()
avg=list(map(float,data_list[3]))
plt.bar(format,avg,color='maroon',width=0.4)
plt.grid(color='b',linestyle='-',linewidth=1)
plt.xlabel("Format")
plt.ylabel("Average")
plt.title("Rohit Sharma: Average across various formats")
plt.savefig('3.png')
plt.show()

#Strike Rate
fig = plt.figure()
srate=list(map(float,data_list[4]))
plt.bar(format,srate,color='orange',width=0.4)
plt.grid(color='b',linestyle='-',linewidth=1)
plt.xlabel("Format")
plt.ylabel("Strike Rate")
plt.title("Rohit Sharma: Strike Rate across various formats")
plt.savefig('4.png')
plt.show()

#Total Runs across formats
x1=[2007,2008,2009,2010,2011,2012,2013,2014,2015,2016,2017,2018,2019,2020]
y1=list(map(int,data_list[5]))
y2=list(map(int,data_list[6]))
y3=list(map(int,data_list[7]))
plt.plot(x1,y1,marker='o')
plt.plot(x1,y2,marker='o')
plt.plot(x1,y3,marker='o')
plt.grid(color='b',linestyle='-',linewidth=1)
plt.xlabel("Format")
plt.ylabel("Runs")
plt.title("Rohit Sharma:Total runs scored per year across formats")
plt.legend(["Tests","ODIs","T20Is"])
plt.savefig('5.png')
plt.show()

#Runs in all formats across all countries
rc('font', weight='bold')
data=["Australia","Bangladesh","England","India","New Zealand","South Africa","Sri Lanka","West Indies"]
bars1=list(map(int,data_list[8]))
bars2=list(map(int,data_list[9]))
bars3=list(map(int,data_list[10]))
bars = np.add(bars1, bars2).tolist()
r = [0,1,2,3,4,5,6,7]
barWidth=0.5
plt.bar(r, bars1, color='#7f6d5f', edgecolor='white', width=barWidth)
plt.bar(r, bars2, bottom=bars1, color='#557f2d', edgecolor='white', width=barWidth)
plt.bar(r, bars3, bottom=bars, color='#2d7f5e', edgecolor='white', width=barWidth)
plt.xticks(r,data, fontweight='bold')
plt.text(-0.125,1950,"1917")
plt.text(0.875,690,"675")
plt.text(1.875,1650,"1638")
plt.text(2.875,6260,"6245")
plt.text(3.875,810,"795")
plt.text(4.875,570,"552")
plt.text(5.875,1070,"1053")
plt.text(6.875,695,"677")
plt.grid(color='b',linestyle='-',linewidth=1)
plt.xlabel("Country")
plt.ylabel("Runs")
plt.title("Rohit Sharma: Runs scored across all formats in every country")
plt.legend(["Tests","ODIs","T20Is"])
plt.savefig('6.png')
plt.show()

# Mode of dismissal
way=["Bowled","Caught","Caught Behind","LBW","Stumped","Run Out"]
data=list(map(int,data_list[11]))
explode= (0,0.1,0,0,0.2,0.1)
fig1, ax1 = plt.subplots()
ax1.pie(data, explode=explode, labels=way, autopct='%1.1f%%',
        shadow=True, startangle=90)
ax1.axis('equal') 
plt.title("Rohit Sharma:Mode of dismissal in ODIs")
plt.show()
way=["Bowled","Caught","Caught Behind","LBW","Stumped","Run Out"]
data=list(map(int,data_list[12]))
explode= (0,0.1,0,0,0.2,0.1)
fig1, ax1 = plt.subplots()
ax1.pie(data, explode=explode, labels=way, autopct='%1.1f%%',
        shadow=True, startangle=90)
ax1.axis('equal') 
plt.title("Rohit Sharma:Mode of dismissal in Tests")
plt.show()
way=["Bowled","Caught","Caught Behind","LBW","Stumped","Run Out"]
data=list(map(int,data_list[13]))
explode= (0,0.1,0,0,0.2,0.1)
fig1, ax1 = plt.subplots()
ax1.pie(data, explode=explode, labels=way, autopct='%1.1f%%',
        shadow=True, startangle=90)
ax1.axis('equal') 
plt.title("Rohit Sharma:Mode of dismissal in T20Is")
plt.savefig('7.png')
plt.show()

#Runs against every country
countries=["Afghanistan","Australia","Bangladesh","England","Ireland","New Zealand","Pakistan","South Africa","Sri Lanka","UAE","West Indies","Zimbabwe"]
t20=list(map(int,data_list[14]))
odi=list(map(int,data_list[15]))
tests=list(map(int,data_list[16]))
x = np.arange(len(countries)) 
width = 0.35
fig, ax = plt.subplots()
rects1 = ax.bar(x - 2*width/3,tests, width, label='Tests')
rects2 = ax.bar(x - 0.5*width/3, odi, width, label='ODIs')
rects3 = ax.bar(x + width/3, t20, width, label='T20Is')
ax.set_xticks(x)
ax.set_xticklabels(countries)
ax.legend()
autolabel(rects1)
autolabel(rects2)
autolabel(rects3)
fig.tight_layout()
plt.grid(color='b',linestyle='-',linewidth=1)
plt.title("Rohit Sharma:Performances by Opponent")
plt.savefig('8.png')
plt.show()

#Average across batting positions
x1=[2,3,4,5,6,7]
y1=list(map(float,data_list[17]))
y2=list(map(float,data_list[18]))
y3=list(map(float,data_list[19]))
plt.plot(x1,y1,marker='o')
plt.plot(x1,y2,marker='o')
plt.plot(x1,y3,marker='o')
plt.grid(color='b',linestyle='-',linewidth=1)
plt.xlabel("Batting Position")
plt.ylabel("Average")
plt.title("Rohit Sharma:Average across batting positions")
plt.legend(["Tests","ODIs","T20Is"])
plt.savefig('9.png')
plt.show()

#Home and away runs
format=["Tests","ODIs","T20Is"]
home=list(map(int,data_list[20]))
away=list(map(int,data_list[21]))
x = np.arange(len(format))  
width = 0.35
fig, ax = plt.subplots()
rects1 = ax.bar(x - width/2, home, width, label='Home')
rects2 = ax.bar(x + width/2, away, width, label='Away')
ax.set_xticks(x)
ax.set_xticklabels(format)
ax.legend()
autolabel(rects1)
autolabel(rects2)
fig.tight_layout()
plt.grid(color='b',linestyle='-',linewidth=1)
plt.title("Rohit Sharma:Total Runs- Home and Away")
plt.legend(["Tests","ODIs","T20Is"])
plt.savefig('10.png')
plt.show()

#Home and away centuries
format=["Tests","ODIs","T20Is"]
home=list(map(int,data_list[22]))
away=list(map(int,data_list[23]))
x = np.arange(len(format))
width = 0.35
fig, ax = plt.subplots()
rects1 = ax.bar(x - width/2, home, width, label='Home')
rects2 = ax.bar(x + width/2, away, width, label='Away')
ax.set_xticks(x)
ax.set_xticklabels(format)
ax.legend()
autolabel(rects1)
autolabel(rects2)
fig.tight_layout()
plt.grid(color='b',linestyle='-',linewidth=1)
plt.title("Rohit Sharma:Centuries-Home and away")
plt.legend(["Tests","ODIs","T20Is"])
plt.savefig('11.png')
plt.show()

#IPL most sixes
srate=[150.11]
sixes=[349]
plt.scatter(srate,sixes,c='r')
srate=[151.91]
sixes=[235]
plt.scatter(srate,sixes,c='b')
srate=[136.75]
sixes=[216]
plt.scatter(srate,sixes,c='m')
srate=[130.61]
sixes=[213]
plt.scatter(srate,sixes,c='g')
srate=[130.73]
sixes=[201]
plt.scatter(srate,sixes,c='k')
srate=[149.87]
sixes=[198]
plt.scatter(srate,sixes,c='c')
srate=[141.54]
sixes=[195]
plt.scatter(srate,sixes,c='y')
srate=[137.14]
sixes=[194]
plt.scatter(srate,sixes,c='lime')
srate=[137.91]
sixes=[190]
plt.scatter(srate,sixes,c='orange')
srate=[129.99]
sixes=[163]
plt.scatter(srate,sixes,c='darkviolet')
plt.legend(["Chris Gayle","AB de Villiers","MS Dhoni","Rohit Sharma","Virat Kohli","Kieron Pollard","David Warner","Suresh Raina","Shane Watson","Robin Uthappa"])
plt.xlabel("Strike Rate")
plt.ylabel("Number of sixes")
plt.title("IPL: Strike Rate vs Number of sixes for the top 10 players")
plt.savefig('12.png')
plt.show()