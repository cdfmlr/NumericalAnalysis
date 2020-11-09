# 实验八 矩阵特征值及特征向量计算

## 一、实验目的

1. 掌握求矩阵的主特征值（即按模最大的特征值）和主特征向量的幂法；
2. 初步了解幂法的加速。

## 二、实验过程和结果

### 1. 正幂法的实现

```python
def power_iteration(A, m0=1, u0=None, eps=1e-8, max_steps=500, verbose=False):
    """正幂法（power iteration a.k.a. the power method）
    计算矩阵 A 的按模最大特征值、特征向量。
    
    Args:
        A:  np_array_like 待求特征值的矩阵 (nxn)
        m0: float 初始特征值 default m0=1
        u0: np_array_like 初始特征向量（n） default u0=None: 取 u0 = (1, 1, ..., 1)
        eps: float 精度要求 default eps=1e-8
        max_steps: int 最大迭代次数 default max_steps=1000
        verbose: bool, 若为 True 则打印出每一步的结果 default verbose=False
        
    Returns:
        (m, u, k): 在 max_steps 次迭代以内得到第一组的满足 eps 的结果
            m: float 所求主特征值
            u: np.array 相应的特征向量
            k: int 迭代次数
        
    Raises:
        ValueError: 给定参数 A u0 尺寸不匹配
        Exception:  无法在max_steps 次迭代以内得到满足精度 eps 的结果
    """
    ...
```

