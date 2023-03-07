import os
import pandas as pd
from sqlalchemy import text
from modules.services_masivian import MasivBasicApi
from modules.functions_for_tables import insert_to_table
from modules.services_db import MariaDbConnection

# Establecer variables
HOST = os.getenv('HOST', '198.100.154.133')
NAME = os.getenv('HOST', 'admin_servicio')
USER = os.getenv('HOST', 'admin_servicio')
PASSW = os.getenv('HOST', 'ZJv5c7CspU')
PORT = os.getenv('PORT', 3306)

# Obtener fuente de datos
mariadb = MariaDbConnection(
    h_host=HOST,
    h_db_name=NAME,
    h_user=USER,
    h_pass=PASSW,
    h_port=PORT
)
mariadb.open_conn_engine()
# mariadb.open_conn()
try:
    # Creacion cuerpo para envio masiv
    base_datos = {
        'Subject': 'Respuesta al reclamo {{numero_reclamo}}',
        'From': 'movistarsoluciones.pe@hasber.net',
        'Template': {
            'Type': 'text/html',
            'Value': """<!DOCTYPE html>
    <html lang="es">
    <body style="margin: 0; padding: 0;">
        <table border="0" width="100%" cellpadding="0" bgcolor="#032556" style="padding: 20px; background-color: #ededed; border-collapse:separate;">
            <tbody>
                <!-- HEADER -->
                <tr>
                <td align="center" style="min-width: 590px;">
                    <table width="590" border="0" cellpadding="0" bgcolor="#032556" style="min-width: 590px; background-color: #019df4; padding: 8px; border-collapse:separate;border-top-left-radius: 10px 10px;border-top-right-radius: 10px 10px;">
                        <tr>
                            <td valign="middle" style="font-size:20px; color:white; font-weight: bold;">
                            <!--<strong style="font-family:Arial,Helvetica,sans-serif; font-size: 18px;">Movistar Soluciones</strong> -->
                            <svg style="width: 40px; height: 40px; margin-left: 10px; " aria-hidden="true" class="svg--inline svg--size" focusable="false" role="img" viewBox="0 0 31 25" xmlns="http://www.w3.org/2000/svg"> <title></title> <path d="M5.64103 3.66661C4.25318 3.68712 1.68491 4.39994 0.514369 9.36917C0.000714888 11.5384 -0.196844 13.7948 0.242725 16.482C0.642783 18.964 1.35894 21.1025 1.84296 22.282C2.01088 22.6871 2.26771 23.1128 2.46527 23.3743C3.03325 24.123 3.98647 24.0769 4.38653 23.8717C4.82116 23.6512 5.32494 23.1128 5.1422 21.882C5.05329 21.2871 4.80141 20.4205 4.65818 19.9384C4.22355 18.4564 3.64075 16.6717 3.59136 15.3999C3.52221 13.6974 4.16922 13.4769 4.59891 13.3794C5.32 13.2153 5.9275 14.0358 6.50042 15.0666C7.18694 16.2974 8.36241 18.4769 9.32058 20.1435C10.1849 21.6461 11.7851 23.2564 14.3485 23.1487C16.9661 23.0358 18.8923 21.9999 19.8851 18.7384C20.6259 16.2974 21.1346 14.4717 21.9496 12.6051C22.888 10.4563 24.1375 9.30763 25.1895 9.65635C26.1674 9.98455 26.4095 10.9743 26.4243 12.4307C26.4342 13.723 26.2909 15.1435 26.1773 16.1897C26.1378 16.5692 26.0637 17.3333 26.0934 17.7538C26.1526 18.5846 26.4984 19.4153 27.4022 19.5487C28.3653 19.6922 29.1358 18.8922 29.442 17.9281C29.5655 17.5487 29.6692 16.964 29.7235 16.5538C30.005 14.4666 30.0791 13.0666 29.9507 10.9333C29.8025 8.44097 29.3333 6.16404 28.5135 4.19481C27.7282 2.31276 26.4687 1.10763 24.8537 0.999939C23.0658 0.88199 21.0112 2.11276 19.9345 4.50763C18.9417 6.71276 18.1465 8.9743 17.6675 10.1281C17.1785 11.2974 16.4623 12.0205 15.356 12.1435C14.0077 12.2922 12.8421 11.2717 11.9926 9.82045C11.2517 8.55379 9.7799 6.14866 8.98967 5.3384C8.24882 4.58455 7.40425 3.63584 5.64103 3.66661Z" fill="currentColor"></path> </svg>                   
                            </td>
                            <td valign="middle" align="right">
                            <strong style="font-family:Arial,Helvetica,sans-serif; font-size: 18px; color: white;">Movistar Soluciones</strong> 
                            </td>
                        </tr>
                    </table>
                </td>
                </tr>
                <!-- CONTENT -->
                <tr>
                <td align="center" style="min-width: 590px;">
                    <table width="590" border="0" cellpadding="0" bgcolor="#032556" style="min-width: 590px; background-color: rgb(255, 255, 255); padding: 20px; border-collapse:separate; border-bottom-right-radius: 10px 10px; border-bottom-left-radius: 10px 10px;">
                        <tbody>
                            <td valign="top" style="font-family:Arial,Helvetica,sans-serif; color: #555; font-size: 14px;">
                <div style="padding-left: 0; font-size: 11px; color:#5F5E65; text-align: center;">
                                            Para asegurar que la informaci&oacute;n llegue a su correo electr&oacute;nico, favor agregue <a style="text-decoration: none; color: #62A1DA;" href="">movistarsoluciones.pe@hasber.net</a> a su lista de correo seguros.
                                </div>
                                        <div style="padding-top: 20px; line-height: 20px;">
                                            <strong>Estimado cliente.</strong> {{nombre_cliente}}
                                            <br>
                                            <br>
                                            Servicio No.: {{numero_servicio}}
                                            <br>
                                            <br>
                                            N&uacute;mero de reclamo {{numero_reclamo}}
                                            <br>
                                            <br>
                                            Mediante la presente aprovechamos la oportunidad para saludarlo y a la vez
                                            informarle que su reclamo del d&iacute;a {{fecha_reclamo}}, ha sido atendido.
                                            <br>
                                            <br>
                                            Se adjunta carta de respuesta que contiene el detalle del an&aacute;lisis y resultado del reclamo.
                                            Nos despedimos renovando nuestro compromiso de seguir trabajando para ofrecerle cada d&iacute;a un mejor servicio.
                                            <br>
                                            <br>
                                            Cordialmente,
                                            <br>
                                            <br>
                                            <strong>Soluciones Movistar.</strong>
                                        </div>
                        </td>
                        </tbody>
                    </table>
                </td>
                </tr>
                <!-- FOOTER -->
                <td align="center">     <div style="font-family:Arial,Helvetica,sans-serif;font-size: 11px; padding: 20px; color:#5F5E65; text-align: center;">
                                            Por favor no responder a esta direcci&oacute;n, ya que este es un buz&oacute;n de env&iacute;o autom&aacute;tico. Este mensaje es exclusivo
                                            para la persona o compa&ntilde;&iacute;a al cual est&aacute; dirigido
                                        </div>
                </td>
                </tr>
            </tbody>
        </table>
    </body>
    </html>"""
        },
        'Recipients': []
    }
    base_notificaciones = pd.read_sql(
        text("""SELECT correo_electronico, nombre_cliente, telefono, expediente, fecha_reclamo
FROM `base_notificaciones` WHERE `fecha_consulta_ruta_local` = '2023-02-01' AND flag_estado_procesado=1;"""),
        con=mariadb.engine.connect()
    )
    counter: int = 0
    recipients: list = []
    for row in base_notificaciones.itertuples():
        if counter < 5:
            recipients.append({
                'To': row[1],
                'Parameters': [
                    {
                        'Name': 'nombre_cliente',
                        'Type': 'text',
                        'Value': row[2]
                    },{
                        'Name': 'numero_servicio',
                        'Type': 'text',
                        'Value': row[3]
                    },{
                        'Name': 'numero_reclamo',
                        'Type': 'text',
                        'Value': row[4]
                    },{
                        'Name': 'fecha_reclamo',
                        'Type': 'text',
                        'Value': row[5].strftime('%Y-%m-%d')
                    }
                ]
            })
        counter += 1
    base_datos['Recipients'] = recipients
    print(base_datos)
    # Envio de destinatarios
    # masiva_api = MasivBasicApi(
    #     url='https://api.masiv.masivian.com/email/v1/delivery',
    #     username='Peru_Aleph_Movistar_Hasber_5D2FC',
    #     password='Sz62cO4]H-'
    # )
    # masiva_api.send_masiv_email(base_datos)
    # Obtener y guardar response del envio
    # insert_to_table(conn=, data=, table_name='log_envio_masiv')
except Exception as err:
    print(err)
    print(err.__class__)
finally:
    mariadb.close_conn()
