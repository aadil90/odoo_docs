# -*- coding: utf-8 -*-

from odoo import models, fields, api


class real_estate(models.Model):
    _name = 'estate.property'
    _description = 'estate.property'

    name = fields.Char(
        string='Title',
        required=True
    )
    description = fields.Text(
        string='Description',
    )
    postcode = fields.Char(
        string='PostCode'
    )
    date_availability = fields.Date(
        string='Date Availability',
        default=fields.Date.context_today,
    )
    expected_price = fields.Float(
        string='Expected Price',
        required=True
    )
    selling_price = fields.Float(
        string='Selling Price',
    )
    bedrooms = fields.Integer(
        string='Bedrooms',
    )
    living_area = fields.Integer(
        string='Living Area',
    )
    facades = fields.Integer(
        string='Facades',
    )
    garage = fields.Boolean(
        string='Garage',
    )
    garden = fields.Boolean(
        string='Garden',
    )
    garden_area = fields.Integer(
        string='Garden Area',
    )
    garden_orientation = fields.Selection(
        string='Garden Orientation',
        selection=[('North', 'North'), ('South', 'South'), ('East','East'),('West','West')]
    )
    