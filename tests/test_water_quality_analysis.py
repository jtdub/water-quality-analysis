from wqautils.models import (
    WaterQualityParameters,
    WaterQualityResult,
)
from wqautils.utils import check_water_quality


def test_check_water_quality_valid():
    params = WaterQualityParameters(
        temperature=20, dissolved_oxygen=8, conductivity=500, turbidity=2, ph=7
    )
    results = check_water_quality(params)
    assert results.temperature.status == "OK"
    assert results.dissolved_oxygen.status == "OK"


def test_check_water_quality_invalid():
    params = WaterQualityParameters(
        temperature=50, dissolved_oxygen=2, conductivity=2000, turbidity=10, ph=5
    )
    results = check_water_quality(params)
    assert results.temperature.status == "Alert"
    assert results.dissolved_oxygen.status == "Alert"


def test_partial_parameters():
    params = WaterQualityParameters(temperature=25)
    results = check_water_quality(params)
    assert results.temperature is not None
    assert results.dissolved_oxygen is None


def test_all_parameters():
    params = WaterQualityParameters(
        temperature=20,
        dissolved_oxygen=8,
        conductivity=500,
        turbidity=2,
        ph=7,
        salinity=30,
        ammonia=0.02,
        nitrate=5,
        nitrite=0.5,
        phosphate=0.05,
        tds=500,
        chlorine=1,
        hardness=100,
        alkalinity=100,
    )
    results = check_water_quality(params)
    assert all(
        isinstance(getattr(results, attr), WaterQualityResult)
        for attr in [
            "temperature",
            "dissolved_oxygen",
            "conductivity",
            "turbidity",
            "ph",
            "salinity",
            "ammonia",
            "nitrate",
            "nitrite",
            "phosphate",
            "tds",
            "chlorine",
            "hardness",
            "alkalinity",
        ]
    )
