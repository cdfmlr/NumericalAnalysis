# 算法流程图

这个文件中存放数值分析实验的各种算法的具体实现的程序流程图（只有报告（`ex?/report`）中用到的）。

这些流程图是使用 [flowchart.js](https://github.com/adrai/flowchart.js) 语法表达的。在例如 Typora 的 Markdown 编辑器中，可以直接看到这些流程图的渲染结果，其他方法参见 [cdfmlr/pyflowchart](https://github.com/cdfmlr/pyflowchart) 与 [adrai/flowchart.js](https://github.com/adrai/flowchart.js)。

## 非线性方程求根

### 二分法

```flow
st4321084112=>start: start dichotomy
io4321084304=>inputoutput: input: f, a, b, eps, eta, verbose
cond4321084624=>operation: raise ValueError('rootless interval: f(a) * f(b) < 0') if  ((f(a) * f(b)) > 0)
cond4321085584=>operation: print(f'n 	 (a, b) 	 f(x_n)') if  verbose
op4321086352=>operation: n = 0
cond4321086672=>condition: while (abs((b - a)) > eps)
op4321122000=>operation: x = ((a + b) / 2)
fx = f(x)
cond4321122640=>operation: print n (a, b) f(x) if  verbose
cond4321123344=>operation: break if  (abs(fx) <= eta)
cond4321123920=>condition: if ((f(a) * fx) < 0)
op4321122448=>operation: b = x
op4321123088=>operation: n += 1
op4321132752=>operation: a = x
op4321086864=>operation: x_final = ((a + b) / 2)
cond4321087248=>operation: print result: x_final if verbose
io4321133520=>inputoutput: output:  (x_final, n)
e4321133328=>end: end function return

st4321084112->io4321084304
io4321084304->op4321086352
op4321086352(right)->cond4321086672
cond4321086672(yes)->op4321122000
op4321122000->cond4321123344
cond4321123344->cond4321123920
cond4321123920(yes)->op4321122448
op4321122448->op4321123088
op4321123088(left)->cond4321086672
cond4321123920(no)->op4321132752
op4321132752->op4321123088
cond4321086672(no)->op4321086864
op4321086864->io4321133520
io4321133520->e4321133328


```

### 不动点迭代

```flow
st4413544336=>start: start fixed_point_iter
io4413544400=>inputoutput: input: phi, x_0, max_steps
op4413544720=>operation: x = x_0
cond4413545104=>operation: x = phi(x) while  i in range(max_steps)
io4413545616=>inputoutput: output:  x
e4413545168=>end: end function return

st4413544336->io4413544400
io4413544400->op4413544720
op4413544720->cond4413545104
cond4413545104->io4413545616
io4413545616->e4413545168
```

### 牛顿迭代法

```flow
st4490506512=>start: start newton_iter
io4490506576=>inputoutput: input: f, x_0, eps, eta, max_steps
op4490506896=>operation: x = x_0
cond4490507344=>condition: for i in range(max_steps)
op4490508880=>operation: x_next = (x - (f(x) / df(x)))
cond4490509072=>operation: break if  ((abs((x_next - x)) <= eps) or (abs(f(x)) <= eta))
op4490509584=>operation: x = x_next
io4490508688=>inputoutput: output:  x
e4490507792=>end: end function return

st4490506512->io4490506576
io4490506576->op4490506896
op4490506896(right)->cond4490507344
cond4490507344(yes)->op4490508880
op4490508880->cond4490509072
cond4490509072->op4490509584
op4490509584(left)->cond4490507344
cond4490507344(no)->io4490508688
io4490508688->e4490507792
```

### 单点截弦

```flow
st4396044944=>start: start single_point_truncation
io4396045008=>inputoutput: input: f, x_0, x_1, eps, eta, max_steps
op4396045328=>operation: x = x_1
cond4396045776=>condition: for i in range(max_steps)
op4396047056=>operation: x_next = (x - ((f(x) / (f(x) - f(x_0))) * (x - x_0)))
cond4396046160=>operation: break if  ((abs((x_next - x)) <= eps) or (abs(f(x)) <= eta))
op4396047952=>operation: x = x_next
io4396046544=>inputoutput: output:  x
e4396046224=>end: end function return

st4396044944->io4396045008
io4396045008->op4396045328
op4396045328->cond4396045776
cond4396045776(yes)->op4396047056
op4396047056->cond4396046160
cond4396046160->op4396047952
op4396047952(left)->cond4396045776
cond4396045776(no)->io4396046544
io4396046544->e4396046224


```

## 插值

### 拉格朗日插值

```flow
st4343026832=>start: start lagrange_interpolate
io4343026896=>inputoutput: input: points, simplify_result, verbose
op4343027216=>operation: x = Symbol('x')
op4343027792=>operation: L = 0
cond4343028048=>condition: for (i, (xi, yi)) in enumerate(points)
op4343050768=>operation: li = 1
cond4343052240=>condition: for j in range(len(points))
cond4343053584=>subroutine: continue if  (j == i)
op4343054160=>operation: (xj, yj) = points[j]
op4343054096=>operation: (xj, yj) = points[j]
li *= ((x - xj) / (xi - xj))
op4343050384=>operation: L += (yi * li)
io4343029328=>inputoutput: output:  L
e4343028176=>end: end function return

st4343026832->io4343026896
io4343026896->op4343027216
op4343027216->op4343027792
op4343027792(right)->cond4343028048
cond4343028048(yes)->op4343050768
op4343050768->cond4343052240
cond4343052240(yes)->cond4343053584
cond4343053584->op4343054096
op4343054096(left)->cond4343052240
cond4343052240(no)->op4343050384
op4343050384(top)->cond4343028048
cond4343028048(no)->io4343029328
io4343029328->e4343028176
```

### 差商

```flow
op4349394064=>operation: 差商缓存 = {}
st4349394512=>start: start difference_quotient
io4349394448=>inputoutput: input: f, xs
op4349415504=>operation: key = get_key(f, xs)
cond4349415760=>condition: if (key in 差商缓存)
io4349415824=>inputoutput: output:  差商缓存[key]
e4349416336=>end: end
cond4349416528=>condition: if (len(xs) == 1)
op4349417168=>operation: dq = f(xs[0])
op4349394256=>operation: 差商缓存[key] = dq
io4349416912=>inputoutput: output:  dq
e4349417104=>end: end
op4349416272=>operation: dq_h = difference_quotient(f, xs[:(- 1)])
dq_l = difference_quotient(f, xs[1:])
op4349417360=>operation: dq_l = difference_quotient(f, xs[1:])
op4349416016=>operation: dq = ((dq_l - dq_h) / (xs[(- 1)] - xs[0]))

op4349394064(right)->st4349394512
st4349394512->io4349394448
io4349394448->op4349415504
op4349415504->cond4349415760
cond4349415760(yes)->io4349415824
io4349415824->e4349416336
cond4349415760(no)->cond4349416528
cond4349416528(yes)->op4349417168
op4349417168->op4349394256
op4349394256->io4349416912
io4349416912->e4349417104
cond4349416528(no)->op4349416272
op4349416272->op4349416016
op4349416016->op4349394256
```

### 牛顿插值

```flow
st4425226768=>start: start newton_interpolate
io4425226832=>inputoutput: input: points, N_start, points_start, simplify_result, verbose
op4425227152=>operation: x = Symbol('x')
f = (lambda x: dict((points + points_start))[x])
op4425228240=>operation: xs = [p[0] for p in points_start]
N = N_start
cond4425228752=>condition: for point in points
sub4425229776=>subroutine: xs.append(point[0])
op4425229904=>operation: N += difference_quotient(f, xs, verbose) * prod([x - xi for xi in xs[:-1]])
cond4425227536=>operation: N = simplify(N) if  simplify_result
io4425230352=>inputoutput: output:  N
e4425228880=>end: end newton_interpolate

st4425226768->io4425226832
io4425226832->op4425227152
op4425227152->op4425228240
op4425228240->cond4425228752
cond4425228752(yes)->sub4425229776
sub4425229776->op4425229904
op4425229904(left)->cond4425228752
cond4425228752(no)->cond4425227536
cond4425227536->io4425230352
io4425230352->e4425228880
```

### 三次样条插值

```flow
st4456153232=>start: start spline3_interpolate
io4456153296=>inputoutput: input: points, simplify_result
op4456153616=>operation: 排序给定的点
ps = sorted(points, key=(lambda p: p[0]))
n = len(points)
op4456154064=>operation: 做一个点映射的函数
_f_dict = dict(ps)
f = (lambda x: _f_dict[x])
op4456154832=>operation: h = (lambda k: (ps[(k + 1)][0] - ps[k][0]))
hks = [h(0)]
op4456154384=>operation: D = np.zeros((n, n))
d = np.zeros(n)
cond4456155408=>condition: for k in range(1, (n - 1))
sub4456156560=>subroutine: hks.append(h(k))
(hk, hks1) = (hks[k], hks[(k - 1)])
_fra = (hks1 + hk)
mu = (hks1 / _fra)
ld = (hk / _fra)
op4456178256=>operation: D[(k, (k - 1))] = mu
D[(k, k)] = 2
D[(k, (k + 1))] = ld
op4456179344=>operation: d[k] = 6 * difference_quotient(f, [ps[k-1][0], ps[k][0], ps[k+1][0]])
op4456156048=>operation: 边界条件（Natural Boundary）
D[(0, 0)] = 1
D[((n - 1), (n - 1))] = 1
d[0] = 0
d[(n - 1)] = 0
op4456156624=>operation: M = np.linalg.solve(D, d)
op4456156496=>operation: piecewises = []
cond4456179728=>condition: for k in range((n - 1))
op4456179088=>operation: s  = M[k] * (ps[k+1][0] - _x) ** 3 / (6 * hks[k])
+ M[k+1] * (_x - ps[k][0]) ** 3 / (6 * hks[k])
+ (ps[k][1] - M[k] * hks[k]**2 / 6) * (ps[k+1][0] - _x) / hks[k]
+ (ps[k+1][1] - M[k+1] * hks[k]**2 / 6) * (_x - ps[k][0]) / hks[k]
cond4456157008=>operation: s = simplify(s) if  simplify_result
sub4456181712=>subroutine: piecewises.append((s, And(_x >= ps[k][0], _x <= ps[k+1][0])))
io4456179216=>inputoutput: output:  Piecewise(*piecewises)
e4456179472=>end: end function spline3_interpolate

st4456153232->io4456153296
io4456153296(right)->op4456153616
op4456153616->op4456154064
op4456154064->op4456154832
op4456154832->op4456154384
op4456154384(right)->cond4456155408
cond4456155408(yes)->sub4456156560
sub4456156560->op4456178256
op4456178256->op4456179344
op4456179344(left)->cond4456155408
cond4456155408(no)->op4456156048
op4456156048->op4456156624
op4456156624->op4456156496
op4456156496->cond4456179728
cond4456179728(yes)->op4456179088
op4456179088->cond4456157008
cond4456157008->sub4456181712
sub4456181712(left)->cond4456179728
cond4456179728(no)->io4456179216
io4456179216->e4456179472
```

## 数值积分

### 科特斯系数

```flow
st4550332880=>start: start function
costes_coefficient
io4550332944=>inputoutput: input: n, k
op4550333328=>operation: ckn = ((-1) ** (n - k)) / n * factorial(k) * factorial(n - k)
h = 1
t = Symbol('t')
cond4550334032=>condition: for j in range((n + 1))
cond4550334352=>operation: h *= (t - j) if  (j != k)
op4550334608=>operation: ckn *= integrate(h, (t, 0, n))
io4550336464=>inputoutput: output:  ckn
e4550335952=>end: end function
costes_coefficient

st4550332880->io4550332944
io4550332944->op4550333328
op4550333328->cond4550334032
cond4550334032(yes)->cond4550334352
cond4550334352(left)->cond4550334032
cond4550334032(no)->op4550334608
op4550334608->io4550336464
io4550336464->e4550335952
```

### 复化梯形求积法

```flow
st4441692176=>start: start composite_trapezium_integral
io4439089808=>inputoutput: input: f, a, b, epsilon, max_iter
sub4441692496=>operation: m = 1
h = b - a
t = h * (f(a) + f(b)) / 2
op4441692624=>operation: t_next = 0
cond4441693328=>condition: for _iter_times in range(int(max_iter))
op4441694672=>operation: h /= 2
op4441695696=>operation: s = sum([f(a + (2 * k - 1) * h) for k in range(1, m+1)])
        t_next = t / 2 + h * s
op4441693648=>operation: t_next = ((t / 2) + (h * s))
op4441696272=>operation: m <<= 1
cond4441696528=>operation: break if  (abs((t_next - t)) <= epsilon)
op4441697040=>operation: t = t_next
io4441693968=>inputoutput: output:  (t_next, (_iter_times + 1))
e4441693072=>end: end function return

st4441692176->io4439089808
io4439089808(right)->sub4441692496
sub4441692496->op4441692624
op4441692624->cond4441693328
cond4441693328(yes)->op4441694672
op4441694672()->op4441695696
op4441695696()->op4441696272
op4441696272->cond4441696528
cond4441696528->op4441697040
op4441697040(left)->cond4441693328
cond4441693328(no)->io4441693968
io4441693968->e4441693072
```

### 复化 Simpson 求积法

```flow
st4441692176=>start: start composite_simpson_integral
io4439089808=>inputoutput: input: f, a, b, epsilon, max_iter
sub4441692496=>operation: m = 1
    h = (b - a) / 2
    i = h * (f(a) + 4 * f((a+b) / 2) + f(b)) / 3
t = h * (f(a) + f(b)) / 2
op4441692624=>operation: t_next = 0
cond4441693328=>condition: for _iter_times in range(int(max_iter))
op4441694672=>operation: h /= 2
op4441695696=>operation: s0 = sum([f(a + (2 * k - 1) * h) for k in range(1, 2 * m + 1)])
        s1 = sum([f(a + (4 * k - 2) * h) for k in range(1, m + 1)])
        i_next = i / 2 + h * (4 * s0 - 2 * s1) / 3
op4441693648=>operation: t_next = ((t / 2) + (h * s))
op4441696272=>operation: m <<= 1
cond4441696528=>operation: break if  (abs((t_next - t)) <= epsilon)
op4441697040=>operation: t = t_next
io4441693968=>inputoutput: output:  (t_next, (_iter_times + 1))
e4441693072=>end: end function composite_simpson_integral

st4441692176->io4439089808
io4439089808(right)->sub4441692496
sub4441692496->op4441692624
op4441692624->cond4441693328
cond4441693328(yes)->op4441694672
op4441694672()->op4441695696
op4441695696()->op4441696272
op4441696272->cond4441696528
cond4441696528->op4441697040
op4441697040(left)->cond4441693328
cond4441693328(no)->io4441693968
io4441693968->e4441693072
```

### Romberg 算法

```flow
st4353469968=>start: start romberg_integral
io4353470032=>inputoutput: input: f, a, b, epsilon, max_iter
op4353470352=>operation: m = 0
op4353478736=>operation: T = [[None] * 4]
    T[0][0] = (b - a) * (f(a) + f(b)) / 2
cond4353479312=>condition: for m in range(1, int(max_iter))
sub4353511824=>operation: T.append(([None] * 4))
op4353480208=>operation: h = ((b - a) / (2 ** m))
op4353482384=>operation: _s = sum((f(a + (2 * k - 1) * h) for k in range(1, 1 + 2**(m-1))))
        T[m][0] = T[m-1][0] / 2 + h * _s
op4353511760=>operation: _t = 4      
(4 ** 1)
        T[m-1][1] = (_t * T[m][0] - T[m-1][0]) / (_t - 1)
cond4353512848=>condition: if (m > 1)
op4353512656=>operation: _t *= 4
(4 ** 2)
            T[m-2][2] = (_t * T[m-1][1] - T[m-2][1]) / (_t - 1)
e4353513296=>end: end function return
cond4353513616=>condition: if (m > 2)
op4353514000=>operation: _t *= 4
(4 ** 3)
            T[m-3][3] = (_t * T[m-2][2] - T[m-3][2]) / (_t - 1)
e4353513040=>end: end function return
cond4353514384=>operation: break if (m > 3) and (abs(T[m-3][3] - T[m-4][3]) < epsilon)
io4353482256=>inputoutput: output:  (T[(m - 3)][3], T, m)
e4353480144=>end: end function return

st4353469968->io4353470032
io4353470032(right)->op4353470352
op4353470352->op4353478736
op4353478736->cond4353479312
cond4353479312(yes)->sub4353511824
sub4353511824()->op4353480208
op4353480208()->op4353482384
op4353482384->op4353511760
op4353511760->cond4353512848
cond4353512848(yes,right)->op4353512656
cond4353512848(no)->cond4353513616
cond4353513616(yes,right)->op4353514000
cond4353513616(no)->cond4353514384
cond4353514384(left)->cond4353479312
cond4353479312(no)->io4353482256
io4353482256->e4353480144
```

### 自适应辛普森求积

```flow
st4481814032=>start: start adaptsim
io4481814224=>inputoutput: input: f, a, b, eps, max_iter
op4481814480=>operation: 初始化变量
    p = [a, b]
    p0 = p
    ep = [eps]
    m = 0
    q = 0
    I = 0
cond4481819152=>condition: for _iter_times in range(int(max_iter))
op4481821200=>operation: n1 = len(ep)
        n = len(p0)
cond4481844240=>operation: break if  (n <= 1)
op4481843792=>operation: h = (p0[1] - p0[0])
s0 = h /  6 * ( f(p0[0]) + 4 * f(p0[0] + h/2) + f(p0[0] + h  ) )
s1 = h / 12 * ( f(p0[0]) + 4 * f(p0[0] + h/4) + f(p0[0] + h/2) )
s2 = h / 12 * ( f(p0[0] + h/2) + 4 * f(p0[0] + 3*h/4) + f(p0[0] + h) )
op4481844880=>operation: s0 = h /  6 * ( f(p0[0]) + 4 * f(p0[0] + h/2) + f(p0[0] + h  ) )
s1 = h / 12 * ( f(p0[0]) + 4 * f(p0[0] + h/4) + f(p0[0] + h/2) )
s2 = h / 12 * ( f(p0[0] + h/2) + 4 * f(p0[0] + 3*h/4) + f(p0[0] + h) )
cond4481844048=>condition: if abs(s0 - s1 - s2) <= 15 * ep[0]
op4481844368=>operation: I += (s1 + s2)
p0 = p0[1:]
ep = ep[1:] if  (n1 >= 2)
q += 1
op4481845584=>operation: p0 = p0[1:]
cond4481846480=>operation: ep = ep[1:] if  (n1 >= 2)
op4481846992=>operation: q += 1
op4481846416=>operation: m += 1
op4481843984=>operation: p0 = [p0[0], p0[0] + h/2] + p0[1:]
ep = [ep[0]/2, ep[0]/2] if n1 == 1 else [ep[0]/2, ep[1]/2] + ep[1:]
p = p0 if q == 0 else p[:q] + p0
op4481846672=>operation: ep = [ep[0]/2, ep[0]/2] if n1 == 1 else [ep[0]/2, ep[1]/2] + ep[1:]
op4481846032=>operation: p = p0 if q == 0 else p[:q] + p0
opendfor=>operation: end for
io4481820048=>inputoutput: output:  (I, m, p)
e4481818896=>end: end function adaptsim

st4481814032->io4481814224
io4481814224->op4481814480
op4481814480->cond4481819152
cond4481819152(yes)->op4481821200
op4481821200->cond4481844240
cond4481844240()->op4481843792
op4481843792(right)->cond4481844048
cond4481844048(yes)->op4481844368
op4481844368->opendfor
cond4481844048(no)->op4481846416
op4481846416->op4481843984
op4481843984()->opendfor
opendfor(left)->cond4481819152
cond4481819152(no)->io4481820048
io4481820048->e4481818896
```

## 常微分方程初值问题解法

### 改进欧拉法

```flow
st4328731792=>start: start improved_euler
io4328731856=>inputoutput: input: f, a, b, h, y0
op4328732176=>operation: x = a
op4328732304=>operation: y = y0
cond4328732816=>condition: while ((x <= b) or (abs((b - x)) < 1e-14))
io4328734096=>inputoutput: output: yield (x, y)
op4328733456=>operation:  y_next_g = y + h * f(x, y)
op4328732688=>operation: y_next = y + h * ( f(x, y) + f(x+h, y_next_g) ) / 2
op4328733648=>operation: x = (x + h)
op4328734224=>operation: y = y_next
e4328731984=>end: end improved_euler

st4328731792->io4328731856
io4328731856->op4328732176
op4328732176->op4328732304
op4328732304->cond4328732816
cond4328732816(yes)->io4328734096
io4328734096->op4328733456
op4328733456->op4328732688
op4328732688->op4328733648
op4328733648->op4328734224
op4328734224(left)->cond4328732816
cond4328732816(no)->e4328731984
```

### 四阶龙格库塔

```flow
st4342742032=>start: start runge_kutta
io4342742096=>inputoutput: input: f, a, b, h, y0
op4342742416=>operation: x = a
    y = y0
cond4342742928=>condition: while ((x <= b) or (abs((b - x)) < 1e-14))
io4342804816=>inputoutput: output: (yield (x, y))
op4342805712=>operation: k1 = f(x, y)
        k2 = f(x + h / 2, y + h * k1 / 2)
        k3 = f(x + h / 2, y + h * k2 / 2)
        k4 = f(x + h, y + h * k3)
op4342805328=>operation: x = x + h
        y = y + h * (k1 + 2 * k2 + 2 * k3 + k4) / 6
e4342742224=>end: end runge_kutta

st4342742032->io4342742096
io4342742096->op4342742416
op4342742416->cond4342742928
cond4342742928(yes)->io4342804816
io4342804816->op4342805712
op4342805712->op4342805328
op4342805328(left)->cond4342742928
cond4342742928(no)->e4342742224
```

### RKF

```flow
st4344490576=>start: start runge_kutta_fehlberg
io4344490640=>inputoutput: input: f, a, b, h_min, h_max, y0, eps
op4344490960=>operation: h = h_max
x = a
y = y0
io4344491088=>inputoutput: output: (yield (x, y))
cond4344491728=>condition: while (x <= b)
op4344530000=>operation: k1 = h * f(x, y)
k2 = h * f(x + h / 4, y + k1 / 4)
k3 = h * f(x + 3 * h / 8, y + 3 * k1 / 32 + 9 * k2/ 32)
k4 = h * f(x + 12 * h / 13, y + 1932 / 2197 * k1 - 7200 / 2197 * k2  + 7296 / 2197 * k3 )
k5 = h * f(x + h, y + 439 / 216 * k1 - 8 * k2 + 3680 / 513 * k3 - 845 / 4104 * k4)
k6 = h * f(x + h / 2, y - 8 / 27 * k1 + 2 * k2 - 3544 / 2565 * k3 + 1859 / 4104 * k4 - 11 / 40 * k5)

op4344530384=>operation: R = abs((((((k1 / 360) - ((128 / 4275) * k3)) - ((2197 / 75240) * k4)) + (k5 / 50)) + ((2 / 55) * k6)))
cond4344530832=>condition: if (R <= (h * eps))
op4344529488=>operation: x = x + h
y = y + k1 * 25 / 216 + 1408 / 2565 * k3 + 2197 / 4104 * k4 - k5 / 5
io4344529808=>inputoutput: output: (yield (x, y))
op4344518672=>operation: delta = (0.84 * (((eps * h) / R) ** (1 / 4)))
cond4344531344=>condition: if (delta <= 0.1)
op4344531472=>operation: h = (0.1 * h)
cond4344530640=>operation: h = h_max if  (h > h_max)
cond4344557968=>operation: break if  (abs((x - b)) < eps)
cond4344558544=>operation: h = (b - x) if  ((x + h) > b)
cond4344558864=>operation: raise GeneratorExit('h_min too small. Failed to continue.') if  (h < h_min)
cond4344531792=>condition: if (delta >= 4)
op4344532624=>operation: h = (4 * h)
op4344532048=>operation: h = (delta * h)
e4344490832=>end: end runge_kutta_fehlberg

st4344490576->io4344490640
io4344490640->op4344490960
op4344490960->io4344491088
io4344491088->cond4344491728
cond4344491728(yes)->op4344530000
op4344530000->op4344530384
op4344530384->cond4344530832
cond4344530832(yes)->op4344529488
op4344529488->io4344529808
io4344529808->op4344518672
op4344518672->cond4344531344
cond4344531344(yes)->op4344531472
op4344531472->cond4344530640
cond4344530640->cond4344557968
cond4344557968->cond4344558544
cond4344558544->cond4344558864
cond4344558864(left)->cond4344491728
cond4344531344(no)->cond4344531792
cond4344531792(yes)->op4344532624
op4344532624->cond4344530640
cond4344531792(no)->op4344532048
op4344532048->cond4344530640
cond4344530832(no)->op4344518672
cond4344491728(no)->e4344490832
```

## 线性方程组的直接解法

### 顺序高斯消元法

```flow
st4314837520=>start: start gaussian_elimination_sequence
io4314837584=>inputoutput: input: a, b
op4314837968=>operation: A = np.c_[a, b]  # 增广矩阵
    n = A.shape[0]
    x = np.zeros(n)
cond4314838480=>condition: for k in range(n - 1)
cond4314839376=>operation: raise Exception('求解失败') if  (A[k][k] == 0)
cond4314879120=>condition: for i in range(k + 1, n)
op4314879248=>operation: m = A[i][k] / A[k][k]
op4314838160=>operation: A[i][k] = 0
cond4314878096=>operation: A[i][j] -= A[k][j] * m while j in range(k + 1, n + 1)
op4314838672=>operation: x[n-1] = A[n-1][n] / A[n-1][n-1]
cond4314880528=>condition: for k in range((n - 2), (- 1), (- 1))
cond4314881168=>operation: A[k][n] -= A[k][j] * x[j] while j in range(k + 1, n)
op4314881424=>operation: x[k] = A[k][n] / A[k][k]
io4314881808=>inputoutput: output:  x
e4314880912=>end: end function return

st4314837520->io4314837584
io4314837584->op4314837968
op4314837968->cond4314838480
cond4314838480(yes)->cond4314839376
cond4314839376(right)->cond4314879120
cond4314879120(yes)->op4314879248
op4314879248->op4314838160
op4314838160->cond4314878096
cond4314878096(left)->cond4314879120
cond4314879120(no,right)->cond4314838480
cond4314838480(no,left)->op4314838672
op4314838672->cond4314880528
cond4314880528(yes)->cond4314881168
cond4314881168->op4314881424
op4314881424(left)->cond4314880528
cond4314880528(no)->io4314881808
io4314881808->e4314880912
```

### LU 分解

```flow
st4491154256=>start: start lu
io4491154448=>inputoutput: input: a, sequence, swap_times
op4491154704=>operation: n = a.shape[0]
op4491154832=>operation: p = np.array([k for k in range(n)])
记录行交换的过程
op4491155344=>operation: swap_times = 0
记录行交换次数
cond4491155856=>condition: for k in range((n - 1))
cond4491191760=>condition: if (not sequence)
op4491191056=>operation: i_max = (k + np.argmax(np.abs(a[k:n, k])))
cond4491193744=>operation: if (i_max != k)
swap_rows(a, i_max, k)
swap_item(p, i_max, k)
swap_times += 1
sub4491193360=>subroutine: swap_item(p, i_max, k)
op4491193424=>operation: swap_times += 1
cond4491193872=>operation: raise Exception('存在为零的主元素') if  (a[k][k] == 0)
cond4491227600=>condition: for i in range((k + 1), n)
op4491227920=>operation: a[i][k] /= a[k][k]
a[i][j] -= (a[i][k] * a[k][j]) while  j in range(k + 1, n)
cond4491228624=>operation: a[i][j] -= (a[i][k] * a[k][j]) while  j in range(k + 1, n)
io4491227984=>inputoutput: output:
np.tril(a, k=-1) + np.identity(a.shape[0]),
np.triu(a), 
p)
e4491192720=>end: end function return

st4491154256->io4491154448
io4491154448(left)->op4491154704
op4491154704->op4491154832
op4491154832(right)->op4491155344
op4491155344->cond4491155856
cond4491155856(yes,right)->cond4491191760
cond4491191760(yes)->op4491191056
op4491191056->cond4491193744
cond4491193872->cond4491227600
cond4491227600(yes,)->op4491227920
op4491227920(left)->cond4491227600
cond4491227600(no)->cond4491155856
cond4491193744(right)->cond4491193872
cond4491191760(no)->cond4491193872
cond4491155856(no)->io4491227984
io4491227984->e4491192720
```

### 解三角方程

```flow
st4431527440=>start: start solve u@x=y
op4431515728=>operation: x = np.zeros(n, dtype=np.float)
x[n-1] = y[n-1] / u[n-1][n-1]
cond4431516432=>condition: for i in range(n-2, -1, -1)
# from n-2 (included) to 0 (included)
op4431517712=>operation: yi = y[i]
yi -= x[j] * u[i][j] while  j in range((i + 1), n)
op4431518608=>operation: x[i] = yi / u[i][i]
e4431527824=>end: end solve

st4431527440(right)->op4431515728
op4431515728(right)->cond4431516432
cond4431516432(yes)->op4431517712
op4431517712->op4431518608
op4431518608(left)->cond4431516432
cond4431516432(no)->e4431527824
```

## 线性方程组的迭代解法

### Jacobi 迭代

```flow
st4349413392=>start: start jacobi_iter
io4349413456=>inputoutput: input: A, b, x0, eps, max_steps, verbose
op4349413776=>operation: D = diag(diag(A))
L = - tril(A, -1)
U = - triu(A, 1)
op4349413904=>operation: B = inv(D) @ (L + U)
    f = inv(D) @ b
op4349414288=>operation: x = x0
cond4349414672=>condition: for i in range(max_steps)
op4349440656=>operation: x_prev = x
op4349441104=>operation: x = B @ x + f
cond4349441296=>operation: break if all(abs(x - x_prev) <= eps)
io4349415184=>inputoutput: output:  x
e4349415248=>end: end function return

st4349413392(left)->io4349413456
io4349413456->op4349413776
op4349413776->op4349413904
op4349413904->op4349414288
op4349414288->cond4349414672
cond4349414672(yes,right)->op4349440656
op4349440656(right)->op4349441104
op4349441104(right)->cond4349441296
cond4349441296(top)->cond4349414672
cond4349414672(no)->io4349415184
io4349415184(right)->e4349415248
```

## 特征值求法

### 正幂法

```flow
st4462604048=>start: start power_iteration
io4462604112=>inputoutput: input: A, m0, u0, eps, max_steps, verbose
op4462616784=>operation: m = m0
u = u0
cond4462617424=>condition: for k in range(int(max_steps))
op4462654160=>operation: m_prev = m
op4462654096=>operation: v = dot(A, u)
mi = argmax(abs(v))
m = v[mi]
u = v / m
op4462654352=>operation: mi = argmax(abs(v))
op4462619920=>operation: m = v[mi]
op4462619536=>operation: u = (v / m)
cond4462654992=>operation: break if  (abs((m - m_prev)) <= eps)
io4462655568=>inputoutput: output:  (m, u, (k + 1))
e4462655632=>end: end function power_iteration

st4462604048(left)->io4462604112
io4462604112->op4462616784
op4462616784->cond4462617424
cond4462617424(yes,right)->op4462654160
op4462654160(right)->op4462654096
op4462654096->cond4462654992
cond4462654992(left)->cond4462617424
cond4462617424(no)->io4462655568
io4462655568(right)->e4462655632
```

### 原点位移算法

```flow
st4546378576=>start: start origin_translation
io4546378640=>inputoutput: input: A, p, x0, eps, max_steps, verbose
op4546378960=>operation: _I = identity(A.shape[0])
eig = p
x = x0
cond4546392208=>condition: for k in range(int(max_steps))
op4546393552=>operation: eig_prev = eig
op4546394192=>operation: x = linalg.solve(A - eig * _I, x)
q = argmax(abs(x))
xq = x[q]
op4546394384=>operation: eig = eig + 1 / xq
x = x / xq
cond4546394768=>operation: break if  all((abs((eig - eig_prev)) <= eps))
io4546392528=>inputoutput: output:  (eig, x, (k + 1))
e4546392400=>end: end function origin_translation

st4546378576(left)->io4546378640
io4546378640->op4546378960
op4546378960->cond4546392208
cond4546392208(yes,right)->op4546393552
op4546393552(right)->op4546394192
op4546394192->op4546394384
op4546394384->cond4546394768
cond4546394768(left)->cond4546392208
cond4546392208(no)->io4546392528
io4546392528->e4546392400
```


