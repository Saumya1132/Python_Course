import pandas as pd

def transpose_dataframe(df):

    return df.transpose()

# Example usage
if __name__ == "__main__":
    data = {'A': [1, 2, 3], 'B': [4, 5, 6]}
    df = pd.DataFrame(data)
    print("Original DataFrame:")
    print(df)
    
    transposed_df = transpose_dataframe(df)
    print("\nTransposed DataFrame:")
    print(transposed_df)
