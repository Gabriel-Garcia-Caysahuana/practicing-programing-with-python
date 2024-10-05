import multiprocessing

def sum_pairs(result_pairs):
    suma = sum(i for i in range(1, 1000000) if i % 2 == 0)
    print(f"Suma de pares calculada en el proceso: {suma}")
    result_pairs.value = suma
    print("Valor de result_pairs en el proceso:", result_pairs.value)  # Debugging adicional

if __name__ == "__main__":
    result_pairs = multiprocessing.Pool('i', 0)
    
    process_01 = multiprocessing.Process(target=sum_pairs, args=(result_pairs,))
    process_01.start()
    process_01.join()

    print("Suma de pares:", result_pairs.value)  # Este valor debe reflejar la suma calculada



# import multiprocessing

# def sum_pairs(result_pairs):
#     suma = sum(i for i in range(1, 1000000) if i % 2 == 0)
#     print(f"Suma de pares calculada en el proceso: {suma}")
#     result_pairs.value = suma

# def sum_nopairs(result_nopairs):
#     suma = sum(i for i in range(1, 1000000) if i % 2 != 0)
#     print(f"Suma de impares calculada en el proceso: {suma}")
#     result_nopairs.value = suma

# if __name__ == "__main__":
    # result_pairs = multiprocessing.Value('i', 0)  # 'i' para enteros
    # result_nopairs = multiprocessing.Value('i', 0)  # 'i' para enteros

    # process_01 = multiprocessing.Process(target=sum_pairs, args=(result_pairs,))
    # process_02 = multiprocessing.Process(target=sum_nopairs, args=(result_nopairs,))

    # process_01.start()
    # process_02.start()

    # process_01.join()
    # process_02.join()

    # print("Suma de pares:", result_pairs.value)
    # print("Suma de impares:", result_nopairs.value)