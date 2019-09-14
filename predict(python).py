# To add a new cell, type '#%%'
# To add a new markdown cell, type '#%% [markdown]'

#%%
import numpy as np
from keras.preprocessing import image
from tkinter import *
from PIL import ImageTk, Image
from tkinter import filedialog
import os
from keras.models import load_model


#%%
classifier = load_model('mymodel.h6')


#%%
classifier.compile(optimizer = 'adam', loss = 'categorical_crossentropy', metrics = ['accuracy'])


#%%
root = Tk()
root.geometry("550x300+300+150")
root.resizable(width=True, height=True)
def openfn():
    filename = filedialog.askopenfilename(title='open')
    return filename
def open_img():
    x = openfn()
    test_image = image.load_img(x, target_size = (128, 128))
    test_image = image.img_to_array(test_image)
    test_image = np.expand_dims(test_image, axis = 0)
    result = classifier.predict_classes(test_image)
    print(result)
    index=['Corn_(maize)___Cercospora_leaf_spot Gray_leaf_spot',
    'Corn_(maize)___Common_rust_',
    'Corn_(maize)___Northern_Leaf_Blight',
    'Corn_(maize)___healthy',
    'Grape___Black_rot',
    'Grape___Esca_(Black_Measles)',
    'Grape___Leaf_blight_(Isariopsis_Leaf_Spot)',
    'Grape___healthy',
    'Orange___Haunglongbing_(Citrus_greening)',
    'Potato___Early_blight',
    'Potato___Late_blight',
    'Potato___healthy',
    'Squash___Powdery_mildew']

    print(str(index[result[0]]))
    label = Label( root, text="Prediction : "+str(index[result[0]]))
    label.pack()
    if(result == 0):
        text = "Nitrogen Phosphorus-potash"
        label = Label( root, text="fertilizers : "+text).pack()
        text="Heavily infected leaves become chlorotic and defoliation occurs,\n Leaf symptoms first occur early in the spring when the leaves are unfolding"
        label1= Label( root, text="symptoms : "+text).pack()
    if(result == 1):
        text = "Urea, Di-ammonium phosphate,Pottasium Chlorite"
        label = Label( root, text="fertilizers: "+text).pack()
        text="Early lessions of this are small,necrotic spots and may have a chlorotic hallow-more visible when the leaf is black lit\nLesions progress from lower to upper leaf"
        label1= Label( root, text="symptoms : "+text).pack()
    if(result == 2):
        text = "Urea,Ammonium Nitrate and ammonium sulphate"
        label = Label( root, text="fertilizers: "+text).pack()
        text="Concentric rings of black spots surround the pith which is the naturally darkened core of the cordon,\nFruit spots are visible on white cultivars of wine grapes and table grapes"
        label1= Label( root, text="symptoms : "+text).pack()
    if(result == 3):
        text = "Mixture of cootonseed meal,bone meal and green sand"
        label = Label( root, text="it is perfect: "+text).pack()
        text="They first appear on the lower,older leaves as small brown spots with concentric rings that form bull's eye,\n The stem,fruit and upper portion will become infected,\n Crops can be severly damaged" 
        label = Label( root, text="no symptoms: "+text).pack()
    if(result == 4):
        text = "Hydrogen peroxide"
        label = Label( root, text="fertilizers : "+text).pack()  
        text="Twigs are covered with powdery mass,\nLeaves grow longer and narrower than normal leaves and the margin in curled"
        label1= Label( root, text="symptoms : "+text).pack()
    if(result == 5):
        text = "Organic Fertilizers"
        label = Label( root, text="fertilizer : "+text).pack()  
        text="Irregular dark,purple spots are scattered over the upper leaf surface,\n As the spots enlarge they begain to look like drops of tar and are actually the accummalations of black fruiting bodies(acervuli) of the fungus"
        label1= Label( root, text="symptoms : "+text).pack()
    if(result == 6):
        text = "Phosphorus mixed fertilizer"
        label = Label( root, text="fertilizer : "+text).pack()  
        text="Upward cupping of the leaves,\n Chlorosis of the leaf margins,erect shoots,smaller,misshaped leaflets and severe stunting of the entire plant "
        label1= Label( root, text="symptoms : "+text).pack()
    if(result == 7):
        text = "Phosphorus mixed fertilizer"
        label = Label( root, text="fertilizer : "+text).pack()  
        text="Upward cupping of the leaves,\n Chlorosis of the leaf margins,erect shoots,smaller,misshaped leaflets and severe stunting of the entire plant "
        label1= Label( root, text="symptoms : "+text).pack()   
    if(result == 8):
        text = "Phosphorus mixed fertilizer"
        label = Label( root, text="fertilizer : "+text).pack()  
        text="Upward cupping of the leaves,\n Chlorosis of the leaf margins,erect shoots,smaller,misshaped leaflets and severe stunting of the entire plant "
        label1= Label( root, text="symptoms : "+text).pack()
    if(result == 9):
        text = "Phosphorus mixed fertilizer"
        label = Label( root, text="fertilizer : "+text).pack()  
        text="Upward cupping of the leaves,\n Chlorosis of the leaf margins,erect shoots,smaller,misshaped leaflets and severe stunting of the entire plant "
        label1= Label( root, text="symptoms : "+text).pack()
    if(result == 10):
        text = "Phosphorus mixed fertilizer"
        label = Label( root, text="fertilizer : "+text).pack()  
        text="Upward cupping of the leaves,\n Chlorosis of the leaf margins,erect shoots,smaller,misshaped leaflets and severe stunting of the entire plant "
        label1= Label( root, text="symptoms : "+text).pack()
    if(result == 11):
        text = "Phosphorus mixed fertilizer"
        label = Label( root, text="fertilizer : "+text).pack()  
        text="Upward cupping of the leaves,\n Chlorosis of the leaf margins,erect shoots,smaller,misshaped leaflets and severe stunting of the entire plant "
        label1= Label( root, text="symptoms : "+text).pack()
    if(result == 12):
        text = "Phosphorus mixed fertilizer"
        label = Label( root, text="fertilizer : "+text).pack()  
        text="Upward cupping of the leaves,\n Chlorosis of the leaf margins,erect shoots,smaller,misshaped leaflets and severe stunting of the entire plant "
        label1= Label( root, text="symptoms : "+text).pack()           
        
    img = Image.open(x)
    img = img.resize((250, 250), Image.ANTIALIAS)
    img = ImageTk.PhotoImage(img)
    panel = Label(root, image=img)
    panel.image = img
    panel.pack()
btn = Button(root, text='open image',command=open_img).pack()
root.mainloop()


#%%



#%%



