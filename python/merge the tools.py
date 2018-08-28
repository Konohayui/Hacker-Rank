def merge_the_tools(string, k):
    # your code goes here
    n = len(string)
    lines = int(n/k)
    l = 0
    
    while l <= lines:
        sub_string_t = list(string[l*k:(l + 1)*k])
        sub_string_u = []
        for s in sub_string_t:
            if s not in sub_string_u:
                sub_string_u.append(s)
                
        print("".join(sub_string_u))
        l += 1
        
        
def merge_the_tools(string, k):
    # your code goes here
    n = len(string)
    lines = int(n/k)
    
    for l in range(lines):
        sub_string_t = list(string[l*k:(l + 1)*k])
        sub_string_u = []
        for s in sub_string_t:
            if s not in sub_string_u:
                sub_string_u.append(s)
                
        print("".join(sub_string_u))
        
        
        
