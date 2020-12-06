# this function reads inae from a path and returns a dictionary of images {filename:img}

def read_image_files(image_path,conversion=cv2.COLOR_BGR2RGB):
    image_files = glob.glob(os.path.join(image_path,'*'))
    image_list = [(os.path.basename(f),cv2.imread(f,conversion)) for f in image_files]
    image_dict = {file:image for (file,image) in image_list}
    return image_dict
