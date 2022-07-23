import pandas as pd
import numpy as np
from wordcloud import WordCloud
import matplotlib.pyplot as plt
from PIL import Image
import operator

df = pd.read_excel('../source/mt_100_3.xlsx')

# 빈칸을 기준으로 리스트 요소 만들기
list1 = []
list2 = []

for i in range(100):
    list1.append(df.loc[i][1])
    list2.append(df.loc[i][3])


count = [0]*100

for j in range(100):
    reason = str(list1[j])
    word1 = reason.find('여름')
    word2 = reason.find('계곡')
    word3 = reason.find('폭포')
    word4 = reason.find('동굴')
    word5 = reason.find('얼음')
    word6 = reason.find('6월')
    word7 = reason.find('7월')
    word8 = reason.find('8월')

    if word1 >= 0: count[j] += 1
    if word2 >= 0: count[j] += 1
    if word3 >= 0: count[j] += 1
    if word4 >= 0: count[j] += 1
    if word5 >= 0: count[j] += 1
    if word6 >= 0: count[j] += 1
    if word7 >= 0: count[j] += 1
    if word8 >= 0: count[j] += 1

for j in range(100):
    reason = str(list2[j])
    word1 = reason.find('여름')
    word2 = reason.find('계곡')
    word3 = reason.find('폭포')
    word4 = reason.find('동굴')
    word5 = reason.find('얼음')
    word6 = reason.find('6월')
    word7 = reason.find('7월')
    word7 = reason.find('8월')

    if word1 >= 0: count[j] += 1
    if word2 >= 0: count[j] += 1
    if word3 >= 0: count[j] += 1
    if word4 >= 0: count[j] += 1
    if word5 >= 0: count[j] += 1
    if word6 >= 0: count[j] += 1
    if word7 >= 0: count[j] += 1
    if word7 >= 0: count[j] += 1

print(count)

res = dict()
for i in range(100):
    mt_name = str(df.loc[i][6])
    res[mt_name] = int((count[i]) * 500)



masking_img = np.array(Image.open('wc_mt1.png'))
cloud = WordCloud(font_path='Goyang.ttf',
                  max_font_size=80,
                  mask=masking_img,
                  background_color='white').fit_words(res)

cloud.to_file('result.png')

plt.imshow(cloud, interpolation='bilinear')
plt.axis('off')
plt.show()

for i in range(5):
    max_mt = max(res.items(), key=operator.itemgetter(1))[0]
    print(max_mt)
    res.pop(max_mt)

