# 标注一致性报告

- 样本数：**1000**
- 标注者：r1, r10, r11, r12, r13, r14, r15, r16, r18, r19, r2, r20 …（共 77 人）
- 类别数：28

## 一、总体一致性

| 指标 | 数值 | 档位 |
|---|---|---|
| Krippendorff's alpha（名义尺度，支持缺标） | 0.2804 | 一般 |
| 95% 置信区间 | [0.257, 0.303] | 1000 次 bootstrap |

> 1000 条样本，区间宽度 0.05。**方向可信（明显高于随机水平），但具体数值需谨慎看待。**

### 标注覆盖

| 标注者 | 标注条数 | 覆盖率 |
|---|---|---|
| r1 | 27 / 1000 | 3% |
| r10 | 15 / 1000 | 2% |
| r11 | 33 / 1000 | 3% |
| r12 | 51 / 1000 | 5% |
| r13 | 3 / 1000 | 0% |
| r14 | 7 / 1000 | 1% |
| r15 | 49 / 1000 | 5% |
| r16 | 63 / 1000 | 6% |
| r18 | 55 / 1000 | 6% |
| r19 | 37 / 1000 | 4% |
| r2 | 110 / 1000 | 11% |
| r20 | 69 / 1000 | 7% |
| r21 | 47 / 1000 | 5% |
| r22 | 21 / 1000 | 2% |
| r23 | 80 / 1000 | 8% |
| r24 | 96 / 1000 | 10% |
| r25 | 4 / 1000 | 0% |
| r26 | 86 / 1000 | 9% |
| r27 | 82 / 1000 | 8% |
| r28 | 13 / 1000 | 1% |
| r29 | 2 / 1000 | 0% |
| r3 | 48 / 1000 | 5% |
| r30 | 28 / 1000 | 3% |
| r31 | 1 / 1000 | 0% |
| r32 | 7 / 1000 | 1% |
| r33 | 94 / 1000 | 9% |
| r34 | 35 / 1000 | 4% |
| r35 | 74 / 1000 | 7% |
| r36 | 43 / 1000 | 4% |
| r37 | 90 / 1000 | 9% |
| r38 | 24 / 1000 | 2% |
| r39 | 54 / 1000 | 5% |
| r4 | 154 / 1000 | 15% |
| r40 | 55 / 1000 | 6% |
| r41 | 56 / 1000 | 6% |
| r42 | 35 / 1000 | 4% |
| r43 | 4 / 1000 | 0% |
| r44 | 1 / 1000 | 0% |
| r45 | 2 / 1000 | 0% |
| r46 | 86 / 1000 | 9% |
| r48 | 6 / 1000 | 1% |
| r49 | 58 / 1000 | 6% |
| r5 | 59 / 1000 | 6% |
| r50 | 37 / 1000 | 4% |
| r51 | 100 / 1000 | 10% |
| r52 | 82 / 1000 | 8% |
| r54 | 8 / 1000 | 1% |
| r55 | 79 / 1000 | 8% |
| r56 | 44 / 1000 | 4% |
| r57 | 45 / 1000 | 4% |
| r58 | 1 / 1000 | 0% |
| r59 | 9 / 1000 | 1% |
| r6 | 69 / 1000 | 7% |
| r60 | 82 / 1000 | 8% |
| r61 | 110 / 1000 | 11% |
| r62 | 72 / 1000 | 7% |
| r63 | 25 / 1000 | 2% |
| r64 | 2 / 1000 | 0% |
| r65 | 4 / 1000 | 0% |
| r66 | 31 / 1000 | 3% |
| r67 | 63 / 1000 | 6% |
| r69 | 1 / 1000 | 0% |
| r7 | 20 / 1000 | 2% |
| r70 | 89 / 1000 | 9% |
| r71 | 3 / 1000 | 0% |
| r72 | 49 / 1000 | 5% |
| r73 | 19 / 1000 | 2% |
| r74 | 37 / 1000 | 4% |
| r75 | 3 / 1000 | 0% |
| r76 | 57 / 1000 | 6% |
| r77 | 11 / 1000 | 1% |
| r78 | 36 / 1000 | 4% |
| r79 | 5 / 1000 | 0% |
| r8 | 30 / 1000 | 3% |
| r80 | 2 / 1000 | 0% |
| r81 | 91 / 1000 | 9% |
| r9 | 5 / 1000 | 0% |

