#Separate Feature and Target Matrix
def get_seprate_features(f_name):
    global X, y
    X = df.drop(f_name,axis = 1) 
    y = df.target