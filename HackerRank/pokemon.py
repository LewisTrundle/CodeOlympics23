import sys

class Euan:
    def __init__(self, x, y, a, b, exp=0):
        self.str = x
        self.max_str = y
        self.a = a
        self.b = b
        self.exp = exp

def training(euan):
    queue = [euan]
    best_euan = euan
    
    while queue:
        current_euan = queue.pop(0)
        
        # train at bank st
        new_str = current_euan.str + current_euan.b
        if new_str > current_euan.max_str:
            if current_euan.exp > best_euan.exp:
                best_euan = current_euan
        else:
            new_exp = current_euan.exp + 1
            queue.append(Euan(new_str, current_euan.max_str, current_euan.a, current_euan.b, new_exp))
        
        # train at the stevie
        new_str = current_euan.str * current_euan.a
        if new_str > current_euan.max_str:
            if current_euan.exp > best_euan.exp:
                best_euan = current_euan
        else:
            new_exp = current_euan.exp + 1
            queue.append(Euan(new_str, current_euan.max_str, current_euan.a, current_euan.b, new_exp))
    
    print(best_euan.exp)
    

x, y, a, b = sys.stdin.read().strip("\n").split(' ')
training(Euan(int(x), int(y), int(a), int(b)))