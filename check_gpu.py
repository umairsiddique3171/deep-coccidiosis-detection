import tensorflow as tf

if __name__ == "__main__":

    gpus = tf.config.list_physical_devices('GPU')
    if gpus:
        print("CUDA GPU is available.")
        for gpu in gpus:
            print(gpu)
    else:
        print("No GPU available.")