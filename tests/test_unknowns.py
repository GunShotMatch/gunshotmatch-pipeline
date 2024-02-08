# stdlib
import re

# 3rd party
import attr
import pytest
from coincidence.regressions import AdvancedDataRegressionFixture
from domdf_python_tools.paths import PathPlus

# this package
from gunshotmatch_pipeline.unknowns import UnknownSettings
from gunshotmatch_pipeline.utils import tomllib

missing_key_toml = """
name = "Unknown Western Double A"
config = "config.toml"
data_directory = "data"
output_directory = "unknowns"
datafile = "aa_5_231123_013.func_0.JDX"
"""


def test_from_toml_missing_keys():
	with pytest.raises(TypeError, match=re.escape("__init__() missing 1 required positional argument: 'method'")):
		UnknownSettings.from_toml(missing_key_toml)


def test_load_unknowns(advanced_data_regression: AdvancedDataRegressionFixture):
	filename = PathPlus(__file__).parent / "unknown.toml"
	unknowns = UnknownSettings.from_toml(filename.read_text())
	advanced_data_regression.check(attr.asdict(unknowns))
