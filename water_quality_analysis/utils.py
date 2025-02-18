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
    if params.salinity is not None:
        results["salinity"] = (
            "Salinity is within normal levels (0 to 35 PSU)."
            if 0 <= params.salinity <= 35
            else "Salinity is outside the normal range."
        )
    if params.ammonia is not None:
        results["ammonia"] = (
            "Ammonia is within safe levels (0 to 0.05 mg/L)."
            if 0 <= params.ammonia <= 0.05
            else "Ammonia is outside safe levels and can be toxic."
        )
    if params.nitrate is not None:
        results["nitrate"] = (
            "Nitrate is within safe levels (0 to 10 mg/L)."
            if 0 <= params.nitrate <= 10
            else "Nitrate is outside safe levels and can cause eutrophication."
        )
    if params.nitrite is not None:
        results["nitrite"] = (
            "Nitrite is within safe levels (0 to 1 mg/L)."
            if 0 <= params.nitrite <= 1
            else "Nitrite is outside safe levels and can harm aquatic life."
        )
    if params.phosphate is not None:
        results["phosphate"] = (
            "Phosphate is within safe levels (0 to 0.1 mg/L)."
            if 0 <= params.phosphate <= 0.1
            else "Phosphate is outside safe levels and can cause eutrophication."
        )
    if params.tds is not None:
        results["tds"] = (
            "TDS is within acceptable range (0 to 1000 mg/L)."
            if 0 <= params.tds <= 1000
            else "TDS is outside acceptable range."
        )
    if params.chlorine is not None:
        results["chlorine"] = (
            "Chlorine is within safe levels (0 to 4 mg/L)."
            if 0 <= params.chlorine <= 4
            else "Chlorine is outside safe levels and can be toxic."
        )
    if params.hardness is not None:
        results["hardness"] = (
            "Hardness is within acceptable levels (0 to 180 mg/L)."
            if 0 <= params.hardness <= 180
            else "Hardness is outside acceptable levels."
        )
    if params.alkalinity is not None:
        results["alkalinity"] = (
            "Alkalinity is within acceptable range (20 to 200 mg/L)."
            if 20 <= params.alkalinity <= 200
            else "Alkalinity is outside acceptable range."
        )
    return results