> 有人漏标，Fleiss' kappa 不适用，改用 Krippendorff's alpha；两两一致性只统计双方共同标注过的样本。

## 二、两两一致性

标注者较多（77 人，1346 对组合），这里只给汇总；

| 指标 | 均值 | 中位数 | 最小 | 最大 |
|---|---|---|---|---|
| 一致率 | 29.31% | 20.00% | 0.00% | 100.00% |
| Cohen's kappa | 0.2016 | 0.0000 | -0.3333 | 1.0000 |

共同标注最多的 10 对（样本量越大越可靠）：

| 标注者 A | 标注者 B | 共同标注 | 一致率 | Cohen's kappa | 档位 |
|---|---|---|---|---|---|
| r37 | r61 | 34 | 97.06% | 0.9672 | 很好 |
| r4 | r61 | 28 | 46.43% | 0.3991 | 一般 |
| r4 | r60 | 26 | 30.77% | 0.2054 | 一般 |
| r37 | r4 | 25 | 36.00% | 0.2767 | 一般 |
| r60 | r61 | 23 | 21.74% | 0.1516 | 差 |
| r19 | r66 | 17 | 52.94% | 0.4667 | 中等 |
| r2 | r52 | 17 | 41.18% | 0.3462 | 一般 |
| r27 | r4 | 17 | 29.41% | 0.1707 | 差 |
| r24 | r33 | 15 | 100.00% | 1.0000 | 很好 |
| r2 | r6 | 14 | 21.43% | 0.0128 | 差 |

## 三、争议样本清单（747 条）

