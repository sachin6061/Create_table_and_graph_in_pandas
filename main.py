import pandas as pd
import matplotlib.pyplot as plt
# Q 1 - 1
df = pd.read_csv('Asg1.csv')
df = pd.DataFrame(df)
# Q 1 - 2
df = df.dropna()
df = df.drop(df[(df.ID == 2)].index)
df = df.astype({'ID': int})

# Q 1 - 3
print(df.head(10))
# df.drop(['Event context', 'Component', 'Origin'], axis=1, inplace=True)
f = {'Event name': 'Event name'}
df = df.groupby(['ID', 'Event name'], as_index=False).count().rename(
    columns={"Time": "COUNT", 'Event name': 'Event_name'})
# action_frequency['Discussion created'] = action_frequency['Event name'] == 'Discussion created'
_id = df.ID.unique().tolist()
loggedin_col = []
submision_col = []
disscussion_col = []
attempt_col = []
for i in _id:
    _col = df.loc[
        (df['ID'] == i) & (df['Event_name'] == 'User has logged in')]
    lis = _col.COUNT.tolist()
    if len(lis) > 0:
        loggedin_col.append(lis[0])
    else:
        loggedin_col.append(0)

    _col = df.loc[
        (df['ID'] == i) & (df['Event_name'] == 'A submission has been submitted.')]
    lis = _col.COUNT.tolist()
    if len(lis) > 0:
        submision_col.append(lis[0])
    else:
        submision_col.append(0)

    _col = df.loc[
        (df['ID'] == i) & (df['Event_name'] == 'Discussion created')]
    lis = _col.COUNT.tolist()
    if len(lis) > 0:
        disscussion_col.append(lis[0])
    else:
        disscussion_col.append(0)

    _col = df.loc[
        (df['ID'] == i) & (df['Event_name'] == 'Quiz attempt submitted')]
    lis = _col.COUNT.tolist()
    if len(lis) > 0:
        attempt_col.append(lis[0])
    else:
        attempt_col.append(0)

# Q2
action_frequency = pd.DataFrame({
    'ID': _id,
    'Total of login': loggedin_col,
    'assignments done': submision_col,
    'discussion created': disscussion_col,
    'quizzes taken': attempt_col,
})
print(action_frequency.head())
#question 3-1
plt.bar(_id, loggedin_col)
plt.show()
