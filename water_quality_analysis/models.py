from pydantic import BaseModel, Field


class WaterQualityParameters(BaseModel):
    """Pydantic model for water quality parameters with validation and descriptions."""

    temperature: float = Field(..., description="Water temperature in Celsius.")
    dissolved_oxygen: float = Field(..., description="Dissolved oxygen in mg/L.")
    conductivity: float = Field(..., description="Conductivity in µS/cm.")
    turbidity: float = Field(..., description="Turbidity in NTU.")
    ph: float = Field(..., description="pH level.")