| 样本 ID | 文本 | 投票 | 分歧度 |
|---|---|---|---|
| ed571ai | I shouldn't be giggle-sn… | r27=realization；r3=remorse；r33=neutral；r54=amusement；r72=joy | 5 种 |
| ed93jar | I never knew how, but I … | r11=annoyance；r15=realization；r23=neutral；r40=excitement；r60=confusion | 5 种 |
| edgfsp5 | This looks so 2010s cgi | r19=approval；r26=relief；r49=neutral；r5=amusement；r66=realization | 5 种 |
| edhccyv | He didn't run off like a… | r36=neutral；r37=realization；r4=disapproval；r61=caring；r7=confusion | 5 种 |
| edis2h9 | I really enjoy “good lif… | r30=joy；r36=amusement；r37=neutral；r4=approval；r64=love | 5 种 |
| edn18yu | Precisely why im closete… | r19=disappointment；r52=nervousness；r55=confusion；r66=sadness；r67=caring | 5 种 |
| edpv00z | saving for when I'm not … | r2=pride；r40=approval；r66=caring；r78=neutral；r8=optimism | 5 种 |
| edrkl7s | I might be wrong about t… | r1=disgust；r22=approval；r23=annoyance；r35=neutral；r8=disapproval | 5 种 |
| ee28uy4 | I bet if anyone else had… | r23=embarrassment；r40=neutral；r41=disapproval；r51=approval；r56=anger | 5 种 |
| ee74f2a | I did Google it, you sel… | r34=sadness；r35=disapproval；r40=neutral；r72=remorse；r8=disappointment | 5 种 |
| eealh2s | Hope she likes cold show… | r16=neutral；r24=love；r50=desire；r56=caring；r81=optimism | 5 种 |
| eeams29 | Surrender to the feeling… | r36=realization；r37=approval；r4=neutral；r48=anger；r60=caring | 5 种 |
| eebefrk | All the plans I have see… | r12=amusement；r4=neutral；r56=excitement；r57=confusion；r60=surprise | 5 种 |
| eebhmot | I'd love either over any… | r23=desire；r26=optimism；r35=approval；r54=love；r8=neutral | 5 种 |
| eel5w0i | She's one among 435 memb… | r11=disapproval；r46=caring；r56=joy；r61=neutral；r81=disgust | 5 种 |
| eennjfg | Even assuming that it's … | r19=sadness；r25=neutral；r27=disappointment；r52=nervousness；r6=embarrassment | 5 种 |
| eex5i60 | Wrong person? Nothing I … | r1=neutral；r4=disapproval；r42=approval；r56=confusion；r61=curiosity | 5 种 |
| ef55xyv | Well ain't that ridiculo… | r33=joy；r37=annoyance；r51=neutral；r56=disappointment；r63=disapproval | 5 种 |
| efbvckm | i know :/ almost perfect… | r2=annoyance；r27=desire；r52=admiration；r63=optimism；r72=approval | 5 种 |
| eff271k | Yeah come back. You are … | r1=love；r2=admiration；r35=approval；r37=neutral；r56=joy | 5 种 |
| efgxg6c | Oh okay ya never heard i… | r2=realization；r38=surprise；r40=neutral；r41=confusion；r42=approval | 5 种 |
| eczyli4 | Dude I spit after this c… | r2=disapproval；r26=joy；r41=annoyance；r42=amusement | 4 种 |
| ed1jrqq | Sir, this would not be w… | r23=approval；r61=disapproval；r66=disappointment；r8=neutral | 4 种 |
| ed1z5mz | I’m not curious why you … | r3=curiosity；r38=disappointment；r49=approval；r70=neutral | 4 种 |
| ed429gc | Oh hell no | r1=surprise；r23=neutral；r4=disappointment；r51=disapproval；r54=surprise | 4 种 |
| ed4z3iz | Having watched Sunderlan… | r15=realization；r46=excitement；r50=neutral；r70=curiosity | 4 种 |
| ed5gooc | He absolutely loves it!! | r1=love；r11=admiration；r23=approval；r6=optimism | 4 种 |
| ed5kdew | It wasn't any better 10 … | r26=disapproval；r27=disappointment；r38=realization；r57=realization；r72=annoyance | 4 种 |
| ed5legu | Everything on the intern… | r12=approval；r26=disapproval；r33=neutral；r63=joy | 4 种 |
| ed5tx8y | That's crazy; I went to … | r23=amusement；r50=joy；r60=surprise；r62=neutral | 4 种 |

> 仅显示分歧度最高的 30 条，共 747 条。

## 四、分歧原因分析

| 原因 | 条数 | 该谁处理 |
|---|---|---|
| 规范未覆盖 | 247 | 补规范，跟标注员无关 |
| 系统性偏差 | 26 | 找当事人培训 |
| 个别错误 | 474 | 加抽检，不必培训 |
| 待人工复核 | 0 | 规则和第三方冲突，人工裁决 |

### 谁的标注习惯有问题

