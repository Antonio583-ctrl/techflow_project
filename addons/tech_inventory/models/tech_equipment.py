from odoo import models, fields, api, _
from odoo.exceptions import ValidationError

class TechEquipment(models.Model):
    _name = 'tech.equipment'
    _description = 'Equipo Tecnológico'
    _order = 'name'
    _rec_name = 'name'

    name = fields.Char(string='Nombre del Equipo', required=True)
    serial = fields.Char(
        string='Número de Serie', 
        required=True, 
        unique=True,
        index=True
    )
    
    category_id = fields.Many2one(
        'tech.category', 
        string='Categoría',
        required=True,
        ondelete='restrict'
    )
    
    employee_id = fields.Many2one(
        'hr.employee', 
        string='Empleado Asignado',
    )
    
    state = fields.Selection([
        ('available', 'Disponible'),
        ('assigned', 'Asignado'),
        ('repair', 'En Reparación'),
        ('decommissioned', 'Desincorporado')
    ], string='Estado', required=True, default='available')
    
    cost = fields.Monetary(
        string='Costo (USD)', 
        currency_field='currency_id',
        required=True
    )
    
    tax_value = fields.Monetary(
        string='Valor con Impuesto (15%)',
        store=True,
        currency_field='currency_id'
    )
    
    currency_id = fields.Many2one(
        'res.currency', 
        default=lambda self: self.env.company.currency_id
    )
    
    notes = fields.Text(string='Notas Adicionales')
    purchase_date = fields.Date(string='Fecha de Compra')
    
    _sql_constraints = [
        ('serial_unique', 'unique(serial)', 'El número de serie debe ser único!')
    ]



