#15a) Visualize correlation matrix using heatmap from Seaborn to enhance readability of 4laptops.csv

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
df2 = pd.read_csv("C:/Users/Chandana D/Downloads/4laptops.csv")
sns.heatmap(df2.corr(numeric_only=True),annot=True)
plt.show()
