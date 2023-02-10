import matplotlib.pyplot as plt
from matplotlib.patches import Circle, Rectangle, Arc
#functions to convert feet to cm
def foot_to_cm(ft, inch):
       ft = int(ft)
       inch = int(inch)

       inch += ft * 12
       cm = round(inch * 2.54, 1)

       return cm
#functions to convert lbs to kg
def lbs_to_kg(lbs):
       kg = lbs*0.453592
       return kg
#functions to remove duplicates in the list
def dedupe(items):
       seen = set()
       for item in items:
              if item not in seen:
                     yield item
                     seen.add(item)
       return(items)

#functions to create basketball court
def create_court(playername):
    # Set-up figure
    fig = plt.figure(figsize=(16, 8))
    ax = fig.add_axes([.2, .1, .6, .8], frame_on=False, 
                       xticks=[], yticks=[])
    
    # Draw the borders of the court
    ax.set_xlim(-20, 960)
    ax.vlines([0, 940], 0, 500) #-250, 250
    ax.hlines([0, 500], 0, 940) #-250, 250
    ax.hlines([190, 190, 330, 330], [0, 750] * 2, [190, 940] * 2) #-80, -80, 80, 80
    ax.hlines([170, 170, 310, 310], [0, 750] * 2, [190, 940] * 2) #-60, -60, 60, 60
    ax.vlines([190, 750], 170, 330) # -80, 80 
    ax.vlines(470, 0, 500) #-250, 250
    ax.vlines([40, 900], 220, 280) # -30, 30
    
    # Add the three point arc, free throw circle, 
    # midcourt circle and backboard and rim
    ax.add_patch(Arc((190,250), 120, 120, theta1=-90, theta2=90))
    ax.add_patch(Arc((190, 250), 120, 120, theta1=90, theta2=-90))
    ax.add_patch(Arc((750, 250), 120, 120, theta1=90, theta2=-90))
    ax.add_patch(Arc((750, 250), 120, 120, theta1=-90, theta2=90))
    ax.hlines([30, 30, 470, 470], [0, 800] * 2, [140, 940] * 2)
    ax.add_patch(Arc((892.5, 250), 475, 475, theta1=112.5, #892.5, 0
                        theta2=-112.5))
    ax.add_patch(Arc((52, 250), 475, 475, theta1=-68.5, #52, 0
                        theta2=68.5))
    ax.add_patch(Arc((47.5, 250), 15, 15, theta1=0, theta2=360)) # 47.5, 0
    ax.add_patch(Arc((892.5, 250), 15, 15, theta1=0, theta2=360)) #892.5, 0
    #ax.add_patch(Circle((470, 0), 60, facecolor='none', lw=2))

    # Text for score, time and decsription
    ax.text(20, 520, playername, 
           fontsize=16, fontweight='bold', label='playername')
    #ax.text(680, 520, "WAS", 
    #       fontsize=16, fontweight='bold', label='away')
    return fig, ax
