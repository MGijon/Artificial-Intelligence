import tensorflow as tf 

node1 = tf.constant(3.0, dtype = tf.float32)
node2 = tf.constant(4.0) # also tf.float 

print(node1, node2) #Tensor("Const:0", shape=(), dtype=float32) Tensor("Const_1:0", shape=(), dtype=float32)

# necesitamos ahora crear una sesión (objeto) para utilizar su método run

sess = tf.Session()
print(sess.run([node1, node2]))  # [3.0, 4.0]

# podemos construir operaciones más complicadas combinando nodos Tensor con operaciones (que también serán nodos)

node3 = tf.add(node1, node2)
print("node3: ", node3)          # node3:  Tensor("Add:0", shape=(), dtype=float32)
print("sess.run(node3): ", sess.run(node3))  # sess.run(node3):  7.0


# Tensor Flow tiene un motor gráfico para mostrar  gráficos de complejidad
# no es muy interesante porque produce siempre el mismo resultado
# un gáfico puede ser parametrozado utilizando como parámetros imputs externos conocidos como 'placeholder's'

a = tf.placeholder(tf.float32)
b = tf.placeholder(tf.float32)
adder_node = a + b                # + provides a shortcut for tf.add(a, b)


print(sess.run(adder_node, {a: 3, b: 4.5}))             # 7.5
print(sess.run(adder_node, {a: [1, 3], b: [2, 4]}))     # [ 3.  7.]

# podemos hacerlo más complicado añadiendo una opepración más

add_and_triple = adder_node * 3
print(sess.run(add_and_triple, {a: 3, b: 4.5}))         # 22.5


'''
In machine learning we will typically want a model that can take arbitrary inputs, such as the one above. 
To make the model trainable, we need to be able to modify the graph to get new outputs with the same input.
Variables allow us to add trainable parameters to a graph. They are constructed with a type and initial value:
'''

W = tf.Variable([.3], dtype = tf.float32)
b = tf.Variable([-.3], dtype = tf.float32)
x = tf.placeholder(tf.float32)

linear_model = W * x + b

'''
Constants are initialized when you call tf.constant, and their value can never change.
By contrast, variables are not initialized when you call tf.Variable. To initialize all 
the variables in a TensorFlow program, you must explicitly call a special operation as follows:
'''

init = tf.global_variables_initializer()
sess.run(init)

'''
It is important to realize init is a handle to the TensorFlow sub-graph that initializes 
all the global variables. Until we call sess.run, the variables are uninitialized.
'''

# como x es un placeholder, podemos evaluar el modelo lineal para varios valores de x de manera
# simultánea de la siguiente manera

print(sess.run(linear_model, {x: [1, 2, 3, 4]}))        # [ 0.          0.30000001  0.60000002  0.90000004]

'''
Para evaluar cómo de bueno es el modelo crearemos un placeholder 'y' para almacenar los valores deseados y 
escribiremos una función de coste.
'''

y = tf.placeholder(tf.float32)
squared_deltas = tf.square(linear_model - y)
loss = tf.reduce_sum(squared_deltas)
print(sess.run(loss, {x: [1, 2, 3, 4], y: [0, -1, -2, -3]}))        # 23.66

'''
We could improve this manually by reassigning the values of W and b to the perfect values of -1 and 1.
A variable is initialized to the value provided to tf.Variable but can be changed using operations like
tf.assign. For example, W=-1 and b=1 are the optimal parameters for our model. We can change W and b accordingly:
'''

fixW = tf.assign(W, [-1.])
fixb = tf.assign(b, [1.])
sess.run([fixW, fixb])

print(sess.run(loss, {x: [1, 2, 3, 4], y: [0, -1, -2, -3]}))       # 0.0

'''
We guessed the "perfect" values of W and b, but the whole point of machine learning is to find the correct model
parameters automatically. We will show how to accomplish this in the next section.-> trainAPI.py
'''



# source = https://www.tensorflow.org/get_started/get_started