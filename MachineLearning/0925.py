
import pandas as pd

path = 'https://github.com/dongupak/DataML/raw/main/csv/'
file = path+'life_expectancy.csv'

life = pd.read_csv(file)
print(life.head(3))

print(life.describe())

import seaborn as sns
import matplotlib.pyplot as plt

#시본 라이브러리의 크기 지정
sns.set(rc={'figure.figsize':(22,20)})
correlation_matrix = life.corr().round(2)
sns.heatmap(data=correlation_matrix, annot=True)