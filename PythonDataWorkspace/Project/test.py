import pandas as pd
import matplotlib
import matplotlib.pyplot as plt

matplotlib.rcParams['font.family'] = 'Malgun Gothic'
matplotlib.rcParams['font.size'] = 15 # 글자크기
matplotlib.rcParams['axes.unicode_minus']=False

filename = r'C:\Private_Projects\nadocoding\PythonDataWorkspace\Project\142801_20230511105324699_excel.xlsx'
df = pd.read_excel(filename, skiprows=2, nrows=2,index_col=0)
df.rename(index={'출생아\xa0수': '출생아 수', '합계\xa0출산율': '합계 출산율'}, inplace=True)
df = df.T
index_str = df.index.astype(str)

fig, ax1 = plt.subplots()

ax1.set_xlabel("년도")
ax1.set_ylabel("출생아 수")
ax1.plot(df.index.astype(str), df['출생아 수'], label='출생아 수', color='b')
ax1.tick_params(axis='y', labelcolor='b')

ax2 = ax1.twinx()  # 축을 공유하는 두 번째 그래프를 생성합니다

ax2.set_ylabel("합계 출산율")
ax2.plot(df.index.astype(str), df['합계 출산율'], label='합계 출산율', color='r')
ax2.tick_params(axis='y', labelcolor='r')

fig.legend(loc='upper left', bbox_to_anchor=(0.15, 1), fontsize=12)
plt.show()

