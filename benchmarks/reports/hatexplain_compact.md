# 标注一致性报告

- 样本数：**10000**
- 标注者：a1, a10, a100, a101, a104, a106, a108, a11, a110, a111, a112, a113 …（共 166 人）
- 类别数：3

## 一、总体一致性

| 指标 | 数值 | 档位 |
|---|---|---|
| Krippendorff's alpha（名义尺度，支持缺标） | 0.4595 | 中等 |
| 95% 置信区间 | [0.450, 0.469] | 1000 次 bootstrap |

> 10000 条样本，区间宽度 0.02。**方向可信（明显高于随机水平），但具体数值需谨慎看待。**

### 标注覆盖

| 标注者 | 标注条数 | 覆盖率 |
|---|---|---|
| a4 | 2791 / 10000 | 28% |
| a9 | 1045 / 10000 | 10% |
| a223 | 992 / 10000 | 10% |
| a203 | 975 / 10000 | 10% |

> 按标注条数排序，仅显示前 4 人（共 166 人）。

> 有人漏标，Fleiss' kappa 不适用，改用 Krippendorff's alpha；两两一致性只统计双方共同标注过的样本。

## 二、两两一致性

标注者较多（166 人，1499 对组合），这里只给汇总；

| 指标 | 均值 | 中位数 | 最小 | 最大 |
|---|---|---|---|---|
| 一致率 | 70.71% | 75.00% | 0.00% | 100.00% |
| Cohen's kappa | 0.4981 | 0.4375 | -1.0000 | 1.0000 |

共同标注最多的 4 对（样本量越大越可靠）：

| 标注者 A | 标注者 B | 共同标注 | 一致率 | Cohen's kappa | 档位 |
|---|---|---|---|---|---|
| a4 | a9 | 408 | 81.86% | 0.6559 | 较好 |
| a4 | a6 | 374 | 50.27% | 0.3286 | 一般 |
| a3 | a4 | 372 | 90.86% | 0.7600 | 较好 |
| a6 | a7 | 314 | 96.18% | 0.8743 | 很好 |

## 三、争议样本清单（5040 条）

| 样本 ID | 文本 | 投票 | 分歧度 |
|---|---|---|---|
| 10007406_gab | the scientific findings … | a205=offensive；a206=hatespeech；a207=normal | 3 种 |
| 1001155_gab | às vezes eu esqueço que … | a19=offensive；a6=hatespeech；a9=normal | 3 种 |
| 10110793_gab | they hate young boys wit… | a203=offensive；a206=hatespeech；a221=normal | 3 种 |
| 10348812_gab | if the illegal immigrant… | a213=hatespeech；a222=offensive；a239=normal | 3 种 |

> 仅显示分歧度最高的 4 条，共 5040 条。

## 四、分歧原因分析

| 原因 | 条数 | 该谁处理 |
|---|---|---|
| 规范未覆盖 | 532 | 补规范，跟标注员无关 |
| 系统性偏差 | 1642 | 找当事人培训 |
| 个别错误 | 2866 | 加抽检，不必培训 |
| 待人工复核 | 0 | 规则和第三方冲突，人工裁决 |

### 谁的标注习惯有问题

| 标注者 | 少数派次数 / 机会 | 主导标签 | 主导占比 | q 值 | 判定 |
|---|---|---|---|---|---|
| a4 | 326 / 2742 | hatespeech | 68% | <0.001 | **系统性偏差** |
| a211 | 235 / 625 | normal | 79% | <0.001 | **系统性偏差** |
| a223 | 217 / 923 | hatespeech | 50% | <0.001 | **显著但分散** |
| a209 | 199 / 813 | offensive | 43% | 0.772 | **无明显规律** |

> 按少数派次数排序，仅显示前 4 人（共 166 人）。

> q 值 = 二项检验 p 值经 Benjamini-Hochberg 校正后的结果。只按次数判断时，标注者一多，随机波动就会被误报成系统性偏差。「显著但分散」表示集中度显著、但主导标签占比低于 60%，不归为系统性偏差。

