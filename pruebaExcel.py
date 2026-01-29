import pandas as pd
if __name__ == "__main__":
    df = pd.read_excel('Example.xlsx')
    laboratorios = df['Laboratorio / Ubicación'].unique()

    i = 0
    for lab in laboratorios:
        print(i,lab)
        i+=1