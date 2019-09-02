"""
Trains and tests ECO-DQN on 200 spin BA graphs.
"""
import experiments.BA_200spin.test.test_eco as test
import experiments.BA_200spin.train.train_eco as train

save_loc="BA_200spin/eco"

train.run(save_loc)

test.run(save_loc, graph_save_loc="_graphs/validation/BA_200spin_m4_100graphs.pkl", batched=True, max_batch_size=25)
test.run(save_loc, graph_save_loc="_graphs/validation/BA_500spin_m4_100graphs.pkl", batched=True, max_batch_size=5)