（这里只保留函数的声明和文档注释，具体实现源码见：[ex8/src/power_method.py](https://github.com/cdfmlr/NumericalAnalysis/blob/master/ex8/src/power_method.py)）

程序流程图：

![截屏2020-11-09 09.40.23](https://tva1.sinaimg.cn/large/0081Kckwly1gkiob1rk2ij319y0u077f.jpg)

算一个课本上的例子（P159 例1）作为测试：

![截屏2020-11-09 09.44.54](https://tva1.sinaimg.cn/large/0081Kckwly1gkiofqrf5gj30l80b676c.jpg)

计算一个比较大的随机矩阵，和 NumPy 求得得结果做比较：

![截屏2020-11-09 09.45.54](https://tva1.sinaimg.cn/large/0081Kckwly1gkiogstus0j30lm06j3ze.jpg)

### 2. 反幂法的实现

反幂法的代码实现在框架上和正幂法相同，只有迭代中值更新的算法，以及最后输出时的取值有所不同：

```python
def inverse_iteration(A, m0=1, u0=None, eps=1e-8, max_steps=500, verbose=False):
    """反幂法（inverse iteration a.k.a. inverse power method）
    计算矩阵 A 的按模最小特征值、特征向量。
    """
    ...
    for k in range(int(max_steps)):
        ...
		v = np.linalg.solve(A, u)
        mi = np.argmax(np.abs(v))
        m = v[mi]
        u = v / m
        ...
    ...
    return 1/m, u, k+1
```

（`...`代表和正幂法相同的代码，完整实现见：[ex8/src/inverse_power.py](https://github.com/cdfmlr/NumericalAnalysis/blob/master/ex8/src/inverse_power.py)）

调用结果：

![截屏2020-11-09 09.53.07](https://tva1.sinaimg.cn/large/0081Kckwly1gkiooayhb2j30lb0dmacx.jpg)

在反幂法中解了一个线性方程组，而且这个方程组是系数矩阵始终不变的，所以可以考虑调用实验6实现的 LU 分解法来求解：

```python
def inverse_iteration(A, m0=1, u0=None, eps=1e-8, max_steps=500, verbose=False):
    """反幂法（inverse iteration a.k.a. inverse power method）
    计算矩阵 A 的按模最小特征值、特征向量。
    """
    ...
    lupA = lu(A)  # lupA = (l, u, p)
    for k in range(int(max_steps)):
        ...
		v = solve_lu(u, *lupA)
        ...
    ...
```

（同样略去了相同代码，完整实现见：[ex8/src/inverse_power.py](https://github.com/cdfmlr/NumericalAnalysis/blob/master/ex8/src/inverse_power.py) ，其中 LU 分解的程序来自实验6： [ex6/src/lu.py](https://github.com/cdfmlr/NumericalAnalysis/blob/master/ex6/src/lu.py)）

调用测试：

![截屏2020-11-09 10.00.10](https://tva1.sinaimg.cn/large/0081Kckwly1gkiovqsxbwj30m50deacz.jpg)

事实上，由于这里调用的 LU 分解算法相当原始，没有做任何计算上的优化，所以计算效率并不高。在不严谨的测试中可以看到，这里对于同一个问题，调用 LU 分解要远慢于使用 NumPy 来解方程：

![截屏2020-11-09 10.02.57](https://tva1.sinaimg.cn/large/0081Kckwly1gkioyjp12mj30lz034aag.jpg)

（这个测试的具体方法可以在这个 Jupyter Notebook 中找到： [ex8/src/ex8.ipynb](https://github.com/cdfmlr/NumericalAnalysis/blob/master/ex8/src/ex8.ipynb)）

### 3. 原点位移法的实现

```python
def origin_translation(A, p, x0=None, eps=1e-8, max_steps=1000, verbose=False):
    """原点位移算法 (没搜到这个方法英文是什么，随便写的 origin_translation)
    
    Args:
        A:  np_array_like, 待求特征值的矩阵 (nxn)
        p:  float 位移因子
        x0: np_array_like, 初始向量（n）, 要求 max(abs(x0)) == 1
                default x0=None: 取 x0 = (1, 1, ..., 1)
        eps: float, 控制精度 default eps=1e-8
        max_steps: 最大迭代次数 default max_steps=1000
        verbose: 打印出每步的结果，default verbose=False
    
    Returns:
        (eig, x, k)
            eig: float, A 的靠近 p 的特征值
            x: np.array, 单位化的特征向量
            k: int, 迭代次数
        
    Raises:
        ValueError: 给定参数 A 和 x0 尺寸不匹配，或 x0 = 0
        Exception:  无法在max_steps 次迭代以内得到满足精度 eps 的结果
    """
    ...
```

（完整实现见：[ex8/src/origin_translation.py](https://github.com/cdfmlr/NumericalAnalysis/blob/master/ex8/src/origin_translation.py)）

算法流程图：

![截屏2020-11-09 10.12.07](https://tva1.sinaimg.cn/large/0081Kckwly1gkip85wx1yj31250u042h.jpg)

调用测试：

![截屏2020-11-09 10.15.38](https://tva1.sinaimg.cn/large/0081Kckwly1gkipbrl8qhj30m704fdgf.jpg)

### 4. 加速法

用动态原点位移算法加速求解按模最大特征值：

```python
def accelerating_max_val_eig(A, x0=None, eps_pi=1e-1, eps_ot=1e-8, max_steps_pi=1000, max_steps_ot=1000, verbose=False):
   """动态原点位移算法求按模最大特征值
    
    Args:
        A:  np_array_like, 待求特征值的矩阵 (nxn)
        x0: np_array_like, 初始向量（n）, default x0=None: 取 x0 = (1, 1, ..., 1)
        eps_pi: float,「正幂法」迭代的控制精度 default eps_pi=1e-1
        eps_ot: float,「原点位移」算法的控制精度，须满足 eps > eps_ot，default eps_ot=1e-8
        max_steps_pi: int,「正幂法」迭代的最大迭代次数 default max_steps_pi=1000
        max_steps_ot: int,「原点位移」算法的最大迭代次数 default max_steps_ot=1000
        verbose: bool: True 则打印出「正幂法」、「原点位移」的完整迭代过程 default verbose=False
    
    Returns:
        (eig, eigv, k)
            eig: float, A 的按模最大特征值
            eigv: np.array, 单位化的特征向量
            k: 迭代次数
        
    Raises:
        ValueError: 参数不合法
        Exception:  无法在max_steps 次迭代以内得到满足精度 eps 的结果
    """
    eig, eigv, k_pi = power_iteration(A, u0=x0, 
                                      eps=eps_pi, max_steps=max_steps_pi, 
                                      verbose=verbose)
    eig, eigv, k_ot = origin_translation(A, eig, x0=eigv, 
                                         eps=eps_ot, max_steps=max_steps_ot, 
                                         verbose=verbose)
    return eig, eigv, k_pi + k_ot
```

（完整实现见：[ex8/src/accelerate.py](https://github.com/cdfmlr/NumericalAnalysis/blob/master/ex8/src/accelerate.py)）

调用测试：

![截屏2020-11-09 10.27.45](https://tva1.sinaimg.cn/large/0081Kckwly1gkipodpropj30ma08f75p.jpg)

用动态原点位移算法加速求解按模最小特征值（完整实现见：[ex8/src/accelerate.py](https://github.com/cdfmlr/NumericalAnalysis/blob/master/ex8/src/accelerate.py)）只需把上述代码中的 `power_iteration` 改为 `inverse_iteration`。调用测试：

![截屏2020-11-09 10.28.19](https://tva1.sinaimg.cn/large/0081Kckwly1gkipoxxqyfj30m2088gmy.jpg)















### 5. 实验内容题目

![截屏2020-11-09 10.36.03](https://tva1.sinaimg.cn/large/0081Kckwly1gkipwzd0nwj30nx0bxwgz.jpg)

![截屏2020-11-09 10.36.36](https://tva1.sinaimg.cn/large/0081Kckwly1gkipxk9mtyj30nw073wfj.jpg)



解：

![截屏2020-11-09 10.34.20](https://tva1.sinaimg.cn/large/0081Kckwly1gkipv6jf14j30m80d240d.jpg)

得到结果：

![截屏2020-11-09 10.37.54](https://tva1.sinaimg.cn/large/0081Kckwly1gkipyx2tmkj30m80ckjtg.jpg)

## 三、思考题分析解答

> 幂法收敛速度取决于什么？为什么？

从幂法的推导中最后得到有 $\lambda_1\approx \frac{x_i^{(k+1)}}{x_i^{(k)}}$，所以幂法的收敛速度取决于主特征值和第二大特征值的比值大小： $|\frac{\lambda_2}{\lambda_1}|$ ，这个值越小收敛越快。当这个比值接近 1 的时候，收敛的速度就比较慢了。

## 四、重点难点分析

1. 求矩阵的按模最大的主特征值和主特征向量的幂法；
2. 幂法的动态原点位移加速。

