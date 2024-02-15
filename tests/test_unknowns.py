# stdlib
import re

# 3rd party
import attrs
import pytest
from coincidence.regressions import AdvancedDataRegressionFixture
from domdf_python_tools.paths import PathPlus

# this package
from gunshotmatch_pipeline.unknowns import UnknownSettings

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
	advanced_data_regression.check(attrs.asdict(unknowns))


tabled_toml = """
name = "Unknown Western Double A"
method = "method.toml"
config = "config.toml"
data_directory = "data"
output_directory = "unknowns"
datafile = "aa_5_231123_013.func_0.JDX"


["Western Double A"]
method = "method.toml"
config = "config.toml"
data_directory = "data"
output_directory = "unknowns"
datafile = "aa_5_231123_013"

["Ward Thompson Classic"]
method = "method.toml"
config = "config.toml"
data_directory = "data"
output_directory = "unknowns"
datafile = "classic_5_231123_018.func_0.JDX"

["Eley Super Game"]
method = "method.toml"
config = "config.toml"
data_directory = "data"
output_directory = "unknowns"
datafile = "esg_5_231123_038.func_0.JDX"

["Holland & Holland Super Twelve"]
method = "method.toml"
config = "config.toml"
data_directory = "data"
output_directory = "unknowns"
datafile = "hh12_5_231123_008.func_0.JDX"

["Eley Hymax"]
method = "method.toml"
config = "config.toml"
data_directory = "data"
output_directory = "unknowns"
datafile = "hymax_5_231123_028.func_0.JDX"

["Gamebore Clear Pigeon"]
method = "method.toml"
config = "config.toml"
data_directory = "data"
output_directory = "unknowns"
datafile = "pigeon_4_061123_033.func_0.JDX"

["Remington RXP"]
method = "method.toml"
config = "config.toml"
data_directory = "data"
output_directory = "unknowns"
datafile = "rxp_5_231123_023.func_0.JDX"
"""


def test_from_toml_table(advanced_data_regression: AdvancedDataRegressionFixture):
	parsed_toml = tomllib.loads(tabled_toml)
	unknowns = UnknownSettings.from_toml_table("Gamebore Clear Pigeon", parsed_toml["Gamebore Clear Pigeon"])
	advanced_data_regression.check(attrs.asdict(unknowns))
