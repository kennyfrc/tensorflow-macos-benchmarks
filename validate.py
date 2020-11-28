import tensorflow as tf
from tensorflow.python.compiler.mlcompute import mlcompute
mlcompute.set_mlc_device(device_name = 'gpu')

print("NOTE: If you're seeing a warning that says 'TF is slow in eager mode when using GPU', that is a good sign. It means you are good to go.")