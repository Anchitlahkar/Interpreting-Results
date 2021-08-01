import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv('Filtered_Data.csv')

star_name = df['Star_Name'].tolist()
distance  = df['Distance'].tolist()
mass = df['Mass'].tolist()
radius = df['Radius'].tolist()
gravity = df['Gravity'].tolist()




plt.figure()
plt.title('Graph')


# distance Graph
sns.barplot(star_name, distance, color='yellow')
plt.ylabel('distance')
plt.show()


# mass Graph
sns.barplot(star_name, mass,  color='red')
plt.ylabel('Mass')
plt.show()


# radius Graph
sns.barplot(star_name, radius,  color='green')
plt.ylabel('Radius')
plt.show()

# gravity Graph
sns.barplot(star_name, distance,  color='blue')
plt.ylabel('gravity')
plt.show() 