# stdlib
from typing import Optional

# 3rd party
import pyms_nist_search
import pytest
from coincidence.regressions import AdvancedDataRegressionFixture
from domdf_python_tools.paths import PathPlus
from domdf_python_tools.typing import PathLike
from libgunshotmatch.consolidate import InvertedFilter
from libgunshotmatch.method import Method
from libgunshotmatch.project import Project

# this package
from gunshotmatch_pipeline import nist_ms_search
from gunshotmatch_pipeline.excluded_peaks import get_excluded_peaks


@pytest.fixture(scope="module")
def project() -> Project:
	filename = PathPlus(__file__).parent / "test_mock_projects" / "Eley Hymax.gsmp"
	return Project.from_file(filename)


class MockEngine(pyms_nist_search.Engine):
	"""
	Engine that returns :py:obj:`None` for the reference data.
	"""

	initialised = False

	def __init__(
			self,
			lib_path: PathLike,
			lib_type: int = ...,
			work_dir: Optional[PathLike] = None,
			debug: bool = False,
			):
		pass

	def get_reference_data(self, spec_loc: int) -> pyms_nist_search.ReferenceData:
		return None  # type: ignore[return-value]


def test_excluded_peaks(project: Project, monkeypatch, advanced_data_regression: AdvancedDataRegressionFixture):
	monkeypatch.setattr(nist_ms_search, "_create_engine", lambda *args, **kwargs: MockEngine(''))
	method = Method()
	peak_filter: InvertedFilter = InvertedFilter.from_method(method.consolidate)
	excluded_peaks = get_excluded_peaks(project, nist_ms_search.PyMSNISTSearchCfg(''), peak_filter)

	advanced_data_regression.check({
			"small_peaks": excluded_peaks.small_peaks,
			"filtered_out_consolidated_peaks": excluded_peaks.filtered_out_consolidated_peaks,
			"debug_stdout": excluded_peaks.debug_stdout.getvalue(),
			})
