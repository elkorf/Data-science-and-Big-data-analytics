import matplotlib.pyplot as plt
import pandas as pd

df = pd.read_csv("/home/hduser/33356/5/dataset.csv")

plt.bar(df["roll"],df["mark"])
plt.show()





