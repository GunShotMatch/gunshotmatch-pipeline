# 3rd party
from coincidence.regressions import AdvancedDataRegressionFixture
from domdf_python_tools.paths import PathPlus
from pytest_regressions.dataframe_regression import DataFrameRegressionFixture
from sklearn.tree import DecisionTreeClassifier  # type: ignore[import-untyped]

# this package
from gunshotmatch_pipeline.decision_tree import data_from_projects, dotsafe_name, fit_decision_tree
from gunshotmatch_pipeline.projects import Projects


def test_fit_decision_tree(
		advanced_data_regression: AdvancedDataRegressionFixture,
		dataframe_regression: DataFrameRegressionFixture,
		):
	filename = PathPlus(__file__).parent / "projects.toml"

	projects = Projects.from_toml(filename.read_text())

	data, factorize_map = data_from_projects(projects)

	dataframe_regression.check(data)
	assert factorize_map == [
			"Eley Hymax",
			"Eley Super Game",
			"Gamebore Clear Pigeon",
			"Holland & Holland Super Twelve",
			"Remington RXP",
			"Ward Thompson Classic",
			"Western Double A",
			]

	classifier = DecisionTreeClassifier(random_state=1234)
	feature_names = fit_decision_tree(data, classifier)
	advanced_data_regression.check(sorted(feature_names), basename="test_fit_decision_tree_feature_names_")


def test_dotsafe_name():
	assert dotsafe_name("Holland & Holland Super Twelve") == "Holland &amp; Holland Super Twelve"
