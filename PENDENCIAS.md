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

- **Endereço próprio** (admin.nortiqtec.com.br). O link "Equipe Nortiq? Acessar a administração" saiu do login das lojas; no protótipo, o atalho fica no quadro "Protótipo · ver outras situações".
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
  - Fica para depois: cancelamento pela própria loja cobrada no cartão pelo Asaas (hoje é com a equipe) e o recibo da fatura paga.
- **Painel Nortiq** ligado ao banco (28/09): Visão geral e Contas assinantes.
  - Nova conta: loja, dono e cobrança direta (Pix, transferência, dinheiro). "Já recebi" registra a primeira mensalidade e manda o convite do dono na hora; "vou receber depois" deixa a conta aguardando, e o convite sai quando o pagamento for registrado. O dia do vencimento é o de hoje (até 28), ou outro escolhido.
  - Ficha da conta com as abas Resumo (andamento: cadastrada, pagamento, convite, senha criada), Mensalidades (registrar e estornar com motivo), Acesso e suporte (quem entra na loja e as ações de atendimento) e Atendimentos (histórico).
  - A Nortiq também encerra e reativa a assinatura (a loja é orientada a falar com a equipe quando tem mensalidade atrasada ou quando o acesso já acabou). Mensalidade atrasada acompanha a loja na assinatura nova.
  - Diferenças do protótipo: sem cupom de parceiro, sem "Alterar forma de cobrança" (a forma é escolhida na nova conta: Pix direto ou cartão pelo Asaas, desde 03/10). Notificações ficou pronto em 29/09, Receitas em 01/10 e Planos em 02/10: nenhuma tela do painel está mais "em construção".
- **Pronto para publicar** (28/09): e-mail pelo Resend (ou Brevo), banco preparado sozinho a cada deploy (papéis com senhas geradas pelo Render, migrations), rotina diária agendada e o passo a passo no README do repositório da API.
  - Falta fazer (pela equipe Nortiq): domínio na GoDaddy com DNS e e-mail contato@ no Cloudflare, projeto no Neon (Virgínia), conta no Resend com o domínio verificado e o Blueprint no Render. Depois: primeiro administrador pelo Shell do Render e a conferência no ar.
- **Metas** ligadas ao banco (28/09).
  - Meta do mês e do próximo (só o dono). Conta o dinheiro que entrou no caixa no mês (recebimentos do Faturamento, menos os estornos), como os números do Faturamento.
  - Mostra quanto já entrou, a porcentagem, quanto falta, os dias que sobram no mês (contando hoje, sem os domingos) e quanto precisa entrar por dia.
  - Meses anteriores (desde que a loja começou, até 12) com "bateu" ou "não bateu", e de onde veio a receita do mês por categoria.
  - Salvar 0 tira a meta. Meses que já passaram não mudam.
  - Os primeiros passos do Início ganharam "Defina a meta do mês"; o Início convida a definir a meta e o bloco da meta tem "Detalhes".
  - Diferença do protótipo: "dias úteis" virou "dias restantes" (segunda a sábado), porque as lojas abrem aos sábados.
- **Google Agenda** ligado (28/09).
  - Cada pessoa (dono ou funcionário) liga a própria conta Google, pela Agenda, pelas Tarefas ou pelo Perfil. O Google só pede a permissão da agenda.
  - Tarefa marcada "Enviar para o Google Agenda" vai para a agenda de quem faz a tarefa; agendamento, para a de quem ligou o envio. Com hora, lembrete 30 minutos antes; tarefa sem hora fica como compromisso do dia inteiro.
  - Mudou no CRM, muda no Google; concluída aparece com ✓; cancelou, desligou o envio ou excluiu, sai do Google. Se o Google estiver fora do ar, fica pendente e vai depois, sozinho.
  - Os compromissos do Google aparecem em cinza na Agenda do CRM, só para ver (com o nome, ou só "Ocupado"). O novo agendamento avisa quando bate com um compromisso do Google.
  - Desconectar: o Nortiq para de enviar e de mostrar; o que já foi enviado continua no Google. Se a pessoa tirar a permissão lá no Google, a conexão cai e a tela avisa para conectar de novo.
  - Diferença do protótipo: no protótipo era "a conta Google da loja"; aqui cada pessoa liga a sua (o lembrete chega no celular de quem vai fazer).
  - Técnico ligado a uma pessoa da equipe (Agenda › Técnicos › Editar › "Pessoa da equipe"): os agendamentos dele marcados para o Google vão para o Google Agenda dessa pessoa, com lembrete no celular dela. Sem pessoa ligada (ou sem Google conectado), vão para quem ligou o envio. Trocar a pessoa move os agendamentos de agenda sozinho.
  - Ligado no sistema de verdade em 03/10 (projeto no Google Cloud e app publicado). Falta a verificação do Google (passo 7 do README da API), que tira o aviso de app não verificado.
