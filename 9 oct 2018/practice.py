

import numpy as np
X_train_all = [i for i in range(1000)]
y_train_all = [2*i for i in range(1000)]
indices=list(range(len(X_train_all)))

np.random.seed(42)
np.random.shuffle(indices)

ind=int(len(indices)*0.80)
# train data
X_train=X_train_all[indices[:ind]]
y_train=y_train_all[indices[:ind]]
# validation data
X_val=X_train_all[indices[-(len(indices)-ind):]]
y_val=y_train_all[indices[-(len(indices)-ind):]]