import functools
import os
import sys
import warnings
from math import ceil
from operator import itemgetter
from threading import Lock
from time import perf_counter

import sqlalchemy
from flask import _app_ctx_stack
from flask import abort
from flask import current_app
from flask import request
from flask.signals import Namespace
from sqlalchemy import event
from sqlalchemy import inspect
from sqlalchemy import orm
from sqlalchemy.engine.url import make_url
from sqlalchemy.orm.exc import UnmappedClassError
from sqlalchemy.orm.session import Session as SessionBase

from .model import DefaultMeta
from .model import Model

try:
    from sqlalchemy.orm import declarative_base
    from sqlalchemy.orm import DeclarativeMeta
except ImportError:
    # SQLAlchemy <= 1.3
    from sqlalchemy.ext.declarative import declarative_base
    from sqlalchemy.ext.declarative import DeclarativeMeta

# Scope the session to the current greenlet if greenlet is available,
# otherwise fall back to the current thread.
