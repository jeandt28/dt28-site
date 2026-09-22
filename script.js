// DT28 Automáticos — JS mínimo, sem dependências externas
(function () {
  "use strict";

  // Menu mobile
  var menuBtn = document.querySelector("[data-menu-open]");
  var closeBtn = document.querySelector("[data-menu-close]");
  var mobileNav = document.querySelector("[data-mobile-nav]");

  function openMenu() {
    if (!mobileNav) return;
    mobileNav.classList.add("is-open");
    document.body.style.overflow = "hidden";
  }
  function closeMenu() {
    if (!mobileNav) return;
    mobileNav.classList.remove("is-open");
    document.body.style.overflow = "";
  }
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

  // Ano no rodapé
  var yearEl = document.querySelector("[data-year]");
  if (yearEl) yearEl.textContent = new Date().getFullYear();
})();
