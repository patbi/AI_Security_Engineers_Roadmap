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
var1["python_1"] = var1["B"] >= 16

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
      <th>python_1</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>10</td>
      <td>15</td>
      <td>True</td>
      <td>False</td>
    </tr>
    <tr>
      <th>1</th>
      <td>20</td>
      <td>16</td>
      <td>True</td>
      <td>True</td>
    </tr>
    <tr>
      <th>2</th>
      <td>30</td>
      <td>17</td>
      <td>False</td>
      <td>True</td>
    </tr>
    <tr>
      <th>3</th>
      <td>40</td>
      <td>18</td>
      <td>False</td>
      <td>True</td>
    </tr>
  </tbody>
</table>
</div>




```python
#Insert
import pandas as pd

var = pd.DataFrame({"A":[1,2,3,4,5],"B":[9,8,7,6,5],"C":[11,12,13,14,15]})

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
      <td>9</td>
      <td>11</td>
    </tr>
    <tr>
      <th>1</th>
      <td>2</td>
      <td>8</td>
      <td>12</td>
    </tr>
    <tr>
      <th>2</th>
      <td>3</td>
      <td>7</td>
      <td>13</td>
    </tr>
    <tr>
      <th>3</th>
      <td>4</td>
      <td>6</td>
      <td>14</td>
    </tr>
    <tr>
      <th>4</th>
      <td>5</td>
      <td>5</td>
      <td>15</td>
    </tr>
  </tbody>
</table>
</div>




```python
var.insert(2,"E",var["A"])

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
      <th>D</th>
      <th>E</th>
      <th>C</th>
      <th>B</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>1</td>
      <td>11</td>
      <td>1</td>
      <td>1</td>
      <td>9</td>
    </tr>
    <tr>
      <th>1</th>
      <td>2</td>
      <td>12</td>
      <td>2</td>
      <td>2</td>
      <td>8</td>
    </tr>
    <tr>
      <th>2</th>
      <td>3</td>
      <td>13</td>
      <td>3</td>
      <td>3</td>
      <td>7</td>
    </tr>
    <tr>
      <th>3</th>
      <td>4</td>
      <td>14</td>
      <td>4</td>
      <td>4</td>
      <td>6</td>
    </tr>
    <tr>
      <th>4</th>
      <td>5</td>
      <td>15</td>
      <td>5</td>
      <td>5</td>
      <td>5</td>
    </tr>
  </tbody>
</table>
</div>




```python
var["f"] = var["A"][:3]

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
      <th>D</th>
      <th>E</th>
      <th>C</th>
      <th>B</th>
      <th>f</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>1</td>
      <td>11</td>
      <td>1</td>
      <td>1</td>
      <td>9</td>
      <td>1.0</td>
    </tr>
    <tr>
      <th>1</th>
      <td>2</td>
      <td>12</td>
      <td>2</td>
      <td>2</td>
      <td>8</td>
      <td>2.0</td>
    </tr>
    <tr>
      <th>2</th>
      <td>3</td>
      <td>13</td>
      <td>3</td>
      <td>3</td>
      <td>7</td>
      <td>3.0</td>
    </tr>
    <tr>
      <th>3</th>
      <td>4</td>
      <td>14</td>
      <td>4</td>
      <td>4</td>
      <td>6</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>4</th>
      <td>5</td>
      <td>15</td>
      <td>5</td>
      <td>5</td>
      <td>5</td>
      <td>NaN</td>
    </tr>
  </tbody>
</table>
</div>




```python
var1 = var.pop("B")

var1
```




    0    9
    1    8
    2    7
    3    6
    4    5
    Name: B, dtype: int64




```python
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
      <th>C</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>1</td>
      <td>11</td>
    </tr>
    <tr>
      <th>1</th>
      <td>2</td>
      <td>12</td>
    </tr>
    <tr>
      <th>2</th>
      <td>3</td>
      <td>13</td>
    </tr>
    <tr>
      <th>3</th>
      <td>4</td>
      <td>14</td>
    </tr>
    <tr>
      <th>4</th>
      <td>5</td>
      <td>15</td>
    </tr>
  </tbody>
</table>
</div>




```python
del var["A"]

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
      <th>C</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>11</td>
    </tr>
    <tr>
      <th>1</th>
      <td>12</td>
    </tr>
    <tr>
      <th>2</th>
      <td>13</td>
    </tr>
    <tr>
      <th>3</th>
      <td>14</td>
    </tr>
    <tr>
      <th>4</th>
      <td>15</td>
    </tr>
  </tbody>
</table>
</div>




```python
# Write csv

import pandas as pd

dis = {"a":[1,2,3,4,5,6],"s":[1,2,3,4,5,6],"d":[1,2,3,4,5,6]}

d = pd.DataFrame(dis)

print(d)

d.to_csv("Test_new.csv",index=False,header=[1,2,3])
```

       a  s  d
    0  1  1  1
    1  2  2  2
    2  3  3  3
    3  4  4  4
    4  5  5  5
    5  6  6  6
    


```python
# Read CSV

import pandas as pd

csv_1 = pd.read_excel(r"C:\Users\ASUS\\pandas\test.xlsx")

csv_1
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
      <th>Symbol</th>
      <th>Security</th>
      <th>Today - Volume</th>
      <th>AVG -volume</th>
      <th>change</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>classes</td>
      <td>entrepreise 1.llc</td>
      <td>765445</td>
      <td>43216</td>
      <td>90.097650</td>
    </tr>
    <tr>
      <th>1</th>
      <td>teachers</td>
      <td>entreprise 2.inc</td>
      <td>2456</td>
      <td>980007</td>
      <td>79.234500</td>
    </tr>
    <tr>
      <th>2</th>
      <td>doctors</td>
      <td>entreprise 3</td>
      <td>45632</td>
      <td>7689543</td>
      <td>70.562780</td>
    </tr>
    <tr>
      <th>3</th>
      <td>kids</td>
      <td>company4</td>
      <td>8769432</td>
      <td>675432</td>
      <td>69.724536</td>
    </tr>
    <tr>
      <th>4</th>
      <td>gadgets</td>
      <td>company5</td>
      <td>123456987</td>
      <td>1234</td>
      <td>65.897654</td>
    </tr>
    <tr>
      <th>5</th>
      <td>offices</td>
      <td>company6</td>
      <td>56438</td>
      <td>9870</td>
      <td>63.892568</td>
    </tr>
    <tr>
      <th>6</th>
      <td>laptops</td>
      <td>company7</td>
      <td>4532</td>
      <td>65432</td>
      <td>62.098765</td>
    </tr>
    <tr>
      <th>7</th>
      <td>books</td>
      <td>company8</td>
      <td>987654</td>
      <td>34543</td>
      <td>60.534289</td>
    </tr>
    <tr>
      <th>8</th>
      <td>roommates</td>
      <td>company9</td>
      <td>2245678987</td>
      <td>4567</td>
      <td>50.625438</td>
    </tr>
    <tr>
      <th>9</th>
      <td>colleges</td>
      <td>company10</td>
      <td>345345</td>
      <td>9876</td>
      <td>49.324567</td>
    </tr>
    <tr>
      <th>10</th>
      <td>chef</td>
      <td>startup11</td>
      <td>7865409</td>
      <td>56437</td>
      <td>48.765431</td>
    </tr>
    <tr>
      <th>11</th>
      <td>architect</td>
      <td>startup12</td>
      <td>345321</td>
      <td>34215</td>
      <td>45.876101</td>
    </tr>
    <tr>
      <th>12</th>
      <td>police officer</td>
      <td>startup13</td>
      <td>56434567</td>
      <td>34567</td>
      <td>44.765413</td>
    </tr>
    <tr>
      <th>13</th>
      <td>actor</td>
      <td>startup14</td>
      <td>23456543</td>
      <td>897654</td>
      <td>43.651433</td>
    </tr>
    <tr>
      <th>14</th>
      <td>electrician</td>
      <td>org15</td>
      <td>8765678</td>
      <td>6754</td>
      <td>40.765190</td>
    </tr>
    <tr>
      <th>15</th>
      <td>firefighter</td>
      <td>org16</td>
      <td>654321</td>
      <td>56432</td>
      <td>40.690165</td>
    </tr>
    <tr>
      <th>16</th>
      <td>waitress</td>
      <td>org17</td>
      <td>6547890</td>
      <td>67543</td>
      <td>40.509818</td>
    </tr>
  </tbody>
</table>
</div>




```python

```


```python
csv_2 = pd.read_excel(r"C:\Users\ASUS\\pandas\test.xlsx",nrows=4)
print(type(csv_2))
csv_2
```

    <class 'pandas.core.frame.DataFrame'>
    




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
      <th>Symbol</th>
      <th>Security</th>
      <th>Today - Volume</th>
      <th>AVG -volume</th>
      <th>change</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>classes</td>
      <td>entrepreise 1.llc</td>
      <td>765445</td>
      <td>43216</td>
      <td>90.097650</td>
    </tr>
    <tr>
      <th>1</th>
      <td>teachers</td>
      <td>entreprise 2.inc</td>
      <td>2456</td>
      <td>980007</td>
      <td>79.234500</td>
    </tr>
    <tr>
      <th>2</th>
      <td>doctors</td>
      <td>entreprise 3</td>
      <td>45632</td>
      <td>7689543</td>
      <td>70.562780</td>
    </tr>
    <tr>
      <th>3</th>
      <td>kids</td>
      <td>company4</td>
      <td>8769432</td>
      <td>675432</td>
      <td>69.724536</td>
    </tr>
  </tbody>
</table>
</div>




```python

```


```python
csv_3 = pd.read_excel(r"C:\Users\ASUS\\pandas\test.xlsx",usecols=["Symbol","change"])
csv_3
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
      <th>Symbol</th>
      <th>change</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>classes</td>
      <td>90.097650</td>
    </tr>
    <tr>
      <th>1</th>
      <td>teachers</td>
      <td>79.234500</td>
    </tr>
    <tr>
      <th>2</th>
      <td>doctors</td>
      <td>70.562780</td>
    </tr>
    <tr>
      <th>3</th>
      <td>kids</td>
      <td>69.724536</td>
    </tr>
    <tr>
      <th>4</th>
      <td>gadgets</td>
      <td>65.897654</td>
    </tr>
    <tr>
      <th>5</th>
      <td>offices</td>
      <td>63.892568</td>
    </tr>
    <tr>
      <th>6</th>
      <td>laptops</td>
      <td>62.098765</td>
    </tr>
    <tr>
      <th>7</th>
      <td>books</td>
      <td>60.534289</td>
    </tr>
    <tr>
      <th>8</th>
      <td>roommates</td>
      <td>50.625438</td>
    </tr>
    <tr>
      <th>9</th>
      <td>colleges</td>
      <td>49.324567</td>
    </tr>
    <tr>
      <th>10</th>
      <td>chef</td>
      <td>48.765431</td>
    </tr>
    <tr>
      <th>11</th>
      <td>architect</td>
      <td>45.876101</td>
    </tr>
    <tr>
      <th>12</th>
      <td>police officer</td>
      <td>44.765413</td>
    </tr>
    <tr>
      <th>13</th>
      <td>actor</td>
      <td>43.651433</td>
    </tr>
    <tr>
      <th>14</th>
      <td>electrician</td>
      <td>40.765190</td>
    </tr>
    <tr>
      <th>15</th>
      <td>firefighter</td>
      <td>40.690165</td>
    </tr>
    <tr>
      <th>16</th>
      <td>waitress</td>
      <td>40.509818</td>
    </tr>
  </tbody>
</table>
</div>




```python

