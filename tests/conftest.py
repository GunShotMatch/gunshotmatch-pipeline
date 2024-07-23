# 3rd party
from coincidence.regressions import _representer_for
from libgunshotmatch.consolidate import ConsolidatedPeak
from libgunshotmatch.peak import PeakList
from pytest_regressions.data_regression import RegressionYamlDumper
from yaml.representer import RepresenterError

pytest_plugins = ("coincidence", )


def represent_undefined(self, data):  # noqa: MAN001,MAN002
	raise RepresenterError("cannot represent an object", data, type(data))


RegressionYamlDumper.represent_undefined = represent_undefined  # type: ignore[method-assign]


@_representer_for(ConsolidatedPeak)
def _represent_consolidated_peak(dumper: RegressionYamlDumper, data: ConsolidatedPeak):  # noqa: MAN002
	return dumper.represent_data(data.to_dict())


@_representer_for(PeakList)
def _represent_peak_list(dumper: RegressionYamlDumper, data: PeakList):  # noqa: MAN002
	return dumper.represent_data(data.to_list())
