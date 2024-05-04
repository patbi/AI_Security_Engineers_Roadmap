```python
import pandas as pd

x = [3,4,5,6]

ser = pd.Series(x,index=['a','s','d','f'],dtype="float",name="python")

print(ser)
print(type(ser))
print(ser.iloc[2])
```

    a    3.0
    s    4.0
    d    5.0
    f    6.0
    Name: python, dtype: float64
    <class 'pandas.core.series.Series'>
    5.0
    


```python
dic = {"name":['python','c','c++','java'], "port":[12,13,14,15], "rank":[1,4,3,2]}

y = pd.Series(dic)

print(y)
```

    name    [python, c, c++, java]
    port          [12, 13, 14, 15]
    rank              [1, 4, 3, 2]
    dtype: object
    


```python
s = pd.Series(12,index=[1,2,3,4,5,6,7])

print(s)
print(type(s))
```

    1    12
    2    12
    3    12
    4    12
    5    12
    6    12
    7    12
    dtype: int64
    <class 'pandas.core.series.Series'>
    


```python
s1 = pd.Series(12,index=[1,2,3,4,5,6,7])
s2 = pd.Series(12,index=[1,2,3,4])

print(s1+s2)
```

    1    24.0
    2    24.0
    3    24.0
    4    24.0
    5     NaN
    6     NaN
    7     NaN
    dtype: float64
    


```python
## DataFrame
import pandas as pd

l=[1,2,3,4,5,6]

var = pd.DataFrame(l)
print(type(var))

```

    <class 'pandas.core.frame.DataFrame'>
    


```python
d = {"a":[1,2,3,4,5],"s":[1,2,3,4,5]}

var1 = pd.DataFrame(d)

print(type(var1))
print(var1)
```

    <class 'pandas.core.frame.DataFrame'>
       a  s
    0  1  1
    1  2  2
    2  3  3
    3  4  4
    4  5  5
    


```python

```
