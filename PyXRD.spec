# -*- mode: python ; coding: utf-8 -*-
import os, sys
from pathlib import Path
from PyInstaller.utils.hooks import collect_submodules, collect_data_files, collect_all

# Use absolute path so spec works regardless of cwd
SPEC_DIR = os.path.dirname(os.path.abspath(SPEC))
src = Path(SPEC_DIR) / 'data' / 'lib' / 'python3.8' / 'site-packages'

# Add src to sys.path so collect_submodules/collect_data_files can find pyxrd/mvc
if str(src) not in sys.path:
    sys.path.insert(0, str(src))

# Collect all pyxrd and mvc data files (.ui, .png, .svg, .csv, etc.)
datas = []
for ext in ('*.ui', '*.png', '*.svg', '*.ico', '*.csv', '*.json', '*.lbl'):
    for f in src.rglob(ext):
        rel = f.parent.relative_to(src)
        datas.append((str(f), str(rel)))

# Collect numpy and scipy fully (C-extensions need special handling)
numpy_datas, numpy_binaries, numpy_hidden = collect_all('numpy')
scipy_datas, scipy_binaries, scipy_hidden = collect_all('scipy')
datas += numpy_datas + scipy_datas

# Collect all submodules so nothing is missed
hidden = (
    collect_submodules('pyxrd') +
    collect_submodules('mvc') +
    numpy_hidden +
    scipy_hidden +
    [
        'PySide6.QtCore',
        'PySide6.QtGui',
        'PySide6.QtWidgets',
        'PySide6.QtUiTools',
        'matplotlib.backends.backend_qtagg',
        'matplotlib.backends.backend_qt',
    ]
)

a = Analysis(
    ['launcher.py'],
    pathex=[str(src)],
    binaries=numpy_binaries + scipy_binaries,
    datas=datas,
    hiddenimports=hidden,
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=['gtk', 'gi', 'cairo', 'Gtk', 'pkg_resources', 'setuptools', 'Pyro4', 'pytest', '_pytest'],
    noarchive=False,
    optimize=0,
)

pyz = PYZ(a.pure)

exe = EXE(
    pyz,
    a.scripts,
    [],
    exclude_binaries=True,
    name='PyXRD',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    console=False,
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
    icon=None,
)

coll = COLLECT(
    exe,
    a.binaries,
    a.datas,
    strip=False,
    upx=True,
    upx_exclude=[],
    name='PyXRD',
)
