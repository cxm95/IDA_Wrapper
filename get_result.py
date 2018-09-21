try:
    import cPickle as pickle
except:
    import pickle


f = open(r"./test_result/pwn20_func_details", 'r')
func_details = pickle.load(f)
f.close()

for ea, (func_name, is_lib, end_addr) in func_details.items():
    print '0x%x - %s - %d - 0x%x' % (ea, func_name, is_lib, end_addr)

