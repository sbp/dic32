#!/usr/bin/env python3

import distutils.core
import os.path
import sys

def generate_version(epoch, recent):
    elapsed = recent - epoch
    years, elapsed = divmod(elapsed, 365.25 * 24 * 3600)
    days, elapsed = divmod(elapsed, 24 * 3600)
    minutes = elapsed // 60
    return "%i.%i.%i" % (years, days, minutes)

if __name__ == "__main__":
    README = "https://github.com/sbp/dic32/blob/master/README.md"

    if os.path.isfile("dic32"):
        recent = max(os.path.getmtime(name) for name in ["dic32", "setup.py"])
        version = generate_version(1423737313, recent)
    else:
        print("Unable to find dic32 script: refusing to install")
        sys.exit(1)

    distutils.core.setup(
        name="dic32",
        version=version,
        author="Sean B. Palmer",
        url="https://github.com/sbp/dic32",
        description="Data integrity checker",
        long_description="Documented in `@sbp/dic32/README.md <%s>`_" % README,
        scripts=["dic32"],
        platforms="Linux and OS X",
        classifiers=[
            "Operating System :: MacOS :: MacOS X",
            "Operating System :: POSIX",
            "Programming Language :: Python :: 3"
        ]
    )
