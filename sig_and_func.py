# coding:utf-8

import idaapi
import idautils
import idc
import os

try:
    import cPickle as pickle
except:
    import pickle

idaapi.autoWait()

def apply_sig(sig_name):
    return idc.ApplySig(sig_name)

"""
@return: func_details: {ea:(func_name, is_lib_func), ... }
"""
def extract_func_type():
    func_details = {} 
    for ea in idautils.Functions():
        func = idaapi.get_func(ea)
        if not idaapi.is_func_entry(func):
            continue
        if ea in func_details:
            raise Exception("ERROR. Two functions are in a same address")
        func_details[ea] = (idc.GetFunctionName(ea), idaapi.FUNC_LIB & func.flags, func.endEA)
    return func_details

apply_sig('libc6_2.23-0ubuntu9_i386')
idaapi.autoWait()
func_details = extract_func_type()


outfile_name = os.path.basename(idaapi.get_input_file_path()) + "_func_details"

f = open(outfile_name, 'w')
pickle.dump(func_details, f)
f.close()
idc.Exit(0)

