import tensorflow as tf

saludo = tf.constant('Hello World!')
sesion = tf.Session()
print(sesion.run(saludo))