#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Gera as páginas de SEO (Dualogic, I-MOTION, Automatizado, DSG, CVT)
a partir de um layout compartilhado (mesmo header/footer/sprite do index.html)."""
import re, json

BUILD = "/home/claude/dt28/build"

with open(f"{BUILD}/index.html", encoding="utf-8") as f:
    idx = f.read()

# Extrai o sprite SVG (mesmo bloco usado no index.html)
sprite = re.search(r'<svg style="display:none" aria-hidden="true"><defs>.*?</defs></svg>', idx, re.S).group(0)

WA = "5544998034786"

def wa(msg):
    from urllib.parse import quote
    return f"https://wa.me/{WA}?text={quote(msg)}"

HEADER_TMPL = """<header class="site-header">
  <div class="container header-inner">
    <a class="brand" href="/#inicio" aria-label="DT28 Automáticos — início">
      <img src="/img/logo.webp" alt="DT28 Automáticos" width="120" height="40" style="height:32px;width:auto">
    </a>
    <nav class="main-nav" aria-label="Principal">
      <a href="/#servicos">Serviços</a>
      <a href="/#transmissoes">Transmissões</a>
      <a href="/#sintomas">Sintomas</a>
      <a href="/#avaliacoes">Avaliações</a>
      <a href="/#regiao">Contato</a>
    </nav>
    <div class="header-actions">
      <a class="btn btn-outline" href="/#regiao">Como chegar</a>
      <a class="btn btn-primary" href="{wa_geral}">
        <svg class="icon icon-sm" aria-hidden="true"><use href="#i-whatsapp"/></svg> WhatsApp
      </a>
      <button class="menu-btn" data-menu-open aria-label="Abrir menu">
        <svg class="icon" aria-hidden="true"><use href="#i-menu"/></svg>
      </button>
    </div>
  </div>
</header>

<div class="mobile-nav" data-mobile-nav>
  <div class="mobile-nav-top">
    <span class="brand"><img src="/img/logo.webp" alt="DT28 Automáticos" style="height:28px;width:auto"></span>
    <button class="menu-btn" data-menu-close aria-label="Fechar menu">
      <svg class="icon" aria-hidden="true"><use href="#i-close"/></svg>
    </button>
  </div>
  <nav aria-label="Menu mobile">
    <a href="/#servicos">Serviços</a>
    <a href="/#transmissoes">Transmissões</a>
    <a href="/#sintomas">Sintomas</a>
    <a href="/#avaliacoes">Avaliações</a>
    <a href="/#regiao">Contato</a>
    <a href="/#faq">Dúvidas frequentes</a>
  </nav>
  <a class="btn btn-primary btn-lg btn-block" href="{wa_geral}">
    <svg class="icon" aria-hidden="true"><use href="#i-whatsapp"/></svg> Falar no WhatsApp
  </a>
</div>
"""

FOOTER_TMPL = """<footer class="site-footer">
  <div class="container">
    <div class="footer-top">
      <div>
        <div class="footer-brand"><img src="/img/logo.webp" alt="DT28 Automáticos" style="height:26px;width:auto"></div>
        <p>Especialistas em transmissões automáticas em Maringá e Sarandi · Desde 2015. Diagnóstico eletrônico, reparo técnico e garantia por escrito.</p>
        <div class="social-row">
          <a class="social-btn" href="https://www.instagram.com/dt28_cambioautomaticos/" aria-label="Instagram da DT28"><svg class="icon-sm icon" aria-hidden="true"><use href="#i-instagram"/></svg></a>
          <a class="social-btn" href="https://www.facebook.com/104496185844160" aria-label="Facebook da DT28"><svg class="icon-sm icon" aria-hidden="true"><use href="#i-facebook"/></svg></a>
          <a class="social-btn" href="{wa_geral}" aria-label="WhatsApp da DT28"><svg class="icon-sm icon" aria-hidden="true"><use href="#i-whatsapp"/></svg></a>
        </div>
      </div>
      <div class="footer-col">
        <h4>Transmissões</h4>
        <a href="/cambio-dualogic">Câmbio Dualogic</a>
        <a href="/cambio-i-motion">Câmbio I-MOTION</a>
        <a href="/cambio-automatizado">Câmbio Automatizado</a>
        <a href="/cambio-dsg">Câmbio DSG</a>
        <a href="/cambio-cvt">Câmbio CVT</a>
      </div>
      <div class="footer-col">
        <h4>DT28 Automáticos</h4>
        <a href="/#servicos">Serviços</a>
        <a href="/#avaliacoes">Avaliações</a>
        <a href="/#faq">Dúvidas frequentes</a>
        <a href="/#regiao">Endereço e horário</a>
        <a href="tel:+5544998034786">(44) 99803-4786</a>
      </div>
    </div>
    <div class="footer-bottom">
      <span>© <span data-year>2026</span> DT28 Automáticos. Todos os direitos reservados.</span>
      <span>CNPJ 47.576.083/0001-25</span>
    </div>
  </div>