- **Uso sem internet** (28/09).
  - O sistema da loja instala como aplicativo no celular e no computador (Android: "Instalar app"; iPhone: "Adicionar à Tela de Início"; computador: ícone na barra de endereço) e abre sem internet.
  - O aparelho guarda uma cópia do estoque, dos clientes (com endereço e equipamentos), da agenda (do mês passado até 4 meses à frente) e das tarefas pendentes. A cópia se atualiza sozinha depois de cada mudança, ao abrir e a cada 15 minutos; dá para atualizar na hora pelo Perfil.
  - Sem internet: essas telas e o Início abrem com a cópia, e o topo avisa "Sem internet: mostrando os dados de hoje, 14:32". Financeiro, metas, vendas e edições precisam de internet (e avisam).
  - Agendamento e tarefa criados sem internet ficam "aguardando internet" e vão sozinhos quando a conexão volta, uma vez só (a chave do aparelho impede duplicar). Se a loja não aceitar (por exemplo, cliente excluído), aparece o motivo, com "Tentar de novo" e "Descartar".
  - Segurança: a cópia não leva o financeiro nem o preço de custo, vale 7 dias sem internet e é apagada ao sair ou quando a sessão termina (inclusive "desconectar aparelho"). Sair com itens não enviados pergunta antes.
- **Três planos, mensal ou anual** (28/09).
  - Básico: até 3 pessoas (o dono e mais 2), com Google Agenda e tudo do dia a dia. R$ 79,90 por mês ou R$ 799 por ano.
  - Profissional: até 8 pessoas, com Metas e Relatórios em PDF. R$ 129,90 por mês ou R$ 1.299 por ano.
  - Pro: pessoas sem limite, WhatsApp automático, IA, estoque pela nota fiscal e suporte prioritário. R$ 199,90 ou R$ 1.999. Aparece como "Em breve" e não é vendido até ficar pronto.
  - Anual: 12 meses pelo preço de 10. A anuidade paga cobre 12 meses (pago até, fim do acesso ao cancelar e a próxima cobrança seguem isso).
  - Meu plano: "Trocar de plano" mostra os três lado a lado, em mensal ou anual. A troca vale na hora e a próxima cobrança já vem com o valor novo. Com a anuidade paga correndo, a troca é com a equipe Nortiq (acerto da diferença).
  - Equipe: mostra "2 de 3 pessoas do plano Básico". Convites pendentes contam. Cheio, o botão de convidar fica bloqueado e aparece "Ver os planos".
  - Metas e Relatórios aparecem no menu com a etiqueta "Profissional"; no Básico, abrem uma explicação com "Ver os planos".
  - Painel Nortiq: a nova conta escolhe o plano e mensal ou anual; a lista e a ficha mostram o plano.
- **Relatórios em PDF** (28/09), no plano Profissional, só para o dono.
  - Período: Este mês, Mês passado, Últimos 3 meses ou Personalizado (até um ano).
  - Sete seções para marcar: resumo (recebido, pago, sobra, vendas e a meta do mês), vendas fechadas, orçamentos por etapa, perdas e objeções, faturamento por categoria, instalações e manutenções, clientes novos. A prévia ao lado mostra os mesmos números do PDF.
  - Cabeçalho com a logo (enviar, trocar ou remover; PNG, JPG ou SVG) e os dados da loja; "Editar dados da loja" leva a Configurações. Observação opcional no rodapé.
  - "Baixar PDF" gera o arquivo A4 no servidor; "Salvar configuração" guarda as seções e a observação.
  - Diferença do protótipo: os dados da empresa são editados em Configurações › Dados da loja (no relatório só a logo).
