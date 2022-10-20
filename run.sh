# pip3 install pytest numpy numdifftools pybind11 requests

# https://colab.research.google.com/drive/1dnXj1U2DWtnaHanFoYa7XODKUDIjcl_6
# https://colab.research.google.com/drive/1DjW7RRF3chDfkp8LcDJCyQB8Bd11nCZ0


# https://github.com/dlsyscourse/hw2/blob/main/hw2.ipynb
# https://www.youtube.com/watch?v=uB81vGRrH0c
# 
# python3 -m pytest tests/test_ops.py -k "op_logsumexp_backward_5"
# python3 -m mugrade submit _r1VOvEAgPZvLXFJ18agr tests/hw2_submit.py -k "submit_optim_sgd"
python3 -m pytest tests/test_resnet.py -v
# python3 -m mugrade submit _r1VOvEAgPZvLXFJ18agr tests/hw2_submit.py

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