```


```python
csv_4 = pd.read_excel(r"C:\Users\ASUS\\pandas\test.xlsx",usecols=[0,3])
csv_4
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
      <th>Symbol</th>
      <th>AVG -volume</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>classes</td>
      <td>43216</td>
    </tr>
    <tr>
      <th>1</th>
      <td>teachers</td>
      <td>980007</td>
    </tr>
    <tr>
      <th>2</th>
      <td>doctors</td>
      <td>7689543</td>
    </tr>
    <tr>
      <th>3</th>
      <td>kids</td>
      <td>675432</td>
    </tr>
    <tr>
      <th>4</th>
      <td>gadgets</td>
      <td>1234</td>
    </tr>
    <tr>
      <th>5</th>
      <td>offices</td>
      <td>9870</td>
    </tr>
    <tr>
      <th>6</th>
      <td>laptops</td>
      <td>65432</td>
    </tr>
    <tr>
      <th>7</th>
      <td>books</td>
      <td>34543</td>
    </tr>
    <tr>
      <th>8</th>
      <td>roommates</td>
      <td>4567</td>
    </tr>
    <tr>
      <th>9</th>
      <td>colleges</td>
      <td>9876</td>
    </tr>
    <tr>
      <th>10</th>
      <td>chef</td>
      <td>56437</td>
    </tr>
    <tr>
      <th>11</th>
      <td>architect</td>
      <td>34215</td>
    </tr>
    <tr>
      <th>12</th>
      <td>police officer</td>
      <td>34567</td>
    </tr>
    <tr>
      <th>13</th>
      <td>actor</td>
      <td>897654</td>
    </tr>
    <tr>
      <th>14</th>
      <td>electrician</td>
      <td>6754</td>
    </tr>
    <tr>
      <th>15</th>
      <td>firefighter</td>
      <td>56432</td>
    </tr>
    <tr>
      <th>16</th>
      <td>waitress</td>
      <td>67543</td>
    </tr>
  </tbody>
</table>
</div>




```python

```


```python
csv_5 = pd.read_excel(r"C:\Users\ASUS\\pandas\test.xlsx",skiprows=[0])
csv_5
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
      <th>classes</th>
      <th>entrepreise 1.llc</th>
      <th>765445</th>
      <th>43216</th>
      <th>90.09765</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>teachers</td>
      <td>entreprise 2.inc</td>
      <td>2456</td>
      <td>980007</td>
      <td>79.234500</td>
    </tr>
    <tr>
      <th>1</th>
      <td>doctors</td>
      <td>entreprise 3</td>
      <td>45632</td>
      <td>7689543</td>
      <td>70.562780</td>
    </tr>
    <tr>
      <th>2</th>
      <td>kids</td>
      <td>company4</td>
      <td>8769432</td>
      <td>675432</td>
      <td>69.724536</td>
    </tr>
    <tr>
      <th>3</th>
      <td>gadgets</td>
      <td>company5</td>
      <td>123456987</td>
      <td>1234</td>
      <td>65.897654</td>
    </tr>
    <tr>
      <th>4</th>
      <td>offices</td>
      <td>company6</td>
      <td>56438</td>
      <td>9870</td>
      <td>63.892568</td>
    </tr>
    <tr>
      <th>5</th>
      <td>laptops</td>
      <td>company7</td>
      <td>4532</td>
      <td>65432</td>
      <td>62.098765</td>
    </tr>
    <tr>
      <th>6</th>
      <td>books</td>
      <td>company8</td>
      <td>987654</td>
      <td>34543</td>
      <td>60.534289</td>
    </tr>
    <tr>
      <th>7</th>
      <td>roommates</td>
      <td>company9</td>
      <td>2245678987</td>
      <td>4567</td>
      <td>50.625438</td>
    </tr>
    <tr>
      <th>8</th>
      <td>colleges</td>
      <td>company10</td>
      <td>345345</td>
      <td>9876</td>
      <td>49.324567</td>
    </tr>
    <tr>
      <th>9</th>
      <td>chef</td>
      <td>startup11</td>
      <td>7865409</td>
      <td>56437</td>
      <td>48.765431</td>
    </tr>
    <tr>
      <th>10</th>
      <td>architect</td>
      <td>startup12</td>
      <td>345321</td>
      <td>34215</td>
      <td>45.876101</td>
    </tr>
    <tr>
      <th>11</th>
      <td>police officer</td>
      <td>startup13</td>
      <td>56434567</td>
      <td>34567</td>
      <td>44.765413</td>
    </tr>
    <tr>
      <th>12</th>
      <td>actor</td>
      <td>startup14</td>
      <td>23456543</td>
      <td>897654</td>
      <td>43.651433</td>
    </tr>
    <tr>
      <th>13</th>
      <td>electrician</td>
      <td>org15</td>
      <td>8765678</td>
      <td>6754</td>
      <td>40.765190</td>
    </tr>
    <tr>
      <th>14</th>
      <td>firefighter</td>
      <td>org16</td>
      <td>654321</td>
      <td>56432</td>
      <td>40.690165</td>
    </tr>
    <tr>
      <th>15</th>
      <td>waitress</td>
      <td>org17</td>
      <td>6547890</td>
      <td>67543</td>
      <td>40.509818</td>
    </tr>
  </tbody>
</table>
</div>




```python
csv_6 = pd.read_excel(r"C:\Users\ASUS\\pandas\test.xlsx",index_col="Symbol")
csv_6
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
      <th>Security</th>
      <th>Today - Volume</th>
      <th>AVG -volume</th>
      <th>change</th>
    </tr>
    <tr>
      <th>Symbol</th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>classes</th>
      <td>entrepreise 1.llc</td>
      <td>765445</td>
      <td>43216</td>
      <td>90.097650</td>
    </tr>
    <tr>
      <th>teachers</th>
      <td>entreprise 2.inc</td>
      <td>2456</td>
      <td>980007</td>
      <td>79.234500</td>
    </tr>
    <tr>
      <th>doctors</th>
      <td>entreprise 3</td>
      <td>45632</td>
      <td>7689543</td>
      <td>70.562780</td>
    </tr>
    <tr>
      <th>kids</th>
      <td>company4</td>
      <td>8769432</td>
      <td>675432</td>
      <td>69.724536</td>
    </tr>
    <tr>
      <th>gadgets</th>
      <td>company5</td>
      <td>123456987</td>
      <td>1234</td>
      <td>65.897654</td>
    </tr>
    <tr>
      <th>offices</th>
      <td>company6</td>
      <td>56438</td>
      <td>9870</td>
      <td>63.892568</td>
    </tr>
    <tr>
      <th>laptops</th>
      <td>company7</td>
      <td>4532</td>
      <td>65432</td>
      <td>62.098765</td>
    </tr>
    <tr>
      <th>books</th>
      <td>company8</td>
      <td>987654</td>
      <td>34543</td>
      <td>60.534289</td>
    </tr>
    <tr>
      <th>roommates</th>
      <td>company9</td>
      <td>2245678987</td>
      <td>4567</td>
      <td>50.625438</td>
    </tr>
    <tr>
      <th>colleges</th>
      <td>company10</td>
      <td>345345</td>
      <td>9876</td>
      <td>49.324567</td>
    </tr>
    <tr>
      <th>chef</th>
      <td>startup11</td>
      <td>7865409</td>
      <td>56437</td>
      <td>48.765431</td>
    </tr>
    <tr>
      <th>architect</th>
      <td>startup12</td>
      <td>345321</td>
      <td>34215</td>
      <td>45.876101</td>
    </tr>
    <tr>
      <th>police officer</th>
      <td>startup13</td>
      <td>56434567</td>
      <td>34567</td>
      <td>44.765413</td>
    </tr>
    <tr>
      <th>actor</th>
      <td>startup14</td>
      <td>23456543</td>
      <td>897654</td>
      <td>43.651433</td>
    </tr>
    <tr>
      <th>electrician</th>
      <td>org15</td>
      <td>8765678</td>
      <td>6754</td>
      <td>40.765190</td>
    </tr>
    <tr>
      <th>firefighter</th>
      <td>org16</td>
      <td>654321</td>
      <td>56432</td>
      <td>40.690165</td>
    </tr>
    <tr>
      <th>waitress</th>
      <td>org17</td>
      <td>6547890</td>
      <td>67543</td>
      <td>40.509818</td>
    </tr>
  </tbody>
</table>
</div>




```python
csv_7 = pd.read_excel(r"C:\Users\ASUS\\pandas\test.xlsx",header=2)
csv_7
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
      <th>teachers</th>
      <th>entreprise 2.inc</th>
      <th>2456</th>
      <th>980007</th>
      <th>79.2345</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>doctors</td>
      <td>entreprise 3</td>
      <td>45632</td>
      <td>7689543</td>
      <td>70.562780</td>
    </tr>
    <tr>
      <th>1</th>
      <td>kids</td>
      <td>company4</td>
      <td>8769432</td>
      <td>675432</td>
      <td>69.724536</td>
    </tr>
    <tr>
      <th>2</th>
      <td>gadgets</td>
      <td>company5</td>
      <td>123456987</td>
      <td>1234</td>
      <td>65.897654</td>
    </tr>
    <tr>
      <th>3</th>
      <td>offices</td>
      <td>company6</td>
      <td>56438</td>
      <td>9870</td>
      <td>63.892568</td>
    </tr>
    <tr>
      <th>4</th>
      <td>laptops</td>
      <td>company7</td>
      <td>4532</td>
      <td>65432</td>
      <td>62.098765</td>
    </tr>
    <tr>
      <th>5</th>
      <td>books</td>
      <td>company8</td>
      <td>987654</td>
      <td>34543</td>
      <td>60.534289</td>
    </tr>
    <tr>
      <th>6</th>
      <td>roommates</td>
      <td>company9</td>
      <td>2245678987</td>
      <td>4567</td>
      <td>50.625438</td>
    </tr>
    <tr>
      <th>7</th>
      <td>colleges</td>
      <td>company10</td>
      <td>345345</td>
      <td>9876</td>
      <td>49.324567</td>
    </tr>
    <tr>
      <th>8</th>
      <td>chef</td>
      <td>startup11</td>
      <td>7865409</td>
      <td>56437</td>
      <td>48.765431</td>
    </tr>
    <tr>
      <th>9</th>
      <td>architect</td>
      <td>startup12</td>
      <td>345321</td>
      <td>34215</td>
      <td>45.876101</td>
    </tr>
    <tr>
      <th>10</th>
      <td>police officer</td>
      <td>startup13</td>
      <td>56434567</td>
      <td>34567</td>
      <td>44.765413</td>
    </tr>
    <tr>
      <th>11</th>
      <td>actor</td>
      <td>startup14</td>
      <td>23456543</td>
      <td>897654</td>
      <td>43.651433</td>
    </tr>
    <tr>
      <th>12</th>
      <td>electrician</td>
      <td>org15</td>
      <td>8765678</td>
      <td>6754</td>
      <td>40.765190</td>
    </tr>
    <tr>
      <th>13</th>
      <td>firefighter</td>
      <td>org16</td>
      <td>654321</td>
      <td>56432</td>
      <td>40.690165</td>
    </tr>
    <tr>
      <th>14</th>
      <td>waitress</td>
      <td>org17</td>
      <td>6547890</td>
      <td>67543</td>
      <td>40.509818</td>
    </tr>
  </tbody>
</table>
</div>




```python
csv_8 = pd.read_excel(r"C:\Users\ASUS\\pandas\test.xlsx",header = None)
csv_8
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
      <th>0</th>
      <th>1</th>
      <th>2</th>
      <th>3</th>
      <th>4</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>Symbol</td>
      <td>Security</td>
      <td>Today - Volume</td>
      <td>AVG -volume</td>
      <td>change</td>
    </tr>
    <tr>
      <th>1</th>
      <td>classes</td>
      <td>entrepreise 1.llc</td>
      <td>765445</td>
      <td>43216</td>
      <td>90.09765</td>
    </tr>
    <tr>
      <th>2</th>
      <td>teachers</td>
      <td>entreprise 2.inc</td>
      <td>2456</td>
      <td>980007</td>
      <td>79.2345</td>
    </tr>
    <tr>
      <th>3</th>
      <td>doctors</td>
      <td>entreprise 3</td>
      <td>45632</td>
      <td>7689543</td>
      <td>70.56278</td>
    </tr>
    <tr>
      <th>4</th>
      <td>kids</td>
      <td>company4</td>
      <td>8769432</td>
      <td>675432</td>
      <td>69.724536</td>
    </tr>
    <tr>
      <th>5</th>
      <td>gadgets</td>
      <td>company5</td>
      <td>123456987</td>
      <td>1234</td>
      <td>65.897654</td>
    </tr>
    <tr>
      <th>6</th>
      <td>offices</td>
      <td>company6</td>
      <td>56438</td>
      <td>9870</td>
      <td>63.89256788</td>
    </tr>
    <tr>
      <th>7</th>
      <td>laptops</td>
      <td>company7</td>
      <td>4532</td>
      <td>65432</td>
      <td>62.098765</td>
    </tr>
    <tr>
      <th>8</th>
      <td>books</td>
      <td>company8</td>
      <td>987654</td>
      <td>34543</td>
      <td>60.534289</td>
    </tr>
    <tr>
      <th>9</th>
      <td>roommates</td>
      <td>company9</td>
      <td>2245678987</td>
      <td>4567</td>
      <td>50.6254378</td>
    </tr>
    <tr>
      <th>10</th>
      <td>colleges</td>
      <td>company10</td>
      <td>345345</td>
      <td>9876</td>
      <td>49.324567</td>
    </tr>
    <tr>
      <th>11</th>
      <td>chef</td>
      <td>startup11</td>
      <td>7865409</td>
      <td>56437</td>
      <td>48.7654312</td>
    </tr>
    <tr>
      <th>12</th>
      <td>architect</td>
      <td>startup12</td>
      <td>345321</td>
      <td>34215</td>
      <td>45.87610098</td>
    </tr>
    <tr>
      <th>13</th>
      <td>police officer</td>
      <td>startup13</td>
      <td>56434567</td>
      <td>34567</td>
      <td>44.7654132</td>
    </tr>
    <tr>
      <th>14</th>
      <td>actor</td>
      <td>startup14</td>
      <td>23456543</td>
      <td>897654</td>
      <td>43.6514328</td>
    </tr>
    <tr>
      <th>15</th>
      <td>electrician</td>
      <td>org15</td>
      <td>8765678</td>
      <td>6754</td>
      <td>40.7651900</td>
    </tr>
    <tr>
      <th>16</th>
      <td>firefighter</td>
      <td>org16</td>
      <td>654321</td>
      <td>56432</td>
      <td>40.6901653</td>
    </tr>
    <tr>
      <th>17</th>
      <td>waitress</td>
      <td>org17</td>
      <td>6547890</td>
      <td>67543</td>
      <td>40.509817643</td>
    </tr>
  </tbody>
