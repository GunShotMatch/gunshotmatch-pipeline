# 3rd party
from coincidence.regressions import AdvancedDataRegressionFixture
from domdf_python_tools.paths import PathPlus
from libgunshotmatch.project import Project

# this package
from gunshotmatch_pipeline.projects import Projects


def test_iter_load_projects(advanced_data_regression: AdvancedDataRegressionFixture):
	filename = PathPlus(__file__).parent / "projects.toml"

	projects = Projects.from_toml(filename.read_text())

	all_names = []
	for project in projects.iter_loaded_projects():
		all_names.append(project.name)
		assert isinstance(project, Project)

	advanced_data_regression.check(all_names)
