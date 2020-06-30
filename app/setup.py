# -*- coding: utf-8 -*-

from distutils.core import setup 
import py2exe 
 
setup(name="Scan-PC", 
 version="1.0", 
 description="Escaneo de equipos", 
 author="Leonardo", 
 author_email="leo.munoz.lobos@gmail.com", 
 url="url del proyecto", 
 license="free", 
 scripts=["scan.py"], 
 console=["scan.py"], 
 options={"Py2Exe": {"bundle_files": 1}}, 
 zipfile=None,
)