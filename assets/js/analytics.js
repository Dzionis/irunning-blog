(function () {
  // Tag every App Store link with a campaign token (ct) so App Store Connect
  // can attribute installs; sessions arriving from ads get ct=pmax for the
  // whole visit. Runs before the gtag guard so links get tagged even when
  // analytics is blocked.
  try {
    var searchParams = new URLSearchParams(window.location.search);
    if (searchParams.has('gclid') || searchParams.get('utm_medium') === 'cpc') {
      sessionStorage.setItem('irun_ct', 'pmax');
    }
    var ct = sessionStorage.getItem('irun_ct') || 'website';
    document.querySelectorAll('a[href*="apps.apple.com"]').forEach(function (link) {
      var url = new URL(link.href);
      url.searchParams.set('ct', ct);
      url.searchParams.set('mt', '8');
      link.href = url.toString();
    });
  } catch (e) { /* sessionStorage unavailable (private mode) — links stay untagged */ }

  if (typeof gtag !== 'function') return;

  var pageName = document.title;

  function track(eventName, params) {
    gtag('event', eventName, Object.assign({ page_name: pageName }, params));
  }

  // Event delegation for all [data-ga-event] elements
  document.addEventListener('click', function (e) {
    var el = e.target.closest('[data-ga-event]');
    if (!el) return;

    var eventName = el.getAttribute('data-ga-event');
    var location  = el.getAttribute('data-ga-location') || '';
    var destination = el.getAttribute('data-ga-destination') || el.href || '';
    var postTitle = el.getAttribute('data-ga-post-title') || '';

    var params = {
      button_location: location,
      destination: destination,
      page_name: pageName
    };

    if (postTitle) params.post_title = postTitle;

    track(eventName, params);

    // Always fire a generic app_store_click for any App Store link
    if (
      destination.indexOf('apps.apple.com') !== -1 &&
      eventName !== 'app_store_click'
    ) {
      track('app_store_click', params);
    }
  });

  // Scroll 90% depth
  var scroll90Fired = false;
  window.addEventListener('scroll', function () {
    if (scroll90Fired) return;
    var scrollTop  = window.pageYOffset || document.documentElement.scrollTop;
    var docHeight  = document.documentElement.scrollHeight - document.documentElement.clientHeight;
    if (docHeight > 0 && scrollTop / docHeight >= 0.9) {
      scroll90Fired = true;
      track('scroll_90', {});
    }
  }, { passive: true });
})();
