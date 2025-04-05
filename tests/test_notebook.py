import pytest
import Mixed_Language_Demo as databrics_code # Import the module
def test_dataframe_creation():
"""
Test for the `create_dataframe` function
"""
# Create the DataFrame
df = databrics_code.create_dataframe()
# Verify the DataFrame structure
assert df is not None
assert len(df) == 3 # Three rows
assert "Name" in df.columns

assert list(df["Name"]) == ["Amar", "Akbar", "Anthony"]
def test_dataframe_summary():
"""
Test the `print_dataframe_summary` function
"""
# Create the DataFrame
df = databrics_code.create_dataframe()
# Ensure no exceptions are raised during summary printing
try:
databrics_code.print_dataframe_summary(df)
except Exception as e:
pytest.fail(f"Summary printing failed with error: {e}")
