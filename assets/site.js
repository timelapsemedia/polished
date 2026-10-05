/* Shared script for polished.media subpages: mobile menu + consent-aware GA4.
   Uses the same consent key as /index.html, so a choice made on any page applies site-wide. */
(function () {
  var toggle = document.getElementById('menuToggle');
  var links = document.getElementById('navLinks');
  if (toggle && links) {
    toggle.addEventListener('click', function () {
      var open = links.classList.toggle('mobile-open');
      toggle.classList.toggle('open', open);
      toggle.setAttribute('aria-expanded', open ? 'true' : 'false');
    });
  }

  var GA_ID = 'G-CP8GKKDKCV';
  var CONSENT_KEY = 'polished_analytics_consent';
  var de = document.documentElement.lang === 'de';

  function loadGA() {
    if (window.gtag) return;
    var s = document.createElement('script');
    s.async = true;
    s.src = 'https://www.googletagmanager.com/gtag/js?id=' + GA_ID;
    document.head.appendChild(s);
    window.dataLayer = window.dataLayer || [];
    window.gtag = function () { window.dataLayer.push(arguments); };
    window.gtag('js', new Date());
    window.gtag('config', GA_ID, { cookie_flags: 'SameSite=None;Secure', cookie_expires: 60 * 60 * 24 * 180 });
  }

  function track(name, params) {
    window.dataLayer = window.dataLayer || [];
    window.dataLayer.push(Object.assign({ event: name }, params || {}));
    if (window.gtag) window.gtag('event', name, params || {});
  }
  document.querySelectorAll('[data-track]').forEach(function (el) {
    el.addEventListener('click', function () { track('cta_click', { cta_id: el.getAttribute('data-track') }); });
  });

  var stored = null;
  try { stored = localStorage.getItem(CONSENT_KEY); } catch (e) {}
  if (stored === 'granted') { loadGA(); return; }
  if (stored === 'denied') return;

  var banner = document.createElement('div');
  banner.className = 'cookie-banner';
  banner.setAttribute('role', 'dialog');
  banner.setAttribute('aria-label', de ? 'Cookie-Einstellungen' : 'Cookie settings');
  banner.innerHTML = de
    ? '<p>Wir nutzen Google Analytics, um anonym zu verstehen, wie polished.media genutzt wird. Du entscheidest frei und kannst deine Wahl jederzeit ändern. Details in der <a href="/#privacy">Datenschutzerklärung</a>.</p><div class="cookie-actions"><button class="cookie-btn" data-c="denied">Nur notwendige</button><button class="cookie-btn primary" data-c="granted">Akzeptieren</button></div>'
    : '<p>We use Google Analytics to anonymously understand how polished.media is used. You\'re free to choose and can change your choice at any time. Details in the <a href="/#privacy">Privacy Policy</a>.</p><div class="cookie-actions"><button class="cookie-btn" data-c="denied">Necessary Only</button><button class="cookie-btn primary" data-c="granted">Accept</button></div>';
  document.body.appendChild(banner);
  setTimeout(function () { banner.classList.add('show'); }, 1500);
  banner.querySelectorAll('[data-c]').forEach(function (btn) {
    btn.addEventListener('click', function () {
      var v = btn.getAttribute('data-c');
      try { localStorage.setItem(CONSENT_KEY, v); } catch (e) {}
      if (v === 'granted') loadGA();
      banner.classList.remove('show');
    });
  });
})();
