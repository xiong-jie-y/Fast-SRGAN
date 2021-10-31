import tensorflow as tf
import os

image_paths = [os.path.join("original", x) for x in os.listdir("original")]
for image_path in image_paths:
    print(image_path)
    image = tf.io.read_file(image_path)
    image = tf.image.decode_jpeg(image, channels=3)
