# 标注一致性报告

- 样本数：**10000**
- 标注者：r0, r1, r10, r11, r12, r13, r14, r15, r16, r17, r18, r19 …（共 80 人）
- 类别数：28

## 一、总体一致性

| 指标 | 数值 | 档位 |
|---|---|---|
| Krippendorff's alpha（名义尺度，支持缺标） | 0.2722 | 一般 |
| 95% 置信区间 | [0.264, 0.279] | 1000 次 bootstrap |

> 10000 条样本，区间宽度 0.02。**方向可信（明显高于随机水平），但具体数值需谨慎看待。**

### 标注覆盖

| 标注者 | 标注条数 | 覆盖率 |
|---|---|---|
| r0 | 9 / 10000 | 0% |
| r1 | 231 / 10000 | 2% |
| r10 | 179 / 10000 | 2% |
| r11 | 374 / 10000 | 4% |
| r12 | 440 / 10000 | 4% |
| r13 | 27 / 10000 | 0% |
| r14 | 81 / 10000 | 1% |
| r15 | 590 / 10000 | 6% |
| r16 | 546 / 10000 | 5% |
| r17 | 17 / 10000 | 0% |
| r18 | 520 / 10000 | 5% |
| r19 | 331 / 10000 | 3% |
| r2 | 957 / 10000 | 10% |
| r20 | 724 / 10000 | 7% |
| r21 | 463 / 10000 | 5% |
| r22 | 267 / 10000 | 3% |
| r23 | 742 / 10000 | 7% |
| r24 | 956 / 10000 | 10% |
| r25 | 55 / 10000 | 1% |
| r26 | 812 / 10000 | 8% |
| r27 | 833 / 10000 | 8% |
| r28 | 153 / 10000 | 2% |
| r29 | 41 / 10000 | 0% |
| r3 | 546 / 10000 | 5% |
| r30 | 253 / 10000 | 3% |
| r31 | 23 / 10000 | 0% |
| r32 | 86 / 10000 | 1% |
| r33 | 794 / 10000 | 8% |
| r34 | 306 / 10000 | 3% |
| r35 | 731 / 10000 | 7% |
| r36 | 452 / 10000 | 5% |
| r37 | 854 / 10000 | 9% |
| r38 | 258 / 10000 | 3% |
| r39 | 530 / 10000 | 5% |
| r4 | 1677 / 10000 | 17% |
| r40 | 709 / 10000 | 7% |
| r41 | 395 / 10000 | 4% |
| r42 | 353 / 10000 | 4% |
| r43 | 67 / 10000 | 1% |
| r44 | 19 / 10000 | 0% |
| r45 | 15 / 10000 | 0% |
| r46 | 832 / 10000 | 8% |
| r48 | 60 / 10000 | 1% |
| r49 | 623 / 10000 | 6% |
| r5 | 513 / 10000 | 5% |
| r50 | 328 / 10000 | 3% |
| r51 | 907 / 10000 | 9% |
| r52 | 920 / 10000 | 9% |
| r53 | 9 / 10000 | 0% |
| r54 | 81 / 10000 | 1% |
| r55 | 788 / 10000 | 8% |
| r56 | 406 / 10000 | 4% |
| r57 | 470 / 10000 | 5% |
| r58 | 26 / 10000 | 0% |
| r59 | 64 / 10000 | 1% |
| r6 | 720 / 10000 | 7% |
| r60 | 873 / 10000 | 9% |
| r61 | 1000 / 10000 | 10% |
| r62 | 758 / 10000 | 8% |
| r63 | 135 / 10000 | 1% |
| r64 | 15 / 10000 | 0% |
| r65 | 22 / 10000 | 0% |
| r66 | 288 / 10000 | 3% |
| r67 | 651 / 10000 | 7% |
| r69 | 10 / 10000 | 0% |
| r7 | 236 / 10000 | 2% |
| r70 | 828 / 10000 | 8% |
| r71 | 21 / 10000 | 0% |
| r72 | 432 / 10000 | 4% |
| r73 | 173 / 10000 | 2% |
| r74 | 303 / 10000 | 3% |
| r75 | 60 / 10000 | 1% |
| r76 | 485 / 10000 | 5% |
| r77 | 141 / 10000 | 1% |
| r78 | 289 / 10000 | 3% |
| r79 | 46 / 10000 | 0% |
| r8 | 351 / 10000 | 4% |
| r80 | 18 / 10000 | 0% |
| r81 | 890 / 10000 | 9% |
| r9 | 84 / 10000 | 1% |

