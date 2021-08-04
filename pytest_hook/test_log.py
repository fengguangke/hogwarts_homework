import pytest
import logging
from pytest_log.log import logger


@pytest.mark.parametrize('name',['张三','李四','王五'])
def test_log(name):
    logger.info(name)


