import numpy as np

class Perceptron(object):
	''' Perceptron classifier.

	Parameters
	----------
	eta : float
		Learning rate (between 0.0 and 1.0).
	n_inter : int
		Passes over the training dataset.

	Attibutes
	---------
	w_ : 1-d array
		Weights after fitting.
	errors_ : list
		Number of misclassifications in every epoch.

	'''

	def __init__(self, eta = 0.01, n_inter = 10):
		self.eta = eta
		self.n_inter = n_inter

	def fit(self, X, y):
		''' Fit training data.

		Parameters
		----------
		X : {array-like}, shape = [n_samples, n_features]
			Training vectors, where n_sambles is 
			the number of samples and 
			n_features us the number of 
			features.
		y : {array-like}, shape = [n_samples]
			Target values

		Returns
		-------

		self : object

		'''
		self.w_ = np.zeros(1 + X.shape[1])
		self.errors_ = []

		for i in range(self.n_inter):
			errors = 0
			for xi, target in zip(X,y):
				update = self.eta * (target - self.predict(xi))
				self.w_[1:] += update * xi
				self.w_[0] += update
				errors += int(update != 0.0)
			self.errors_.append(errors)
		return self

	def net_input(self, X):
		''' Calculate new input '''
		return np.dot(X, self.w_[1:0]) + self.w_[0]

	def predict(self, X):
		''' Return class label after unit step '''
		return np.where(self.net_input(X) >= 0.0, 1, -1)