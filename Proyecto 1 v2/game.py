import turtle
import voice_handler
import pywhatkit

screen = turtle.Screen()

t = turtle.Turtle()
t.shape('turtle')
screen.bgcolor('lightgreen')
t.up()

voice_handler.speak('Da órdenes o dí ALTO para finalizar')

while True:
    voice_handler.speak('¿Hacia dónde quieres moverte?')
    command = voice_handler.get_audio()
    print(command)

    if 'alto' in command:
        screen.destroy()
        break
    
    elif 'izquierda' in command:
            voice_handler.speak('Moviendome a la izquierda')
            print('Moviendome a la izquierda')
            t.left(180)
            t.forward(250)
            t.left(180)
    elif 'derecha' in command:
            voice_handler.speak('Moviendome a la derecha')
            print('Moviendome derecha')
            t.forward(250)
    elif 'arriba' in command:
            voice_handler.speak('Moviendome arriba')
            print('Moviendome arriba')
            t.left(90)
            t.forward(250)
            t.right(90)
    elif 'abajo' in command:
            voice_handler.speak('Moviendome abajo')
            print('Moviendome abajo')
            t.right(90)
            t.forward(250)
            t.left(90)
    elif 'motomami' in command:
        voice_handler.speak('reproduciendo a la motomami en Youtube')
        pywhatkit.playonyt('ROSALÍA - CHICKEN TERIYAKI (Official Audio)')
        screen.destroy()
        break
    else: 
        voice_handler.speak('Lo siento, no he podido entenderte mi motomami')
        print("¿Hacia dónde quieres moverte?")

screen.mainloop()
