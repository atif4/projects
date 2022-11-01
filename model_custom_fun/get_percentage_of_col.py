def get_percentage_of_col(col_id, mas1 = "Percentage of Patients Haven't Heart Disease: {:.2f}%",
                                mas2 = "Percentage of Patients Have Heart Disease: "):
    zero = len(df[df[col_id] == 0])
    one = len(df[df[col_id] == 1])
    print(mas1 , "{:.2f}%".format((zero / (len(df[col_id]))*100)))
    print(mas2 , "{:.2f}%".format((one / (len(df[col_id]))*100)))
get_percentage_of_target_col('target')