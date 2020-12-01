# -*- mode: python ; coding: utf-8 -*-

block_cipher = None

modulo1 = open("modulo_1.txt", "r").readlines()
modulo2 = open("modulo_2.txt", "r").readlines()
exclude1 = [i.replace("\n", "") for i in modulo1]
exclude2 = [i.replace("\n", "") for i in modulo2]

modulos_excluidos = list(set(exclude1) | set(exclude2))

a = Analysis(['script.py'],
             pathex=['D:\\CursoPyQt\\whatspy'],
             binaries=[],
             datas=[],
             hiddenimports=[],
             hookspath=[],
             runtime_hooks=[],
             excludes=modulos_excluidos,
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher,
             noarchive=False)
pyz = PYZ(a.pure, a.zipped_data,
             cipher=block_cipher)
exe = EXE(pyz,
          a.scripts,
          [],
          exclude_binaries=True,
          name='script',
          debug=False,
          bootloader_ignore_signals=False,
          strip=False,
          upx=True,
          console=True )
coll = COLLECT(exe,
               a.binaries,
               a.zipfiles,
               a.datas,
               strip=False,
               upx=True,
               upx_exclude=[],
               name='script')
