---
layout: post
title: "线代笔记（Week3）"
author: "evilkant"
date: 2023-03-24
categories: learning
tag: 数学
---
Week 3
---
### 线性变换的Nullity和Rank

考虑线性变换$T: V -> W$，定义

$T$的null space，记为$N(T)$；$T$的nullity，记为$nullity(T)$，如下

$$
N(T)=\{v\in V | Tv = 0\}\\
nullity(T)=dim(N(T))
$$

$T$的range，记为$R(T)$；$T$的rank，记为$rank(T)$，如下

$$
R(T)= \{w| Tv=W, v\in V\}\\
rank(T) = dim(R(T))
$$

两个极端的例子：零变换$T(v)=0$的nullity为n，恒等变换$T(v)=v$的rank为n。

### 维度定理
记$dim(V)=n$
> $n = nullity(T) + rank(T)$


Proof:
记$dim(N(T))=k,k\leq n$, 只需证明$dim(R(T)) = n - k$
让$\\{v_1, ..., v_k\\}$作为$N(T)$的一组基，显然这是线性无关的$V$的一个向量子集，根据Replacement Theorem（Week2）的推论，必然被$V$的某一组基包括，记该基为$\\{v_1, ..., v_k, v_{k+1}, ...v_{n}\\}$
接下来证明$S=\\{Tv_{k+1}, ..., Tv_{n}\\}$构成$R(T)$的基。

（1）首先证明$span(S)=R(T)$

考虑$R(T)$中的一个典型向量$w$, 根据定义有$T(v)=w, v\in V$，而$v=a_1v_1 + ... + a_nv_n$，由于$T$是线性变换，有$Tv=a_1Tv_1 + ... + a_nTv_n$，由于$\\{v_1, ..,v_k\\}$是$N(T)$的基，有$v=a_{k+1}Tv_{k+1}+...+a_n Tv_n$，故有$span(S)=R(T)$

（2）然后证明$S$线性无关

假设$S$线性相关，则存在一组不全为0的数$b_{k+1},...,b_n$使得$b_{k+1} Tv_{k+1}+...+b_nTv_{n} = 0$，即$T(b_{k+1}v_{k+1} + ... + b_n v_n)=0$，即$v'=b_{k+1}v_{k+1} + ... + b_n v_n \in N(T)$，所以$v' = c_1v_1+...+c_k v_k$，所以有$c_1v_1+...+c_k v_k - (b_{k+1}v_{k+1} + ... + b_n v_n)=0$，意味着$\\{v_1, ..., v_k, v_{k+1}, ...v_{n}\\}$线性相关，矛盾，故$S$线性无关

综上，$S=\\{Tv_{k+1}, ..., Tv_{n}\\}$构成$R(T)$的基，故$dim(R(T)) = n - k$，故$n = nullity(T) + rank(T)$，证毕。