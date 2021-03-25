from matplotlib import pyplot as plt  
import numpy as np
from matplotlib import rc

#Number of matches 
format=['Tests','ODIs','T20Is','First-Class','List A','T20s']
data=[38,225,111,98,296,343]
explode= (0.2,0.1,0,0,0,0)
fig1, ax1 = plt.subplots()
ax1.pie(data, explode=explode, labels=format, autopct='%1.1f%%',
        shadow=True, startangle=90)
ax1.axis('equal') 
plt.title("Rohit Sharma:Number of matches played across formats")
plt.show()

#Number of centuries and half centuries
centuries=[7,29,4,24,32,6]
half_centuries=[12,43,22,32,56,64]
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
plt.show()

#Average
fig = plt.figure()
avg=[46.69,49.15,32.54,55.41,46.46,32.03]
plt.bar(format,avg,color='maroon',width=0.4)
plt.grid(color='b',linestyle='-',linewidth=1)
plt.xlabel("Format")
plt.ylabel("Average")
plt.title("Rohit Sharma: Average across various formats")
plt.show()

#Strike Rate
fig = plt.figure()
avg=[58.41,88.84,138.96,62.84,88.39,133.58]
plt.bar(format,avg,color='orange',width=0.4)
plt.grid(color='b',linestyle='-',linewidth=1)
plt.xlabel("Format")
plt.ylabel("Strike Rate")
plt.title("Rohit Sharma: Strike Rate across various formats")
plt.show()

#Total Runs across formats
x1=[2007,2008,2009,2010,2011,2012,2013,2014,2015,2016,2017,2018,2019,2020]
y1=[0,0,0,0,0,0,333,237,326,288,217,184,556,474]
y2=[61,532,102,504,611,168,1196,578,815,564,1293,1030,1490,171]
y3=[88,8,145,94,80,116,8,200,128,497,279,590,396,140]
plt.plot(x1,y1,marker='o')
plt.plot(x1,y2,marker='o')
plt.plot(x1,y3,marker='o')
plt.grid(color='b',linestyle='-',linewidth=1)
plt.xlabel("Format")
plt.ylabel("Runs")
plt.title("Rohit Sharma:Total runs scored per year across formats")
plt.legend(["Tests","ODIs","T20Is"])
plt.show()

#Runs in all formats across all countries
rc('font', weight='bold')
data=["Australia","Bangladesh","England","India","New Zealand","South Africa","Sri Lanka","West Indies"]
bars1=[408,6,34,1670,122,123,202,50]
bars2=[1328,331,1335,3556,437,256,583,517]
bars3=[181,338,269,1019,236,173,268,110]
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
plt.show()

# Mode of dismissal
way=["Bowled","Caught","Caught Behind","LBW","Stumped","Run Out"]
data=[29,87,36,18,3,13]
explode= (0,0.1,0,0,0.2,0.1)
fig1, ax1 = plt.subplots()
ax1.pie(data, explode=explode, labels=way, autopct='%1.1f%%',
        shadow=True, startangle=90)
ax1.axis('equal') 
plt.title("Rohit Sharma:Mode of dismissal in ODIs")
plt.show()
way=["Bowled","Caught","Caught Behind","LBW","Stumped","Run Out"]
data=[10,23,10,10,3,0]
explode= (0,0.1,0,0,0.2,0.1)
fig1, ax1 = plt.subplots()
ax1.pie(data, explode=explode, labels=way, autopct='%1.1f%%',
        shadow=True, startangle=90)
ax1.axis('equal') 
plt.title("Rohit Sharma:Mode of dismissal in Tests")
plt.show()
way=["Bowled","Caught","Caught Behind","LBW","Stumped","Run Out"]
data=[16,46,9,9,3,5]
explode= (0,0.1,0,0,0.2,0.1)
fig1, ax1 = plt.subplots()
ax1.pie(data, explode=explode, labels=way, autopct='%1.1f%%',
        shadow=True, startangle=90)
ax1.axis('equal') 
plt.title("Rohit Sharma:Mode of dismissal in T20Is")
plt.show()

#Runs against every country
countries=["Afghanistan","Australia","Bangladesh","England","Ireland","New Zealand","Pakistan","South Africa","Sri Lanka","UAE","West Indies","Zimbabwe"]
t20=[1,318,452,317,149,338,70,362,289,39,519,10]
odi=[19,2208,660,482,64,703,720,766,1665,57,1523,242]
tests=[0,408,33,379,0,360,0,678,419,0,338,0]
x = np.arange(len(countries))  # the label locations
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
plt.show()

#Average across batting positions
x1=[2,3,4,5,6,7]
y1=[64.38,21.40,4,29.13,54.58,0]
y2=[57.87,15,31.09,45.37,28.57,14]
y3=[32.93,113,36.20,14.50,36,7]
plt.plot(x1,y1,marker='o')
plt.plot(x1,y2,marker='o')
plt.plot(x1,y3,marker='o')
plt.grid(color='b',linestyle='-',linewidth=1)
plt.xlabel("Batting Position")
plt.ylabel("Average")
plt.title("Rohit Sharma:Average across batting positions")
plt.legend(["Tests","ODIs","T20Is"])
plt.show()

#Home and away runs
format=["Tests","ODIs","T20Is"]
home=[1670,3556,1019]
away=[945,5587,1845]
x = np.arange(len(format))  # the label locations
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
plt.show()

#Home and away centuries
format=["Tests","ODIs","T20Is"]
home=[7,11,3]
away=[0,18,1]
x = np.arange(len(format))  # the label locations
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
plt.show()