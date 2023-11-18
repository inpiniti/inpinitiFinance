# inpiniti finance

본 모듈은 Dart 전자공시시스템에서 재무정보와
KRX 정보데이터시스템에서 개별종목 시세 추이 그리고
Daum 에서 섹터정보 및 종목정보를 조회하는 라이브러리입니다.

API 사용에 대한 책임은 사용자 본인에게 있으며, 도의적으로 무분별한 호출을 자제해 주시기 부탁드립니다. 또한 결과물은 참고용으로만 사용하셔야 하며, 투자에 대한 책임은 사용자에게 있습니다.

## 환경설정

### 1. 설치

```
pip install inpinitiFinance
```

### 2. import

```
import ifinance as dt
```

### 3. dart api key 설정

dart 를 이용하시려면 dart에서 생성한 api_key 를 지정해주셔야 합니다.

```
api_key = 'your_api_key_here'

dt.set_api_key(api_key)
```

### 4. 재무재표 정보 가져오기

```
df = dt.get_financial_dataframe('005930')
print(df)
```

### 5. 섹터 정보 가져오기

```
df = dt.get_sector_dataframe()
print(df)
```

```
   sectorCode    sectorName
0     G101010  에너지 장비 및 서비스
1     G101020        석유와 가스
2     G151010            화학
3     G151030           포장재
4     G151040          비철금속
..        ...           ...
82    G502010            광고
83    G502020     방송과엔터테인먼트
84    G502030            출판
85    G502040      게임엔터테인먼트
86    G502050    양방향미디어와서비스
```

### 6. 종목정보 가져오기

```
df = dt.get_stock_dataframe('G101010')
print(df)
```

```
   sectorCode    sectorName
0     G101010  에너지 장비 및 서비스
1     G101020        석유와 가스
2     G151010            화학
3     G151030           포장재
4     G151040          비철금속
..        ...           ...
82    G502010            광고
83    G502020     방송과엔터테인먼트
84    G502030            출판
85    G502040      게임엔터테인먼트
86    G502050    양방향미디어와서비스
```

### 7. 월 종가 정보 가져오기

```
df = dt.get_monthly_stock_dataframe('KR7005930003')
print(df)
```

```
    isu_abbrv isu_srt_cd mkt_nm  ...  mmend_clsprc_change_9 mmend_clsprc_change_12 next_mmend_clsprc_change
0        삼성전자     005930  KOSPI  ...                    NaN                    NaN                -0.586081
1        삼성전자     005930  KOSPI  ...                    NaN                    NaN                 6.190125
2        삼성전자     005930  KOSPI  ...                    NaN                    NaN                -2.151284
3        삼성전자     005930  KOSPI  ...               3.296703                    NaN                -7.304965
4        삼성전자     005930  KOSPI  ...              -3.684598              -4.249084                -2.983933
..        ...        ...    ...  ...                    ...                    ...                      ...
102      삼성전자     005930  KOSPI  ...               6.564885               9.062500                -4.154728
103      삼성전자     005930  KOSPI  ...              -6.302521               2.137405                 2.242152
104      삼성전자     005930  KOSPI  ...              -5.263158              -4.201681                -2.192982
105      삼성전자     005930  KOSPI  ...              -4.154728              -7.340720                 8.370703
106      삼성전자     005930  KOSPI  ...               8.370703               3.868195                      NaN
```