> 有人漏标，Fleiss' kappa 不适用，改用 Krippendorff's alpha；两两一致性只统计双方共同标注过的样本。

## 二、两两一致性

标注者较多（80 人，2055 对组合），这里只给汇总；

| 指标 | 均值 | 中位数 | 最小 | 最大 |
|---|---|---|---|---|
| 一致率 | 27.65% | 25.71% | 0.00% | 100.00% |
| Cohen's kappa | 0.1794 | 0.1443 | -0.4545 | 1.0000 |

共同标注最多的 10 对（样本量越大越可靠）：

| 标注者 A | 标注者 B | 共同标注 | 一致率 | Cohen's kappa | 档位 |
|---|---|---|---|---|---|
| r37 | r61 | 352 | 96.31% | 0.9587 | 很好 |
| r4 | r60 | 343 | 36.15% | 0.2980 | 一般 |
| r4 | r61 | 257 | 36.58% | 0.2866 | 一般 |
| r37 | r4 | 237 | 38.40% | 0.3193 | 一般 |
| r60 | r61 | 202 | 27.23% | 0.2015 | 一般 |
| r27 | r4 | 168 | 30.95% | 0.2171 | 一般 |
| r36 | r7 | 160 | 14.37% | 0.0876 | 差 |
| r37 | r60 | 152 | 36.18% | 0.3096 | 一般 |
| r19 | r66 | 150 | 44.00% | 0.3953 | 一般 |
| r27 | r61 | 122 | 39.34% | 0.2703 | 一般 |

## 三、争议样本清单（7484 条）

| 样本 ID | 文本 | 投票 | 分歧度 |
|---|---|---|---|
| eczt9t1 | Yes but as he has gotten… | r36=caring；r37=neutral；r4=sadness；r56=disgust；r57=disappointment | 5 种 |
| ed02nla | We are killing this plan… | r1=annoyance；r37=approval；r51=fear；r56=grief；r78=neutral | 5 种 |
| ed0a9kb | Dance with the devil by … | r24=admiration；r36=disgust；r55=sadness；r60=disapproval；r70=annoyance | 5 种 |
| ed0tdoy | This joke is “the cheesi… | r20=remorse；r37=annoyance；r60=amusement；r65=approval；r67=admiration | 5 种 |
| ed0yu6p | Is it bad if I didnt eve… | r11=disappointment；r12=curiosity；r51=neutral；r56=embarrassment；r67=disgust | 5 种 |
| ed1ezv3 | Workers of the world uni… | r11=optimism；r26=annoyance；r5=pride；r61=realization；r8=neutral | 5 种 |
| ed2w1tr | Here a great example of … | r11=curiosity；r36=neutral；r4=realization；r51=admiration；r55=anger | 5 种 |
| ed33s33 | I would enjoy this if it… | r19=approval；r25=disapproval；r32=joy；r35=desire；r67=excitement | 5 种 |
| ed33tvv | It's an "inconvenient tr… | r21=annoyance；r38=realization；r57=disappointment；r60=neutral；r67=amusement | 5 种 |
| ed35exb | so far better than pinke… | r11=admiration；r26=optimism；r35=realization；r42=approval；r72=neutral | 5 种 |
| ed37e40 | There is no Ana meta. Pr… | r15=realization；r19=approval；r2=disappointment；r26=relief；r8=neutral | 5 种 |
| ed3aiug | That proposed sub name t… | r16=desire；r4=embarrassment；r5=disappointment；r60=annoyance；r77=realization | 5 种 |
| ed3c8g2 | I've been working in eng… | r12=curiosity；r38=sadness；r51=neutral；r52=approval；r8=disapproval | 5 种 |
| ed3ksp2 | Tucking your jeans into … | r30=neutral；r37=annoyance；r4=amusement；r48=disappointment；r60=disapproval | 5 种 |
| ed42qi0 | Wait, serious? | r15=curiosity；r42=neutral；r52=anger；r56=surprise；r60=confusion | 5 种 |
| ed4fewz | Wow, someones lived a sh… | r11=excitement；r34=surprise；r35=realization；r36=gratitude；r39=joy | 5 种 |
| ed4k1fg | I can do the first bit? … | r11=caring；r21=confusion；r23=approval；r36=neutral；r46=optimism | 5 种 |
| ed571ai | I shouldn't be giggle-sn… | r27=realization；r3=remorse；r33=neutral；r54=amusement；r72=joy | 5 种 |
| ed5r62e | The last Super Bowl Cham… | r23=gratitude；r26=neutral；r3=grief；r60=sadness；r8=admiration | 5 种 |
| ed5yq3r | It looked like a bad sui… | r11=disappointment；r2=embarrassment；r33=neutral；r71=realization；r8=disapproval | 5 种 |
| ed6cdt1 | Complete opposite for me… | r46=disappointment；r5=neutral；r52=nervousness；r60=embarrassment；r72=annoyance | 5 种 |
| ed6j5va | This one is solid. OP's … | r14=amusement；r27=neutral；r30=admiration；r37=annoyance；r61=disgust | 5 种 |
| ed6jkj0 | There is no *inherent* m… | r19=optimism；r5=realization；r55=confusion；r66=approval；r70=disapproval | 5 种 |
| ed6s3i1 | Governments aren't gener… | r1=approval；r15=disapproval；r38=anger；r51=neutral；r55=realization | 5 种 |
| ed6sfmx | It’s not you. These subs… | r23=disgust；r27=fear；r3=sadness；r6=neutral；r81=annoyance | 5 种 |
| ed6upz2 | Edit your post and inste… | r11=remorse；r20=confusion；r33=neutral；r60=caring；r70=disapproval | 5 种 |
| ed74jc9 | I don’t think you know w… | r38=confusion；r39=realization；r5=neutral；r60=annoyance；r62=disapproval | 5 种 |
| ed7g8hv | That’s very creepy and w… | r26=optimism；r33=neutral；r41=disgust；r50=fear；r67=sadness | 5 种 |
| ed8649i | They’re more just contro… | r36=disapproval；r40=neutral；r49=approval；r56=disappointment；r61=realization | 5 种 |
| ed8hbpx | Well she mostly horrible… | r3=approval；r38=neutral；r51=admiration；r60=annoyance；r62=fear | 5 种 |

