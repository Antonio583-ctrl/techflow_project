from odoo import models, fields, api

class TechRating(models.Model):
    _name = 'tech.rating'
    _description = 'Valoración de Equipo Tecnológico'
    _order = 'rating_date desc'

    equipment_id = fields.Many2one(
        'tech.equipment',
        string='Equipo',
        required=True,
        ondelete='cascade'
    )

    evaluated_by_id = fields.Many2one(
        'res.users',
        string='Evaluado Por',
        default=lambda self: self.env.user,
        required=True
    )

    rating_date = fields.Date(
        string='Fecha de Valoración',
        default=fields.Date.today,
        required=True
    )

    rating = fields.Selection([
        ('malo', 'Malo'),
        ('regular', 'Regular'),
        ('bueno', 'Bueno'),
        ('excelente', 'Excelente')
    ], string='Valoración', required=True)

    is_recommended = fields.Boolean(
        string='¿Recomendado?',
        compute='_compute_is_recommended',
        store=True
    )

    active = fields.Boolean(default=True)

    name = fields.Char(
        string='Nombre',
        compute='_compute_name',
        store=True
    )

    @api.depends('rating')
    def _compute_is_recommended(self):
        for record in self:
            record.is_recommended = record.rating == 'excelente'

    @api.depends('equipment_id', 'rating_date')
    def _compute_name(self):
        for record in self:
            if record.equipment_id and record.rating_date:
                record.name = f"{record.equipment_id.name} - {record.rating_date}"
            else:
                record.name = "Valoración"