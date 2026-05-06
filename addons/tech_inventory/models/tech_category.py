from odoo import models, fields, api

class TechCategory(models.Model):
    _name = 'tech.category'
    _description = 'Categoría de Equipo Tecnológico'
    _order = 'name'

    name = fields.Char(string='Nombre', required=True)
    description = fields.Text(string='Descripción')
    
    equipment_count = fields.Integer(
        string='Cantidad de Equipos',
        compute='_compute_equipment_count'
    )

    @api.depends('name')
    def _compute_equipment_count(self):
        for category in self:
            category.equipment_count = self.env['tech.equipment'].search_count([
                ('category_id', '=', category.id)
            ])
