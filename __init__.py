# This file is part of account_reconcile_different_party module for Tryton.
# The COPYRIGHT file at the top level of this repository contains
# the full copyright notices and license terms.
from trytond.pool import Pool
from .account import *
from .move import *


def register():
    Pool.register(
        Account,
        Reconciliation,
        module='account_reconcile_different_party', type_='model')
