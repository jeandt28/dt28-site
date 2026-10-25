# -*- coding: utf-8 -*-
# Páginas novas (out/2026): troca de óleo por diálise, PowerShift, TCM e guia de sintomas.
# Executado pelo gen_subpages.py (usa build_page e os templates de lá).

# ---------------------------------------------------------------
# TROCA DE ÓLEO POR DIÁLISE
# ---------------------------------------------------------------
build_page(
    key="diálise",
    title="Troca de Óleo do Câmbio por Diálise em Sarandi | DT28",
    description="Troca de fluido do câmbio automático por diálise, com teste do fluido Autool, em Sarandi, atendendo Maringá e região. Até 10x sem juros no cartão.",
    h1="Troca de óleo de câmbio automático por diálise em Sarandi",
    lead="Renovação do fluido da transmissão com equipamento de diálise, quando tecnicamente indicada, e teste do fluido com equipamento Autool.",
    eyebrow="Troca de fluido",
    wa_msg="Olá! Quero fazer a troca de óleo do câmbio automático por diálise. Carro/ano: ____ Tipo de câmbio (se souber): ____ Quilometragem: ____ Melhor dia para agendar: ____",
    final_q="Quer agendar a troca de óleo do câmbio?",
    cta_text="Agendar troca de óleo no WhatsApp",
    body_html="""
        <h2>Por que o fluido do câmbio automático precisa de atenção</h2>
        <p>Em uma transmissão automática, o fluido não serve só para lubrificar. Ele também transmite pressão para o acionamento das marchas, ajuda a resfriar o conjunto e protege as peças internas. Com o uso, o calor e o tempo, o fluido perde suas propriedades. Isso pode afetar a qualidade das trocas de marcha e acelerar o desgaste da transmissão.</p>

        <h2>Como funciona a troca por diálise</h2>
        <p>Na troca convencional, apenas parte do fluido sai pelo bujão do cárter. Uma quantidade importante continua retida no conversor de torque, no radiador e nas linhas do sistema. Na diálise, o equipamento é ligado ao circuito de arrefecimento do câmbio e substitui o fluido usado pelo fluido novo de forma progressiva, com o motor em funcionamento. O resultado é uma renovação mais completa do fluido.</p>

        <div class="content-image">
          <img src="/img/dialise-oleo.webp" alt="Equipamento de troca de óleo de câmbio por diálise na oficina DT28 Câmbios Automáticos" loading="lazy" decoding="async" width="287" height="293">
          <span class="content-image-cap">Equipamento de diálise usado pela DT28</span>
        </div>

        <h2>Teste do fluido com equipamento Autool</h2>
        <p>Antes de indicar a troca, a DT28 pode avaliar a condição do fluido com o testador Autool. O teste ajuda a identificar o nível de degradação e a indicar o momento adequado da troca, em vez de seguir apenas a quilometragem.</p>

        <h2>Quando a troca por diálise é indicada</h2>
        <p>A indicação depende do tipo de transmissão, da especificação do fabricante, da quilometragem, das condições de uso e do estado do fluido. Caminhonetes que puxam carga, rebocam ou rodam muito em estrada costumam exigir mais do fluido. Em cada caso, a DT28 usa o fluido correto para a aplicação do câmbio.</p>

        <h2>O que a troca de fluido não resolve</h2>
        <p>Quando o câmbio já apresenta defeito, como trancos fortes, patinação ou modo de emergência, a troca de óleo sozinha pode não resolver. Nesses casos, o primeiro passo é o <a href="/#servicos">diagnóstico especializado</a>, para encontrar a causa antes de qualquer serviço. Veja também os <a href="/sinais-de-problema-no-cambio-automatico">sinais de problema no câmbio automático</a>.</p>

        <h2>Pagamento</h2>
        <p>As trocas de fluido podem ser parceladas em até 10x sem juros no cartão de crédito. Também aceitamos dinheiro, Pix e cartão de débito.</p>
    """,
    faq_items=[
        ("A troca por diálise serve para todo câmbio automático?", "A diálise é usada conforme a aplicação e a especificação de cada transmissão. Envie o modelo e o ano do veículo pelo WhatsApp para confirmarmos o procedimento indicado."),
        ("Qual fluido é usado na troca?", "Usamos o fluido indicado para a especificação da transmissão do seu veículo."),
        ("Trocar o óleo resolve tranco no câmbio?", "Nem sempre. Se o câmbio já apresenta sintomas, é preciso diagnosticar a causa. A troca de fluido é manutenção e não substitui o reparo de um componente com defeito."),
        ("Posso parcelar a troca de óleo do câmbio?", "Sim. As trocas de fluido podem ser parceladas em até 10x sem juros no cartão de crédito."),
    ],
    hero_img="/img/teste-fluido-atf.webp",
    hero_img_alt="Teste de vida útil do fluido ATF com equipamento Autool na DT28 Câmbios Automáticos",
    hero_img_w="1536", hero_img_h="1024",
)

