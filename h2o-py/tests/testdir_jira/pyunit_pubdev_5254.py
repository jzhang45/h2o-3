import h2o
from h2o.estimators import H2OGeneralizedLinearEstimator

from tests import pyunit_utils


def pubdev_5254():
    data = h2o.import_file("pyunit_pubdev_5254.csv")
    data[1] = data[1].round().asfactor()
    data.summary()

    estimator = H2OGeneralizedLinearEstimator(family="binomial", Lambda=0, missing_values_handling="MeanImputation")
    estimator.train(x=["second", "third"], y="first", training_frame=data)
    estimator.summary()


if __name__ == "__main__":
    pyunit_utils.standalone_test(pubdev_5254)
else:
    pubdev_5254()
