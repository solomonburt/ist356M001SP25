from IPython.display import display
from ipywidgets import interact_manual

text = "student name"  
vals = [ 'IMT', 'IST', 'ADA'] 
min, max, step = 0.0, 4.0, 0.05     

@interact_manual(major=vals, gpa=(min,max,step), name=text)
def on_click(major, gpa, name): 
    if gpa < 1.8:
        status = "Not in good standing"
    elif gpa > 3.4:
        status = "Dean's list"
    else: 
        status = "no list"                            
    display(major)                                            
    display(gpa)                                            
    display(name)
    display(status)