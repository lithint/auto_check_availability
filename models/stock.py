from openerp import api
from openerp.osv import osv, fields

class StockMove(osv.osv):
    _inherit = 'stock.move'


    #If this is a newly created picking in confirmed state
    #Do the obvious, seriously.
    @api.cr_uid_ids_context
    def _picking_assign(self, cr, uid, move_ids, procurement_group, \
		location_from, location_to, context=None):
	picking_obj = self.pool.get('stock.picking')

        res = super(StockMove, self)._picking_assign(cr, uid, move_ids, procurement_group, \
		location_from, location_to, context=context)

	moves = self.browse(cr, uid, move_ids)
	if moves[0].picking_id and moves[0].picking_id.state == 'confirmed':
	    picking_obj.action_assign(cr, uid, [moves[0].picking_id.id])

	return res
