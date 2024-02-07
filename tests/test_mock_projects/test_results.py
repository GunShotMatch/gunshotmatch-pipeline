# 3rd party
import numpy
import pytest
from coincidence.regressions import AdvancedDataRegressionFixture, _representer_for
from domdf_python_tools.paths import PathPlus
from libgunshotmatch.project import Project
from pytest_regressions.data_regression import RegressionYamlDumper

# this package
from gunshotmatch_pipeline import results


@_representer_for(
		numpy.int64,
		numpy.int32,
		numpy.float64,
		)
def _represent_numpy(dumper: RegressionYamlDumper, data: int):  # noqa: MAN002
	return dumper.represent_data(int(data))


@pytest.fixture(scope="module")
def hymax_project() -> Project:
	filename = PathPlus(__file__).parent / "Eley Hymax.gsmp"
	return Project.from_file(filename)


@pytest.mark.usefixtures("fixed_datetime")
def test_matches(hymax_project: Project, advanced_data_regression: AdvancedDataRegressionFixture):
	advanced_data_regression.check(results.matches(hymax_project))


def test_machine_learning_data_one_project(
		hymax_project: Project,
		advanced_data_regression: AdvancedDataRegressionFixture,
		):
	advanced_data_regression.check(results.machine_learning_data(hymax_project))


@pytest.mark.parametrize("normalize", [True, False])
def test_compounds_one_project(
		hymax_project: Project,
		advanced_data_regression: AdvancedDataRegressionFixture,
		normalize: bool,
		):
	advanced_data_regression.check(results.compounds(hymax_project, normalize=normalize))
