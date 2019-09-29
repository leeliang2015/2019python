from sklearn.pipeline import Pipeline
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import GridSearchCV
from sklearn.preprocessing import Imputer
from sklearn.impute import SimpleImputer

# 调参候选
knn_params = {'classify__n_neighbors':[1,2,3,4,5,6]}

# 实例化KNN模型
knn = KNeighborsClassifier()

# 管道设计
mean_impute = Pipeline([('imputer', SimpleImputer (strategy='mean')),
                        ('classify',knn)
                       ])

x = pima.drop('onset_disbetes', axis=1) # 丢弃y
y = pima['onset_disbetes']