| 标注者 | 少数派次数 / 机会 | 主导标签 | 主导占比 | q 值 | 判定 |
|---|---|---|---|---|---|
| r4 | 37 / 124 | disapproval | 16% | 0.093 | **无明显规律** |
| r60 | 30 / 56 | annoyance | 20% | 0.018 | **无明显规律** |
| r2 | 27 / 83 | joy | 11% | 0.053 | **无明显规律** |
| r23 | 27 / 59 | neutral | 15% | 0.630 | **无明显规律** |
| r51 | 23 / 86 | neutral | 13% | 0.715 | **无明显规律** |
| r67 | 23 / 46 | surprise | 22% | <0.001 | **无明显规律** |
| r27 | 22 / 61 | neutral | 32% | 0.041 | **无明显规律** |
| r55 | 21 / 66 | confusion | 14% | 0.051 | **无明显规律** |
| r24 | 20 / 84 | neutral | 55% | <0.001 | **无明显规律** |
| r52 | 20 / 66 | disappointment | 15% | 0.062 | **无明显规律** |
| r61 | 20 / 92 | approval | 35% | 0.001 | **无明显规律** |
| r3 | 19 / 37 | approval | 42% | <0.001 | **无明显规律** |
| r46 | 19 / 60 | annoyance | 42% | <0.001 | **无明显规律** |
| r62 | 19 / 58 | disapproval | 21% | 0.075 | **无明显规律** |
| r15 | 18 / 37 | realization | 22% | 0.017 | **无明显规律** |
| r26 | 17 / 63 | disapproval | 24% | 0.052 | **无明显规律** |
| r39 | 17 / 47 | realization | 24% | 0.013 | **无明显规律** |
| r37 | 16 / 79 | neutral | 38% | 0.024 | **无明显规律** |
| r35 | 15 / 60 | neutral | 40% | 0.018 | **无明显规律** |
| r18 | 14 / 43 | disapproval | 21% | 0.125 | **无明显规律** |
| r41 | 14 / 39 | neutral | 43% | 0.013 | **无明显规律** |
| r5 | 14 / 39 | neutral | 21% | 0.410 | **无明显规律** |
| r70 | 14 / 69 | anger | 21% | 0.004 | **无明显规律** |
| r81 | 14 / 75 | admiration | 21% | 0.019 | **无明显规律** |
| r12 | 13 / 39 | approval | 31% | 0.034 | **无明显规律** |
| r20 | 13 / 56 | confusion | 23% | 0.007 | **无明显规律** |
| r6 | 13 / 51 | neutral | 23% | 0.379 | **无明显规律** |
| r21 | 12 / 39 | caring | 25% | <0.001 | **无明显规律** |
| r49 | 12 / 46 | love | 17% | <0.001 | **无明显规律** |
| r16 | 11 / 54 | admiration | 18% | 0.106 | **无明显规律** |

> 按少数派次数排序，仅显示前 30 人（共 77 人）。

> q 值 = 二项检验 p 值经 Benjamini-Hochberg 校正后的结果。只按次数判断时，标注者一多，随机波动就会被误报成系统性偏差。

### 逐条判定

