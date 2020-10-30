import numpy as np
import traceback

from .origin_translation import origin_translation
from .power_method import power_iteration
from .inverse_power import inverse_iteration


def accelerating_max_val_eig(A, x0=None, eps_pi=1e-1, eps_ot=1e-8, max_steps_pi=1000, max_steps_ot=1000, verbose=False):
    """动态原点位移算法求按模最大特征值

    Args:
        A:  np_array_like, 待求特征值的矩阵 (nxn)
        x0: np_array_like, 初始向量（n）, 要求 max(abs(x0)) == 1
                default x0=None: 取 x0 = (1, 1, ..., 1)
        eps_pi: float,「正幂法」迭代的控制精度
                default eps_pi=1e-1
        eps_ot: float,「原点位移」算法的控制精度，必须满足 eps > eps_ot
                default eps_ot=1e-8
        max_steps_pi: int,「正幂法」迭代的最大迭代次数
                default max_steps_pi=1000
        max_steps_ot: int,「原点位移」算法的最大迭代次数
                default max_steps_ot=1000
        verbose: bool:
                - False: 不打印任何过程信息;
                - True: 打印出「正幂法」、「原点位移」的完整迭代过程;
                default verbose=False

    Returns:
        (eig, eigv, k)
            eig: float, A 的按模最大特征值
            eigv: np.array, 单位化的特征向量
            k: 迭代次数

    Raises:
        ValueError: 参数 A 不是方阵，
                    或 A 和给定 x0 尺寸不匹配
                    或 x0 = 0
        Exception:  无法在max_steps 次迭代以内得到满足精度 eps 的结果
    """
    # 异常输入检测会在 power_iteration 中完成，此处不必重复辛劳

    if verbose:
        print("    power_iteration:")

    eig, eigv, k_pi = power_iteration(
        A, u0=x0, eps=eps_pi, max_steps=max_steps_pi, verbose=verbose)

    if verbose:
        print("    origin_translation:")

    eig, eigv, k_ot = origin_translation(
        A, eig, x0=eigv, eps=eps_ot, max_steps=max_steps_ot, verbose=verbose)

    return eig, eigv, k_pi + k_ot


def accelerating_min_val_eig(A, x0=None, eps_ii=1e-1, eps_ot=1e-8, max_steps_ii=1000, max_steps_ot=1000, verbose=False):
    """动态原点位移算法求按模最小特征值

    Args:
        A:  np_array_like, 待求特征值的矩阵 (nxn)
        x0: np_array_like, 初始向量（n）, 要求 max(abs(x0)) == 1
                default x0=None: 取 x0 = (1, 1, ..., 1)
        eps_ii: float,「反幂法」迭代的控制精度
                default eps_ii=1e-1
        eps_ot: float,「原点位移」算法的控制精度，必须满足 eps > eps_ot
                default eps_ot=1e-8
        max_steps_ii: int,「反幂法」迭代的最大迭代次数
                default max_steps_ii=1000
        max_steps_ot: int,「原点位移」算法的最大迭代次数
                default max_steps_ot=1000
        verbose: bool:
                - False: 不打印任何过程信息;
                - True: 打印出「正幂法」、「原点位移」的完整迭代过程;
                default verbose=False

    Returns:
        (eig, eigv, k)
            eig: float, A 的按模最大特征值
            eigv: np.array, 单位化的特征向量
            k: 迭代次数

    Raises:
        ValueError: 参数 A 不是方阵，
                    或 A 和给定 x0 尺寸不匹配
                    或 x0 = 0
        Exception:  无法在max_steps 次迭代以内得到满足精度 eps 的结果
    """
    # 异常输入检测会在 power_iteration 中完成，此处不必重复辛劳

    if verbose:
        print("    inverse_iteration:")

    eig, eigv, k_ii = inverse_iteration(
        A, u0=x0, eps=eps_ii, max_steps=max_steps_ii, verbose=verbose)

    if verbose:
        print("    origin_translation:")

    eig, eigv, k_ot = origin_translation(
        A, eig, x0=eigv, eps=eps_ot, max_steps=max_steps_ot, verbose=verbose)

    return eig, eigv, k_ii + k_ot
