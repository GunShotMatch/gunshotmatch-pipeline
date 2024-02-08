# stdlib
import os

# 3rd party
import sdjson
from coincidence.regressions import AdvancedFileRegressionFixture
from domdf_python_tools.paths import PathPlus
from libgunshotmatch.method import Method

# this package
from gunshotmatch_pipeline import prepare_datafile


def test_prepare_datafile(
		advanced_file_regression: AdvancedFileRegressionFixture,
		monkeypatch,
		):
	monkeypatch.setenv("USERNAME", "test-user")
	datafile = PathPlus(__file__).parent / "CBC_5_SUBTRACT.JDX"
	repeat, gcms_data = prepare_datafile(datafile, Method(), verbose=True)
	assert repeat.peaks
	assert repeat.peaks.datafile_name == "CBC_5_SUBTRACT"

	assert repeat.datafile.intensity_matrix is not None

	as_dict = {
			"name": repeat.datafile.name,
			"original_filename": os.path.split(repeat.datafile.original_filename)[1],
			"original_filetype": int(repeat.datafile.original_filetype),
			"description": repeat.datafile.description,
			"version": repeat.datafile.version,
			}

	advanced_file_regression.check(sdjson.dumps(as_dict), extension=".json")

	advanced_file_regression.check(
			sdjson.dumps(repeat.datafile.intensity_matrix.time_list, indent=2),
			extension=".im-times.json",
			)
	advanced_file_regression.check(
			sdjson.dumps(repeat.datafile.intensity_matrix.mass_list, indent=2),
			extension=".im-masses.json",
			)
	# advanced_data_regression.check([[str(round_rt(intensity)) for intensity in row] for row in datafile.intensity_matrix.intensity_array])
