{
    'name': 'TechFlow - Gestión de Activos Tecnológicos',
    'version': '1.0.0',
    'category': 'Inventory',
    'summary': 'Gestión de activos tecnológicos de hardware',
    'description': """
        Módulo para gestionar activos tecnológicos de la empresa TechGuárico.
        Permite controlar equipos, asignaciones y estados de hardware.
    """,
    'author': 'TechFlow',
    'website': '', #'https://techflow.com',
    'depends': ['base', 'mail', 'hr'],
    'data': [
        'security/tech_security.xml',
        'security/ir.model.access.csv',
        'views/tech_category_views.xml',
        'views/tech_equipment_views.xml',
        'views/tech_rating_views.xml',
        'views/menus.xml',
        'data/demo_data.xml',
    ],
    'demo': [],
    'installable': True,
    'application': True,
    'auto_install': False,
    'license': 'LGPL-3',
}
