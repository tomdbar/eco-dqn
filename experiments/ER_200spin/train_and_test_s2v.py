"""
Trains and tests S2V-DQN on 200 spin ER graphs.
"""
import experiments.ER_200spin.test.test_s2v as test
import experiments.ER_200spin.train.train_s2v as train

save_loc="ER_200spin/s2v"

train.run(save_loc)

test.run(save_loc, graph_save_loc="_graphs/validation/ER_200spin_p15_100graphs.pkl", batched=True, max_batch_size=25)
test.run(save_loc, graph_save_loc="_graphs/validation/ER_500spin_p15_100graphs.pkl", batched=True, max_batch_size=5)