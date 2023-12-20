import os
import cv2
import matplotlib.pyplot as plt
from tkinter import Tk, Button, filedialog

def import_images():
    root = Tk()
    root.withdraw()
    folder_path = filedialog.askdirectory(title="Select Folder Containing Images")
    
    if folder_path:
        images = []
        for filename in os.listdir(folder_path):
            if filename.endswith(".jpg") or filename.endswith(".png"):
                image_path = os.path.join(folder_path, filename)
                image = cv2.imread(image_path)
                images.append(image)
        
        display_images(images)
    else:
        print("No folder selected.")

def display_images(images):
    num_images = len(images)
    fig, axs = plt.subplots(nrows=num_images, ncols=2, figsize=(10, 5*num_images))
    
    for i, image in enumerate(images):
        axs[i, 0].imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
        axs[i, 0].axis('off')
        axs[i, 0].set_title('Image {}'.format(i+1))
        
        blue_hist = cv2.calcHist([image], channels=[0], mask=None, histSize=[256], ranges=[0, 256])
        axs[i, 1].plot(blue_hist, color='blue')
        axs[i, 1].set_xlim([0, 256])
        axs[i, 1].set_title('Histogram (Blue Channel)')
        
    plt.tight_layout()
    plt.show()

# GUI initialization
root = Tk()
root.title("Image Analyzer")

button = Button(root, text="Analyze DAPI", command=import_images)
button.pack(padx=10, pady=10)

root.mainloop()