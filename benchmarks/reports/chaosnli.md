# 标注一致性报告

- 样本数：**1000**
- 标注者：s1, s2, s3, s4, s5（共 5 人）
- 类别数：3

## 一、总体一致性

| 指标 | 数值 | 档位 |
|---|---|---|
| Fleiss' kappa（5 人） | 0.2627 | 一般 |
| 95% 置信区间 | [0.239, 0.286] | 1000 次 bootstrap |

> 1000 条样本，区间宽度 0.05。**方向可信（明显高于随机水平），但具体数值需谨慎看待。**

## 二、两两一致性

| 标注者 A | 标注者 B | 共同标注 | 一致率 | Cohen's kappa | 档位 |
|---|---|---|---|---|---|
| s1 | s2 | 1000 | 52.10% | 0.2529 | 一般 |
| s1 | s3 | 1000 | 53.30% | 0.2725 | 一般 |
| s1 | s4 | 1000 | 52.70% | 0.2629 | 一般 |
| s1 | s5 | 1000 | 53.10% | 0.2710 | 一般 |
| s2 | s3 | 1000 | 53.80% | 0.2797 | 一般 |
| s2 | s4 | 1000 | 53.60% | 0.2768 | 一般 |
| s2 | s5 | 1000 | 50.20% | 0.2248 | 一般 |
| s3 | s4 | 1000 | 51.50% | 0.2447 | 一般 |
| s3 | s5 | 1000 | 53.70% | 0.2804 | 一般 |
| s4 | s5 | 1000 | 52.50% | 0.2623 | 一般 |

## 三、争议样本清单（852 条）

| 样本 ID | 文本 | 投票 | 分歧度 |
|---|---|---|---|
| 10080c | In that case, price disc… | s1=contradiction；s2=neutral；s3=contradiction；s4=neutral；s5=entailment | 3 种 |
| 101467n | Horwitz makes us see tha… | s1=contradiction；s2=neutral；s3=neutral；s4=neutral；s5=entailment | 3 种 |
| 102563n | The judge gave vent to a… | s1=neutral；s2=contradiction；s3=neutral；s4=entailment；s5=neutral | 3 种 |
| 103400n | In Roman times a temple … | s1=contradiction；s2=entailment；s3=neutral；s4=contradiction；s5=contradiction | 3 种 |
| 103909n | Watergate remains for ma… | s1=entailment；s2=contradiction；s3=entailment；s4=neutral；s5=contradiction | 3 种 |
| 104399n | A survey of surgeons wor… | s1=neutral；s2=neutral；s3=neutral；s4=contradiction；s5=entailment | 3 种 |
| 105176n | I'd noticed him more tha… | s1=neutral；s2=neutral；s3=entailment；s4=contradiction；s5=entailment | 3 种 |
| 105561e | and they just put instru… | s1=entailment；s2=contradiction；s3=neutral；s4=entailment；s5=neutral | 3 种 |
| 107020c | in you know just dealing… | s1=neutral；s2=entailment；s3=entailment；s4=neutral；s5=contradiction | 3 种 |
| 10724n | Traditionally, certain d… | s1=neutral；s2=neutral；s3=contradiction；s4=entailment；s5=neutral | 3 种 |
| 108624c | Exhibit 3 presents total… | s1=contradiction；s2=neutral；s3=contradiction；s4=contradiction；s5=entailment | 3 种 |
| 108846e | Or, eligibility could be… | s1=entailment；s2=neutral；s3=neutral；s4=contradiction；s5=entailment | 3 种 |
| 109510n | so i really i really don… | s1=neutral；s2=neutral；s3=neutral；s4=contradiction；s5=entailment | 3 种 |
| 111011e | yep that's what he's wor… | s1=entailment；s2=entailment；s3=neutral；s4=neutral；s5=contradiction | 3 种 |
| 111577n | But overinterpretation o… | s1=entailment；s2=neutral；s3=neutral；s4=neutral；s5=contradiction | 3 种 |
| 111693e | The conspiracy-minded al… | s1=entailment；s2=entailment；s3=neutral；s4=contradiction；s5=contradiction | 3 种 |
| 111805c | and uh the whole organiz… | s1=neutral；s2=contradiction；s3=contradiction；s4=contradiction；s5=entailment | 3 种 |
| 112402c | Although the accounting … | s1=contradiction；s2=neutral；s3=entailment；s4=neutral；s5=neutral | 3 种 |
| 112592n | Maps of hiking trails ar… | s1=neutral；s2=neutral；s3=contradiction；s4=entailment；s5=contradiction | 3 种 |
| 112621n | Enter the realm of shopp… | s1=entailment；s2=entailment；s3=neutral；s4=entailment；s5=contradiction | 3 种 |
| 113280n | Also downtown is the Flo… | s1=contradiction；s2=neutral；s3=entailment；s4=contradiction；s5=neutral | 3 种 |
| 113628e | 5 The share of gross nat… | s1=entailment；s2=contradiction；s3=neutral；s4=entailment；s5=entailment | 3 种 |
| 114492n | and the same is true of … | s1=contradiction；s2=neutral；s3=entailment；s4=entailment；s5=neutral | 3 种 |
| 114916n | It spoke of thousands of… | s1=neutral；s2=neutral；s3=neutral；s4=entailment；s5=contradiction | 3 种 |
| 116176c | Students of human misery… | s1=entailment；s2=neutral；s3=entailment；s4=contradiction；s5=neutral | 3 种 |
| 117329e | His heels clicked togeth… | s1=neutral；s2=entailment；s3=entailment；s4=entailment；s5=contradiction | 3 种 |
| 117576e | but i don't know you kno… | s1=entailment；s2=entailment；s3=contradiction；s4=neutral；s5=neutral | 3 种 |
| 117894n | I never said you were a … | s1=entailment；s2=neutral；s3=neutral；s4=contradiction；s5=neutral | 3 种 |
| 121677n | The DO concentration mus… | s1=contradiction；s2=contradiction；s3=entailment；s4=neutral；s5=entailment | 3 种 |
| 122645n | Then you're ready for th… | s1=neutral；s2=neutral；s3=entailment；s4=entailment；s5=contradiction | 3 种 |

