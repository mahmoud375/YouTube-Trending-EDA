import pandas as pd
import numpy as np
import pytest
from io import StringIO

from pathlib import Path
import sys

project_root = Path(__file__).resolve().parent.parent
sys.path.append(str(project_root))

from src.preprocessing.data_utils import (
    load_data,
    explore_data,
    unique_values_with_counts,
    handle_missing_values,
    encode_categorical,
    drop_columns,
    convert_to_datetime,
    save_table
)

@pytest.fixture
def dummy_df():
    return pd.DataFrame({
        "A": [1, 2, np.nan, 4],
        "B": ["x", "y", "x", None],
        "C": [10, 20, 30, 40],
    })

def test_unique_values_with_counts(dummy_df):
    result = unique_values_with_counts(dummy_df, "B")
    assert result["x"] == 2
    assert result["y"] == 1

def test_handle_missing_mean(dummy_df):
    filled = handle_missing_values(dummy_df, strategy="mean")
    assert not filled.isnull().any().any()
    assert filled.loc[2, "A"] == pytest.approx((1 + 2 + 4) / 3)

def test_handle_missing_differentiated(dummy_df):
    filled = handle_missing_values(dummy_df, strategy="differentiated")
    assert not filled.isnull().any().any()
    assert filled.loc[2, "A"] == 2.0  # median of [1, 2, 4]
    assert filled.loc[3, "B"] == "x"  # mode of ["x", "y", "x"]

def test_encode_categorical(dummy_df):
    encoded = encode_categorical(dummy_df)
    assert np.issubdtype(encoded["B"].dtype, np.integer)

def test_drop_columns(dummy_df):
    dropped = drop_columns(dummy_df, ["B", "D"])  # D doesn't exist
    assert "B" not in dropped.columns
    assert "A" in dropped.columns

def test_convert_to_datetime():
    df = pd.DataFrame({"date": ["25.01.06", "23.15.05"]})
    converted = convert_to_datetime(df, "date", "%y.%d.%m")
    assert np.issubdtype(converted["date"].dtype, np.datetime64)
    assert converted["date"].iloc[0].year == 2025

def test_save_table_csv(tmp_path):
    df = pd.DataFrame({"a": [1, 2], "b": ["x", "y"]})
    path = tmp_path / "test_output"
    save_table(df, str(path), format="csv")
    loaded = pd.read_csv(f"{path}.csv")
    pd.testing.assert_frame_equal(df, loaded)

def test_load_data():
    sample_csv = "col1,col2\n1,x\n2,y"
    df = load_data(StringIO(sample_csv))
    assert df.shape == (2, 2)
    assert list(df.columns) == ["col1", "col2"]

def test_handle_missing_invalid_strategy(dummy_df):
    with pytest.raises(ValueError):
        handle_missing_values(dummy_df, strategy="invalid")

def test_unique_values_column_not_found(dummy_df):
    with pytest.raises(ValueError):
        unique_values_with_counts(dummy_df, "Z")
