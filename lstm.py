import numpy as np
import kim as kim
import kim.nn as nn

import datetime
from timeit import default_timer as timer

started_at = timer()
kim.autograd.CompGraph.MAX_NODE_COUNT = 0

# Fix python3 -m pytest -k "test_lstm[cuda-True-True-1-1-1-1-13]" # bị hang
# giảm seq_length từ 13 => 9 chạy ok!
# => ko phải bị hang mà là chạy quá lâu ko ra, 
device, init_hidden, bias = kim.default_device(), True, True
hidden_size, input_size, batch_size, num_layers, seq_length = 1, 1, 1, 1, 130

x = np.random.randn(seq_length, batch_size, input_size).astype(np.float32)
h0 = np.random.randn(num_layers, batch_size, hidden_size).astype(np.float32)
c0 = np.random.randn(num_layers, batch_size, hidden_size).astype(np.float32)

model = nn.LSTM(input_size, hidden_size, num_layers, bias, device=device)

if init_hidden:
    output, (h, c) = model(kim.Tensor(x, device=device), (kim.Tensor(h0, device=device), kim.Tensor(c0, device=device)))
else:
    output, (h, c) = model(kim.Tensor(x, device=device), None)

print(">>>", output.shape)
output.sum().backward()

tensor_count = kim.autograd.CompGraph.MAX_NODE_COUNT
timespent = datetime.timedelta(seconds=timer() - started_at)
print(f"seq_length %i, tensor_count %i, timespent: %s" % (seq_length, tensor_count, timespent))

print("\nDONE")
print(model.lstm_cells[0].W_ih.grad.detach().numpy())