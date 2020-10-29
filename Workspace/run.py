def num2txt(num, k=3):
    numstr = str(num)
    txt = ""
    mismatch = len(numstr) % k
    if mismatch:
        numstr = "0" * (k - mismatch) + numstr
    start = 0
    for end in range(k, len(numstr)+1, k):
        txt += chr(int(numstr[start:end]))
        start = end
    return txt

def stuff():
    # nice gary
    import pandas as pd 
    from IPython.display import display

    print("Input")
    df = pd.read_csv("input.csv")
    df.index = [''] * len(df)
    display(df)

    print("Output")
    display(df[::-1])