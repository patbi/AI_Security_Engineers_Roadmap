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
d = {"a":[1,2,3,4,5],"s":[1,2,3,4,5],"d":[1,2,3,4,5],1:[1,2,3,4,5]}

var1 = pd.DataFrame(d, columns=["a",1], index=["a","s","d","f","g"])

print(type(var1))
print(var1)
```

    <class 'pandas.core.frame.DataFrame'>
       a  1
    a  1  1
    s  2  2
    d  3  3
    f  4  4
    g  5  5
    


```python

```


```python
d = {"a":[1,2,3,4,5],"s":[1,2,3,4,5],"d":[1,2,3,4,5],1:[1,2,3,4,5]}

var1 = pd.DataFrame(d)

print(type(var1))
print(var1)
print(var1["a"][3])
```

    <class 'pandas.core.frame.DataFrame'>
       a  s  d  1
    0  1  1  1  1
    1  2  2  2  2
    2  3  3  3  3
    3  4  4  4  4
    4  5  5  5  5
    4
    


```python
list_1 = [[1,2,3,4,5],[11,12,13,14,15]]

var2 = pd.DataFrame(list_1)

print(type(var2))
print(var2)

```

    <class 'pandas.core.frame.DataFrame'>
        0   1   2   3   4
    0   1   2   3   4   5
    1  11  12  13  14  15
    


```python
sr = {"s":pd.Series([1,2,3,4]),"r":pd.Series([1,2,3,4])}

var3 = pd.DataFrame(sr)

print(type(var3))
print(var3)


```

    <class 'pandas.core.frame.DataFrame'>
       s  r
    0  1  1
    1  2  2
    2  3  3
    3  4  4
    


```python
import pandas as pd

var = pd.DataFrame({"A":[1,2,3,4],"B":[5,6,7,8]})

var 
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>A</th>
      <th>B</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>1</td>
      <td>5</td>
    </tr>
    <tr>
      <th>1</th>
      <td>2</td>
      <td>6</td>
    </tr>
    <tr>
      <th>2</th>
      <td>3</td>
      <td>7</td>
    </tr>
    <tr>
      <th>3</th>
      <td>4</td>
      <td>8</td>
    </tr>
  </tbody>
</table>
</div>




```python
var["C"] = var["A"]+var["B"]

var
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>A</th>
      <th>B</th>
      <th>C</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>1</td>
      <td>5</td>
      <td>6</td>
    </tr>
    <tr>
      <th>1</th>
      <td>2</td>
      <td>6</td>
      <td>8</td>
    </tr>
    <tr>
      <th>2</th>
      <td>3</td>
      <td>7</td>
      <td>10</td>
    </tr>
    <tr>
      <th>3</th>
      <td>4</td>
      <td>8</td>
      <td>12</td>
    </tr>
  </tbody>
</table>
</div>




```python
var["C"] = var["A"] - var["B"]

var
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>A</th>
      <th>B</th>
      <th>C</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>1</td>
      <td>5</td>
      <td>-4</td>
    </tr>
    <tr>
      <th>1</th>
      <td>2</td>
      <td>6</td>
      <td>-4</td>
    </tr>
    <tr>
      <th>2</th>
      <td>3</td>
      <td>7</td>
      <td>-4</td>
    </tr>
    <tr>
      <th>3</th>
      <td>4</td>
      <td>8</td>
      <td>-4</td>
    </tr>
  </tbody>
</table>
</div>




```python

```


```python
var["C"] = var["A"] * var["B"]

var
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>A</th>
      <th>B</th>
      <th>C</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>1</td>
      <td>5</td>
      <td>5</td>
    </tr>
    <tr>
      <th>1</th>
      <td>2</td>
      <td>6</td>
      <td>12</td>
    </tr>
    <tr>
      <th>2</th>
      <td>3</td>
      <td>7</td>
      <td>21</td>
    </tr>
    <tr>
      <th>3</th>
      <td>4</td>
      <td>8</td>
      <td>32</td>
    </tr>
  </tbody>
</table>
</div>




```python
var["C"] = var["A"] / var["B"]

var
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>A</th>
      <th>B</th>
      <th>C</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>1</td>
      <td>5</td>
      <td>0.200000</td>
    </tr>
    <tr>
      <th>1</th>
      <td>2</td>
      <td>6</td>
      <td>0.333333</td>
    </tr>
    <tr>
      <th>2</th>
      <td>3</td>
      <td>7</td>
      <td>0.428571</td>
    </tr>
    <tr>
      <th>3</th>
      <td>4</td>
      <td>8</td>
      <td>0.500000</td>
    </tr>
  </tbody>
</table>
</div>




```python
var1 = pd.DataFrame({"A":[10,20,30,40],"B":[15,16,17,18]})

var1
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>A</th>
      <th>B</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>10</td>
      <td>15</td>
    </tr>
    <tr>
      <th>1</th>
      <td>20</td>
      <td>16</td>
    </tr>
    <tr>
      <th>2</th>
      <td>30</td>
      <td>17</td>
    </tr>
    <tr>
      <th>3</th>
      <td>40</td>
      <td>18</td>
    </tr>
  </tbody>
</table>
</div>




```python
var1["Python"] = var1["A"] <= 20

var1
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>A</th>
      <th>B</th>
      <th>Python</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>10</td>
      <td>15</td>
      <td>True</td>
    </tr>
    <tr>
      <th>1</th>
      <td>20</td>
      <td>16</td>
      <td>True</td>
    </tr>
    <tr>
      <th>2</th>
      <td>30</td>
      <td>17</td>
      <td>False</td>
    </tr>
    <tr>
      <th>3</th>
      <td>40</td>
      <td>18</td>
      <td>False</td>
    </tr>
  </tbody>
</table>
</div>




```python

```


```python

```
