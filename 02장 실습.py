#!/usr/bin/env python
# coding: utf-8

# In[4]:


#Do it! 실습 2-2
# 시퀀스 원소의 최댓값 출력하기

from typing import Any, Sequence

def max_of(a: Sequence) -> Any:
    """시퀀스형 a원소의 최댓값을 반환"""
    maximum = a[0]
    for i in range(1, len(a)):
        if a[i] > maximum:
            maximum = a[i]
    return maximum
    
if __name__ == '__main__':
    print('배열의 최댓값을 구합니다.')
    num = int(input('원소 수를 입력하시오.:'))
    x = [None] * num #원소 수가 num인 러스트를 생성
        
    for i in range(num):
        x[i] = int(input(f'x[{i}]값을 입력하세요.: '))
        
    print(f'최댓값은 {max_of(x)}입니다.')


# In[6]:


#Do it! 실습 2-6
# 뮤터블 시퀀스 원소를 역순으로 정렬

from typing import Any, MutableSequence

def reverse_array(a: MutableSequence) -> None:
    """뮤터블 시퀀스 a의 원소를 역순으로 정렬"""
    n = len(a)
    for i in range(n//2):
        a[i], a[n - i - 1] = a[n - i -1], a[i]
        
if __name__ == '__main__':
    print('배열 원소를 역순으로 정렬합니다.')
    nx = int(input('원소 수를 입력하세요: '))
    x = [None] * nx #원소 수가 nx인 리스트를 생성

    for i in range(nx):
        x[i] = int(input(f'x[{i}]값을 입력하세요.: '))
        
    reverse_array(x)
    
    print('배열 원소를 역순으로 정렬했습니다.')
    for i in range(nx):
        print(f'x[{i}] = {x[i]}')
        
        


# In[8]:


#Do it! 실습 2-10
# 1,000 이하의 소수를 나열하기(알고리즘 개선 2)

counter = 0
ptr = 0
prime = [None] * 500

prime[ptr] = 2
ptr += 1

prime[ptr] = 3
ptr += 1

for n in range(5, 1001, 2):
    i = 1
    while prime[i] * prime[i] <= n:
        counter += 2
        if n % prime[i] == 0:
            break
        i += 1
    else:
        prime[ptr] = n
        ptr += 1
        counter += 1
        
for i in range(ptr):
    print(prime[i])
print(f'곱셈과 나눗셈을 실행한 횟수: {counter}')


# In[ ]:




