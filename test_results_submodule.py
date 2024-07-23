# stdlib
from collections import defaultdict
from typing import Dict

# 3rd party
from domdf_python_tools.paths import PathPlus

# this package
import gunshotmatch_pipeline.results
from gunshotmatch_pipeline.projects import Projects, process_projects
from gunshotmatch_pipeline.results import compounds, matches
from gunshotmatch_pipeline.utils import project_plural

root_dir = PathPlus(__file__).parent.abspath()
decision_tree_data_dir = root_dir / "decision_tree_data"
decision_tree_data_dir.maybe_make()

projects = Projects.from_toml(PathPlus("projects.toml").read_text())
print(f"Testing results submodule for {len(projects)} {project_plural(len(projects))}:")
for project in projects.per_project_settings:
	print(f"  {project}")

project_file_dir = PathPlus(projects.global_settings.output_directory)
project_objects = list(projects.iter_loaded_projects())
for p in project_objects:
	print(gunshotmatch_pipeline.results.matches(p))

print(gunshotmatch_pipeline.results.compounds(*project_objects))
exit()
# Get single array of compound name to 5x peak areas per propellant
compound_data = combined_data(projects)
compound_data_norm = combined_data(projects, normalize=True)

(decision_tree_data_dir / "compounds.json").dump_json(compound_data, indent=2)
(decision_tree_data_dir / "compounds_norm.json").dump_json(compound_data_norm, indent=2)

decision_tree_compound_data = _machine_learning_data(projects)
decision_tree_compound_norm_data = _machine_learning_data(projects, normalize=True)

(decision_tree_data_dir / "compounds_for_decision_tree.json").dump_json(decision_tree_compound_data, indent=2)
(decision_tree_data_dir / "compounds_for_decision_tree_norm.json").dump_json(
		decision_tree_compound_norm_data, indent=2
		)
