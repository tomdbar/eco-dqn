"""
Trains and tests ECO-DQN on 40 spin ER graphs.
"""
import experiments.ER_40spin.test.test_eco as test
import experiments.ER_40spin.train.train_eco as train

save_loc="ER_40spin/eco"

train.run(save_loc)

test.run(save_loc, graph_save_loc="_graphs/validation/ER_40spin_p15_100graphs.pkl", batched=True, max_batch_size=None)
test.run(save_loc, graph_save_loc="_graphs/validation/ER_60spin_p15_100graphs.pkl", batched=True, max_batch_size=None)
test.run(save_loc, graph_save_loc="_graphs/validation/ER_100spin_p15_100graphs.pkl", batched=True, max_batch_size=None)
test.run(save_loc, graph_save_loc="_graphs/validation/ER_200spin_p15_100graphs.pkl", batched=True, max_batch_size=25)
test.run(save_loc, graph_save_loc="_graphs/validation/ER_500spin_p15_100graphs.pkl", batched=True, max_batch_size=5)

