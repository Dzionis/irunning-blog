(function () {
  // Header: hairline + shadow only once the page has scrolled
  var header = document.querySelector('.site-header');
  // Post pages: thin reading-progress bar under the header
  var progress = document.querySelector('.read-progress span');
  var article = document.querySelector('.post-content');

  function onScroll() {
    var y = window.scrollY || window.pageYOffset;
    if (header) header.classList.toggle('is-scrolled', y > 8);
    if (progress && article) {
      var rect = article.getBoundingClientRect();
      var total = rect.height - window.innerHeight * 0.6;
      var done = Math.min(1, Math.max(0, -rect.top / (total > 0 ? total : 1)));
      progress.style.transform = 'scaleX(' + done + ')';
    }
  }
  window.addEventListener('scroll', onScroll, { passive: true });
  onScroll();

  // Blog listing: category filter chips, deep-linkable as /blog/#training
  var grid = document.getElementById('posts-grid');
  var chips = document.querySelectorAll('.filter-chip');
  if (!grid || !chips.length) return;
  var cards = grid.querySelectorAll('.post-card');

  function apply(filter, fromHash) {
    var known = false;
    chips.forEach(function (chip) { if (chip.dataset.filter === filter) known = true; });
    if (!known) filter = 'all';
    chips.forEach(function (chip) {
      var on = chip.dataset.filter === filter;
      chip.classList.toggle('is-active', on);
      chip.setAttribute('aria-pressed', on ? 'true' : 'false');
    });
    grid.classList.toggle('is-filtered', filter !== 'all');
    cards.forEach(function (card) {
      var show = filter === 'all' || card.dataset.category === filter;
      card.hidden = !show;
      if (show) card.classList.add('is-visible');
    });
    if (!fromHash) {
      history.replaceState(null, '', filter === 'all' ? location.pathname : '#' + filter);
    }
  }

  chips.forEach(function (chip) {
    chip.addEventListener('click', function () { apply(chip.dataset.filter, false); });
  });
  window.addEventListener('hashchange', function () { apply(location.hash.slice(1), true); });
  if (location.hash) apply(location.hash.slice(1), true);
})();
