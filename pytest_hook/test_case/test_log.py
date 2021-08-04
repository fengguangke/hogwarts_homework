import pytest
import logging
import time
from pytest_log.log import logger

@pytest.mark.parametrize('name',['张三','李四','王五'])
def test_log(name,request):
    logger.info(request.config.rootdir)
    logger.info(request.config.rootpath)
    logger.info(name)


