# Normalize
def get_normalize_data(data_id):
    X = (data_id - np.min(data_id)) / (np.max(data_id) - np.min(data_id)).values
    #return X