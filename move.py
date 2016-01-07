# This file is part of account_reconcile_different_party module for Tryton.
# The COPYRIGHT file at the top level of this repository contains
# the full copyright notices and license terms.
from trytond.pool import PoolMeta
from trytond.model import fields

__all__ = ['Line', 'Reconciliation']
__metaclass__ = PoolMeta


class Line():
    __name__ = 'account.move.line'

    @classmethod
    def __setup__(cls):
        super(Line, cls).__setup__()
        if cls.party.states.get('invisible'):
            cls.party.states.pop('invisible')

    @fields.depends('party')
    def on_change_account(self):
        party = self.party
        super(Line, self).on_change_account()
        # Not remove party if account is not party required
        if party:
            self.party = party

    def check_account(self):
        try:
            super(Line, self).check_account()
        except:
            # Not raise if there is a party and account is not party required
            if self.account.party_required or not self.party:
                raise


class Reconciliation():
    __name__ = 'account.move.reconciliation'

    @classmethod
    def check_lines(cls, reconciliations):
        for reconciliation in reconciliations:
            for line in reconciliation.lines:
                if line.account.different_party_reconcile:
                    line.party = None
        super(Reconciliation, cls).check_lines(reconciliations)
