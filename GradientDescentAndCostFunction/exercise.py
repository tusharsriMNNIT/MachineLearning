import numpy as np
import pandas as pd

def gradient_descent(x,y):
    
    m_curr = b_curr = 0
    iterations = 100
    learn = 0.0025
    n = len(x)
    
    for i in range(iterations):
        y_pred = m_curr * x + b_curr
        cost = (1/n) * sum([val**2 for val in (y-y_pred)])
        
        md = -(2/n) * sum(x * (y - y_pred))
        bd = -(2/n) * sum(y - y_pred)
        
        m_curr = m_curr - learn * md
        b_curr = b_curr - learn * bd
        
        print("{}-> m->{}, b->{}, cost->{}".format(i,m_curr,b_curr,cost))


df = pd.read_csv('test_scores.csv')

x = np.array(list(df['math']))
y = np.array(list(df['cs']))

gradient_descent(x,y)