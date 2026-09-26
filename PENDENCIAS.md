# Pendências de design

Revisão das telas do protótipo feita antes de começar o back-end (26/09/2026).
Lista os fluxos que o sistema precisa para funcionar e que ainda não têm tela.

## Já resolvido nesta revisão

- **Esqueci minha senha** (login): pedir o link por e-mail, mensagem genérica que não revela se o e-mail existe, prévia do e-mail, criação da nova senha e aviso de link vencido ou já usado. O link vale 1 hora, funciona uma vez e um pedido novo cancela o anterior. Depois de salvar, a conta sai de todos os aparelhos e volta para o login.
- **Responsividade:** todas as telas e janelas foram abertas em 390 px de largura, sem nada saindo da tela.

## Etapa 1 do design: acesso e conta (feito em 26/09)

Para ver cada situação no protótipo, use o painel "Protótipo · ver outras situações" embaixo do login: **Situação do login**, **Entrar como** (dono ou funcionária) e **Assinatura da loja**.

- **Visão do funcionário:** a Camila (funcionária) vê Início, Orçamentos, Clientes, Estoque, Tarefas, Agenda e Configurações. Não vê Faturamento, Metas, Relatórios, Meu plano, Equipe nem dados da loja. No estoque só consulta, sem preço de custo e sem o valor total em estoque. Se abrir uma página que não é dela, aparece "Esta área é do dono da loja".
- **Configurações em abas:** Perfil, Segurança, Equipe e Dados da loja (o funcionário vê só Perfil e Segurança).
- **Equipe:** lista com papel e situação, convidar pessoa por e-mail (o convite vale 48 horas), alterar papel, desativar (pede para quem vão as tarefas pendentes e desconecta a pessoa de todos os aparelhos), reativar, reenviar e cancelar convite. A loja nunca fica sem um dono ativo. Quadro "O que cada papel vê".
- **Segurança da conta:** alterar a senha (pede a senha atual; os outros aparelhos são desconectados), lista de aparelhos conectados com "Desconectar" e "Sair de todos os outros aparelhos" com confirmação.
- **Menu da conta:** clicar no nome abre Minha conta, Segurança da conta e Sair.
- **Situações do login:** entrada pelo site (Área do CRM, a pessoa digita o endereço da loja), loja não encontrada, e-mail ou senha incorretos (mensagem única), muitas tentativas (espera até um horário), usuário desativado, sessão expirada e assinatura encerrada.
- **Pagamento em atraso:** faixa de aviso durante os 15 dias de tolerância. Depois, tela "Acesso pausado": o dono só consegue abrir Meu plano para pagar; o funcionário vê que precisa falar com o dono. Meu plano mostra a mensalidade em atraso com o botão de pagar.

## Etapa 2 do design: pagamento direto, exportação e atendimento (feito em 26/09)

- **Pagamento fora do Asaas** (painel Nortiq): ao cadastrar a loja, escolher "Pelo Asaas" ou "Direto com a Nortiq" (Pix, transferência, dinheiro ou outra forma). Na ficha da loja: **Registrar pagamento** (mês, valor, data e forma), histórico dos pagamentos com quem registrou, **Estornar** com motivo (o registro fica riscado, nunca some) e **Alterar forma de cobrança**. A regra de atraso (15 dias) vale igual para as duas formas. Na loja, o Meu plano mostra a chave Pix da Nortiq e o botão para enviar o comprovante pelo WhatsApp.
- **Exportar os dados da loja** (Configurações, Dados da loja, só o dono): arquivo .zip com uma planilha por assunto. O link vale 7 dias e também vai por e-mail. Lembrado na janela de cancelamento e no aviso de assinatura cancelada; na assinatura encerrada dá para pedir a cópia por e-mail.
- **Atendimento pelo painel Nortiq** (ficha da loja, abas Resumo, Acesso e suporte, Atendimentos): enviar link de nova senha, liberar login bloqueado por tentativas, desconectar de todos os aparelhos, trocar o e-mail de acesso do dono (pede como o pedido foi confirmado), reenviar convite e convidar novo dono. Cada ação fica registrada. A equipe Nortiq vê só quem tem acesso à loja, nunca clientes, orçamentos, estoque ou faturamento.

### Decisões de 26/09
- **Cópia de segurança:** cópias automáticas do Neon (voltar o banco a qualquer momento dos últimos dias) + botão "Exportar dados" para a loja. Cópia semanal separada por loja fica para depois.
- **Assinatura paga fora do Asaas:** permitida; a equipe Nortiq registra cada pagamento no painel.

## Falta desenhar para a primeira versão

Ordem sugerida: primeiro o que impede a loja de usar o sistema no dia a dia.

### Acesso e conta
1. ~~Equipe~~, ~~Segurança da conta~~, ~~Erros do login~~, ~~Sessão expirada~~ e ~~Pagamento em atraso~~: feitos na etapa 1 (acima).
2. **Técnicos da agenda** (nome e cor): cadastrar na Equipe ou na Agenda.
3. **Login da administração Nortiq:** endereço próprio, e-mail e senha, recuperação de senha e verificação em duas etapas (código no celular), já que o painel troca e-mail de dono e registra pagamentos. Tirar o link "Equipe Nortiq? Acessar a administração" do login das lojas, que existe só no protótipo.

### Dados do dia a dia
4. **Clientes:** novo cliente, editar, excluir (com confirmação; a ficha some da lista e o histórico fica guardado), adicionar equipamento, registrar manutenção feita.
5. **Orçamentos:** editar os dados depois de criado (produto, valor, pagamento, endereço) e excluir (com confirmação).
6. **Tarefas:** nova tarefa, editar, excluir.
7. **Agenda:** editar, concluir e cancelar agendamento (com confirmação no cancelamento).
8. **Estoque:** histórico de movimentações do produto; registrar entrada, saída, perda, devolução e ajuste; desativar produto em vez de excluir.

### Faturamento
9. Novo lançamento (receita ou despesa), editar, marcar como recebido (total ou parcial), cancelar com motivo, ver os cancelados. Mostrar quando o lançamento veio de uma venda (ORC-0431).
10. **Reabrir venda que já tem dinheiro recebido:** janela que pede a decisão: manter o lançamento ou registrar o estorno.

### Estados gerais
11. **Carregando:** padrão para listas e painéis (esqueleto) e botões com "Salvando" ou "Enviando". O botão do design system já tem esse estado.
12. **Erros gerais:** sem conexão, erro inesperado ("Não foi possível salvar. Tente de novo.") e página não encontrada.
13. **Loja nova, sem dados:** estados vazios de Início, Orçamentos, Clientes, Estoque (sugerindo importar a planilha), Faturamento, Agenda e Metas (definir a primeira meta).

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
- Cópia semanal separada por loja no armazenamento de arquivos (além das cópias do Neon).
- Pedido de ajuda enviado de dentro do CRM (hoje o pedido chega pelo WhatsApp).
- Histórico de alterações visível para o dono.
- Permissões personalizadas por funcionário.
- Configurações da plataforma no painel Nortiq (dias de tolerância do atraso) e cadastro de cupons.

## O que já estava certo

- Confirmações com motivo em "Cancelar assinatura" e "Marcar como perdido".
- Listas com mensagem quando a busca ou o filtro não encontra nada.
- Janelas (novo orçamento, produto, importação, agendamento, nova conta, cancelamento) funcionando no celular.
