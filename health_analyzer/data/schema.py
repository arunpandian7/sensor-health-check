import polars as pl

sensor_lookup_schema = {
    "sensor_class_type": pl.String,
    "lower_limit": pl.Int32,
    "higher_limit": pl.Int32,
    "cost": pl.Int64,
}

sensor_reading_schema = {
    "vendor_id": pl.String,
    "machine_id": pl.String,
    "sensor_id": pl.String,
    "sensor_value": pl.Int64
}
