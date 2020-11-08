# 实验七 线性方程组的迭代解法

## 一、实验目的

1. 掌握解线性方程组的雅可比迭代和高斯-塞德尔迭代算法；
2. 初步掌握解线性方程组的迭代算法的设计方法。

## 二、实验过程和结果

有唯一解的非奇异线性方程组 $Ax=b$，可以等价为不动点方程 $x=Bx+f$，由此建立迭代公式：
$$
x^{(k+1)}=Bx^{(k)}+f\qquad k=0,1,2,\dots
$$
通过特定方式构建 $B$ 和 $f$，给定初始向量 $x^{(0)}$ 即可迭代解出原方程的数值近似解。

### 1. 雅可比迭代法

把系数矩阵 $A$ 分裂成 $A=D-L-U$，其中 $D=diag(a_{11},\dots,a_{nn})$，$-L$ 和 $-U$ 分别是 $A$ 的下三角和上三角部分。则 Jacobi 迭代法就是取 $B=D^{-1}(L+U),\quad f=D^{-1}b$：
$$
x^{(k+1)}=D^{-1}(L+U)x^{(k)}+D^{-1}b,\qquad k=0,1,2,\dots
$$
编程实现（这里只保留函数声明头和简化的文档注释，具体实现源码见https://github.com/cdfmlr/NumericalAnalysis/blob/master/ex7/src/jacobi_iter.py）：

```python
def jacobi_iter(A, b, x0=None, eps=1e-5, max_steps=5000, verbose=False):
    """雅可比（Jacobi）迭代法求解线性方程组: A @ x = b
    
    Args:
        A:  np_array_like, 系数矩阵
        b:  np_array_like, 右端常数
        x0: np_array_like, 迭代初值 default x0=None: use a random array.
        eps: float, 精度要求
        max_steps: int, 最大迭代次数
        verbose: bool, 如果计算成功，打印出结果及迭代次数
        
    Returns:
        x: 方程组的解
        
    Raises:
        ValueError: 参数 A, b 和 x0 存在形状不匹配
        Expection:  达到最大迭代次数，仍不满足精度
    """
    ...
```

具体的程序流程图：

