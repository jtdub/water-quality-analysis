from .models import WaterQualityParameters

def check_water_quality(params: WaterQualityParameters) -> dict:
    """Checks water quality parameters and returns a dictionary with status messages."""
    results = {}
    if 0 <= params.temperature <= 35:
        results["temperature"] = "Temperature is within the normal range (0°C to 35°C)."
    else:
        results["temperature"] = (
            "Temperature is outside the normal range. Extreme temperatures can harm aquatic life."
        )

    if 5 <= params.dissolved_oxygen <= 14:
        results["dissolved_oxygen"] = (
            "Dissolved oxygen is within the normal range (5 to 14 mg/L)."
        )
    else:
        results["dissolved_oxygen"] = (
            "Dissolved oxygen is outside the normal range. This can affect aquatic life."
        )

    if 50 <= params.conductivity <= 1500:
        results["conductivity"] = (
            "Conductivity is within the normal range (50 to 1500 µS/cm)."
        )
    else:
        results["conductivity"] = (
            "Conductivity is outside the normal range, possibly indicating pollution."
        )

    if 0 <= params.turbidity <= 5:
        results["turbidity"] = "Turbidity is within the normal range (0 to 5 NTU)."
    else:
        results["turbidity"] = (
            "Turbidity is outside the normal range, which affects aquatic organisms."
        )

    if 6.5 <= params.ph <= 8.5:
        results["ph"] = "pH is within the normal range (6.5 to 8.5)."
    else:
        results["ph"] = (
            "pH is outside the normal range, potentially harmful to aquatic life."
        )

    return results
