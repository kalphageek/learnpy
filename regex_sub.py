#re.sub(pattern, repl, string, count=0, flags=0)
res = re.sub(r'def\s+([a-zA-Z_][a-zA-Z_0-9]*)\s*\(\s*\):',
               r'static PyObject*\npy_\1(void)\n{',
              'def myfunc():')
#-->'static PyObject*\npy_myfunc(void)\n{'

def dashrepl(matchobj):
    if matchobj.group(0) == '-': return ' '
    else: return '-'
res = re.sub('-{1,2}', dashrepl, 'pro----gram-files')
#-->'pro--gram files'

res = re.sub(r'\sAND\s', ' & ', 'Baked Beans And Spam', flags=re.IGNORECASE)
#-->'Baked Beans & Spam'