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

## Etapa 3 do design: login da administração Nortiq (feito em 26/09)

- **Endereço próprio** (admin.nortiq.com.br). O link "Equipe Nortiq? Acessar a administração" saiu do login das lojas; no protótipo, o atalho fica no quadro "Protótipo · ver outras situações".
- **Entrada em duas etapas:** e-mail e senha, depois o código de 6 números do aplicativo autenticador do celular (Google Authenticator ou Microsoft Authenticator). Perdeu o celular? Entra com um dos 10 códigos de recuperação, e cada um funciona uma vez.
- **Primeiro acesso pelo convite** (3 passos): criar a senha (pelo menos 12 caracteres e 1 número), ativar o código do celular pelo QR code e guardar os códigos de recuperação.
- **Esqueci minha senha** da administração, com mensagem que não revela se o e-mail existe. O código do celular continua sendo pedido depois da senha nova.
- **Erros:** senha incorreta, código incorreto e muitas tentativas.
- **Segurança da conta** (menu no nome): alterar senha, ver a verificação em duas etapas, gerar novos códigos de recuperação, configurar em outro celular e aparelhos conectados. Na administração, cada entrada vale até 12 horas.
- **Primeiro administrador:** nortiqtec@gmail.com. A conta é criada quando o servidor for instalado: um comando envia o convite para esse e-mail e a senha é criada por você, nunca fica escrita no código.

## Etapa 4 do design: Faturamento da loja (feito em 26/09)

- **Resumo do mês:** recebido, pago, a receber e a pagar (com quantos estão vencidos), e a sobra até agora.
- **Abas:** Todos, A receber, A pagar, Recebidos e pagos, Cancelados. Cada lançamento mostra a situação: a receber, a pagar, parcial, vencido, recebido, pago, cancelado ou estornado.
- **Novo lançamento** (receita ou despesa), com opção "já recebi/já paguei". **Editar** descrição, valor, vencimento, categoria e forma.
- **Registrar recebimento ou pagamento**, total ou parcial (o resto continua em aberto).
- **Estornar** com motivo: o recebimento fica no histórico e o valor volta a ficar em aberto.
- **Cancelar** com motivo: sai das contas e vai para a aba Cancelados. Nada é apagado.
- **Venda fechada** cria sozinha o lançamento a receber. O valor acompanha o orçamento. Reabrir a venda sem dinheiro recebido cancela o lançamento com o motivo.
- **Reabrir venda que já tem dinheiro recebido:** a janela pede a decisão: manter o lançamento ou registrar o estorno (com motivo). Só o dono decide; o funcionário vê um aviso.
- **Ficha do orçamento:** quadro "Financeiro desta venda" com a situação e o botão "Ver no Faturamento" (só para o dono).
- **Perfil do administrador:** aba Perfil em Minha conta para trocar o nome que aparece no painel.

## Etapa 5 do design: Clientes e Orçamentos (feito em 26/09)

- **Novo cliente** (botão ao lado da busca em Clientes): nome, WhatsApp, tipo (cliente ou interessado), bairro, endereço e como chegou. Se o WhatsApp já estiver em outra ficha, a tela avisa e oferece "Abrir a ficha" ou "Salvar mesmo assim" (o mesmo número pode estar em duas fichas, como decidido na revisão do banco).
- **Editar dados** do cliente pela ficha. Trocar o nome atualiza os orçamentos e a agenda dele.
- **Excluir cliente** (só o dono), com as mensagens decididas: com pendências, "Antes de excluir…" e a lista do que falta encerrar (orçamentos em andamento, agendamentos marcados e tarefas pendentes); sem pendências, confirmação. A ficha sai da lista, com **Desfazer** logo depois, e fica na aba **Excluídos**, onde o dono pode **Restaurar ficha**.
- **Cliente excluído no novo orçamento:** ao escrever o nome de uma ficha excluída, aparece "Esta ficha foi excluída. Restaure a ficha para usá-la de novo." com o botão Restaurar ficha (preenche WhatsApp e endereço).
- **Adicionar equipamento:** equipamento (lista do estoque ou texto livre), data da instalação, garantia e manutenção (sem, a cada 6 meses ou uma vez por ano). A próxima manutenção já nasce marcada.
- **Registrar manutenção** em cada equipamento: o que foi feito, data e valor. A próxima manutenção é marcada sozinha, o aviso do Início some e, para o dono, o valor pode ir para o Faturamento como recebido.
- **Editar orçamento:** produto, valor, forma de pagamento, endereço e observações. Se já for venda, o lançamento do Faturamento acompanha o valor novo, sem ficar menor que o já recebido.
- **Excluir orçamento** (só o dono): com dinheiro recebido, pede o estorno antes ("Ver no Faturamento"); com agendamento marcado ou tarefa pendente, mostra "Antes de excluir…" com a lista; sem nada disso, confirma e cancela o lançamento a receber. Tem **Desfazer**; se for venda, volta com um lançamento a receber novo.
- **Mensagem de WhatsApp** para cliente sem compra: "Primeiro contato" ou "Orçamento" no lugar de "Pós-venda".

## Etapa 6 do design: Tarefas e Agenda (feito em 26/09)

