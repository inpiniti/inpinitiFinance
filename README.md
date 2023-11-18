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
            code symbolCode        name
0   KR7270520000    A270520      지오릿에너지
1   KR7180060006    A180060          탑선
2   KR7095910006    A095910       에스에너지
3   KR7278990007    A278990         EMB
4   KR7148140007    A148140        비디아이
5   KR7099220006    A099220         SDN
6   KR7126720002    A126720     수산인더스트리
7   KR7083650002    A083650      비에이치아이
8   KR7379390008    A379390      이성씨엔아이
9   KR7046120002    A046120        오르비텍
10  KR7043200005    A043200          파루
11  KR7389260001    A389260       대명에너지
12  KR7060900008    A060900         DGP
13  KR7005090006    A005090      SGC에너지
14  KR7322000001    A322000  HD현대에너지솔루션
15  KR7137950002    A137950      제이씨케미칼
16  KR7044490001    A044490          태웅
17  KR7013810007    A013810         스페코
18  KR7018000000    A018000         유니슨
19  KR7313760001    A313760         윌링스
20  KR7112610001    A112610       씨에스윈드
21  KR7294630009    A294630          서남
22  KR7282720002    A282720      금양그린파워
23  KR7009830001    A009830       한화솔루션
24  KR7038870002    A038870       에코바이오
25  KR7224760009    A224760      엔에스컴퍼니
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
