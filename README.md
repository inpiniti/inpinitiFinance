# inpiniti finance

![version](https://img.shields.io/badge/version-1.0.1-blue)
![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)
![Dependencies](https://img.shields.io/badge/Dependencies-OpenDartReader-green.svg)
![Dependencies](https://img.shields.io/badge/Dependencies-pandas-green.svg)
![Dependencies](https://img.shields.io/badge/Dependencies-requests-green.svg)
![Dependencies](https://img.shields.io/badge/Dependencies-sklearn-green.svg)
![Dependencies](https://img.shields.io/badge/Dependencies-keras-green.svg)

본 모듈은 Dart 전자공시시스템에서 재무정보,
KRX 정보데이터시스템에서 개별종목 시세 추이,
Daum 에서 섹터정보 종목정보 등을 크롤링하여 데이터를 dataframe 제공해주는 라이브러리입니다.

API 사용에 대한 책임은 사용자 본인에게 있으며, 도의적으로 무분별한 호출을 자제해 주시기 부탁드립니다. 또한 결과물은 참고용으로만 사용하셔야 하며, 투자에 대한 책임은 사용자에게 있습니다.

## 환경설정

### 1. 설치

```
pip install inpinitiFinance
```

### 2. import

```
import ifinance
```

### 3. dart api key 설정

dart 를 이용하시려면 dart에서 생성한 api_key 를 지정해주셔야 합니다.

```
api_key = 'your_api_key_here'

ifinance.set_api_key(api_key)
```

### 4. 재무재표 정보 가져오기

```
df = ifinance.get_financial_dataframe('005930')
print(df)
```

### 5. 섹터 정보 가져오기

```
df = ifinance.get_sector_dataframe()
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
df = ifinance.get_stock_dataframe('G101010')
print(df)
```

```
            code symbolCode        name        date  tradePrice       change  changePrice  changeRate  accTradePrice  accTradeVolume     marketCap foreignRatio
0   KR7270520000    A270520      지오릿에너지  2023-11-17      2880.0         RISE         80.0    0.028571   3.138572e+09         1064248  1.202760e+11        4.000
1   KR7180060006    A180060          탑선  2023-11-17      9190.0         RISE        190.0    0.021111   9.190000e+03               1  8.590505e+10        0.000
2   KR7095910006    A095910       에스에너지  2023-11-17      1889.0         RISE          4.0    0.002122   8.710130e+07           46229  3.684401e+10        1.770
3   KR7278990007    A278990         EMB  2023-11-17     11500.0         RISE         10.0    0.000870   2.905000e+06             255  5.423347e+10        0.000
4   KR7148140007    A148140        비디아이  2023-11-17       640.0         EVEN          0.0    0.000000   0.000000e+00               0  2.765355e+10        0.540
5   KR7099220006    A099220         SDN  2023-11-17      1225.0         FALL          2.0    0.001630   9.027009e+07           74213  6.881047e+10        1.930
6   KR7126720002    A126720     수산인더스트리  2023-11-17     19010.0         FALL        150.0    0.007829   2.941202e+08           15460  2.715769e+11        0.700
7   KR7083650002    A083650      비에이치아이  2023-11-17      7040.0         FALL         60.0    0.008451   7.866034e+08          111973  2.178484e+11        0.910
8   KR7379390008    A379390      이성씨엔아이  2023-11-17      8990.0         FALL         80.0    0.008820   0.000000e+00               0  2.554473e+10        0.000
9   KR7046120002    A046120        오르비텍  2023-11-17      3330.0         FALL         55.0    0.016248   5.006091e+08          150541  9.013918e+10        2.880
10  KR7043200005    A043200          파루  2023-11-17       696.0         FALL         12.0    0.016949   1.986788e+08          280970  2.909580e+10        0.430
11  KR7389260001    A389260       대명에너지  2023-11-17     15460.0         FALL        300.0    0.019036   2.675089e+08           17296  2.635930e+11        0.960
12  KR7060900008    A060900         DGP  2023-11-17      1759.0         FALL         36.0    0.020056   1.153163e+08           65833  4.442922e+10        3.240
13  KR7005090006    A005090      SGC에너지  2023-11-17     28300.0         FALL        600.0    0.020761   1.187380e+09           41615  4.077841e+11        5.320
14  KR7322000001    A322000  HD현대에너지솔루션  2023-11-17     23550.0         FALL        500.0    0.020790   6.214132e+08           26430  2.637600e+11        8.760
15  KR7137950002    A137950      제이씨케미칼  2023-11-17      6690.0         FALL        190.0    0.027616   6.619587e+08           98360  1.489717e+11        2.370
16  KR7044490001    A044490          태웅  2023-11-17     15730.0         FALL        460.0    0.028413   1.678214e+09          106263  3.147161e+11        4.310
17  KR7013810007    A013810         스페코  2023-11-17      3310.0         FALL        105.0    0.030747   4.614688e+08          138538  4.850961e+10        1.610
18  KR7018000000    A018000         유니슨  2023-11-17      1193.0         FALL         41.0    0.033225   2.450125e+08          206253  1.506735e+11        1.790
19  KR7313760001    A313760         윌링스  2023-11-17      7610.0         FALL        270.0    0.034264   5.500667e+08           71269  4.405338e+10        0.690
20  KR7112610001    A112610       씨에스윈드  2023-11-17     48850.0         FALL       1750.0    0.034585   1.111761e+10          225791  2.060073e+12       11.920
21  KR7294630009    A294630          서남  2023-11-17      3885.0         FALL        150.0    0.037175   3.971054e+09         1027964  9.144691e+10        1.330
22  KR7282720002    A282720      금양그린파워  2023-11-17     12240.0         FALL        480.0    0.037736   6.773848e+08           54996  1.483427e+11        0.590
23  KR7009830001    A009830       한화솔루션  2023-11-17     31750.0         FALL       1250.0    0.037879   2.479295e+10          774867  5.457588e+12       23.180
24  KR7038870002    A038870       에코바이오  2023-11-17      5610.0         FALL        320.0    0.053963   2.450061e+09          428549  7.642201e+10        1.710
25  KR7224760009    A224760      엔에스컴퍼니  2023-11-17      4760.0  LOWER_LIMIT        830.0    0.148479   2.564000e+04               5  1.875297e+10        0.000
```

### 7. 월 종가 정보 가져오기

```
df = ifinance.get_monthly_stock_dataframe('KR7005930003')
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

# 8. 딥러닝

8번 부터는 위에서 조회한 데이터를 가지고 학습을 시켜 모델을 만드는 함수입니다.
모델로 부터 예측하고자 하면 `predict()` 이라는 함수로 예측을 하시면 됩니다.

```
model = ifinance.ai.deep_learning(df)
```

```
Epoch 1/10
3/3 [==============================] - 0s 2ms/step - loss: 706845312.0000
Epoch 2/10
3/3 [==============================] - 0s 580us/step - loss: 450014688.0000
Epoch 3/10
3/3 [==============================] - 0s 688us/step - loss: 281121024.0000
Epoch 4/10
3/3 [==============================] - 0s 552us/step - loss: 125484616.0000
Epoch 5/10
3/3 [==============================] - 0s 530us/step - loss: 189583840.0000
Epoch 6/10
3/3 [==============================] - 0s 546us/step - loss: 88214128.0000
Epoch 7/10
3/3 [==============================] - 0s 466us/step - loss: 67864080.0000
Epoch 8/10
3/3 [==============================] - 0s 483us/step - loss: 52074252.0000
Epoch 9/10
3/3 [==============================] - 0s 695us/step - loss: 29803728.0000
Epoch 10/10
3/3 [==============================] - 0s 641us/step - loss: 35682296.0000
1/1 [==============================] - 0s 31ms/step
Deep Learning MSE: 4770194.0000
```

# 9. Linear Regression

```
model = ifinance.ai.regressor(df)
```

```
LinearRegression MSE: 87.4084
```

# 10. Ridge Regression

```
model = ifinance.ai.ridge(df)
```

```
Ridge Regression MSE: 87.3161
```

# 11. Lasso Regression

```
model = ifinance.ai.lasso(df)
```

```
Lasso Regression MSE: 76.6489
```

# 12. ElasticNet Regression

```
model = ifinance.ai.elastic_net(df)
```

```
Elastic Net Regression MSE: 79.1272
```

# 13. Desicion Tree Regression

```
model = ifinance.ai.decision_tree(df)
```

```
Decision Tree Regression MSE: 475.2224
```

# 14. random_forest

```
model = ifinance.ai.random_forest(df)
```

```
Random Forest Regression MSE: 200.4157
```