- **Nova tarefa** (em Tarefas e nas fichas de cliente e de orçamento): o que fazer, dia, hora (opcional), cliente, orçamento, quem faz e envio para a Google Agenda. As tarefas se organizam sozinhas pela data: Atrasadas, Hoje, Esta semana e Mais para frente.
- **Editar e excluir tarefa:** o lápis em cada linha abre a tarefa; excluir pede confirmação e tem **Desfazer**. A lista mostra quem é o responsável quando não é você, e a concluída mostra quem concluiu.
- **Desativar usuário da equipe:** as tarefas pendentes dele passam de verdade para a pessoa escolhida.
- **Agenda, detalhe do agendamento:** Editar (dia, horário, técnico, endereço), **Marcar como feito** (só no dia ou depois; dá para desmarcar) e **Cancelar agendamento** com motivo. O cancelado sai da agenda e fica guardado; o botão **Cancelados** em "Mostrar" traz de volta, riscado. Agendamento que já passou e ficou sem registro mostra o aviso "Marque como feito ou cancele".
- **Instalação ligada a orçamento:** mudar o dia atualiza a data de instalação no orçamento; cancelar deixa "A definir".
- **Técnicos** (botão na Agenda, só o dono): adicionar, editar nome e cor (4 cores do design system), desativar (os agendamentos marcados continuam, com aviso) e reativar. Técnico desativado some da escolha do técnico.
- **Ficha excluída** no novo agendamento ou na nova tarefa: mesma mensagem da etapa 5, com Restaurar ficha.
- As travas de exclusão de cliente e de orçamento passam a contar todo agendamento marcado, como no banco. Os agendamentos antigos de exemplo foram marcados como feitos.

- **Cópia de segurança:** cópias automáticas do Neon (voltar o banco a qualquer momento dos últimos dias) + botão "Exportar dados" para a loja. Cópia semanal separada por loja fica para depois.
- **Assinatura paga fora do Asaas:** permitida; a equipe Nortiq registra cada pagamento no painel.

## Falta desenhar para a primeira versão

Ordem sugerida: primeiro o que impede a loja de usar o sistema no dia a dia.

### Acesso e conta
1. ~~Equipe~~, ~~Segurança da conta~~, ~~Erros do login~~, ~~Sessão expirada~~ e ~~Pagamento em atraso~~: feitos na etapa 1 (acima).
2. ~~Técnicos da agenda~~: feito na etapa 6 (acima).
3. ~~Login da administração Nortiq~~: feito na etapa 3 (acima).

### Dados do dia a dia
4. ~~Clientes~~: feito na etapa 5 (acima).
5. ~~Orçamentos~~: feito na etapa 5 (acima).
6. ~~Tarefas~~: feito na etapa 6 (acima).
7. ~~Agenda~~: feito na etapa 6 (acima).
8. **Estoque:** histórico de movimentações do produto; registrar entrada, saída, perda, devolução e ajuste; desativar produto em vez de excluir.

### Faturamento
9. ~~Lançamentos, recebimentos, estorno, cancelamento e reabrir venda paga~~: feitos na etapa 4 (acima). Fica para depois: parcelas (vários vencimentos num lançamento) e recibo em PDF.

### Estados gerais
10. **Carregando:** padrão para listas e painéis (esqueleto) e botões com "Salvando" ou "Enviando". O botão do design system já tem esse estado.
11. **Erros gerais:** sem conexão, erro inesperado ("Não foi possível salvar. Tente de novo.") e página não encontrada.
12. **Loja nova, sem dados:** estados vazios de Início, Orçamentos, Clientes, Estoque (sugerindo importar a planilha), Faturamento, Agenda e Metas (definir a primeira meta).

### Mensagens das travas de exclusão (decidido em 26/09)
O banco recusa estas ações; as telas precisam explicar o motivo e mostrar o caminho. Textos propostos:

| Situação | Mensagem | Botões |
|---|---|---|
| Excluir cliente com pendências | **Antes de excluir Marta Oliveira.** Ainda há 1 orçamento em negociação, 1 agendamento marcado e 2 tarefas pendentes com este cliente. Encerre ou cancele esses itens e tente de novo. | Ver pendências · Fechar |
| Excluir cliente sem pendências | **Excluir Marta Oliveira?** A ficha sai da lista de clientes. Orçamentos, lançamentos e histórico continuam guardados, e a ficha pode ser restaurada. | Excluir cliente · Cancelar |
| Usar cliente excluído (novo orçamento, tarefa ou agendamento) | Esta ficha foi excluída. Restaure a ficha para usá-la de novo. | Restaurar ficha · Cancelar |
| Excluir orçamento com dinheiro recebido | **Antes de excluir ORC-0415.** Este orçamento tem R$ 1.890,00 recebido. Se o dinheiro foi devolvido, registre o estorno no Faturamento e depois exclua. Se a venda aconteceu, mantenha o orçamento. | Ver no Faturamento · Fechar |
| Excluir orçamento com pendências | **Antes de excluir ORC-0403.** Ainda há 2 agendamentos marcados e 1 tarefa pendente com este orçamento. Encerre ou cancele esses itens e tente de novo. | Ver pendências · Fechar |
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
