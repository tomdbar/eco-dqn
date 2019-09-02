"""
Trains and tests ECO-DQN on 60 spin BA graphs.
"""
import experiments.BA_60spin.train.train_eco as train
import experiments.BA_60spin.test.test_eco as test

save_loc="BA_60spin/eco"

train.run(save_loc)

test.run(save_loc, graph_save_loc="_graphs/validation/BA_60spin_m4_100graphs.pkl", batched=True, max_batch_size=None)
test.run(save_loc, graph_save_loc="_graphs/validation/BA_100spin_m4_100graphs.pkl", batched=True, max_batch_size=None)
test.run(save_loc, graph_save_loc="_graphs/validation/BA_200spin_m4_100graphs.pkl", batched=True, max_batch_size=25)
test.run(save_loc, graph_save_loc="_graphs/validation/BA_500spin_m4_100graphs.pkl", batched=True, max_batch_size=5)
