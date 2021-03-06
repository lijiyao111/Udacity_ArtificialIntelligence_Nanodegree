import math
import statistics
import warnings

import numpy as np
from hmmlearn.hmm import GaussianHMM
from sklearn.model_selection import KFold
from asl_utils import combine_sequences


class ModelSelector(object):
    '''
    base class for model selection (strategy design pattern)
    '''

    def __init__(self, all_word_sequences: dict, all_word_Xlengths: dict, this_word: str,
                 n_constant=3,
                 min_n_components=2, max_n_components=10,
                 random_state=14, verbose=False):
        self.words = all_word_sequences
        self.hwords = all_word_Xlengths
        self.sequences = all_word_sequences[this_word]
        self.X, self.lengths = all_word_Xlengths[this_word]
        self.this_word = this_word
        self.n_constant = n_constant
        self.min_n_components = min_n_components
        self.max_n_components = max_n_components
        self.random_state = random_state
        self.verbose = verbose

    def select(self):
        raise NotImplementedError

    def base_model(self, num_states):
        # with warnings.catch_warnings():
        warnings.filterwarnings("ignore", category=DeprecationWarning)
        # warnings.filterwarnings("ignore", category=RuntimeWarning)
        try:
            hmm_model = GaussianHMM(n_components=num_states, covariance_type="diag", n_iter=1000,
                                    random_state=self.random_state, verbose=False).fit(self.X, self.lengths)
            if self.verbose:
                print("model created for {} with {} states".format(self.this_word, num_states))
            return hmm_model
        except:
            if self.verbose:
                print("failure on {} with {} states".format(self.this_word, num_states))
            return None


class SelectorConstant(ModelSelector):
    """ select the model with value self.n_constant

    """

    def select(self):
        """ select based on n_constant value

        :return: GaussianHMM object
        """
        best_num_components = self.n_constant
        return self.base_model(best_num_components)


class SelectorBIC(ModelSelector):
    """ select the model with the lowest Baysian Information Criterion(BIC) score

    http://www2.imm.dtu.dk/courses/02433/doc/ch6_slides.pdf
    Bayesian information criteria: BIC = -2 * logL + p * logN
    """

    def select(self):
        """ select the best model for self.this_word based on
        BIC score for n between self.min_n_components and self.max_n_components

        :return: GaussianHMM object
        """
        warnings.filterwarnings("ignore", category=DeprecationWarning)

        # TODO implement model selection based on BIC scores
        best_score, best_n_components  = None, None
        for n_components in range(self.min_n_components, self.max_n_components+1):
            try:
                # Create model and logLoss based on current n_components
                model = GaussianHMM(n_components=n_components, n_iter=1000).fit(self.X, self.lengths)
                logL = model.score(self.X, self.lengths)
                # Calculate # free params & logN
                n_features = self.X.shape[1]
                p = n_components * (n_components-1) + 2 * n_features * n_components
                logN = np.log(self.X.shape[0])
                # Calculate score
                i_score = -2 * logL + p * logN
                if(best_score is None or i_score < best_score):
                    best_score, best_n_components = i_score, n_components
            except Exception as e:
                if self.verbose:
                    print("failure on {} with {} states".format(self.this_word, n_components))
                continue

        if(best_score == None):
            best_n_components = 3
        return self.base_model(best_n_components)
        # raise NotImplementedError


class SelectorDIC(ModelSelector):
    ''' select best model based on Discriminative Information Criterion

    Biem, Alain. "A model selection criterion for classification: Application to hmm topology optimization."
    Document Analysis and Recognition, 2003. Proceedings. Seventh International Conference on. IEEE, 2003.
    http://citeseerx.ist.psu.edu/viewdoc/download?doi=10.1.1.58.6208&rep=rep1&type=pdf
    DIC = log(P(X(i)) - 1/(M-1)SUM(log(P(X(all but i))
    '''

    def select(self):
        warnings.filterwarnings("ignore", category=DeprecationWarning)
        # TODO implement model selection using DIC scores
        best_score, best_n_components = None, None

        for n_components in range(self.min_n_components, self.max_n_components+1):
            # Calculate logL for all words with n_components

            n_components_models, n_components_ml = {}, {}
            for word in self.words.keys():
                X_i, lengths_i = self.hwords[word]
                try:
                    # Train model for current word with current n_components
                    model = GaussianHMM(n_components=n_components, n_iter=1000).fit(X_i, lengths_i)
                    logL = model.score(X_i, lengths_i)
                    n_components_models[word] = model
                    n_components_ml[word] = logL
                except Exception as e:
                    # Skip model if can't be created
                    if self.verbose:
                        print("failure on {} with {} states".format(self.this_word, n_components))
                    continue

            if(self.this_word not in n_components_ml): continue

            avg = np.mean([n_components_ml[word] for word in n_components_ml.keys() if word != self.this_word])
            DIC = n_components_ml[self.this_word] - avg

            if(best_score is None or DIC > best_score):
                best_score, best_n_components = DIC, n_components
        if(best_score == None):
            best_n_components = 3
        return self.base_model(best_n_components)

        # raise NotImplementedError


class SelectorCV(ModelSelector):
    ''' select best model based on average log Likelihood of cross-validation folds

    '''

    def select(self):
        warnings.filterwarnings("ignore", category=DeprecationWarning)

        # TODO implement model selection using CV
        best_score, best_n_components = None, None
        for n_components in range(self.min_n_components, self.max_n_components+1):
            scores, n_splits = [], 3
            if(len(self.sequences) < 3):
                try:
                    model = GaussianHMM(n_components=n_components, n_iter=1000).fit(self.X, self.lengths)
                    logL = model.score(self.X, self.lengths)
                    if(best_score is None or logL > best_score):
                        best_score, best_n_components = logL, n_components
                except Exception as e:
                    continue
            else:
                split_method = KFold(random_state=self.random_state, n_splits=n_splits)
                for cv_train_idx, cv_test_idx in split_method.split(self.sequences):
                    X_train, lengths_train = combine_sequences(cv_train_idx, self.sequences)
                    X_test,  lengths_test  = combine_sequences(cv_test_idx, self.sequences)
                    try:
                        model = GaussianHMM(n_components=n_components, n_iter=1000).fit(X_train, lengths_train)
                        logL = model.score(X_test, lengths_test)
                        scores.append(logL)
                    except Exception as e:
                        break

                training_successful = len(scores) == n_splits
                if(not training_successful): continue
                avg = np.average(scores)
                if(best_score is None or avg > best_score):
                    best_score, best_n_components = avg, n_components

        if(best_score == None):
            best_n_components = 3
        return self.base_model(best_n_components)
        # raise NotImplementedError
