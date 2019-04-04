with open('master.data', 'r') as f:
    lines = f.readlines()

import re as r

with open('final.txt','w+') as n:
    req_lines = n.readlines()
    for i in range(0,len(lines)-1):
        x = r'\[\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}.\d{3}Z\]'    #to remove date
        u = r'(\\\w\d*\w\[\d*\w\[\d*-\d*-\d* \d*:\d*:\d*.\d*\])'  # to remove starting u
        p = r'(\d*[-/]\d*[-/]\d* \d*:\d*:\d*)'
        z= r'(\d*[-/]\d*[-/T ]\d*[: ]\d*:\d*[.:]\d*[,.+Z]\d*)'
        re = r'\w\d* \d*:\d*:\d*.\d*\s*1 \w*.\w*:\d*\]'



        combined= r'|'.join((x,u,z,p,re))
        remove_date = lines[i].strip('{"log":"').replace('"stream":', '').replace('"time":', '')

        log = r.sub(combined, '', remove_date)
        y = r.sub('[{}""]', '', log)
        if y[0] == ' ': y = y.strip()

        n.write(y+'\n')

with open('final.txt','r') as n:
    req_lines = n.readlines()
    wanted_list=['INFO','info','ERROR','error','stderr','WARNING','REPL','CRIT','DEBUG','AUDIT','warn','NETWORK','ACCESS','FINE','CONTROL','RECOVERY','STORAGE','FTDC','ASIO','INDEX','COMMAND','REPL_HB']
    with open('cleanedFinal.txt', 'w+') as c:
        for i in wanted_list:
            for j in req_lines:
                if i in j:
                    c.write(j)

