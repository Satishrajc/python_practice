import pytest

# Define a fixture to set up and tear down a database connection
@pytest.fixture
def database_connection():
    # Code to set up the database connection
    connection = "Database Connection"
    yield connection  # The fixture yields the resource to the test function
    # Code to tear down the database connection
    print("Closing Database Connection")

# Test function using the "database_connection" fixture
def test_database_operations(database_connection):
    # Test logic that uses the database connection
    print(f"Performing Database Operations using {database_connection}")
    # The fixture will automatically handle setup and teardown
