# Invisible-Cloak
  Simple Mask background project using  Opnecv and numpy in Python
## Table of contents
  * [General Information](#GeneralInformation)
  * [Python Library](#Pythonlibrary)
  * [Change Color](#colorchange)
  * [Screenshots](#result)
  * [Contact](#contact)
  
## <a name="GeneralInformation"></a>General Information:
  This project is basically mask the current video which has a color(We specify) to an Another Image

## <a name="Pythonlibrary"></a>Python Library:
  * Opencv version : 3.1.14
  * Numpy version  : 1.20.0

## <a name="colorchange"></a>Change Color:
  The `Cloak.py` file will mask the white color to `back.jpg` image.
    
You can even mask the color as you want by making changes in the below code:
      ![ss1](https://user-images.githubusercontent.com/55131291/110211691-c9883e00-7ebd-11eb-949b-ff1f7c8bacc5.png)
In the above code, change the range in which your hsv color lies.
  ```
  low_val_b = np.array([0,0,0])
  up_val_b = np.array([0, 0, 255])
  ```
Make your changes here.

## <a name="result"></a>Screenshots:

My Actual Background:

![before](https://user-images.githubusercontent.com/55131291/110211931-ed984f00-7ebe-11eb-8231-901f81ea592c.png)

After Execution:

![after](https://user-images.githubusercontent.com/55131291/110211933-eec97c00-7ebe-11eb-98a5-23a4eb185247.png)

## <a name="contact"></a>Contact:
  * Twitter : [@saisrinivenkat](https://twitter.com/saisrinivenkat)
  * Mail    : <saisrinivenkat000@gmail.com>
  

  
