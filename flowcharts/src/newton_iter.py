def newton_iter(f, x_0, eps=0, eta=0, max_steps=20):
    x = x_0
    for i in range(max_steps):
        
        x_next = x - f(x) / df(x)
        
        if abs(x_next - x) <= eps or abs(f(x)) <= eta:
           break
        
        x = x_next
    return x
