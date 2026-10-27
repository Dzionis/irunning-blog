(function () {
  if (window.matchMedia && window.matchMedia('(prefers-reduced-motion: reduce)').matches) return;

  var observer = new IntersectionObserver(
    function (entries) {
      var visible = entries.filter(function (e) { return e.isIntersecting; });
      visible.forEach(function (entry, i) {
        var el = entry.target;
        el.style.transitionDelay = (i * 80) + 'ms';
        el.classList.add('is-visible');
        observer.unobserve(el);
        // Drop the reveal classes once done so hover transforms work again
        setTimeout(function () {
          el.style.transitionDelay = '';
          el.classList.remove('animate-on-scroll', 'is-visible');
        }, 650 + i * 80);
      });
    },
    { threshold: 0.12 }
  );

  document.querySelectorAll(
    '.feature-card, .split-card, .review-card, .post-card, .session-card, .shot-card, .watch-card'
  ).forEach(function (card) {
    card.classList.add('animate-on-scroll');
    observer.observe(card);
  });
})();
