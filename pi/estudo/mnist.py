import tensorflow as tf
import tensorflow_datasets as tfds

BUFFER_SIZE = 70_000
BATCH_SIZE = 128
NUM_EPOCHS = 20

mnist_dataset, mnist_info = tfds.load(name='mnist', with_info=True, as_supervised=True)
mnist_train, mnist_test = mnist_dataset['train'], mnist_dataset['test']

def scale(image, label):
    image = tf.cast(image, tf.float32)
    image /= 255.
    return image, label

train_and_validation_data = mnist_train.map(scale)
test_data = mnist_test.map(scale)

num_validation_samples = 0.1 * mnist_info.splits['train'].num_examples
num_validation_samples = tf.cast(num_validation_samples, tf.int64)

num_test_samples = mnist_info.splits['test'].num_examples
num_test_samples = tf.cast(num_test_samples, tf.int64)

train_and_validation_data = train_and_validation_data.shuffle(BUFFER_SIZE)

train_data = train_and_validation_data.skip(num_validation_samples)
validation_data = train_and_validation_data.take(num_validation_samples)

train_data = train_data.batch(BATCH_SIZE)
validation_data = validation_data.batch(num_validation_samples)
test_data = test_data.batch(num_test_samples)

model = tf.keras.Sequential([
    tf.keras.layers.Conv2D(50, 5, activation='relu', input_shape=(28,28,1))
])