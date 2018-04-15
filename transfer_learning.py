import tensorflow as tf
import os

os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'
device_name = tf.test.gpu_device_name()
#if device_name != '/device:GPU:0':
#  raise SystemError('GPU device not found')
#print('Found GPU at: {}'.format(device_name))
from sutils import *
import os, json
from glob import glob

import tensorflow.python.keras
import tensorflow as tf

from tensorflow.python.keras.applications import inception_v3
from tensorflow.python.keras.applications import vgg16
from tensorflow.python.keras.preprocessing import image
from tensorflow.python.keras.models import Model
from tensorflow.python.keras.layers import Dense, GlobalAveragePooling2D
from tensorflow.python.keras import backend as K

from keras.applications.imagenet_utils import preprocess_input, decode_predictions

from IPython.display import Image
from keras.preprocessing import image
import numpy as np


print(tf.keras.__version__)
print(tf.__version__)

model = inception_v3.InceptionV3(weights='imagenet', include_top=True)
image_path = "./imagenet/"


img_path = os.path.join(image_path, 'cow.jpg')
img = image.load_img(img_path, target_size=(299, 299))
x = image.img_to_array(img)
x = np.expand_dims(x, axis=0)
x = inception_v3.preprocess_input(x)
print('Input image shape:', x.shape)

preds = model.predict(x)

print(' ')
print('Predicted:', decode_predictions(preds))

Image(img_path)
img.show()




