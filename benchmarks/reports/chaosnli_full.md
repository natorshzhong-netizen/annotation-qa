# 标注一致性报告

- 样本数：**1599**
- 标注者：s1, s2, s3, s4, s5（共 5 人）
- 类别数：3

## 一、总体一致性

| 指标 | 数值 | 档位 |
|---|---|---|
| Fleiss' kappa（5 人） | 0.3027 | 一般 |
| 95% 置信区间 | [0.284, 0.320] | 1000 次 bootstrap |

> 1599 条样本，区间宽度 0.04。**方向可信（明显高于随机水平），但具体数值需谨慎看待。**

## 二、两两一致性

| 标注者 A | 标注者 B | 共同标注 | 一致率 | Cohen's kappa | 档位 |
|---|---|---|---|---|---|
| s1 | s2 | 1599 | 54.53% | 0.2943 | 一般 |
| s1 | s3 | 1599 | 55.10% | 0.3019 | 一般 |
| s1 | s4 | 1599 | 55.91% | 0.3176 | 一般 |
| s1 | s5 | 1599 | 55.53% | 0.3097 | 一般 |
| s2 | s3 | 1599 | 53.85% | 0.2822 | 一般 |
| s2 | s4 | 1599 | 54.41% | 0.2941 | 一般 |
| s2 | s5 | 1599 | 52.91% | 0.2687 | 一般 |
| s3 | s4 | 1599 | 55.10% | 0.3037 | 一般 |
| s3 | s5 | 1599 | 56.16% | 0.3181 | 一般 |
| s4 | s5 | 1599 | 57.16% | 0.3367 | 一般 |

## 三、争议样本清单（1307 条）

