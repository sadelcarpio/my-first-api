import tensorflow as tf


def load_model():
    cats_vs_dogs_model = tf.keras.models.load_model('../../my-first-api-main/models/modelo-cats-vs-dogs.h5')
    return cats_vs_dogs_model


def format_image(path: str | None = None, content: bytes | None = None):
    if path is not None:
        img = tf.keras.utils.load_img(path, target_size=(224, 224))
        x = tf.keras.utils.img_to_array(img)
    elif content is not None:
        x = tf.io.decode_image(content)
        x = tf.image.resize(x, (224, 224))
    else:
        return
    x = x / 255
    x = tf.expand_dims(x, 0)
    return x