### 逐条判定

| 样本 | 判定 | 依据 |
|---|---|---|
| 10002346_gab<br>a202=normal / a203=offensive / a204=normal | **个别错误** | a203 的标注偏离多数派，但本人没有固定倾向——可能是疏忽，也可能是规范有歧义 |
| 10007406_gab<br>a205=offensive / a206=hatespeech / a207=normal | **规范未覆盖** | 3 人各标一种，没有多数派——多半是规范没写清这种情况怎么处理 |
| 10008196_gab<br>a200=hatespeech / a208=hatespeech / a209=normal | **个别错误** | a209 的标注偏离多数派，但本人没有固定倾向——可能是疏忽，也可能是规范有歧义 |
| 1001155_gab<br>a19=offensive / a6=hatespeech / a9=normal | **规范未覆盖** | 3 人各标一种，没有多数派——多半是规范没写清这种情况怎么处理 |

> 仅显示前 4 条，共 5040 条争议。

## 五、哪两类最容易混

行 = 多数派本该选的类别，列 = 少数派实际选的类别。

| 多数派 ＼ 少数派 | hatespeech | normal | offensive |
|---|---|---|---|
| **hatespeech** |  | 375 | 1055 |
| **normal** | 297 |  | 991 |
| **offensive** | 803 | 987 |  |

> 最集中的混淆：「hatespeech」→「offensive」1055 次（a207×78、a202×75、a6×71、a39×37、a209×36、a205×34、a4×34、a13×33、a212×33、a200×32、a222×28、a221×25、a211×24、a41×23、a228×22、a19×20、a7×20、a203×16、a56×15、a92×15、a57×14、a52×14、a233×13、a208×12、a210×12、a199×11、a206×11、a67×11、a229×10、a231×10、a215×9、a64×9、a201×9、a217×8、a55×8、a223×8、a37×8、a241×8、a2×7、a43×7、a104×6、a93×6、a17×6、a232×6、a204×6、a62×6、a83×5、a100×5、a60×5、a27×5、a96×5、a78×4、a77×4、a10×4、a220×4、a14×4、a234×4、a50×4、a61×4、a46×4、a227×3、a235×3、a90×3、a3×3、a230×3、a238×3、a11×3、a30×3、a15×3、a42×3、a226×2、a216×2、a8×2、a247×2、a33×2、a58×2、a1×2、a108×2、a65×2、a63×2、a29×2、a80×2、a214×2、a88×2、a213×1、a23×1、a48×1、a110×1、a91×1、a156×1、a132×1、a5×1、a160×1、a130×1、a81×1、a162×1、a59×1、a70×1、a148×1、a142×1、a20×1、a85×1、a21×1、a12×1、a34×1、a219×1、a47×1、a239×1、a89×1、a225×1、a106×1、a32×1、a68×1、a53×1）。

> 若同一格里全是同一个人，更像**个人理解偏差**（培训）；若分散在多人身上，更像**两类定义本身模糊**（补规范）。

## 六、本周行动

1. **【补规范】** 10007406_gab「the scientific findings that advocates and the pro gay media cite tend to come from decidedly unrepresentative samples that have been collected from places like bulletin boards at gay parenting support groups where everyone has an interest in proving that gay parenting is a success austin ruse」—— 没有多数派，确认归哪类后写进规范
2. **【补规范】** 1001155_gab「às vezes eu esqueço que meu nome tem origem sandnigger」—— 没有多数派，确认归哪类后写进规范
3. **【补规范】** 10110793_gab「they hate young boys with morals and father figures that can protect avenge them there is not a tranny in the us that would go camping without a shower mirror if you search for gay camping every place has air conditioning as recreated summer camps」—— 没有多数派，确认归哪类后写进规范
4. **【补规范】** 10348812_gab「if the illegal immigrant is a supposed doctor why is he leaving his own country why cant he finance himself properly if he wants to take up his practice why isnt he applying legally」—— 没有多数派，确认归哪类后写进规范

> 仅显示前 4 项，共 663 项。
