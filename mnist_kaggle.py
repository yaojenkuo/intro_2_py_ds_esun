import numpy as np
import tensorflow as tf

# 自訂 next_batch() 函數
def next_batch(batch_size, t_i, t_l, iie, ec, n_e):    
    train_images = t_i
    train_labels = t_l
    index_in_epoch = iie
    epochs_completed = ec
    num_examples = n_e
    
    start = index_in_epoch
    index_in_epoch += batch_size
      
    if index_in_epoch > num_examples:
        epochs_completed += 1
        perm = np.arange(num_examples)
        np.random.shuffle(perm)
        train_images = train_images[perm]
        train_labels = train_labels[perm]
        start = 0
        index_in_epoch = batch_size
        assert batch_size <= num_examples
    end = index_in_epoch
    return train_images[start:end], train_labels[start:end]

# 設定參數
n_features = 784
n_labels = 10

# 啟動 InteractiveSession
sess = tf.InteractiveSession()
x = tf.placeholder(tf.float32, shape=[None, n_features])
y_ = tf.placeholder(tf.float32, shape=[None, n_labels])

# 自訂初始化權重的函數
def weight_variable(shape):
    initial = tf.truncated_normal(shape, stddev=0.1)
    return tf.Variable(initial)

def bias_variable(shape):
    initial = tf.constant(0.1, shape=shape)
    return tf.Variable(initial)
    
# 自訂 convolution 與 max-pooling 的函數
def conv2d(x, W):
    return tf.nn.conv2d(x, W, strides=[1, 1, 1, 1], padding='SAME')

def max_pool_2x2(x):
    return tf.nn.max_pool(x, ksize=[1, 2, 2, 1], strides=[1, 2, 2, 1], padding='SAME')

# 第一層是 Convolution 層（32 個神經元），會利用解析度 5x5 的 filter 取出 32 個特徵，然後將圖片降維成解析度 14x14
W_conv1 = weight_variable([5, 5, 1, 32])
b_conv1 = bias_variable([32])
x_image = tf.reshape(x, [-1, 28, 28, 1])
h_conv1 = tf.nn.relu(conv2d(x_image, W_conv1) + b_conv1)
h_pool1 = max_pool_2x2(h_conv1)

# 第二層是 Convolution 層（64 個神經元），會利用解析度 5x5 的 filter 取出 64 個特徵，然後將圖片降維成解析度 7x7
W_conv2 = weight_variable([5, 5, 32, 64])
b_conv2 = bias_variable([64])
h_conv2 = tf.nn.relu(conv2d(h_pool1, W_conv2) + b_conv2)
h_pool2 = max_pool_2x2(h_conv2)

# 第三層是 Densely Connected 層（1024 個神經元），會將圖片的 1024 個特徵攤平
W_fc1 = weight_variable([7 * 7 * 64, 1024])
b_fc1 = bias_variable([1024])
h_pool2_flat = tf.reshape(h_pool2, [-1, 7 * 7 * 64])
h_fc1 = tf.nn.relu(tf.matmul(h_pool2_flat, W_fc1) + b_fc1)

# 輸出結果之前使用 Dropout 函數避免過度配適
keep_prob = tf.placeholder(tf.float32)
h_fc1_drop = tf.nn.dropout(h_fc1, keep_prob)

# 第四層是輸出層（10 個神經元），使用跟之前相同的 Softmax 函數輸出結果
W_fc2 = weight_variable([1024, 10])
b_fc2 = bias_variable([10])
y_conv = tf.matmul(h_fc1_drop, W_fc2) + b_fc2

# 訓練與模型評估
cross_entropy = tf.reduce_mean(tf.nn.softmax_cross_entropy_with_logits(logits = y_conv, labels = y_))
tf.summary.scalar("CrossEntropy", cross_entropy)
train_step = tf.train.AdamOptimizer(1e-4).minimize(cross_entropy)
correct_prediction = tf.equal(tf.argmax(y_conv,1), tf.argmax(y_,1))
accuracy = tf.reduce_mean(tf.cast(correct_prediction, tf.float32))
tf.summary.scalar("Accuracy", accuracy)

# 初始化
sess.run(tf.global_variables_initializer())
for i in range(20000):
    #get new batch
    batch_X, batch_y = next_batch(50, X_train, y_train, 0, 0, X_train.shape[0])
    if i%100 == 0:
        train_accuracy = accuracy.eval(feed_dict = {x: batch_X, y_: batch_y, keep_prob: 1.0})
        print "step %i, training accuracy %.2f" % (i, train_accuracy)
    train_step.run(feed_dict={x: batch_X, y_: batch_y, keep_prob: 0.5})

# 預測
predict = tf.argmax(y_conv, 1)
predicted_labels = predict.eval(feed_dict={x: X_test, keep_prob: 1.0})

# 關閉 session
sess.close()

# 輸出資料
ImageId = np.arange(1, 28001)
my_solution = pd.DataFrame(predicted_labels.astype('int'), ImageId, columns = ["Label"])
my_solution.to_csv("mnist/cnn_solution.csv", index_label = ["ImageId"])