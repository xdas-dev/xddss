# xddss/__init__.py

import sys
import importlib
import types
import xdas

sys.modules[__name__] = xdas

def mirror_submodule(name):
    try:
        module = importlib.import_module(name)
        alias = name.replace("xdas", "xddss", 1)
        sys.modules[alias] = module
        return module
    except ImportError:
        raise AttributeError(f"Module {name} not found")

def __getattr__(name):
    # Called for xddss.<name>
    fqname = f"xdas.{name}"
    return mirror_submodule(fqname)

def __dir__():
    return dir(xdas)

# Needed for nested submodules like xddss.io.asn to work
__path__ = xdas.__path__