# ---------------------------------------------------------------
# POWERSHIFT
# ---------------------------------------------------------------
build_page(
    key="powershift",
    title="Câmbio PowerShift em Sarandi e Maringá | DT28",
    description="Diagnóstico, manutenção e programação de TCM do câmbio PowerShift de dupla embreagem em Sarandi, atendendo Maringá e região. Fale com a DT28.",
    h1="Câmbio PowerShift em Sarandi e Maringá",
    lead="Diagnóstico, manutenção e programação de módulo do câmbio PowerShift de dupla embreagem.",
    eyebrow="Dupla embreagem",
    wa_msg="Olá! Meu carro tem câmbio PowerShift e está com problema. Carro/ano: ____ Sintoma: ____ Melhor dia para agendar: ____",
    body_html="""
        <h2>O que é o câmbio PowerShift</h2>
        <p>PowerShift é o nome usado pela Ford para a sua transmissão de dupla embreagem a seco, aplicada em modelos como Fiesta, Focus e EcoSport. Assim como o DSG, ela usa duas embreagens que trabalham alternadas, com o acionamento controlado por uma unidade eletrônica, o TCM.</p>

        <h2>Sintomas comuns no PowerShift</h2>
        <ul>
          <li>Trepidação ao sair com o carro, principalmente em subidas ou em baixa velocidade</li>
          <li>Trancos nas trocas de marcha</li>
          <li>Demora para engatar ou hesitação ao acelerar</li>
          <li>Ruídos durante as trocas</li>
          <li>Luz de câmbio acesa ou mensagem de falha no painel</li>
          <li>Ativação do modo de emergência</li>
        </ul>

        <h2>Possíveis causas</h2>
        <p>Os sintomas podem estar ligados às embreagens, aos atuadores, à contaminação das embreagens por vazamento de óleo, ao TCM ou à necessidade de atualização e adaptação do módulo. Cada caso tem uma origem própria. Por isso, a DT28 faz o diagnóstico eletrônico antes de indicar qualquer peça.</p>

        <h2>Serviços da DT28 no câmbio PowerShift</h2>
        <ul>
          <li>Diagnóstico eletrônico da transmissão</li>
          <li>Manutenção preventiva e corretiva</li>
          <li>Reparo e substituição de componentes, conforme diagnóstico</li>
          <li>Programação de TCM PowerShift com aparelho avançado</li>
        </ul>
        <p>Saiba mais sobre a <a href="/programacao-tcm">programação de TCM</a> e sobre o <a href="/cambio-dsg">câmbio DSG</a>, outro sistema de dupla embreagem atendido pela DT28.</p>

        <div class="content-image">
          <img src="/img/diagnostico-eletronico.webp" alt="Oficina da DT28 Câmbios Automáticos em Sarandi com veículos nos elevadores" loading="lazy" decoding="async" width="680" height="424">
          <span class="content-image-cap">Estrutura da DT28 em Sarandi para diagnóstico e reparo</span>
        </div>
    """,
    faq_items=[
        ("Vocês atendem câmbio PowerShift?", "Sim. A DT28 faz diagnóstico, manutenção e programação de TCM do câmbio PowerShift."),
        ("Trepidação no PowerShift sempre é embreagem?", "Não necessariamente. A trepidação pode estar ligada às embreagens, aos atuadores, a contaminação por óleo ou ao módulo. O diagnóstico é que confirma a causa."),
        ("É preciso programar o TCM depois do reparo?", "Depende do serviço realizado e do veículo. Em alguns casos é necessário fazer adaptações ou programação do módulo, o que é avaliado durante o atendimento."),
    ],
    hero_img="/img/tcm-programacao.webp",
    hero_img_alt="Programação de módulo de transmissão com notebook na bancada da DT28",
    hero_img_w="926", hero_img_h="675",
)

