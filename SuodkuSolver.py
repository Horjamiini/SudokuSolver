import pygame
import sys
from pygame.locals import *
from LogicTests import ListLogic


def main(): 
    pygame.init()
    screen = pygame.display.set_mode((500,300))
    font = pygame.font.Font(None, 32)
    clock = pygame.time.Clock()
    window_width = screen.get_width()
    window_height = screen.get_height()
    pygame.display.set_caption('SudokuSolver')
    ## Set size and font for grid
    grid_size = [300,300]
    grid_font = pygame.font.SysFont("Arial",25,True)
    
    ## Rect for typing and variable for text
    type_rect = pygame.Rect(330,20,150,33)
    user_text = ''



    ## Lists for impact rects and for storing user input
    impact_rects = []
    user_inputs = []

    ## Color settings
    color_inactive = pygame.Color('yellow')
    color_active = pygame.Color('orange')
    color = color_inactive
    
    active = False

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit(0)
            
            if event.type == pygame.MOUSEBUTTONDOWN:
                
                ## Todo button logics // functions?
                if window_width-170 <= event.pos[0] <= window_width-170+150 and window_height-60 <= event.pos[1] <= window_height-60+40:
                    pygame.quit()
                    sys.exit(0)
                    
                elif window_width-170 <= event.pos[0] <= window_width-170+150 and window_height-120 <= event.pos[1] <= window_height-120+40:
                    user_inputs.clear()

                ## Store position of click position if click is in impact_rects
                clicked_rect = [r for r in impact_rects if r.collidepoint(event.pos)]

                ## If click was in impact_rects store x & y positions and change active
                if len(clicked_rect) != 0 and clicked_rect[0].collidepoint(event.pos):
                    click_rect_xpos = clicked_rect[0].x
                    click_rect_ypos = clicked_rect[0].y
                    active = True
                
                else:
                    active = False

                color = color_active if active else color_inactive

            if event.type == pygame.KEYDOWN:
                if active:  
                    # Store user inputs to list, clear input and change active if enter is pressed
                    if event.key == pygame.K_RETURN:
                        if user_text != '':
                            ListLogic(int(user_text),user_inputs,click_rect_xpos,click_rect_ypos)
                            print(user_inputs)
                            user_text = ''
                            active = False
                            color = color_active if active else color_inactive
                    ## Allow use to erase input
                    elif event.key == pygame.K_BACKSPACE:
                        user_text = user_text[:-1]
                    else:
                        # Allow user only type one number
                        if event.unicode.isdigit() and len(user_text) == 0:
                            user_text += event.unicode
        
        

        ## Draw rectangle for sudoku grid
        screen.fill("white")
        pygame.draw.rect(screen,"black",[0,0,grid_size[0],grid_size[1]],width=4)

        ## Draw rectangles to create the complete grid
        CreateGrid(screen,grid_size)

        ## Create input spaces for each rectangle
        CreateInputRects(grid_size,impact_rects)

        ## Draw thicker lines for outlines and divide subgrids
        pygame.draw.line(screen,"black",[0,100],[300,100],width=2)
        pygame.draw.line(screen,"black",[0,200],[300,200],width=2)
        pygame.draw.line(screen,"black",[100,0],[100,300],width=2)
        pygame.draw.line(screen,"black",[200,0],[200,300],width=2)

        txt_surface = font.render(user_text, True, color)
        # Resize the box if the text is too long.
        width = max(200, txt_surface.get_width()+10)
        type_rect.w = width
        # Blit the text.
        screen.blit(txt_surface, (type_rect.x+5, type_rect.y+5))
        # Blit the users input numbers to the grid.
        AddNumberToRect(screen,grid_font,user_inputs)
        # Draw the input box
        pygame.draw.rect(screen, color, type_rect, 2)

        # Draw buttons
        DrawButtons(screen,window_width,window_height)

        pygame.display.flip()
        clock.tick(30)



        
### Todo change color of clicked rect?
def CreateGrid(screen,grid_size):
    xrange = 9
    yrange = 9
    rec_width = (grid_size[0]/9)
    rec_height = (grid_size[1]/9)
    Og_rec_width = rec_width
    Og_rec_height = rec_height
        
    for i in range(yrange):
        for j in range(xrange):
            pygame.draw.rect(screen,"black",[0,0,rec_width,rec_height],width=1)
            rec_height += Og_rec_height
        rec_height = Og_rec_height
        rec_width += Og_rec_width
        

def CreateInputRects(grid_size,impact_rects):
    xpos = 0
    ypos = 0
    x = (grid_size[0]/9)
    y = (grid_size[1]/9)

    for j in range(9):

        for i in range(9):
            input_rect = pygame.Rect(xpos,ypos,33,33)
            impact_rects.append(input_rect)
            xpos += x
        xpos = 0
        ypos += y

def AddNumberToRect(screen,font,user_inputs):
        
        if len(user_inputs) != 0:
          for i in user_inputs:
                txt_surface = font.render(str(i[0]), True, 'black')
                screen.blit(txt_surface,((i[1] + 10),i[2] + 2))

def DrawButtons(screen,width,height):
        mouse = pygame.mouse.get_pos()
        light_color = (170,170,170)
        dark_color = (100,100,100)
        btn_txt_color = (255,255,255)
        button_font = pygame.font.SysFont('Robot',30,True)
        solve_btn_txt = button_font.render('Solve',True,btn_txt_color)
        reset_btn_txt = button_font.render('Reset',True,btn_txt_color)
        quit_btn_txt = button_font.render('Quit',True,btn_txt_color)
        ## Quit button active
        if width-170 <= mouse[0] <= width-170+150 and height-60 <= mouse[1] <= height-60+40:
            pygame.draw.rect(screen,light_color,[(width - 170),(height - 60),150,40])
            pygame.draw.rect(screen,dark_color,[(width - 170),(height - 120),150,40])
            pygame.draw.rect(screen,dark_color,[(width - 170),(height - 180),150,40]) 
        ## Reset button active  
        elif width-170 <= mouse[0] <= width-170+150 and height-120 <= mouse[1] <= height-120+40:
            pygame.draw.rect(screen,dark_color,[(width - 170),(height - 60),150,40])
            pygame.draw.rect(screen,light_color,[(width - 170),(height - 120),150,40])
            pygame.draw.rect(screen,dark_color,[(width - 170),(height - 180),150,40])
        ## Solve button acitve
        elif width-170 <= mouse[0] <= width-170+150 and height-180 <= mouse[1] <= height-180+40:
            pygame.draw.rect(screen,dark_color,[(width - 170),(height - 60),150,40])
            pygame.draw.rect(screen,dark_color,[(width - 170),(height - 120),150,40])
            pygame.draw.rect(screen,light_color,[(width - 170),(height - 180),150,40])
        ## All button deactive
        else:
            pygame.draw.rect(screen,dark_color,[(width - 170),(height - 60),150,40])
            pygame.draw.rect(screen,dark_color,[(width - 170),(height - 120),150,40])
            pygame.draw.rect(screen,dark_color,[(width - 170),(height - 180),150,40])

        screen.blit(quit_btn_txt, ((width - 170 + 45),(height - 60 + 10)))
        screen.blit(reset_btn_txt,((width - 170 + 45),(height - 120 + 10)))
        screen.blit(solve_btn_txt,((width - 170 + 45),(height - 180 + 10)))



        
            


if __name__ == '__main__':
    main()