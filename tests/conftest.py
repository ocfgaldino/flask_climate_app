import pytest
from climate.app import create_app

@pytest.fixture(scope="module")
def app():
    """Instance of Main Flask APP"""
    return create_app()