</table>
</div>




```python
csv_9 = pd.read_excel(r"C:\Users\ASUS\\pandas\test.xlsx", dtype={"Today - Volume":"float"})
csv_9
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
      <th>Symbol</th>
      <th>Security</th>
      <th>Today - Volume</th>
      <th>AVG -volume</th>
      <th>change</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>classes</td>
      <td>entrepreise 1.llc</td>
      <td>7.654450e+05</td>
      <td>43216</td>
      <td>90.097650</td>
    </tr>
    <tr>
      <th>1</th>
      <td>teachers</td>
      <td>entreprise 2.inc</td>
      <td>2.456000e+03</td>
      <td>980007</td>
      <td>79.234500</td>
    </tr>
    <tr>
      <th>2</th>
      <td>doctors</td>
      <td>entreprise 3</td>
      <td>4.563200e+04</td>
      <td>7689543</td>
      <td>70.562780</td>
    </tr>
    <tr>
      <th>3</th>
      <td>kids</td>
      <td>company4</td>
      <td>8.769432e+06</td>
      <td>675432</td>
      <td>69.724536</td>
    </tr>
    <tr>
      <th>4</th>
      <td>gadgets</td>
      <td>company5</td>
      <td>1.234570e+08</td>
      <td>1234</td>
      <td>65.897654</td>
    </tr>
    <tr>
      <th>5</th>
      <td>offices</td>
      <td>company6</td>
      <td>5.643800e+04</td>
      <td>9870</td>
      <td>63.892568</td>
    </tr>
    <tr>
      <th>6</th>
      <td>laptops</td>
      <td>company7</td>
      <td>4.532000e+03</td>
      <td>65432</td>
      <td>62.098765</td>
    </tr>
    <tr>
      <th>7</th>
      <td>books</td>
      <td>company8</td>
      <td>9.876540e+05</td>
      <td>34543</td>
      <td>60.534289</td>
    </tr>
    <tr>
      <th>8</th>
      <td>roommates</td>
      <td>company9</td>
      <td>2.245679e+09</td>
      <td>4567</td>
      <td>50.625438</td>
    </tr>
    <tr>
      <th>9</th>
      <td>colleges</td>
      <td>company10</td>
      <td>3.453450e+05</td>
      <td>9876</td>
      <td>49.324567</td>
    </tr>
    <tr>
      <th>10</th>
      <td>chef</td>
      <td>startup11</td>
      <td>7.865409e+06</td>
      <td>56437</td>
      <td>48.765431</td>
    </tr>
    <tr>
      <th>11</th>
      <td>architect</td>
      <td>startup12</td>
      <td>3.453210e+05</td>
      <td>34215</td>
      <td>45.876101</td>
    </tr>
    <tr>
      <th>12</th>
      <td>police officer</td>
      <td>startup13</td>
      <td>5.643457e+07</td>
      <td>34567</td>
      <td>44.765413</td>
    </tr>
    <tr>
      <th>13</th>
      <td>actor</td>
      <td>startup14</td>
      <td>2.345654e+07</td>
      <td>897654</td>
      <td>43.651433</td>
    </tr>
    <tr>
      <th>14</th>
      <td>electrician</td>
      <td>org15</td>
      <td>8.765678e+06</td>
      <td>6754</td>
      <td>40.765190</td>
    </tr>
    <tr>
      <th>15</th>
      <td>firefighter</td>
      <td>org16</td>
      <td>6.543210e+05</td>
      <td>56432</td>
      <td>40.690165</td>
    </tr>
    <tr>
      <th>16</th>
      <td>waitress</td>
      <td>org17</td>
      <td>6.547890e+06</td>
      <td>67543</td>
      <td>40.509818</td>
    </tr>
  </tbody>
</table>
</div>




```python
# Pandas Function

import pandas as pd

csv_11 = pd.read_excel(r"C:\Users\ASUS\\pandas\test.xlsx")

csv_11
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
      <th>Symbol</th>
      <th>Security</th>
      <th>Today - Volume</th>
      <th>AVG -volume</th>
      <th>change</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>classes</td>
      <td>entrepreise 1.llc</td>
      <td>765445</td>
      <td>43216</td>
      <td>90.097650</td>
    </tr>
    <tr>
      <th>1</th>
      <td>teachers</td>
      <td>entreprise 2.inc</td>
      <td>2456</td>
      <td>980007</td>
      <td>79.234500</td>
    </tr>
    <tr>
      <th>2</th>
      <td>doctors</td>
      <td>entreprise 3</td>
      <td>45632</td>
      <td>7689543</td>
      <td>70.562780</td>
    </tr>
    <tr>
      <th>3</th>
      <td>kids</td>
      <td>company4</td>
      <td>8769432</td>
      <td>675432</td>
      <td>69.724536</td>
    </tr>
    <tr>
      <th>4</th>
      <td>gadgets</td>
      <td>company5</td>
      <td>123456987</td>
      <td>1234</td>
      <td>65.897654</td>
    </tr>
    <tr>
      <th>5</th>
      <td>offices</td>
      <td>company6</td>
      <td>56438</td>
      <td>9870</td>
      <td>63.892568</td>
    </tr>
    <tr>
      <th>6</th>
      <td>laptops</td>
      <td>company7</td>
      <td>4532</td>
      <td>65432</td>
      <td>62.098765</td>
    </tr>
    <tr>
      <th>7</th>
      <td>books</td>
      <td>company8</td>
      <td>987654</td>
      <td>34543</td>
      <td>60.534289</td>
    </tr>
    <tr>
      <th>8</th>
      <td>roommates</td>
      <td>company9</td>
      <td>2245678987</td>
      <td>4567</td>
      <td>50.625438</td>
    </tr>
    <tr>
      <th>9</th>
      <td>colleges</td>
      <td>company10</td>
      <td>345345</td>
      <td>9876</td>
      <td>49.324567</td>
    </tr>
    <tr>
      <th>10</th>
      <td>chef</td>
      <td>startup11</td>
      <td>7865409</td>
      <td>56437</td>
      <td>48.765431</td>
    </tr>
    <tr>
      <th>11</th>
      <td>architect</td>
      <td>startup12</td>
      <td>345321</td>
      <td>34215</td>
      <td>45.876101</td>
    </tr>
    <tr>
      <th>12</th>
      <td>police officer</td>
      <td>startup13</td>
      <td>56434567</td>
      <td>34567</td>
      <td>44.765413</td>
    </tr>
    <tr>
      <th>13</th>
      <td>actor</td>
      <td>startup14</td>
      <td>23456543</td>
      <td>897654</td>
      <td>43.651433</td>
    </tr>
    <tr>
      <th>14</th>
      <td>electrician</td>
      <td>org15</td>
      <td>8765678</td>
      <td>6754</td>
      <td>40.765190</td>
    </tr>
    <tr>
      <th>15</th>
      <td>firefighter</td>
      <td>org16</td>
      <td>654321</td>
      <td>56432</td>
      <td>40.690165</td>
    </tr>
    <tr>
      <th>16</th>
      <td>waitress</td>
      <td>org17</td>
      <td>6547890</td>
      <td>67543</td>
      <td>40.509818</td>
    </tr>
  </tbody>
</table>
</div>




```python
csv_11.index
```




    RangeIndex(start=0, stop=17, step=1)




```python
csv_11.columns
```




    Index(['Symbol', 'Security', 'Today - Volume', 'AVG -volume', 'change'], dtype='object')




```python
csv_11.describe()
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
      <th>Today - Volume</th>
      <th>AVG -volume</th>
      <th>change</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>count</th>
      <td>1.700000e+01</td>
      <td>1.700000e+01</td>
      <td>17.000000</td>
    </tr>
    <tr>
      <th>mean</th>
      <td>1.461284e+08</td>
      <td>6.274895e+05</td>
      <td>56.883312</td>
    </tr>
    <tr>
      <th>std</th>
      <td>5.419468e+08</td>
      <td>1.848627e+06</td>
      <td>14.834704</td>
    </tr>
    <tr>
      <th>min</th>
      <td>2.456000e+03</td>
      <td>1.234000e+03</td>
      <td>40.509818</td>
    </tr>
    <tr>
      <th>25%</th>
      <td>3.453210e+05</td>
      <td>9.876000e+03</td>
      <td>44.765413</td>
    </tr>
    <tr>
      <th>50%</th>
      <td>9.876540e+05</td>
      <td>4.321600e+04</td>
      <td>50.625438</td>
    </tr>
    <tr>
      <th>75%</th>
      <td>8.769432e+06</td>
      <td>6.754300e+04</td>
      <td>65.897654</td>
    </tr>
    <tr>
      <th>max</th>
      <td>2.245679e+09</td>
      <td>7.689543e+06</td>
      <td>90.097650</td>
    </tr>
  </tbody>
</table>
</div>




```python
csv_11.head()
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
      <th>Symbol</th>
      <th>Security</th>
      <th>Today - Volume</th>
      <th>AVG -volume</th>
      <th>change</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>classes</td>
      <td>entrepreise 1.llc</td>
      <td>765445</td>
      <td>43216</td>
      <td>90.097650</td>
    </tr>
    <tr>
      <th>1</th>
      <td>teachers</td>
      <td>entreprise 2.inc</td>
      <td>2456</td>
      <td>980007</td>
      <td>79.234500</td>
    </tr>
    <tr>
      <th>2</th>
      <td>doctors</td>
      <td>entreprise 3</td>
      <td>45632</td>
      <td>7689543</td>
      <td>70.562780</td>
    </tr>
    <tr>
      <th>3</th>
      <td>kids</td>
      <td>company4</td>
      <td>8769432</td>
      <td>675432</td>
      <td>69.724536</td>
    </tr>
    <tr>
      <th>4</th>
      <td>gadgets</td>
      <td>company5</td>
      <td>123456987</td>
      <td>1234</td>
      <td>65.897654</td>
    </tr>
  </tbody>
