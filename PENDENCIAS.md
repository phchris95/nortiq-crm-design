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

## Etapa 7 do design: Estoque com baixa automática (feito em 26/09)

- **Ficha do produto** (clique no produto): quantidade, mínimo, preço de venda e de custo (o custo só o dono vê), e o **histórico de movimentações**: cadastro, entradas, vendas, vendas desfeitas, perdas, devoluções, ajustes e importações, com data, quem fez, a quantidade e o saldo depois de cada uma. A venda tem o link "Abrir orçamento".
- **Registrar movimentação** (só o dono): entrada (com custo da compra, opcional), saída sem venda, perda, devolução e ajuste pela contagem. Perda e ajuste pedem o motivo. Mostra antes "o estoque passa de 6 para 9 un". Saída e perda à mão não deixam o estoque negativo.
- **Editar dados** não muda mais a quantidade: ela só muda por movimentação. No produto novo, a quantidade inicial entra no histórico como cadastro. A importação de planilha também registra entradas e ajustes.
- **Desativar produto** (em vez de excluir): sai da escolha dos orçamentos, continua no histórico e na aba **Desativados**, e dá para reativar.
- **Baixa automática:** a ficha do orçamento ganhou **Produtos do orçamento**, com **Adicionar produto** do estoque (quantidade e preço) e o botão de tirar. Quando a venda é fechada, os produtos saem sozinhos do estoque; se a venda for reaberta, perdida ou excluída, eles voltam; na venda já fechada, o produto adicionado na hora (por exemplo, pelo técnico na obra) sai na mesma hora e o lançamento no Faturamento acompanha o novo total.
- **Vendeu sem ter no estoque:** a venda passa e o produto fica com quantidade negativa e o aviso "Repor 1 un", até a próxima entrada.
- O funcionário abre a ficha do produto só para consulta (sem custo e sem registrar movimentação).

## Etapa 8 do design: estados gerais (feito em 26/09)

No login do protótipo há um seletor novo, **Estado das telas**, para ver cada situação:

- **Loja nova, sem dados:** o Início vira **Primeiros passos** (conferir os dados da loja, cadastrar os produtos, convidar a equipe, primeiro cliente, primeiro orçamento e a meta do mês), com o progresso "2 de 6" e o atalho de cada passo. A funcionária vê só os passos que ela pode fazer. Cada tela vazia explica para que serve e oferece o primeiro passo: Orçamentos, Clientes, Estoque (importar a planilha ou cadastrar produto), Tarefas, Agenda, Faturamento, Relatórios e Metas (definir a primeira meta ali mesmo). Dá para ocultar os primeiros passos e ver o Início completo.
- **Carregando:** ao abrir uma tela aparece o esqueleto (blocos cinza no lugar dos números e da lista) e, ao salvar, o botão fica em **Salvando…** até o servidor responder.
- **Sem conexão:** faixa no topo avisando que nada novo é salvo até a internet voltar, com **Tentar de novo**. Ao salvar sem conexão, a janela continua aberta com o que foi digitado.
- **Erro ao salvar:** aviso dentro da janela ("Não foi possível salvar agora. O que você digitou continua aqui.") com **Tentar de novo**. No protótipo vale para novo orçamento, cliente, tarefa e movimentação do estoque; no sistema real, para todas as janelas.
- **Erro ao abrir uma tela:** aviso com **Tentar de novo**, **Voltar para o Início**, **Falar com a Nortiq** e o **código do erro**, que a equipe Nortiq usa para achar a falha no registro do servidor.
- **Página não encontrada:** para link errado ou item excluído, com **Voltar para o Início**. Um item de outra loja também cai aqui (o sistema nunca revela que ele existe).
- Nos cartões do Início, as listas vazias ganharam uma frase ("Nenhuma instalação marcada para esta semana") e o menu não mostra mais o número 0.

## Etapa 9 do design: Receitas da Nortiq além do CRM (feito em 26/09)

No painel da administração, item novo no menu: **Receitas**.

