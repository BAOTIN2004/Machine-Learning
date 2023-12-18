import numpy as np
import pandas as pd
from matplotlib import pyplot as plt
import matplotlib.patches as patches
data=pd.read_csv("ml.csv")

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

def vung(data):
    # Đếm số lặp lại của các phần tử trong cột 'playlist_subgenre'

    subgenre_counts = df['playlist_subgenre'].value_counts()

    # Tạo một biểu đồ diện tích với track_popularity và duration_ms
    plt.figure(figsize=(10, 6))

    # Biểu đồ diện tích cho track_popularity
    plt.fill_between(df.index, df['track_popularity'], label='Độ Phổ Biến', color='red', alpha=0.4)

    # Biểu đồ diện tích cho duration_ms
    plt.fill_between(df.index, df['duration_ms'], label='Thời Lượng (ms)', color='orange', alpha=0.4)

    # Đặt tên trục và tiêu đề biểu đồ
    plt.xlabel("Chỉ số Bài Hát")
    plt.ylabel("Giá Trị")
    plt.title("So Sánh Độ Phổ Biến và Thời Lượng của Bài Hát")
    plt.legend()

    # Hiển thị biểu đồ
    plt.show()

def matdo(data):
    # Thiết lập kiểu của seaborn
    sns.set(style="whitegrid")

    # Tạo subplot
    plt.figure(figsize=(12, 8))

    # Tạo đồ thị mật độ cho cột 'track_popularity'
    sns.kdeplot(data=df, x='track_popularity', fill=True, common_norm=False, palette="crest")

    # Đặt tiêu đề và nhãn
    plt.title('Đồ Thị Mật Độ của Độ Phổ Biến Bài Hát', fontsize=16)
    plt.xlabel('Độ Phổ Biến Bài Hát', fontsize=14)
    plt.ylabel('Mật Độ', fontsize=14)

    # Hiển thị đồ thị
    plt.show()

def cot(data):
    # Chọn cột chứa dữ liệu bạn muốn vẽ biểu đồ
    column_to_plot = 'track_popularity'  # Thay 'track_popularity' bằng tên cột chứa dữ liệu bài hát

    # Chọn 15 dòng đầu tiên
    df_subset = df.head(15)

    # Vẽ biểu đồ cột
    plt.figure(figsize=(12, 6))
    plt.bar(df_subset.index, df_subset[column_to_plot], color='skyblue')
    plt.title('Biểu đồ cột về dữ liệu bài hát từ file Excel (15 dòng đầu tiên)')
    plt.xlabel('Thể loại bài hát')
    plt.ylabel('Độ phổ biến')
    plt.xticks(df_subset.index, df_subset['playlist_genre'], rotation=45, ha='right')  # Sử dụng tên thể loại bài hát làm nhãn trục x

    # Thêm số liệu lên trục y
    for i, value in enumerate(df_subset[column_to_plot]):
        plt.text(i, value + 0.1, str(value), ha='center', va='bottom')

    plt.show()

def bubble(data):
    # Tạo biểu đồ Bubble
    plt.figure(figsize=(12, 8))
    scatter = plt.scatter(df['danceability'], df['energy'], s=df['track_popularity']*10, c=df['track_popularity'], cmap='viridis', alpha=0.8)

    # Đặt tiêu đề và nhãn
    plt.title('Biểu Đồ Bubble Danceability và Energy với Độ Phổ Biến Bài Hát', fontsize=16)
    plt.xlabel('Danceability', fontsize=14)
    plt.ylabel('Energy', fontsize=14)

    # Thêm colorbar để hiển thị độ phổ biến
    cbar = plt.colorbar(scatter)
    cbar.set_label('Track Popularity', rotation=270, labelpad=15)

    # Hiển thị đồ thị
    plt.show()