- **Painel Nortiq: Mapa de assinantes e Prospecção** (29/09), só para o administrador principal (quem instalou a administração; os convidados não veem).
  - Mapa: Brasil por estado e mundo por país, com a cor mais forte onde há mais lojas. Clicar num estado mostra as cidades e as lojas (com link para a ficha). Filtros por situação (ativas, em dia, em atraso, aguardando, todas) e por plano. As lojas passam a ter país (hoje todas do Brasil), pronto para quando a cobrança aceitar outros países.
  - Prospecção: busca empresas no Google ("loja de aquecedores" em "Taubaté SP"), com telefone, site, endereço, nota e link do Google Maps. "Salvar lead" guarda na lista; a lista tem situação (novo, contatado, interessado, negociando, virou cliente, descartado), anotação e excluir (quando a empresa pede para não ser contatada).
  - Mensagens prontas (até 5) com {empresa} e {cidade}. "Enviar mensagem" mostra o texto já com o nome e a cidade da empresa (dá para ajustar) e abre o WhatsApp Web na conversa; você só aperta enviar. O lead vira "Contatado" com a data do último contato.
  - Falta fazer (pela equipe Nortiq): ativar a Places API (New) no Google Cloud e colocar a chave no Render (passo 7 do README da API). O Google cobra por busca depois da cota gratuita; o painel limita a 200 buscas por dia e para em 900 no mês (abaixo da cota grátis), sem chamar o Google.
  - Depois: envio automático pela API oficial do WhatsApp (o ambiente já está preparado).
- **Site nortiqtec.com.br** (29/09), na pasta `site/` do repositório da API, publicado pelo Render como site estático.
  - Vitrine com as telas do sistema, destaques, funcionalidades, planos (mensal e anual, Pro "em breve"), como começar, dúvidas e WhatsApp com mensagem pronta.
  - **Entrar**: a pessoa digita o endereço da loja e vai direto para `sualoja.nortiqtec.com.br/entrar` (o navegador lembra o último endereço).
  - Páginas de **privacidade** e **termos de uso**, exigidas pelo Google para liberar o Google Agenda.
  - Falta preencher (antes de publicar): razão social, CNPJ e cidade do foro (marcados em amarelo nas duas páginas) e criar o e-mail `contato@nortiqtec.com.br`.
- **Sino de notificações** (29/09), no topo do sistema da loja.
  - O sistema avisa sozinho, sem repetir: agenda de amanhã ("Instalação amanhã às 08:00"), tarefa do dia (para o responsável), orçamento enviado há 3 dias sem resposta, manutenção vencendo em até 7 dias, garantia terminando em até 15 dias, produto que zerou ou ficou abaixo do mínimo depois de uma saída, e a mensalidade (disponível, vence hoje, em atraso, pagamento recebido).
  - Cada pessoa vê só a parte do sistema que abre: a mensalidade só o dono vê; a tarefa, só o responsável. A leitura é de cada pessoa. Abas Todas e Não lidas, "Marcar todas como lidas"; tocar abre o orçamento, o cliente ou a tela certa.
  - Painel Nortiq › Notificações: enviar um aviso para todas as lojas, só as em atraso ou as escolhidas, com a tela que abre ao tocar, prévia e e-mail opcional para o dono. A lista das enviadas mostra quantas lojas já abriram. Cobrança abre sempre Meu plano e só o dono vê.
- **Exclusão dos dados 90 dias depois do fim do acesso** (29/09).
  - Com a assinatura encerrada (cancelada e passado o período pago), só o dono entra, para baixar a cópia dos dados. A tela mostra até quando os dados ficam guardados; o sino e Meu plano também.
  - A rotina diária manda e-mail ao dono quando o acesso termina, 30 e 7 dias antes, e quando os dados são apagados (uma vez cada).
  - Passados 90 dias, apaga de vez clientes, orçamentos, estoque, agenda, tarefas, financeiro, metas, notificações, a equipe e o histórico desses dados. Ficam o cadastro da loja, a assinatura, as faturas, os pagamentos, os atendimentos e os registros de acesso.
  - Painel Nortiq: a conta mostra "dados guardados até" ou "dados apagados em". Reativar uma loja apagada: ela volta vazia, com as listas padrão; é preciso convidar o dono de novo.
  - Privacidade, termos e dúvidas do site atualizados com essa regra.
