import PySimpleGUI as gui
import requests
import textwrap



input = gui.popup_get_text('Enter Location', 'Enter your location')
print(input)

params = {
  'access_key': '1261911b962a009e45e7d4e65d687c92',
  'query': input,
  'units': 'm'
}

api_result = requests.get('http://api.weatherstack.com/current', params)
api_response = api_result.json();

txt = u'On %s in %s at %s,%s it is %s degrees celsius, while feeling like %s degrees celsius, with a description of %s the wind speed is %s km/h, the wind degree is %s degrees, the wind is flowing %s, the chance of precipitation is %s{}, the humidity level is %s{}, the UV index is of %s, there is a visibility of %s km, and the pressure is of %s hPa ' % (api_response['location']['localtime'],api_response['request']['query'],api_response['location']['lon'],api_response['location']['lat'],api_response['current']['temperature'],api_response['current']['feelslike'],api_response['current']['weather_descriptions'],api_response['current']['wind_speed'],api_response['current']['wind_degree'],api_response['current']['wind_dir'],api_response['current']['precip'],api_response['current']['humidity'],api_response['current']['uv_index'],api_response['current']['visibility'],api_response['current']['pressure'])
PercentSign = '%'
fullText = txt.format(PercentSign, PercentSign)

new_txt = textwrap.wrap(fullText, 40)

gui.theme('DarkAmber')
layout = [
    [gui.Text(new_txt, size=(80, None), key="OUT")],
    [gui.Button("OK")],
]

textWindow = gui.Window("Weather Client", layout, margins = (200,75), resizable = True, location = (0,0))

while True:
    event, values = textWindow.read()
    # End program if user closes window or
    # presses the OK button
    if event == "OK" or event == gui.WIN_CLOSED:
        textWindow.close()
        break
