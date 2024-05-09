def main():
    rain_mm = 5
    
    # first code:
    if rain_mm < 6 and rain_mm > 4:
        print("illegal")
    else:
        print("legal")
    
    # second code:
    if not (rain_mm == 5):
        print("legal")
    else:
        print("illegal")
    
    # same

    # first code:
    if rain_mm > 20 and rain_mm < 40:
        print("legal")
    else:
        print("illegal")
    
    # second code:
    if not (rain_mm < 20 and rain_mm > 40):
        print("legal")
    else:
        print("illegal")
    
    # different

    # first code:
    if rain_mm > 6 and rain_mm < 4:
        print("illegal")
    else:
        print("legal")
    
    # second code:
    if not (False):
        print("legal")
    else:
        print("illegal")
    
    # same  

if __name__ == "__main__":
    main()