![截屏2020-11-08 15.39.15](https://tva1.sinaimg.cn/large/0081Kckwly1gkht284vqoj313i0u041e.jpg)

调用测试：

![截屏2020-11-08 15.41.10](https://tva1.sinaimg.cn/large/0081Kckwly1gkht44li26j30jo02d3yo.jpg)



### 2. 高斯-塞德尔迭代法

与 Jacobi 迭代类似，做  $A=D-L-U$ 的分解之后，Gauss Seidel 迭代表示为：
$$
x^{(k+1)}=(D-L)^{-1}Ux^{(k)}+(D-L)^{-1}b,\qquad k=0,1,2,\dots
$$
也就是 $(1)$ 式取 $B=(D-L)^{-1}U$，$f=(D-L)^{-1}b$ 的情形。

编程实现和 Jacobi 迭代类似，只需修改 B 和 f 的求解方法：

```python
def gauss_seidel_iter(A, b, x0=None, eps=1e-5, max_steps=5000, verbose=False):
    ...
    inv_DsL = np.linalg.pinv(D - L)
    
    B = inv_DsL @ U
    f = inv_DsL @ b
    ...
```

（完整代码实现见：https://github.com/cdfmlr/NumericalAnalysis/blob/master/ex7/src/gauss_seidel_iter.py）

调用测试：

![截屏2020-11-08 15.50.25](https://tva1.sinaimg.cn/large/0081Kckwly1gkhtdr9v84j30lx01taa7.jpg)

### 3. 逐次超松弛迭代法

逐次超松弛（Successive over-relaxation，SOR）迭代法引入一个**松弛因子** $\omega>0$，迭代方程：
$$
x^{(k+1)}=
(D-\omega L)^{-1}
\left((1-\frac{1}{\omega})D+\omega U\right)
x^{(k)}
+
\omega(D-\omega L)^{-1}b,
\qquad k=0,1,2,\dots
$$
也就是 $(1)$ 式取 $B=(D-\omega L)^{-1}\left((1-\frac{1}{\omega})D+\omega U\right)$，$f=\omega(D-\omega L)^{-1}b$ 的情形。

编程实现依然和 Jacobi 迭代类似，只需修改 B 和 f 的求解方法，此处不在赘述。

调用测试：

![截屏2020-11-08 16.01.46](https://tva1.sinaimg.cn/large/0081Kckwly1gkhtpkvkrzj30ju01sq32.jpg)

（完整代码实现见：https://github.com/cdfmlr/NumericalAnalysis/blob/master/ex7/src/sor.py）

### 4. 三个算法的封装与比较

上述的 Jacobi 迭代法、Gauss Seidel 迭代法、SOR 迭代法的代码实现相当类似，仅有 B、f 的计算方法有差异，所以完全可以用简单的面向对象方法进行封装，避免代码重复：

![si](https://tva1.sinaimg.cn/large/0081Kckwly1gkhu0c1kefj319w0osmyq.jpg)

（具体的代码实现见：https://github.com/cdfmlr/NumericalAnalysis/blob/master/ex7/src/simple_iteration.py）

对于实验内容中的问题分别使用 Jacobi、Gauss-Seidel 迭代以及取不同的松弛因子的 SOR，在相同的初值、精度要求下，得到的计算结果如下：

![截屏2020-11-08 16.18.27](https://tva1.sinaimg.cn/large/0081Kckwly1gkhu6ycuf0j30p9083t9v.jpg)

可以看到，Gauss-Seidel 在收敛速度上优于 Jacobi 迭代。

取不同松弛因子会对 SOR 的收敛速度有影响，可以进一步实验来寻找一个较优的松弛因子：

```python
for w in np.linspace(0.1, 1.9, 100):
    rs = SOR(A, b, w)(x0=[0, 0, 0, 0], eps=1e-9, verbose=True)
```

通过一系列计算，得到不同松弛因子取值与迭代次数的关系，如下图所示：

![截屏2020-11-08 16.57.24](https://tva1.sinaimg.cn/large/0081Kckwly1gkhvbfjr66j30b707cq32.jpg)

容易确定其中最优的迭代次数为 `17` 次，对应的松弛因子为 `1.2272727272727273` 或 `1.2454545454545456`，最优的松弛因子应该在这两个值之间，容易利用二分法进一步逼近最优松弛因子。这里我认为进一步试算意义不大了，故不在继续。

（具体求解过程源码见：https://github.com/cdfmlr/NumericalAnalysis/blob/master/ex7/src/ex7.ipynb）





## 三、思考题分析解答

（1）

![截屏2020-11-08 18.23.43](https://tva1.sinaimg.cn/large/0081Kckwly1gkhxta3dj6j31f80bumz8.jpg)

解：

首先把问题录入计算机，并使用已有工具求出一个参考的解：

![截屏2020-11-08 18.24.16](https://tva1.sinaimg.cn/large/0081Kckwly1gkhxttm2p9j30uk045mxd.jpg)

直接利用 Gauss-Seidel 求解，会遇到无法收敛的问题：

![截屏2020-11-08 18.28.12](https://tva1.sinaimg.cn/large/0081Kckwly1gkhxxx74b6j30t8091mzh.jpg)

手动做一些行变换，使其严格对角占优，就可以解了：

![截屏2020-11-08 18.51.21](https://tva1.sinaimg.cn/large/0081Kckwly1gkhym221spj30pl04dmxk.jpg)

（具体求解过程源码见：https://github.com/cdfmlr/NumericalAnalysis/blob/master/ex7/src/ex7.ipynb）







（2）

![截屏2020-11-08 18.36.06](https://tva1.sinaimg.cn/large/0081Kckwly1gkhy6729bwj31ei0ea0w5.jpg)

解：

首先把问题录入计算机（随意取 $b=[1,1,1]$），并求出参考的解：

![截屏2020-11-08 18.40.56](https://tva1.sinaimg.cn/large/0081Kckwly1gkhyb6vnpzj30ln076q3e.jpg)

分别用 Jacobi 和 Gauss-Seidel 迭代计算 $A_1x=b$， Jacobi 迭代正确的到了结果，而 Gauss-Seidel 方法没有收敛：![截屏2020-11-08 18.48.08](https://tva1.sinaimg.cn/large/0081Kckwly1gkhyipfvmqj30pi0badi2.jpg)

计算 $A_2x=b$ 时则相反， Jacobi 迭代不收敛，而 Gauss-Seidel 可以计算出结果：

![截屏2020-11-08 18.47.25](https://tva1.sinaimg.cn/large/0081Kckwly1gkhyhxctiwj30pe0bd0v6.jpg)

## 四、重点难点分析

1. 掌握解线性方程组的雅可比迭代和高斯-塞德尔迭代算法；
2. 初步掌握解线性方程组的迭代算法的设计方法。

