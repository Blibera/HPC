import logging
import itertools
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from tqdm import tqdm
from hmmlearn.hmm import GaussianHMM
from sklearn.model_selection import train_test_split
import csv
add = []
ff = open("C:/Users/DI_Lab/Desktop/20년도 Kisti 과제/HMM/hmm learn/변수 일부만/collectl.csv", "w",newline='')
write = csv.writer(ff)

class HpcPredictor(object):
    def __init__(self, n_latency=10, test_size=0.33,
                 n_hidden_states=5, n_steps_cpu_bus_cycles=10,
                 n_steps_msr_tsc=10, n_steps_cpu_ref_cycles=10, n_steps_frac_change=50):

        self._init_logger()

        self.n_latency = n_latency

        self.hmm = GaussianHMM(n_components=n_hidden_states)

        self._split_train_test_data(test_size)

        self._compute_all_possible_outcomes(n_steps_cpu_bus_cycles, n_steps_msr_tsc,
                                            n_steps_cpu_ref_cycles, n_steps_frac_change)

    # setting logger
    def _init_logger(self):
        self._logger = logging.getLogger(__name__)
        handler = logging.StreamHandler()
        formatter = logging.Formatter(
            '%(asctime)s %(name)-12s %(levelname)-8s %(message)s')
        handler.setFormatter(formatter)
        self._logger.addHandler(handler)
        self._logger.setLevel(logging.DEBUG)

    # split train/test data from input dataset
    def _split_train_test_data(self, test_size):
        data = pd.read_csv('C:/Users/DI_Lab/Desktop/20년도 Kisti 과제/HMM/hmm learn/변수 일부만/test2 - 복사본 (2).csv')
        # shuffle=False 'time serial'
        test_data = pd.read_csv('C:/Users/DI_Lab/Desktop/20년도 Kisti 과제/HMM/hmm learn/변수 일부만/test2 - 복사본 (2) - 복사본.csv')

        self._train_data = data
        self._test_data = test_data

        #print("split train test data is complete")

    # important part about our paper _ Extracting Features
    @staticmethod
    def _extract_features(data):
        cpu_bus_cycles = np.array(data['Perf_node01_msr_tsc_'])
        msr_tsc = np.array(data['Perf_node01_cpu_ref_cycles_'])
        cpu_ref_cycles = np.array(data['IPC'])
        frac_change = np.array(data['power_per'])

        print("extract features is complete")

        return np.column_stack((cpu_bus_cycles, msr_tsc, cpu_ref_cycles, frac_change))

    # training use train_data/_extract_features
    def fit(self):
        self._logger.info('>>> Extracting Features')
        feature_vactor = HpcPredictor._extract_features(self._train_data)
        self._logger.info('Features extraction Completed <<<')
        g = self.hmm.fit(feature_vactor)
        print(feature_vactor)
        print(g)
        #print("fit is complete")

    # make array about all_possible_outcomes (_extract_features)
    def _compute_all_possible_outcomes(self, n_steps_cpu_bus_cycles, n_steps_msr_tsc,
                                       n_steps_cpu_ref_cycles, n_steps_frac_change):
        '''
        all_possible_outcomes range _ you should be check here!
        '''
        cpu_bus_cycles_range = np.linspace(-0.5, 0.5, n_steps_cpu_bus_cycles)
        msr_tsc_range = np.linspace(-0.5, 0.5, n_steps_msr_tsc)
        cpu_ref_cycles_range = np.linspace(-0.5, 0.5, n_steps_cpu_ref_cycles)
        frac_change_range = np.linspace(-0.5, 0.5, n_steps_frac_change)

        # itertools.product : compute the cartesian product of input iterables
        self._possible_outcomes = np.array(list(itertools.product(cpu_bus_cycles_range, msr_tsc_range
                                                                  , cpu_ref_cycles_range, frac_change_range)))
        #print('compute all possible outcomes is complete')

    def _get_most_probable_outcome(self, day_index):
        # i think this mean 10-markov model (latency = 10)
        previous_data_start_index = max(0, day_index - self.n_latency)
        previous_data_end_index = max(0, day_index)
        previous_data = self._test_data.iloc[previous_data_end_index: previous_data_start_index]
        previous_data_features = HpcPredictor._extract_features(previous_data)

        outcome_score = []
        # calculate every possible outcome's hmm score
        for possible_outcome in self._possible_outcomes:
            total_data = np.row_stack(
                (previous_data_features, possible_outcome))
            outcome_score.append(self.hmm.score(total_data))

        most_probable_outcome = self._possible_outcomes[np.argmax(outcome_score)]

        #print('get most probable outcome is complete')

        # use most max score_decode
        return most_probable_outcome

    def predict_close_power(self, day_index):
        open_price = self._test_data.iloc[day_index]['before']
        _, _, _,predicted_frac_change = self._get_most_probable_outcome(day_index)
        add.append(predicted_frac_change)
        # predict value...but it use frac_change. we can't use it(?)
        # hmm.decode can be used
        print(open_price)
        return open_price * (1 + predicted_frac_change), print(open_price* (1 + predicted_frac_change))

    def predict_close_power_for_time(self, times, with_plot=False):
        predicted_close_power = []
        for day_index in tqdm(range(times)):
            predicted_close_power.append(self.predict_close_power(day_index))
        print(predicted_close_power)

        if with_plot:
            test_data = self._test_data[0: times]
            times = np.array(test_data['num'])
            actual_close_prices = test_data['total']

            fig = plt.figure(figsize=(10, 8))

            axes = fig.add_subplot(111)
            axes.plot(times, actual_close_prices, 'bo-', label="actual")
            axes.plot(times, predicted_close_power, 'r+-', label="predicted")

            fig.autofmt_xdate()

            plt.legend()
            plt.show()

        # return predicted_close_power

hpc_predictor = HpcPredictor()
hpc_predictor.fit()
hpc_predictor.predict_close_power_for_time(10, with_plot=True)

write.writerow(add)