from pydantic import BaseModel


class SensorReading(BaseModel):
    vendor_id: str
    machine_id: str
    sensor_id: str
    sensor_value: int


class SensorLookUp(BaseModel):
    class_type: str
    lower_limit: int
    higher_limit: int
    cost: int