> 仅显示分歧度最高的 30 条，共 852 条。

## 四、分歧原因分析

| 原因 | 条数 | 该谁处理 |
|---|---|---|
| 规范未覆盖 | 107 | 补规范，跟标注员无关 |
| 系统性偏差 | 0 | 找当事人培训 |
| 个别错误 | 745 | 加抽检，不必培训 |
| 待人工复核 | 0 | 规则和第三方冲突，人工裁决 |

### 谁的标注习惯有问题

| 标注者 | 少数派次数 / 机会 | 主导标签 | 主导占比 | q 值 | 判定 |
|---|---|---|---|---|---|
| s5 | 237 / 893 | neutral | 39% | 0.979 | **无明显规律** |
| s1 | 234 / 893 | neutral | 45% | 0.601 | **无明显规律** |
| s2 | 231 / 893 | neutral | 45% | 0.601 | **无明显规律** |
| s3 | 226 / 893 | neutral | 46% | 0.601 | **无明显规律** |
| s4 | 225 / 893 | neutral | 48% | 0.601 | **无明显规律** |

> q 值 = 二项检验 p 值经 Benjamini-Hochberg 校正后的结果。只按次数判断时，标注者一多，随机波动就会被误报成系统性偏差。

### 逐条判定

| 样本 | 判定 | 依据 |
|---|---|---|
| 10004n<br>s1=neutral / s2=neutral / s3=entailment / s4=neutral / s5=entailment | **个别错误** | s3、s5 的标注偏离多数派，但本人没有固定倾向——可能是疏忽，也可能是规范有歧义 |
| 100136e<br>s1=entailment / s2=entailment / s3=neutral / s4=entailment / s5=neutral | **个别错误** | s3、s5 的标注偏离多数派，但本人没有固定倾向——可能是疏忽，也可能是规范有歧义 |
| 100231n<br>s1=neutral / s2=neutral / s3=entailment / s4=neutral / s5=neutral | **个别错误** | s3 的标注偏离多数派，但本人没有固定倾向——可能是疏忽，也可能是规范有歧义 |
| 100248n<br>s1=neutral / s2=entailment / s3=neutral / s4=entailment / s5=entailment | **个别错误** | s1、s3 的标注偏离多数派，但本人没有固定倾向——可能是疏忽，也可能是规范有歧义 |
| 100319e<br>s1=entailment / s2=neutral / s3=neutral / s4=entailment / s5=neutral | **个别错误** | s1、s4 的标注偏离多数派，但本人没有固定倾向——可能是疏忽，也可能是规范有歧义 |
| 100373c<br>s1=contradiction / s2=contradiction / s3=neutral / s4=neutral / s5=neutral | **个别错误** | s1、s2 的标注偏离多数派，但本人没有固定倾向——可能是疏忽，也可能是规范有歧义 |
| 100409e<br>s1=entailment / s2=entailment / s3=neutral / s4=neutral / s5=neutral | **个别错误** | s1、s2 的标注偏离多数派，但本人没有固定倾向——可能是疏忽，也可能是规范有歧义 |
| 100613n<br>s1=neutral / s2=entailment / s3=neutral / s4=neutral / s5=entailment | **个别错误** | s2、s5 的标注偏离多数派，但本人没有固定倾向——可能是疏忽，也可能是规范有歧义 |
| 100623n<br>s1=neutral / s2=entailment / s3=neutral / s4=neutral / s5=neutral | **个别错误** | s2 的标注偏离多数派，但本人没有固定倾向——可能是疏忽，也可能是规范有歧义 |
| 100768n<br>s1=entailment / s2=entailment / s3=neutral / s4=entailment / s5=entailment | **个别错误** | s3 的标注偏离多数派，但本人没有固定倾向——可能是疏忽，也可能是规范有歧义 |
| 100792c<br>s1=contradiction / s2=neutral / s3=neutral / s4=neutral / s5=contradiction | **个别错误** | s1、s5 的标注偏离多数派，但本人没有固定倾向——可能是疏忽，也可能是规范有歧义 |
| 10080c<br>s1=contradiction / s2=neutral / s3=contradiction / s4=neutral / s5=entailment | **规范未覆盖** | 三人各标一种，没有多数派——多半是规范没写清这种情况怎么处理 |
| 100895c<br>s1=neutral / s2=neutral / s3=neutral / s4=neutral / s5=contradiction | **个别错误** | s5 的标注偏离多数派，但本人没有固定倾向——可能是疏忽，也可能是规范有歧义 |
| 101104n<br>s1=entailment / s2=entailment / s3=entailment / s4=contradiction / s5=entailment | **个别错误** | s4 的标注偏离多数派，但本人没有固定倾向——可能是疏忽，也可能是规范有歧义 |
| 10119e<br>s1=entailment / s2=neutral / s3=entailment / s4=entailment / s5=entailment | **个别错误** | s2 的标注偏离多数派，但本人没有固定倾向——可能是疏忽，也可能是规范有歧义 |
| 101253n<br>s1=neutral / s2=neutral / s3=entailment / s4=neutral / s5=neutral | **个别错误** | s3 的标注偏离多数派，但本人没有固定倾向——可能是疏忽，也可能是规范有歧义 |
| 101467n<br>s1=contradiction / s2=neutral / s3=neutral / s4=neutral / s5=entailment | **个别错误** | s1、s5 的标注偏离多数派，但本人没有固定倾向——可能是疏忽，也可能是规范有歧义 |
| 101809c<br>s1=contradiction / s2=neutral / s3=neutral / s4=contradiction / s5=neutral | **个别错误** | s1、s4 的标注偏离多数派，但本人没有固定倾向——可能是疏忽，也可能是规范有歧义 |
| 101981n<br>s1=neutral / s2=neutral / s3=neutral / s4=entailment / s5=entailment | **个别错误** | s4、s5 的标注偏离多数派，但本人没有固定倾向——可能是疏忽，也可能是规范有歧义 |
| 102563n<br>s1=neutral / s2=contradiction / s3=neutral / s4=entailment / s5=neutral | **个别错误** | s2、s4 的标注偏离多数派，但本人没有固定倾向——可能是疏忽，也可能是规范有歧义 |
| 102647c<br>s1=neutral / s2=entailment / s3=neutral / s4=neutral / s5=neutral | **个别错误** | s2 的标注偏离多数派，但本人没有固定倾向——可能是疏忽，也可能是规范有歧义 |
| 102817c<br>s1=neutral / s2=neutral / s3=neutral / s4=neutral / s5=contradiction | **个别错误** | s5 的标注偏离多数派，但本人没有固定倾向——可能是疏忽，也可能是规范有歧义 |
| 102857n<br>s1=entailment / s2=entailment / s3=neutral / s4=entailment / s5=entailment | **个别错误** | s3 的标注偏离多数派，但本人没有固定倾向——可能是疏忽，也可能是规范有歧义 |
| 103155e<br>s1=entailment / s2=entailment / s3=entailment / s4=neutral / s5=entailment | **个别错误** | s4 的标注偏离多数派，但本人没有固定倾向——可能是疏忽，也可能是规范有歧义 |
| 103168n<br>s1=entailment / s2=neutral / s3=entailment / s4=entailment / s5=entailment | **个别错误** | s2 的标注偏离多数派，但本人没有固定倾向——可能是疏忽，也可能是规范有歧义 |
| 103169n<br>s1=entailment / s2=entailment / s3=entailment / s4=neutral / s5=entailment | **个别错误** | s4 的标注偏离多数派，但本人没有固定倾向——可能是疏忽，也可能是规范有歧义 |
| 103354n<br>s1=neutral / s2=neutral / s3=entailment / s4=entailment / s5=entailment | **个别错误** | s1、s2 的标注偏离多数派，但本人没有固定倾向——可能是疏忽，也可能是规范有歧义 |
| 103364n<br>s1=entailment / s2=entailment / s3=entailment / s4=neutral / s5=entailment | **个别错误** | s4 的标注偏离多数派，但本人没有固定倾向——可能是疏忽，也可能是规范有歧义 |
| 103400e<br>s1=contradiction / s2=contradiction / s3=entailment / s4=contradiction / s5=entailment | **个别错误** | s3、s5 的标注偏离多数派，但本人没有固定倾向——可能是疏忽，也可能是规范有歧义 |
| 103400n<br>s1=contradiction / s2=entailment / s3=neutral / s4=contradiction / s5=contradiction | **个别错误** | s2、s3 的标注偏离多数派，但本人没有固定倾向——可能是疏忽，也可能是规范有歧义 |

