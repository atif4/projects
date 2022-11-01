def get_group_cols(col_id):
    return df.groupby([col_id]).mean()
# it group all the col by one particular col value. such as,col name == target  (0,1)