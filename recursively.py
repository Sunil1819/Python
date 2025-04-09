import os
def mergetextfiles(input_dir, output_file):
    with open(output_file,'w') as outfile:
        for root,dirs,files in os.walk(input_dir):
            for file in files:
                if file.endswith('.txt'):
                    file_path = os.path.join(root, file)
                    with open(file_path,'r') as infile:
                        outfile.write(infile.read())
                        outfile.write('\n')
inputdirectory=r'C:\Users\Sunil\handson'
outputfilepath=r'C:\Users\Sunil\handson\virat.txt'
mergetextfiles(inputdirectory,outputfilepath)

