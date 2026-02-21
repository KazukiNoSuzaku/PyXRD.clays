"""
PyXRD portable launcher.
Works both when run directly and when frozen by PyInstaller.
"""
import os
import sys

# When frozen by PyInstaller, sys._MEIPASS is the bundle directory.
# When run normally, we add the bundled site-packages to sys.path.
if getattr(sys, 'frozen', False):
    bundle_dir = sys._MEIPASS
    if bundle_dir not in sys.path:
        sys.path.insert(0, bundle_dir)
else:
    bundle_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)),
                              'data', 'lib', 'python3.8', 'site-packages')
    if bundle_dir not in sys.path:
        sys.path.insert(1, bundle_dir)

from pyxrd.core import run_main
run_main()