</table>
</div>




```python
csv_11.tail()
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
      <th>Symbol</th>
      <th>Security</th>
      <th>Today - Volume</th>
      <th>AVG -volume</th>
      <th>change</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>12</th>
      <td>police officer</td>
      <td>startup13</td>
      <td>56434567</td>
      <td>34567</td>
      <td>44.765413</td>
    </tr>
    <tr>
      <th>13</th>
      <td>actor</td>
      <td>startup14</td>
      <td>23456543</td>
      <td>897654</td>
      <td>43.651433</td>
    </tr>
    <tr>
      <th>14</th>
      <td>electrician</td>
      <td>org15</td>
      <td>8765678</td>
      <td>6754</td>
      <td>40.765190</td>
    </tr>
    <tr>
      <th>15</th>
      <td>firefighter</td>
      <td>org16</td>
      <td>654321</td>
      <td>56432</td>
      <td>40.690165</td>
    </tr>
    <tr>
      <th>16</th>
      <td>waitress</td>
      <td>org17</td>
      <td>6547890</td>
      <td>67543</td>
      <td>40.509818</td>
    </tr>
  </tbody>
</table>
</div>




```python
csv_11[:5]
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
      <th>Symbol</th>
      <th>Security</th>
      <th>Today - Volume</th>
      <th>AVG -volume</th>
      <th>change</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>classes</td>
      <td>entrepreise 1.llc</td>
      <td>765445</td>
      <td>43216</td>
      <td>90.097650</td>
    </tr>
    <tr>
      <th>1</th>
      <td>teachers</td>
      <td>entreprise 2.inc</td>
      <td>2456</td>
      <td>980007</td>
      <td>79.234500</td>
    </tr>
    <tr>
      <th>2</th>
      <td>doctors</td>
      <td>entreprise 3</td>
      <td>45632</td>
      <td>7689543</td>
      <td>70.562780</td>
    </tr>
    <tr>
      <th>3</th>
      <td>kids</td>
      <td>company4</td>
      <td>8769432</td>
      <td>675432</td>
      <td>69.724536</td>
    </tr>
    <tr>
      <th>4</th>
      <td>gadgets</td>
      <td>company5</td>
      <td>123456987</td>
      <td>1234</td>
      <td>65.897654</td>
    </tr>
  </tbody>
</table>
</div>




```python
csv_11[6:11]
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
      <th>Symbol</th>
      <th>Security</th>
      <th>Today - Volume</th>
      <th>AVG -volume</th>
      <th>change</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>6</th>
      <td>laptops</td>
      <td>company7</td>
      <td>4532</td>
      <td>65432</td>
      <td>62.098765</td>
    </tr>
    <tr>
      <th>7</th>
      <td>books</td>
      <td>company8</td>
      <td>987654</td>
      <td>34543</td>
      <td>60.534289</td>
    </tr>
    <tr>
      <th>8</th>
      <td>roommates</td>
      <td>company9</td>
      <td>2245678987</td>
      <td>4567</td>
      <td>50.625438</td>
    </tr>
    <tr>
      <th>9</th>
      <td>colleges</td>
      <td>company10</td>
      <td>345345</td>
      <td>9876</td>
      <td>49.324567</td>
    </tr>
    <tr>
      <th>10</th>
      <td>chef</td>
      <td>startup11</td>
      <td>7865409</td>
      <td>56437</td>
      <td>48.765431</td>
    </tr>
  </tbody>
</table>
</div>




```python
print(type(csv_11))
```

    <class 'pandas.core.frame.DataFrame'>
    


```python
csv_11.index.array
```




    <NumpyExtensionArray>
    [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]
    Length: 17, dtype: int64




```python
csv_11.to_numpy()
```




    array([['classes', 'entrepreise 1.llc', 765445, 43216, 90.09765],
           ['teachers', 'entreprise 2.inc', 2456, 980007, 79.2345],
           ['doctors', 'entreprise 3', 45632, 7689543, 70.56278],
           ['kids', 'company4', 8769432, 675432, 69.724536],
           ['gadgets', 'company5', 123456987, 1234, 65.897654],
           ['offices', 'company6', 56438, 9870, 63.89256788],
           ['laptops', 'company7', 4532, 65432, 62.098765],
           ['books', 'company8', 987654, 34543, 60.534289],
           ['roommates', 'company9', 2245678987, 4567, 50.6254378],
           ['colleges', 'company10', 345345, 9876, 49.324567],
           ['chef', 'startup11', 7865409, 56437, 48.7654312],
           ['architect', 'startup12', 345321, 34215, 45.87610098],
           ['police officer', 'startup13', 56434567, 34567, 44.7654132],
           ['actor', 'startup14', 23456543, 897654, 43.6514328],
           ['electrician', 'org15', 8765678, 6754, 40.76519],
           ['firefighter', 'org16', 654321, 56432, 40.6901653],
           ['waitress', 'org17', 6547890, 67543, 40.509817643]], dtype=object)




```python
import numpy as np
v = np.asarray(csv_11)
v
```




    array([['classes', 'entrepreise 1.llc', 765445, 43216, 90.09765],
           ['teachers', 'entreprise 2.inc', 2456, 980007, 79.2345],
           ['doctors', 'entreprise 3', 45632, 7689543, 70.56278],
           ['kids', 'company4', 8769432, 675432, 69.724536],
           ['gadgets', 'company5', 123456987, 1234, 65.897654],
           ['offices', 'company6', 56438, 9870, 63.89256788],
           ['laptops', 'company7', 4532, 65432, 62.098765],
           ['books', 'company8', 987654, 34543, 60.534289],
           ['roommates', 'company9', 2245678987, 4567, 50.6254378],
           ['colleges', 'company10', 345345, 9876, 49.324567],
           ['chef', 'startup11', 7865409, 56437, 48.7654312],
           ['architect', 'startup12', 345321, 34215, 45.87610098],
           ['police officer', 'startup13', 56434567, 34567, 44.7654132],
           ['actor', 'startup14', 23456543, 897654, 43.6514328],
           ['electrician', 'org15', 8765678, 6754, 40.76519],
           ['firefighter', 'org16', 654321, 56432, 40.6901653],
           ['waitress', 'org17', 6547890, 67543, 40.509817643]], dtype=object)




```python
csv_11.sort_index(axis=0,ascending=False)
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
      <th>Symbol</th>
      <th>Security</th>
      <th>Today - Volume</th>
      <th>AVG -volume</th>
      <th>change</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>16</th>
      <td>waitress</td>
      <td>org17</td>
      <td>6547890</td>
      <td>67543</td>
      <td>40.509818</td>
    </tr>
    <tr>
      <th>15</th>
      <td>firefighter</td>
      <td>org16</td>
      <td>654321</td>
      <td>56432</td>
      <td>40.690165</td>
    </tr>
    <tr>
      <th>14</th>
      <td>electrician</td>
      <td>org15</td>
      <td>8765678</td>
      <td>6754</td>
      <td>40.765190</td>
    </tr>
    <tr>
      <th>13</th>
      <td>actor</td>
      <td>startup14</td>
      <td>23456543</td>
      <td>897654</td>
      <td>43.651433</td>
    </tr>
    <tr>
      <th>12</th>
      <td>police officer</td>
      <td>startup13</td>
      <td>56434567</td>
      <td>34567</td>
      <td>44.765413</td>
    </tr>
    <tr>
      <th>11</th>
      <td>architect</td>
      <td>startup12</td>
      <td>345321</td>
      <td>34215</td>
      <td>45.876101</td>
    </tr>
    <tr>
      <th>10</th>
      <td>chef</td>
      <td>startup11</td>
      <td>7865409</td>
      <td>56437</td>
      <td>48.765431</td>
    </tr>
    <tr>
      <th>9</th>
      <td>colleges</td>
      <td>company10</td>
      <td>345345</td>
      <td>9876</td>
      <td>49.324567</td>
    </tr>
    <tr>
      <th>8</th>
      <td>roommates</td>
      <td>company9</td>
      <td>2245678987</td>
      <td>4567</td>
      <td>50.625438</td>
    </tr>
    <tr>
      <th>7</th>
      <td>books</td>
      <td>company8</td>
      <td>987654</td>
      <td>34543</td>
      <td>60.534289</td>
    </tr>
    <tr>
      <th>6</th>
      <td>laptops</td>
      <td>company7</td>
      <td>4532</td>
      <td>65432</td>
      <td>62.098765</td>
    </tr>
    <tr>
      <th>5</th>
      <td>offices</td>
      <td>company6</td>
      <td>56438</td>
      <td>9870</td>
      <td>63.892568</td>
    </tr>
    <tr>
      <th>4</th>
      <td>gadgets</td>
      <td>company5</td>
      <td>123456987</td>
      <td>1234</td>
      <td>65.897654</td>
    </tr>
    <tr>
      <th>3</th>
      <td>kids</td>
      <td>company4</td>
      <td>8769432</td>
      <td>675432</td>
      <td>69.724536</td>
    </tr>
    <tr>
      <th>2</th>
      <td>doctors</td>
      <td>entreprise 3</td>
      <td>45632</td>
      <td>7689543</td>
      <td>70.562780</td>
    </tr>
    <tr>
      <th>1</th>
      <td>teachers</td>
      <td>entreprise 2.inc</td>
      <td>2456</td>
      <td>980007</td>
      <td>79.234500</td>
    </tr>
    <tr>
      <th>0</th>
      <td>classes</td>
      <td>entrepreise 1.llc</td>
      <td>765445</td>
      <td>43216</td>
      <td>90.097650</td>
    </tr>
  </tbody>
</table>
</div>




```python
csv_11.loc[[2,3],["Symbol", "Security"]]
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
      <th>Symbol</th>
      <th>Security</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>2</th>
      <td>doctors</td>
      <td>entreprise 3</td>
    </tr>
    <tr>
      <th>3</th>
      <td>kids</td>
      <td>company4</td>
    </tr>
  </tbody>
</table>
</div>




```python
csv_11.loc[[2,3],:]
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
      <th>Symbol</th>
      <th>Security</th>
      <th>Today - Volume</th>
      <th>AVG -volume</th>
      <th>change</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>2</th>
      <td>doctors</td>
      <td>entreprise 3</td>
      <td>45632</td>
      <td>7689543</td>
      <td>70.562780</td>
    </tr>
    <tr>
      <th>3</th>
      <td>kids</td>
      <td>company4</td>
      <td>8769432</td>
      <td>675432</td>
      <td>69.724536</td>
    </tr>
  </tbody>
</table>
</div>




```python
csv_11.iloc[0,1]
```




    'entrepreise 1.llc'




```python
csv_11.iloc[0,2]
```




    765445




