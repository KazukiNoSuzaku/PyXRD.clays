# -*- mode: python ; coding: utf-8 -*-
import os
from pathlib import Path

src = Path('data/lib/python3.8/site-packages')

# Collect all pyxrd and mvc data files (.ui, .png, .svg, .csv, etc.)
datas = []

for ext in ('*.ui', '*.png', '*.svg', '*.ico', '*.csv', '*.json', '*.lbl'):
    for f in src.rglob(ext):
        rel = f.parent.relative_to(src)
        datas.append((str(f), str(rel)))

a = Analysis(
    ['launcher.py'],
    pathex=[str(src)],
    binaries=[],
    datas=datas,
    hiddenimports=[
        'pyxrd',
        'mvc',
        'PySide6.QtCore',
        'PySide6.QtGui',
        'PySide6.QtWidgets',
        'PySide6.QtUiTools',
        'matplotlib.backends.backend_qtagg',
        'matplotlib.backends.backend_qt',
        'numpy',
    ],
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=['gtk', 'gi', 'cairo', 'Gtk', 'scipy'],
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
    console=False,  # No console window
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