- **Setores da equipe** (01/10), em Configurações › Equipe.
  - Cada funcionário fica num setor, com uma cor. A loja começa com Vendas (azul), Técnicos de campo (verde), Estoque e compras (laranja) e Administrativo (roxo); o dono muda, cria outros (até 12) e exclui os vazios.
  - Para cada setor, o dono escolhe o nível em cada parte do sistema: orçamentos, clientes, estoque (consulta sem custo, ou cadastra e movimenta com custo), tarefas, agenda, faturamento, metas e relatórios. Ex.: Vendas confere o estoque para ver o que falta; Estoque e compras mexe no estoque, mas não cria orçamento.
  - Sempre só do dono: excluir orçamentos e clientes, importar planilha, estornar e cancelar no faturamento, definir metas, a equipe, Meu plano e os dados da loja.
  - A lista da equipe fica separada por setor, com a cor de cada um; convite e "Papel e setor" mostram o que a pessoa vai ver. A mudança vale na próxima tela que a pessoa abrir; o topo mostra o setor de quem está usando.
- **Receitas no painel Nortiq** (01/10), igual ao protótipo.
  - Números do mês: recebido (CRM e serviços), a receber (com as vencidas), receita mensal recorrente (assinaturas e contratos) e contratos ativos; e de onde vem o dinheiro no mês.
  - Nova receita: cliente (loja do CRM ou cliente de fora, cadastrado ali mesmo), serviço e como cobrar: uma vez, em parcelas (o total é dividido sem perder centavo, um mês depois do outro) ou todo mês por contrato (a cobrança de cada mês entra sozinha, pela rotina diária e ao abrir a tela, sem repetir). "Já recebi" registra a receita, ou a primeira parcela.
  - Cada receita abre com o contato do cliente, o histórico e as ações: registrar recebimento (sempre o valor todo; dia e forma), estornar e cancelar com motivo. O contrato mostra as cobranças dele e pode ser encerrado com motivo. Nada é apagado.
  - Serviços oferecidos: acrescentar e desligar (desligado sai de Nova receita; o que já foi lançado continua).
  - Ficha da conta assinante: aba Serviços com o que a Nortiq vendeu para aquela loja e "Nova receita".
  - No celular tudo vira lista: nada rola para o lado (conferido no teste automático).
  - Fica para depois: cobrar pelo Asaas (link de pagamento) em vez de só registrar, e editar valor ou vencimento de uma receita a receber.
- **Planos no painel Nortiq** (02/10), igual ao protótipo: os três planos com o preço mensal e o anual, o que cada um inclui, "À venda" ou "Em breve", as lojas pagantes (quantas no anual e quantas aguardando o primeiro pagamento) e a receita por mês de cada plano; embaixo, a receita recorrente somada. Os preços não mudam pela tela (mudar o preço de quem já assina é uma decisão à parte).
- **Protótipo atualizado** (01/10) com o que o sistema ganhou depois de 27/09: setores da equipe, os três planos (Trocar de plano e a etiqueta "Profissional" no Básico), Google Agenda e Usar sem internet no Perfil, e, no painel Nortiq, Planos, Mapa de assinantes e Prospecção.
- **Cartão de crédito pelo Asaas** (03/10): cobrança automática todo mês (ou todo ano). O Pix direto, registrado à mão pela equipe, continua igual.
  - Nova conta: campo "Cobrança" com "Direto com a Nortiq" ou "Cartão de crédito pelo Asaas (automática)" (só aparece com a chave do Asaas no Render). No cartão, o sistema cria o cliente e a assinatura no Asaas e o dono recebe por e-mail o link para cadastrar o cartão na página segura do Asaas. O Nortiq não recebe nem guarda os dados do cartão.
  - O Asaas avisa o Nortiq a cada mudança (webhook com token): paga, vencida, estornada ou cancelada. O primeiro pagamento aprovado libera a loja e manda o convite para criar a senha, sozinho. Aviso repetido não muda nada; aviso que falhar a rotina diária tenta de novo.
  - Ficha da conta: "Cartão de crédito pelo Asaas" na cobrança, "Copiar link" na mensalidade em aberto e "Pago em … no cartão · confirmado pelo Asaas". Encerrar tira a assinatura do Asaas; reativar cria outra lá e manda o link do cartão de novo.
  - Meu plano (loja): a próxima mensalidade aparece "Agendada", cobrada sozinha no cartão no vencimento, sem botão de pagar. Se o cartão for recusado, ela fica em atraso, com o botão Pagar que abre a página do Asaas. Trocar de plano, cancelar e reativar no cartão é com a equipe Nortiq (WhatsApp); site, termos e privacidade já falam do cartão e do Asaas.
  - Fica para depois: a loja assinar sozinha pelo site, com o cartão; cancelar e trocar de plano no cartão pelo próprio Meu plano; cobrança internacional.