- **Números do mês:** recebido (CRM + serviços), a receber, receita mensal recorrente (assinaturas + contratos) e contratos ativos. A Visão geral passou a somar os contratos na receita recorrente.
- **De onde vem o dinheiro:** quanto cada origem rendeu no mês (assinaturas do CRM, criação de site, automação, agente de IA...).
- **Nova receita:** cliente (uma loja do CRM ou outro cliente, cadastrado ali mesmo), serviço, descrição e como cobrar: **uma vez**, **em parcelas** (divide o total e mostra as datas) ou **todo mês** (contrato: valor, dia do vencimento e primeiro mês). Dá para marcar "já recebi".
- **Lançamentos:** abas A receber (com as vencidas), Recebidas, Todas e Canceladas, e busca. Cada receita abre com o histórico e as ações: registrar recebimento (dia e forma), estornar (com motivo) e cancelar (com motivo). Nada é apagado.
- **Contratos mensais:** a cobrança de cada mês entra sozinha na lista; encerrar o contrato (com motivo) para os meses seguintes.
- **Serviços oferecidos:** a lista que aparece em Nova receita; dá para acrescentar e desligar serviços.
- **Ficha da conta assinante:** aba nova **Serviços**, com o que a Nortiq vendeu para aquela loja e o botão "Nova receita para esta loja".
- A loja nunca vê essas receitas; elas ficam só no painel da Nortiq.
- Fica para depois: gerar a cobrança pelo Asaas (link de pagamento) em vez de só registrar, e editar valor ou vencimento de uma receita a receber.

## Decisões de 26/09
- **Cópia de segurança:** cópias automáticas do Neon (voltar o banco a qualquer momento dos últimos dias) + botão "Exportar dados" para a loja. Cópia semanal separada por loja fica para depois.
- **Assinatura paga fora do Asaas:** permitida; a equipe Nortiq registra cada pagamento no painel.
- **Baixa automática do estoque na venda:** ligada. A venda pode deixar o estoque negativo (vendeu antes de chegar); movimentação à mão não.

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
8. ~~Estoque~~: feito na etapa 7 (acima), com a baixa automática na venda.

### Faturamento
9. ~~Lançamentos, recebimentos, estorno, cancelamento e reabrir venda paga~~: feitos na etapa 4 (acima). Fica para depois: parcelas (vários vencimentos num lançamento) e recibo em PDF.

### Estados gerais
10. ~~Carregando~~, 11. ~~Erros gerais~~ e 12. ~~Loja nova, sem dados~~: feitos na etapa 8 (acima).

Com isso, todo o desenho da primeira versão está pronto. O próximo passo é a API.

## Sistema de verdade (repositório privado da API)

- **Login** da loja e da administração: ligado ao banco (27/09).
- **Orçamentos e Clientes** ligados ao banco (27/09): funil, novo orçamento, ficha com etapas, objeção, produtos, perdido com motivo, excluir e restaurar; lista de clientes com abas e busca, ficha, novo, editar, excluir e restaurar; registro de contatos pelo WhatsApp.
- Pequenas diferenças em relação ao protótipo, decididas ao ligar as telas:
  - No novo orçamento, o nome do cliente e o produto **sugerem** fichas e produtos do estoque enquanto a pessoa digita (no protótipo o produto era uma lista fixa).
  - Na comunicação, além de "Abrir no WhatsApp", um botão **"Só anotar"** para registrar ligação, visita ou conversa na loja.
  - A ficha do orçamento ganhou o quadro **Histórico do orçamento** (quem mudou a etapa e quando).
  - No funil, a objeção não aparece mais nos cartões de venda fechada, instalação agendada e concluído.
  - No celular, a barra de etapas mostra "Etapa 4 de 6 · Venda fechada" em vez dos seis nomes apertados.