> 仅显示分歧度最高的 30 条，共 7484 条。

## 四、分歧原因分析

| 原因 | 条数 | 该谁处理 |
|---|---|---|
| 规范未覆盖 | 2618 | 补规范，跟标注员无关 |
| 系统性偏差 | 219 | 找当事人培训 |
| 个别错误 | 4647 | 加抽检，不必培训 |
| 待人工复核 | 0 | 规则和第三方冲突，人工裁决 |

### 谁的标注习惯有问题

| 标注者 | 少数派次数 / 机会 | 主导标签 | 主导占比 | q 值 | 判定 |
|---|---|---|---|---|---|
| r4 | 453 / 1292 | neutral | 17% | 0.761 | **无明显规律** |
| r2 | 260 / 729 | neutral | 10% | 1.000 | **无明显规律** |
| r15 | 224 / 456 | realization | 20% | <0.001 | **显著但分散** |
| r23 | 222 / 572 | approval | 19% | <0.001 | **显著但分散** |
| r60 | 220 / 604 | annoyance | 26% | <0.001 | **显著但分散** |
| r46 | 210 / 645 | annoyance | 29% | <0.001 | **显著但分散** |
| r52 | 205 / 722 | anger | 14% | <0.001 | **显著但分散** |
| r3 | 204 / 411 | approval | 31% | <0.001 | **显著但分散** |
| r67 | 188 / 465 | surprise | 12% | <0.001 | **显著但分散** |
| r27 | 187 / 613 | neutral | 30% | <0.001 | **显著但分散** |
| r55 | 182 / 625 | disappointment | 13% | <0.001 | **显著但分散** |
| r62 | 175 / 587 | neutral | 21% | 0.262 | **无明显规律** |
| r26 | 174 / 625 | neutral | 22% | 0.144 | **无明显规律** |
| r24 | 171 / 768 | neutral | 65% | <0.001 | **系统性偏差** |
| r81 | 171 / 711 | confusion | 16% | <0.001 | **显著但分散** |
| r51 | 166 / 703 | neutral | 22% | 0.118 | **无明显规律** |
| r61 | 166 / 845 | neutral | 22% | 0.118 | **无明显规律** |
| r70 | 158 / 626 | neutral | 17% | 0.721 | **无明显规律** |
| r40 | 157 / 526 | neutral | 25% | 0.015 | **显著但分散** |
| r35 | 149 / 562 | neutral | 32% | <0.001 | **显著但分散** |
| r6 | 149 / 546 | neutral | 30% | <0.001 | **显著但分散** |
| r49 | 142 / 478 | neutral | 10% | 1.000 | **无明显规律** |
| r20 | 138 / 577 | neutral | 17% | 0.686 | **无明显规律** |
| r33 | 137 / 637 | neutral | 74% | <0.001 | **系统性偏差** |
| r12 | 128 / 346 | approval | 24% | <0.001 | **显著但分散** |
| r18 | 128 / 418 | approval | 16% | 0.082 | **无明显规律** |
| r37 | 123 / 742 | realization | 20% | <0.001 | **显著但分散** |
| r5 | 123 / 384 | neutral | 16% | 0.780 | **无明显规律** |
| r39 | 115 / 411 | neutral | 19% | 0.497 | **无明显规律** |
| r76 | 100 / 382 | annoyance | 16% | <0.001 | **显著但分散** |

