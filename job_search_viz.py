import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.read_excel("C:\\Users\\richa\\OneDrive\\Documents\\Job applications.xlsx")
print(df.head())

# create histogram
plt.figure(figsize=(10,6))
sns.histplot(data=df, x='Country', stat='count', bins='auto', kde=False)
plt.xlabel('Country')
plt.ylabel('# of Job Applications')
plt.title('# of Job Applications by Country')
plt.xticks(rotation=45)
plt.tight_layout()

plt.show()