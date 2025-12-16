import pandas as pd

# 1) 데이터 불러오기
df = pd.read_csv("youtube_video_trend.csv", low_memory=False)

# 2) 업로드 시간 컬럼 변환: publishedAt → datetime
df['publish_time'] = pd.to_datetime(df['publishedAt'], errors='coerce')

# 변환이 잘 되었는지 체크 (null이 너무 많으면 문제)
print("Datetime 변환 후 null 개수:", df['publish_time'].isna().sum())

# 3) 요일 / 시간대 컬럼 생성
df['weekday'] = df['publish_time'].dt.day_name()     # Monday, Tuesday ...
df['hour'] = df['publish_time'].dt.hour              # 0~23시

# 4) 요일 순서 정렬
weekday_order = ['Monday','Tuesday','Wednesday','Thursday','Friday','Saturday','Sunday']
df['weekday'] = pd.Categorical(df['weekday'], categories=weekday_order, ordered=True)

# 5) 요일 & 시간대별 조회수 평균 계산
weekday_views = df.groupby('weekday')['view_count'].mean().reset_index()
hour_views = df.groupby('hour')['view_count'].mean().reset_index()

# 6) CSV로 저장
df.to_csv("youtube_time_processed.csv", index=False)
weekday_views.to_csv("youtube_weekday_avg.csv", index=False)
hour_views.to_csv("youtube_hour_avg.csv", index=False)

