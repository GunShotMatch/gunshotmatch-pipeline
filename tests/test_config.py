# 3rd party
import attr
from coincidence.regressions import AdvancedDataRegressionFixture, AdvancedFileRegressionFixture
from domdf_python_tools.paths import PathPlus

# this package
from gunshotmatch_pipeline.config import Configuration
from gunshotmatch_pipeline.nist_ms_search import PyMSNISTSearchCfg


def test_load_config(advanced_data_regression: AdvancedDataRegressionFixture):
	filename = PathPlus(__file__).parent / "config.toml"
	config = Configuration.from_toml(filename.read_text())
	advanced_data_regression.check(attr.asdict(config))


# def test_json_config(advanced_data_regression: AdvancedDataRegressionFixture):

# 	config = Configuration(pyms_nist_search=PyMSNISTSearchCfg(library_path="/path/to/mainlib", user_library=True))
# 	advanced_data_regression.check(config.to_dict())
# 	assert Configuration.from_json(json.dumps(config.to_dict())) == config


def test_export_config(advanced_file_regression: AdvancedFileRegressionFixture):

	config = Configuration(pyms_nist_search=PyMSNISTSearchCfg(library_path="/path/to/mainlib", user_library=True))
	advanced_file_regression.check(config.to_toml())
