import PySimpleGUI as sg

sg.theme('DarkAmber')

layout = [
	[sg.T('Registration without using any HTML | CSS')],
	[sg.T('Name: ', size=(15, 1)), sg.In()],
	[sg.T('E-mail: ', size=(15, 1)), sg.In()],
	[sg.T('Number: ', size=(15, 1)), sg.In()],
	[sg.Cancel(), sg.Button('Register')]
]

window = sg.Window('Register', layout)

while True:
	event, values = window()
	if event in [None, 'Cancel']:
		break
	elif event == 'Register': 
		name = values[0]
		email = values[1]
		number = values[2]
		new_layout = [
			[sg.T('Your name: ' + name)],
			[sg.T('Your email: ' + email)],
			[sg.T('Your number: ' + number)]
		]
		new_win = sg.Window('Register successful!', new_layout)

		window.close()
		while True:
			ev2, values = new_win()
			if ev2 == None:
				break
		new_win.close()