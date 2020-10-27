import numpy as np


class SimpleIteration(object):
    """求解线性方程组的迭代法:
        A @ x = b

    调用 SimpleIteration 子类实例得到解, e.g. JacobiIteration(A, b)()

    """

    def __init__(self, A, b):
        """
        A:  np_array_like, 系数矩阵
        b:  np_array_like, 右端常数
        """
        self.A = np.array(A)
        self.b = np.array(b)

        n, m = self.A.shape
        if n != m or n != len(self.b):
            raise ValueError(f"Not match: A({n, m}) and b({len(b)},)")

    @staticmethod
    def _dlu(A):
        """分裂 A:
            A = D - L - U

        Args:
            A: np.array

        Returns:
            (D, L, U)
        """
        D = np.diag(np.diag(A))
        L = - np.tril(A, -1)
        U = - np.triu(A, 1)

        return D, L, U

    def _B_f(self):
        """计算迭代 x = B @ x + f 的 B 和 f
        """
        raise NotImplementedError('_B_f')

    def __call__(self, x0=None, eps=1e-5, max_steps=5000, verbose=False):
        """线性方程组「简单迭代法」的迭代过程
            x = B @ x + f

        其中 B, f 调用 self._B_f() 得到


        Args:
            x0: np_array_like, 迭代初值
                default x0=None means using random values.
            eps: float, 精度要求
            max_steps: int, 最大迭代次数
            verbose: bool, 如果计算成功，打印出结果及迭代次数

        Returns:
            x: 方程组的解

        Raises:
            ValueError: x0 形状不符合问题
            Expection:  达到最大迭代次数，仍不满足精度
        """
        if not x0:
            x0 = np.random.random(self.A.shape[0])

        x0_shape = np.shape(x0)
        if x0_shape[0] != self.A.shape[0]:
            raise ValueError(
                f"Not match: A({self.A.shape}) and x0({x0_shape})")

        B, f = self._B_f()

        x = x0
        i = 0
        for i in range(int(max_steps)):
            x_prev = np.array(x)  # deep copy

            x = B @ x + f

            if np.all(np.abs(x - x_prev) <= eps):  # 达到精度要求
                break
        else:
            raise Exception(
                f"{self.method_name()} cannot reach eps ({eps}) after max_steps ({max_steps}). The last result: x = {x}")

        if verbose:
            print(f"{self.method_name()} get result x = {x} after {i} iterations.")

    def method_name(self):
        return self.__class__.__name__


class JacobiIteration(SimpleIteration):
    """雅可比（Jacobi）迭代法求解线性方程组:
        A @ x = b
    """

    def _B_f(self):
        D, L, U = self._dlu(self.A)

        inv_D = np.linalg.pinv(D)

        B = inv_D @ (L + U)
        f = inv_D @ self.b

        return B, f


class GaussSeidel(SimpleIteration):
    """高斯-赛德尔迭代（Gauss–Seidel method）求解线性方程组:
        A @ x = b
    """

    def _B_f(self):
        D, L, U = self._dlu(self.A)

        inv_DsL = np.linalg.pinv(D - L)

        B = inv_DsL @ U
        f = inv_DsL @ self.b

        return B, f


class SOR(SimpleIteration):
    """逐次超松驰法（Successive over-relaxation, SOR）求解线性方程组:
        A @ x = b
    """

    def __init__(self, A, b, w=1):
        """
        w:  float, 松弛因子 w > 0
            default w=1，即 Gauss–Seidel 迭代
        """
        super().__init__(A, b)
        self.w = w

    def _B_f(self):
        D, L, U = self._dlu(self.A)
        w = self.w

        _inv_DsWL = np.linalg.pinv(D - w * L)

        B = _inv_DsWL @ ((1-w) * D + w * U)
        f = w * _inv_DsWL @ self.b

        return B, f

    def method_name(self):
        return super().method_name() + f' (w={self.w})'