| 样本 ID | 文本 | 投票 | 分歧度 |
|---|---|---|---|
| 100248n | But we don't rule out re… | s1=neutral；s2=entailment；s3=contradiction；s4=neutral；s5=neutral | 3 种 |
| 100637e | the only problem is it's… | s1=contradiction；s2=entailment；s3=contradiction；s4=contradiction；s5=neutral | 3 种 |
| 101253n | In his effort to build n… | s1=neutral；s2=neutral；s3=entailment；s4=entailment；s5=contradiction | 3 种 |
| 101467n | Horwitz makes us see tha… | s1=neutral；s2=neutral；s3=neutral；s4=contradiction；s5=entailment | 3 种 |
| 101470e | Yet, in the mouths of th… | s1=entailment；s2=neutral；s3=contradiction；s4=neutral；s5=neutral | 3 种 |
| 10229n | The governing statute pr… | s1=entailment；s2=neutral；s3=neutral；s4=contradiction；s5=neutral | 3 种 |
| 102647c | This was built 15 years … | s1=entailment；s2=contradiction；s3=contradiction；s4=contradiction；s5=neutral | 3 种 |
| 102817c | yes they would they just… | s1=contradiction；s2=entailment；s3=entailment；s4=contradiction；s5=neutral | 3 种 |
| 102817n | yes they would they just… | s1=contradiction；s2=neutral；s3=entailment；s4=contradiction；s5=contradiction | 3 种 |
| 10289n | Most produce is locally … | s1=entailment；s2=neutral；s3=neutral；s4=entailment；s5=contradiction | 3 种 |
| 103400e | In Roman times a temple … | s1=contradiction；s2=neutral；s3=entailment；s4=contradiction；s5=entailment | 3 种 |
| 103400n | In Roman times a temple … | s1=entailment；s2=contradiction；s3=entailment；s4=contradiction；s5=neutral | 3 种 |
| 105196e | Indeed, said San'doro. [… | s1=neutral；s2=neutral；s3=contradiction；s4=entailment；s5=entailment | 3 种 |
| 105911c | and to have children and… | s1=entailment；s2=contradiction；s3=neutral；s4=entailment；s5=contradiction | 3 种 |
| 105911n | and to have children and… | s1=neutral；s2=contradiction；s3=neutral；s4=entailment；s5=neutral | 3 种 |
| 106390n | Mykonos has had a head s… | s1=contradiction；s2=entailment；s3=entailment；s4=neutral；s5=neutral | 3 种 |
| 106411n | His diet was of wheaten … | s1=contradiction；s2=entailment；s3=entailment；s4=neutral；s5=entailment | 3 种 |
| 108027n | The door opened and Seve… | s1=neutral；s2=neutral；s3=entailment；s4=neutral；s5=contradiction | 3 种 |
| 109443n | Waterloo. [SEP] The defe… | s1=neutral；s2=contradiction；s3=entailment；s4=contradiction；s5=entailment | 3 种 |
| 109876c | Text Box 2.1: Gross Dome… | s1=entailment；s2=contradiction；s3=neutral；s4=contradiction；s5=contradiction | 3 种 |
| 110671n | No, John, I said, "it is… | s1=entailment；s2=contradiction；s3=entailment；s4=contradiction；s5=neutral | 3 种 |
| 111805c | and uh the whole organiz… | s1=entailment；s2=contradiction；s3=contradiction；s4=neutral；s5=contradiction | 3 种 |
| 112293n | Cave 31 tries to emulate… | s1=neutral；s2=neutral；s3=entailment；s4=contradiction；s5=neutral | 3 种 |
| 112402c | Although the accounting … | s1=neutral；s2=entailment；s3=neutral；s4=contradiction；s5=neutral | 3 种 |
| 112592n | Maps of hiking trails ar… | s1=contradiction；s2=contradiction；s3=neutral；s4=neutral；s5=entailment | 3 种 |
| 11299e | 'Not part of your biogra… | s1=entailment；s2=entailment；s3=entailment；s4=neutral；s5=contradiction | 3 种 |
| 113570c | Time reports that Harrer… | s1=neutral；s2=entailment；s3=neutral；s4=contradiction；s5=contradiction | 3 种 |
| 114916n | It spoke of thousands of… | s1=contradiction；s2=neutral；s3=entailment；s4=entailment；s5=neutral | 3 种 |
| 114988e | Each one planting itself… | s1=neutral；s2=entailment；s3=contradiction；s4=entailment；s5=neutral | 3 种 |
| 115830n | The avenue on the left l… | s1=contradiction；s2=contradiction；s3=neutral；s4=entailment；s5=neutral | 3 种 |

> 仅显示分歧度最高的 30 条，共 1307 条。

## 四、分歧原因分析

| 原因 | 条数 | 该谁处理 |
|---|---|---|
| 规范未覆盖 | 132 | 补规范，跟标注员无关 |
| 系统性偏差 | 0 | 找当事人培训 |
| 个别错误 | 1175 | 加抽检，不必培训 |
| 待人工复核 | 0 | 规则和第三方冲突，人工裁决 |

### 谁的标注习惯有问题

| 标注者 | 少数派次数 / 机会 | 主导标签 | 主导占比 | q 值 | 判定 |
|---|---|---|---|---|---|
| s2 | 385 / 1467 | neutral | 46% | 0.847 | **无明显规律** |
| s3 | 370 / 1467 | neutral | 49% | 0.759 | **无明显规律** |
| s1 | 365 / 1467 | neutral | 44% | 0.847 | **无明显规律** |
| s5 | 355 / 1467 | neutral | 48% | 0.767 | **无明显规律** |
| s4 | 349 / 1467 | neutral | 45% | 0.847 | **无明显规律** |

> q 值 = 二项检验 p 值经 Benjamini-Hochberg 校正后的结果。只按次数判断时，标注者一多，随机波动就会被误报成系统性偏差。

### 逐条判定

