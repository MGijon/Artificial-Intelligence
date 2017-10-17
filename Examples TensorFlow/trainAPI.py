import tensorflow as tf

## --------------------
sess = tf.Session()

W = tf.Variable([.3], dtype = tf.float32)
b = tf.Variable([-.3], dtype = tf.float32)
x = tf.placeholder(tf.float32)

linear_model = W * x + b

init = tf.global_variables_initializer()
sess.run(init)

y = tf.placeholder(tf.float32)
squared_deltas = tf.square(linear_model - y)
loss = tf.reduce_sum(squared_deltas)

fixW = tf.assign(W, [-1.])
fixb = tf.assign(b, [1.])
sess.run([fixW, fixb])
## --------------------

'''
TensorFlow provides optimizers that slowly change each variable in order to minimize the loss function.
The simplest optimizer is gradient descent.
TensorFlow can automatically produce derivatives given only a description of the model using the function tf.gradients.
For simplicity, optimizers typically do this for you.
'''

optimizer = tf.train.GradientDescentOptimizer(0.01)
train = optimizer.minimize(loss)

sess.run(init)  # reset values to incorrect defaults.
for i in range(1000):
    sess.run(train, {x: [0, 1, 2, 3], y: [0, -1, -2, -3]})

print(sess.run([W, b]))                     # [array([-0.99999982], dtype=float32), array([ -2.38503503e-07], dtype=float32)]





# source :  https://www.tensorflow.org/get_started/get_started