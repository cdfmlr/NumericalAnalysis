def fixed_point_iter(phi, x_0, max_steps=25, verbose=False):
    x = x_0
    for i in range(max_steps):
        x = phi(x)
    return x