| 样本 | 判定 | 依据 |
|---|---|---|
| eczcf47<br>r35=nervousness / r72=sadness | **规范未覆盖** | 三人各标一种，没有多数派——多半是规范没写清这种情况怎么处理 |
| eczgakj<br>r12=neutral / r55=optimism / r6=neutral | **个别错误** | r55 的标注偏离多数派，但本人没有固定倾向——可能是疏忽，也可能是规范有歧义 |
| eczl7i9<br>r46=annoyance / r50=love / r51=love | **个别错误** | r46 的标注偏离多数派，但本人没有固定倾向——可能是疏忽，也可能是规范有歧义 |
| eczm50f<br>r26=gratitude / r4=gratitude / r62=admiration / r74=gratitude / r81=gratitude | **个别错误** | r62 的标注偏离多数派，但本人没有固定倾向——可能是疏忽，也可能是规范有歧义 |
| eczt1qw<br>r19=disapproval / r24=optimism / r37=approval / r66=optimism | **个别错误** | r19、r37 的标注偏离多数派，但本人没有固定倾向——可能是疏忽，也可能是规范有歧义 |
| eczwg8f<br>r33=excitement / r5=admiration / r70=admiration | **个别错误** | r33 的标注偏离多数派，但本人没有固定倾向——可能是疏忽，也可能是规范有歧义 |
| eczyli4<br>r2=disapproval / r26=joy / r41=annoyance / r42=amusement | **规范未覆盖** | 三人各标一种，没有多数派——多半是规范没写清这种情况怎么处理 |
| ed00f1z<br>r18=joy / r24=excitement / r26=joy | **个别错误** | r24 的标注偏离多数派，但本人没有固定倾向——可能是疏忽，也可能是规范有歧义 |
| ed06ebu<br>r19=surprise / r5=surprise / r52=realization / r57=excitement | **个别错误** | r52、r57 的标注偏离多数派，但本人没有固定倾向——可能是疏忽，也可能是规范有歧义 |
| ed09n9p<br>r39=realization / r50=approval / r51=approval / r61=neutral / r72=neutral | **规范未覆盖** | 三人各标一种，没有多数派——多半是规范没写清这种情况怎么处理 |
| ed0cf46<br>r2=disapproval / r40=neutral / r6=neutral | **个别错误** | r2 的标注偏离多数派，但本人没有固定倾向——可能是疏忽，也可能是规范有歧义 |
| ed0i4do<br>r2=neutral / r21=realization / r46=remorse / r8=remorse / r9=realization | **规范未覆盖** | 三人各标一种，没有多数派——多半是规范没写清这种情况怎么处理 |
| ed0ww1z<br>r16=admiration / r21=neutral / r42=disapproval / r8=neutral | **个别错误** | r16、r42 的标注偏离多数派，但本人没有固定倾向——可能是疏忽，也可能是规范有歧义 |
| ed17oph<br>r10=admiration / r30=admiration / r70=amusement | **个别错误** | r70 的标注偏离多数派，但本人没有固定倾向——可能是疏忽，也可能是规范有歧义 |
| ed1gfcr<br>r24=neutral / r36=neutral / r50=approval / r57=caring | **个别错误** | r50、r57 的标注偏离多数派，但本人没有固定倾向——可能是疏忽，也可能是规范有歧义 |
| ed1gozt<br>r24=neutral / r3=disapproval / r4=neutral | **个别错误** | r3 的标注偏离多数派，但本人没有固定倾向——可能是疏忽，也可能是规范有歧义 |
| ed1jrqq<br>r23=approval / r61=disapproval / r66=disappointment / r8=neutral | **规范未覆盖** | 三人各标一种，没有多数派——多半是规范没写清这种情况怎么处理 |
| ed1me0x<br>r23=disapproval / r24=neutral / r33=neutral | **个别错误** | r23 的标注偏离多数派，但本人没有固定倾向——可能是疏忽，也可能是规范有歧义 |
| ed1vmyz<br>r19=approval / r41=neutral / r66=optimism | **规范未覆盖** | 三人各标一种，没有多数派——多半是规范没写清这种情况怎么处理 |
| ed1z5mz<br>r3=curiosity / r38=disappointment / r49=approval / r70=neutral | **规范未覆盖** | 三人各标一种，没有多数派——多半是规范没写清这种情况怎么处理 |
| ed20lrl<br>r35=relief / r5=admiration | **规范未覆盖** | 三人各标一种，没有多数派——多半是规范没写清这种情况怎么处理 |
| ed21plv<br>r16=desire / r26=neutral / r27=neutral / r51=neutral | **个别错误** | r16 的标注偏离多数派，但本人没有固定倾向——可能是疏忽，也可能是规范有歧义 |
| ed23xtm<br>r18=admiration / r33=amusement / r49=admiration / r56=love / r70=love | **规范未覆盖** | 三人各标一种，没有多数派——多半是规范没写清这种情况怎么处理 |
| ed28pcl<br>r26=annoyance / r62=neutral | **规范未覆盖** | 三人各标一种，没有多数派——多半是规范没写清这种情况怎么处理 |
| ed29flo<br>r12=joy / r2=desire / r51=desire | **个别错误** | r12 的标注偏离多数派，但本人没有固定倾向——可能是疏忽，也可能是规范有歧义 |
| ed2b17j<br>r27=neutral / r36=disapproval / r4=disapproval / r7=realization | **个别错误** | r27、r7 的标注偏离多数派，但本人没有固定倾向——可能是疏忽，也可能是规范有歧义 |
| ed2f4wf<br>r2=joy / r21=joy / r40=neutral | **个别错误** | r40 的标注偏离多数派，但本人没有固定倾向——可能是疏忽，也可能是规范有歧义 |
| ed2g0ls<br>r24=gratitude / r26=annoyance / r40=gratitude / r49=gratitude / r57=gratitude | **个别错误** | r26 的标注偏离多数派，但本人没有固定倾向——可能是疏忽，也可能是规范有歧义 |
| ed2jgez<br>r36=embarrassment / r48=joy / r72=optimism / r73=joy | **个别错误** | r36、r72 的标注偏离多数派，但本人没有固定倾向——可能是疏忽，也可能是规范有歧义 |
| ed2oj4q<br>r52=excitement / r57=joy | **规范未覆盖** | 三人各标一种，没有多数派——多半是规范没写清这种情况怎么处理 |

