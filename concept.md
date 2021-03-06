1. 质数：质数又称素数。一个大于 1 的自然数，除了 1 和它自身外，不能整除其他自然数的数叫做质数；否则称为合数。

2. 闰年：  
   普通年:能被 4 整除但不能被 100 整除的年份为普通闰年。（如 2004 年就是闰年，1999 年不是闰年。
   世纪年:能被 400 整除的为世纪闰年。（如 2000 年是闰年，1900 年不是闰年）。

3. 阶乘：  
   一个正整数的阶乘（factorial）是所有小于及等于该数的正整数的积，并且 0 的阶乘为 1。自然数 n 的阶乘写作 n!。

4. 斐波那契数列：  
   指的是这样一个数列 0, 1, 1, 2, 3, 5, 8, 13,特别指出：第 0 项是 0，第 1 项是第一个 1。从第三项开始，每一项都等于前两项之和。

5. 阿姆斯特朗数：
   如果一个 n 位正整数等于其各位数字的 n 次方之和,则称该数为阿姆斯特朗数。例如 1^3 + 5^3 + 3^3 = 153

6. 二进制：二进制是计算技术中广泛采用的一种数制。二进制数据是用 0 和 1 两个数码来表示的数。它的基数为 2，进位规则是“逢二进一”，借位规则是“借一当二”。

7. 八进制：Octal，缩写 OCT 或 O，一种以 8 为基数的计数法，采用 0，1，2，3，4，5，6，7 八个数字，逢八进 1。一些编程语言中常常以数字 0 开始表明该数字是八进制。

8. 十六进制：是计算机中数据的一种表示方法。同我们日常生活中的表示法不一样。它由 0-9，A-F 组成，字母不区分大小写。与 10 进制的对应关系是：0-9 对应 0-9；A-F 对应 10-15；N 进制的数可以用 0~(N-1)的数表示，超过 9 的用字母 A-F。

9. 最大公约数：指两个或多个整数共有约数中最大的一个。

10. 最小公倍数：两个或多个整数公有的倍数叫做它们的公倍数，其中除 0 以外最小的一个公倍数就叫做这几个整数的最小公倍数。

11. 邻近算法(KNN)：数据挖掘分类技术中最简单的方法之一。所谓 K 最近邻，就是 k 个最近的邻居的意思，说的是每个样本都可以用它最接近的 k 个邻居来代表。

12. 分类（classification）：将实例数据划分到合适的类别中。应用实例：判断网站是否被黑客入侵（二分类 ），手写数字的自动识别（多分类）。

13. 回归（regression）：主要用于预测数值型数据。应用实例：股票价格波动的预测，房屋价格的预测等。

14. 决策树(Decision Tree）是在已知各种情况发生概率的基础上，通过构成决策树来求取净现值的期望值大于等于零的概率，评价项目风险，判断其可行性的决策分析方法，是直观运用概率分析的一种图解法。

15. 贝叶斯定理：是关于随机事件 A 和 B 的条件概率（或边缘概率）的一则定理。其中 P(A|B)是在 B 发生的情况下 A 发生的可能性。

16. 朴素贝叶斯原理：

    - 提取所有文档中的词条并进行去重
    - 获取文档的所有类别
    - 计算每个类别中的文档数目
    - 对每篇训练文档:
      - 对每个类别:
        - 如果词条出现在文档中-->增加该词条的计数值（for 循环或者矩阵相加）
        - 增加所有词条的计数值（此类别下词条总数）
    - 对每个类别:
      - 对每个词条:
        - 将该词条的数目除以总词条数目得到的条件概率（P(词条|类别)）
    - 返回该文档属于每个类别的条件概率（P(类别|文档的所有词条)）

17. 条件概率：指事件 A 在另外一个事件 B 已经发生条件下的发生概率。条件概率表示为：P（A|B），读作“在 B 的条件下 A 的概率”。[详细](https://github.com/YaliixxG/Maths-and-AIlearning/blob/master/Conditional-probability.md)

18.数据结构：数据元素相互之间存在的一种和多种特定的关系集合，包括两个部分组成逻辑结构，存储结构。[详细](https://github.com/YaliixxG/Maths-and-AIlearning/blob/master/data-structure.md)
