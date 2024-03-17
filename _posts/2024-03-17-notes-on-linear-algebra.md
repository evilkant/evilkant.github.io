---
layout: post
title: "线代笔记"
author: "evilkant"
date: 2023-03-17
categories: jekyll update
tag: 数学
---

学习陶哲轩的[lecture notes](https://terrytao.files.wordpress.com/2016/12/linear-algebra-notes.pdf)产生的笔记。这也未尝不是一个线性变换:D

---

线性代数研究线性变换(linear transformation)的代数性质(algebraic properties)。

变换(transformation)是任何把输入转换为输出的过程，和函数、映射等概念类似。

线性变化是保留向量加法(vector addition)和标量乘法(scalar multiplication)的变换。

$$
F(aX+bY) = aF(X) + bF(Y)
$$

牛顿第二定律F=ma，即a = F/m，就是一个（向量的）线性变换：力变为原来的k倍，加速度也变为原来的k倍；两个力产生的加速度的和等于两个力的和产生的加速度。

代数(algebra)主要关心对象之间的相等关系(equating objects)，另一个常见的数学分支——组合学(combinatoric)，关心的是计数对象(counting objects)。

---

线性代数关心的对象主要是向量(vector)和向量空间(vector space)。

向量空间是任何满足下述条件的对象的集合(collection of objects) V：

- V上定义向量加法(vector addition)和标量乘法(scalar multiplication)两种操作
- 向量加法和标量乘法需要满足若干规则，比如交换律、结合律、分配律等
- V对于向量加法和标量乘法封闭：对V中元素做这两个操作的结果仍在V中
- V需要包括零向量(additive identity)和各元素的逆元(additive inverse)

向量即向量空间中的元素。

这是一个非常抽象的定义，在该定义下，三维空间可以是一个向量空间，多项式函数的集合也可以是一个向量空间。这是一种强大的思维方式：不关心对象是什么，只关心对象能做什么。用程序设计的术语来说，不关心实现，只关心接口。

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

Proof Sketch: only if部分trivial，if部分利用-v = -1(v)。

---

从向量空间V中的一组向量出发怎么构建一个向量子空间？最简单的方式就是考虑这组向量的**线性组合**。

$$
向量集合S=\{v_1, ..., v_n\}的线性组合是任何形如v=a_1v_1+...+a_nv_n的向量
$$

向量集合S的所有线性组合构成S的Span（记为Span(s)）。可以证明Span(s)是V的一个子向量空间。

我们说向量集合S是线性相关(linear dependent)的，如果

$$
存在一组非全零的数a_1,...,a_n使得a_1v_1+...+a_nv_n=0
$$

否则说S是线性无关(linear independent)

不妨设$a_1$非零，那么$v_1$可以写作$v_2, ..., v_n$的线性组合，所以在线性组合中可以用$v_2, ..., v_n$来替换掉$v_1$，也就是说$v_1$是冗余的。向量集合线性相关就是说集合中存在冗余向量。

$$
我们说v_1, ..., v_n构成向量空间V的基(basis)，当且仅当，S张成V，而且S线性无关。
$$

可以证明，V的任何一组基，其中向量的数目（基数）相同，这个数目被定义为向量空间V的维度。

