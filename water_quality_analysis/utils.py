from .models import WaterQualityParameters


def check_water_quality(params: WaterQualityParameters) -> dict:
    """Checks water quality parameters and returns a dictionary with status messages, excluding None values."""
    results = {}
    if params.temperature is not None:
        results["temperature"] = (
            "Temperature is within the normal range (0°C to 35°C)."
            if 0 <= params.temperature <= 35
            else "Temperature is outside the normal range."
        )
    if params.dissolved_oxygen is not None:
        results["dissolved_oxygen"] = (
            "Dissolved oxygen is within the normal range (5 to 14 mg/L)."
            if 5 <= params.dissolved_oxygen <= 14
            else "Dissolved oxygen is outside the normal range."
        )
    if params.conductivity is not None:
        results["conductivity"] = (
            "Conductivity is within the normal range (50 to 1500 µS/cm)."
            if 50 <= params.conductivity <= 1500
            else "Conductivity is outside the normal range."
        )
    if params.turbidity is not None:
        results["turbidity"] = (
            "Turbidity is within the normal range (0 to 5 NTU)."
            if 0 <= params.turbidity <= 5
            else "Turbidity is outside the normal range."
        )
    if params.ph is not None:
        results["ph"] = (
            "pH is within the normal range (6.5 to 8.5)."
            if 6.5 <= params.ph <= 8.5
            else "pH is outside the normal range."
        )
    return results