| 样本 | 判定 | 依据 |
|---|---|---|
| 10004n<br>s1=entailment / s2=neutral / s3=entailment / s4=neutral / s5=entailment | **个别错误** | s2、s4 的标注偏离多数派，但本人没有固定倾向——可能是疏忽，也可能是规范有歧义 |
| 100136e<br>s1=neutral / s2=entailment / s3=neutral / s4=entailment / s5=entailment | **个别错误** | s1、s3 的标注偏离多数派，但本人没有固定倾向——可能是疏忽，也可能是规范有歧义 |
| 10015n<br>s1=neutral / s2=neutral / s3=entailment / s4=neutral / s5=neutral | **个别错误** | s3 的标注偏离多数派，但本人没有固定倾向——可能是疏忽，也可能是规范有歧义 |
| 100231n<br>s1=entailment / s2=entailment / s3=neutral / s4=entailment / s5=entailment | **个别错误** | s3 的标注偏离多数派，但本人没有固定倾向——可能是疏忽，也可能是规范有歧义 |
| 100248c<br>s1=contradiction / s2=neutral / s3=neutral / s4=contradiction / s5=contradiction | **个别错误** | s2、s3 的标注偏离多数派，但本人没有固定倾向——可能是疏忽，也可能是规范有歧义 |
| 100248n<br>s1=neutral / s2=entailment / s3=contradiction / s4=neutral / s5=neutral | **个别错误** | s2、s3 的标注偏离多数派，但本人没有固定倾向——可能是疏忽，也可能是规范有歧义 |
| 100319e<br>s1=entailment / s2=neutral / s3=entailment / s4=neutral / s5=entailment | **个别错误** | s2、s4 的标注偏离多数派，但本人没有固定倾向——可能是疏忽，也可能是规范有歧义 |
| 100332e<br>s1=entailment / s2=contradiction / s3=entailment / s4=entailment / s5=entailment | **个别错误** | s2 的标注偏离多数派，但本人没有固定倾向——可能是疏忽，也可能是规范有歧义 |
| 100349e<br>s1=neutral / s2=entailment / s3=neutral / s4=entailment / s5=neutral | **个别错误** | s2、s4 的标注偏离多数派，但本人没有固定倾向——可能是疏忽，也可能是规范有歧义 |
| 100373c<br>s1=neutral / s2=neutral / s3=contradiction / s4=contradiction / s5=neutral | **个别错误** | s3、s4 的标注偏离多数派，但本人没有固定倾向——可能是疏忽，也可能是规范有歧义 |
| 100409e<br>s1=neutral / s2=entailment / s3=neutral / s4=neutral / s5=neutral | **个别错误** | s2 的标注偏离多数派，但本人没有固定倾向——可能是疏忽，也可能是规范有歧义 |
| 100613c<br>s1=contradiction / s2=neutral / s3=contradiction / s4=contradiction / s5=contradiction | **个别错误** | s2 的标注偏离多数派，但本人没有固定倾向——可能是疏忽，也可能是规范有歧义 |
| 100623n<br>s1=entailment / s2=entailment / s3=neutral / s4=neutral / s5=neutral | **个别错误** | s1、s2 的标注偏离多数派，但本人没有固定倾向——可能是疏忽，也可能是规范有歧义 |
| 100637e<br>s1=contradiction / s2=entailment / s3=contradiction / s4=contradiction / s5=neutral | **个别错误** | s2、s5 的标注偏离多数派，但本人没有固定倾向——可能是疏忽，也可能是规范有歧义 |
| 100768n<br>s1=entailment / s2=entailment / s3=neutral / s4=entailment / s5=entailment | **个别错误** | s3 的标注偏离多数派，但本人没有固定倾向——可能是疏忽，也可能是规范有歧义 |
| 100792c<br>s1=contradiction / s2=neutral / s3=neutral / s4=contradiction / s5=neutral | **个别错误** | s1、s4 的标注偏离多数派，但本人没有固定倾向——可能是疏忽，也可能是规范有歧义 |
| 100792n<br>s1=entailment / s2=neutral / s3=entailment / s4=entailment / s5=entailment | **个别错误** | s2 的标注偏离多数派，但本人没有固定倾向——可能是疏忽，也可能是规范有歧义 |
| 10080c<br>s1=contradiction / s2=contradiction / s3=neutral / s4=contradiction / s5=neutral | **个别错误** | s3、s5 的标注偏离多数派，但本人没有固定倾向——可能是疏忽，也可能是规范有歧义 |
| 101104n<br>s1=entailment / s2=entailment / s3=entailment / s4=contradiction / s5=entailment | **个别错误** | s4 的标注偏离多数派，但本人没有固定倾向——可能是疏忽，也可能是规范有歧义 |
| 101195n<br>s1=neutral / s2=contradiction / s3=neutral / s4=contradiction / s5=contradiction | **个别错误** | s1、s3 的标注偏离多数派，但本人没有固定倾向——可能是疏忽，也可能是规范有歧义 |
| 10119e<br>s1=entailment / s2=neutral / s3=entailment / s4=neutral / s5=neutral | **个别错误** | s1、s3 的标注偏离多数派，但本人没有固定倾向——可能是疏忽，也可能是规范有歧义 |
| 101245n<br>s1=entailment / s2=neutral / s3=entailment / s4=entailment / s5=entailment | **个别错误** | s2 的标注偏离多数派，但本人没有固定倾向——可能是疏忽，也可能是规范有歧义 |
| 101253n<br>s1=neutral / s2=neutral / s3=entailment / s4=entailment / s5=contradiction | **规范未覆盖** | 三人各标一种，没有多数派——多半是规范没写清这种情况怎么处理 |
| 101467n<br>s1=neutral / s2=neutral / s3=neutral / s4=contradiction / s5=entailment | **个别错误** | s4、s5 的标注偏离多数派，但本人没有固定倾向——可能是疏忽，也可能是规范有歧义 |
| 101470e<br>s1=entailment / s2=neutral / s3=contradiction / s4=neutral / s5=neutral | **个别错误** | s1、s3 的标注偏离多数派，但本人没有固定倾向——可能是疏忽，也可能是规范有歧义 |
| 101525c<br>s1=neutral / s2=contradiction / s3=neutral / s4=neutral / s5=neutral | **个别错误** | s2 的标注偏离多数派，但本人没有固定倾向——可能是疏忽，也可能是规范有歧义 |
| 101809c<br>s1=neutral / s2=neutral / s3=neutral / s4=entailment / s5=entailment | **个别错误** | s4、s5 的标注偏离多数派，但本人没有固定倾向——可能是疏忽，也可能是规范有歧义 |
| 101809n<br>s1=neutral / s2=entailment / s3=entailment / s4=neutral / s5=entailment | **个别错误** | s1、s4 的标注偏离多数派，但本人没有固定倾向——可能是疏忽，也可能是规范有歧义 |
| 101981n<br>s1=entailment / s2=neutral / s3=neutral / s4=neutral / s5=entailment | **个别错误** | s1、s5 的标注偏离多数派，但本人没有固定倾向——可能是疏忽，也可能是规范有歧义 |
| 102031e<br>s1=entailment / s2=entailment / s3=contradiction / s4=entailment / s5=contradiction | **个别错误** | s3、s5 的标注偏离多数派，但本人没有固定倾向——可能是疏忽，也可能是规范有歧义 |