# ---------------------------------------------------------------
# TCM
# ---------------------------------------------------------------
build_page(
    key="tcm",
    title="Diagnóstico e Programação de TCM do Câmbio em Sarandi | DT28",
    description="Programação de TCM com aparelho avançado, clonagem de módulo e instalação de código VIN para câmbio automático e de dupla embreagem. DT28 em Sarandi.",
    h1="Diagnóstico e programação de TCM em Sarandi",
    lead="Programação do módulo de controle da transmissão com aparelho avançado, clonagem de módulo e instalação de código VIN.",
    eyebrow="Módulo de transmissão",
    wa_msg="Olá! Preciso de diagnóstico ou programação de TCM. Carro/ano: ____ Câmbio: ____ O que aconteceu: ____",
    final_q="Precisa de diagnóstico ou programação de TCM?",
    cta_text="Falar sobre programação de TCM",
    body_html="""
        <h2>O que é o TCM</h2>
        <p>O TCM, sigla em inglês para módulo de controle da transmissão, é a central eletrônica que comanda o câmbio. Ele lê sensores, como velocidade e posição do acelerador, e decide quando e como trocar as marchas. Em câmbios automatizados e de dupla embreagem, também controla o acionamento das embreagens.</p>

        <h2>Quando a programação do TCM pode ser necessária</h2>
        <ul>
          <li>Substituição do módulo de transmissão</li>
          <li>Atualização de software indicada para o sistema</li>
          <li>Adaptações e aprendizados após reparo ou troca de componentes</li>
          <li>Clonagem de dados ao trocar o módulo</li>
          <li>Instalação do código VIN no módulo</li>
        </ul>
        <p>A necessidade de programação depende do veículo e do serviço realizado. A DT28 confirma isso no diagnóstico.</p>

        <h2>Aplicações atendidas</h2>
        <p>Trabalhamos com programação de TCM com aparelho avançado em aplicações como Hyundai, 6T30, 6T40, DQ200, DQ250, PowerShift e outras. Envie o modelo, o ano e o tipo de câmbio pelo WhatsApp para confirmarmos o atendimento do seu veículo.</p>

        <h2>Diagnóstico antes da programação</h2>
        <p>Nem toda falha de câmbio se resolve com programação. Antes, a DT28 faz a leitura eletrônica e os testes necessários para entender a causa do problema, que pode ser elétrica, hidráulica ou mecânica. Veja também o <a href="/cambio-dsg">câmbio DSG</a>, o <a href="/cambio-powershift">câmbio PowerShift</a> e o <a href="/cambio-cvt">câmbio CVT</a>.</p>
    """,
    faq_items=[
        ("Vocês fazem clonagem de módulo do câmbio?", "Sim. A DT28 tem equipamento para clonagem de módulo e instalação de código VIN, conforme a aplicação do veículo."),
        ("A programação de TCM resolve tranco no câmbio?", "Em alguns casos ajuda, principalmente quando a falha está relacionada a software ou adaptações. Mas o tranco também pode ter causa mecânica ou hidráulica, por isso fazemos o diagnóstico antes."),
        ("Quais câmbios vocês programam?", "Trabalhamos com Hyundai, 6T30, 6T40, DQ200, DQ250, PowerShift e outras aplicações. Consulte o seu modelo pelo WhatsApp."),
    ],
    hero_img="/img/tcm-programacao.webp",
    hero_img_alt="Programação de TCM em módulo de câmbio DQ200 na DT28 Câmbios Automáticos",
    hero_img_w="926", hero_img_h="675",
)

