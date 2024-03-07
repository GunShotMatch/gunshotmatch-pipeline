# stdlib
from typing import List, Tuple

# 3rd party
from coincidence.regressions import AdvancedDataRegressionFixture
from domdf_python_tools.paths import PathPlus
from sklearn.ensemble import RandomForestClassifier  # type: ignore[import]

# this package
from gunshotmatch_pipeline.decision_tree import DecisionTreeVisualiser
from gunshotmatch_pipeline.decision_tree.export import deserialise_random_forest


def load_classifier(filename: PathPlus) -> Tuple[RandomForestClassifier, List[str], List[str]]:
	json_model = filename.load_json()
	classifier = deserialise_random_forest(json_model["classifier"])
	factorize_map = json_model["factorize_map"]
	feature_names = json_model["feature_names"]

	assert classifier.feature_names_in_ == feature_names
	return classifier, factorize_map, feature_names


def test_graphviz_export(tmp_pathplus: PathPlus, advanced_data_regression: AdvancedDataRegressionFixture):
	classifier, factorize_map, feature_names = load_classifier(PathPlus("tests/decision-tree.json"))

	dtv = DecisionTreeVisualiser(classifier, feature_names, factorize_map)
	dtv.visualise_tree(filename=(tmp_pathplus / "tree").as_posix())

	output_files = [p.name for p in tmp_pathplus.iterchildren(match="*.dot")]
	output_files.sort()

	advanced_data_regression.check({
			"feature_names": dtv.feature_names,
			"factorize_map": dtv.factorize_map,
			"_dotsafe_class_names": dtv._dotsafe_class_names,
			"output_files": output_files,
			})
