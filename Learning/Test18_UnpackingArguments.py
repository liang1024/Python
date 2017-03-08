'''
Unpacking Arguments:打包参数
'''

def health_calculator(age, apples_ate, cigs_smomked):
    answer = (100 - age) + (apples_ate * 3.5) - (cigs_smomked * 2)
    print(answer)

buckys_data = [27, 20, 0]

health_calculator(buckys_data[0], buckys_data[1], buckys_data[2])
health_calculator(*buckys_data)
