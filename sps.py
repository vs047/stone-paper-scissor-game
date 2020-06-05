import pygame
import random
pygame.init()
screen=pygame.display.set_mode((600,600))
pygame.display.set_caption("Rock,Paper and scissors")
font1=pygame.font.SysFont(pygame.font.get_fonts()[0],30,True,False)
font2=pygame.font.SysFont(pygame.font.get_fonts()[1],30,False,False)
font3=pygame.font.SysFont(pygame.font.get_fonts()[12],50,False,False)
class game:
    @staticmethod
    def gameloop(screen):
        windowoptions1={"PLAY":[(80,500,100,40),(255,0,0)],"ABOUT":[(250,500,100,40),(0,255,0)],"EXIT":[(420,500,100,40),(0,0,255)]}
        availablechoices={"STONE":[pygame.image.load("stone.png"),(10,200)],"PAPER":[pygame.image.load("paper.png"),(220,200)],"SCISSOR":[pygame.image.load("scissor.png"),(430,200)]}
        choices=["STONE","PAPER","SCISSOR"]
        exit_game=False
        players={"YOU":(100,150),"COMPUTER":(370,150)}
        gameplay=True
        about=False
        image1=pygame.image.load("61QkvmvEdVL.png")
        image1=pygame.transform.scale(image1,(600,600))
        image2=pygame.image.load("download.png")
        image2=pygame.transform.scale(image2,(250,350))
        image3=pygame.image.load("1.png")
        image4=pygame.image.load("2.png")
        image5=pygame.image.load("3.png")
        val=None
        win,loose=False,False
        score=0
        pygame.mixer_music.load("Game-Menu.wav")
        pygame.mixer_music.play(-1)
        while not(exit_game):
            if gameplay:
                screen.blit(image1,(0,0))
                text1=font3.render("Game of Fortune",1,(255,165,0))
                screen.blit(text1,(100,10))
                for i in windowoptions1:
                    text1=font1.render(i,1,(255,165,0))
                    pygame.draw.rect(screen,windowoptions1[i][1],windowoptions1[i][0])
                    screen.blit(text1,(windowoptions1[i][0][0]+5,windowoptions1[i][0][1]+2))
                for event in pygame.event.get():
                    if event.type==pygame.QUIT:
                        exit_game=True
                    elif event.type==pygame.MOUSEBUTTONDOWN:
                        if windowoptions1["PLAY"][0][0]<=pygame.mouse.get_pos()[0]<= windowoptions1["PLAY"][0][0]+ windowoptions1["PLAY"][0][2] and  windowoptions1["PLAY"][0][1]<=pygame.mouse.get_pos()[1]<= windowoptions1["PLAY"][0][1]+ windowoptions1["PLAY"][0][3]:
                            play=True
                            gameplay=False
                        elif windowoptions1["ABOUT"][0][0]<=pygame.mouse.get_pos()[0]<= windowoptions1["ABOUT"][0][0]+ windowoptions1["ABOUT"][0][2] and  windowoptions1["ABOUT"][0][1]<=pygame.mouse.get_pos()[1]<= windowoptions1["ABOUT"][0][1]+ windowoptions1["ABOUT"][0][3]:
                            about=True
                            gameplay=False
                        elif windowoptions1["EXIT"][0][0]<=pygame.mouse.get_pos()[0]<= windowoptions1["EXIT"][0][0]+ windowoptions1["EXIT"][0][2] and  windowoptions1["EXIT"][0][1]<=pygame.mouse.get_pos()[1]<= windowoptions1["EXIT"][0][1]+ windowoptions1["EXIT"][0][3]:
                            exit_game=True
            elif about:
                screen.fill((0,0,0))
                text1=font3.render("RULES",1,(255,255,255))
                screen.blit(text1,(250,10))
                text1=font1.render("Press enter to go to main menu",1,(0,0,125))
                screen.blit(text1,(100,550))
                screen.blit(image3,(150,120))
                screen.blit(image4,(100,250))
                screen.blit(image5,(110,400))
                for event in pygame.event.get():
                    if event.type==pygame.QUIT:
                        exit_game=True
                    elif event.type==pygame.KEYDOWN:
                        if event.key==pygame.K_RETURN:
                            about=False
                            gameplay=True
            elif play:
                if val==None:
                    screen.fill((0,0,0))
                    text2=font2.render("Choose any one option",1,(255,255,255))
                    screen.blit(text2,(30,100))
                    screen.blit(image2,(200,250))
                    for i in availablechoices:
                        text2=font2.render(i,1,(255,255,255))
                        pygame.draw.rect(screen,(183,132,167),(availablechoices[i][1][0],availablechoices[i][1][1],170,40))
                        screen.blit(text2,availablechoices[i][1])
                else:
                    screen.fill((0,0,0))
                    for i in players:
                        text1=font2.render(i,1,(0,255,0))
                        screen.blit(text1,players[i])
                    text2=font2.render(f"score:{score}",1,(255,255,255))
                    screen.blit(text2,(5,4))
                    screen.blit(availablechoices[val][0],(10,200))
                    screen.blit(availablechoices[choices[computer]][0],(350,200))
                    if (val=="STONE" and choices[computer]=="PAPER") or (val=="PAPER" and choices[computer]=="SCISSOR") or (val=="SCISSOR" and choices[computer]=="STONE"):
                        text2=font2.render("GAME OVER",1,(255,255,255))
                        loose=True
                    elif (val=="PAPER" and choices[computer]=="STONE") or (val=="SCISSOR" and choices[computer]=="PAPER") or (val=="STONE" and choices[computer]=="SCISSOR"):
                        text2=font2.render("YOU WON",1,(255,255,255))
                        win=True
                    elif val==choices[computer]:
                        text2=font2.render("DRAW",1,(255,255,255))
                    screen.blit(text2,(250,550))
                for event in pygame.event.get():
                    if event.type==pygame.QUIT:
                        exit_game=True
                    elif event.type==pygame.KEYDOWN:
                        if event.key==pygame.K_RETURN and val!=None:
                            val=None
                            if win:
                                win=False
                                score+=1
                            elif loose:
                                score=0
                                loose=False
                    elif event.type==pygame.MOUSEBUTTONDOWN:
                        if 10<=pygame.mouse.get_pos()[0]<=180 and 200<=pygame.mouse.get_pos()[1]<=240:
                            val="STONE"
                            computer=random.randint(0,2)
                        elif 220<=pygame.mouse.get_pos()[0]<=390 and 200<=pygame.mouse.get_pos()[1]<=240:
                            val="PAPER"
                            computer=random.randint(0,2)
                        elif 430<=pygame.mouse.get_pos()[0]<=600 and 200<=pygame.mouse.get_pos()[1]<=240:
                            val="SCISSOR"
                            computer=random.randint(0,2)
            pygame.display.update()
        pygame.quit()
game.gameloop(screen)
