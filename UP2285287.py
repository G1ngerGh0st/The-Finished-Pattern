from graphix import *
TILE = 100
SMALL_TILE = 10
VALID_SIZES = [5, 7, 9]
VALID_COLOURS = ["red", "green", "blue", "magenta", "orange", "purple"]



def draw_rectangle(win, point1, point2, colour):
    rect = Rectangle(point1, point2)
    rect.fill_colour = colour
    rect.draw(win)


def get_input(prompt, valid_options):
    while True:
        user_input = input(prompt).strip().lower()
        if user_input in valid_options:
            return user_input
        else:
            print(f"Invalid input. Please enter one of the following: {', '.join(valid_options)}")

def get_window_size():
    size = int(get_input("Enter the size of the window: ", [str(size) for size in VALID_SIZES]))
    if size == 5:
        return 500
    elif size == 7:
        return 700
    else:
        return 900
    

def get_colours():
    colours = []
    while len(colours) < 3:
        colour = get_input(f"Enter colour {len(colours) + 1}: ", VALID_COLOURS)
        if colour not in colours:
            colours.append(colour)
        else:
            print("Colour already chosen. Please choose a different colour.")
    return colours

def draw_lines(win, point1, point2):
    center = Point((point1.x + point2.x) // 2, (point1.y + point2.y) // 2)
    for x in range(point1.x, point2.x + 1, SMALL_TILE):
        top_point = Point(x, point1.y)
        bottom_point = Point(x, point2.y)
        Line(top_point, center).draw(win)
        Line(bottom_point, center).draw(win)
    for y in range(point1.y, point2.y + 1, SMALL_TILE):
        left_point = Point(point1.x, y)
        right_point = Point(point2.x, y)
        Line(left_point, center).draw(win)
        Line(right_point, center).draw(win)

def program():
    win = Window("Patterns", SCREEN, SCREEN)
    colours = get_colours()
    
    for y in range(0, SCREEN, TILE):
        for x in range(0, SCREEN, TILE):
            p1 = Point(x, y)
            p2 = Point(x + TILE, y + TILE)
            draw_rectangle(win, p1, p2, colours[0])
           
    
    for i in range(0, SCREEN, TILE * 2):
        draw_rectangle(win, Point(i, 0), Point(i + TILE, TILE), colours[1])  
        draw_rectangle(win, Point(0, i), Point(TILE, i + TILE), colours[1])  
        draw_rectangle(win, Point(i, SCREEN - TILE), Point(i + TILE, SCREEN), colours[1])  
        draw_rectangle(win, Point(SCREEN - TILE, i), Point(SCREEN, i + TILE), colours[1])  
        
        draw_rectangle(win, Point(i + TILE, 0), Point(i + 2 * TILE, TILE), colours[2])
        draw_rectangle(win, Point(0, i + TILE), Point(TILE, i + 2 * TILE), colours[2])  
        draw_rectangle(win, Point(i + TILE, SCREEN - TILE), Point(i + 2 * TILE, SCREEN), colours[2])  
        draw_rectangle(win, Point(SCREEN - TILE, i + TILE), Point(SCREEN, i + 2 * TILE), colours[2])  
    
    for y in range(0, SCREEN, TILE):
        for x in range(0, SCREEN, TILE):
            if x == y:
                p1 = Point(x, y)
                p2 = Point(x + TILE, y + TILE)
                draw_lines(win, p1, p2)
    
    win.get_mouse()
    win.close()

SCREEN = get_window_size()
program()


