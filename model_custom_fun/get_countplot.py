def get_countplot(col_id, df_id):
    sns.countplot(x=col_id, data=df_id, palette="bwr")
    plt.show()