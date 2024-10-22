def dot_product(vector1, vector2):
    return sum(a * b for a, b in zip(vector1, vector2))

if __name__ == "__main__":
    v1 = list(map(int, input("Enter elements of the first vector (space-separated): ").split()))
    v2 = list(map(int, input("Enter elements of the second vector (space-separated): ").split()))
    result = dot_product(v1, v2)
    print(f"The dot product of the vectors is: {result}")
#changes

