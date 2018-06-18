import pandas as pd

# Series와 dict 데이터를 사용한 DataFrame
d = {
    'one': pd.Series([1, 2, 3], index=['a', 'b', 'c']),
    'two': pd.Series([10, 20, 30, 40], index=['a', 'b', 'c', 'd'])
}
df = pd.DataFrame(d)
print(df)

# list와 dict를 활용
data = [
    {'name': '둘리', 'age': 10, 'phone': '010-1111-1111'},
    {'name': '마이콜', 'age': 30, 'phone': '010-2222-2222'},
    {'name': '도우넛', 'age': 20, 'phone': '010-3333-3333'}
]

df = pd.DataFrame(data)
print(df)

df2 = pd.DataFrame(df, columns=['name', 'phone'])
print(df2)

# 데이터 추가 (열 추가)
df2['height'] = [150, 160, 170]
print(df2)

