import pandas as pd

# Create a DataFrame
data = {
    'Name': ['Alice', 'Bob', 'Charlie', 'David'],
    'Age': [25, 32, 18, 41],
    'City': ['New York', 'Los Angeles', 'Chicago', 'Houston']
}
df = pd.DataFrame(data)

# Data manipulation
df['Age Group'] = pd.cut(df['Age'], bins=[0, 18, 35, 60], labels=['Youth', 'Adult', 'Senior'])
df['Age in Months'] = df['Age'] * 12

# Data visualization
import matplotlib.pyplot as plt

df['Age'].plot(kind='bar')
plt.xlabel('Person')
plt.ylabel('Age')
plt.title('Age of Persons')
plt.show()