```python
csv_11.drop("Security", axis=1)
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
      <th>Symbol</th>
      <th>Today - Volume</th>
      <th>AVG -volume</th>
      <th>change</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>classes</td>
      <td>765445</td>
      <td>43216</td>
      <td>90.097650</td>
    </tr>
    <tr>
      <th>1</th>
      <td>teachers</td>
      <td>2456</td>
      <td>980007</td>
      <td>79.234500</td>
    </tr>
    <tr>
      <th>2</th>
      <td>doctors</td>
      <td>45632</td>
      <td>7689543</td>
      <td>70.562780</td>
    </tr>
    <tr>
      <th>3</th>
      <td>kids</td>
      <td>8769432</td>
      <td>675432</td>
      <td>69.724536</td>
    </tr>
    <tr>
      <th>4</th>
      <td>gadgets</td>
      <td>123456987</td>
      <td>1234</td>
      <td>65.897654</td>
    </tr>
    <tr>
      <th>5</th>
      <td>offices</td>
      <td>56438</td>
      <td>9870</td>
      <td>63.892568</td>
    </tr>
    <tr>
      <th>6</th>
      <td>laptops</td>
      <td>4532</td>
      <td>65432</td>
      <td>62.098765</td>
    </tr>
    <tr>
      <th>7</th>
      <td>books</td>
      <td>987654</td>
      <td>34543</td>
      <td>60.534289</td>
    </tr>
    <tr>
      <th>8</th>
      <td>roommates</td>
      <td>2245678987</td>
      <td>4567</td>
      <td>50.625438</td>
    </tr>
    <tr>
      <th>9</th>
      <td>colleges</td>
      <td>345345</td>
      <td>9876</td>
      <td>49.324567</td>
    </tr>
    <tr>
      <th>10</th>
      <td>chef</td>
      <td>7865409</td>
      <td>56437</td>
      <td>48.765431</td>
    </tr>
    <tr>
      <th>11</th>
      <td>architect</td>
      <td>345321</td>
      <td>34215</td>
      <td>45.876101</td>
    </tr>
    <tr>
      <th>12</th>
      <td>police officer</td>
      <td>56434567</td>
      <td>34567</td>
      <td>44.765413</td>
    </tr>
    <tr>
      <th>13</th>
      <td>actor</td>
      <td>23456543</td>
      <td>897654</td>
      <td>43.651433</td>
    </tr>
    <tr>
      <th>14</th>
      <td>electrician</td>
      <td>8765678</td>
      <td>6754</td>
      <td>40.765190</td>
    </tr>
    <tr>
      <th>15</th>
      <td>firefighter</td>
      <td>654321</td>
      <td>56432</td>
      <td>40.690165</td>
    </tr>
    <tr>
      <th>16</th>
      <td>waitress</td>
      <td>6547890</td>
      <td>67543</td>
      <td>40.509818</td>
    </tr>
  </tbody>
</table>
</div>




```python
# #Handling Missing Values

import pandas as pd

csv_13 = pd.read_excel(r"C:\Users\ASUS\\pandas\test.xlsx")

csv_13
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
      <th>Symbol</th>
      <th>Security</th>
      <th>Today - Volume</th>
      <th>AVG -volume</th>
      <th>change</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>classes</td>
      <td>entrepreise 1.llc</td>
      <td>7.654450e+05</td>
      <td>43216.0</td>
      <td>90.097650</td>
    </tr>
    <tr>
      <th>1</th>
      <td>teachers</td>
      <td>entreprise 2.inc</td>
      <td>NaN</td>
      <td>980007.0</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>2</th>
      <td>doctors</td>
      <td>entreprise 3</td>
      <td>4.563200e+04</td>
      <td>7689543.0</td>
      <td>70.562780</td>
    </tr>
    <tr>
      <th>3</th>
      <td>kids</td>
      <td>company4</td>
      <td>8.769432e+06</td>
      <td>675432.0</td>
      <td>69.724536</td>
    </tr>
    <tr>
      <th>4</th>
      <td>gadgets</td>
      <td>company5</td>
      <td>1.234570e+08</td>
      <td>1234.0</td>
      <td>65.897654</td>
    </tr>
    <tr>
      <th>5</th>
      <td>offices</td>
      <td>company6</td>
      <td>5.643800e+04</td>
      <td>9870.0</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>6</th>
      <td>laptops</td>
      <td>company7</td>
      <td>4.532000e+03</td>
      <td>65432.0</td>
      <td>62.098765</td>
    </tr>
    <tr>
      <th>7</th>
      <td>books</td>
      <td>company8</td>
      <td>9.876540e+05</td>
      <td>34543.0</td>
      <td>60.534289</td>
    </tr>
    <tr>
      <th>8</th>
      <td>roommates</td>
      <td>company9</td>
      <td>2.245679e+09</td>
      <td>4567.0</td>
      <td>50.625438</td>
    </tr>
    <tr>
      <th>9</th>
      <td>colleges</td>
      <td>company10</td>
      <td>NaN</td>
      <td>9876.0</td>
      <td>49.324567</td>
    </tr>
    <tr>
      <th>10</th>
      <td>chef</td>
      <td>startup11</td>
      <td>7.865409e+06</td>
      <td>56437.0</td>
      <td>48.765431</td>
    </tr>
    <tr>
      <th>11</th>
      <td>architect</td>
      <td>startup12</td>
      <td>3.453210e+05</td>
      <td>NaN</td>
      <td>45.876101</td>
    </tr>
    <tr>
      <th>12</th>
      <td>police officer</td>
      <td>startup13</td>
      <td>5.643457e+07</td>
      <td>34567.0</td>
      <td>44.765413</td>
    </tr>
    <tr>
      <th>13</th>
      <td>actor</td>
      <td>startup14</td>
      <td>2.345654e+07</td>
      <td>897654.0</td>
      <td>43.651433</td>
    </tr>
    <tr>
      <th>14</th>
      <td>electrician</td>
      <td>org15</td>
      <td>NaN</td>
      <td>6754.0</td>
      <td>40.765190</td>
    </tr>
    <tr>
      <th>15</th>
      <td>firefighter</td>
      <td>org16</td>
      <td>6.543210e+05</td>
      <td>56432.0</td>
      <td>40.690165</td>
    </tr>
    <tr>
      <th>16</th>
      <td>waitress</td>
      <td>org17</td>
      <td>6.547890e+06</td>
      <td>67543.0</td>
      <td>40.509818</td>
    </tr>
  </tbody>
</table>
</div>




```python
csv_13.dropna(axis=1)
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
      <th>Symbol</th>
      <th>Security</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>classes</td>
      <td>entrepreise 1.llc</td>
    </tr>
    <tr>
      <th>1</th>
      <td>teachers</td>
      <td>entreprise 2.inc</td>
    </tr>
    <tr>
      <th>2</th>
      <td>doctors</td>
      <td>entreprise 3</td>
    </tr>
    <tr>
      <th>3</th>
      <td>kids</td>
      <td>company4</td>
    </tr>
    <tr>
      <th>4</th>
      <td>gadgets</td>
      <td>company5</td>
    </tr>
    <tr>
      <th>5</th>
      <td>offices</td>
      <td>company6</td>
    </tr>
    <tr>
      <th>6</th>
      <td>laptops</td>
      <td>company7</td>
    </tr>
    <tr>
      <th>7</th>
      <td>books</td>
      <td>company8</td>
    </tr>
    <tr>
      <th>8</th>
      <td>roommates</td>
      <td>company9</td>
    </tr>
    <tr>
      <th>9</th>
      <td>colleges</td>
      <td>company10</td>
    </tr>
    <tr>
      <th>10</th>
      <td>chef</td>
      <td>startup11</td>
    </tr>
    <tr>
      <th>11</th>
      <td>architect</td>
      <td>startup12</td>
    </tr>
    <tr>
      <th>12</th>
      <td>police officer</td>
      <td>startup13</td>
    </tr>
    <tr>
      <th>13</th>
      <td>actor</td>
      <td>startup14</td>
    </tr>
    <tr>
      <th>14</th>
      <td>electrician</td>
      <td>org15</td>
    </tr>
    <tr>
      <th>15</th>
      <td>firefighter</td>
      <td>org16</td>
    </tr>
    <tr>
      <th>16</th>
      <td>waitress</td>
      <td>org17</td>
    </tr>
  </tbody>
</table>
</div>




```python
csv_13.dropna(how="any")
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
      <th>Symbol</th>
      <th>Security</th>
      <th>Today - Volume</th>
      <th>AVG -volume</th>
      <th>change</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>classes</td>
      <td>entrepreise 1.llc</td>
      <td>7.654450e+05</td>
      <td>43216.0</td>
      <td>90.097650</td>
    </tr>
    <tr>
      <th>2</th>
      <td>doctors</td>
      <td>entreprise 3</td>
      <td>4.563200e+04</td>
      <td>7689543.0</td>
      <td>70.562780</td>
    </tr>
    <tr>
      <th>3</th>
      <td>kids</td>
      <td>company4</td>
      <td>8.769432e+06</td>
      <td>675432.0</td>
      <td>69.724536</td>
    </tr>
    <tr>
      <th>4</th>
      <td>gadgets</td>
      <td>company5</td>
      <td>1.234570e+08</td>
      <td>1234.0</td>
      <td>65.897654</td>
    </tr>
    <tr>
      <th>6</th>
      <td>laptops</td>
      <td>company7</td>
      <td>4.532000e+03</td>
      <td>65432.0</td>
      <td>62.098765</td>
    </tr>
    <tr>
      <th>7</th>
      <td>books</td>
      <td>company8</td>
      <td>9.876540e+05</td>
      <td>34543.0</td>
      <td>60.534289</td>
    </tr>
    <tr>
      <th>8</th>
      <td>roommates</td>
      <td>company9</td>
      <td>2.245679e+09</td>
      <td>4567.0</td>
      <td>50.625438</td>
    </tr>
    <tr>
      <th>10</th>
      <td>chef</td>
      <td>startup11</td>
      <td>7.865409e+06</td>
      <td>56437.0</td>
      <td>48.765431</td>
    </tr>
    <tr>
      <th>12</th>
      <td>police officer</td>
      <td>startup13</td>
      <td>5.643457e+07</td>
      <td>34567.0</td>
      <td>44.765413</td>
    </tr>
    <tr>
      <th>13</th>
      <td>actor</td>
      <td>startup14</td>
      <td>2.345654e+07</td>
      <td>897654.0</td>
      <td>43.651433</td>
    </tr>
    <tr>
      <th>15</th>
      <td>firefighter</td>
      <td>org16</td>
      <td>6.543210e+05</td>
      <td>56432.0</td>
      <td>40.690165</td>
    </tr>
    <tr>
      <th>16</th>
      <td>waitress</td>
      <td>org17</td>
      <td>6.547890e+06</td>
      <td>67543.0</td>
      <td>40.509818</td>
    </tr>
  </tbody>
</table>
</div>




