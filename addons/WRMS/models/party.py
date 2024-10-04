from odoo import models, fields
from odoo import api

class Party(models.Model):
 _name = 'wrms.party'
 _rec_name = 'party_no'
 _description = 'Party'

 party_no = fields.Char(string='Party Number', required=True)
 num_passengers = fields.Float(compute='_compute_num_guests',string='Number of Passengers')
 head_of_party = fields.Char(string="Head of Party", compute='_compute_head_of_party')
 has_kids = fields.Boolean(compute='_compute_kids', string='Has Kids?')
 visitor_ids = fields.One2many(
  comodel_name='res.partner', inverse_name='party_id', string='Guests', domain='[("is_company", "!=", True)]'
 )
 raft_id = fields.Many2one(
  comodel_name='wrms.raft', string='Raft'
 )
 trip_id = fields.Many2one(
  comodel_name='wrms.trip', string='Trip'
 )
 booking_ids = fields.One2many(
  comodel_name='wrms.booking', inverse_name='party_id', string='Booking'
 )

 @api.depends('visitor_ids')
 def _compute_num_guests(self):
  for party in self:
   party.num_passengers = len(party.visitor_ids)

 @api.depends('visitor_ids')
 def _compute_head_of_party(self):
  for party in self:
   party.head_of_party = ''
   if party.visitor_ids:
    party.head_of_party = party.visitor_ids[0].name

 @api.depends('visitor_ids')
 def _compute_kids(self):
  for party in self:
   party.has_kids = False
   for visitor in party.visitor_ids:
    if visitor.age<15:
     party.has_kids = True
     break

