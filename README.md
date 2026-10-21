# Lotofácil Completo

Aplicativo web responsivo com gerador de jogos, conferidor, estatísticas e teste retrospectivo walk-forward. Feito para funcionar em navegador móvel e ser publicado em GitHub Pages.

## Conteúdo
- `index.html`, `style.css`, `app.js`: aplicativo.
- `data/history.json`: histórico extraído da planilha fornecida.
- `manifest.json` e `sw.js`: suporte PWA/cache offline.
- `scripts/update_history.py`: atualiza o histórico usando a API pública da CAIXA.
- `scripts/validate_history.py`: valida estrutura e sequência do histórico.

## Publicar no GitHub Pages
1. Descompacte a pasta.
2. Envie todo o conteúdo da pasta para a raiz do repositório (não envie apenas o ZIP).
3. Em Settings → Pages, selecione a branch e a pasta raiz.
4. Abra o endereço publicado. A primeira carga precisa de conexão; depois o app pode abrir offline com o cache.

## Atualizar resultados
Execute `python scripts/update_history.py` em um ambiente com Python e `requests` instalados. O script consulta a API da CAIXA e atualiza `data/history.json`. Em GitHub Actions, agende a execução e faça commit do arquivo atualizado. O botão do app tenta atualizar diretamente no navegador, mas a API pode bloquear chamadas por CORS.

## Limites estatísticos
A estratégia equilibrada mistura amostragem ponderada por frequências históricas e amostragem aleatória, e tenta diversificar jogos. Isso é heurística, não modelo preditivo validado. O teste retrospectivo usa apenas concursos anteriores ao sorteio testado e compara com amostras aleatórias; ele não garante vantagem no futuro. Uma aposta simples tem probabilidade de 1 em 3.268.760 de acertar 15 dezenas. Consulte o preço e as regras atualizadas no portal oficial da CAIXA antes de apostar.

## Histórico incluído
3721 concursos, do 1 (2003-09-29) ao 3721 (2026-06-27). Essa base é a planilha fornecida e não contém automaticamente concursos posteriores ao arquivo original.
