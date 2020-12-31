'''this file contains the implementation of all screens used in the program'''

#pygame -- for drawing screens
import pygame

class Screens:
    '''this class defines the screens to be drawn'''

    def __init__(self):
        self.name = 'NoName'

        #defining fonts to be used
        self.title_font = ''
        self.normal_text_font = ''
        self.width = 1000
        self.height = 800
        self.screen_size = (1000, 800)

    def welcome_screen(self, screen, user_number):
        '''this method draws the welcome screen'''

        #redrawing the screen
        screen.fill((255,255,255))

        #defining fonts to be used
        self.title_font = pygame.font.SysFont(None, 80)
        self.normal_text_font = pygame.font.SysFont(None, 40)

        #drawing first line
        text_surface = self.title_font.render("Corsi Block Tapping Task", True, (0, 0, 0), (255, 255, 255))
        text_rect = text_surface.get_rect()
        text_rect.center = (self.screen_size[0]/2.0, 300)
        screen.blit(text_surface, text_rect)

        #drawing second line
        text_surface = self.normal_text_font.render(f"This is your number: {user_number}. Press SPACE to continue.", True, (0, 0, 0), (255, 255, 255))
        text_rect = text_surface.get_rect()
        text_rect.center = (self.screen_size[0]/2.0, 500)
        screen.blit(text_surface, text_rect)

        pygame.display.flip() #update the display
            
    def show_instructions (self, screen):
        '''Screen with the description of the task'''

        #redrawing the screen
        screen.fill((255,255,255))

        #drawing first line
        text_surface = self.title_font.render("Corsi Block Tapping Task", True, (0, 0, 0), (255, 255, 255))
        text_rect = text_surface.get_rect()
        text_rect.center = (self.screen_size[0]/2.0, 150)
        screen.blit(text_surface, text_rect)

        #drawing second line
        text_surface = self.normal_text_font.render("You will be presented with four screens with blocks.", True, (0, 0, 0), (255, 255, 255))
        text_rect = text_surface.get_rect()
        text_rect.center = (self.screen_size[0]/2.0, 300)
        screen.blit(text_surface, text_rect)
        
        #drawing third line
        text_surface = self.normal_text_font.render("Computer will show the sequence changing the color of blocks", True, (0, 0, 0), (255, 255, 255))
        text_rect = text_surface.get_rect()
        text_rect.center = (self.screen_size[0]/2.0, 350)
        screen.blit(text_surface, text_rect)

        #drawing fourth line
        text_surface = self.normal_text_font.render("from black to grey.", True, (0, 0, 0), (255, 255, 255))
        text_rect = text_surface.get_rect()
        text_rect.center = (self.screen_size[0]/2.0, 400)
        screen.blit(text_surface, text_rect)

        #drawing fifth line
        text_surface = self.normal_text_font.render("Your task is to repeat the shown sequence.", True, (0, 0, 0), (255, 255, 255))
        text_rect = text_surface.get_rect()
        text_rect.center = (self.screen_size[0]/2.0, 450)
        screen.blit(text_surface, text_rect)

        #drawing sixth line
        text_surface = self.normal_text_font.render("Press SPACE to continue.", True, (0, 0, 0), (255, 255, 255))
        text_rect = text_surface.get_rect()
        text_rect.center = (self.screen_size[0]/2.0, 550)
        screen.blit(text_surface, text_rect)

        pygame.display.flip() #update the display
    
    def rules_of_use (self, screen):
        '''Screen with the rules for using '''

        #redrawing the screen
        screen.fill((255,255,255))

        #drawing first line
        text_surface = self.title_font.render("Corsi Block Tapping Task", True, (0, 0, 0), (255, 255, 255))
        text_rect = text_surface.get_rect()
        text_rect.center = (self.screen_size[0]/2.0, 150)
        screen.blit(text_surface, text_rect)

        #drawing second line
        text_surface = self.normal_text_font.render("Start repeating the sequence only after seeing", True, (0, 0, 0), (255, 255, 255))
        text_rect = text_surface.get_rect()
        text_rect.center = (self.screen_size[0]/2.0, 300)
        screen.blit(text_surface, text_rect)
        
        #drawing third line
        text_surface = self.normal_text_font.render("that all blocks are black again.", True, (0, 0, 0), (255, 255, 255))
        text_rect = text_surface.get_rect()
        text_rect.center = (self.screen_size[0]/2.0, 350)
        screen.blit(text_surface, text_rect)

        #drawing fourth line
        text_surface = self.normal_text_font.render("After each trial you will be shown your results.", True, (0, 0, 0), (255, 255, 255))
        text_rect = text_surface.get_rect()
        text_rect.center = (self.screen_size[0]/2.0, 400)
        screen.blit(text_surface, text_rect)

        #drawing fifth line
        text_surface = self.normal_text_font.render("After all trials you will be shown the summary of your results.", True, (0, 0, 0), (255, 255, 255))
        text_rect = text_surface.get_rect()
        text_rect.center = (self.screen_size[0]/2.0, 450)
        screen.blit(text_surface, text_rect)

        #drawing sixth line
        text_surface = self.normal_text_font.render("Press SPACE to start the task.", True, (0, 0, 0), (255, 255, 255))
        text_rect = text_surface.get_rect()
        text_rect.center = (self.screen_size[0]/2.0, 550)
        screen.blit(text_surface, text_rect)

        pygame.display.flip() #update the display

    #time - time spent on repeating the sequence
    #corr_seq_len - the number of correctly tapped blocks from the beginning
    #err_made - number of errors made by user
    def intermadiate_screen (self, screen, time, corr_seq_len, err_made):
        '''Intermediate screen'''
        
        #redrawing the screen
        screen.fill((255,255,255))

        #drawing first line
        text_surface = self.title_font.render("Corsi Block Tapping Task", True, (0, 0, 0), (255, 255, 255))
        text_rect = text_surface.get_rect()
        text_rect.center = (self.screen_size[0]/2.0, 150)
        screen.blit(text_surface, text_rect)

        #drawing second line
        text_surface = self.title_font.render("Your intermediate results", True, (0, 0, 0), (255, 255, 255))
        text_rect = text_surface.get_rect()
        text_rect.center = (self.screen_size[0]/2.0, 200)
        screen.blit(text_surface, text_rect)
        
        #drawing third line
        text_surface = self.normal_text_font.render(f"Time spent: {time}.", True, (0, 0, 0), (255, 255, 255))
        text_rect = text_surface.get_rect()
        text_rect.center = (self.screen_size[0]/2.0, 350)
        screen.blit(text_surface, text_rect)

        #drawing fourth line
        text_surface = self.normal_text_font.render(f"Number of correctly tapped blocks from the beginning: {corr_seq_len}.", True, (0, 0, 0), (255, 255, 255))
        text_rect = text_surface.get_rect()
        text_rect.center = (self.screen_size[0]/2.0, 400)
        screen.blit(text_surface, text_rect)

        #drawing fifth line
        text_surface = self.normal_text_font.render(f"Number of errors made: {err_made}.", True, (0, 0, 0), (255, 255, 255))
        text_rect = text_surface.get_rect()
        text_rect.center = (self.screen_size[0]/2.0, 450)
        screen.blit(text_surface, text_rect)

        #drawing sixth line
        text_surface = self.normal_text_font.render("Press SPACE to start the next trial.", True, (0, 0, 0), (255, 255, 255))
        text_rect = text_surface.get_rect()
        text_rect.center = (self.screen_size[0]/2.0, 550)
        screen.blit(text_surface, text_rect)

        pygame.display.flip() #update the display

    #max_length - maximum length repeated by user without errors
    #seq1time - time spent on the first sequence
    #seq2time - time spent on the first sequence
    #seq3time - time spent on the first sequence
    #seq4time - time spent on the first sequence
    #final_score - final score
    def final_screen (self, screen, max_length, seq1time, seq2time, seq3time, seq4time, final_score):
        '''Final screen with the results'''
 
        #redrawing the screen
        screen.fill((255,255,255))

        #drawing first line
        text_surface = self.title_font.render("Corsi Block Tapping Task", True, (0, 0, 0), (255, 255, 255))
        text_rect = text_surface.get_rect()
        text_rect.center = (self.screen_size[0]/2.0, 150)
        screen.blit(text_surface, text_rect)

        #drawing second line
        text_surface = self.title_font.render("Your final results", True, (0, 0, 0), (255, 255, 255))
        text_rect = text_surface.get_rect()
        text_rect.center = (self.screen_size[0]/2.0, 200)
        screen.blit(text_surface, text_rect)
        
        #drawing third line
        text_surface = self.normal_text_font.render(f"Time spenton the first sequence: {seq1time}.", True, (0, 0, 0), (255, 255, 255))
        text_rect = text_surface.get_rect()
        text_rect.center = (self.screen_size[0]/2.0, 350)
        screen.blit(text_surface, text_rect)
        
        #drawing fourth line
        text_surface = self.normal_text_font.render(f"Time spenton the second sequence: {seq2time}.", True, (0, 0, 0), (255, 255, 255))
        text_rect = text_surface.get_rect()
        text_rect.center = (self.screen_size[0]/2.0, 400)
        screen.blit(text_surface, text_rect)
        
        #drawing fifth line
        text_surface = self.normal_text_font.render(f"Time spenton the third sequence: {seq3time}.", True, (0, 0, 0), (255, 255, 255))
        text_rect = text_surface.get_rect()
        text_rect.center = (self.screen_size[0]/2.0, 450)
        screen.blit(text_surface, text_rect)
        
        #drawing sixth line
        text_surface = self.normal_text_font.render(f"Time spenton the fourth sequence: {seq4time}.", True, (0, 0, 0), (255, 255, 255))
        text_rect = text_surface.get_rect()
        text_rect.center = (self.screen_size[0]/2.0, 500)
        screen.blit(text_surface, text_rect)

        #drawing seventh line
        text_surface = self.normal_text_font.render(f"Max number of correctly tapped blocks from the beginning: {max_length}.", True, (0, 0, 0), (255, 255, 255))
        text_rect = text_surface.get_rect()
        text_rect.center = (self.screen_size[0]/2.0, 550)
        screen.blit(text_surface, text_rect)

        #drawing eighth line
        text_surface = self.normal_text_font.render(f"Final score: {final_score}.", True, (0, 0, 0), (255, 255, 255))
        text_rect = text_surface.get_rect()
        text_rect.center = (self.screen_size[0]/2.0, 600)
        screen.blit(text_surface, text_rect)

        #drawing ninth line
        text_surface = self.normal_text_font.render("Press SPACE to save the results.", True, (0, 0, 0), (255, 255, 255))
        text_rect = text_surface.get_rect()
        text_rect.center = (self.screen_size[0]/2.0, 700)
        screen.blit(text_surface, text_rect)

        pygame.display.flip() #update the display

    def goodbye_screen (self, screen):
        '''Goodbye screen'''

        #redrawing the screen
        screen.fill((255,255,255))

        #defining fonts to be used
        self.title_font = pygame.font.SysFont(None, 80)
        self.normal_text_font = pygame.font.SysFont(None, 40)

        #drawing first line
        text_surface = self.title_font.render("Corsi Block Tapping Task", True, (0, 0, 0), (255, 255, 255))
        text_rect = text_surface.get_rect()
        text_rect.center = (self.screen_size[0]/2.0, 300)
        screen.blit(text_surface, text_rect)

        #drawing second line
        text_surface = self.normal_text_font.render("This is the end of the Corsi Block Tapping Task.", True, (0, 0, 0), (255, 255, 255))
        text_rect = text_surface.get_rect()
        text_rect.center = (self.screen_size[0]/2.0, 400)
        screen.blit(text_surface, text_rect)

        #drawing third line
        text_surface = self.normal_text_font.render("Thank you for participation.", True, (0, 0, 0), (255, 255, 255))
        text_rect = text_surface.get_rect()
        text_rect.center = (self.screen_size[0]/2.0, 450)
        screen.blit(text_surface, text_rect)

        #drawing fourth line
        text_surface = self.normal_text_font.render("Have a nice day!", True, (0, 0, 0), (255, 255, 255))
        text_rect = text_surface.get_rect()
        text_rect.center = (self.screen_size[0]/2.0, 550)
        screen.blit(text_surface, text_rect)

        pygame.display.flip() #update the display

    def repeat_sequence_screen (self, screen):
        '''Repeat the sequence'''
        #redrawing the screen
        screen.fill((255,255,255))

        #defining fonts to be used
        self.title_font = pygame.font.SysFont(None, 80)
        self.normal_text_font = pygame.font.SysFont(None, 40)

        #drawing first line
        text_surface = self.title_font.render("Corsi Block Tapping Task", True, (0, 0, 0), (255, 255, 255))
        text_rect = text_surface.get_rect()
        text_rect.center = (self.screen_size[0]/2.0, 300)
        screen.blit(text_surface, text_rect)

        #drawing second line
        text_surface = self.normal_text_font.render("Press SPACE and repeat the sequence you've just seen.", True, (0, 0, 0), (255, 255, 255))
        text_rect = text_surface.get_rect()
        text_rect.center = (self.screen_size[0]/2.0, 500)
        screen.blit(text_surface, text_rect)

        pygame.display.flip() #update the display

def main():
    '''THIS IS MAIN'''

    flag = True

    #insert the number of the participant
    user_input = input("Insert your number here: ")
    print(f'User number is {user_input}') 

    #defining screen parameters
    pygame.init()
    pygame.display.set_mode((1000, 800))
    screen = pygame.display.get_surface()
    #screen.fill((255,255,255))

    #creating a test object
    screen_test = Screens()
    screen_test.welcome_screen(screen, user_input)
    
    #transition to the next screen
    while flag:
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                screen_test.show_instructions(screen)
                flag = False

    flag = True

    #transition to the next screen
    while flag:
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                screen_test.rules_of_use(screen)
                flag = False

    flag = True

    #transition to the next screen
    while flag:
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                screen_test.intermadiate_screen(screen, 1, 2, 3)
                flag = False

    flag = True

    #transition to the next screen
    while flag:
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                screen_test.final_screen(screen, 1, 2, 3, 4, 5, 6)
                flag = False

    flag = True

    #transition to the next screen
    while flag:
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                screen_test.goodbye_screen(screen)
                flag = False

    flag = True

    #transition to the next screen
    while flag:
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                screen_test.repeat_sequence_screen(screen)
                flag = False
    flag = True

#class functions testing
if __name__ == '__main__':
    main()
