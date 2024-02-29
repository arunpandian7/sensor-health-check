from abc import ABC
import polars as pl
from health_analyzer.data.schema import sensor_lookup_schema, sensor_reading_schema

class BaseDataInterface(ABC):
    def __init__(self) -> None:
        self.sensor_lookup_df = pl.DataFrame(schema=sensor_lookup_schema)
        self.sensors_df = pl.DataFrame(schema=sensor_reading_schema)
        super().__init__()

    def load_data_df(self):
        raise NotImplementedError

    def save_data_df(self):
        raise NotImplementedError


class CSVInterface(BaseDataInterface):
    def load_data_df(self, sensors_data_path, lookup_data_path):
        self.sensors_df = pl.read_csv(sensors_data_path, schema=sensor_reading_schema)
        self.sensor_lookup_df = pl.read_csv(lookup_data_path, schema=sensor_lookup_schema)
        return self

