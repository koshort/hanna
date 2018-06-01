# -*- coding: utf-8 -*-
from hanna import translit
from hanna.cgi import Translit

def test_translit():
    translit(u"かみ")

def test_cgi_translit():
    t = Translit()
    t.ja(u"さくらがさくよ")