import numpy as np
import pandas as pd


def make_data_simple(): 
    x_a = []
    for i in range(0, 200):
        numb = np.random.normal(loc=90.0, scale=30.0, size=None)
        x_a.append(numb)
        
    y_a = []
    for i in x_a:
        num = 3.5 * i + 60 + np.random.normal(loc=0.0, scale=50.0, size=None)
        y_a.append(num)
        
    dict_a = {'x': x_a , 'y' : y_a}
    df = pd.DataFrame(dict_a)
    
    return df

def make_data_mult_quantitative():    
    x_a = []
    for i in range(0, 200):
        numb = np.random.normal(loc=90.0, scale=10.0, size=None)
        x_a.append(numb)
        
    y_a = []
    for i in x_a:
        num = 3.5 * i + 60 + np.random.normal(loc=0.0, scale=50.0, size=None)
        y_a.append(num)

    dict_a = {'x': x_a , 'y' : y_a} 
    df_a = pd.DataFrame(dict_a)

    df_a['pred'] = 3.5 * df_a['x'] + 60
    df_a['residuals'] = df_a['y'] - df_a['pred']
    df_a['noise'] = np.random.normal(loc=0.0, scale=50.0, size=200)
    df_a['z'] = df_a['residuals'] - df_a['x'] + df_a['noise']
        
    w_a = []
    for i in x_a:
        num = 1 * i + 0 + np.random.normal(loc=0.0, scale=75.0, size=None)
        w_a.append(num)
        
    df_a['w'] = w_a  
    df = df_a[['x', 'y', 'z', 'w']]  

    return df


def make_data_intercept():    
    x_a = []
    for i in range(0, 200):
        numb = np.random.normal(loc=90.0, scale=30.0, size=None)
        x_a.append(numb)
        
    y_a = []
    for i in x_a:
        num = 3.5 * i + 60 + np.random.normal(loc=0.0, scale=50.0, size=None)
        y_a.append(num)
        
    x_b = []
    for i in range(0, 100):
        numb = np.random.normal(loc=90.0, scale=30.0, size=None)
        x_b.append(numb)
        
    y_b = []
    for i in x_b:
        num = 3.5 * i + -150 + np.random.normal(loc=0.0, scale=50.0, size=None)
        y_b.append(num)
        
    dict_a = {'x': x_a , 'y' : y_a}
    dict_b = {'x': x_b , 'y' : y_b}
    df_a = pd.DataFrame(dict_a)
    df_b = pd.DataFrame(dict_b)
    df_a['type'] ='A'
    df_b['type'] ='B'
    df = pd.concat([df_a, df_b])
    
    return df

def make_data_slope():    
    x_a = []
    for i in range(0, 200):
        numb = np.random.normal(loc=90.0, scale=50.0, size=None)
        x_a.append(numb)
        
    y_a = []
    for i in x_a:
        num = 3.5 * i + 20 + np.random.normal(loc=0.0, scale=120.0, size=None)
        y_a.append(num)
        
    x_b = []
    for i in range(0, 100):
        numb = np.random.normal(loc=90.0, scale=30.0, size=None)
        x_b.append(numb)
        
    y_b = []
    for i in x_b:
        num = 10 * i + 20 + np.random.normal(loc=0.0, scale=200.0, size=None)
        y_b.append(num)
        
    dict_a = {'x': x_a , 'y' : y_a}
    dict_b = {'x': x_b , 'y' : y_b}
    df_a = pd.DataFrame(dict_a)
    df_b = pd.DataFrame(dict_b)
    df_a['type'] ='A'
    df_b['type'] ='B'
    df = pd.concat([df_a, df_b])
    
    return df


def make_data_complex():    
    x_a = []
    for i in range(0, 100):
        numb = np.random.normal(loc=90.0, scale=30.0, size=None)
        x_a.append(numb)
        
    y_a = []
    for i in x_a:
        num = 3.5 * i + 250 + np.random.normal(loc=0.0, scale=100.0, size=None)
        y_a.append(num)
        
    x_b = []
    for i in range(0, 100):
        numb = np.random.normal(loc=90.0, scale=30.0, size=None)
        x_b.append(numb)
        
    y_b = []
    for i in x_b:
        num = -2 * i + 20 + np.random.normal(loc=0.0, scale=70.0, size=None)
        y_b.append(num)
    
    x_c = []
    for i in range(0, 100):
        numb = np.random.normal(loc=90.0, scale=20.0, size=None)
        x_c.append(numb)
        
    y_c = []
    for i in x_c:
        num = 5 * i + -230 + np.random.normal(loc=0.0, scale= 80.0, size=None)
        y_c.append(num)
    
    x_d = []
    for i in range(0, 100):
        numb = np.random.normal(loc=100.0, scale=40.0, size=None)
        x_d.append(numb)
        
    y_d = []
    for i in x_d:
        num = 5 * i + 246 + np.random.normal(loc=0.0, scale = 80.0, size=None)
        y_d.append(num)
    
    dict_a = {'x': x_a , 'y' : y_a}
    dict_b = {'x': x_b , 'y' : y_b}
    dict_c = {'x': x_c , 'y' : y_c}
    dict_d = {'x': x_d , 'y' : y_d}
    df_a = pd.DataFrame(dict_a)
    df_b = pd.DataFrame(dict_b)
    df_c = pd.DataFrame(dict_c)
    df_d = pd.DataFrame(dict_d)
    
    df_a['type_a'] ='A'
    df_b['type_a'] ='A'
    df_a['type_b'] ='A'
    df_b['type_b'] ='B'
    df_c['type_a'] ='B'
    df_d['type_a'] ='B'
    df_c['type_b'] ='A'
    df_d['type_b'] ='B'
    
    df = pd.concat([df_a, df_b, df_c, df_d])
    
    return df

def make_data_reg():    
    x_a = []
    for i in range(0, 20):
        numb = np.random.normal(loc=90.0, scale=30.0, size=None)
        x_a.append(numb)
        
    y_a = []
    for i in x_a:
        num = 3.5 * i + 60 + np.random.normal(loc=0.0, scale=50.0, size=None)
        y_a.append(num)
        
    dict_a = {'x': x_a , 'y' : y_a}
    df = pd.DataFrame(dict_a)
    return df
