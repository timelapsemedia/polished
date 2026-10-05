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

  // Inquiry forms (FormSubmit AJAX -> polished.media@gmx.de)
  document.querySelectorAll('form[data-formsubmit]').forEach(function (form) {
    var de = form.getAttribute('data-lang') === 'de';
    var t = de ? {
      required: 'Bitte fülle alle Pflichtfelder aus und bestätige die Datenschutzerklärung.',
      email: 'Bitte gib eine gültige E-Mail-Adresse ein.',
      sending: 'Wird gesendet …', sent: '✓ Anfrage gesendet', submit: 'Anfrage senden →',
      ok: function (e) { return '<strong>Danke, deine Anfrage ist angekommen.</strong><br>Tim antwortet persönlich an ' + e + ', meist innerhalb von 24 Stunden.'; },
      fail: 'Das Senden hat gerade nicht geklappt. Bitte versuch es noch einmal oder schreib direkt an '
    } : {
      required: 'Please fill in all required fields and accept the privacy policy.',
      email: 'Please enter a valid email address.',
      sending: 'Sending…', sent: '✓ Request sent', submit: 'Send Request →',
      ok: function (e) { return '<strong>Thanks — your request is in.</strong><br>I\'ll reply personally to ' + e + ', usually within 24 hours.'; },
      fail: 'Sending didn\'t work just now. Please try again, or email me directly at '
    };
    var statusEl = form.querySelector('.form-status');
    var btn = form.querySelector('button[type="submit"]');
    function val(name) { var el = form.elements[name]; return el ? el.value.trim() : ''; }
    function show(cls, htmlText) { statusEl.className = 'form-status show ' + cls; statusEl.innerHTML = htmlText; }
    form.addEventListener('submit', function (e) {
      e.preventDefault();
      if (val('_honey')) return;
      var name = val('name'), email = val('email'), message = val('message');
      var genre = val('genre'), service = val('service'), tracks = val('tracks'), files = val('files');
      if (!name || !email || !message || !form.elements.consent.checked) { show('error', t.required); return; }
      if (!/^[^\s@]+@[^\s@]+\.[^\s@]+$/.test(email)) { show('error', t.email); return; }
      var subject = (de ? 'Mastering-Anfrage' : 'Mastering Inquiry') + (service ? ' · ' + service : '') + (genre ? ' · ' + genre : '') + ' — ' + name;
      var mail = '<a href="mailto:polished.media@gmx.de?subject=' + encodeURIComponent(subject) + '">polished.media@gmx.de</a>.';
      btn.disabled = true; btn.textContent = t.sending; statusEl.className = 'form-status';
      fetch('https://formsubmit.co/ajax/polished.media@gmx.de', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json', 'Accept': 'application/json' },
        body: JSON.stringify({
          name: name, email: email, genre: genre || '—', service: service || '—', tracks: tracks || '—',
          files: files || '—', message: message, language: de ? 'Deutsch' : 'English',
          consent: 'Requester agreed to the privacy policy',
          _subject: subject, _replyto: email, _template: 'table', _captcha: 'false'
        })
      })
        .then(function (res) { return res.json().then(function (data) { return { ok: res.ok, data: data }; }); })
        .then(function (r) {
          if (!r.ok || String(r.data.success) !== 'true') throw new Error(r.data.message || 'failed');
          track('form_submit', { service: service, genre: genre, lang: de ? 'de' : 'en' });
          track('generate_lead', { service: service, genre: genre, lang: de ? 'de' : 'en' });
          form.reset();
          show('success', t.ok(email.replace(/[<>&"]/g, '')));
          btn.textContent = t.sent;
          setTimeout(function () { btn.textContent = t.submit; btn.disabled = false; }, 8000);
        })
        .catch(function () {
          show('error', t.fail + mail);
          btn.textContent = t.submit; btn.disabled = false;
        });
    });
  });

  function disableGA() {
    window['ga-disable-' + GA_ID] = true;
    document.cookie.split(';').map(function (c) { return c.trim().split('=')[0]; })
      .filter(function (n) { return n.indexOf('_ga') === 0; })
      .forEach(function (n) {
        document.cookie = n + '=; Max-Age=0; path=/';
        document.cookie = n + '=; Max-Age=0; path=/; domain=.' + location.hostname;
      });
  }

  var banner = document.createElement('div');
  banner.className = 'cookie-banner';
  banner.setAttribute('role', 'dialog');
  banner.setAttribute('aria-label', de ? 'Cookie-Einstellungen' : 'Cookie settings');
  banner.innerHTML = de
    ? '<p>Wir nutzen Google Analytics, um anonym zu verstehen, wie polished.media genutzt wird. Du entscheidest frei und kannst deine Wahl jederzeit über „Cookie-Einstellungen“ im Footer ändern. Details in der <a href="/#privacy">Datenschutzerklärung</a>.</p><div class="cookie-actions"><button class="cookie-btn" data-c="denied">Nur notwendige</button><button class="cookie-btn primary" data-c="granted">Akzeptieren</button></div>'
    : '<p>We use Google Analytics to anonymously understand how polished.media is used. You\'re free to choose and can change your choice any time via "Cookie settings" in the footer. Details in the <a href="/#privacy">Privacy Policy</a>.</p><div class="cookie-actions"><button class="cookie-btn" data-c="denied">Necessary Only</button><button class="cookie-btn primary" data-c="granted">Accept</button></div>';
  document.body.appendChild(banner);
  banner.querySelectorAll('[data-c]').forEach(function (btn) {
    btn.addEventListener('click', function () {
      var v = btn.getAttribute('data-c');
      try { localStorage.setItem(CONSENT_KEY, v); } catch (e) {}
      if (v === 'granted') loadGA(); else disableGA();
      banner.classList.remove('show');
    });
  });
  document.querySelectorAll('.cookie-settings-link').forEach(function (a) {
    a.addEventListener('click', function (e) { e.preventDefault(); banner.classList.add('show'); });
  });

  var stored = null;
  try { stored = localStorage.getItem(CONSENT_KEY); } catch (e) {}
  if (stored === 'granted') loadGA();
  else if (stored !== 'denied') setTimeout(function () { banner.classList.add('show'); }, 1500);
})();