> 仅显示前 30 条，共 852 条争议。

## 五、哪两类最容易混

行 = 多数派本该选的类别，列 = 少数派实际选的类别。

| 多数派 ＼ 少数派 | contradiction | entailment | neutral |
|---|---|---|---|
| **contradiction** |  | 48 | 162 |
| **entailment** | 76 |  | 349 |
| **neutral** | 254 | 264 |  |

> 最集中的混淆：「entailment」→「neutral」349 次（s4×78、s3×73、s2×69、s1×65、s5×64）。

> 若同一格里全是同一个人，更像**个人理解偏差**（培训）；若分散在多人身上，更像**两类定义本身模糊**（补规范）。

## 六、本周行动

1. **【补规范】** 10080c「In that case, price discrimination can survive. [SEP] Right now, no leeway is possible with the price.」—— 三人各持一说，确认归哪类后写进规范
2. **【补规范】** 103909n「Watergate remains for many an unhealed wound, and Clinton's critics delight in needling him with Watergate comparisons--whether to Whitewater or Flytrap. [SEP] Clinton has several similarities to Whitewater or Flytrap.」—— 三人各持一说，确认归哪类后写进规范
3. **【补规范】** 105176n「I'd noticed him more than once and I'd figured it out in my own mind that he was afraid of somebody or something. [SEP] I saw him a few times and I thought that he was hiding something and is scared to be found out.」—— 三人各持一说，确认归哪类后写进规范
4. **【补规范】** 105561e「and they just put instructors out there and you you sign up for instruction and they just give you an arm band and if you see an instructor who's not doing anything you just tap him on the shoulder and ask him questions and they'll show you things [SEP] The instructors are marked with armbands, and anytime you want to know anything, you just find one of them. 」—— 三人各持一说，确认归哪类后写进规范
5. **【补规范】** 107020c「in you know just dealing with the customer maybe that's there only reason why they don't it'd seem like they'd just put a little barrel out there and say it pour here and go on  we'll take your money [SEP] The customers were just one of many reasons.」—— 三人各持一说，确认归哪类后写进规范
6. **【补规范】** 108846e「Or, eligibility could be restricted to those who have already been pregnant, or at least sexually active; to those over age 13, or under age 21; or some combination thereof. [SEP] Eligibility is restricted to those over age 13, quite possibly.」—— 三人各持一说，确认归哪类后写进规范
7. **【补规范】** 111011e「yep that's what he's worried about the trees or a bush because lilac bushes they they grow fast some people uh would really like to have them and then the people that do have them they spread and they sprout all over their their lawn [SEP] He's worried about the trees because the lilac bushes grow so fast they could wrap around them.」—— 三人各持一说，确认归哪类后写进规范
8. **【补规范】** 111693e「The conspiracy-minded allege that the chains also leverage their influence to persuade the big publishers to produce more blockbusters at the expense of moderate-selling books. [SEP] Big publishers want to produce more high budget films, even if that means badly selling books.」—— 三人各持一说，确认归哪类后写进规范
9. **【补规范】** 112592n「Maps of hiking trails are available at the Government Publications Ceter, Low Block, Government Offices, 66 Queensway in Central. [SEP] The maps show all the popular trails for walking and biking.」—— 三人各持一说，确认归哪类后写进规范
10. **【补规范】** 113280n「Also downtown is the Flower Market, on Wall and 8th streets; fresh-cut flowers and a variety of plants can be had for bargain prices, but the best selections are found before dawn. [SEP] Fresh-cut flowers available at the market range from cheap to expensive.」—— 三人各持一说，确认归哪类后写进规范
11. **【补规范】** 114492n「and the same is true of the drug hangover you know if you [SEP] It's just like a drug hangover but worse.」—— 三人各持一说，确认归哪类后写进规范
12. **【补规范】** 116176c「Students of human misery can savor its underlying sadness and futility. [SEP] Students of human misery will be delighted to see how sad it truly is.」—— 三人各持一说，确认归哪类后写进规范
13. **【补规范】** 117576e「but i don't know you know  maybe you could do that for a certain period of time but i mean how long does that kind of a thing take you know to to um say to question the person or to get into their head [SEP] It might take a long time to do that because getting inside a person's head takes time.」—— 三人各持一说，确认归哪类后写进规范
14. **【补规范】** 121677n「The DO concentration must not fall below [SEP] The DO concentration fell below.」—— 三人各持一说，确认归哪类后写进规范
15. **【补规范】** 122645n「Then you're ready for the fray, either in the bustling great bazaars such as Delhi's Chandni Chowk or Mumbai's Bhuleshwar, or the more sedate ambience of grander shops and showrooms. [SEP] All of the great bazaars are bustling at all times. 」—— 三人各持一说，确认归哪类后写进规范
16. **【补规范】** 126286e「more than anything else in this day and age that's got to be a big factor in your decision's just the the cost of how much you're gonna pay [SEP] In your decisions age is a big factor」—— 三人各持一说，确认归哪类后写进规范
17. **【补规范】** 127290n「The logic of analysis in case studies is the same [SEP] The logic for the case studies is the same thing as in the data collection.」—— 三人各持一说，确认归哪类后写进规范
18. **【补规范】** 129081e「right oh they've really done uh good job of keeping everybody informed of what's going on sometimes i've wondered if it wasn't almost more than we needed to know [SEP] After sharing all information with everyone, I think I may have shared too much. 」—— 三人各持一说，确认归哪类后写进规范
19. **【补规范】** 130928n「Still, I guess that can be got over. [SEP] There are some things that you need to ignore.」—— 三人各持一说，确认归哪类后写进规范
20. **【补规范】** 131216n「To the northwest of the chateau, the Grand Trianon palace, surrounded by pleasantly unpompous gardens, was the home of Louis XIV's mistress, Madame de Maintenon, where the aging king increasingly took refuge. [SEP] Grand Trianon palace was the residence of Louis XIV.」—— 三人各持一说，确认归哪类后写进规范
21. **【补规范】** 134217e「uh-huh and is it true i mean is it um [SEP] It's true.」—— 三人各持一说，确认归哪类后写进规范
22. **【补规范】** 134616e「But, as the last problem I'll outline suggests, neither of the previous two objections matters. [SEP] I will not continue to outline any more problems.」—— 三人各持一说，确认归哪类后写进规范
23. **【补规范】** 1364n「yeah it's true it is in in fact i have a friend of mine that moved to North Carolina she's um an emergency room nurse she does the operating room [SEP] My friend moved to NC to take a job as a nurse in a trauma unit at a hospital emergency room.」—— 三人各持一说，确认归哪类后写进规范
24. **【补规范】** 136860c「Dole : We ought to agree that somebody else should do it. [SEP] We don't agree that anyone should do it.」—— 三人各持一说，确认归哪类后写进规范
25. **【补规范】** 138337e「Also, why Princess Di was like President  The public cared more about her empathy than about her actions. [SEP] They scared more about empathy than actions.」—— 三人各持一说，确认归哪类后写进规范
26. **【补规范】** 138359n「Jon shifted and the sword tip slid past. [SEP] The man tried again to stab him.」—— 三人各持一说，确认归哪类后写进规范
27. **【补规范】** 138448c「Indeed, recent economic research suggests that investment in information technology explains most of the acceleration in labor productivity growth-a major component of overall economic growth-since 1995. [SEP] Investment in the financial sector explains most of the acceleration in labor productivity.」—— 三人各持一说，确认归哪类后写进规范
28. **【补规范】** 140428c「huh do you have your own kiln or do you do you [SEP] You don't have a kiln, do you?」—— 三人各持一说，确认归哪类后写进规范
29. **【补规范】** 142816n「a good team but they're an underdog that's why i like them is the Philadelphia Eagles [SEP] The Philadelphia Eagles is great team.」—— 三人各持一说，确认归哪类后写进规范
30. **【补规范】** 143608n「In research designs based on statistical inference, the criterion for establishing casuality is whether the findings are likely to have occurred by chance following appropriate comparisons to eliminate alternative interpretations. [SEP] Research designs may be based on statistical inference in different organizations. 」—— 三人各持一说，确认归哪类后写进规范

> 仅显示前 30 项，共 112 项。