> 按少数派次数排序，仅显示前 30 人（共 80 人）。

> q 值 = 二项检验 p 值经 Benjamini-Hochberg 校正后的结果。只按次数判断时，标注者一多，随机波动就会被误报成系统性偏差。

### 逐条判定

| 样本 | 判定 | 依据 |
|---|---|---|
| eczbpfi<br>r52=excitement / r61=optimism | **规范未覆盖** | 三人各标一种，没有多数派——多半是规范没写清这种情况怎么处理 |
| eczbrwg<br>r33=neutral / r35=approval / r51=neutral | **个别错误** | r35 的标注偏离多数派，但本人没有固定倾向——可能是疏忽，也可能是规范有歧义 |
| eczbz1n<br>r15=sadness / r2=sadness / r26=disappointment / r70=sadness / r81=disappointment | **个别错误** | r26、r81 的标注偏离多数派，但本人没有固定倾向——可能是疏忽，也可能是规范有歧义 |
| eczcf47<br>r35=nervousness / r72=sadness | **规范未覆盖** | 三人各标一种，没有多数派——多半是规范没写清这种情况怎么处理 |
| eczdbay<br>r11=confusion / r2=annoyance / r51=neutral / r57=realization | **规范未覆盖** | 三人各标一种，没有多数派——多半是规范没写清这种情况怎么处理 |
| eczdkqb<br>r10=neutral / r49=approval | **规范未覆盖** | 三人各标一种，没有多数派——多半是规范没写清这种情况怎么处理 |
| eczdx1e<br>r28=caring / r3=desire / r56=desire / r62=admiration / r76=optimism | **个别错误** | r28、r62、r76 的标注偏离多数派，但本人没有固定倾向——可能是疏忽，也可能是规范有歧义 |
| eczdygs<br>r37=curiosity / r4=confusion / r61=curiosity | **个别错误** | r4 的标注偏离多数派，但本人没有固定倾向——可能是疏忽，也可能是规范有歧义 |
| eczex23<br>r73=optimism / r81=confusion | **规范未覆盖** | 三人各标一种，没有多数派——多半是规范没写清这种情况怎么处理 |
| eczf05d<br>r26=neutral / r3=approval / r33=neutral / r46=approval | **规范未覆盖** | 三人各标一种，没有多数派——多半是规范没写清这种情况怎么处理 |
| eczfbty<br>r15=gratitude / r34=admiration / r36=joy / r50=joy / r52=excitement | **个别错误** | r15、r34、r52 的标注偏离多数派，但本人没有固定倾向——可能是疏忽，也可能是规范有歧义 |
| eczfxm4<br>r23=admiration / r24=neutral / r33=neutral | **个别错误** | r23 的标注偏离多数派，但本人没有固定倾向——可能是疏忽，也可能是规范有歧义 |
| eczgakj<br>r12=neutral / r55=optimism / r6=neutral | **个别错误** | r55 的标注偏离多数派，但本人没有固定倾向——可能是疏忽，也可能是规范有歧义 |
| eczhm1p<br>r16=anger / r24=anger / r42=neutral | **个别错误** | r42 的标注偏离多数派，但本人没有固定倾向——可能是疏忽，也可能是规范有歧义 |
| ecziu7i<br>r2=fear / r4=neutral / r72=confusion | **规范未覆盖** | 三人各标一种，没有多数派——多半是规范没写清这种情况怎么处理 |
| eczj0e1<br>r21=neutral / r24=neutral / r35=curiosity | **个别错误** | r35 的标注偏离多数派，但本人没有固定倾向——可能是疏忽，也可能是规范有歧义 |
| eczj7xk<br>r15=caring / r3=caring / r67=anger | **个别错误** | r67 的标注偏离多数派，但本人没有固定倾向——可能是疏忽，也可能是规范有歧义 |
| eczjljm<br>r52=anger / r75=annoyance | **规范未覆盖** | 三人各标一种，没有多数派——多半是规范没写清这种情况怎么处理 |
| eczkq1i<br>r15=gratitude / r23=admiration / r40=excitement / r8=gratitude | **个别错误** | r23、r40 的标注偏离多数派，但本人没有固定倾向——可能是疏忽，也可能是规范有歧义 |
| eczl7i9<br>r46=annoyance / r50=love / r51=love | **个别错误** | r46 的标注偏离多数派，但本人没有固定倾向——可能是疏忽，也可能是规范有歧义 |
| eczlqn3<br>r36=neutral / r60=caring / r7=annoyance / r72=neutral | **个别错误** | r60、r7 的标注偏离多数派，但本人没有固定倾向——可能是疏忽，也可能是规范有歧义 |
| eczm4tg<br>r27=disgust / r80=fear | **规范未覆盖** | 三人各标一种，没有多数派——多半是规范没写清这种情况怎么处理 |
| eczm50f<br>r26=gratitude / r4=gratitude / r62=admiration / r74=gratitude / r81=gratitude | **个别错误** | r62 的标注偏离多数派，但本人没有固定倾向——可能是疏忽，也可能是规范有歧义 |
| eczn3lg<br>r36=annoyance / r41=annoyance / r6=optimism / r61=annoyance / r62=neutral | **个别错误** | r6、r62 的标注偏离多数派，但本人没有固定倾向——可能是疏忽，也可能是规范有歧义 |
| ecznpdw<br>r41=optimism / r56=neutral / r70=desire / r77=desire | **个别错误** | r41、r56 的标注偏离多数派，但本人没有固定倾向——可能是疏忽，也可能是规范有歧义 |
| eczocof<br>r24=neutral / r39=fear | **规范未覆盖** | 三人各标一种，没有多数派——多半是规范没写清这种情况怎么处理 |
| eczoevf<br>r27=disapproval / r40=anger / r72=anger / r74=disgust / r77=anger | **个别错误** | r27、r74 的标注偏离多数派，但本人没有固定倾向——可能是疏忽，也可能是规范有歧义 |
| eczowjx<br>r36=joy / r4=disapproval / r60=annoyance / r7=joy | **个别错误** | r4、r60 的标注偏离多数派，但本人没有固定倾向——可能是疏忽，也可能是规范有歧义 |
| eczpfqw<br>r42=neutral / r49=confusion / r55=confusion | **个别错误** | r42 的标注偏离多数派，但本人没有固定倾向——可能是疏忽，也可能是规范有歧义 |
| eczq1hv<br>r17=approval / r4=approval / r60=disapproval / r7=sadness | **个别错误** | r60、r7 的标注偏离多数派，但本人没有固定倾向——可能是疏忽，也可能是规范有歧义 |

