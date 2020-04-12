import numpy as np


def gradient_descent(x,y):
    m_curr = b_curr = 0
    n = len(x)
    learning = 0.07
    iterations = 100
    
    for i in range(iterations):
        
        y_pred = (m_curr * x + b_curr)
        cost = (1/n) * sum([val**2 for val in (y - y_pred)])
        
        md = -(2/n) * sum(x * (y - y_pred))
        bd = -(2/n) * sum(y - y_pred)
        
        m_curr = m_curr - learning * md
        b_curr = b_curr - learning * bd
        
        print("{}-> m--> {} b--> {} cost--> {}".format(i,m_curr,b_curr,cost))
    

x = np.array([1,2,3,4,5])
y = np.array([5,7,9,11,13])

gradient_descent(x,y)