def imaginary_dict(lst):
    return {i.real:i.imag for i in lst}
print(imaginary_dict([complex(i) for i in input().split()]))




