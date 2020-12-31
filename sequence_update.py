'''Sequence that will be shown to a user, sequence of blocks'''
# this class is made entirely for the screen with width = 1000 and height = 800

#pygame is the library for drawing
#time is the library for time
#random is the library for creating randomly generated objects
#numpy is library used to work with CSV file
import time
import pygame
import sys
import random
from numpy import genfromtxt

#importing the predefined class with block
from Block import Block
from screens import Screens

class Sequence:
    '''Sequence class defines the main functions that will be used by a sequence'''

    # constructor to initiate the sequence
    # i -- the number of sequence that the researcher is using (1-4 or -1 (read from file) or 0 (create random))
    # dict -- the dictionary for mapping the block ID with the block itself
    def __init__(self, i):
        self.i = i
        self.sequence = []
        self.dict = dict()
        self.screens = Screens()

    def create_sequence(self): #creating sequences
        '''this method creates one of four standard sequences depending on the given parameter i'''
        if self.i == 1: #predefined in program sequence
            #creating Blocks and locating them on the screen
            pressed = False
            block1 = Block(400, 120, 50, pressed, 1)
            block2 = Block(100, 100, 50, pressed, 2)
            block3 = Block(600, 150, 50, pressed, 3)
            block4 = Block(125, 300, 50, pressed, 4)
            block5 = Block(425, 315, 50, pressed, 5)
            block6 = Block(625, 335, 50, pressed, 6)
            block7 = Block(60, 450, 50, pressed, 7)
            block8 = Block(450, 580, 50, pressed, 8)
            block9 = Block(550, 550, 50, pressed, 9)

            #creating a dictionary
            self.dict.update({block1.ID: block1})
            self.dict.update({block2.ID: block2})
            self.dict.update({block3.ID: block3})
            self.dict.update({block4.ID: block4})
            self.dict.update({block5.ID: block5})
            self.dict.update({block6.ID: block6})
            self.dict.update({block7.ID: block7})
            self.dict.update({block8.ID: block8})
            self.dict.update({block9.ID: block9})

            #putting the created blocks into a list for keeping the sequence
            self.sequence = [block1, block2, block3, block4, block5, block6, block7, block8, block9]
        elif self.i == 2: #predefined in program sequence
            #creating Blocks and locating them on the screen
            pressed = False
            block1 = Block(100, 550, 50, pressed, 1)
            block2 = Block(200, 570, 50, pressed, 2)
            block3 = Block(600, 700, 50, pressed, 3)
            block4 = Block(300, 350, 50, pressed, 4)
            block5 = Block(350, 450, 50, pressed, 5)
            block6 = Block(700, 600, 50, pressed, 6)
            block7 = Block(400, 100, 50, pressed, 7)
            block8 = Block(500, 70, 50, pressed, 8)
            block9 = Block(800, 200, 50, pressed, 9)

            #creating a dictionary
            self.dict.update({block1.ID: block1})
            self.dict.update({block2.ID: block2})
            self.dict.update({block3.ID: block3})
            self.dict.update({block4.ID: block4})
            self.dict.update({block5.ID: block5})
            self.dict.update({block6.ID: block6})
            self.dict.update({block7.ID: block7})
            self.dict.update({block8.ID: block8})
            self.dict.update({block9.ID: block9})

            #putting the created blocks into a list for keeping the sequence
            self.sequence = [block1, block2, block3, block4, block5, block6, block7, block8, block9]
        elif self.i == 3: #predefined in program sequence
            #creating Blocks and locating them on the screen
            pressed = False
            block1 = Block(100, 300, 50, pressed, 1)
            block2 = Block(400, 600, 50, pressed, 2)
            block3 = Block(460, 525, 50, pressed, 3)
            block4 = Block(600, 400, 50, pressed, 4)
            block5 = Block(800, 450, 50, pressed, 5)
            block6 = Block(150, 15, 50, pressed, 6)
            block7 = Block(185, 75, 50, pressed, 7)
            block8 = Block(625, 60, 50, pressed, 8)
            block9 = Block(850, 80, 50, pressed, 9)

            #creating a dictionary
            self.dict.update({block1.ID: block1})
            self.dict.update({block2.ID: block2})
            self.dict.update({block3.ID: block3})
            self.dict.update({block4.ID: block4})
            self.dict.update({block5.ID: block5})
            self.dict.update({block6.ID: block6})
            self.dict.update({block7.ID: block7})
            self.dict.update({block8.ID: block8})
            self.dict.update({block9.ID: block9})

            #putting the created blocks into a list for keeping the sequence
            self.sequence = [block1, block2, block3, block4, block5, block6, block7, block8, block9]
        elif self.i == 4: #predefined in program sequence
            #creating Blocks and locating them on the screen
            pressed = False
            block1 = Block(100, 120, 50, pressed, 1)
            block2 = Block(250, 250, 50, pressed, 2)
            block3 = Block(170, 380, 50, pressed, 3)
            block4 = Block(70, 510, 50, pressed, 4)
            block5 = Block(200, 700, 50, pressed, 5)
            block6 = Block(600, 50, 50, pressed, 6)
            block7 = Block(700, 120, 50, pressed, 7)
            block8 = Block(650, 250, 50, pressed, 8)
            block9 = Block(620, 450, 50, pressed, 9)
            block10 = Block(750, 700, 50, pressed, 10)

            #creating a dictionary
            self.dict.update({block1.ID: block1})
            self.dict.update({block2.ID: block2})
            self.dict.update({block3.ID: block3})
            self.dict.update({block4.ID: block4})
            self.dict.update({block5.ID: block5})
            self.dict.update({block6.ID: block6})
            self.dict.update({block7.ID: block7})
            self.dict.update({block8.ID: block8})
            self.dict.update({block9.ID: block9})
            self.dict.update({block10.ID: block10})

            #putting the created blocks into a list for keeping the sequence
            self.sequence = [block1, block2, block3, block4, block5, block6, block7, block8, block9, block10]

        elif self.i == 0: #creating random sequence
            self.create_random_sequence()
        elif self.i == -1: #reading sequence from CSV file
            self.read_sequence_from_CSV()
        else:
            print("Researcher does not know how to use this program. Error.")

    def create_random_sequence(self): #creating random sequences
        '''this method creates the sequence with randomly generated and placed blocks'''
        pressed = False
        order_list = [0, 1, 2, 3, 4, 5, 6, 7, 8] #the list of the positions of blocks which will be shuffled
        random.shuffle(order_list) #shuffling the list of positions
        for i in range(len(order_list)):

            #if the last element is 0 - sequence will consist of 8 elements, otherwise - 9
            if i == len(order_list) - 1 and order_list[i] == 0:
                break
            #generating x and y coordinates
            if order_list[i] == 0:
                x_coord = random.randint(0, 273)
                y_coord = random.randint(0, 206)
            if order_list[i] == 1:
                x_coord = random.randint(333, 606)
                y_coord = random.randint(0, 206)
            if order_list[i] == 2:
                x_coord = random.randint(666, 940)
                y_coord = random.randint(0, 206)
            if order_list[i] == 3:
                x_coord = random.randint(0, 273)
                y_coord = random.randint(266, 473)
            if order_list[i] == 4:
                x_coord = random.randint(333, 606)
                y_coord = random.randint(266, 473)
            if order_list[i] == 5:
                x_coord = random.randint(666, 940)
                y_coord = random.randint(266, 473)
            if order_list[i] == 6:
                x_coord = random.randint(0, 273)
                y_coord = random.randint(533, 740)
            if order_list[i] == 7:
                x_coord = random.randint(333, 606)
                y_coord = random.randint(533, 740)
            if order_list[i] == 8:
                x_coord = random.randint(666, 940)
                y_coord = random.randint(533, 740)
            
            #creating a block, adding it to sequence and to the dictionary
            block_id = i + 1
            block = Block(x_coord, y_coord, 50, pressed, block_id)
            self.sequence.append(block)
            self.dict.update({block.ID: block})

    def read_sequence_from_CSV(self):
        '''This method reads the coordinates of blocks for the sequence from the predefined CSV file'''
        table_to_array = genfromtxt('sequence.csv', delimiter = ',')
        print(table_to_array)
        for i in range(1, len(table_to_array)):
            block_id = table_to_array[i][0]
            x_coord = table_to_array[i][1]
            y_coord = table_to_array[i][2]
            length = table_to_array[i][3]
            block = Block(x_coord, y_coord, length, False, block_id)
            self.sequence.append(block)
            self.dict.update({block.ID: block})

    def draw_sequence_human(self, screen, event):
        '''this method draws the sequence made by a user'''
        #redrawing the screen
        #screen.fill((255,255,255))

        for block in self.sequence:
            block.clicked(screen, event)

    def draw_sequence_comp(self, screen):
        '''this method draws the sequence which user will need to repeat'''
        #first showing user the blocks themselves
        for block in self.sequence:
            block.draw_block(screen)
            pygame.display.update()

        #waiting 2 seconds to allow user see all the blocks
        time.sleep(2)

        #showing user the pattern by changing the color of blocks from black to grey
        for block in self.sequence:
            block.draw_computer(screen)
            pygame.display.update()
            #print(f'{block.ID}')
            time.sleep(0.5)

        #waiting 2 seconds to allow user see all the blocks
        time.sleep(2)
        print('')
        #changing color back to black
        for block in self.sequence:
            block.pressed = False

        for block in self.sequence:
            block.draw_block(screen)
            pygame.display.update()

    # user_seq -- the sequence which user entered
    def compare_sequences(self, user_seq):
        '''this method compares sequences and returns the number of errors user made'''
        #k -- counter for errors that user made while repeating the pattern
        #if this metod returns -1, we know that there is an error in input
        k=-1

        #we can compare sequences only if they are of the same length
        if len(user_seq) == len(self.sequence):
            k = 0
            #the loop comparing two sequences by comparing each pair of elements
            for i in range(len(self.sequence)):

                #if elements on the same position in two sequences are not equal,
                #then the counter is getting +1
                if user_seq[i].ID != self.sequence[i].ID:
                    k = k + 1
        return k

    # user_seq -- the sequence which user entered
    def compare_sequences_length(self, user_seq):
        '''this method compares sequences and returns the length of the correctly repeated sequence'''
        #k -- counter for errors that user made while repeating the pattern
        #if this metod returns -1, we know that there is an error in input
        k=-1

        #we can compare sequences only if they are of the same length
        if len(user_seq) == len(self.sequence):
            k = 0
            #the loop comparing two sequences by comparing each pair of elements
            for i in range(len(self.sequence)):

                #if elements on the same position in two sequences are not equal,
                #then then break
                if user_seq[i].ID != self.sequence[i].ID:
                    break
                #if elements on the same position are equal, the length of the correct
                #sequence is increased by 1
                k = k + 1
        return k

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

    #creating the test object
    test_sequence = Sequence(-1)
    test_sequence.create_sequence()
    test_sequence.draw_sequence_comp(screen)
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            test_sequence.draw_sequence_human(screen, event)
            pygame.display.update()

#class functions testing
if __name__ == '__main__':
    main()
