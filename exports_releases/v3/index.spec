# -*- mode: python ; coding: utf-8 -*-

block_cipher = None


a = Analysis(['C:/Users/sergi/Desktop/exe/index.py'],
             pathex=['C:\\Users\\sergi\\Desktop\\exe'],
             binaries=[],
             datas=[('C:/Users/sergi/Desktop/exe/chess_notations.py', '.'), ('C:/Users/sergi/Desktop/exe/pieces.py', '.')],
             hiddenimports=['pygame', 'PIL', 'numpy', 'copy', 'sys', 'math'],
             hookspath=[],
             runtime_hooks=[],
             excludes=[],
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher,
             noarchive=False)
pyz = PYZ(a.pure, a.zipped_data,
             cipher=block_cipher)
exe = EXE(pyz,
          a.scripts,
          a.binaries,
          a.zipfiles,
          a.datas,
          [],
          name='index',
          debug=False,
          bootloader_ignore_signals=False,
          strip=False,
          upx=True,
          upx_exclude=[],
          runtime_tmpdir=None,
          console=False , icon='C:\\Users\\sergi\\Desktop\\exe\\images\\ico.ico')
