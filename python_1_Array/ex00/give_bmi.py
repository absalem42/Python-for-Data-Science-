import numpy as np




def give_bmi(height: list[int | float], weight: list[int | float]) -> list[int | float]:
    if len(height) !=  len(weight):
        raise ValueError("Height and weight lists must be the same length.")
    Bmi = []
    for h, w, in height, weight:
        Bmi.append(w / h**2)
    return Bmi




# def apply_limit(bmi: list[int | float], limit: int) -> list[bool]:
# #your code here











def main():
    try:
        height = [2.71, 1.15]
        weight = [165.3, 38.4]
        bmi = give_bmi(height, weight)
        print(bmi, type(bmi))
        # print(apply_limit(bmi, 26))
    except ValueError as e:
        print(ValueError.__name__ + ":", e)



if __name__ == "__main__":
    main()