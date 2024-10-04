from odoo import models, fields
class Visitor(models.Model):
 # _name = 'wrms.visitor'
 _description = 'Visitor'
 _inherit = 'res.partner'
 # name = fields.Char(string='Full Name', required=True)
 age = fields.Integer(string='Age')
 party_id = fields.Many2one(
  comodel_name = 'wrms.party', string='Party',
 )
 raft_id = fields.Many2one(
  comodel_name='wrms.raft', string='Raft',
 )
 trip_id = fields.Many2one(
  comodel_name='wrms.trip', string='Trip'
 )
 booking_id = fields.Many2one(
  comodel_name='wrms.booking', string='Booking',
 )


# class Partner(models.Model):
#  _name = 'wrms.partner'
#  _description = 'Partner'
#  _inherit = 'res.partner'
#
#  name = fields.Char(string='Full Name', required=True)
#  age = fields.Integer(string='Age', required=True)
#  party_id = fields.Many2one(
#   comodel_name = 'wrms.party', string='Party',
#  )
#  raft_id = fields.Many2one(
#   comodel_name='wrms.raft', string='Raft',
#  )
#  trip_id = fields.Many2one(
#   comodel_name='wrms.trip', string='Trip'
#  )
#  booking_id = fields.Many2one(
#   comodel_name='wrms.booking', string='Booking',
#  )