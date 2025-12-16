import platform
import distro
import subprocess
import sys


if platform.system() == "Linux":
    print(distro.name(pretty=True))
else:
    pass
    