```python
csv_13.dropna(subset=["change"])
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
      <th>Symbol</th>
      <th>Security</th>
      <th>Today - Volume</th>
      <th>AVG -volume</th>
      <th>change</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>classes</td>
      <td>entrepreise 1.llc</td>
      <td>7.654450e+05</td>
      <td>43216.0</td>
      <td>90.097650</td>
    </tr>
    <tr>
      <th>2</th>
      <td>doctors</td>
      <td>entreprise 3</td>
      <td>4.563200e+04</td>
      <td>7689543.0</td>
      <td>70.562780</td>
    </tr>
    <tr>
      <th>3</th>
      <td>kids</td>
      <td>company4</td>
      <td>8.769432e+06</td>
      <td>675432.0</td>
      <td>69.724536</td>
    </tr>
    <tr>
      <th>4</th>
      <td>gadgets</td>
      <td>company5</td>
      <td>1.234570e+08</td>
      <td>1234.0</td>
      <td>65.897654</td>
    </tr>
    <tr>
      <th>6</th>
      <td>laptops</td>
      <td>company7</td>
      <td>4.532000e+03</td>
      <td>65432.0</td>
      <td>62.098765</td>
    </tr>
    <tr>
      <th>7</th>
      <td>books</td>
      <td>company8</td>
      <td>9.876540e+05</td>
      <td>34543.0</td>
      <td>60.534289</td>
    </tr>
    <tr>
      <th>8</th>
      <td>roommates</td>
      <td>company9</td>
      <td>2.245679e+09</td>
      <td>4567.0</td>
      <td>50.625438</td>
    </tr>
    <tr>
      <th>9</th>
      <td>colleges</td>
      <td>company10</td>
      <td>NaN</td>
      <td>9876.0</td>
      <td>49.324567</td>
    </tr>
    <tr>
      <th>10</th>
      <td>chef</td>
      <td>startup11</td>
      <td>7.865409e+06</td>
      <td>56437.0</td>
      <td>48.765431</td>
    </tr>
    <tr>
      <th>11</th>
      <td>architect</td>
      <td>startup12</td>
      <td>3.453210e+05</td>
      <td>NaN</td>
      <td>45.876101</td>
    </tr>
    <tr>
      <th>12</th>
      <td>police officer</td>
      <td>startup13</td>
      <td>5.643457e+07</td>
      <td>34567.0</td>
      <td>44.765413</td>
    </tr>
    <tr>
      <th>13</th>
      <td>actor</td>
      <td>startup14</td>
      <td>2.345654e+07</td>
      <td>897654.0</td>
      <td>43.651433</td>
    </tr>
    <tr>
      <th>14</th>
      <td>electrician</td>
      <td>org15</td>
      <td>NaN</td>
      <td>6754.0</td>
      <td>40.765190</td>
    </tr>
    <tr>
      <th>15</th>
      <td>firefighter</td>
      <td>org16</td>
      <td>6.543210e+05</td>
      <td>56432.0</td>
      <td>40.690165</td>
    </tr>
    <tr>
      <th>16</th>
      <td>waitress</td>
      <td>org17</td>
      <td>6.547890e+06</td>
      <td>67543.0</td>
      <td>40.509818</td>
    </tr>
  </tbody>
</table>
</div>




```python
csv_13.dropna(inplace=True)

csv_13
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
      <th>Symbol</th>
      <th>Security</th>
      <th>Today - Volume</th>
      <th>AVG -volume</th>
      <th>change</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>classes</td>
      <td>entrepreise 1.llc</td>
      <td>7.654450e+05</td>
      <td>43216.0</td>
      <td>90.097650</td>
    </tr>
    <tr>
      <th>2</th>
      <td>doctors</td>
      <td>entreprise 3</td>
      <td>4.563200e+04</td>
      <td>7689543.0</td>
      <td>70.562780</td>
    </tr>
    <tr>
      <th>3</th>
      <td>kids</td>
      <td>company4</td>
      <td>8.769432e+06</td>
      <td>675432.0</td>
      <td>69.724536</td>
    </tr>
    <tr>
      <th>4</th>
      <td>gadgets</td>
      <td>company5</td>
      <td>1.234570e+08</td>
      <td>1234.0</td>
      <td>65.897654</td>
    </tr>
    <tr>
      <th>6</th>
      <td>laptops</td>
      <td>company7</td>
      <td>4.532000e+03</td>
      <td>65432.0</td>
      <td>62.098765</td>
    </tr>
    <tr>
      <th>7</th>
      <td>books</td>
      <td>company8</td>
      <td>9.876540e+05</td>
      <td>34543.0</td>
      <td>60.534289</td>
    </tr>
    <tr>
      <th>8</th>
      <td>roommates</td>
      <td>company9</td>
      <td>2.245679e+09</td>
      <td>4567.0</td>
      <td>50.625438</td>
    </tr>
    <tr>
      <th>10</th>
      <td>chef</td>
      <td>startup11</td>
      <td>7.865409e+06</td>
      <td>56437.0</td>
      <td>48.765431</td>
    </tr>
    <tr>
      <th>12</th>
      <td>police officer</td>
      <td>startup13</td>
      <td>5.643457e+07</td>
      <td>34567.0</td>
      <td>44.765413</td>
    </tr>
    <tr>
      <th>13</th>
      <td>actor</td>
      <td>startup14</td>
      <td>2.345654e+07</td>
      <td>897654.0</td>
      <td>43.651433</td>
    </tr>
    <tr>
      <th>15</th>
      <td>firefighter</td>
      <td>org16</td>
      <td>6.543210e+05</td>
      <td>56432.0</td>
      <td>40.690165</td>
    </tr>
    <tr>
      <th>16</th>
      <td>waitress</td>
      <td>org17</td>
      <td>6.547890e+06</td>
      <td>67543.0</td>
      <td>40.509818</td>
    </tr>
  </tbody>
</table>
</div>




```python
csv_13.dropna(thresh = 1)
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
      <th>Symbol</th>
      <th>Security</th>
      <th>Today - Volume</th>
      <th>AVG -volume</th>
      <th>change</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>classes</td>
      <td>entrepreise 1.llc</td>
      <td>7.654450e+05</td>
      <td>43216.0</td>
      <td>90.097650</td>
    </tr>
    <tr>
      <th>2</th>
      <td>doctors</td>
      <td>entreprise 3</td>
      <td>4.563200e+04</td>
      <td>7689543.0</td>
      <td>70.562780</td>
    </tr>
    <tr>
      <th>3</th>
      <td>kids</td>
      <td>company4</td>
      <td>8.769432e+06</td>
      <td>675432.0</td>
      <td>69.724536</td>
    </tr>
    <tr>
      <th>4</th>
      <td>gadgets</td>
      <td>company5</td>
      <td>1.234570e+08</td>
      <td>1234.0</td>
      <td>65.897654</td>
    </tr>
    <tr>
      <th>6</th>
      <td>laptops</td>
      <td>company7</td>
      <td>4.532000e+03</td>
      <td>65432.0</td>
      <td>62.098765</td>
    </tr>
    <tr>
      <th>7</th>
      <td>books</td>
      <td>company8</td>
      <td>9.876540e+05</td>
      <td>34543.0</td>
      <td>60.534289</td>
    </tr>
    <tr>
      <th>8</th>
      <td>roommates</td>
      <td>company9</td>
      <td>2.245679e+09</td>
      <td>4567.0</td>
      <td>50.625438</td>
    </tr>
    <tr>
      <th>10</th>
      <td>chef</td>
      <td>startup11</td>
      <td>7.865409e+06</td>
      <td>56437.0</td>
      <td>48.765431</td>
    </tr>
    <tr>
      <th>12</th>
      <td>police officer</td>
      <td>startup13</td>
      <td>5.643457e+07</td>
      <td>34567.0</td>
      <td>44.765413</td>
    </tr>
    <tr>
      <th>13</th>
      <td>actor</td>
      <td>startup14</td>
      <td>2.345654e+07</td>
      <td>897654.0</td>
      <td>43.651433</td>
    </tr>
    <tr>
      <th>15</th>
      <td>firefighter</td>
      <td>org16</td>
      <td>6.543210e+05</td>
      <td>56432.0</td>
      <td>40.690165</td>
    </tr>
    <tr>
      <th>16</th>
      <td>waitress</td>
      <td>org17</td>
      <td>6.547890e+06</td>
      <td>67543.0</td>
      <td>40.509818</td>
    </tr>
  </tbody>
</table>
</div>




```python
# #Handling Missing Values

import pandas as pd

csv_14 = pd.read_excel(r"C:\Users\ASUS\\pandas\test.xlsx")

csv_14
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
      <th>Symbol</th>
      <th>Security</th>
      <th>Today - Volume</th>
      <th>AVG -volume</th>
      <th>change</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>classes</td>
      <td>entrepreise 1.llc</td>
      <td>7.654450e+05</td>
      <td>43216.0</td>
      <td>90.097650</td>
    </tr>
    <tr>
      <th>1</th>
      <td>teachers</td>
      <td>entreprise 2.inc</td>
      <td>NaN</td>
      <td>980007.0</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>2</th>
      <td>doctors</td>
      <td>entreprise 3</td>
      <td>4.563200e+04</td>
      <td>7689543.0</td>
      <td>70.562780</td>
    </tr>
    <tr>
      <th>3</th>
      <td>kids</td>
      <td>company4</td>
      <td>8.769432e+06</td>
      <td>675432.0</td>
      <td>69.724536</td>
    </tr>
    <tr>
      <th>4</th>
      <td>gadgets</td>
      <td>company5</td>
      <td>1.234570e+08</td>
      <td>1234.0</td>
      <td>65.897654</td>
    </tr>
    <tr>
      <th>5</th>
      <td>offices</td>
      <td>company6</td>
      <td>5.643800e+04</td>
      <td>9870.0</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>6</th>
      <td>laptops</td>
      <td>company7</td>
      <td>4.532000e+03</td>
      <td>65432.0</td>
      <td>62.098765</td>
    </tr>
    <tr>
      <th>7</th>
      <td>books</td>
      <td>company8</td>
      <td>9.876540e+05</td>
      <td>34543.0</td>
      <td>60.534289</td>
    </tr>
    <tr>
      <th>8</th>
      <td>roommates</td>
      <td>company9</td>
      <td>2.245679e+09</td>
      <td>4567.0</td>
      <td>50.625438</td>
    </tr>
    <tr>
      <th>9</th>
      <td>colleges</td>
      <td>company10</td>
      <td>NaN</td>
      <td>9876.0</td>
      <td>49.324567</td>
    </tr>
    <tr>
      <th>10</th>
      <td>chef</td>
      <td>startup11</td>
      <td>7.865409e+06</td>
      <td>56437.0</td>
      <td>48.765431</td>
    </tr>
    <tr>
      <th>11</th>
      <td>architect</td>
      <td>startup12</td>
      <td>3.453210e+05</td>
      <td>NaN</td>
      <td>45.876101</td>
    </tr>
    <tr>
      <th>12</th>
      <td>police officer</td>
      <td>startup13</td>
      <td>5.643457e+07</td>
      <td>34567.0</td>
      <td>44.765413</td>
    </tr>
    <tr>
      <th>13</th>
      <td>actor</td>
      <td>startup14</td>
      <td>2.345654e+07</td>
      <td>897654.0</td>
      <td>43.651433</td>
    </tr>
    <tr>
      <th>14</th>
      <td>electrician</td>
      <td>org15</td>
      <td>NaN</td>
      <td>6754.0</td>
      <td>40.765190</td>
    </tr>
    <tr>
      <th>15</th>
      <td>firefighter</td>
      <td>org16</td>
      <td>6.543210e+05</td>
      <td>56432.0</td>
      <td>40.690165</td>
    </tr>
    <tr>
      <th>16</th>
      <td>waitress</td>
      <td>org17</td>
      <td>6.547890e+06</td>
      <td>67543.0</td>
      <td>40.509818</td>
    </tr>
  </tbody>
</table>
</div>