> 仅显示前 30 条，共 747 条争议。

## 五、哪两类最容易混

行 = 多数派本该选的类别，列 = 少数派实际选的类别。

| 多数派 ＼ 少数派 | admiration | amusement | anger | annoyance | approval | caring | confusion | curiosity | desire | disappointment | disapproval | disgust | embarrassment | excitement | fear | gratitude | grief | joy | love | nervousness | neutral | optimism | pride | realization | relief | remorse | sadness | surprise |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| **admiration** |  | 1 |  | 1 | 3 | 1 |  | 1 |  | 1 |  |  |  | 3 |  | 5 |  | 1 | 2 |  | 13 | 1 |  |  | 1 |  |  | 1 |
| **amusement** | 2 |  |  | 1 | 1 |  | 1 |  |  | 1 | 1 | 1 |  |  | 1 |  |  | 5 |  |  | 7 | 1 |  | 2 |  |  |  | 1 |
| **anger** |  |  |  | 2 |  |  |  | 1 |  | 1 |  |  | 1 |  |  |  |  |  |  |  | 2 |  |  |  |  |  |  |  |
| **annoyance** | 2 | 1 | 8 |  | 1 | 2 |  |  | 1 | 3 | 6 | 2 |  |  |  |  |  | 1 |  |  | 11 | 1 | 1 | 1 |  |  | 3 | 1 |
| **approval** | 1 |  |  | 1 |  | 2 |  |  | 1 |  | 1 |  |  | 2 |  |  |  | 1 |  |  | 9 | 1 |  | 2 |  |  |  | 1 |
| **caring** | 1 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | 1 | 2 | 1 |  |  |  |  |  |  |
| **confusion** |  |  |  | 1 |  |  |  | 4 |  | 1 | 1 |  |  |  |  |  |  |  |  |  | 5 |  |  | 2 |  |  |  |  |
| **curiosity** | 1 |  |  | 1 | 2 |  | 7 |  |  |  | 2 |  |  |  |  |  |  | 2 |  |  | 12 |  |  | 1 |  |  |  | 2 |
| **desire** |  | 1 |  | 1 |  |  |  |  |  |  |  |  |  | 1 |  |  |  | 1 | 1 |  | 2 | 2 |  | 1 |  |  |  |  |
| **disappointment** |  | 1 | 1 |  | 2 |  |  |  |  |  | 1 |  | 1 |  |  |  |  |  |  |  | 4 | 1 |  |  |  |  |  | 2 |
| **disapproval** |  | 1 | 4 | 2 | 4 |  | 2 |  | 1 | 2 |  | 1 |  | 2 |  |  |  |  |  |  | 11 | 2 |  | 4 |  |  |  |  |
| **disgust** |  |  |  | 3 |  |  |  |  |  | 1 | 2 |  | 1 |  | 1 |  |  |  |  |  |  |  |  |  |  |  |  |  |
| **embarrassment** |  |  |  | 2 |  |  | 1 |  |  | 1 |  | 1 |  |  |  |  |  |  |  |  | 2 |  |  |  |  |  | 1 | 1 |
| **excitement** |  |  |  |  |  | 1 |  |  | 1 |  |  |  |  |  |  |  |  | 1 |  |  | 2 |  |  |  |  |  |  |  |
| **fear** |  |  | 1 |  | 1 |  | 1 |  |  |  |  | 1 |  |  |  |  | 1 |  |  |  | 1 |  |  |  |  |  |  |  |
| **gratitude** | 1 | 1 |  | 2 | 1 |  |  |  |  |  | 1 |  |  |  |  |  |  |  | 1 |  | 1 |  |  |  |  |  |  |  |
| **joy** | 1 | 1 | 1 |  | 1 |  | 1 | 1 |  |  |  |  | 1 | 2 |  | 2 |  |  |  |  | 4 | 2 |  | 1 | 2 |  | 1 |  |
| **love** | 3 |  | 1 | 1 | 4 |  |  |  | 1 | 1 | 1 |  |  | 2 |  |  |  | 3 |  |  | 3 |  |  | 1 |  |  |  |  |
| **neutral** | 20 | 8 | 10 | 33 | 48 | 7 | 17 | 19 | 4 | 16 | 40 | 8 | 5 | 13 | 3 | 2 | 1 | 9 | 3 | 2 |  | 14 | 2 | 29 |  | 3 | 5 | 8 |
| **optimism** | 1 |  |  | 1 | 7 | 2 |  | 1 | 1 | 1 | 1 |  | 1 |  |  | 2 |  | 1 |  |  | 5 |  | 1 |  |  |  |  |  |
| **pride** | 1 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | 1 |  |  |  |  |  |  |  |
| **realization** | 1 |  |  | 2 |  |  | 1 |  | 1 | 1 | 3 |  |  |  |  |  |  |  |  |  | 10 | 1 |  |  |  |  |  |  |
| **relief** |  |  |  | 1 |  |  |  |  |  |  | 1 |  |  |  |  |  |  |  |  |  |  |  |  | 1 |  |  |  |  |
| **remorse** |  |  |  |  |  |  |  |  |  |  | 1 |  |  |  |  | 2 | 1 |  |  |  | 1 |  |  |  |  |  | 3 |  |
| **sadness** |  |  |  |  |  |  |  |  |  | 3 | 1 |  | 1 |  |  |  |  |  |  |  | 3 |  |  |  |  |  |  |  |
| **surprise** | 1 |  |  | 1 | 1 |  |  |  |  | 2 | 1 |  |  | 5 |  |  |  |  |  |  | 2 |  |  | 1 |  |  |  |  |

