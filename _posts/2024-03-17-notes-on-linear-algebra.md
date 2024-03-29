---
layout: post
title: "线代笔记（Week1-2）"
author: "evilkant"
date: 2023-03-21
categories: learning
tag: 数学
---

学习陶哲轩的[lecture notes](https://terrytao.files.wordpress.com/2016/12/linear-algebra-notes.pdf)产生的笔记。这也未尝不是一个线性变换:D

---

线性代数研究线性变换(linear transformation)的代数性质(algebraic properties)。

变换(transformation)是任何把输入转换为输出的过程，和映射基本等价。

线性变化是保留向量加法(vector addition)和标量乘法(scalar multiplication)的变换。

数学上说一个映射$f$保留了一个操作$g$，就是在说$f(g(x_1, x_2, ...,x_n))=g(f(x_1), f(x_2), ...f(x_n))$，换句话说先做操作再做映射和先做映射再做操作的结果是一样的。

保留向量加法和标量乘法，用数学语言表达就是

$$
F(aX+bY) = aF(X) + bF(Y)
$$

比如牛顿第二定律$F=ma$，即$a = F/m$，就是一个（向量的）线性变换：力变为原来的$k$倍，加速度也变为原来的$k$倍；两个力产生的加速度的和等于两个力的和产生的加速度。

代数(algebra)主要关心对象之间的相等关系(equating objects)，另一个常见的数学分支——组合学(combinatorics)，关心的是计数对象(counting objects)。

---

线性代数关心的对象主要是向量(vector)和向量空间(vector space)。

向量空间是任何满足下述条件的对象的集合(collection of objects) V：

- V上定义向量加法(vector addition)和标量乘法(scalar multiplication)两种操作
- 向量加法和标量乘法需要满足若干规则，比如交换律、结合律、分配律等
- V对于向量加法和标量乘法封闭：对V中元素做这两个操作的结果仍在V中
- V需要包括零向量(additive identity)和各元素的逆元(additive inverse)

向量即向量空间中的元素。

这是一个非常抽象的定义，在该定义下，三维空间可以是一个向量空间，函数的集合、甚至无穷序列的集合都可以是一个向量空间。这是一种强大的思维方式：不关心对象是什么，只关心对象能做什么。用程序设计的术语来说，不关心实现，只关心接口。

这也是一个公理化定义，从上述公理（完整规则参见原notes）可以产生许多（显然的）推论，比如notes中留作练习的

$$
0\vec{v} = \vec{0} \\
Proof: LHS = 0\vec{v} + \vec{0} = 0\vec{v}+\vec{v}+(-\vec{v})=(0+1)\vec{v}+(-\vec{v})=\vec{v}+(-\vec{v})=\vec{0}=RHS
$$

或者

$$
a\vec{0} = \vec{0}\\
Proof: LHS = a(0\vec{v})=0(a\vec{v})=\vec{0}=RHS
$$

定义向量空间S是向量空间V的子向量空间，如果S是V的一个子集。

不难证明，如果S是向量空间V的一个子集，那么S是一个向量空间当且仅当S对于向量加法和标量乘法是封闭的。

Proof Sketch: only if部分trivial，if部分利用$-v = -1(v)$。

---

从向量空间V中的一组向量出发怎么构建一个向量子空间？最简单的方式就是考虑这组向量的**线性组合(linear combination)**。

$$
向量集合S=\{v_1, ..., v_n\}的线性组合是任何形如v=a_1v_1+...+a_nv_n的向量
$$

向量集合$S$的所有线性组合构成$S$的**张成空间(span)**，记为$Span(S)$。

$Span(S)$不仅是V的一个子向量空间，而且是包括$S$的最小的子向量空间。

如果$Span(S)=V$，那么我们说$S$是$V$的**生成集(spanning set)**。

如果$Span(S)=V$，那么再往$S$里加向量对于$V$的生成/张成已经没有帮助了，但我们能问是否可以从$S$中减去某些向量后仍然生成$V$。

如果

$$
存在一组非全零的数a_1,...,a_n使得a_1v_1+...+a_nv_n=0
$$

那么我们说向量集合$S$是线性相关(linear dependent)的，否则说S是线性无关(linear independent)。

如果$S$线性相关，不失一般性，假设设$a_1$非零，那么$v_1$可以写作$v_2, ..., v_n$的线性组合，所以在线性组合中可以用$v_2, ..., v_n$来替换掉$v_1$，也就是说$v_1$是冗余的，踢掉$v_1$后，$S$中剩下的元素仍然可以生成$V$。

而如果$S$线性无关，我们无法踢掉其中的任一向量，此时$S$不仅是一个生成集，还是一个“最小生成集”，这和图的最小生成树是非常类似的，不过在线性代数里，我们管这个“最小生成集”叫**基(basis)**。

$$
我们说S=\{v_1, ..., v_n\}构成向量空间V的基(basis)，当且仅当，S张成V，而且S线性无关。
$$

$V$的基向量就好比是$V$的原子，在这个意义上，基类似自然数集合中的质数，而且跟质因数分解定理类似，如果$S$是$V$的基，那么$V$中向量都有唯一的$S$的线性组合表示。
举些例子：集合$S=\\{(1,0), (0,1)\\}$是$R^2$的基，无穷集合$S=\\{1, x, x^2, ...\\}$是多项式向量空间的基。
一个向量空间可以有多组基，比如$\\{(0,1), (1,0)\\}$和$\\{(1,1), (1,-1)\\}$都是$R^2$的基。
但可以证明，$V$的任何一组基，其向量的数目（基数）相同，这个数目被定义为向量空间$V$的维度。
首先证明如下定理：

>如果$S$是向量空间$V$的一个基数为$n$的子集，且$V=Span(S)$，$L$是$V$的一个基数为$m$的子集，且$L$线性无关，那么$n \geq  m$

Proof:

不妨记$S=\{s_1, ..., s_n\}$，$L=\{l_1, ..., l_m\}$。因为$V=Span(S)$且$L\subseteq V$，所以$l_1 = a_1s_1 + ... + a_ns_n$，$a_1,...,a_n$不可能全为零，否则$l_1=0$，这导致$L$线性相关，和前提矛盾。不妨让$a_1\neq 0$，那么$s_1 = \frac{2}{a_1}l_1 - \frac{a_2}{a_1}s_2 - 
...-\frac{a_n}{a_1}s_n$，即$s_1$可写作$S' = \{l_1,s_2, ...,s_n\}$的线性组合，既然$Span(S)=V$，那么$Span(S')=V$。

