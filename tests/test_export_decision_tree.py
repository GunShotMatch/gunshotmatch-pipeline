# stdlib
import json
import random
from typing import Any, List, Tuple

# 3rd party
import numpy
import pytest
from sklearn.datasets import make_classification  # type: ignore[import]
from sklearn.ensemble import RandomForestClassifier  # type: ignore[import]
from sklearn.feature_extraction import FeatureHasher  # type: ignore[import]
from sklearn.tree import DecisionTreeClassifier  # type: ignore[import]

# this package
from gunshotmatch_pipeline.decision_tree.export import (
		deserialise_decision_tree,
		deserialise_random_forest,
		serialise_decision_tree,
		serialise_random_forest
		)


@pytest.fixture()
def dataset() -> Tuple[List[float], List[int]]:

	X, y = make_classification(n_samples=50, n_features=3, n_classes=3, n_informative=3, n_redundant=0, random_state=0, shuffle=False)

	return X, y


@pytest.fixture()
def sparse_dataset() -> Tuple[Any, List[int]]:
	feature_hasher = FeatureHasher(n_features=3)
	features = []
	for _ in range(0, 100):
		features.append({'a': random.randint(0, 2), 'b': random.randint(3, 5), 'c': random.randint(6, 8)})
	y_sparse = [random.randint(0, 2) for i in range(0, 100)]
	X_sparse = feature_hasher.transform(features)

	return X_sparse, y_sparse


@pytest.mark.parametrize("absolute", [True, False])
def test_decision_tree(dataset: Tuple[List[float], List[int]], absolute: bool):
	model = DecisionTreeClassifier()

	if absolute:
		model.fit(numpy.absolute(dataset[0]), dataset[1])
	else:
		model.fit(*dataset)

	serialised_model = serialise_decision_tree(model)
	# Check can convert to JSON
	json.dumps(serialised_model)

	deserialised_model = deserialise_decision_tree(serialised_model)

	expected_predictions = model.predict(dataset[0])
	actual_predictions = deserialised_model.predict(dataset[0])

	numpy.testing.assert_array_equal(expected_predictions, actual_predictions)


@pytest.mark.parametrize("absolute", [True, False])
def test_decision_tree_sparse(sparse_dataset: Tuple[List[float], List[int]], absolute: bool):
	model = DecisionTreeClassifier()

	if absolute:
		model.fit(numpy.absolute(sparse_dataset[0]), sparse_dataset[1])
	else:
		model.fit(*sparse_dataset)

	serialised_model = serialise_decision_tree(model)
	# Check can convert to JSON
	json.dumps(serialised_model)

	deserialised_model = deserialise_decision_tree(serialised_model)

	expected_predictions = model.predict(sparse_dataset[0])
	actual_predictions = deserialised_model.predict(sparse_dataset[0])

	numpy.testing.assert_array_equal(expected_predictions, actual_predictions)


@pytest.mark.parametrize("absolute", [True, False])
def test_random_forest(dataset: Tuple[List[float], List[int]], absolute: bool):
	model = RandomForestClassifier(n_estimators=10, max_depth=5, random_state=0)

	if absolute:
		model.fit(numpy.absolute(dataset[0]), dataset[1])
	else:
		model.fit(*dataset)

	serialised_model = serialise_random_forest(model)
	# Check can convert to JSON
	json.dumps(serialised_model)

	deserialised_model = deserialise_random_forest(serialised_model)

	expected_predictions = model.predict(dataset[0])
	actual_predictions = deserialised_model.predict(dataset[0])

	numpy.testing.assert_array_equal(expected_predictions, actual_predictions)


@pytest.mark.parametrize("absolute", [True, False])
def test_random_forest_sparse(sparse_dataset: Tuple[List[float], List[int]], absolute: bool):
	model = RandomForestClassifier(n_estimators=10, max_depth=5, random_state=0)

	if absolute:
		model.fit(numpy.absolute(sparse_dataset[0]), sparse_dataset[1])
	else:
		model.fit(*sparse_dataset)

	serialised_model = serialise_random_forest(model)
	# Check can convert to JSON
	json.dumps(serialised_model)

	deserialised_model = deserialise_random_forest(serialised_model)

	expected_predictions = model.predict(sparse_dataset[0])
	actual_predictions = deserialised_model.predict(sparse_dataset[0])

	numpy.testing.assert_array_equal(expected_predictions, actual_predictions)
