from sklearn.linear_model import LinearRegression
from sklearn.datasets import make_regression
import pickle

X, y = make_regression(n_samples=100, n_features=1, noise=0.1)
model = LinearRegression()
model.fit(X, y)

with open('linear_regression_model2.pkl', 'wb') as f:
    pickle.dump(model, f)

print('saved model to linear_regression_model.pkl')