> 仅显示前 30 条，共 7484 条争议。

## 五、哪两类最容易混

行 = 多数派本该选的类别，列 = 少数派实际选的类别。

| 多数派 ＼ 少数派 | admiration | amusement | anger | annoyance | approval | caring | confusion | curiosity | desire | disappointment | disapproval | disgust | embarrassment | excitement | fear | gratitude | grief | joy | love | nervousness | neutral | optimism | pride | realization | relief | remorse | sadness | surprise |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| **admiration** |  | 18 | 2 | 12 | 48 | 7 | 3 | 4 | 1 | 3 | 4 | 1 | 1 | 25 | 2 | 36 |  | 17 | 16 | 1 | 111 | 10 | 15 | 9 | 3 | 1 | 2 | 10 |
| **amusement** | 7 |  | 7 | 17 | 18 | 2 | 2 | 4 | 4 | 8 | 7 | 4 |  | 6 | 2 | 2 |  | 45 | 3 |  | 88 | 8 |  | 9 |  |  | 2 | 4 |
| **anger** |  | 1 |  | 30 | 2 | 3 | 2 | 1 | 1 | 9 | 9 | 19 | 3 | 1 | 1 | 1 |  |  |  |  | 52 | 1 |  | 4 | 1 |  | 2 | 1 |
| **annoyance** | 7 | 7 | 46 |  | 22 | 5 | 11 | 6 | 3 | 25 | 28 | 21 | 5 | 6 | 3 |  |  | 4 | 2 | 5 | 94 | 8 | 1 | 16 | 1 | 1 | 9 | 10 |
| **approval** | 29 | 5 | 3 | 14 |  | 15 | 7 | 6 | 13 | 12 | 21 | 1 |  | 11 |  | 5 |  | 9 | 6 | 1 | 146 | 24 | 1 | 22 | 5 | 3 | 7 | 7 |
| **caring** | 4 | 1 | 3 | 6 | 13 |  | 2 | 2 | 4 | 2 | 4 | 1 |  | 1 | 1 | 8 |  | 2 | 3 | 2 | 40 | 10 | 1 | 1 | 5 | 3 | 1 | 2 |
| **confusion** | 1 | 1 | 2 | 6 | 6 | 2 |  | 33 | 2 | 2 | 4 | 1 |  | 2 | 1 |  |  |  |  | 1 | 64 | 3 | 1 | 5 |  |  | 4 | 8 |
| **curiosity** | 12 | 1 | 8 | 10 | 15 |  | 56 |  | 4 | 4 | 6 | 1 |  | 12 | 2 |  |  | 5 | 2 |  | 106 | 4 | 2 | 4 |  |  | 1 | 7 |
| **desire** | 2 | 4 | 1 | 6 | 10 | 2 | 1 | 3 |  | 2 | 2 |  |  | 3 | 1 |  |  | 2 | 4 |  | 28 | 15 | 1 | 3 |  | 1 | 1 | 1 |
| **disappointment** |  | 2 | 10 | 11 | 9 | 5 | 3 | 2 | 1 |  | 11 | 2 | 2 |  | 4 | 1 | 2 | 1 | 1 | 4 | 38 | 2 |  | 7 |  | 3 | 7 | 6 |
| **disapproval** | 2 | 9 | 14 | 34 | 37 | 6 | 11 | 1 | 2 | 31 |  | 14 | 2 | 5 | 1 |  |  | 1 |  | 1 | 134 | 7 |  | 22 | 1 | 2 | 9 | 2 |
| **disgust** | 2 | 2 | 13 | 13 | 4 |  | 3 | 1 | 1 | 8 | 10 |  | 2 | 1 | 3 |  |  |  |  |  | 23 |  |  | 2 |  |  | 4 | 2 |
| **embarrassment** | 1 | 1 |  | 7 | 3 |  | 2 | 1 |  | 4 | 1 | 1 |  |  |  |  |  | 1 |  | 1 | 10 |  |  | 1 |  | 2 | 2 | 2 |
| **excitement** | 4 | 5 | 1 | 4 | 6 | 1 |  | 5 | 3 |  | 2 |  |  |  |  |  |  | 13 |  |  | 29 | 6 |  | 1 |  |  |  | 4 |
| **fear** | 1 |  | 2 | 4 | 2 | 3 | 2 | 1 |  | 3 | 5 | 4 | 2 |  |  |  | 1 |  |  | 4 | 16 |  |  | 3 |  |  | 1 | 5 |
| **gratitude** | 8 | 3 | 2 | 5 | 6 | 5 | 1 | 1 | 4 | 1 | 1 |  |  | 5 |  |  |  | 5 | 4 |  | 19 | 4 | 1 | 1 | 2 |  | 1 |  |
| **grief** | 1 | 1 |  |  | 3 |  |  |  | 1 |  |  |  |  |  |  |  |  | 1 | 1 |  | 4 |  |  | 1 |  |  | 1 |  |
| **joy** | 15 | 11 | 2 | 4 | 9 | 3 | 1 | 1 | 2 | 1 | 2 | 1 | 2 | 14 |  | 10 |  |  | 3 |  | 28 | 3 | 2 | 3 | 4 |  | 1 | 1 |
| **love** | 34 | 3 | 2 | 7 | 22 | 2 | 1 |  | 4 | 1 | 6 | 3 |  | 8 |  | 4 |  | 34 |  | 1 | 43 | 3 | 1 | 10 |  | 1 | 1 | 1 |
| **nervousness** |  |  |  | 2 | 1 | 1 | 1 | 1 |  |  | 1 |  |  |  | 2 |  |  |  |  |  | 2 |  |  |  |  |  |  |  |
| **neutral** | 152 | 96 | 121 | 278 | 475 | 119 | 159 | 170 | 63 | 142 | 248 | 78 | 46 | 86 | 30 | 22 | 11 | 84 | 46 | 24 |  | 123 | 32 | 223 | 25 | 24 | 81 | 76 |
| **optimism** | 12 |  | 2 | 2 | 24 | 6 | 2 | 2 | 15 | 6 | 3 | 2 | 1 | 4 | 1 | 15 |  | 9 |  | 1 | 56 |  | 7 | 7 | 1 | 1 |  |  |
| **pride** | 1 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | 1 | 1 |  | 3 |  |  |  |  |  |  |  |
| **realization** | 4 | 4 | 1 | 12 | 21 | 2 | 5 | 4 | 2 | 4 | 12 | 2 | 1 | 1 | 2 |  |  | 2 |  | 1 | 53 | 5 | 1 |  | 3 | 1 | 4 | 6 |
| **relief** | 1 |  |  | 1 | 1 |  | 1 |  |  | 1 | 1 |  |  | 1 |  | 2 |  | 4 |  |  | 6 |  |  | 2 |  |  | 1 | 3 |
| **remorse** |  |  | 1 | 1 | 2 | 5 |  |  |  | 9 | 2 |  | 4 |  | 1 | 8 | 4 |  |  | 1 | 7 | 1 |  | 5 |  |  | 20 |  |
| **sadness** |  |  | 3 | 5 | 5 | 7 |  |  |  | 25 | 10 | 4 | 2 |  | 2 |  | 2 |  | 2 | 2 | 30 |  | 1 | 3 | 1 | 10 |  | 1 |
| **surprise** | 13 | 4 | 4 | 8 | 7 | 1 | 6 | 12 |  | 10 | 8 |  | 2 | 17 | 1 |  |  | 5 |  | 1 | 44 | 3 |  | 19 |  | 1 | 1 |  |

