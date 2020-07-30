#!/usr/bin/env python
# coding: utf-8

# In[2]:


import numpy as np
def game(min_=1, max_=101):
    number = np.random.randint(min_, max_)
    count = 0
    
    # условие на основании кол-ва символов в числе
    
    n_num = len(str(number))
    low = 10**(n_num - 1) 
    high = 10**n_num - 1

    while True:
        count += 1
        predict = (low + high) // 2
        if number == predict:
            break
        elif number > predict:
            low = predict
        else:
            high = predict
    return count
print('С помощью Вашего отличного алгоритма мне удалось угадать число за',game(),'попыток(ки)')





# 
