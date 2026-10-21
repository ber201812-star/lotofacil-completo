#!/usr/bin/env python3
import json,pathlib,sys
p=pathlib.Path(__file__).resolve().parents[1]/'data'/'history.json'
data=json.loads(p.read_text(encoding='utf-8'))
errors=[]
seen=set()
for i,d in enumerate(data):
    c=d.get('concurso');nums=d.get('dezenas',[])
    if c in seen: errors.append(f'concurso duplicado: {c}')
    seen.add(c)
    if len(nums)!=15 or len(set(nums))!=15 or any(not isinstance(n,int) or n<1 or n>25 for n in nums):
        errors.append(f'dezenas inválidas no concurso {c}')
    if i and c!=data[i-1]['concurso']+1: errors.append(f'quebra de sequência entre {data[i-1]["concurso"]} e {c}')
print(f'Registros: {len(data)}')
if data: print(f'Intervalo: {data[0]["concurso"]} a {data[-1]["concurso"]}')
if errors:
    print('\\n'.join(errors));sys.exit(1)
print('Validação OK: sem duplicações, sem falhas de sequência e com 15 dezenas válidas por concurso.')