> 最集中的混淆：「neutral」→「approval」48 次（r3×6、r74×5、r61×4、r23×3、r22×3、r50×2、r15×2、r62×2、r60×2、r18×2、r12×2、r73×1、r26×1、r19×1、r42×1、r39×1、r51×1、r41×1、r5×1、r48×1、r57×1、r81×1、r4×1、r6×1、r29×1、r59×1）。

> 若同一格里全是同一个人，更像**个人理解偏差**（培训）；若分散在多人身上，更像**两类定义本身模糊**（补规范）。

## 六、本周行动

1. **【补规范】** eczcf47「It's probably more like when the only tool you have is a hammer, everything looks like a nail. I'm so sick of this paranoia.」—— 三人各持一说，确认归哪类后写进规范
2. **【补规范】** eczyli4「Dude I spit after this comment. I haven’t laughed like that in awhile.」—— 三人各持一说，确认归哪类后写进规范
3. **【补规范】** ed09n9p「They're only part of it. There are subliminals as well. My sa is cured. Have a blast keeping yours if that's what you want」—— 三人各持一说，确认归哪类后写进规范
4. **【补规范】** ed0i4do「I misunderstood "come back strong" 」—— 三人各持一说，确认归哪类后写进规范
5. **【补规范】** ed1jrqq「Sir, this would not be worth watching if he left out the best part.」—— 三人各持一说，确认归哪类后写进规范
6. **【补规范】** ed1vmyz「My friend is also interested!!! 👸🏻 Sent u a PM girly!」—— 三人各持一说，确认归哪类后写进规范
7. **【补规范】** ed1z5mz「I’m not curious why you think it’s relevant to have this information be held more favorably than all the real world analysis.」—— 三人各持一说，确认归哪类后写进规范
8. **【补规范】** ed20lrl「We don't care as much for 69. Hard to do properly. Glad it works for you. We prefer to take turns.」—— 三人各持一说，确认归哪类后写进规范
9. **【补规范】** ed23xtm「I noticed that too. How cute.」—— 三人各持一说，确认归哪类后写进规范
10. **【补规范】** ed28pcl「neither did they, but when they found out... oh boy」—— 三人各持一说，确认归哪类后写进规范
11. **【补规范】** ed2oj4q「Hi [NAME]. Nice to meet you, I'm promet. 」—— 三人各持一说，确认归哪类后写进规范
12. **【补规范】** ed2rfl3「Keeping the stomach warm also helps. Holding the baby with their stomach against yours helps them fall asleep. But it doesn't work all the time unfortunately.」—— 三人各持一说，确认归哪类后写进规范
13. **【补规范】** ed2sjal「I'm too late to rub this into all the casual's faces. :(」—— 三人各持一说，确认归哪类后写进规范
14. **【补规范】** ed37yew「The original Halloween movie is still the scariest film I have ever seen. Being chased by [NAME] in this game is terrifying.」—— 三人各持一说，确认归哪类后写进规范
15. **【补规范】** ed3lkkt「Don't, it's shit compared to the original. It's rather WATERed down :P Jokes aside it isn't as good.」—— 三人各持一说，确认归哪类后写进规范
16. **【补规范】** ed3n7rp「I thought it was all of Yorkshire... could be wrong though and it is just City if York!」—— 三人各持一说，确认归哪类后写进规范
17. **【补规范】** ed4ld1c「Weird! Also in Winnipeg, no issues. Do you have a VPN?」—— 三人各持一说，确认归哪类后写进规范
18. **【补规范】** ed4ri5e「I understand your frustration with [NAME] hate but [NAME] as a character though... /s」—— 三人各持一说，确认归哪类后写进规范
19. **【补规范】** ed4z3iz「Having watched Sunderland Till I Die it makes me desperate for some sort of insight into the way Arsenal operate behind the scenes.」—— 三人各持一说，确认归哪类后写进规范
20. **【补规范】** ed571ai「I shouldn't be giggle-snorting to this, but internally I am.」—— 三人各持一说，确认归哪类后写进规范
21. **【补规范】** ed5gooc「He absolutely loves it!!」—— 三人各持一说，确认归哪类后写进规范
22. **【补规范】** ed5legu「Everything on the internet is real and serious... Im here to be downvoted and laugh.」—— 三人各持一说，确认归哪类后写进规范
23. **【补规范】** ed5tx8y「That's crazy; I went to a super [RELIGION] high school and I think I can remember 2 girls the entire 4 years that became teen moms.」—— 三人各持一说，确认归哪类后写进规范
24. **【补规范】** ed63csu「Afraid not. I was just given a different perspective.」—— 三人各持一说，确认归哪类后写进规范
25. **【补规范】** ed6621v「Omg!!! just saw an interview of her! Wow this [NAME] is a horrible mother!!! Oh my Gooood! 😱」—— 三人各持一说，确认归哪类后写进规范
26. **【补规范】** ed6gq9t「Haha you have a cut on your face you must be the worst person who ever lived.」—— 三人各持一说，确认归哪类后写进规范
27. **【补规范】** ed6idhj「it sounds like a huge pain in the ass to use compared to current systems in place though.」—— 三人各持一说，确认归哪类后写进规范
28. **【补规范】** ed6mnnl「Join Wattpad! There are many great books and it's free :) If you want "real" books, [NAME] is definitely worth reading. 」—— 三人各持一说，确认归哪类后写进规范
29. **【补规范】** ed6vidl「What in the fuck? Now is garbage!」—— 三人各持一说，确认归哪类后写进规范
30. **【补规范】** ed7tqvl「It's ridiculous that [NAME] has inspired way more people to join rather than leave but there are way more media articles by people who have left.」—— 三人各持一说，确认归哪类后写进规范

> 仅显示前 30 项，共 298 项。