</footer>

<a class="wa-float" href="{wa_geral}" aria-label="Falar com especialista no WhatsApp">
  <svg class="icon" aria-hidden="true"><use href="#i-whatsapp"/></svg>
  <span class="wa-text">Falar com especialista</span>
</a>

<script src="/script.js" defer></script>
</body>
</html>
"""

PAGE_TMPL = """<!DOCTYPE html>
<html lang="pt-BR">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{title}</title>
<meta name="description" content="{description}">
<meta name="theme-color" content="#0a0a0a">
<link rel="canonical" href="{canonical}">
<meta property="og:url" content="{canonical}">
<meta property="og:type" content="website">
<meta property="og:locale" content="pt_BR">
<meta property="og:site_name" content="DT28 Automáticos">
<meta property="og:title" content="{title}">
<meta property="og:description" content="{description}">
<meta property="og:image" content="https://www.dt28cambioautomaticos.com.br/og-image.jpg">
<meta name="twitter:card" content="summary_large_image">
<link rel="icon" href="/favicon.png" type="image/png">
<link rel="apple-touch-icon" href="/apple-touch-icon.png">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800;900&display=swap" rel="stylesheet">
<link rel="stylesheet" href="/styles.css">
<script type="application/ld+json">{schema}</script>
</head>
<body>
<a class="visually-hidden" href="#conteudo">Pular para o conteúdo</a>
{sprite}
{header}
<main id="conteudo">
  <div class="container">
    <nav class="breadcrumb" aria-label="Breadcrumb">
      <a href="/">Início</a><span class="sep">/</span><span class="current">{crumb}</span>
    </nav>
  </div>

  <section class="subpage-hero">
    <div class="container">
      <span class="eyebrow">{eyebrow}</span>
      <h1>{h1}</h1>
      <p class="hero-lead">{lead}</p>
      <div class="cta-row" style="margin-top:24px">
        <a class="btn btn-primary btn-lg" href="{wa_specific}">📲 Falar com um especialista sobre {short_name}</a>
        <a class="btn btn-outline btn-lg" href="/#servicos">Ver todos os serviços</a>
      </div>
      <div class="subpage-hero-media">
        <img src="{hero_img}" alt="{hero_img_alt}" loading="eager" fetchpriority="high" width="{hero_img_w}" height="{hero_img_h}">
      </div>
    </div>
  </section>

  <section class="section">
    <div class="container subpage-grid">
      <div class="content-block">
        {body}

        <h2>Perguntas frequentes sobre {short_name}</h2>
        <div class="faq-list">
          {faq_html}
        </div>

        <h2>Outras transmissões que trabalhamos</h2>
        <div class="related-row">
          {related_links}
        </div>
      </div>

      <aside class="side-cta">
        <h3>Diagnóstico especializado</h3>
        <p>Envie o modelo, ano e sintoma do seu {short_name} e receba orientação sobre o próximo passo para avaliação do veículo.</p>
        <a class="btn btn-primary btn-block" href="{wa_specific}">📲 Falar no WhatsApp</a>
        <p style="margin-top:16px;font-size:13px">Rua Tiradentes, 782 – Sarandi/PR<br>Seg. a sex.: 08h–12h · 13h30–18h</p>
      </aside>
    </div>
  </section>

  <section class="section section--alt">
    <div class="container">
      <div class="final-cta">
        <span class="eyebrow">Fale com a DT28</span>
        <h2>Está com problema no {short_name}?</h2>
        <p>Envie o modelo, ano do veículo e os sintomas apresentados. Nossa equipe poderá orientar você sobre o próximo passo para avaliação do veículo.</p>
        <div class="cta-row">
          <a class="btn btn-primary btn-lg" href="{wa_specific}">📲 Falar com a DT28 no WhatsApp</a>
        </div>
      </div>
    </div>
  </section>
