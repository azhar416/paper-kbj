import tensorflow as tf
print(tf.__version__)
print("Is GPU available: ", tf.config.list_physical_devices('GPU'))