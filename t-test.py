

import kaggle

import pandas as pd
import scipy.stats as stats

kaggle.api.authenticate()
kaggle.api.dataset_download_files('uciml/student-alcohol-consumption', path='data', unzip=True)

data = pd.read_csv('data/student-mat.csv')
print('data의 크기:', data.shape)
print(data.head()) # dataframe의 처음 5개 행만 출력

exam = data[['sex', 'G1', 'G2','G3']] # 성별, 성적 데이터만 추출

# t-test를 위해 남성 여성 구분하여 새로운 변수에 저장
male = exam[exam['sex']=='M']
female = exam[exam['sex']=='F']

# descript() 남, 여학생 성적결과에 대한 평균과 표준편차값만 확인 

# 남학생 성적에 대한 기술통계값
print(male.describe()) 
# 여학생 성적에 대한 기술통계값
# print(female.describe())

# spicy.stats.ttest_ind() 함수를 사용하여 t-test를 수행 (독립표본 T검정, Independent samples T-test)
# 총 3개 시험(G1, G2, G3)에 대해 남학생, 여학생의 평균 점수 차이가 통계적으로 유의미한지 확인

print('G1에 대한 t-test 결과:', stats.ttest_ind(male['G1'], female['G1'], equal_var=True))
print('G2에 대한 t-test 결과:', stats.ttest_ind(male['G2'], female['G2'], equal_var=True))
print('G3에 대한 t-test 결과:', stats.ttest_ind(male['G3'], female['G3'], equal_var=True))


"""
- statistic: t-test 통계량
  - t-통계량 = (남학생 평균 - 여학생 평균) / sqrt((남학생 분산/남학생 수) + (여학생 분산/여학생 수)) 
  - 두 집단 간 평균의 차이를 표준오차로 나눈 값
  - 집단 간평균 차이가 무작위 변동(variation)에 의해 발생할 가능성이 얼마나 적은지를 나타냄
  - t-통계량의 절대값이 클수록 두 집단의 평균 차이가 크다는 것을 의미 & 두 집단 간 차이가 통계적으로 유의미한 것
- pvalue: t-test의 p-value
  - p값은 귀무가설(두 집단의 평균이 같다)이 참일 때, 관측된 통계량 또는 더 극단적인 통계량이 나올 확률
  - p값이 작을 수록 귀무가설이 거짓일 가능성이 높음
  - p값이 클 수록 두 집단 간 차이가 통계적으로 유의미하지 않다는 것을 의미
  - 일반적으로 p값이 0.05미만일 경우 귀무가설을 기각하고 두 집단 간 차이가 통계적으로 유의미하다고 판단

- df = degree of freedom (자유도)
  - 
"""