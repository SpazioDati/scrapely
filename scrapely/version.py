try:
    from ._version import version as __version__
except ImportError:
    # Package is not installed, try to get version from git
    try:
        from setuptools_scm import get_version
        __version__ = get_version(root='..', relative_to=__file__)
    except (ImportError, LookupError):
        __version__ = '0.0.0.dev0'
