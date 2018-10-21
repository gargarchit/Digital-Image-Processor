import numpy as np
import matplotlib.pyplot as plt
import utils.utils as utils


def left_sobel(img):

    """
    Applies left sobel filter to a colored numpy image.

    Parameters:
    arg1 (np.array): Numpy image matrix.

    Returns:
    np.array: Filterd left sobel image.
    """

    kernel = np.array([[1., 0., -1.],
                   [2., 0., -2.],
                   [1., 0., -1.]])

    img = utils.rgb2gray(img)

    new_image = np.zeros((img.shape[0]-kernel.shape[0]+1, img.shape[1]-kernel.shape[1]+1))

    for ix in range(new_image.shape[0]):
        for iy in range(new_image.shape[1]):
            im_patch = img[ix:ix+kernel.shape[0], iy:iy+kernel.shape[1]]
            h_prod = im_patch * kernel

            new_image[ix, iy] = max(0, h_prod.sum())
    new_image = new_image.astype(np.uint8)
    new_image = utils.InvertGrayImg(new_image)
    return new_image


def right_sobel(img):

    """
    Applies right sobel filter to a colored numpy image.

    Parameters:
    arg1 (np.array): Numpy image matrix.

    Returns:
    np.array: Filterd right sobel image.

    """

    kernel = np.array([[-1., 0., 1.],
                   [-2., 0., 2.],
                   [-1., 0., 1.]])

    img = utils.rgb2gray(img)

    new_image = np.zeros((img.shape[0]-kernel.shape[0]+1, img.shape[1]-kernel.shape[1]+1))

    for ix in range(new_image.shape[0]):
        for iy in range(new_image.shape[1]):
            im_patch = img[ix:ix+kernel.shape[0], iy:iy+kernel.shape[1]]
            h_prod = im_patch * kernel

            new_image[ix, iy] = max(0, h_prod.sum())
    new_image = new_image.astype(np.uint8)
    new_image = utils.InvertGrayImg(new_image)
    return new_image


def top_sobel(img):

    """
    Applies top sobel filter to a colored numpy image.

    Parameters:
    arg1 (np.array): Numpy image matrix.

    Returns:
    np.array: Filterd top sobel image.
    """

    kernel = np.array([[1., 2., 1.],
                   [0., 0., 0.],
                   [-1., -2., -1.]])

    img = utils.rgb2gray(img)

    new_image = np.zeros((img.shape[0]-kernel.shape[0]+1, img.shape[1]-kernel.shape[1]+1))

    for ix in range(new_image.shape[0]):
        for iy in range(new_image.shape[1]):
            im_patch = img[ix:ix+kernel.shape[0], iy:iy+kernel.shape[1]]
            h_prod = im_patch * kernel

            new_image[ix, iy] = max(0, h_prod.sum())
    new_image = new_image.astype(np.uint8)
    new_image = utils.InvertGrayImg(new_image)
    return new_image


def gray_scale(img):
    """
    Applies gray scale filter to a colored numpy image.

    Parameters:
    arg1 (np.array): Numpy image matrix.

    Returns:
    np.array: Filterd gray scale image.
    """
    return utils.rgb2gray(img).astype(np.uint8)


def outline(img):

    """
    Applies Outline filter to a colored numpy image.

    Parameters:
    arg1 (np.array): Numpy image matrix.

    Returns:
    np.array: Filtered outlined image.
    """

    kernel = np.array([[-1., -1., -1.],
                   [-1., 8., -1.],
                   [-1., -1., -1.]])

    img = utils.rgb2gray(img)

    new_image = np.zeros((img.shape[0]-kernel.shape[0]+1, img.shape[1]-kernel.shape[1]+1))

    for ix in range(new_image.shape[0]):
        for iy in range(new_image.shape[1]):
            im_patch = img[ix:ix+kernel.shape[0], iy:iy+kernel.shape[1]]
            h_prod = im_patch * kernel

            new_image[ix, iy] = max(0, h_prod.sum())
    new_image = new_image.astype(np.uint8)
    new_image = utils.InvertGrayImg(new_image)
    return new_image


def rotate(img):
    """
    Rotates the image by 90 degrees.

    Parameters:
    arg1 (np.array): Numpy image matrix.

    Returns:
    np.array: Rotated image.
    """
    new_image=np.zeros_like(img)
    new_image=new_image.reshape(img.shape[1],img.shape[0],3)
    imgr=img[:,:,0]
    imgg=img[:,:,1]
    imgb=img[:,:,2]
    imgr=np.transpose(imgr)
    imgg=np.transpose(imgg)
    imgb=np.transpose(imgb)
    new_image[:,:,0]=imgr
    new_image[:,:,1]=imgg
    new_image[:,:,2]=imgb
    return new_image



def invert(img):

    """
    Rotates the image by 180 degrees.

    Parameters:
    arg1 (np.array): numpy image matrix.

    Returns:
    np.array: Inverted image.
    """

    new_img = np.zeros_like(img)

    for ix in range(new_img.shape[0]):
        for iy in range(new_img.shape[1]):
            new_img[ix, iy] = img[img.shape[0]-ix-1, img.shape[1]-iy-1]
    return new_img


