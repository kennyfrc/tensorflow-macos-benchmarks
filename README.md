## Guide

* Run the `install.sh` script if you want to reinstall tensorflow-macos in your system
* To boot the virtual environment, you'll need to use the bash script that the installer has given you. It will look like this: `. "/Users/kennyfrc/tensorflow_macos_venv/bin/activate"`.
* Once you have ran the virtual environment, run the `validate.py` script to check if you have correctly installed tensorflow for macos.

## Benchmarks

Device I used is MacBook Pro (13-inch, 2019), 2.4 GHz Quad-Core Intel Core i5, 8GB RAM, Radeon RX 5700 XT 8 GB.

For `benchmark_mnist.py` (you need `pip install -r requirements.txt`:

```
Train on 469 steps, validate on 79 steps
Epoch 1/12
469/469 [==============================] - 63s 128ms/step - batch: 234.0000 - size: 1.0000 - loss: 0.1607 - accuracy: 0.9530 - val_loss: 0.0528 - val_accuracy: 0.9827
Epoch 2/12
469/469 [==============================] - 62s 129ms/step - batch: 234.0000 - size: 1.0000 - loss: 0.0439 - accuracy: 0.9863 - val_loss: 0.0375 - val_accuracy: 0.9874
Epoch 3/12
469/469 [==============================] - 62s 129ms/step - batch: 234.0000 - size: 1.0000 - loss: 0.0257 - accuracy: 0.9917 - val_loss: 0.0369 - val_accuracy: 0.9881
Epoch 4/12
469/469 [==============================] - 61s 126ms/step - batch: 234.0000 - size: 1.0000 - loss: 0.0188 - accuracy: 0.9937 - val_loss: 0.0327 - val_accuracy: 0.9899
Epoch 5/12
469/469 [==============================] - 61s 127ms/step - batch: 234.0000 - size: 1.0000 - loss: 0.0116 - accuracy: 0.9964 - val_loss: 0.0441 - val_accuracy: 0.9864
Epoch 6/12
469/469 [==============================] - 61s 126ms/step - batch: 234.0000 - size: 1.0000 - loss: 0.0092 - accuracy: 0.9970 - val_loss: 0.0341 - val_accuracy: 0.9903
Epoch 7/12
469/469 [==============================] - 61s 125ms/step - batch: 234.0000 - size: 1.0000 - loss: 0.0078 - accuracy: 0.9973 - val_loss: 0.0338 - val_accuracy: 0.9897
Epoch 8/12
469/469 [==============================] - 61s 127ms/step - batch: 234.0000 - size: 1.0000 - loss: 0.0065 - accuracy: 0.9979 - val_loss: 0.0392 - val_accuracy: 0.9888
Epoch 9/12
469/469 [==============================] - 61s 125ms/step - batch: 234.0000 - size: 1.0000 - loss: 0.0057 - accuracy: 0.9980 - val_loss: 0.0404 - val_accuracy: 0.9895
Epoch 10/12
469/469 [==============================] - 61s 126ms/step - batch: 234.0000 - size: 1.0000 - loss: 0.0048 - accuracy: 0.9985 - val_loss: 0.0464 - val_accuracy: 0.9887
Epoch 11/12
469/469 [==============================] - 61s 127ms/step - batch: 234.0000 - size: 1.0000 - loss: 0.0047 - accuracy: 0.9986 - val_loss: 0.0473 - val_accuracy: 0.9890
Epoch 12/12
469/469 [==============================] - 63s 128ms/step - batch: 234.0000 - size: 1.0000 - loss: 0.0032 - accuracy: 0.9988 - val_loss: 0.0453 - val_accuracy: 0.9897


Summary:
* 64s/epoch
* 129ms/step
* 98.9% final accuracy
```