```python
csv_14.fillna("python")
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
      <th>Symbol</th>
      <th>Security</th>
      <th>Today - Volume</th>
      <th>AVG -volume</th>
      <th>change</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>classes</td>
      <td>entrepreise 1.llc</td>
      <td>765445.0</td>
      <td>43216.0</td>
      <td>90.09765</td>
    </tr>
    <tr>
      <th>1</th>
      <td>teachers</td>
      <td>entreprise 2.inc</td>
      <td>python</td>
      <td>980007.0</td>
      <td>python</td>
    </tr>
    <tr>
      <th>2</th>
      <td>doctors</td>
      <td>entreprise 3</td>
      <td>45632.0</td>
      <td>7689543.0</td>
      <td>70.56278</td>
    </tr>
    <tr>
      <th>3</th>
      <td>kids</td>
      <td>company4</td>
      <td>8769432.0</td>
      <td>675432.0</td>
      <td>69.724536</td>
    </tr>
    <tr>
      <th>4</th>
      <td>gadgets</td>
      <td>company5</td>
      <td>123456987.0</td>
      <td>1234.0</td>
      <td>65.897654</td>
    </tr>
    <tr>
      <th>5</th>
      <td>offices</td>
      <td>company6</td>
      <td>56438.0</td>
      <td>9870.0</td>
      <td>python</td>
    </tr>
    <tr>
      <th>6</th>
      <td>laptops</td>
      <td>company7</td>
      <td>4532.0</td>
      <td>65432.0</td>
      <td>62.098765</td>
    </tr>
    <tr>
      <th>7</th>
      <td>books</td>
      <td>company8</td>
      <td>987654.0</td>
      <td>34543.0</td>
      <td>60.534289</td>
    </tr>
    <tr>
      <th>8</th>
      <td>roommates</td>
      <td>company9</td>
      <td>2245678987.0</td>
      <td>4567.0</td>
      <td>50.625438</td>
    </tr>
    <tr>
      <th>9</th>
      <td>colleges</td>
      <td>company10</td>
      <td>python</td>
      <td>9876.0</td>
      <td>49.324567</td>
    </tr>
    <tr>
      <th>10</th>
      <td>chef</td>
      <td>startup11</td>
      <td>7865409.0</td>
      <td>56437.0</td>
      <td>48.765431</td>
    </tr>
    <tr>
      <th>11</th>
      <td>architect</td>
      <td>startup12</td>
      <td>345321.0</td>
      <td>python</td>
      <td>45.876101</td>
    </tr>
    <tr>
      <th>12</th>
      <td>police officer</td>
      <td>startup13</td>
      <td>56434567.0</td>
      <td>34567.0</td>
      <td>44.765413</td>
    </tr>
    <tr>
      <th>13</th>
      <td>actor</td>
      <td>startup14</td>
      <td>23456543.0</td>
      <td>897654.0</td>
      <td>43.651433</td>
    </tr>
    <tr>
      <th>14</th>
      <td>electrician</td>
      <td>org15</td>
      <td>python</td>
      <td>6754.0</td>
      <td>40.76519</td>
    </tr>
    <tr>
      <th>15</th>
      <td>firefighter</td>
      <td>org16</td>
      <td>654321.0</td>
      <td>56432.0</td>
      <td>40.690165</td>
    </tr>
    <tr>
      <th>16</th>
      <td>waitress</td>
      <td>org17</td>
      <td>6547890.0</td>
      <td>67543.0</td>
      <td>40.509818</td>
    </tr>
  </tbody>
</table>
</div>




```python
csv_14.fillna({"Today - Volume":"javascript","AVG -volume":"python","change":"c"})
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
      <th>Symbol</th>
      <th>Security</th>
      <th>Today - Volume</th>
      <th>AVG -volume</th>
      <th>change</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>classes</td>
      <td>entrepreise 1.llc</td>
      <td>765445.0</td>
      <td>43216.0</td>
      <td>90.09765</td>
    </tr>
    <tr>
      <th>1</th>
      <td>teachers</td>
      <td>entreprise 2.inc</td>
      <td>javascript</td>
      <td>980007.0</td>
      <td>c</td>
    </tr>
    <tr>
      <th>2</th>
      <td>doctors</td>
      <td>entreprise 3</td>
      <td>45632.0</td>
      <td>7689543.0</td>
      <td>70.56278</td>
    </tr>
    <tr>
      <th>3</th>
      <td>kids</td>
      <td>company4</td>
      <td>8769432.0</td>
      <td>675432.0</td>
      <td>69.724536</td>
    </tr>
    <tr>
      <th>4</th>
      <td>gadgets</td>
      <td>company5</td>
      <td>123456987.0</td>
      <td>1234.0</td>
      <td>65.897654</td>
    </tr>
    <tr>
      <th>5</th>
      <td>offices</td>
      <td>company6</td>
      <td>56438.0</td>
      <td>9870.0</td>
      <td>c</td>
    </tr>
    <tr>
      <th>6</th>
      <td>laptops</td>
      <td>company7</td>
      <td>4532.0</td>
      <td>65432.0</td>
      <td>62.098765</td>
    </tr>
    <tr>
      <th>7</th>
      <td>books</td>
      <td>company8</td>
      <td>987654.0</td>
      <td>34543.0</td>
      <td>60.534289</td>
    </tr>
    <tr>
      <th>8</th>
      <td>roommates</td>
      <td>company9</td>
      <td>2245678987.0</td>
      <td>4567.0</td>
      <td>50.625438</td>
    </tr>
    <tr>
      <th>9</th>
      <td>colleges</td>
      <td>company10</td>
      <td>javascript</td>
      <td>9876.0</td>
      <td>49.324567</td>
    </tr>
    <tr>
      <th>10</th>
      <td>chef</td>
      <td>startup11</td>
      <td>7865409.0</td>
      <td>56437.0</td>
      <td>48.765431</td>
    </tr>
    <tr>
      <th>11</th>
      <td>architect</td>
      <td>startup12</td>
      <td>345321.0</td>
      <td>python</td>
      <td>45.876101</td>
    </tr>
    <tr>
      <th>12</th>
      <td>police officer</td>
      <td>startup13</td>
      <td>56434567.0</td>
      <td>34567.0</td>
      <td>44.765413</td>
    </tr>
    <tr>
      <th>13</th>
      <td>actor</td>
      <td>startup14</td>
      <td>23456543.0</td>
      <td>897654.0</td>
      <td>43.651433</td>
    </tr>
    <tr>
      <th>14</th>
      <td>electrician</td>
      <td>org15</td>
      <td>javascript</td>
      <td>6754.0</td>
      <td>40.76519</td>
    </tr>
    <tr>
      <th>15</th>
      <td>firefighter</td>
      <td>org16</td>
      <td>654321.0</td>
      <td>56432.0</td>
      <td>40.690165</td>
    </tr>
    <tr>
      <th>16</th>
      <td>waitress</td>
      <td>org17</td>
      <td>6547890.0</td>
      <td>67543.0</td>
      <td>40.509818</td>
    </tr>
  </tbody>
</table>
</div>




```python
csv_14.ffill()
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
      <th>Symbol</th>
      <th>Security</th>
      <th>Today - Volume</th>
      <th>AVG -volume</th>
      <th>change</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>classes</td>
      <td>entrepreise 1.llc</td>
      <td>7.654450e+05</td>
      <td>43216.0</td>
      <td>90.097650</td>
    </tr>
    <tr>
      <th>1</th>
      <td>teachers</td>
      <td>entreprise 2.inc</td>
      <td>7.654450e+05</td>
      <td>980007.0</td>
      <td>90.097650</td>
    </tr>
    <tr>
      <th>2</th>
      <td>doctors</td>
      <td>entreprise 3</td>
      <td>4.563200e+04</td>
      <td>7689543.0</td>
      <td>70.562780</td>
    </tr>
    <tr>
      <th>3</th>
      <td>kids</td>
      <td>company4</td>
      <td>8.769432e+06</td>
      <td>675432.0</td>
      <td>69.724536</td>
    </tr>
    <tr>
      <th>4</th>
      <td>gadgets</td>
      <td>company5</td>
      <td>1.234570e+08</td>
      <td>1234.0</td>
      <td>65.897654</td>
    </tr>
    <tr>
      <th>5</th>
      <td>offices</td>
      <td>company6</td>
      <td>5.643800e+04</td>
      <td>9870.0</td>
      <td>65.897654</td>
    </tr>
    <tr>
      <th>6</th>
      <td>laptops</td>
      <td>company7</td>
      <td>4.532000e+03</td>
      <td>65432.0</td>
      <td>62.098765</td>
    </tr>
    <tr>
      <th>7</th>
      <td>books</td>
      <td>company8</td>
      <td>9.876540e+05</td>
      <td>34543.0</td>
      <td>60.534289</td>
    </tr>
    <tr>
      <th>8</th>
      <td>roommates</td>
      <td>company9</td>
      <td>2.245679e+09</td>
      <td>4567.0</td>
      <td>50.625438</td>
    </tr>
    <tr>
      <th>9</th>
      <td>colleges</td>
      <td>company10</td>
      <td>2.245679e+09</td>
      <td>9876.0</td>
      <td>49.324567</td>
    </tr>
    <tr>
      <th>10</th>
      <td>chef</td>
      <td>startup11</td>
      <td>7.865409e+06</td>
      <td>56437.0</td>
      <td>48.765431</td>
    </tr>
    <tr>
      <th>11</th>
      <td>architect</td>
      <td>startup12</td>
      <td>3.453210e+05</td>
      <td>56437.0</td>
      <td>45.876101</td>
    </tr>
    <tr>
      <th>12</th>
      <td>police officer</td>
      <td>startup13</td>
      <td>5.643457e+07</td>
      <td>34567.0</td>
      <td>44.765413</td>
    </tr>
    <tr>
      <th>13</th>
      <td>actor</td>
      <td>startup14</td>
      <td>2.345654e+07</td>
      <td>897654.0</td>
      <td>43.651433</td>
    </tr>
    <tr>
      <th>14</th>
      <td>electrician</td>
      <td>org15</td>
      <td>2.345654e+07</td>
      <td>6754.0</td>
      <td>40.765190</td>
    </tr>
    <tr>
      <th>15</th>
      <td>firefighter</td>
      <td>org16</td>
      <td>6.543210e+05</td>
      <td>56432.0</td>
      <td>40.690165</td>
    </tr>
    <tr>
      <th>16</th>
      <td>waitress</td>
      <td>org17</td>
      <td>6.547890e+06</td>
      <td>67543.0</td>
      <td>40.509818</td>
    </tr>
  </tbody>
</table>
</div>




```python
csv_14.fillna(12,inplace=True)
csv_14
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
      <th>Symbol</th>
      <th>Security</th>
      <th>Today - Volume</th>
      <th>AVG -volume</th>
      <th>change</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>classes</td>
      <td>entrepreise 1.llc</td>
      <td>7.654450e+05</td>
      <td>43216.0</td>
      <td>90.097650</td>
    </tr>
    <tr>
      <th>1</th>
      <td>teachers</td>
      <td>entreprise 2.inc</td>
      <td>1.200000e+01</td>
      <td>980007.0</td>
      <td>12.000000</td>
    </tr>
    <tr>
      <th>2</th>
      <td>doctors</td>
      <td>entreprise 3</td>
      <td>4.563200e+04</td>
      <td>7689543.0</td>
      <td>70.562780</td>
    </tr>
    <tr>
      <th>3</th>
      <td>kids</td>
      <td>company4</td>
      <td>8.769432e+06</td>
      <td>675432.0</td>
      <td>69.724536</td>
    </tr>
    <tr>
      <th>4</th>
      <td>gadgets</td>
      <td>company5</td>
      <td>1.234570e+08</td>
      <td>1234.0</td>
      <td>65.897654</td>
    </tr>
    <tr>
      <th>5</th>
      <td>offices</td>
      <td>company6</td>
      <td>5.643800e+04</td>
      <td>9870.0</td>
      <td>12.000000</td>
    </tr>
    <tr>
      <th>6</th>
      <td>laptops</td>
      <td>company7</td>
      <td>4.532000e+03</td>
      <td>65432.0</td>
      <td>62.098765</td>
    </tr>
    <tr>
      <th>7</th>
      <td>books</td>
      <td>company8</td>
      <td>9.876540e+05</td>
      <td>34543.0</td>
      <td>60.534289</td>
    </tr>
    <tr>
      <th>8</th>
      <td>roommates</td>
      <td>company9</td>
      <td>2.245679e+09</td>
      <td>4567.0</td>
      <td>50.625438</td>
    </tr>
    <tr>
      <th>9</th>
      <td>colleges</td>
      <td>company10</td>
      <td>1.200000e+01</td>
      <td>9876.0</td>
      <td>49.324567</td>
    </tr>
    <tr>
      <th>10</th>
      <td>chef</td>
      <td>startup11</td>
      <td>7.865409e+06</td>
      <td>56437.0</td>
      <td>48.765431</td>
    </tr>
    <tr>
      <th>11</th>
      <td>architect</td>
      <td>startup12</td>
      <td>3.453210e+05</td>
      <td>12.0</td>
      <td>45.876101</td>
    </tr>
    <tr>
      <th>12</th>
      <td>police officer</td>
      <td>startup13</td>
      <td>5.643457e+07</td>
      <td>34567.0</td>
      <td>44.765413</td>
    </tr>
    <tr>
      <th>13</th>
      <td>actor</td>
      <td>startup14</td>
      <td>2.345654e+07</td>
      <td>897654.0</td>
      <td>43.651433</td>
    </tr>
    <tr>
      <th>14</th>
      <td>electrician</td>
      <td>org15</td>
      <td>1.200000e+01</td>
      <td>6754.0</td>
      <td>40.765190</td>
    </tr>
    <tr>
      <th>15</th>
      <td>firefighter</td>
      <td>org16</td>
      <td>6.543210e+05</td>
      <td>56432.0</td>
      <td>40.690165</td>
    </tr>
    <tr>
      <th>16</th>
      <td>waitress</td>
      <td>org17</td>
      <td>6.547890e+06</td>
      <td>67543.0</td>
      <td>40.509818</td>
    </tr>
  </tbody>
