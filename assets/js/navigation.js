(function () {
  var header = document.querySelector('.site-header');
  var links = Array.prototype.slice.call(document.querySelectorAll('.nav-links a[href^="#"]'));
  var sections = links.map(function (link) {
    return { link: link, section: document.getElementById(link.hash.slice(1)) };
  }).filter(function (entry) { return entry.section; });
  if (!sections.length) return;

  function update() {
    var marker = (header ? header.getBoundingClientRect().bottom : 0) +
                 Math.min(160, window.innerHeight * 0.25);
    var current = null;
    sections.forEach(function (entry) {
      if (entry.section.getBoundingClientRect().top <= marker) current = entry;
    });
    sections.forEach(function (entry) {
      if (entry === current) entry.link.setAttribute('aria-current', 'location');
      else entry.link.removeAttribute('aria-current');
    });
  }

  var scheduled = false;
  function scheduleUpdate() {
    if (scheduled) return;
    scheduled = true;
    window.requestAnimationFrame(function () {
      scheduled = false;
      update();
    });
  }
  window.addEventListener('scroll', scheduleUpdate, { passive: true });
  window.addEventListener('resize', scheduleUpdate);
  window.addEventListener('load', scheduleUpdate);
  window.addEventListener('hashchange', scheduleUpdate);
  if (document.fonts && document.fonts.ready) document.fonts.ready.then(scheduleUpdate);
  update();
})();
