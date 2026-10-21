#!/usr/bin/env python3
"""Atualiza data/history.json usando a API pública da CAIXA."""
import json, pathlib, time, sys
from datetime import datetime
import requests

ROOT=pathlib.Path(__file__).resolve().parents[1]
OUT=ROOT/'data'/'history.json'
API='https://servicebus2.caixa.gov.br/portaldeloterias/api/lotofacil'
HEADERS={'User-Agent':'Mozilla/5.0','Accept':'application/json, text/plain, */*'}
def date_norm(s):
    if not s: return ''
    for fmt in ('%d/%m/%Y','%Y-%m-%d'):
        try:return datetime.strptime(s,fmt).strftime('%Y-%m-%d')
        except ValueError:pass
    return s
def main():
    sess=requests.Session();sess.headers.update(HEADERS)
    try:
        r=sess.get(API,timeout=25);r.raise_for_status();latest=r.json()
        last=int(latest.get('numero') or latest.get('numeroConcurso') or latest.get('concurso'))
    except Exception as e:
        sys.exit(f'Não foi possível consultar o último concurso: {e}')
    old=[]
    if OUT.exists():
        try:old=json.loads(OUT.read_text(encoding='utf-8'))
        except Exception:old=[]
    by={int(x['concurso']):x for x in old if 'concurso' in x}
    start=max(1,(max(by) if by else 0)+1)
    for c in range(start,last+1):
        try:
            r=sess.get(f'{API}/{c}',timeout=20);r.raise_for_status();x=r.json()
            nums=sorted(int(n) for n in (x.get('listaDezenas') or x.get('dezenas') or []))
            if len(nums)==15 and len(set(nums))==15 and all(1<=n<=25 for n in nums):
                by[c]={'concurso':c,'data':date_norm(x.get('dataApuracao') or x.get('dataSorteio')),'dezenas':nums}
            else: print(f'Aviso: concurso {c} retornou dados incompletos.')
            time.sleep(.05)
        except Exception as e: print(f'Aviso: falha no concurso {c}: {e}')
    result=[by[k] for k in sorted(by)]
    OUT.write_text(json.dumps(result,ensure_ascii=False,separators=(',',':')),encoding='utf-8')
    print(f'Histórico salvo: {len(result)} concursos; último concurso local: {result[-1]["concurso"] if result else "nenhum"}; API informa até {last}.')
if __name__=='__main__':main()