</main>
{footer}
"""

ALL_PAGES = {
    "dualogic": {"name": "Dualogic", "slug": "cambio-dualogic"},
    "imotion": {"name": "I-MOTION", "slug": "cambio-i-motion"},
    "automatizado": {"name": "Automatizado", "slug": "cambio-automatizado"},
    "dsg": {"name": "DSG", "slug": "cambio-dsg"},
    "cvt": {"name": "CVT", "slug": "cambio-cvt"},
}

def related_row(exclude_key):
    links = []
    for k, v in ALL_PAGES.items():
        if k == exclude_key:
            continue
        links.append(f'<a href="/{v["slug"]}">Câmbio {v["name"]}</a>')
    return "\n          ".join(links)

def faq_block(items):
    out = []
    for i, (q, a) in enumerate(items):
        open_attr = " open" if i == 0 else ""
        out.append(f'<details class="faq-item"{open_attr}><summary class="faq-q">{q}<span class="plus"></span></summary><div class="faq-a">{a}</div></details>')
    return "\n          ".join(out)

def faq_schema(items):
    return {
        "@context": "https://schema.org", "@type": "FAQPage",
        "mainEntity": [
            {"@type": "Question", "name": q, "acceptedAnswer": {"@type": "Answer", "text": a}}
            for q, a in items
        ]
    }

def breadcrumb_schema(name, url):
    return {
        "@context": "https://schema.org", "@type": "BreadcrumbList",
        "itemListElement": [
            {"@type": "ListItem", "position": 1, "name": "Início", "item": "https://www.dt28cambioautomaticos.com.br/"},
            {"@type": "ListItem", "position": 2, "name": name, "item": url}
        ]
    }

def build_page(key, title, description, h1, lead, eyebrow, body_html, faq_items, wa_msg,
                hero_img, hero_img_alt, hero_img_w, hero_img_h):
    info = ALL_PAGES[key]
    canonical = f"https://www.dt28cambioautomaticos.com.br/{info['slug']}"
    wa_link = wa(wa_msg)
    wa_geral = wa("Olá! Vim pelo site da DT28 e gostaria de falar sobre o câmbio do meu carro.")

    schema_list = [
        breadcrumb_schema(f"Câmbio {info['name']}", canonical),
        faq_schema(faq_items),
        {
            "@context": "https://schema.org", "@type": "Service",
            "serviceType": f"Diagnóstico, manutenção e reparo de câmbio {info['name']}",
            "provider": {"@type": "AutoRepair", "name": "DT28 Automáticos", "telephone": "+55-44-99803-4786",
                         "address": {"@type": "PostalAddress", "streetAddress": "Rua Tiradentes, 782 - Jardim Panorama",
                                     "addressLocality": "Sarandi", "addressRegion": "PR", "postalCode": "87113-060", "addressCountry": "BR"}},
            "areaServed": [{"@type": "City", "name": "Sarandi"}, {"@type": "City", "name": "Maringá"}],
            "url": canonical
        }
    ]
    # combine as @graph
    schema = json.dumps({"@context": "https://schema.org", "@graph": schema_list}, ensure_ascii=False)

    html = PAGE_TMPL.format(
        title=title, description=description, canonical=canonical,
        schema=schema, sprite=sprite,
        header=HEADER_TMPL.format(wa_geral=wa_geral),
        crumb=f"Câmbio {info['name']}",
        eyebrow=eyebrow, h1=h1, lead=lead,
        wa_specific=wa_link, short_name=info["name"],
        hero_img=hero_img, hero_img_alt=hero_img_alt, hero_img_w=hero_img_w, hero_img_h=hero_img_h,
        body=body_html,
        faq_html=faq_block(faq_items),
        related_links=related_row(key),
        footer=FOOTER_TMPL.format(wa_geral=wa_geral),
    )
    with open(f"{BUILD}/{info['slug']}.html", "w", encoding="utf-8") as f:
        f.write(html)
    print("wrote", info["slug"] + ".html", len(html), "bytes")


# ---------------------------------------------------------------
# DUALOGIC
# ---------------------------------------------------------------
build_page(
    key="dualogic",
    title="Câmbio Dualogic: Diagnóstico e Reparo em Sarandi e Maringá | DT28 Automáticos",
    description="Especialista em câmbio Dualogic em Sarandi e Maringá. Diagnóstico eletrônico, manutenção e reparo com garantia por escrito. Fale com a DT28 no WhatsApp.",
    h1="Câmbio Dualogic em Sarandi e Maringá",
    lead="A DT28 Automáticos é referência regional em diagnóstico, manutenção e reparo de transmissões Dualogic.",
    eyebrow="Especialista em Dualogic",
    wa_msg="Olá! Meu carro tem câmbio Dualogic e está com problema. Carro/ano: ____ Sintoma: ____",
    body_html="""
        <h2>O que é o câmbio Dualogic</h2>
        <p>O Dualogic é um sistema de transmissão automatizada: parte de uma caixa de câmbio manual, mas as trocas de marcha e o acionamento da embreagem são controlados eletronicamente, sem pedal de embreagem para o motorista. Por depender de atuadores eletro-hidráulicos e de uma central eletrônica própria, o funcionamento suave do Dualogic está diretamente ligado à calibração e à leitura eletrônica corretas do sistema.</p>

        <h2>Principais sintomas de problema no câmbio Dualogic</h2>
        <ul>
          <li>Trancos ao trocar de marcha</li>
          <li>Demora para engatar ou confirmar a marcha</li>
          <li>Marcha neutra inesperada durante a condução</li>
          <li>Dificuldade para sair do ponto morto</li>
          <li>Luz de câmbio ou de injeção acesa no painel</li>
          <li>Ativação do modo de segurança/emergência</li>
        </ul>

        <h2>Possíveis causas</h2>
        <p>Os sintomas do Dualogic podem estar relacionados a diferentes fatores — atuador de embreagem, unidade eletrônica (TCM), calibração das trocas, desgaste da embreagem ou componentes mecânicos internos. Cada caso tem uma origem própria, e a causa exata só é confirmada com diagnóstico eletrônico.</p>

        <h2>A importância do diagnóstico</h2>
        <p>Como o Dualogic depende de leitura eletrônica precisa, o diagnóstico antes de qualquer reparo evita a troca desnecessária de peças e direciona o serviço diretamente para a causa real do problema — economizando tempo e evitando gastos que não resolveriam o sintoma.</p>

        <h2>Serviços realizados pela DT28 em câmbio Dualogic</h2>
        <ul>
          <li>Diagnóstico eletrônico do sistema Dualogic</li>
          <li>Manutenção preventiva e corretiva</li>
          <li>Reparo de componentes do câmbio</li>
          <li>Leitura e programação de TCM com aparelho avançado, quando aplicável ao veículo</li>
        </ul>
        <p>Não trabalhamos apenas com a troca de peças: nosso objetivo é identificar a causa do problema e executar o reparo adequado.</p>
    """,
    faq_items=[
        ("Vocês trabalham com Dualogic?", "Sim. A DT28 é especializada em diagnóstico, manutenção e reparo de transmissões Dualogic."),
        ("O Dualogic precisa de óleo específico?", "Cada aplicação tem uma especificação própria de fluido. Avaliamos o veículo para indicar o produto e o procedimento corretos."),
        ("Dá para reparar sem trocar o câmbio inteiro?", "Em muitos casos sim. O problema costuma estar em componentes específicos, como o atuador ou a embreagem, e pode ser resolvido com reparo direcionado após o diagnóstico."),
    ],
    hero_img="/img/dualogic-hero.webp",
    hero_img_alt="Unidade de câmbio Dualogic sobre bancada da DT28 Automáticos",
    hero_img_w="483", hero_img_h="932",
)

# ---------------------------------------------------------------
# I-MOTION
# ---------------------------------------------------------------
build_page(
    key="imotion",
    title="Câmbio I-MOTION: Diagnóstico e Reparo em Sarandi e Maringá | DT28 Automáticos",
    description="Especialista em câmbio I-MOTION em Sarandi e Maringá. Diagnóstico eletrônico, manutenção e reparo com garantia por escrito. Fale com a DT28 no WhatsApp.",
    h1="Câmbio I-MOTION em Sarandi e Maringá",
    lead="A DT28 Automáticos é referência regional em diagnóstico, manutenção e reparo de transmissões I-MOTION.",
    eyebrow="Especialista em I-MOTION",
    wa_msg="Olá! Meu carro tem câmbio I-MOTION e está com problema. Carro/ano: ____ Sintoma: ____",
    body_html="""
        <h2>O que é o câmbio I-MOTION</h2>
        <p>O I-MOTION é um sistema de transmissão automatizada: assim como o Dualogic, parte de uma caixa manual, mas as trocas de marcha e o acionamento da embreagem são feitos por atuadores eletrônicos, sem pedal de embreagem para o motorista. O bom funcionamento depende diretamente da calibração eletrônica e da leitura correta dos sensores do sistema.</p>

        <h2>Principais sintomas de problema no câmbio I-MOTION</h2>
        <ul>
          <li>Trancos nas trocas de marcha</li>
          <li>Patinação ou hesitação na aceleração</li>
          <li>Demora para engatar a marcha</li>
          <li>Luz de câmbio ou de injeção acesa</li>
          <li>Ativação do modo de emergência</li>
          <li>Dificuldade para engrenar a partir do ponto morto</li>
        </ul>

        <h2>Possíveis causas</h2>
        <p>Os sintomas do I-MOTION podem ter origem em diferentes pontos — atuador de marchas, embreagem, unidade eletrônica (TCM) ou calibração do sistema. Cada veículo apresenta um quadro próprio, e a causa exata só é confirmada com diagnóstico eletrônico.</p>

        <h2>A importância do diagnóstico</h2>
        <p>O diagnóstico eletrônico permite identificar exatamente qual componente está gerando o sintoma antes de qualquer reparo, evitando substituições desnecessárias e direcionando o serviço para a causa real do problema.</p>

        <h2>Serviços realizados pela DT28 em câmbio I-MOTION</h2>
        <ul>
          <li>Diagnóstico eletrônico do sistema I-MOTION</li>
          <li>Manutenção preventiva e corretiva</li>
          <li>Reparo de componentes do câmbio</li>
          <li>Leitura e programação de TCM com aparelho avançado, quando aplicável ao veículo</li>
        </ul>
        <p>Não trabalhamos apenas com a troca de peças: nosso objetivo é identificar a causa do problema e executar o reparo adequado.</p>
    """,
    faq_items=[
        ("Vocês trabalham com I-MOTION?", "Sim. A DT28 é especializada em diagnóstico, manutenção e reparo de transmissões I-MOTION."),
        ("Qual a diferença entre I-MOTION e um câmbio automático convencional?", "O I-MOTION é uma transmissão automatizada: usa uma base de câmbio manual com acionamento eletrônico da embreagem e das marchas, diferente do automático convencional, que utiliza conversor de torque."),
        ("Dá para reparar sem trocar o câmbio inteiro?", "Em muitos casos sim. O problema costuma estar em componentes específicos, e pode ser resolvido com reparo direcionado após o diagnóstico."),
    ],
    hero_img="/img/imotion-hero.webp",
    hero_img_alt="Unidade de câmbio I-MOTION sobre bancada da DT28 Automáticos",
    hero_img_w="483", hero_img_h="932",
)

# ---------------------------------------------------------------
# AUTOMATIZADO
# ---------------------------------------------------------------
build_page(
    key="automatizado",
    title="Câmbio Automatizado: Diagnóstico e Manutenção em Sarandi e Maringá | DT28",
    description="Especialistas em câmbio automatizado em Sarandi e Maringá: Dualogic, I-MOTION, EASYTRONIC. Diagnóstico eletrônico e reparo com garantia. WhatsApp DT28.",
    h1="Câmbio Automatizado em Sarandi e Maringá",
    lead="Trabalhamos com diagnóstico, manutenção e reparo de sistemas de câmbio automatizado, com destaque para Dualogic e I-MOTION.",
    eyebrow="Câmbio automatizado",
    wa_msg="Olá! Meu carro tem câmbio automatizado e está com problema. Carro/ano: ____ Sintoma: ____",
    body_html="""
        <h2>O que é o câmbio automatizado</h2>
        <p>Automatizado é o nome dado às transmissões que utilizam uma caixa de câmbio manual com o acionamento das marchas e da embreagem controlado eletronicamente, sem embreagem manual para o motorista. Dualogic, I-MOTION e EASYTRONIC são exemplos desse tipo de sistema, cada um com sua própria central eletrônica e lógica de funcionamento.</p>

        <h2>Principais sintomas de problema no câmbio automatizado</h2>
        <ul>
          <li>Trancos nas trocas de marcha</li>
          <li>Demora para engatar ou confirmar a marcha</li>
          <li>Falhas nas trocas</li>
          <li>Luz de câmbio ou de injeção acesa</li>
          <li>Ativação do modo de emergência</li>
        </ul>

        <h2>Possíveis causas</h2>
        <p>Como o sistema depende de atuadores eletrônicos, embreagem e uma unidade de controle própria, os sintomas podem ter diferentes origens. A causa exata é identificada por meio de diagnóstico eletrônico, específico para cada sistema.</p>

        <h2>A importância do diagnóstico</h2>
        <p>Cada sistema automatizado tem particularidades de calibração e leitura eletrônica. Por isso, o diagnóstico correto — específico para Dualogic, I-MOTION ou EASYTRONIC — é o que direciona o reparo para a causa real do problema.</p>

        <h2>Serviços realizados pela DT28 em câmbio automatizado</h2>
        <ul>
          <li>Diagnóstico eletrônico especializado por sistema</li>
          <li>Manutenção preventiva e corretiva</li>
          <li>Reparo de componentes do câmbio</li>
          <li>Leitura e programação de TCM com aparelho avançado, quando aplicável ao veículo</li>
        </ul>
        <div class="content-image">
          <img src="/img/mecatronica-vw.webp" alt="Módulo de mecatrônica sobre bancada da DT28 Automáticos" loading="lazy" decoding="async" width="483" height="932">
          <span class="content-image-cap">Mecatrônica: unidade eletrônica que comanda os atuadores do câmbio automatizado</span>
        </div>

        <p>Veja o conteúdo específico de <a href="/cambio-dualogic">câmbio Dualogic</a> e <a href="/cambio-i-motion">câmbio I-MOTION</a>, nossos dois sistemas automatizados de maior especialização.</p>
    """,
    faq_items=[
        ("O câmbio automatizado precisa de manutenção?", "A manutenção depende do sistema, do veículo, das condições de uso e do histórico da transmissão. O ideal é realizar uma avaliação técnica."),
        ("Automatizado é a mesma coisa que automático?", "Não. O automatizado parte de uma base de câmbio manual com acionamento eletrônico das marchas e da embreagem. O automático convencional usa conversor de torque."),
        ("Vocês atendem Dualogic e I-MOTION?", "Sim, são nossas duas maiores especialidades dentro dos sistemas automatizados."),
    ],
    hero_img="/img/dualogic-imotion-banner.webp",
    hero_img_alt="Componentes de câmbio automatizado (Dualogic e I-MOTION) sobre bancada da DT28",
    hero_img_w="1400", hero_img_h="933",
)

# ---------------------------------------------------------------
# DSG
# ---------------------------------------------------------------
build_page(
    key="dsg",
    title="Câmbio DSG: Diagnóstico e Manutenção em Sarandi e Maringá | DT28 Automáticos",
    description="Diagnóstico e manutenção de câmbio DSG em Sarandi e Maringá. Mecatrônica, leitura eletrônica e reparo com garantia por escrito. Fale com a DT28.",
    h1="Câmbio DSG em Sarandi e Maringá",
    lead="Trabalhamos com diagnóstico e manutenção de transmissões DSG, incluindo mecatrônica e leitura eletrônica.",
    eyebrow="Especialista em DSG",
    wa_msg="Olá! Meu carro tem câmbio DSG e está com problema. Carro/ano: ____ Sintoma: ____",
    body_html="""
        <h2>O que é o câmbio DSG</h2>
        <p>O DSG é uma transmissão automática de dupla embreagem: utiliza dois conjuntos de embreagem que trabalham de forma alternada para realizar trocas de marcha rápidas, sem interrupção de torque. O controle é feito por uma unidade eletrônica (mecatrônica), responsável por comandar embreagens e atuadores.</p>

        <h2>Principais sintomas de problema no câmbio DSG</h2>
        <ul>
          <li>Trancos nas trocas de marcha</li>
          <li>Vibração ao arrancar ou em baixa velocidade</li>
          <li>Ruído incomum durante as trocas</li>
          <li>Luz de câmbio acesa no painel</li>
          <li>Ativação do modo de emergência</li>
        </ul>

        <h2>Possíveis causas</h2>
        <p>Os sintomas do DSG costumam estar relacionados à mecatrônica, às embreagens duplas ou ao nível e qualidade do óleo da transmissão. A confirmação da causa depende de diagnóstico eletrônico específico para o sistema.</p>

        <h2>A importância do diagnóstico</h2>
        <p>Por ser um sistema de dupla embreagem com controle totalmente eletrônico, o DSG exige leitura eletrônica precisa antes de qualquer intervenção, evitando reparo ou troca de peças sem necessidade.</p>

        <h2>Serviços realizados pela DT28 em câmbio DSG</h2>
        <ul>
          <li>Diagnóstico eletrônico do sistema DSG</li>
          <li>Manutenção preventiva e corretiva</li>
          <li>Reparo de mecatrônica</li>
          <li>Leitura e programação de TCM com aparelho avançado (compatível com DQ200, DQ250 e outros)</li>
          <li>Troca de óleo por diálise, conforme aplicação da transmissão</li>
        </ul>

        <div class="content-image">
          <img src="/img/tcm-programacao.webp" alt="Programação de TCM da DT28 em módulo Audi DQ200/0CW com notebook" loading="lazy" decoding="async" width="1300" height="866">
          <span class="content-image-cap">Programação de TCM com aparelho avançado, compatível com DQ200 e DQ250</span>
        </div>

        <div class="content-image">
          <img src="/img/dsg-detalhe.webp" alt="Unidade de câmbio DSG sobre bancada da DT28 Automáticos" loading="lazy" decoding="async" width="512" height="341">
          <span class="content-image-cap">Unidade DSG em diagnóstico na oficina DT28</span>
        </div>
    """,
    faq_items=[
        ("Vocês trabalham com DSG?", "Sim. A DT28 trabalha com transmissões DSG."),
        ("Vocês fazem troca de óleo por diálise no DSG?", "Sim. A DT28 realiza troca de fluido utilizando equipamento de diálise, conforme aplicação e especificação da transmissão."),
        ("Quais modelos de mecatrônica DSG vocês atendem?", "Trabalhamos com programação de TCM com aparelho avançado, incluindo DQ200, DQ250 e outros. Envie o modelo e o ano do seu carro pelo WhatsApp para confirmarmos o atendimento."),
    ],
    hero_img="/img/dsg-hero.webp",
    hero_img_alt="Mecatrônica de câmbio DSG Volkswagen sobre bancada da DT28 Automáticos",
    hero_img_w="1145", hero_img_h="1374",
)

# ---------------------------------------------------------------
# CVT
# ---------------------------------------------------------------
build_page(
    key="cvt",
    title="Câmbio CVT: Diagnóstico e Manutenção em Sarandi e Maringá | DT28 Automáticos",
    description="Especialistas em câmbio CVT em Sarandi e Maringá: correia, polias, corpo de válvulas e TCM. Diagnóstico eletrônico e troca de óleo por diálise.",
    h1="Câmbio CVT em Sarandi e Maringá",
    lead="Trabalhamos com diagnóstico e manutenção de transmissões CVT, da correia ao corpo de válvulas.",
    eyebrow="Especialista em CVT",
    wa_msg="Olá! Meu carro tem câmbio CVT e gostaria de um diagnóstico/orçamento. Carro/ano: ____ Sintoma: ____",
    body_html="""
        <h2>O que é o câmbio CVT</h2>
        <p>O CVT (transmissão continuamente variável) não utiliza marchas fixas: um sistema de polias e correia (ou corrente) varia a relação de transmissão de forma contínua, controlado por uma unidade eletrônica (TCM) que ajusta a tensão e a posição das polias conforme a condução.</p>

        <h2>Principais sintomas de problema no câmbio CVT</h2>
        <ul>
          <li>Patinação, principalmente em acelerações</li>
          <li>Sensação de "elástico" — motor acelera sem resposta proporcional</li>
          <li>Ruído ou vibração durante a condução</li>
          <li>Superaquecimento da transmissão</li>
          <li>Luz de câmbio acesa no painel</li>
        </ul>

        <h2>Possíveis causas</h2>
        <p>Os sintomas do CVT costumam estar relacionados ao desgaste da correia ou corrente, ao corpo de válvulas, à unidade eletrônica (TCM) ou ao óleo fora da especificação correta para o sistema. O diagnóstico eletrônico é o que confirma a causa real.</p>

        <h2>A importância do diagnóstico</h2>
        <p>Como o CVT é sensível à especificação do óleo e à calibração eletrônica, o diagnóstico antes do reparo evita intervenções desnecessárias e direciona o serviço para a causa correta — que pode ser um componente específico, e não o câmbio inteiro.</p>

        <h2>Serviços realizados pela DT28 em câmbio CVT</h2>
        <ul>
          <li>Diagnóstico eletrônico especializado em CVT</li>
          <li>Manutenção de correia, polias e corpo de válvulas</li>
          <li>Leitura e programação de TCM com aparelho avançado</li>
          <li>Troca de óleo por diálise, conforme aplicação da transmissão</li>
        </ul>

        <div class="content-image">
          <img src="/img/dialise-oleo.webp" alt="Equipamento de troca de óleo por diálise da DT28 Automáticos" loading="lazy" decoding="async" width="512" height="342">
          <span class="content-image-cap">Troca de óleo por diálise: fluido limpo, mais vida útil para a transmissão</span>
        </div>
    """,
    faq_items=[
        ("Vocês trabalham com CVT?", "Sim. A DT28 trabalha com transmissões CVT."),
        ("Vocês fazem troca de óleo CVT por diálise?", "Sim. A DT28 realiza troca de fluido utilizando equipamento de diálise, conforme aplicação e especificação da transmissão."),
        ("Patinação no CVT sempre significa troca da correia?", "Não necessariamente. A patinação pode estar relacionada à correia, ao corpo de válvulas ou à TCM. O diagnóstico é o que indica o componente exato."),
    ],
    hero_img="/img/cvt-hero.webp",
    hero_img_alt="Unidade de câmbio CVT sobre bancada da DT28 Automáticos",
    hero_img_w="512", hero_img_h="341",
)

print("done")
