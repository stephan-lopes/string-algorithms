if __name__ == "__main__":
    s = "Compre 1 e Leve 2"
    ld = [i for i in s if i.isdigit()][-1]
    print(ld)