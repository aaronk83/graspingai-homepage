// Small JS to enhance form UX; page still works without JS

document.addEventListener('DOMContentLoaded', () => {
  const y = document.getElementById('year');
  if (y) y.textContent = new Date().getFullYear();
});

const form = document.getElementById('contactForm');
if (form) {
  form.addEventListener('submit', async (e) => {
    e.preventDefault();
    const success = form.querySelector('.form-success');
    const error = form.querySelector('.form-error');

    // Honeypot
    const hp = form.querySelector('input[name="company"]').value.trim();
    if (hp) return;

    const data = new FormData(form);
    try {
      const resp = await fetch(form.action, { method: 'POST', body: data, headers: { 'Accept': 'application/json' } });
      if (resp.ok) {
        if (success) success.hidden = false;
        if (error) error.hidden = true;
        form.reset();
      } else {
        if (success) success.hidden = true;
        if (error) error.hidden = false;
      }
    } catch {
      if (success) success.hidden = true;
      if (error) error.hidden = false;
    }
  });
}

// Services accordions: desktop open by default, mobile collapsed
document.addEventListener('DOMContentLoaded', function () {
  const accordions = document.querySelectorAll('#services details.service-card');
  if (!accordions.length) return;

  const isMobile = window.matchMedia('(max-width: 900px)').matches;

  accordions.forEach((details) => {
    if (isMobile) {
      details.removeAttribute('open'); // collapsed by default on mobile
    } else {
      details.setAttribute('open', 'open'); // expanded by default on desktop
    }
  });
});
