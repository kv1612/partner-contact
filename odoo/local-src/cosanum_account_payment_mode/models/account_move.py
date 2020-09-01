# Copyright 2020 Camptocamp SA
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html)

from odoo import api, models


class AccountMove(models.Model):
    _inherit = "account.move"

    @api.depends("partner_id", "payment_mode_id")
    def _compute_invoice_partner_bank(self):
        super()._compute_invoice_partner_bank()
        for move in self:
            bank = move._get_payment_mode_bank_id()
            if bank:
                move.invoice_partner_bank_id = bank
        return

    @api.onchange("partner_id")
    def _onchange_partner_id(self):
        """On change partner set invoice_partner_bank.

        The compute method aboves should be enough but it is not called in the
        form when the partner_id chagnes (it works with the OCA module, alone !?)

        So this onchange fixes that.
        """
        res = super()._onchange_partner_id()
        bank = self._get_payment_mode_bank_id()
        if bank:
            self.invoice_partner_bank_id = bank
        return res

    def _get_payment_mode_bank_id(self):
        """Get the bank account linked to the selected payment mode.

        Only the fixed payment mode link type is used by Cosanum so no specific
        code for the variable type, needed.
        """
        self.ensure_one()
        if (
            self.partner_id
            and self.payment_mode_id
            and self.type == "out_invoice"
        ):
            return self.payment_mode_id.fixed_journal_id.bank_account_id
        else:
            return None
