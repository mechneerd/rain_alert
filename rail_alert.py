mport smtplib
import requests

api_key = 'YOUR_API_KEY'
end_point = 'https://api.openweathermap.org/data/2.5/onecall'
lat = '16.735680'
lng = '82.215610'
my_email = 'YOUR_EMAIL_ID'
my_password = "YOUR_PASSWORD"


weather_parameters = {
    'lat': lat,
    'lon': lng,
    'appid': 'api_key',
    'exclude': 'current,minutely,daily'
}

rain = False
response = requests.get(end_point, params=weather_parameters)
weather_data = response.json()
for i in range(0, 12):
    id_code = weather_data['hourly'][i]['weather'][0]['id']
    print(id_code)
    if int(id_code) < 700:
        rain = True
    else:
        rain = False

if rain:
    connection = smtplib.SMTP('smtp.gmail.com')
    connection.starttls()
    connection.login(my_email, my_password)
    connection.sendmail(
        from_addr='FROM_MAIL_ID',
        to_addrs='TO_MAIL_ID',
        msg=f'subject: rain alert \n\n its going to rain today take your umbrella'
    )
Footer
