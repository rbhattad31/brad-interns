import scipy.io as syio
n = 1706256
syio.savemat('num.mat', {'num': n})
matlab_file_contents = syio.loadmat('num.mat')
print(matlab_file_contents)
matlab_file_contents = syio.whosmat('num.mat')
print(matlab_file_contents)
#string Input
import scipy.io as syio
string = 'Ayush Bhattad'
syio.savemat('str.mat', {'str': string})
matlab_file_contents = syio.loadmat('str.mat')
print(matlab_file_contents)
matlab_file_contents = syio.whosmat('str.mat')
print(matlab_file_contents)
