import tensorflow as tf

# Model Parameters / Parámetros del modelo
W = tf.Variable([.3], dtype = tf.float32)
b = tf.Variable([-.3], dtype = tf.float32)

# Model input and output / Entradas y salidas del modelo
x = tf.placeholder(tf.float32)
linear_model = W * x + b
y = tf.placeholder(tf.float32)

# loss / Función de pérdida
loss = tf.reduce_sum(tf.square(linear_model - y)) # sum of the squares

# optimizer / Optimizador
optimizer = tf.train.GradientDescentOptimizer(0.01)
train = optimizer.minimize(loss)

# Training data / datos para el entrenamiento
x_train = [1., 2., 3., 4.]
y_train = [0., -1., -2., -3.]

# Trainig loop / bucle de entrenamiento
init = tf.global_variables_initializer()
sess = tf.Session()
sess.run(init)          # reset values to wrong / devolvemos los valores a erróeos
for i in range(1000):
    sess.run(train, {x: x_train, y: y_train})

# Evaluating training accuracy / evaluando la precisión del entrenamiento
curr_W, curr_b, curr_loss = sess.run([W, b, loss], {x: x_train, y: y_train})
print("W: %s b: %s loss: %s"%(curr_W, curr_b, curr_loss))

# Out / Salida: W: [-0.9999969] b: [ 0.99999082] loss: 5.69997e-11


# source : https://www.tensorflow.org/get_started/get_started