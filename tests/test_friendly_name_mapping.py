# this package
from gunshotmatch_pipeline.utils import friendly_name_mapping


def test_friendly_name_mapping():
	assert friendly_name_mapping["Benzenamine, 4-nitro-N-phenyl-"] == "4-NDPA"
	assert friendly_name_mapping["Benzenamine, 2-nitro-N-phenyl-"] == "2-NDPA"
	assert friendly_name_mapping["N,N'-Diethyl-N,N'-diphenylurea"] == "Ethyl Centralite"
	assert friendly_name_mapping["Benzene, nitro-"] == "Nitrobenzene"
	assert friendly_name_mapping["Benzene, 2-methyl-1,3-dinitro-"] == "2,6-DNT"
	assert friendly_name_mapping["Benzene, 1-methyl-2,3-dinitro-"] == "2,3-DNT"
	assert friendly_name_mapping["Benzene, 1-methyl-2,4-dinitro-"] == "2,4-DNT"
	assert friendly_name_mapping["Phenol, 2-nitro-"] == "2-Nitrophenol"
	assert friendly_name_mapping["Benzene, 1-methyl-4-nitro-"] == "4-Nitrotoluene"
	assert friendly_name_mapping["Benzene, 1-methyl-3-nitro-"] == "3-Nitrotoluene"
	assert friendly_name_mapping["Benzene, 1-methyl-2-nitro-"] == "2-Nitrotoluene"
	assert friendly_name_mapping["Benzenamine, N-ethyl-N-nitroso-"] == "N-Nitroso-N-ethylaniline"
	assert friendly_name_mapping["Phenol, 4-methyl-2-nitro-"] == "4-Methyl-2-nitrophenol"
	assert friendly_name_mapping["Diphenylamine"] == "Diphenylamine"