- **Vídeo de apresentação** (03/10), aprovado: 16 s, versões 16:9 (site) e 9:16 (Instagram), com trilha instrumental original e efeitos sutis. Os vídeos prontos, as composições e o guia do estilo (padrão para os próximos) estão em `video/`.
- **Site:** privacidade, termos e rodapé com o nome e o endereço de Paulo Henrique Barbosa dos Santos (responsável até a abertura do CNPJ) e o foro de Carapicuíba (SP). Falta, depois: colocar o vídeo na página inicial e trocar pelo CNPJ quando a empresa for aberta.
- **No ar** (03/10): domínio `nortiqtec.com.br` (GoDaddy, DNS no Cloudflare), banco no Neon (Virgínia), e-mails pelo Resend (domínio verificado), `contato@` encaminhado para o Gmail pelo Cloudflare, Blueprint no Render (lojas, administração, rotina diária e site, plano Hobby), os endereços `nortiqtec.com.br`, `www`, `admin.` e `*.nortiqtec.com.br` com certificado, e o primeiro administrador criado. Testado de ponta a ponta com uma loja de teste: convite por e-mail, senha e entrada na loja.
  - **Google Agenda no ar** (03/10): domínio verificado no Search Console, projeto no Google Cloud da conta nortiqtec@gmail.com, tela de permissão ("Nortiq CRM", links do site, permissões `openid`, `userinfo.email` e `calendar.events`), cliente "Nortiq Lojas" com o retorno em `app.nortiqtec.com.br/google/retorno`, chaves no `nortiq-lojas` do Render e app publicado (em produção). Testado na loja de teste: conectou e o agendamento apareceu no Google Agenda. Até o Google verificar, quem conecta vê "o Google não verificou este app" (segue em Avançado), com limite de 100 pessoas.
  - Falta (externo): pedir a verificação do acesso à agenda no Google (vídeo no YouTube como não listado; a marca já foi verificada), a Places API para a Prospecção, a conta no Asaas (sandbox primeiro, com o webhook) e conferir no Billing do Render a cobrança do terceiro domínio (o Hobby inclui 2).
- **Testes de uso (04/10):** a loja de teste recebe planilhas de exemplo (40 produtos e 30 clientes fictícios, com WhatsApp (11) 90000-00xx) para usar no dia a dia e apontar o que melhorar.
  - **Importar clientes por planilha** (Excel ou CSV, só o dono), igual à de produtos: o sistema reconhece as colunas pelo título; quem já tem ficha (mesmo WhatsApp ou e-mail) fica como está; linha com erro é explicada e fica de fora.
  - **Hora numa lista** (de 15 em 15 minutos) no agendamento e na tarefa, no lugar do relógio do Android, que ficava cortado em tela pequena ou com letra grande. Mudar o começo do agendamento leva o fim junto.
  - **Personalização:** a logo da loja (Configurações › Dados da loja) aparece no menu, com a assinatura "Nortiq" pequena, e ao lado da saudação no Início; cada pessoa pode pôr a própria foto (Configurações › Perfil), que aparece no topo e na equipe.
  - **Varredura no celular** (360 e 320 px) de todas as telas e janelas: nada cortado nem rolando para o lado; corrigido o retângulo cinza que aparecia dentro do campo ao tocar.
  - **Google Agenda:** a Agenda busca de novo os compromissos do Google quando a pessoa volta para a tela. A marca do app já foi verificada pelo Google; falta pedir a verificação do acesso à agenda, com o vídeo.
- Depois do lançamento: assinatura pelo site com o cartão, cobrança internacional, cupons de parceiros, WhatsApp oficial na prospecção e o plano Pro.

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
