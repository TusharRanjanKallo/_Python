def Analyze_logs(f):
    Lcount=0
    Icount=0
    Wcount= 0
    Ecount=0
    Error_line=[]
    for line in f:
        Lcount+=1
        if "INFO" in line:
            Icount+=1
        elif "WARNING" in line:
            Wcount+=1
        elif "ERROR" in line:
            Ecount+=1
            Error_line.append(line)
    return Icount,Wcount,Ecount,Error_line,Lcount



def message(msg):
    res=[]
    for line in msg:
        idx=line.find("ERROR")
        if idx!=-1:
            idx+=6
            line=line[idx:]
            res.append(line)
        else:
            pass
    return res

def mostfreq(msg):
    freq_dict={}
    for m in msg:
        if m in freq_dict:
            freq_dict[m]+=1
        else:
            freq_dict[m]=1
    return freq_dict


    
with open(r"C:Docs\system1.log", "r") as f:
    info,warning,error,error_lines,line_count=Analyze_logs(f)
    if len(error_lines)>0:
        error_messages=message(error_lines)
        most_freq_error=mostfreq(error_messages)
        most=max(most_freq_error,key=most_freq_error.get)
        nmost=most_freq_error[max(most_freq_error,key=most_freq_error.get)]
    else:
        most="No ERROR!"
        nmost=0

    summary=["Summary of system.log:\n",f"Total line in the file: {line_count}\n",f"Total no. of INFO count: {info}\n",f"Total no. of WARNING count: {warning}\n",f"Total no. of ERROR count:{error}\n",f"Most frequent ERROR: {most}({nmost} times)\n"]



with open(r"C:Docs\log_summary1.txt","w") as s:
    for i in summary:
        s.write(str(i))
    print("Summary has been updated!")