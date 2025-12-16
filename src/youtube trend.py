import pandas as pd

df = pd.read_csv("youtube video trend.csv", low_memory=False)

# 날짜 변환
df['publishedAt'] = pd.to_datetime(df['publishedAt'], errors='coerce')

# 파생 변수 생성
df['title_length'] = df['title'].astype(str).apply(len)
df['tags_count'] = df['tags'].astype(str).apply(
    lambda x: len(x.split(',')) if x != 'nan' else 0
)
df['publish_weekday'] = df['publishedAt'].dt.day_name()
df['publish_hour'] = df['publishedAt'].dt.hour

# 카테고리 매핑 (네가 쓰던 것 그대로)
category_map = {
    1: "Film & Animation",
    2: "Autos & Vehicles",
    10: "Music",
    15: "Pets & Animals",
    17: "Sports",
    19: "Travel & Events",
    20: "Gaming",
    22: "People & Blogs",
    23: "Comedy",
    24: "Entertainment",
    25: "News & Politics",
    26: "Howto & Style",
    27: "Education",
    28: "Science & Technology",
    29: "Nonprofits & Activism",
    30: "Movies"
}
df["category_name"] = df["categoryId"].map(category_map)

analysis_df = df[[
    "title",
    "title_length",
    "view_count",     # view_count로 수정
    "category_name"   # category_name으로 수정
]]

# Tableau로 넘길 csv 저장
analysis_df.to_csv("youtube_title_length_analysis.csv", index=False)
df['title_length'].corr(df['views'])
