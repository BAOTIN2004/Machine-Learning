from matplotlib import pyplot as plt
import numpy as np, pandas as pd
import seaborn as sns
import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots
data=pd.read_csv('Top Football Leagues Scorers(2016-2020).csv')

# allTimeTopTen = data["job_title"].value_counts().nlargest(10).reset_index()
# sns.barplot(x=allTimeTopTen["job_title"], y=allTimeTopTen["index"])
# plt.title("Top 10 công việc Data Scicence phổ biến nhất")
# plt.xlabel("Count")
# plt.ylabel("Job Title")
# plt.show()
# a=data[(data['Country']=='Spain') & (data['Year']==2016)]
# 

# a=data.groupby(['League'])['Year'].value_counts()

a=data['OnTarget'].value_counts()
print(a)
def histogram_chart(data):
    # goals_CR7=data[(data['Player Names']=='Cristiano Ronaldo') ]
    # a=goals_CR7['Goals']
    # b=[2016,2017,2018,2019]
    # fig,ax = plt.subplots(1,1)
    # ax.hist(a,bins=b)
    # plt.show()\
     # a=data[(data['Country']=='Spain') & (data['Year']==2019)]
    fig,ax = plt.subplots(1,1)
    a=data[data['Year']==2018]
    b= a['xG Per Avg Match'] 
    bins = [0, 0.2, 0.4, 0.6, 0.8, 1]
    counts, bins, patches = ax.hist(b, bins=[0, 0.2, 0.4, 0.6, 0.8, 1], edgecolor='black')
    # ax.hist(b, bins = [0,0.2,0.4,0.6,0.8,1], edgecolor='black',)
    ax.set_title("Tần suất tỉ lệ bàn thắng kì vọng trong năm 2018",fontsize=22,fontweight='bold')
    ax.set_xticks([0,0.2,0.4,0.6,0.8,1])
    ax.set_xlabel('Tỉ lệ bàn thắng kì vọng',fontsize=18)
    ax.set_ylabel('Số lượng',fontsize=18)
    for count, bin_edge in zip(counts, bins):
        if count > 0:
            ax.text(bin_edge + 0.1, count, str(count), ha='center', va='bottom')
    plt.show()

def doughnut_chart(data):
    pass
    
    # phan tich nam 2016
    # data_2016=data[data['Year']==2016]
    # goals_by_player=data_2016.groupby(['Player Names', 'League'])['Goals'].sum()
    # # Sắp xếp giảm dần và chọn 10 cầu thủ đầu tiên
    # top_10_scorers =  goals_by_player.nlargest(10)
    # print(top_10_scorers)
    # plot=px.sunburst(data_frame=top_10_scorers.reset_index(),
    #                  path=[ 'League','Player Names'],values='Goals',
    #                  title='Top 10 caau thu ghi nhieu ban nhat nam 2016',
    #                  )
    # plot.show()


def line_chart(data):
    
# Đọc dữ liệu từ file CSV


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


