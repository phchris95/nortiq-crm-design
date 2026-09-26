# Pendências de design

Revisão das telas do protótipo feita antes de começar o back-end (26/09/2026).
Lista os fluxos que o sistema precisa para funcionar e que ainda não têm tela.

## Já resolvido nesta revisão

- **Esqueci minha senha** (login): pedir o link por e-mail, mensagem genérica que não revela se o e-mail existe, prévia do e-mail, criação da nova senha e aviso de link vencido ou já usado. O link vale 1 hora, funciona uma vez e um pedido novo cancela o anterior. Depois de salvar, a conta sai de todos os aparelhos e volta para o login.
- **Responsividade:** todas as telas e janelas foram abertas em 390 px de largura, sem nada saindo da tela.

## Falta desenhar para a primeira versão

Ordem sugerida: primeiro o que impede a loja de usar o sistema no dia a dia.

### Acesso e conta
1. **Equipe** (Configurações): lista de usuários, convidar funcionário por e-mail, trocar o papel (dono ou funcionário), desativar e reativar, reenviar convite. Precisa de confirmação ao desativar. Os técnicos da agenda (nome e cor) também podem ser cadastrados aqui.
2. **Segurança da conta** (Configurações, Perfil): alterar a senha (pede a senha atual) e "Sair de todos os aparelhos".
3. **Erros do login:** e-mail ou senha incorretos (mensagem única, sem dizer qual dos dois), muitas tentativas (esperar alguns minutos), usuário desativado, loja não encontrada (endereço que não existe), assinatura encerrada.
4. **Sessão expirada:** voltar ao login com aviso.
5. **Pagamento em atraso:** faixa de aviso durante a tolerância e, depois do limite, tela "Acesso pausado" que só deixa abrir Meu plano.
6. **Administração Nortiq:** login próprio (admin.nortiq.com.br) com recuperação de senha. Tirar o link "Equipe Nortiq? Acessar a administração" do login das lojas, que existe só no protótipo.

### Dados do dia a dia
7. **Clientes:** novo cliente, editar, excluir (com confirmação; a ficha some da lista e o histórico fica guardado), adicionar equipamento, registrar manutenção feita.
8. **Orçamentos:** editar os dados depois de criado (produto, valor, pagamento, endereço) e excluir (com confirmação).
9. **Tarefas:** nova tarefa, editar, excluir.
10. **Agenda:** editar, concluir e cancelar agendamento (com confirmação no cancelamento).
11. **Estoque:** histórico de movimentações do produto; registrar entrada, saída, perda, devolução e ajuste; desativar produto em vez de excluir.

### Faturamento
12. Novo lançamento (receita ou despesa), editar, marcar como recebido (total ou parcial), cancelar com motivo, ver os cancelados. Mostrar quando o lançamento veio de uma venda (ORC-0431).
13. **Reabrir venda que já tem dinheiro recebido:** janela que pede a decisão: manter o lançamento ou registrar o estorno.

### Estados gerais
14. **Carregando:** padrão para listas e painéis (esqueleto) e botões com "Salvando" ou "Enviando". O botão do design system já tem esse estado.
15. **Erros gerais:** sem conexão, erro inesperado ("Não foi possível salvar. Tente de novo.") e página não encontrada.
16. **Loja nova, sem dados:** estados vazios de Início, Orçamentos, Clientes, Estoque (sugerindo importar a planilha), Faturamento, Agenda e Metas (definir a primeira meta).

### Mensagens das travas de exclusão (decidido em 26/09)
O banco recusa estas ações; as telas precisam explicar o motivo e mostrar o caminho. Textos propostos:

| Situação | Mensagem | Botões |
|---|---|---|
| Excluir cliente com pendências | **Antes de excluir Marta Oliveira.** Ainda há 1 orçamento em negociação, 1 agendamento marcado e 2 tarefas pendentes com este cliente. Encerre ou cancele esses itens e tente de novo. | Ver pendências · Fechar |
| Excluir cliente sem pendências | **Excluir Marta Oliveira?** A ficha sai da lista de clientes. Orçamentos, lançamentos e histórico continuam guardados, e a ficha pode ser restaurada. | Excluir cliente · Cancelar |
| Usar cliente excluído (novo orçamento, tarefa ou agendamento) | Esta ficha foi excluída. Restaure a ficha para usá-la de novo. | Restaurar ficha · Cancelar |
| Desativar usuário com tarefas | **Alan Souza tem 3 tarefas pendentes.** Escolha quem fica com elas antes de desativar. | Campo "Passar para" · Passar tarefas e desativar · Cancelar |
| Desativar usuário sem tarefas | **Desativar Alan Souza?** Ele sai do sistema na hora, em todos os aparelhos. O que ele fez continua registrado, e você pode reativar depois. | Desativar · Cancelar |
| Produto ou técnico desativado | Não aparecem nas listas de escolha. Se o orçamento ou agendamento antigo já usa um deles, ele continua lá, com a marca "desativado". | — |

## Pode ficar para depois

- Listas configuráveis pela loja (origens, formas de pagamento, motivos de perda, categorias).
- Exportar os dados da loja (LGPD e cancelamento).
- Histórico de alterações visível para o dono.
- Permissões personalizadas por funcionário.
- Configurações da plataforma no painel Nortiq (dias de tolerância do atraso) e cadastro de cupons.

## O que já estava certo

- Confirmações com motivo em "Cancelar assinatura" e "Marcar como perdido".
- Listas com mensagem quando a busca ou o filtro não encontra nada.
- Janelas (novo orçamento, produto, importação, agendamento, nova conta, cancelamento) funcionando no celular.
