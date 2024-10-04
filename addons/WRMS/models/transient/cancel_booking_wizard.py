from odoo import models, fields, api
from odoo.exceptions import UserError

class CancelBookingWizard(models.TransientModel):
    _name = 'cancel.booking.wizard'
    _description = 'Booking Cancel Confirmation'

    booking_id = fields.Many2one('wrms.booking', string='Booking', required=True)
    cancellation_reason = fields.Text(string='Cancellation Reason', required=True)


    def action_confirm_cancel(self):
        if self.cancellation_reason:
            self.booking_id.action_set_canceled()
            self.booking_id.write({'cancellation_reason': self.cancellation_reason})
            return {'type': 'ir.actions.act_window_close'}
        else:
            raise UserError("You must provide a reason for cancellation.")

    def action_cancel(self):
        return {'type': 'ir.actions.act_window_close'}