from pydantic import BaseModel, Field


class WaterQualityParameters(BaseModel):
    """Pydantic model for water quality parameters with optional fields."""

    temperature: float | None = Field(None, description="Water temperature in Celsius.")
    dissolved_oxygen: float | None = Field(
        None, description="Dissolved oxygen in mg/L."
    )
    conductivity: float | None = Field(None, description="Conductivity in µS/cm.")
    turbidity: float | None = Field(None, description="Turbidity in NTU.")
    ph: float | None = Field(None, description="pH level.")