def negative(img):

    """
    Negates the given image.

    Parameters:
    arg1 (np.array): numpy image matrix.

    Returns:
    np.array: Negative of the given image.
    """

    new_img = np.zeros_like(img)

    for ix in range(new_img.shape[0]):
        for iy in range(new_img.shape[1]):
            for iz in range(new_img.shape[2]):
                new_img[ix, iy, iz] = 255 - img[ix, iy, iz]

    return new_img.astype(np.uint8)


def emboss(img):

    """
    Applies Emboss filter to a colored numpy image.

    Parameters:
    arg1 (np.array): Numpy image matrix.

    Returns:
    np.array: Filtered Embossed image.
    """

    kernel = np.array([[-2., -1., 0.],
                   [-1., 1., 1.],
                   [0., 1., 2.]])

    new_image = np.zeros((img.shape[0]-kernel.shape[0]+1, img.shape[1]-kernel.shape[1]+1, 3))

    for iz in range(new_image.shape[2]):
        for ix in range(new_image.shape[0]):
            for iy in range(new_image.shape[1]):
                im_patch = img[ix:ix+kernel.shape[0], iy:iy+kernel.shape[1], iz]
                h_prod = im_patch * kernel
                new_image[ix, iy, iz] = max(0, h_prod.sum())

    return new_image.astype(np.uint8)


def sharpen(img):

    """
    Applies Sharpen filter to a colored numpy image.

    Parameters:
    arg1 (np.array): Numpy image matrix.

    Returns:
    np.array: Filtered Sharpen image.
    """

    kernel = np.array([[0., -1., 0.],
                   [-1., 5. , -1.],
                   [0., -1., 0.]])

    new_image = np.zeros((img.shape[0]-kernel.shape[0]+1, img.shape[1]-kernel.shape[1]+1, 3))

    for iz in range(new_image.shape[2]):
        for ix in range(new_image.shape[0]):
            for iy in range(new_image.shape[1]):
                im_patch = img[ix:ix+kernel.shape[0], iy:iy+kernel.shape[1], iz]
                h_prod = im_patch * kernel
                new_image[ix, iy, iz] = max(0, h_prod.sum())

    return new_image.astype(np.uint8)



def sepia(img):

    """
    Applies sepia filter to the given image.

    Parameters:
    arg1 (np.array): numpy image matrix.

    Returns:
    np.array: Image with sepia filter applied.
    """

    new_img = np.zeros_like(img)

    for ix in range(new_img.shape[0]):
        for iy in range(new_img.shape[1]):
            new_img[ix, iy, 0] = 0.393*img[ix,iy,0] + 0.769*img[ix,iy,1] + 0.189*img[ix,iy,2]
            new_img[ix, iy, 1] = 0.349*img[ix,iy,0] + 0.686*img[ix,iy,1] + 0.168*img[ix,iy,2]
            new_img[ix, iy, 2] = 0.272*img[ix,iy,0] + 0.534*img[ix,iy,1] + 0.131*img[ix,iy,2]

    return new_img.astype(np.uint8)



def identity(img):

    """
    Applies identity filter to a colored numpy image.

    Parameters:
    arg1 (np.array): Numpy image matrix.

    Returns:
    np.array: Identity image.
    """

    kernel = np.array([[0., 0., 0.],
                   [0., 1. , 0.],
                   [0., 0., 0.]])

    new_image = np.zeros((img.shape[0]-kernel.shape[0]+1, img.shape[1]-kernel.shape[1]+1, 3))

    for iz in range(new_image.shape[2]):
        for ix in range(new_image.shape[0]):
            for iy in range(new_image.shape[1]):
                im_patch = img[ix:ix+kernel.shape[0], iy:iy+kernel.shape[1], iz]
                h_prod = im_patch * kernel
                new_image[ix, iy, iz] = max(0, h_prod.sum())

    return new_image.astype(np.uint8)


def crop(img, top_left, bottom_right):

    """
    Crops the image to given dimension.

    Parameters:
    arg1 (np.array): Numpy image matrix.
    arg2 (np.array): Top left corner co-ordinates.
    arg3 (np.array): Top right corner co-ordinates.

    Returns:
    np.array: Cropped image.
    """

    if(top_left[0]<0 or top_left[1]<0 or bottom_right[0]<0 or bottom_right[1]<0):
        print("\nCan not Crop!")
        return img

    if(bottom_right[0] > img.shape[0] or bottom_right[1] > img.shape[1] or top_left[0] > bottom_right[0] or top_left[1] > bottom_right[1]):
        print("\nCan not Crop!")
        return img

    new_img = np.zeros((bottom_right[0] - top_left[0], bottom_right[1] - top_left[1], 3))
    for ix in range(new_img.shape[0]):
        for iy in range(new_img.shape[1]):
            new_img[ix, iy, :] = img[ix + top_left[0], iy + top_left[1], :]

    return new_img.astype(np.uint8)
