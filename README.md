# Gerenciador de Tarefas via CLI
Este gerenciador de tarefas serve para ajudar o usuário a entender melhor o funcionamento de python, a leitura de arquivos, o uso de arrays e, principalmente, organizar as próprias idéias no projeto.

---

## Changelog
Changelog manual para me manter a par do que estou fazendo.

### 18/11/2026 
- Base criada: o gerenciador realiza a leitura de um arquivo .json chamado "tarefas.json", cujo qual precisa possuir pelo menos um par de colchetes `[]` e insere os dados que o usuário quer inserir, além de salvar no arquivo e listar esses dados. <strong>Ainda não é possível ~~remover, marcar como concluído nem~~ criar arquivos próprios, como outras listas</strong>. 
- Repositório modificado para manter o foco apenas no projeto do sistema de tarefas. 
- Readme atualizado com [Changelog](#Changelog) organizado por data e [To Do](#To-Do) list.
- Adicionadas as funcionalidades de <strong>marcar tarefa como concluída</strong> e <strong>remover tarefa da lista</strong>, com a própria lista tendo seu index atualizado.
- Código separado em funções para facilitar controle e escalamento.
- Prevenção de erros de digitação do usuário como caracteres inválidos ou números fora do escopo no menu.
- Tarefas sendo exibidas a cada menu quando há interação necessária.
- Sistema agora salva no momento da inserção da tarefa (se você iniciava o programa às 23:59 e salvava algo às 00:00, o código considerava a data em que o programa iniciou, ou seja, na data anterior).
- Conteúdo fica salvo com encoding UTF-8.

### 19/11/2026
- Laço principal foi colocado no main().
- Corrigido erro em que eu estava utilizando a lista do menu para concluir ou remover itens.
- Corrigida formatação do documento. Agora o arquivo salva mesmo com acentos ao invés de salvar como `Programa\u00e7\u00e3o`.
- Corrigidas algumas variáveis que não tinham uso.
- Aplicado o padrão snake_case nas variáveis.
- Outros blocos repetidos foram inseridos em uma única função.
- `verificar_escolha` retorna `None` ao invés de 0.
- Removida mensagem dizendo para utilizar 0 para cancelar no menu principal.
- `menu_loop` sem uso foi removido.

---

## To-Do List (lista de afazeres para a lista de tarefas, redundante mas é isso aí mesmo)
- [x] Opção `Remover tarefa` funcionando.
- [x] Opção `Marcar como concluída` funcionando.
- [x] Verificar e validar as respostas do usuário para prevenir erros.
- [ ] Impedir inserção de tarefas ~~com apenas uma ou duas palavras~~ vazias.
- [ ] Padronizar a linguagem.
- [ ] Colocar `Data de Conclusão` para as tarefas.
- [ ] Permitir que o sistema rode mesmo sem um arquivo `.json`.
- [ ] Possibilitar a criação de várias listas (pode ser útil).
- [ ] Armazenar e ler o(s) arquivo(s) de tarefas em uma pasta específica do sistema ao invés da raíz onde o projeto se encontra.
- [x] Configurar formatação UTF-8 (acho que seria essa) no arquivo.