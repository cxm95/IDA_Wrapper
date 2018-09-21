#coding:utf-8

import subprocess
import os
import sys
import time
import argparse
import logging
import shutil
import IPython
logging.basicConfig()
l = logging.getLogger("IDA.Analyser")
l.setLevel(logging.WARNING)

try:
    import cPickle as pickle
except:
    import pickle

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="sFuzz IDA Analyser interface.")
    parser.add_argument('-b', '--binary', help="path to the binary to be analysed.")
    parser.add_argument('-o', '--output', help="output folder to cache the analyse result.")
    
# init pathes
    script_path = 'sig_and_func.py'
    script_a_path = os.path.join(os.path.split(os.path.realpath(__file__))[0], script_path)

    binary_r_path = os.path.basename(args.binary)
    binary_a_path = os.path.abspath(args.binary)
    ida_r_path = 'ida_linux/idaq'
    ida_a_path = os.path.join(os.path.split(os.path.realpath(__file__))[0], ida_r_path)
    tmpfile_path = binary_a_path + "_func_details"
    if not os.path.isfile(tmpfile_path):

        l.warning("Analysis %s,  %s with %s to %s" % (ida_a_path, binary_a_path, script_a_path, args.output))

        server_args = ['Xvfb',':19','-screen','0','1280x1024x8','-fbdir','/var/tmp']
        xplayer = subprocess.Popen(server_args)
        new_env = os.environ.copy()
        new_env['DISPLAY'] = ':19'
        ida_process = subprocess.Popen([ida_a_path, "-A", "-S"+script_a_path, binary_a_path], env=new_env)
        ida_process.wait()
        
        xplayer.terminate()
        idb_a_path = binary_a_path + ".idb"
        l.warning('Cleaning %s' % idb_a_path)
        os.remove(idb_a_path)

    if not args.output:
        l.warning('no output.')
        sys.exit(0)
    
    output_f_a_path = args.output
    output_a_path = os.path.join(output_f_a_path, os.path.basename(tmpfile_path))
    l.warning("Copying %s to %s." %(tmpfile_path, output_a_path))
    if not os.path.isdir(output_f_a_path):
        sys.exit(0)
    if not os.path.isfile(tmpfile_path):
        shutil.move(tmpfile_path,output_f_a_path)
        
    l.warning('IDA Analysis finished. Outfile: %s' % output_a_path)
