# coding: utf-8

"""
Utilidades para subir archivos al servidor

"""


from fabric.operations import put
from fabric.api import *
import os

env.user = 'lm'

env.hosts = ['178.32.253.90']

def subir():
    destino = "/usr/share/nginx/html/programas/"
    put("index.html", destino, use_sudo=True)
    put("programas_redined.js", destino, use_sudo=True)

