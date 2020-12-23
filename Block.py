'''Block object which will be used in a corsi-blocks test'''

#pygame is the library for drawing
import pygame

class Block:
    '''Block class defines the main functions that can be done with the block'''

    #Constructor to initiate a block (square)
    #x and y -- coordinates of the top left corner
    #length -- the length of one side of the square
    #pressed -- is the boolean variable for detecting whether a user clicked on the block
    #ID -- the id of the block
    def __init__(self, x, y, length, pressed, ID):
        self.x_coord = x
        self.y_coord = y
        self.length = length
        self.pressed = pressed
        self.ID = ID

    def draw_block(self, screen):
        '''function for drawing a block with initialized parameters'''
        if self.pressed:
            pygame.draw.rect(screen, (169,169,169),
            (self.x_coord, self.y_coord, self.length, self.length),0)
        else:
            pygame.draw.rect(screen, (0, 0, 0),
            (self.x_coord, self.y_coord, self.length, self.length),0)

    def clicked(self, screen, event):
        '''function for detecting whether a user has pressed on the block'''
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            coord_x, coord_y = pygame.mouse.get_pos()
            if coord_x >= self.x_coord and coord_x <= self.x_coord + self.length and coord_y >= self.y_coord and coord_y <= self.y_coord + self.length:
                self.pressed = True
        self.draw_block(screen)

    def draw_computer(self, screen):
        '''function for the computer to show the user the pattern'''
        self.pressed = True
        self.draw_block(screen)

#this class will be tested, thus, we need this main method
#as it sets the environment where we are going to test
def main():
    '''This is MAAAAIN'''
    #defining the screen parameters
    pygame.init()
    width = 1000
    height = 800
    pygame.display.set_mode((width, height))
    screen = pygame.display.get_surface()
    screen.fill((255,255,255))

    #creating an object
    pressed = False
    block1 = Block(100, 100, 50, pressed, 1)

    #drawing initial block
    #block1.draw_block(screen)
    #pygame.display.update()

    #checking and updating the color when the block is clicked
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                #sys.exit()
            block1.clicked(screen, event)
            pygame.display.update()

#class functions testing
if __name__ == '__main__':
    main()
