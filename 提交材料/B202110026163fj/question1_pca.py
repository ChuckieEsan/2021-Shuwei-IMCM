import pandas as pd
from sklearn.decomposition import PCA
from sklearn.preprocessing import StandardScaler

data = pd.read_excel(r'.\data\data.xlsx', index_col=0)
sc = StandardScaler()
data_std = sc.fit_transform(data)
pca = PCA(n_components=4)
pca.fit_transform(data_std)