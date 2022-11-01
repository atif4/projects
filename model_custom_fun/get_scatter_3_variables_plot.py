def get_scatter_3_variables_plot(col_id1, col_id2,col_id3,xlabel,ylabel,col,leg1,leg2):
    plt.scatter(x=df[col_id1][df[col_id3]==1], y=df[col_id2][(df[col_id3]==1)], c=col)
    plt.scatter(x=df[col_id1][df[col_id3]==0], y=df[col_id2][(df[col_id3]==0)])
    plt.legend([leg1,leg2])
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.show()