- **Estoque, Tarefas e Agenda** ligados ao banco (28/09), com os equipamentos e a manutenção na ficha do cliente e a importação de planilha (Excel .xlsx ou CSV).
  - A planilha é lida no próprio navegador (sem serviço de fora). O formato antigo do Excel (.xls) pede para salvar como .xlsx ou CSV.
  - Fichas de cliente e orçamento ganharam "Nova tarefa" e "Agendar"; o orçamento mostra a instalação marcada.
  - A Agenda tem as visões Semana e Mês; a visão Ano ficou para depois.
  - Fica para depois: ligação com o Google Agenda (trazer e enviar compromissos).
- **Faturamento e Início** ligados ao banco (28/09).
  - Faturamento: números do mês pelo caixa (o que entrou e saiu de fato, com os estornos descontados), lançamentos com abas e busca, recebimento parcial ou total, estorno e cancelamento com motivo.
  - A venda fechada entra sozinha no Faturamento, ainda sem data de vencimento; aparece como "sem data" até alguém editar.
  - Reabrir uma venda com dinheiro recebido: o dono escolhe manter o lançamento ou registrar o estorno (como no protótipo); o funcionário vê que é decisão do dono.
  - Início: números do dia, manutenções e garantias vencendo (com "Avisar" pelo WhatsApp), meta do mês (quando houver), instalações da semana, funil e retornos de hoje. Loja nova vê os primeiros passos (produtos, primeiro cliente, primeiro orçamento); os passos de dados da loja, equipe e meta entram junto com as Configurações e as Metas.
  - Fica para depois: o sino de notificações e o "Conversão do mês" comparado ao mês anterior.
- **Configurações e Meu plano** ligados ao banco (28/09).
  - Configurações: Perfil (nome, função, WhatsApp), Segurança (trocar a senha, aparelhos conectados, sair dos outros), Equipe (convite por e-mail, reenviar ou cancelar convite, papel, desativar passando as tarefas, reativar) e Dados da loja. Cada aba tem endereço próprio; o menu da conta ganhou "Minha conta" e "Segurança".
  - CNPJ, cidade e endereço de acesso só mudam pela equipe Nortiq (aparecem para leitura).
  - Cópia dos dados: o arquivo .zip (uma planilha por assunto) é montado na hora e baixado direto, em vez de "preparando… avisamos por e-mail". O pedido com link por 7 dias fica para quando houver lojas grandes.
  - Meu plano: faturas, "Pagar" com QR code do Pix, código copia e cola (já com o valor e a identificação da loja) e a chave Pix da Nortiq; "Enviar comprovante" abre o WhatsApp da Nortiq. A equipe registra o Pix no painel e a fatura fica paga.
  - Cancelar pela própria loja (com motivo): o acesso continua até o fim do período pago e as mensalidades futuras deixam de ser cobradas. Reativar antes do fim do acesso traz de volta as mesmas condições e as mensalidades tiradas. Com mensalidade atrasada, ou depois que o acesso acabou, a reativação é com a equipe Nortiq.
  - Com o acesso pausado continuam abertos Configurações e, para o dono, Meu plano.
  - Os primeiros passos do Início ganharam "Convide sua equipe".
  - Fica para depois: cancelamento de loja cobrada pelo Asaas (hoje é com a equipe) e o recibo da fatura paga.
- Próximas partes a ligar: o painel da administração (cadastrar loja com convite do dono, lista de lojas, registrar Pix, atendimento); depois do lançamento, metas e relatórios.

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
- **Tour guiado no primeiro acesso** (sugestão de 26/09): balões apontando cada parte da tela ("1 de 16"), com Próximo, Voltar e Pular; um tour para o dono e outro para funcionário e técnico; ajustado ao celular; aparece uma vez por usuário e pode ser revisto pelo menu da conta. Também serve para mostrar novidades.

## O que já estava certo

- Confirmações com motivo em "Cancelar assinatura" e "Marcar como perdido".
- Listas com mensagem quando a busca ou o filtro não encontra nada.
- Janelas (novo orçamento, produto, importação, agendamento, nova conta, cancelamento) funcionando no celular.
