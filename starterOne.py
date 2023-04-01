from ursina import *
from ursina.prefabs.radial_menu import RadialMenu, RadialMenuButton

from ursina import Entity
from ursina import curve

import wikipedia as w
import webbrowser

app = Ursina()
window.fullscreen_size=Vec2()

def submit():
    if query_field.text!='':
        p=str(query_field.text).strip()
        pp=p.split(" ")
        par=''
        for i in pp:par+=i+'+'
        parse=par.rstrip('+')      
        wikiP = w.search(f'{parse}')        
        
        fx=0
        lp=int(len(wikiP)//3)
        if lp < 2:
            lp = 1
        hueO = random.randrange(0,255)
        hueI = random.randrange(0,255)
        for z in range(lp):
            rndStart = random.randrange(-3,3)
            for y in range(lp):
                rndStart = random.randrange(-3,3)
                for x in range(lp):
                    rndStart = random.randrange(-3,3)
                    rr = random.randrange(-3,3)
                    if rr==1:rd=-1
                    else: rd=1                  
                    try:                        
                        draggable_button = YourCube(
                                            position=(rndStart+z*rd, rndStart+y*rd, rndStart+x*rd), 
                                            wikiQue=str(wikiP[fx]), 
                                            hueObject=(hueO,hueI))
                        draggable_button.tooltip = Tooltip(str(wikiP[fx]))                        
                    except:
                        continue
                    fx+=1
        query_field.text = ''

def wikiSearch(parse, hueObject):
    p=str(parse).strip()
    pp=p.split(" ")
    par=''
    for i in pp:par+=i+'+'
    parse=par.rstrip('+')
    wikiP = w.search(f'{parse}')
    query_field.text

    hueO = int(hueObject[0])
    hueI = int(hueObject[1])
    wikiP = w.search(f'{parse}')
    query_field.text
    fx=0
    lp=int(len(wikiP))
    if lp < 2:
        lp = 1    
    for x in range(lp):
        rndStart = random.randrange(-4,4)
        rndX = random.randrange(-12,14)
        rndY = random.randrange(-12,14)
        rndZ = random.randrange(-12,14)
        rr = random.randrange(1,3)
        if rr==1:rd=-1
        else: rd=1
        print(rd)
        try:
            draggable_button = YourCube(
                                position=((rndStart*rd)+(rndX*rd), (rndStart*rd)+(rndY*rd), (rndStart*rd)+(rndZ*rd)), 
                                wikiQue=str(wikiP[fx]), 
                                hueObject=(hueO, hueI))
            draggable_button.tooltip = Tooltip(str(wikiP[fx]))            
        except IndexError:
            continue
        fx+=1
    query_field.text = ''

def clearAll():
    application.hot_reloader.reload_code()

def openWiki(parse):
    p=str(parse).strip()
    pp=p.split(" ")
    par=''
    for i in pp:par+=i+'+'
    parse=par.rstrip('+')
    # os.system(f'start firefox "https://pl.wikipedia.org/w/index.php?search={parse}"')
    webbrowser.open_new_tab(f"https://pl.wikipedia.org/w/index.php?search={parse}")

def openGoogle(parse):
    p=str(parse).strip()
    pp=p.split(" ")
    par=''
    for i in pp:par+=i+'+'
    parse=par.rstrip('+')
    # os.system(f'start firefox "https://www.google.com/search?q={parse}"')
    webbrowser.open_new_tab(f"https://www.google.com/search?q={parse}")

def openPhotoGoogle(parse):
    p=str(parse).strip()
    pp=p.split(" ")
    par=''
    for i in pp:par+=i+'+'
    parse=par.rstrip('+')
    # os.system(f'start firefox "https://www.google.com/search?q={parse}&sxsrf=&source=lnms&tbm=isch&sa=&biw=&dpr="')
    webbrowser.open_new_tab(f"https://www.google.com/search?q={parse}&sxsrf=&source=lnms&tbm=isch&sa=&biw=&dpr=")
    # https://www.google.com/search?q=&sxsrf=&source=lnms&tbm=isch&sa=&biw=&dpr=

def openYoutube(parse):
    p=str(parse).strip()
    pp=p.split(" ")
    par=''
    for i in pp:par+=i+'+'
    parse=par.rstrip('+')
    # os.system(f'start firefox "https://www.youtube.com/results?search_query={parse}"')
    webbrowser.open_new_tab(f"https://www.youtube.com/results?search_query={parse}")
    #https://www.youtube.com/results?search_query=korwin+mikke

def openGithub(parse):
    p=str(parse).strip()
    pp=p.split(" ")
    par=''
    for i in pp:par+=i+'+'
    parse=par.rstrip('+')
    os.system(f'start firefox "https://github.com/search?q={parse}"')
    webbrowser.open_new_tab(f"https://github.com/search?q={parse}")
    # https://github.com/search?q=einstine

class YourCube(Button):
    def __init__(self, position=(0,0,0), wikiQue=str(''), hueObject=(1,1)):
        self.rcR = hueObject[0]
        self.rcG = hueObject[1]       
        super().__init__(
            parent = scene,
            position = position,
            model = 'cube',
            origin_y = .5,
            texture = './net_cube.png',
            # color = color.color(random.randrange(0,150), random.randrange(0,90), random.uniform(.01, 1.0)),
            color = color.color(self.rcR, self.rcG, random.uniform(.01, .5)),
            highlight_color = color.lime)

        self.wikiQue = wikiQue
        # 

    def input(self, key):
        if self.hovered:
            if key == 'left mouse up': 
                # camera.editor_position = camera.position              
                print(self.wikiQue)
                try:
                    SEP = ' '
                    STEP=9
                    MAX=1000
                    c = w.summary(self.wikiQue)
                    c=str(c)
                    cc = c.split(SEP)
                    lcc=len(cc)
                    conAll=''
                    steps=[]
                    for x in range(0, lcc, STEP):
                        steps.append(x)
                    for i in steps:
                        for y in range(STEP):
                            try:conAll+=str(cc[i+y]).strip()+SEP
                            except:break
                        conAll+='\n'
                    con=conAll[:MAX] + '...'.strip()
                except:con = ''

                desc = dedent(f'''<scale:.5><azure>{con}''').strip()

                Text.default_resolution = 780 * Text.size


                # print_on_screen(con, position=(0,0), origin=(.50,0), scale=.7)
                def ObjMenu():                    
                    def wikiButtonClick():wikiSearch(self.wikiQue, hueObject=(self.rcR, self.rcG));destroy(rm.backgroundButton);destroy(rm.infoText)
                    def openWikiButtonClick():openWiki(self.wikiQue);destroy(rm.backgroundButton);destroy(rm.infoText)
                    def googleButtonClick():openGoogle(self.wikiQue);destroy(rm.backgroundButton);destroy(rm.infoText)
                    def youtubeButtonClick():openYoutube(self.wikiQue);destroy(rm.backgroundButton);destroy(rm.infoText)
                    def githubButtonClick():openGithub(self.wikiQue);destroy(rm.backgroundButton);destroy(rm.infoText)
                    def photosButtonClick():openPhotoGoogle(self.wikiQue);destroy(rm.backgroundButton);destroy(rm.infoText)
                    def removeButtonClick():destroy(self);destroy(rm.backgroundButton);destroy(rm.infoText)
                    def nextMenu():rm.enabled = False;destroy(rm.backgroundButton);destroy(rm.infoText)
                    def takeButtonClick():
                        draggable_button = InfoCube(position=self.position, wikiQue=str(), hueObject=(self.rcR, self.rcG))
                        draggable_button.tooltip = Tooltip(str(self.wikiQue))
                        rm.enabled = False;destroy(rm.backgroundButton);destroy(rm.infoText)
                        destroy(self)
                    
                    rm = RadialMenu(
                        # background_color=Button(text='Wiki'),
                        buttons = (
                            RadialMenuButton(text='More..', on_click=wikiButtonClick, color=color.yellow, scale=1, text_color=color.black),
                            RadialMenuButton(text='Wiki', on_click=openWikiButtonClick, color=color.blue, scale=1),
                            RadialMenuButton(text='Google', on_click=googleButtonClick, color=color.gray, scale=1.1),
                            RadialMenuButton(text='Video', on_click=youtubeButtonClick, color=color.black, scale=1.3),
                            RadialMenuButton(text='Add me', on_click=takeButtonClick, color=color.green, scale=1.5, text_color=color.black),
                            RadialMenuButton(text='Remove', on_click=removeButtonClick, color=color.red, scale=1.6),
                            RadialMenuButton(text='Clear', on_click=clearAll, color=color.pink, scale=1.5),
                            RadialMenuButton(text='Git', on_click=githubButtonClick, color=color.red, scale=1.3),
                            RadialMenuButton(text='Photo', on_click=photosButtonClick, color=color.orange, scale=1.1),
                            
                            ), 
                        backgroundButton= Button(text=self.wikiQue, text_color=color.white, text_origin=(0, .15), scale=2, on_click=nextMenu),
                        enabled = True,                        
                        infoText = Text(text=desc, position=(.47,.0), origin=(0,0), background=False)
                        ) 
                    
                
                ObjMenu()
                
            if key == 'right mouse down':
                pass

        if held_keys['q']:
            sys.exit()

class InfoCube(Draggable):
    def __init__(self, position=(0,0,0), wikiQue=str(''), hueObject=(1,1)):
        self.rcR = hueObject[0]
        self.rcG = hueObject[1]
        super().__init__(            
            parent = scene,
            position = position,
            model = 'cube',
            origin_y = .5,
            texture = './net_cube.png',
            color = color.color(self.rcR, self.rcG, 1),
            highlight_color = color.color(self.rcR, self.rcG, .3))
        self.wikiQue = wikiQue
    
        

query_field = InputField(y=-.45, x=-.60)
Button('search', scale=.2, color=color.gray.tint(-.4), y=-.45, x=-.28, on_click=submit).fit_to_text()



EditorCamera()
app.run()