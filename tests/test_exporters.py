# 3rd party
import pytest
from coincidence.regressions import AdvancedFileRegressionFixture
from domdf_python_tools.paths import PathPlus
from libgunshotmatch.datafile import Datafile, Repeat
from libgunshotmatch.method import Method
from libgunshotmatch.project import Project

# this package
from gunshotmatch_pipeline import prepare_datafile
from gunshotmatch_pipeline.exporters import (
		verify_saved_datafile,
		verify_saved_project,
		write_combined_csv,
		write_matches_json
		)


@pytest.fixture(scope="module")
def repeat() -> Repeat:
	datafile = PathPlus(__file__).parent / "CBC_5_SUBTRACT.JDX"
	with pytest.MonkeyPatch.context() as mp:
		mp.setenv("USERNAME", "test-user")
		repeat, gcms_data = prepare_datafile(datafile, Method(), verbose=True)
	return repeat


@pytest.fixture(scope="module")
def project() -> Project:
	filename = PathPlus(__file__).parent / "test_mock_projects" / "Eley Hymax.gsmp"
	return Project.from_file(filename)


def test_write_combined_csv(
		project: Project,
		tmp_pathplus: PathPlus,
		advanced_file_regression: AdvancedFileRegressionFixture,
		):

	for repeat in project.datafile_data.values():
		write_combined_csv(repeat, tmp_pathplus)
		filename = tmp_pathplus / f"{repeat.name}_COMBINED.csv"
		assert filename.exists()
		assert filename.is_file()
		advanced_file_regression.check_file(filename, extension=f"_{repeat.name}.csv")


def test_verify_saved_datafile(
		repeat: Repeat,
		tmp_pathplus: PathPlus,
		):
	filename = PathPlus(repeat.datafile.export(tmp_pathplus))
	assert filename.name == "CBC_5_SUBTRACT.gsmd"
	assert filename.exists()
	assert filename.is_file()

	datafile = Datafile.from_file(filename)

	verify_saved_datafile(repeat.datafile, datafile)


def test_verify_saved_project(
		project: Project,
		tmp_pathplus: PathPlus,
		):
	filename = PathPlus(project.export(tmp_pathplus))
	assert filename.name == "Eley Hymax.gsmp"
	assert filename.exists()
	assert filename.is_file()

	new_project = Project.from_file(filename)

	verify_saved_project(project, new_project)


@pytest.mark.usefixtures("fixed_datetime")
def test_write_matches_json(
		project: Project,
		tmp_pathplus: PathPlus,
		advanced_file_regression: AdvancedFileRegressionFixture,
		):
	write_matches_json(project, tmp_pathplus)
	filename = tmp_pathplus / "Eley Hymax.json"
	assert filename.exists()
	assert filename.is_file()
	advanced_file_regression.check_file(filename)
