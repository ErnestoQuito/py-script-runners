data = {'nombre_cliente': 'Ernesto Quito Gonzales',
                'numero_servicio':'hjishfiafh',
                'numero_reclamo':'RECLAMO-51545',
                'fecha_reclamo':'2023-01-01'}

with open(r'scripts\template.html', 'r') as html:
    with open('RMA-C-FC165960-2023-P.html', 'w') as to_html:
        to_html.write(
            html.read().format(
                *data
            )
        )
