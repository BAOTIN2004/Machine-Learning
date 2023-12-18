from matplotlib import pyplot as plt
import numpy as np, pandas as pd
import seaborn as sns
import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots
data=pd.read_csv('Top Football Leagues Scorers(2016-2020).csv')

def histogram_chart(data):
    fig,ax = plt.subplots(1,1)
    a=data[data['Year']==2018]
    b= a['xG Per Avg Match'] 
    bins = [0, 0.2, 0.4, 0.6, 0.8, 1]
    counts, bins, patches = ax.hist(b, bins=[0, 0.2, 0.4, 0.6, 0.8, 1], edgecolor='black')
    # ax.hist(b, bins = [0,0.2,0.4,0.6,0.8,1], edgecolor='black',)
    ax.set_title("Tần suất tỉ lệ bàn thắng kì vọng trung bình mỗi trận trong năm 2018",fontsize=26,fontweight='bold')
    ax.set_xticks([0,0.2,0.4,0.6,0.8,1])
    ax.set_xlabel('Tỉ lệ bàn thắng kì vọng',fontsize=22)
    ax.set_ylabel('Số lượng',fontsize=22)
    for count, bin_edge in zip(counts, bins):
        if count > 0:
            ax.text(bin_edge + 0.1, count, str(count), ha='center', va='bottom')
    plt.show()

def doughnut_chart(sizes,text,colors,labels,values,year,radius=1):
    # du lieu 2016 
    col = [[i/255 for i in c] for c in colors]
    plt.axis('equal')
    width = 0.35
    kwargs = dict(colors=col, startangle=180)
    outside, _ = plt.pie(sizes, radius=radius, pctdistance=1-width/2,labels=None,**kwargs)
    plt.setp( outside, width=width, edgecolor='white')

    kwargs = dict(size=20, fontweight='bold', va='center')
    plt.text(0, 0, text, ha='center', **kwargs)
    
    plt.title('Đóng góp trong tổng số bàn thắng của ba giải đấu được so sánh với nhau trong năm 2016 & 2017',y=1.08,fontsize=22)
    plt.legend(labels=["La Liga", "Serie A", "Bundesliga"], title='Tên giải', loc='upper right',fontsize=22)
    annotation_text = 'Năm 2017' if year == 2017 else 'Năm 2016'
    annotation_xy = (1.25*radius,0) if year == 2017 else (0,0)
    plt.annotate(annotation_text, annotation_xy, ha='center', fontsize=14, fontweight='bold', color='black')

laliga_2016 = data[(data['League'] == 'La Liga') & (data['Year'] == 2016)]
serieA_2016 = data[(data['League'] == 'Serie A') & (data['Year'] == 2016)]
bundesliga_2016 = data[(data['League'] == 'Bundesliga') & (data['Year'] == 2016)]
    # du lieu 2017
laliga_2017 = data[(data['League'] == 'La Liga') & (data['Year'] == 2017)]
serieA_2017 = data[(data['League'] == 'Serie A') & (data['Year'] == 2017)]
bundesliga_2017=data[(data['League'] == 'Bundesliga') & (data['Year'] == 2017)]

    # Tính tổng số bàn thắng 2016
goals_laliga_2016 = laliga_2016['Goals'].sum()
goals_serieA_2016=serieA_2016['Goals'].sum()
goals_bundesliga_2016=bundesliga_2016['Goals'].sum()
    # Tính tổng số bàn thắng 2017
goals_laliga_2017 = laliga_2017['Goals'].sum()
goals_serieA_2017=serieA_2017['Goals'].sum()
goals_bundesliga_2017=bundesliga_2017['Goals'].sum()

# Group colors
c1 = (226, 33, 7)
c2 = (60, 121, 189)

# Subgroup colors
d1 = (226, 33, 7)
d2 = (6, 50, 25)
d3 = (60, 121, 189)

colors = [d1,d2,d3]  # Cam, Tím, Xanh nước biển
print(goals_bundesliga_2017)
# 2016
doughnut_chart([310,349,285],"",colors,["La liga","Serie A","Bundesliga"],values=[310,349,285],radius=1,year=2016)
doughnut_chart([334,297,251],"", colors,["La liga","Serie A","Bundesliga"],values=[334,297,251],radius=1.3,year=2017)
#2017

plt.show()


def line_chart(data):
# Lọc dữ liệu cho Cristiano Ronaldo
    ronaldo_data = data[data['Player Names'] == 'Cristiano Ronaldo' ]
# Nhóm dữ liệu theo năm và tính số trận và tổng số phút thi đấu
    games_and_minutes_by_year = ronaldo_data.groupby('Year').agg({'Matches_Played': 'sum', 'Mins': 'sum'})
# Tính số phút thi đấu trung bình mỗi trận
    games_and_minutes_by_year['Average Minutes Per Game'] = games_and_minutes_by_year['Mins'] / games_and_minutes_by_year['Matches_Played']
    plt.figure(figsize=(10, 6))
    plt.plot(games_and_minutes_by_year.index, games_and_minutes_by_year['Average Minutes Per Game'], marker='o', linestyle='-', color='b')
    plt.xlabel('Năm',fontsize=18)
    plt.ylabel('Số phút',fontsize=18)
    plt.title('Số phút thi đấu trung bình mỗi trận của Cristiano Ronaldo qua các năm',fontsize=22,fontweight='bold')
    plt.xticks([year for year in games_and_minutes_by_year.index if isinstance(year, int)])
    for year, value in zip(games_and_minutes_by_year.index, games_and_minutes_by_year['Average Minutes Per Game']):
        plt.text(year, value, f'{value:.2f}', ha='right', va='bottom')
        plt.yticks(np.arange(85, 96, 2))
    plt.ylim(85, 96)
    plt.show()