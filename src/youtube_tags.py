import pandas as pd

# 1. 원본 데이터 불러오기
df = pd.read_csv("youtube video trend.csv")

# 2. 결측치 처리 (태그가 없는 경우 빈 문자열로 변환)
df['tags'] = df['tags'].fillna("")

# 3. 태그 개수 계산
# tags가 "tag1|tag2|tag3" 이런 형태라고 가정
df['tag_count'] = df['tags'].apply(lambda x: 0 if x == "" else len(x.split('|')))

# 4. title_length도 함께 계산 (Q2 연계)
df['title_length'] = df['title'].astype(str).apply(len)

# 5. 필요한 컬럼만 정리 (선택사항)
# df = df[['title', 'views', 'tag_count', 'title_length', 'category', 'publishedAt']]

# 6. 새로운 파일로 저장 (Tableau용)
df.to_csv("youtube_tags.csv", index=False)


