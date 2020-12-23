'''this file contains the final implementation of the corsi tapping task without screens'''

#pygame -- library for drawing
#time -- library that works with time
import time
import pygame

#importing the predefined classes
from sequence_update import Sequence
from user_sequence import detect_block_ID
from save import filelog

def main():
    '''This is the body of the main executable program'''
    #defining the screen parameters
    pygame.init()
    width = 1000
    height = 800
    pygame.display.set_mode((width, height))
    screen = pygame.display.get_surface()
    screen.fill((255,255,255))

    #creating the first sequence
    #the first sequence is using one of the predefined in program sequences
    sequence1 = Sequence(1)
    sequence1.create_sequence()
    sequence1.draw_sequence_comp(screen)

    #variable for keeping the maximum length that user repeated correctly
    max_length = -1

    #creating a list for tracking user input
    user_seq = []

    all_blocks_tapped = 0

    #start a timer
    time_start = time.time()
    #interaction with the user
    while all_blocks_tapped < len(sequence1.sequence):
        for event in pygame.event.get():
            sequence1.draw_sequence_human(screen, event)
            k = detect_block_ID(sequence1.sequence, event)
            if k != None:
                user_seq.append(sequence1.dict[detect_block_ID(sequence1.sequence, event)])
                all_blocks_tapped = all_blocks_tapped + 1
            pygame.display.update()

    #end of interaction with the user, stop timer and calculate total time
    time_end = time.time()
    #total time spent on this sequence
    seq1time = time_end - time_start

    #summarizing the results
    if sequence1.compare_sequences(user_seq) == 0:
        print('User did not make any mistakes!')
        print(f'User spend {seq1time}sec on this sequence')
        print(f'The correct sequence from the beginning: {sequence1.compare_sequences_length(user_seq)} blocks')
        #checking the maximum length
        if max_length < sequence1.compare_sequences_length(user_seq):
            max_length = sequence1.compare_sequences_length(user_seq)
    elif sequence1.compare_sequences(user_seq) == -1 or sequence1.compare_sequences_length(user_seq) == -1:
        print('Error occured')
    else:
        print(f'User made {sequence1.compare_sequences(user_seq)} mistakes')
        print(f'User spend {seq1time}sec on this sequence')
        print(f'The correct sequence from the beginning: {sequence1.compare_sequences_length(user_seq)} blocks')
        #checking the maximum length
        if max_length < sequence1.compare_sequences_length(user_seq):
            max_length = sequence1.compare_sequences_length(user_seq)
    #counting the errors made by the user with this sequence
    err1 = sequence1.compare_sequences(user_seq)

    #redrawing the screen
    screen.fill((255,255,255))

    #creating the second sequence
    #second sequence is randomly generated
    sequence2 = Sequence(0)
    sequence2.create_sequence()
    sequence2.draw_sequence_comp(screen)

    #creating a list for tracking user input
    user_seq = []

    all_blocks_tapped = 0

    #start a timer
    time_start = time.time()
    #interaction with the user
    while all_blocks_tapped < len(sequence2.sequence):
        for event in pygame.event.get():
            sequence2.draw_sequence_human(screen, event)
            k = detect_block_ID(sequence2.sequence, event)
            if k != None:
                user_seq.append(sequence2.dict[detect_block_ID(sequence2.sequence, event)])
                all_blocks_tapped = all_blocks_tapped + 1
            pygame.display.update()

    #end of interaction with the user, stop timer and calculate total time
    time_end = time.time()
    #total time spent on this sequence
    seq2time = time_end - time_start

    #summarizing the results
    if sequence2.compare_sequences(user_seq) == 0:
        print('User did not make any mistakes!')
        print(f'User spend {seq2time}sec on this sequence')
        print(f'The correct sequence from the beginning: {sequence2.compare_sequences_length(user_seq)} blocks')
        #checking the maximum length
        if max_length < sequence2.compare_sequences_length(user_seq):
            max_length = sequence2.compare_sequences_length(user_seq)
    elif sequence2.compare_sequences(user_seq) == -1 or sequence2.compare_sequences_length(user_seq) == -1:
        print('Error occured')
    else:
        print(f'User made {sequence2.compare_sequences(user_seq)} mistakes')
        print(f'User spend {seq2time}sec on this sequence')
        print(f'The correct sequence from the beginning: {sequence2.compare_sequences_length(user_seq)} blocks')
        #checking the maximum length
        if max_length < sequence2.compare_sequences_length(user_seq):
            max_length = sequence2.compare_sequences_length(user_seq)
    #counting the errors made by the user with this sequence
    err2 = sequence2.compare_sequences(user_seq)

    #redrawing the screen
    screen.fill((255,255,255))

    #creating the third sequence
    sequence3 = Sequence(-1)
    sequence3.create_sequence()
    sequence3.draw_sequence_comp(screen)

    #creating a list for tracking user input
    user_seq = []

    all_blocks_tapped = 0

    #start a timer
    time_start = time.time()
    #interaction with the user
    while all_blocks_tapped < len(sequence3.sequence):
        for event in pygame.event.get():
            sequence3.draw_sequence_human(screen, event)
            k = detect_block_ID(sequence3.sequence, event)
            if k != None:
                user_seq.append(sequence3.dict[detect_block_ID(sequence3.sequence, event)])
                all_blocks_tapped = all_blocks_tapped + 1
            pygame.display.update()

    #end of interaction with the user, stop timer and calculate total time
    time_end = time.time()
    #total time spent on this sequence
    seq3time = time_end - time_start

    #summarizing the results
    if sequence3.compare_sequences(user_seq) == 0:
        print('User did not make any mistakes!')
        print(f'User spend {seq3time}sec on this sequence')
        print(f'The correct sequence from the beginning: {sequence3.compare_sequences_length(user_seq)} blocks')
        #checking the maximum length
        if max_length < sequence3.compare_sequences_length(user_seq):
            max_length = sequence3.compare_sequences_length(user_seq)
    elif sequence3.compare_sequences(user_seq) == -1 or sequence3.compare_sequences_length(user_seq) == -1:
        print('Error occured')
    else:
        print(f'User made {sequence3.compare_sequences(user_seq)} mistakes')
        print(f'User spend {seq3time}sec on this sequence')
        print(f'The correct sequence from the beginning: {sequence3.compare_sequences_length(user_seq)} blocks')
        #checking the maximum length
        if max_length < sequence3.compare_sequences_length(user_seq):
            max_length = sequence3.compare_sequences_length(user_seq)
    #counting the errors made by the user with this sequence
    err3 = sequence3.compare_sequences(user_seq)

    #redrawing the screen
    screen.fill((255,255,255))

    #creating the fourth sequence
    sequence4 = Sequence(0)
    sequence4.create_sequence()
    sequence4.draw_sequence_comp(screen)

    #creating a list for tracking user input
    user_seq = []

    all_blocks_tapped = 0

    #start a timer
    time_start = time.time()
    #interaction with the user
    while all_blocks_tapped < len(sequence4.sequence):
        for event in pygame.event.get():
            sequence4.draw_sequence_human(screen, event)
            k = detect_block_ID(sequence4.sequence, event)
            if k != None:
                user_seq.append(sequence4.dict[detect_block_ID(sequence4.sequence, event)])
                all_blocks_tapped = all_blocks_tapped + 1
            pygame.display.update()

    #end of interaction with the user, stop timer and calculate total time
    time_end = time.time()
    #total time spent on this sequence
    seq4time = time_end - time_start

    #summarizing the results
    if sequence4.compare_sequences(user_seq) == 0:
        print('User did not make any mistakes!')
        print(f'User spend {seq4time}sec on this sequence')
        print(f'The correct sequence from the beginning: {sequence4.compare_sequences_length(user_seq)} blocks')
        #checking the maximum length
        if max_length < sequence4.compare_sequences_length(user_seq):
            max_length = sequence4.compare_sequences_length(user_seq)
    elif sequence4.compare_sequences(user_seq) == -1 or sequence4.compare_sequences_length(user_seq) == -1:
        print('Error occured')
    else:
        print(f'User made {sequence4.compare_sequences(user_seq)} mistakes')
        print(f'User spend {seq4time}sec on this sequence')
        print(f'The correct sequence from the beginning: {sequence4.compare_sequences_length(user_seq)} blocks')
        #checking the maximum length
        if max_length < sequence4.compare_sequences_length(user_seq):
            max_length = sequence4.compare_sequences_length(user_seq)
    #counting the errors made by the user with this sequence
    err4 = sequence4.compare_sequences(user_seq)

    #variable for calculating the final score of the user
    #final score is the total possible scores to earn
    #minus the number of errors made by the user in all four sequences
    final_score = len(sequence1.sequence) + len(sequence2.sequence) + len(sequence3.sequence) + len(sequence4.sequence) - err1 - err2 - err3 - err4

    #saving results to file
    filelog(1007, max_length, seq1time, seq2time, seq3time, seq4time, final_score)
    pygame.quit()


#start corsi tapping task
if __name__ == '__main__':
    main()
