# -*- coding: utf-8 -*-
#
# Electrum - lightweight STRAKS client
# Copyright (C) 2018 The Electrum developers
#
# Permission is hereby granted, free of charge, to any person
# obtaining a copy of this software and associated documentation files
# (the "Software"), to deal in the Software without restriction,
# including without limitation the rights to use, copy, modify, merge,
# publish, distribute, sublicense, and/or sell copies of the Software,
# and to permit persons to whom the Software is furnished to do so,
# subject to the following conditions:
#
# The above copyright notice and this permission notice shall be
# included in all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND,
# EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF
# MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND
# NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS
# BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN
# ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN
# CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

import os
import json


def read_json(filename, default):
    path = os.path.join(os.path.dirname(__file__), filename)
    try:
        with open(path, 'r') as f:
            r = json.loads(f.read())
    except:
        r = default
    return r


class STRAKS_Mainnet:

    TESTNET = False
    WIF_PREFIX = 0xcc
    ADDRTYPE_P2PKH = 63
    ADDRTYPE_P2SH = 5
    SEGWIT_HRP = "stak"
    GENESIS = "00000df14d859c4b3219d93978bcf02afc123d2344a2ed39033e1208948aa7c0"
    DEFAULT_PORTS = {'t': '50001', 's': '50002'}
    DEFAULT_SERVERS = read_json('servers.json', {})
    CHECKPOINTS = read_json('checkpoints.json', [])

    # Version numbers for BIP32 extended keys
    # standard: xprv, xpub
    # segwit in p2sh: yprv, ypub
    # native segwit: zprv, zpub
    XPRV_HEADERS = {
        'standard': 0x0488ade4,
        'p2wpkh-p2sh': 0x049d7878,
        'p2wsh-p2sh': 0x295b005,
        'p2wpkh': 0x4b2430c,
        'p2wsh': 0x2aa7a99
    }
    XPUB_HEADERS = {
        'standard': 0x0488b21e,
        'p2wpkh-p2sh': 0x049d7cb2,
        'p2wsh-p2sh': 0x295b43f,
        'p2wpkh': 0x4b24746,
        'p2wsh': 0x2aa7ed3
    }


class STRAKS_Testnet:

    TESTNET = True
    WIF_PREFIX = 0xef
    ADDRTYPE_P2PKH = 127
    ADDRTYPE_P2SH = 19
    SEGWIT_HRP = "tstak"
    GENESIS = "000000cd747bd0b653e1fe417b60c1d9e990600cf2ff193404ea12c3ecb348b4"
    DEFAULT_PORTS = {'t': '51001', 's': '51002'}
    DEFAULT_SERVERS = read_json('servers_testnet.json', {})
    CHECKPOINTS = read_json('checkpoints_testnet.json', [])

    XPRV_HEADERS = {
        'standard':    0x46002A10,  # tprv
        'p2wpkh-p2sh': 0x044a4e28,  # uprv
        'p2wsh-p2sh':  0x024285b5,  # Uprv
        'p2wpkh':      0x045f18bc,  # vprv
        'p2wsh':       0x02575048,  # Vprv
    }
    XPUB_HEADERS = {
        'standard':    0xA2AEC9A6,  # tpub
        'p2wpkh-p2sh': 0x044a5262,  # upub
        'p2wsh-p2sh':  0x024289ef,  # Upub
        'p2wpkh':      0x045f1cf6,  # vpub
        'p2wsh':       0x02575483,  # Vpub
    }


class STRAKS_Regtest(STRAKS_Testnet):

    SEGWIT_HRP = "stakrt"
    GENESIS = "000002db0642636c786f756062dd7a92f35a2be1665816f8bfa33111ae902b37"
    DEFAULT_SERVERS = read_json('servers_regtest.json', {})
    CHECKPOINTS = []


# don't import net directly, import the module instead (so that net is singleton)
net = STRAKS_Mainnet


def set_mainnet():
    global net
    net = STRAKS_Mainnet


def set_testnet():
    global net
    net = STRAKS_Testnet


def set_regtest():
    global net
    net = STRAKS_Regtest
