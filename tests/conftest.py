import pytest
from myfood.app import create_app

@pytest.fixture(scope='module')
def app():
  """instace of Main flask app"""
  return create_app()
