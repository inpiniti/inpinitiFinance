import ifinance
import pandas as pd

pd.set_option('display.max_columns', None)
pd.set_option('display.max_rows', None)

# 양방향미디어와서비스 조회
df = ifinance.get_stock_dataframe('G502050')

# print(df)
# 0   KR7089230007    A089230  THE E&M
# 1   KR7134580000    A134580    탑코미디어
# 2   KR7417180007    A417180    핑거스토리
# 3   KR7067160002    A067160   아프리카TV
# 4   KR7057680001    A057680   티사이언티픽
# 5   KR7035420009    A035420    NAVER <<
# 6   KR7317530004    A317530    캐리소프트
# 7   KR7035720002    A035720      카카오 <<
# 8   KR7408920007    A408920     메쎄이상
# 9   KR7202960001    A202960    판도라티비
# 10  KR7300080009    A300080      플리토
# 11  KR7207760000    A207760    미스터블루
# 12  KR7020120002    A020120  키다리스튜디오
# 13  KR7289220006    A289220   자이언트스텝
# 14  KR7239340003    A239340     줌인터넷
# 15  KR7214270001    A214270      FSN
# 16  KR7376300000    A376300      디어유
# 17  KR7443250006    A443250  레뷰코퍼레이션

samsung = ifinance.get_monthly_stock_dataframe('KR7005930003')
naver = ifinance.get_monthly_stock_dataframe('KR7035420009')
kakao = ifinance.get_monthly_stock_dataframe('KR7035720002')

# samsung, naver, kakao 데이터프레임을 병합
merged = pd.concat([samsung, naver, kakao])

print(merged)

# 딥러닝 모델 생성
model = ifinance.ai.deep_learning(samsung)

# 2023.09 날짜 데이터 가져와서 
selected_data_ = merged[(merged['year'] == '2023') & (merged['month'] == '09')]

# 2023.12 예측
# 제거 isu_abbrv isu_srt_cd mkt_nm
selected_data = selected_data_.drop(['isu_abbrv', 'isu_srt_cd', 'mkt_nm', 'next_mmend_clsprc_change'], axis=1)

# float 타입으로 변환
selected_data = selected_data.astype('float32')

# 생성한 딥러닝 모델로 예측
predicted_data = model.predict(selected_data)

for isu_abbrv, prediction in zip(selected_data_['isu_abbrv'], predicted_data):
    print(f"{isu_abbrv}: {prediction[0]}")

# 삼성전자: -2800.45556640625
# NAVER: -8107.1904296875
# 카카오: -1882.025390625