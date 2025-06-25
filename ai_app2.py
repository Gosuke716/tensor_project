import pickle
from sklearn.datasets import make_regression


X, y = make_regression(n_samples=100, n_features=1, noise=0.1)


with open('linear_regression_model2.pkl', 'rb') as f:
    loaded_model = pickle.load(f)

print('loaded model from linear_regression_model2.pkl')

y_pred = loaded_model.predict(X)
print(y_pred)