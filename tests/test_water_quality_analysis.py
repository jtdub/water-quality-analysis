from water_quality_analysis.models import WaterQualityParameters
from water_quality_analysis.utils import check_water_quality


def test_check_water_quality_valid():
    params = WaterQualityParameters(
        temperature=20, dissolved_oxygen=8, conductivity=500, turbidity=2, ph=7
    )
    results = check_water_quality(params)
    assert (
        results["temperature"]
        == "Temperature is within the normal range (0°C to 35°C)."
    )
    assert (
        results["dissolved_oxygen"]
        == "Dissolved oxygen is within the normal range (5 to 14 mg/L)."
    )


def test_check_water_quality_invalid():
    params = WaterQualityParameters(
        temperature=50, dissolved_oxygen=2, conductivity=2000, turbidity=10, ph=5
    )
    results = check_water_quality(params)
    assert "outside the normal range" in results["temperature"]
    assert "outside the normal range" in results["dissolved_oxygen"]
