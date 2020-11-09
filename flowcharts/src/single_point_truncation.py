def single_point_truncation(f, x_0, x_1, eps=0, eta=0, max_steps=20):    
    x = x_1
    for i in range(max_steps):   
        x_next = x - f(x) / (f(x) - f(x_0)) * (x - x_0)
        
        if abs(x_next - x) <= eps or abs(f(x)) <= eta:
           break
        
        x = x_next
    
    return x