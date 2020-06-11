from koblitz import *
import turtle

# initializing the turtle settings
ob = turtle.Turtle()
ob.speed(10000)
ob.hideturtle()
wn = turtle.Screen()
wn.bgcolor("black")
ob.pencolor("teal")


def turn_sequence_generator(private_key):
    iterations = private_key[1]
    old = ['f', 'l']
    new = ['f', 'l']
    steps = []
    k = 0
    while(k < iterations):
        for i in range(0, len(old)-1):
            if old[i] == 'r':
                old[i] = 'l'
            elif old[i] == 'l':
                old[i] = 'r'
        for i in range(0, len(old)//2):
            t = old[i]
            old[i] = old[len(old)-i-2]
            old[len(old)-i-2] = t
        for i in old:
            new.append(i)
        for i in old[:]:
            old.remove(i)
        for i in new:
            old.append(i)
        for i in steps[:]:
            steps.remove(i)
        for i in range(0, len(new)):
            steps.append(new[i])
        k += 1
    return steps


def dragon_render(starting_point, private_key):
    size = private_key[0]

    x_start = starting_point[0]
    y_start = starting_point[1]
    angle = private_key[2]

    #print('Starting Point : (' + str(x_start) + ', ' + str(y_start) + ')')

    ob.penup()
    ob.goto(x_start, y_start)
    ob.pendown()

    ob.left(angle)

    steps = turn_sequence_generator(private_key)
    steps = steps[:-1]
    ob.pencolor('green')
    for i in steps:
        if i == 'f':
            ob.forward(size)
        elif i == 'r':
            ob.right(90)
        elif i == 'l':
            ob.left(90)

    x_end = round(ob.xcor())
    y_end = round(ob.ycor())

    #print('Ending Point : (' + str(x_end) + ', ' + str(y_end) + ')')
    return (x_end,y_end)


def reverse_dragon_render(starting_point, private_key):
    size = private_key[0]

    x_start = starting_point[0]
    y_start = starting_point[1]

    angle = private_key[2]

    #print('Reverse Starting Point : (' + str(x_start) + ', ' + str(y_start) + ')')

    ob.penup()
    ob.goto(x_start, y_start)
    ob.pendown()

    steps = turn_sequence_generator(private_key)
    steps = steps[:-1]
    ob.left(180+angle)
    ob.pencolor('red')
    for i in steps:
        if i == 'f':
            ob.forward(size)
        elif i == 'r':
            ob.right(90)
        elif i == 'l':
            ob.left(90)

    x_end = round(ob.xcor())
    y_end = round(ob.ycor())

    #print('Reverse Ending Point : (' + str(x_end) + ', ' + str(y_end) + ')')
    return (x_end,y_end)

def point_to_character(points):
    output_x = 'X'
    output_y = 'Y'
    for x,y in points:
        output_x += str(x) + 'X'
        output_y += str(y) + 'Y'

    return output_x+output_y

def character_to_point(output):
    output_x,output_y = output.split('XY')
    x_end = output_x.split('X')
    x_end = x_end[1:]
    x_end = [int(x) for x in x_end]
    y_end = output_y.split('Y')
    y_end = y_end[:-1]
    y_end = [int(y) for y in y_end]
    points = []
    for i in range(len(x_end)):
        points.append((x_end[i],y_end[i]))  
    return points





def dragon_encrypt(plainText,private_key):
    starting_points = koblitz_encoder(plainText,private_key[3],private_key[4])
    ending_points = []
    for point in starting_points:
        end_point = dragon_render(point,private_key)
        ending_points.append(end_point)
    encrypted_text = point_to_character(ending_points)
    return encrypted_text

def dragon_decrypt(cipherText,private_key):
    ending_points = character_to_point(cipherText)
    starting_points = []
    for point in ending_points:
        start_point = reverse_dragon_render(point,private_key)
        starting_points.append(start_point)
    decrypted_text = koblitz_decoder(starting_points)
    return decrypted_text

if __name__ == '__main__':
    print('-------------------Dragon_Crypto-------------------\n')
    plainText = input("Enter Message: ")
    print('\n-------------------Private Key---------------------')
    size = int(input('Size of Dragon: '))
    iterations = int(input('No. of Iterations: '))
    angle = int(input('Angle: '))
    print('Curve Parameters')
    elliptic_a = int(input("Enter A: "))
    elliptic_b = int(input("Enter B: "))
    print('---------------------------------------------------')
    private_key = (size,iterations,angle,elliptic_a,elliptic_b)
    print('-------------------Encryption----------------------\n')
    cipherText = dragon_encrypt(plainText,private_key)
    print("Encrypted Message: ", cipherText)
    print('\n---------------------------------------------------')
    print('-------------------Decryption----------------------\n')
    decrypt = dragon_decrypt(cipherText,private_key)
    print("Decrypted message: ", decrypt)

    turtle.done()