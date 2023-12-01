import numpy as np
import pandas as pd
from matplotlib import pyplot as plt
import matplotlib.patches as patches
data=pd.read_csv("ml.csv")


def historgram(data):
    playlist_genres = data['playlist_genre']
    # Đếm số lần xuất hiện của từng thể loại
    genre_counts = playlist_genres.value_counts()

    # Chuẩn bị dữ liệu cho biểu đồ
    labels, data = genre_counts.index, genre_counts.values

    # Vẽ biểu đồ histogram
    for label, count in zip(labels, data):
        plt.bar(label, count, width=0.4,color="blue")
        plt.text(label,count,str(count),ha='center' ,va='bottom')
    # plt.bar(labels, data)

    # Đặt tên cho trục x và y và tiêu đề biểu đồ
    plt.xlabel('Thể loại nhạc')
    plt.ylabel('Số lần xuất hiện')
    plt.title('Biểu đồ tần suất thể laoij nhạc')

    #  chỉnh kích thước 
    plt.bar(labels, data, width=0.5)
    # Hiển thị biểu đồ
    plt.show()

def doughnut(data):
    playlist_genres = data['playlist_genre']

    # Đếm số lần xuất hiện của từng thể loại
    genre_counts = playlist_genres.value_counts()

    # Tạo đối tượng biểu đồ
    fig, ax = plt.subplots(figsize=(10, 10))

    # Hình tròn ngoài biểu thị số lần xuất hiện của thể loại
    ax.pie(genre_counts, labels=genre_counts.index, autopct='%1.1f%%', startangle=90, radius=1, wedgeprops=dict(width=0.3))

    # Hình tròn trong biểu thị tỉ lệ phần trăm
    inner_circle = patches.Circle((0, 0), 0.7, color='white')
    ax.add_patch(inner_circle)

    # Đặt tên cho biểu đồ
    plt.title('Biểu đồ Doughnut tỉ lệ phần trăm thể loại nhạc trong các playlist')

    # Hiển thị biểu đồ
    plt.show()

def line(data):
    # Chuyển cột 'track_album_release_date' sang định dạng datetime để trích xuất thông tin năm
    data['track_album_release_date'] = pd.to_datetime(data['track_album_release_date'])
    data['release_year'] = data['track_album_release_date'].dt.year

    # Đếm số lượng bài hát phát hành theo từng năm
    songs_per_year = data['release_year'].value_counts().sort_index()

    # Tạo đối tượng biểu đồ đường
    plt.figure(figsize=(10, 6))
    plt.plot(songs_per_year.index, songs_per_year.values, marker='o', linestyle='-', color='b')

    # Đặt tên cho trục x và y và tiêu đề biểu đồ
    plt.xlabel('Năm')
    plt.ylabel('Số lượng bài hát')
    plt.title('Biểu đồ đường số lượng bài hát phát hành theo từng năm')

    # Hiển thị biểu đồ
    plt.show()

def tron(data):
    playlist_genres = data['playlist_genre']

    # Đếm số lần xuất hiện của từng thể loại
    genre_counts = playlist_genres.value_counts()

    # Tạo đối tượng biểu đồ
    plt.figure(figsize=(10, 10))

    # Vẽ biểu đồ tròn
    plt.pie(genre_counts, labels=genre_counts.index, autopct='%1.1f%%', startangle=90)

    # Đặt tên cho biểu đồ
    plt.title('Biểu đồ Tròn với số lần xuất hiện của từng thể loại')

    # Hiển thị biểu đồ
    plt.show()

tron(data)