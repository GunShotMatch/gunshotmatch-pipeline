# 3rd party
import attr
from coincidence.regressions import AdvancedDataRegressionFixture
from domdf_python_tools.paths import PathPlus

# this package
from gunshotmatch_pipeline.unknowns import UnknownSettings


def test_load_unknowns(advanced_data_regression: AdvancedDataRegressionFixture):
	filename = PathPlus(__file__).parent / "unknown.toml"
	unknowns = UnknownSettings.from_toml(filename.read_text())
	advanced_data_regression.check(attr.asdict(unknowns))
