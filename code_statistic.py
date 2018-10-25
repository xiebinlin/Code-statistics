import os

ROOT_PATH=r"C:\Users\msi\Desktop\monodepth-master"
INCLUDE_EMPTY_LINE=False

def StatCodeLine(file_path,include_empty_line,code_line_cnt):
    count=code_line_cnt
    if os.path.isdir(file_path):
        files=os.listdir(file_path)
        for file in files:
            if file[-2:] != 'py':
                continue
            tmp_path=os.path.join(file_path,file)
            #print tmp_path
            if not os.path.isdir(tmp_path):
                count=count+StatFileLine(tmp_path,include_empty_line)
            else:
                count=StatCodeLine(tmp_path,include_empty_line,count)
    else:
        count=count+StatFileLine(file_path,include_empty_line)
    return count

def StatFileLine(file_name,include_empty_line):
    count=0
    f=open(file_name,'rb')
    while True:
        line=f.readline()
        if not line:
            break
        else:
            if True!=include_empty_line :
                if ""==line.strip() :
                    continue
            count=count+1
    f.close()
    return count

if __name__ == "__main__":
    StatCount=StatCodeLine(ROOT_PATH,INCLUDE_EMPTY_LINE,0)
    print("Total code line count : " + str(StatCount))