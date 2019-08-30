#!env python3
# -*- coding: utf-8 -*-
import logging

logger = logging.getLogger()
logging.basicConfig(level=logging.CRITICAL)
logger.debug("hello")
logger.info("world")
logger.warning("python")
logger.error("standard")
logger.critical("library")
