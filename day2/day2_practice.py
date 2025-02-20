#for i in range(10):
 #   i+=2
  #  print(i)

# def my_range(*args):
#     i=0
#     if len(args)==1:
#         while(i<args[0]):
#             yield i
#             i+=1
#     elif len(args)==2:
#         i=args[0]
#         while i<args[1]:
#             yield i
#             i+=1
#     elif len(args)==3:
#         i=args[0]
#         if args[0]<args[1] and args[-1]>0:
#             while i<args[1]:
#                 yield i
#                 i+=args[-1]
#         elif args[0]>args[1] and args[2]<0:
#             while i>args[1]:
#                 yield i
#                 i+=args[2]
# for i in my_range(10,20,2):
#     print(i)

def generate_permutations(s, current_permutation, permutations):
    # Base case: if the current permutation is the same length as the string, add it to the result
    if len(current_permutation) == len(s):
        permutations.append(current_permutation)
        return
    
    # Recursive case: iterate over each character in the string
    for i in range(len(s)):
        # Skip if the character is already in the current permutation
        if s[i] in current_permutation:
            continue
        # Include the character in the current permutation and recurse
        generate_permutations(s, current_permutation + s[i], permutations)

# Input string
num = "312"

# List to store the permutations
permutations = []

# Generate permutations
generate_permutations(num, "", permutations)

# Print all permutations
for perm in permutations:
    print(perm)

for i in permutations:
    if i>num:
        print("smallest largest number",i)
        break

# def generate_perm(inp_str,lst):
#     while True:
#         str1=''
#         for i in inp_str:
#             if i not in str1:
#                 str1+=i
                


# num=input("enter a number")
# perm=[]
# generate_perm(num,perm)