# ---------------------------------------------------------------
# GUIA: SINAIS DE PROBLEMA NO CÂMBIO AUTOMÁTICO
# ---------------------------------------------------------------
build_page(
    key="sinais",
    kind="article",
    title="Sinais de Problema no Câmbio Automático | DT28",
    description="Trancos, patinação, demora para engatar e luz no painel: veja os sinais de que o câmbio automático precisa de avaliação e o que fazer em cada caso.",
    h1="Sinais de que o câmbio automático precisa de avaliação",
    lead="Um guia da DT28 para reconhecer os sintomas mais comuns e saber quando procurar um especialista.",
    eyebrow="Guia do câmbio automático",
    wa_msg="Olá! Li o guia no site da DT28 e meu câmbio está com um sintoma. Carro/ano: ____ Sintoma: ____ Quando acontece: ____",
    final_q="Percebeu algum desses sinais?",
    cta_text="Descrever o sintoma no WhatsApp",
    body_html="""
        <p>O câmbio automático costuma dar sinais antes de um problema maior. Reconhecer esses sinais cedo pode evitar danos adicionais. Este guia ajuda a entender cada sintoma, mas não substitui o diagnóstico: o mesmo sintoma pode ter causas diferentes.</p>

        <h2>Trancos nas trocas de marcha</h2>
        <p>Trocas bruscas, com batida ou solavanco, podem estar ligadas ao fluido, ao corpo de válvulas, a solenoides, a embreagens internas ou ao módulo eletrônico. Repare se o tranco acontece com o motor frio ou quente e em quais marchas.</p>

        <h2>Patinação</h2>
        <p>O motor acelera, o giro sobe, mas o carro não ganha velocidade na mesma proporção. Esse sintoma merece atenção rápida, porque rodar com o câmbio patinando pode aumentar o desgaste interno. No câmbio CVT, a patinação pode ter relação com a correia, as polias, o corpo de válvulas ou o TCM. Saiba mais na página do <a href="/cambio-cvt">câmbio CVT</a>.</p>

        <h2>Demora para engatar</h2>
        <p>Demora ao colocar em D ou R, ou hesitação para sair com o carro, pode indicar nível ou condição inadequada do fluido, perda de pressão interna ou falha eletrônica.</p>

        <h2>Trepidação ao arrancar</h2>
        <p>Vibração ao sair com o carro é comum em problemas de câmbios de dupla embreagem, como DSG e PowerShift, mas também pode aparecer em outros sistemas. Veja as páginas do <a href="/cambio-dsg">câmbio DSG</a> e do <a href="/cambio-powershift">câmbio PowerShift</a>.</p>

        <h2>Luz no painel ou modo de emergência</h2>
        <p>Quando o módulo identifica uma falha, pode acender a luz de câmbio ou de injeção e limitar as marchas, no chamado modo de emergência. Nesse caso, o ideal é evitar rodar até avaliar o veículo, para não agravar o problema.</p>

        <h2>Vazamento ou cheiro de queimado</h2>
        <p>Manchas avermelhadas ou escuras embaixo do carro e cheiro de óleo queimado podem indicar vazamento ou superaquecimento do fluido. Falta de fluido compromete a lubrificação e a pressão do câmbio.</p>

        <h2>O que fazer ao perceber um sintoma</h2>
        <ul>
          <li>Anote quando acontece: motor frio ou quente, em subida, em qual marcha</li>
          <li>Verifique se há luz acesa no painel</li>
          <li>Evite insistir em rodar com o câmbio patinando ou em modo de emergência</li>
          <li>Procure um especialista em câmbio automático para o diagnóstico</li>
        </ul>

        <h2>Manutenção preventiva</h2>
        <p>Avaliar a condição do fluido e fazer a troca no momento certo ajuda a preservar a transmissão. Na DT28, o fluido pode ser testado com o equipamento Autool, e a troca é feita por diálise quando indicada. Saiba mais sobre a <a href="/troca-de-oleo-cambio-automatico">troca de óleo do câmbio automático por diálise</a>.</p>
    """,
    faq_items=[
        ("Posso continuar rodando com o câmbio dando tranco?", "Não é recomendado continuar rodando sem saber a causa. Dependendo do problema, o uso pode aumentar o dano. O ideal é agendar uma avaliação."),
        ("Um sintoma já indica qual peça está com defeito?", "Não. O mesmo sintoma pode ter causas diferentes. Só o diagnóstico técnico confirma a origem do problema."),
        ("Como agendar uma avaliação na DT28?", "Pelo WhatsApp (44) 99803-4786, com antecedência mínima de 3 dias, sujeito à aprovação do especialista."),
    ],
    hero_img="/img/diagnostico-eletronico.webp",
    hero_img_alt="Oficina da DT28 Câmbios Automáticos em Sarandi com caminhonete e carros nos elevadores",
    hero_img_w="680", hero_img_h="424",
)