既然$Span(S')=V$，那么有$l_2=b_1l_1 + b_2s_2 ... + b_ns_n$，$b_2,...,b_n$不可能全为零，否则会导致$L$线性相关。不妨设$b_2\neq 0$，那么$s_2$可以写作$S''=\{l_1,l_2, s_3, ..., s_n\}$的线性组合，此时$Span(S'')=V$。

如果$n\lt m$，那么重复上述过程n次后，我们得到$Span(\{l_1,...,l_n\})=V$，意味着$l_m$可以由$l_1,...,l_n$线性组合得到，那么$L$是线性相关的，和题设矛盾。

所以一定有$n\geq m$。

因此下列推论成立：
>如果n个向量的$A$是$V$的一组基，m个向量的$B$是$V$的一组基，那么一定有$n=m$。

Proof：
因为$Span(A)=V$且$B$线性无关，所以有$n \geq m$。又因为$Span(B)=V$且$A$线性无关，所以又$n \leq m$。因此$n=m$。

---

考虑如下问题：给定$n$个数据点$\\{(x_1, y_1), (x_2, y_2), ..., (x_n, y_n)\\}$，求$f(x)$满足$f(x_i)=y_i$, 其中$i=1,...,n$。

并不容易直接猜到$f(x)$，但是考虑下述简化问题：求$f_1(x)$满足$f(x_1)=1$, $f(x_i)=0$, 其中$i=2,...,n$。

如果我们能求出$f_i(x)$，那么显然$f(x)=\sum_i y_if_i(x)$即符合题意的函数。

$f_i(x)$需要在$x_j (j\neq i)$处为0，故可令

$$
f_i(x) = C\prod_{j \neq i}(x-x_j)
$$

带入$f_i(x_i)=1$，可得$C=\frac{1}{\prod_{j \neq i}(x_i-x_j)}$，故

$$
f_i(x) = \frac{1}{\prod_{j \neq i}(x_i-x_j)} \prod_{j \neq i}(x-x_j)
$$

故有

$$
f(x) = \sum_i (\frac{y_i}{\prod_{j \neq i}(x_i-x_j)} \prod_{j \neq i}(x-x_j))
$$

$f(x)$即拉格朗日插值公式，插值效果如图：

![image](/assets/img/interpolate.png)
