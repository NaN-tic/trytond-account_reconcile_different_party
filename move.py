# This file is part of account_reconcile_different_party module for Tryton.
# The COPYRIGHT file at the top level of this repository contains
# the full copyright notices and license terms.
from trytond.pool import PoolMeta

__all__ = ['Reconciliation']
__metaclass__ = PoolMeta


class Reconciliation():
    __name__ = 'account.move.reconciliation'

    @classmethod
    def check_lines(cls, reconciliations):
        for reconciliation in reconciliations:
            for line in reconciliation.lines:
                if line.account.different_party_reconcile:
                    line.party = None
        super(Reconciliation, cls).check_lines(reconciliations)
