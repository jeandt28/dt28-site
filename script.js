// DT28 Câmbios Automáticos — JS mínimo, sem dependências externas
(function () {
  "use strict";

  // Menu mobile
  var menuBtn = document.querySelector("[data-menu-open]");
  var closeBtn = document.querySelector("[data-menu-close]");
  var mobileNav = document.querySelector("[data-mobile-nav]");

  if (menuBtn) menuBtn.setAttribute("aria-expanded", "false");
  function openMenu() {
    if (!mobileNav) return;
    mobileNav.classList.add("is-open");
    document.body.style.overflow = "hidden";
    if (menuBtn) menuBtn.setAttribute("aria-expanded", "true");
    if (closeBtn) closeBtn.focus();
  }
  function closeMenu() {
    if (!mobileNav) return;
    mobileNav.classList.remove("is-open");
    document.body.style.overflow = "";
    if (menuBtn) menuBtn.setAttribute("aria-expanded", "false");
  }
  document.addEventListener("keydown", function (e) {
    if (e.key === "Escape" && mobileNav && mobileNav.classList.contains("is-open")) {
      closeMenu();
      if (menuBtn) menuBtn.focus();
    }
  });
  if (menuBtn) menuBtn.addEventListener("click", openMenu);
  if (closeBtn) closeBtn.addEventListener("click", closeMenu);
  if (mobileNav) {
    mobileNav.querySelectorAll("a").forEach(function (a) {
      a.addEventListener("click", closeMenu);
    });
  }

  // Header: leve sombra ao rolar
  var header = document.querySelector(".site-header");
  if (header) {
    var onScroll = function () {
      if (window.scrollY > 6) header.style.borderBottomColor = "rgba(227,19,42,.35)";
      else header.style.borderBottomColor = "";
    };
    window.addEventListener("scroll", onScroll, { passive: true });
  }

  // Medição de contatos (WhatsApp e telefone).
  // Envia eventos para o GA4 (gtag) ou Google Tag Manager (dataLayer) somente se já estiverem instalados.
  // Um clique registra a intenção de contato, não um orçamento ou cliente.
  document.addEventListener("click", function (e) {
    var a = e.target.closest ? e.target.closest("a[href]") : null;
    if (!a) return;
    var href = a.getAttribute("href") || "";
    var tipo = href.indexOf("wa.me/") !== -1 ? "whatsapp" : (href.indexOf("tel:") === 0 ? "telefone" : null);
    if (!tipo) return;
    var dados = {
      contact_method: tipo,
      link_text: (a.textContent || a.getAttribute("aria-label") || "").trim().slice(0, 80),
      page_path: location.pathname
    };
    var nome = tipo === "whatsapp" ? "click_whatsapp" : "click_telefone";
    if (typeof window.gtag === "function") {
      window.gtag("event", nome, dados);
    } else if (Array.isArray(window.dataLayer)) {
      dados.event = nome;
      window.dataLayer.push(dados);
    }
  });

  // Instagram: carrega o script de incorporação só quando a seção se aproxima da tela
  var igSection = document.querySelector(".ig-grid");
  if (igSection) {
    var loadIg = function () {
      if (document.querySelector('script[src*="instagram.com/embed.js"]')) return;
      var sc = document.createElement("script");
      sc.async = true;
      sc.src = "https://www.instagram.com/embed.js";
      document.body.appendChild(sc);
    };
    if ("IntersectionObserver" in window) {
      var io = new IntersectionObserver(function (entries) {
        if (entries.some(function (en) { return en.isIntersecting; })) { loadIg(); io.disconnect(); }
      }, { rootMargin: "600px 0px" });
      io.observe(igSection);
    } else {
      loadIg();
    }
  }

  // Vídeo do topo: começa sozinho sem som (os navegadores bloqueiam som automático).
  // O botão liga o som e recomeça a apresentação do início.
  var heroVideo = document.querySelector("[data-hero-video]");
  var soundBtn = document.querySelector("[data-video-sound]");
  if (heroVideo) {
    var reduce = window.matchMedia && window.matchMedia("(prefers-reduced-motion: reduce)").matches;
    if (reduce) { heroVideo.removeAttribute("autoplay"); heroVideo.pause(); }
    else {
      // Espera a página terminar de carregar para não disputar banda com o conteúdo principal
      var startVideo = function () { var p = heroVideo.play(); if (p && p.catch) p.catch(function () {}); };
      if (document.readyState === "complete") startVideo();
      else window.addEventListener("load", startVideo, { once: true });
    }
  }
  if (heroVideo && soundBtn) {
    soundBtn.addEventListener("click", function () {
      if (heroVideo.muted) {
        heroVideo.muted = false;
        heroVideo.loop = false;
        heroVideo.currentTime = 0;
        heroVideo.play();
        soundBtn.textContent = "🔇 Sem som";
        soundBtn.setAttribute("aria-pressed", "true");
        if (typeof window.gtag === "function") window.gtag("event", "video_som_ativado");
        else if (Array.isArray(window.dataLayer)) window.dataLayer.push({ event: "video_som_ativado" });
      } else {
        heroVideo.muted = true;
        soundBtn.textContent = "🔊 Ouvir o Jean";
        soundBtn.setAttribute("aria-pressed", "false");
      }
    });
    heroVideo.addEventListener("ended", function () {
      heroVideo.muted = true; heroVideo.loop = true; heroVideo.play();
      soundBtn.textContent = "🔊 Ouvir o Jean";
      soundBtn.setAttribute("aria-pressed", "false");
    });
  }

  // Galeria: amplia a foto em tela cheia, com setas e tecla Esc
  var lb = document.querySelector("[data-lightbox]");
  var links = Array.prototype.slice.call(document.querySelectorAll("[data-galeria]"));
  if (lb && links.length && typeof lb.showModal === "function") {
    var lbImg = lb.querySelector("[data-lb-img]"), lbCap = lb.querySelector("[data-lb-cap]"), atual = 0;
    var mostrar = function (i) {
      atual = (i + links.length) % links.length;
      var a = links[atual], img = a.querySelector("img"), cap = a.parentNode.querySelector("figcaption");
      lbImg.src = a.getAttribute("href");
      lbImg.alt = img ? img.alt : "";
      lbCap.textContent = cap ? cap.textContent : "";
    };
    links.forEach(function (a, i) {
      a.addEventListener("click", function (e) { e.preventDefault(); mostrar(i); lb.showModal(); });
    });
    lb.querySelector("[data-lb-close]").addEventListener("click", function () { lb.close(); });
    lb.querySelector("[data-lb-prev]").addEventListener("click", function () { mostrar(atual - 1); });
    lb.querySelector("[data-lb-next]").addEventListener("click", function () { mostrar(atual + 1); });
    lb.addEventListener("click", function (e) { if (e.target === lb) lb.close(); });
    lb.addEventListener("keydown", function (e) {
      if (e.key === "ArrowLeft") mostrar(atual - 1);
      if (e.key === "ArrowRight") mostrar(atual + 1);
    });
    lb.addEventListener("close", function () { lbImg.removeAttribute("src"); if (links[atual]) links[atual].focus(); });
  }

  // Ano no rodapé
  var yearEl = document.querySelector("[data-year]");
  if (yearEl) yearEl.textContent = new Date().getFullYear();

  // Revelação suave ao rolar: só para blocos abaixo da primeira tela; sem JS tudo aparece normalmente
  var reduceMotion = window.matchMedia && window.matchMedia("(prefers-reduced-motion: reduce)").matches;
  if (!reduceMotion && "IntersectionObserver" in window) {
    var alvos = document.querySelectorAll(".section-head, .card, .step, .gallery-item, .galeria-item, .spot-card, .faq-item, .final-cta, .video-frame, .evidence-item, .content-image");
    var limite = window.innerHeight * 0.9;
    var revIo = new IntersectionObserver(function (entries) {
      entries.forEach(function (en) {
        if (!en.isIntersecting) return;
        en.target.classList.add("is-in");
        revIo.unobserve(en.target);
      });
    }, { rootMargin: "0px 0px -8% 0px" });
    var pendentes = 0;
    alvos.forEach(function (el) {
      if (el.getBoundingClientRect().top < limite) return;
      el.classList.add("reveal"); revIo.observe(el); pendentes++;
    });
    if (pendentes) document.documentElement.classList.add("js-reveal");
  }
})();