> 最集中的混淆：「neutral」→「approval」475 次（r3×42、r15×35、r4×31、r23×29、r42×20、r61×19、r35×17、r51×16、r74×16、r40×16、r52×14、r12×14、r22×14、r18×13、r6×12、r62×12、r26×11、r81×11、r37×10、r46×9、r39×9、r70×9、r73×8、r60×8、r50×7、r72×7、r59×6、r57×5、r2×4、r76×4、r66×4、r41×4、r56×3、r19×3、r63×3、r20×3、r8×2、r32×2、r30×2、r67×2、r55×2、r34×2、r5×2、r49×1、r11×1、r54×1、r75×1、r28×1、r24×1、r21×1、r38×1、r36×1、r48×1、r65×1、r29×1、r71×1）。

> 若同一格里全是同一个人，更像**个人理解偏差**（培训）；若分散在多人身上，更像**两类定义本身模糊**（补规范）。

## 六、本周行动

1. **【补规范】** eczbpfi「I would cheer hard for a Cyborg win in that tourney.」—— 三人各持一说，确认归哪类后写进规范
2. **【补规范】** eczcf47「It's probably more like when the only tool you have is a hammer, everything looks like a nail. I'm so sick of this paranoia.」—— 三人各持一说，确认归哪类后写进规范
3. **【补规范】** eczdbay「When people don't understand things they invent gods. how little we have changed in all these years.」—— 三人各持一说，确认归哪类后写进规范
4. **【补规范】** eczdkqb「Why did you expect to feel comfortable? What have you done to change?」—— 三人各持一说，确认归哪类后写进规范
5. **【补规范】** eczex23「E - Either we turn it around and make the playoffs or tank and [NAME] gets fired so win win right?」—— 三人各持一说，确认归哪类后写进规范
6. **【补规范】** eczf05d「Definitely. I find if I don't exercise for a few weeks I'll gain a few pounds quick..」—— 三人各持一说，确认归哪类后写进规范
7. **【补规范】** ecziu7i「I feel like I got lured into a fever dream by a normal combo video's beginning」—— 三人各持一说，确认归哪类后写进规范
8. **【补规范】** eczjljm「[NAME] dude I see [NAME] so rarely that I forget that he's the OG "Fuck this character fuck this stupid game" king. 」—— 三人各持一说，确认归哪类后写进规范
9. **【补规范】** eczm4tg「He is like a bad cartoon that’s hard to turn off.」—— 三人各持一说，确认归哪类后写进规范
10. **【补规范】** eczocof「Definitely accurate, lasted about a month total in a Disney “internship” program... was more like slavery. Terrible experience that ruined Disney for me」—— 三人各持一说，确认归哪类后写进规范
11. **【补规范】** eczqke5「i was planning on getting smashed but instead i'm sober...... no bullshit whatsoever」—— 三人各持一说，确认归哪类后写进规范
12. **【补规范】** eczs8ld「How can you look at that. it hurts.」—— 三人各持一说，确认归哪类后写进规范
13. **【补规范】** eczsaya「It's a shitty made shirt but if it was done well I'd wear it.」—— 三人各持一说，确认归哪类后写进规范
14. **【补规范】** eczt9t1「Yes but as he has gotten bigger and older it has gotten so much worse.」—— 三人各持一说，确认归哪类后写进规范
15. **【补规范】** ecztsvi「#PLAY [NAME] I miss that :( baseball plz come back」—— 三人各持一说，确认归哪类后写进规范
16. **【补规范】** eczusbt「"By far one of the best" Mmmm」—— 三人各持一说，确认归哪类后写进规范
17. **【补规范】** eczw7wb「Another year filled with Mets disappointments...... LGM! Can't wait for Spring Training!」—— 三人各持一说，确认归哪类后写进规范
18. **【补规范】** eczyli4「Dude I spit after this comment. I haven’t laughed like that in awhile.」—— 三人各持一说，确认归哪类后写进规范
19. **【补规范】** eczyr6d「I don’t think there are strippers necessarily, but it does make me question what he wants to do without me there」—— 三人各持一说，确认归哪类后写进规范
20. **【补规范】** eczzbru「Just the best WR in the league retweeting the best TE in the league, nothing to see here....」—— 三人各持一说，确认归哪类后写进规范
21. **【补规范】** ed00o9u「Not gonna lie I’m pretty out of it for New Years so I probably knew-jerked more than necessary. Happy New Years my man!」—— 三人各持一说，确认归哪类后写进规范
22. **【补规范】** ed01cgx「Omg what simple brilliance. The nbme is a waste of time!? Genius!」—— 三人各持一说，确认归哪类后写进规范
23. **【补规范】** ed01nso「I'm keeping my mouth shut. I don't want you yokels crowding up the wine store I go to.」—— 三人各持一说，确认归哪类后写进规范
24. **【补规范】** ed02jg5「Ok will do, but I listened to the ep right before I posted this.」—— 三人各持一说，确认归哪类后写进规范
25. **【补规范】** ed02nla「We are killing this planet」—— 三人各持一说，确认归哪类后写进规范
26. **【补规范】** ed0450z「Good for you, maybe some day you'll come to an understanding of each other but familiarity breeds contempt.」—— 三人各持一说，确认归哪类后写进规范
27. **【补规范】** ed04rm7「She already had plans with some of her friends and it would have been weird for me to get there, I didn’t know any of them. 」—— 三人各持一说，确认归哪类后写进规范
28. **【补规范】** ed05fwr「Pet-sitting is over, didn't know I was lonely without a doggo until now. 」—— 三人各持一说，确认归哪类后写进规范
29. **【补规范】** ed061gc「My ex would have believed that kinda stuff too. Some people aren’t really into movies」—— 三人各持一说，确认归哪类后写进规范
30. **【补规范】** ed0620k「Seeing the past doesn't mean being in the past」—— 三人各持一说，确认归哪类后写进规范

> 仅显示前 30 项，共 2694 项。
