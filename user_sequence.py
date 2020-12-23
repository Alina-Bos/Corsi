'''this file is created for testing all the functions of sequence_update.py
and block.py and adding the processing of user input'''
#this file contains lines of code that will be in an executable file for the user

#pygame -- library for drawing
#time -- library that works with time
import time
import pygame

#importing the predefined classes
from sequence_update import Sequence

#seq -- sequence selected by computer that is given to user
def detect_block_ID(seq, event):
    '''this function detects the block on which user pressed and returns its ID'''
    if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
        coord_x, coord_y = pygame.mouse.get_pos()
        for i in range(len(seq)):
            if coord_x >= seq[i].x_coord and coord_x <= seq[i].x_coord + seq[i].length and coord_y >= seq[i].y_coord and coord_y <= seq[i].y_coord + seq[i].length:
                return seq[i].ID


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
    test_sequence = Sequence(1)
    test_sequence.create_sequence()
    test_sequence.draw_sequence_comp(screen)

    #creating a list for tracking user input
    user_seq = []

    all_blocks_tapped = 0

    #start a timer
    time_start = time.time()
    #interaction with the user
    while all_blocks_tapped < 9:
        for event in pygame.event.get():
            test_sequence.draw_sequence_human(screen, event)
            k = detect_block_ID(test_sequence.sequence, event)
            if k != None:
                user_seq.append(test_sequence.dict[detect_block_ID(test_sequence.sequence, event)])
                all_blocks_tapped = all_blocks_tapped + 1
            pygame.display.update()

    #end of interaction with the user, stop timer and calculate total time
    time_end = time.time()
    total_time = time_end - time_start

    if test_sequence.compare_sequences(user_seq) == 0:
        print('User did not make any mistakes!')
        print(f'User spend {total_time}sec on this sequence')
        print(f'The correct sequence from the beginning: {test_sequence.compare_sequences_length(user_seq)} blocks')
    elif test_sequence.compare_sequences(user_seq) == -1 or test_sequence.compare_sequences_length(user_seq) == -1:
        print('Error occured')
    else:
        print(f'User made {test_sequence.compare_sequences(user_seq)} mistakes')
        print(f'User spend {total_time}sec on this sequence')
        print(f'The correct sequence from the beginning: {test_sequence.compare_sequences_length(user_seq)} blocks')

    pygame.quit()

#class functions testing
if __name__ == '__main__':
    main()
