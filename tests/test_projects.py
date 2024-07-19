# 3rd party
import attrs
from coincidence.regressions import AdvancedDataRegressionFixture
from domdf_python_tools.paths import PathPlus

# this package
from gunshotmatch_pipeline.projects import Projects


def test_load_projects(advanced_data_regression: AdvancedDataRegressionFixture):
	filename = PathPlus(__file__).parent / "projects.toml"
	projects = Projects.from_toml(filename.read_text())
	advanced_data_regression.check(attrs.asdict(projects))


# def test_json_projects(advanced_data_regression: AdvancedDataRegressionFixture):

# 	filename = PathPlus(__file__).parent / "projects.toml"
# 	projects = Projects.from_toml(filename.read_text())
# 	assert Projects.from_json(json.dumps(projects.to_dict())) == projects
# 	advanced_data_regression.check(projects.to_dict())

# def test_export_projects(advanced_file_regression: AdvancedFileRegressionFixture):
# 	filename = PathPlus(__file__).parent / "projects.toml"
# 	projects = Projects.from_toml(filename.read_text())
# 	advanced_file_regression.check(projects.to_toml())


def test_get_project_settings(advanced_data_regression: AdvancedDataRegressionFixture):
	filename = PathPlus(__file__).parent / "projects.toml"
	projects = Projects.from_toml(filename.read_text())
	advanced_data_regression.check(attrs.asdict(projects.get_project_settings("Gamebore Clear Pigeon")))


def test_iter_project_settings(advanced_data_regression: AdvancedDataRegressionFixture):
	filename = PathPlus(__file__).parent / "projects.toml"
	projects = Projects.from_toml(filename.read_text())
	advanced_data_regression.check([attrs.asdict(ps) for ps in projects.iter_project_settings()])
