# Train and test cifar10
# - - - - - - - - - - - 
# ./get_data.py
# cd apps
# python3 cifar10.py
# KIM_DEVICE=cuda_triton python3 simple_training.py

# Common tests for a specific backend
# - - - - - - - - - - - - - - - - - -
# KIM_BACKEND=nd KIM_DEVICE=cuda_triton ./tests.sh
# KIM_BACKEND=nd KIM_DEVICE=cuda ./tests.sh
# KIM_BACKEND=nd KIM_DEVICE=cpu ./tests.sh
# KIM_BACKEND=nd KIM_DEVICE=cpu_numpy ./tests.sh
# KIM_BACKEND=np ./tests.sh

# Heavy tests
# - - - - - -
# python3 -m pytest tests/test_mlp_resnet.py tests/test_data.py tests/test_cifar_ptb_data.py

#######
# hw4 #
#######

# python3 -m mugrade submit _r1VOvEAgPZvLXFJ18agr -k "resnet9"
# python3 -m mugrade submit _r1VOvEAgPZvLXFJ18agr -k "submit_ptb"
python3 -m mugrade submit _r1VOvEAgPZvLXFJ18agr -k "language_model"

# python3 -m pytest -l -v -k "language_model_implementation"
# python3 -m pytest -l -v -k "language_model_training"

# https://github.com/dlsyscourse/hw4/blob/main/hw4.ipynb
# https://github.com/dlsyscourse/public_notebooks/blob/main/convolution_implementation.ipynb
# https://github.com/dlsyscourse/public_notebooks/blob/main/rnn_implementation.ipynb
# https://youtu.be/7kclgMIcMq0?t=2354 => conv via matmul


#######
# hw3 #
#######

# https://colab.research.google.com/drive/1dnXj1U2DWtnaHanFoYa7XODKUDIjcl_6
# https://colab.research.google.com/drive/1DjW7RRF3chDfkp8LcDJCyQB8Bd11nCZ0

# python3 -m pytest tests/test_ndarray.py -v -k "(permute or reshape or broadcast or getitem) and cpu and not compact"
# python3 -m mugrade submit _r1VOvEAgPZvLXFJ18agr tests/hw3_submit.py -k "python_ops"

# make && python3 -m pytest -v -k "(compact or setitem) and cpu"
# python3 -m mugrade submit _r1VOvEAgPZvLXFJ18agr tests/hw3_submit.py -k "cpu_compact_setitem"

# make && python3 -m pytest -v -k "(ewise_fn or ewise_max or log or exp or tanh or (scalar and not setitem)) and cpu"
# python3 -m mugrade submit _r1VOvEAgPZvLXFJ18agr tests/hw3_submit.py -k "ndarray_cpu_ops"

# make && python3 -m pytest -v -k "reduce and cpu"
# python3 -m mugrade submit _r1VOvEAgPZvLXFJ18agr tests/hw3_submit.py -k "ndarray_cpu_reductions"

# make && python3 -m pytest -v -k "matmul and cpu"
# python3 -m mugrade submit _r1VOvEAgPZvLXFJ18agr tests/hw3_submit.py -k "ndarray_cpu_matmul"



#######
# hw2 #
#######

# https://github.com/dlsyscourse/hw2/blob/main/hw2.ipynb
# https://www.youtube.com/watch?v=uB81vGRrH0c

# python3 -m pytest tests/test_data.py
# python3 -m pytest tests/test_nn.py
# python3 -m pytest tests/test_optim.py
# python3 -m pytest tests/test_mlp_resnet.py
# python3 -m pytest tests/test_mlp_resnet.py -v -k "test_mlp_eval_epoch_1"
# python3 -m pytest tests/test_mlp_resnet.py -v -k "test_mlp_train_mnist_1"
# python3 -m mugrade submit _r1VOvEAgPZvLXFJ18agr tests/hw2_submit.py -k "mlp_resnet"



#######
# hw1 #
#######

# https://colab.research.google.com/github/dlsyscourse/hw1/blob/master/hw1.ipynb
# https://www.youtube.com/watch?v=cNADlHfHQHg
# 
# python3 -m pytest
# python3 -m pytest -l -v -k "forward"
# python3 -m pytest -l -v -k "backward"
# python3 -m pytest -v -k "topo_sort"
# python3 -m pytest -v -k "compute_gradient"
# python3 -m pytest -v -k "nn_softmax_loss"
# python3 -m pytest -v -k "nn_epoch"
# python3 -m mugrade submit _r1VOvEAgPZvLXFJ18agr tests/hw1_submit.py