> 仅显示前 30 条，共 1307 条争议。

## 五、哪两类最容易混

行 = 多数派本该选的类别，列 = 少数派实际选的类别。

| 多数派 ＼ 少数派 | contradiction | entailment | neutral |
|---|---|---|---|
| **contradiction** |  | 85 | 255 |
| **entailment** | 103 |  | 592 |
| **neutral** | 360 | 429 |  |

> 最集中的混淆：「entailment」→「neutral」592 次（s2×128、s4×118、s5×117、s3×115、s1×114）。

> 若同一格里全是同一个人，更像**个人理解偏差**（培训）；若分散在多人身上，更像**两类定义本身模糊**（补规范）。

## 六、本周行动

1. **【补规范】** 101253n「In his effort to build nationalism across Turkey in the 1920s, Ataterk instituted a campaign to suppress Kurdish identity that continues today. [SEP] His campaign to suppress the identity of the Kurds was successful.」—— 三人各持一说，确认归哪类后写进规范
2. **【补规范】** 102817c「yes they would they just wouldn't be able to own the kind of automobiles that they think they deserve to own or the kind of homes that we think we deserve to own we might have to you know just be able to i think if we a generation went without debt then the next generation like if if our our generation my husband and i we're twenty eight if we lived our lives and didn't become you know indebted like you know our generation before us that um the budget would balance and that we became accustomed to living with what we could afford which we wouldn't be destitute i mean we wouldn't be living on the street by any means but just compared to how spoiled we are we would be in our own minds but i feel like the generation after us would oh man it it would be so good it would be so much better it wouldn't be perfect but then they could learn to live with what what they could afford to save to buy and if you want a nicer car than that well you save a little longer [SEP] I am glad our generation has no debt.」—— 三人各持一说，确认归哪类后写进规范
3. **【补规范】** 10289n「Most produce is locally grown, with some from the restaurant's own organic garden. [SEP] Most produce is local and some is grown inside the restaurant.」—— 三人各持一说，确认归哪类后写进规范
4. **【补规范】** 103400e「In Roman times a temple to Jupiter stood here, followed in the fourth century by the first Christian church, Saint-Etienne. [SEP] Saint-Etienne, a Christian church, had a temple to Jupiter during Roman times.」—— 三人各持一说，确认归哪类后写进规范
5. **【补规范】** 103400n「In Roman times a temple to Jupiter stood here, followed in the fourth century by the first Christian church, Saint-Etienne. [SEP] Saint-Etienne, a Christian church, had a temple to Jupiter and performed rituals during Roman times」—— 三人各持一说，确认归哪类后写进规范
6. **【补规范】** 105196e「Indeed, said San'doro. [SEP] Indeed, they said.」—— 三人各持一说，确认归哪类后写进规范
7. **【补规范】** 105911c「and to have children and just get a day care or someone to take care of it and not really have the bonding process that takes place with babies and stuff you know [SEP] The children should not go to day car.」—— 三人各持一说，确认归哪类后写进规范
8. **【补规范】** 106390n「Mykonos has had a head start as far as diving is concerned because it was never banned here (after all, there are no ancient sites to protect). [SEP] Protection of ancient sites is the reason for diving bans in other places.」—— 三人各持一说，确认归哪类后写进规范
9. **【补规范】** 109443n「Waterloo. [SEP] The defeat of Napoleon.」—— 三人各持一说，确认归哪类后写进规范
10. **【补规范】** 110671n「No, John, I said, "it isn't one of us.  [SEP] John didn't know if they were one of us.」—— 三人各持一说，确认归哪类后写进规范
11. **【补规范】** 112592n「Maps of hiking trails are available at the Government Publications Ceter, Low Block, Government Offices, 66 Queensway in Central. [SEP] The maps show all the popular trails for walking and biking.」—— 三人各持一说，确认归哪类后写进规范
12. **【补规范】** 113570c「Time reports that Harrer denies having known she was.) [SEP] Harrer was will aware that she was.」—— 三人各持一说，确认归哪类后写进规范
13. **【补规范】** 114916n「It spoke of thousands of years, even before the times of the old empire. [SEP] The old Empire died out.」—— 三人各持一说，确认归哪类后写进规范
14. **【补规范】** 114988e「Each one planting itself in the sides of Stark's neck. [SEP] Stark's neck was hit twice.」—— 三人各持一说，确认归哪类后写进规范
15. **【补规范】** 115830n「The avenue on the left leads towards the pointed Divan Tower (Divan Kulesi), at the foot of which lie the Council Chamber and the Grand Vezir's Office. [SEP] The avenue does not lead farther than the Grand Vezir's Ofiice.  」—— 三人各持一说，确认归哪类后写进规范
16. **【补规范】** 116059n「These days, newspaper writers are no longer allowed the kind of license he took. [SEP] Newspaper writers need to be more factual and careful these days.」—— 三人各持一说，确认归哪类后写进规范
17. **【补规范】** 118141n「it can't last seven years but it can last five IBM says let's throw it away Leading Edge will say we'll buy it from you [SEP] The new computer wont last for seven years.」—— 三人各持一说，确认归哪类后写进规范
18. **【补规范】** 119901n「Most pundits side with bushy-headed George Stephanopoulos ( This Week ), arguing that only air strikes would be politically palatable. [SEP] George's stance on air strikes has gained a large pundit following.」—— 三人各持一说，确认归哪类后写进规范
19. **【补规范】** 121360e「The tip was hooked towards the edge, the same way the tips are hammered for knives used for slaughter. [SEP] They were weapons used to kill.」—— 三人各持一说，确认归哪类后写进规范
20. **【补规范】** 123703c「Specifically, by defining mission improvement objectives, senior executives determine whether their organization needs a CIO who is a networking/marketing specialist, business change agent, operations specialist, policy/oversight manager, or any combination thereof. [SEP] A CIO does not need to be an operations specialist.」—— 三人各持一说，确认归哪类后写进规范
21. **【补规范】** 123953e「'These are human lives. [SEP] These are Hunan lives」—— 三人各持一说，确认归哪类后写进规范
22. **【补规范】** 124839n「(A bigger contribution may or may not mean, I really, really support Candidate X.) Freedom of association is an even bigger stretch--one that Justice Thomas would laugh out of court if some liberal proposed it. [SEP] There were some liberals opposed to it.」—— 三人各持一说，确认归哪类后写进规范
23. **【补规范】** 125238c「If the collecting entity transfers the nonexchange revenue to the General Fund or another entity, the amount is accounted for as a custodial activity by the collecting entity. [SEP] Nonexchange revenue to the General Mills.」—— 三人各持一说，确认归哪类后写进规范
24. **【补规范】** 125910n「i don't know if you have a place there called uh or you probably have something similar we call it Service Merchandise [SEP] There is usually a similar place anywhere you go.」—— 三人各持一说，确认归哪类后写进规范
25. **【补规范】** 131910n「Las Vegas now seems poised to accept the multiple layers of its existence as a tourist city. [SEP] Las Vegas appeals to multiple types of people.」—— 三人各持一说，确认归哪类后写进规范
26. **【补规范】** 134446n「On the second point, Judge Newton said in a recent interview, I've heard this complaint a hundred times. [SEP] Judge Newton was not convinced by the second point.」—— 三人各持一说，确认归哪类后写进规范
27. **【补规范】** 135021n「you know we keep a couple hundred dollars um if that much charged on those which isn't too bad it's just your normal [SEP] We have money on there, which isn't great」—— 三人各持一说，确认归哪类后写进规范
28. **【补规范】** 136860n「Dole : We ought to agree that somebody else should do it. [SEP] Someone else we appoint will do it.」—— 三人各持一说，确认归哪类后写进规范
29. **【补规范】** 13714e「oh you went to the dollar movie yeah yeah they show up at the dollar movie right after they get come out you know they're usually not not that great or didn't do that great anyway let me see let me see another movie i watched uh i want to see is uh that new one uh [SEP] they are shown at the dollar movie theater immediately after they're released」—— 三人各持一说，确认归哪类后写进规范
30. **【补规范】** 13884c「I take it Americans have a higher opinion of morality than you have even. [SEP] I take it that you have an unusually high opinion of morality.」—— 三人各持一说，确认归哪类后写进规范

> 仅显示前 30 项，共 137 项。
