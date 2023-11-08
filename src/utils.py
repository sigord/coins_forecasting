"""Defines utility functions and classes"""
import logging
import logging.config

from functools import wraps, reduce

import yaml

CONF_LOGGER_PATH = "conf/logging.conf"
CONF_MAIN_PATH = "conf/conf.yaml"

logging.config.fileConfig(CONF_LOGGER_PATH)
logger = logging.getLogger("root")


def log(func):
    """
    Decorator to log function calls and exceptions
    """
    @wraps(func)
    def wrapper(*args, **kwargs):
        args_repr = [repr(a) for a in args]
        kwargs_repr = [f"{k}={v!r}" for k, v in kwargs.items()]
        signature = ", ".join(args_repr + kwargs_repr)
        logger.debug(
            f"function {func.__name__} called with args {signature}"
        )
        try:
            result = func(*args, **kwargs)
            return result
        except Exception as e:
            logger.exception(
                f"Exception raised in {func.__name__}. exception: {str(e)}"
            )
            raise e
    return wrapper


class DotDict(dict):
    """
    Dot notation access to dictionary attributes
    source: 
    https://stackoverflow.com/questions/39463936/python-accessing-yaml-values-using-dot-notation
    """
    # update, __setitem__ etc. omitted, but required if
    # one tries to set items using dot notation. Essentially
    # this is a read-only view.

    def __getattribute__(self, k):
        try:
            v = self[k]
        except KeyError:
            return super().__getattribute__(k)
        if isinstance(v, dict):
            return DotDict(v)
        return v

    def __getitem__(self, k):
        if isinstance(k, str) and '.' in k:
            k = k.split('.')
        if isinstance(k, (list, tuple)):
            return reduce(lambda d, kk: d[kk], k, self)
        return super().__getitem__(k)

    def get(self, k, default=None):
        if isinstance(k, str) and '.' in k:
            try:
                return self[k]
            except KeyError:
                return default
        return super().get(k, default=default)


class Config(DotDict):
    """
    Provides access to configuration file in dot notation
    """

    def __init__(self, path):
        with open(path, mode='r') as file:
            super().__init__(yaml.safe_load(file))


conf = Config(CONF_MAIN_PATH)