</table>
</div>




```python
#Replace

import pandas as pd

csv_15 = pd.read_excel(r"C:\Users\ASUS\\pandas\test.xlsx")

csv_15
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
      <th>Symbol</th>
      <th>Security</th>
      <th>Today - Volume</th>
      <th>AVG -volume</th>
      <th>change</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>classes</td>
      <td>entrepreise 1.llc</td>
      <td>765445.0</td>
      <td>43216.0</td>
      <td>90.097650</td>
    </tr>
    <tr>
      <th>1</th>
      <td>teachers</td>
      <td>entreprise 2.inc</td>
      <td>NaN</td>
      <td>980007.0</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>2</th>
      <td>doctors</td>
      <td>entreprise 3</td>
      <td>45632.0</td>
      <td>7689543.0</td>
      <td>70.562780</td>
    </tr>
    <tr>
      <th>3</th>
      <td>kids</td>
      <td>company4</td>
      <td>8769432.0</td>
      <td>675432.0</td>
      <td>69.724536</td>
    </tr>
    <tr>
      <th>4</th>
      <td>gadgets</td>
      <td>company5</td>
      <td>123456987.0</td>
      <td>1234.0</td>
      <td>65.897654</td>
    </tr>
    <tr>
      <th>5</th>
      <td>offices</td>
      <td>company6</td>
      <td>56438.0</td>
      <td>9870.0</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>6</th>
      <td>laptops</td>
      <td>company7</td>
      <td>1.0</td>
      <td>65432.0</td>
      <td>62.098765</td>
    </tr>
    <tr>
      <th>7</th>
      <td>books</td>
      <td>company8</td>
      <td>1.0</td>
      <td>34543.0</td>
      <td>60.534289</td>
    </tr>
    <tr>
      <th>8</th>
      <td>roommates</td>
      <td>company9</td>
      <td>1.0</td>
      <td>4567.0</td>
      <td>50.625438</td>
    </tr>
    <tr>
      <th>9</th>
      <td>colleges</td>
      <td>company10</td>
      <td>1.0</td>
      <td>9876.0</td>
      <td>49.324567</td>
    </tr>
    <tr>
      <th>10</th>
      <td>chef</td>
      <td>startup11</td>
      <td>1.0</td>
      <td>56437.0</td>
      <td>48.765431</td>
    </tr>
    <tr>
      <th>11</th>
      <td>architect</td>
      <td>startup12</td>
      <td>1.0</td>
      <td>NaN</td>
      <td>45.876101</td>
    </tr>
    <tr>
      <th>12</th>
      <td>police officer</td>
      <td>startup13</td>
      <td>1.0</td>
      <td>34567.0</td>
      <td>44.765413</td>
    </tr>
    <tr>
      <th>13</th>
      <td>actor</td>
      <td>startup14</td>
      <td>1.0</td>
      <td>897654.0</td>
      <td>43.651433</td>
    </tr>
    <tr>
      <th>14</th>
      <td>electrician</td>
      <td>org15</td>
      <td>1.0</td>
      <td>6754.0</td>
      <td>40.765190</td>
    </tr>
    <tr>
      <th>15</th>
      <td>firefighter</td>
      <td>org16</td>
      <td>654321.0</td>
      <td>56432.0</td>
      <td>40.690165</td>
    </tr>
    <tr>
      <th>16</th>
      <td>waitress</td>
      <td>org17</td>
      <td>6547890.0</td>
      <td>67543.0</td>
      <td>40.509818</td>
    </tr>
  </tbody>
</table>
</div>




```python
csv_15.replace(to_replace=1,value=22)
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
      <th>Symbol</th>
      <th>Security</th>
      <th>Today - Volume</th>
      <th>AVG -volume</th>
      <th>change</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>classes</td>
      <td>entrepreise 1.llc</td>
      <td>765445.0</td>
      <td>43216.0</td>
      <td>90.097650</td>
    </tr>
    <tr>
      <th>1</th>
      <td>teachers</td>
      <td>entreprise 2.inc</td>
      <td>NaN</td>
      <td>980007.0</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>2</th>
      <td>doctors</td>
      <td>entreprise 3</td>
      <td>45632.0</td>
      <td>7689543.0</td>
      <td>70.562780</td>
    </tr>
    <tr>
      <th>3</th>
      <td>kids</td>
      <td>company4</td>
      <td>8769432.0</td>
      <td>675432.0</td>
      <td>69.724536</td>
    </tr>
    <tr>
      <th>4</th>
      <td>gadgets</td>
      <td>company5</td>
      <td>123456987.0</td>
      <td>1234.0</td>
      <td>65.897654</td>
    </tr>
    <tr>
      <th>5</th>
      <td>offices</td>
      <td>company6</td>
      <td>56438.0</td>
      <td>9870.0</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>6</th>
      <td>laptops</td>
      <td>company7</td>
      <td>22.0</td>
      <td>65432.0</td>
      <td>62.098765</td>
    </tr>
    <tr>
      <th>7</th>
      <td>books</td>
      <td>company8</td>
      <td>22.0</td>
      <td>34543.0</td>
      <td>60.534289</td>
    </tr>
    <tr>
      <th>8</th>
      <td>roommates</td>
      <td>company9</td>
      <td>22.0</td>
      <td>4567.0</td>
      <td>50.625438</td>
    </tr>
    <tr>
      <th>9</th>
      <td>colleges</td>
      <td>company10</td>
      <td>22.0</td>
      <td>9876.0</td>
      <td>49.324567</td>
    </tr>
    <tr>
      <th>10</th>
      <td>chef</td>
      <td>startup11</td>
      <td>22.0</td>
      <td>56437.0</td>
      <td>48.765431</td>
    </tr>
    <tr>
      <th>11</th>
      <td>architect</td>
      <td>startup12</td>
      <td>22.0</td>
      <td>NaN</td>
      <td>45.876101</td>
    </tr>
    <tr>
      <th>12</th>
      <td>police officer</td>
      <td>startup13</td>
      <td>22.0</td>
      <td>34567.0</td>
      <td>44.765413</td>
    </tr>
    <tr>
      <th>13</th>
      <td>actor</td>
      <td>startup14</td>
      <td>22.0</td>
      <td>897654.0</td>
      <td>43.651433</td>
    </tr>
    <tr>
      <th>14</th>
      <td>electrician</td>
      <td>org15</td>
      <td>22.0</td>
      <td>6754.0</td>
      <td>40.765190</td>
    </tr>
    <tr>
      <th>15</th>
      <td>firefighter</td>
      <td>org16</td>
      <td>654321.0</td>
      <td>56432.0</td>
      <td>40.690165</td>
    </tr>
    <tr>
      <th>16</th>
      <td>waitress</td>
      <td>org17</td>
      <td>6547890.0</td>
      <td>67543.0</td>
      <td>40.509818</td>
    </tr>
  </tbody>
</table>
</div>




```python
csv_15.replace(to_replace="company4", value="python")
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
      <th>Symbol</th>
      <th>Security</th>
      <th>Today - Volume</th>
      <th>AVG -volume</th>
      <th>change</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>classes</td>
      <td>entrepreise 1.llc</td>
      <td>765445.0</td>
      <td>43216.0</td>
      <td>90.097650</td>
    </tr>
    <tr>
      <th>1</th>
      <td>teachers</td>
      <td>entreprise 2.inc</td>
      <td>NaN</td>
      <td>980007.0</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>2</th>
      <td>doctors</td>
      <td>entreprise 3</td>
      <td>45632.0</td>
      <td>7689543.0</td>
      <td>70.562780</td>
    </tr>
    <tr>
      <th>3</th>
      <td>kids</td>
      <td>python</td>
      <td>8769432.0</td>
      <td>675432.0</td>
      <td>69.724536</td>
    </tr>
    <tr>
      <th>4</th>
      <td>gadgets</td>
      <td>company5</td>
      <td>123456987.0</td>
      <td>1234.0</td>
      <td>65.897654</td>
    </tr>
    <tr>
      <th>5</th>
      <td>offices</td>
      <td>company6</td>
      <td>56438.0</td>
      <td>9870.0</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>6</th>
      <td>laptops</td>
      <td>company7</td>
      <td>1.0</td>
      <td>65432.0</td>
      <td>62.098765</td>
    </tr>
    <tr>
      <th>7</th>
      <td>books</td>
      <td>company8</td>
      <td>1.0</td>
      <td>34543.0</td>
      <td>60.534289</td>
    </tr>
    <tr>
      <th>8</th>
      <td>roommates</td>
      <td>company9</td>
      <td>1.0</td>
      <td>4567.0</td>
      <td>50.625438</td>
    </tr>
    <tr>
      <th>9</th>
      <td>colleges</td>
      <td>company10</td>
      <td>1.0</td>
      <td>9876.0</td>
      <td>49.324567</td>
    </tr>
    <tr>
      <th>10</th>
      <td>chef</td>
      <td>startup11</td>
      <td>1.0</td>
      <td>56437.0</td>
      <td>48.765431</td>
    </tr>
    <tr>
      <th>11</th>
      <td>architect</td>
      <td>startup12</td>
      <td>1.0</td>
      <td>NaN</td>
      <td>45.876101</td>
    </tr>
    <tr>
      <th>12</th>
      <td>police officer</td>
      <td>startup13</td>
      <td>1.0</td>
      <td>34567.0</td>
      <td>44.765413</td>
    </tr>
    <tr>
      <th>13</th>
      <td>actor</td>
      <td>startup14</td>
      <td>1.0</td>
      <td>897654.0</td>
      <td>43.651433</td>
    </tr>
    <tr>
      <th>14</th>
      <td>electrician</td>
      <td>org15</td>
      <td>1.0</td>
      <td>6754.0</td>
      <td>40.765190</td>
    </tr>
    <tr>
      <th>15</th>
      <td>firefighter</td>
      <td>org16</td>
      <td>654321.0</td>
      <td>56432.0</td>
      <td>40.690165</td>
    </tr>
    <tr>
      <th>16</th>
      <td>waitress</td>
      <td>org17</td>
      <td>6547890.0</td>
      <td>67543.0</td>
      <td>40.509818</td>
    </tr>
  </tbody>
</table>
</div>




```python

```


```python

```
