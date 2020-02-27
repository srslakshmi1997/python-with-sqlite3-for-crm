from cx_Freeze import setup,Executable
import sys
import os

build_exe_options={"packages":['sqlite3','sys','os','prettytable','re','textwrap'],'include_files':[(os.path.join(os.path.abspath('C:\Python27'), 'DLLs', 'sqlite3.dll'),'sqlite3.dll')]} 

setup(
    name="CRM",
    version='0.1',
    description='CRM',
    options={"build_exe":build_exe_options},
    executables=[Executable(script="CRMv2.py",icon="CRM.ico")])
