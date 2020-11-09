# 差商缓存
差商缓存 = {}

def difference_quotient(f, xs: list):
    # 尝试从缓存读取
    key = get_key(f, xs)
    if key in 差商缓存:
        return 差商缓存[key]

    if len(xs) == 1: # 0阶
        dq = f(xs[0])
    else: # n 阶
        dq_h = difference_quotient(f, xs[:-1])
        dq_l = difference_quotient(f, xs[1: ])
        dq = (dq_l - dq_h) / (xs[-1] - xs[0])

    # 写入缓存
    差商缓存[key] = dq

    return dq