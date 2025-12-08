# Developer Handover Guide

## Tech Stack Recommendation
*   **Framework:** Vanilla HTML/CSS/JS (as requested) or Next.js/Tailwind for scalability.
*   **Styling:** TailwindCSS (v3.4) via CDN for the HTML template, or dedicated CSS file.
*   **Iconography:** Lucide Icons or Heroicons (SVG).

## Performance Optimization
1.  **Images:**
    *   Convert all assets to WebP.
    *   Attributes: `loading="lazy"` on below-fold images. `width` and `height` specified preventing layout shift.
    *   Hero image: `loading="eager"`, compress to <150KB.
2.  **CSS:**
    *   Critical CSS inline in `<head>`.
    *   Defer non-critical styles.
3.  **JS:**
    *   Defer all scripts (`defer` attribute).

## Analytics (GA4) setup
Insert this snippet in `<head>`:

```html
<!-- Google Tag Manager / GA4 -->
<script async src="https://www.googletagmanager.com/gtag/js?id=G-XXXXXXXXXX"></script>
<script>
  window.dataLayer = window.dataLayer || [];
  function gtag(){dataLayer.push(arguments);}
  gtag('js', new Date());

  gtag('config', 'G-XXXXXXXXXX');
</script>
```

## Accessibility Checklist
*   [ ] All `<img>` tags have `alt`.
*   [ ] ARIA labels on Icon-only buttons.
*   [ ] Semantic HTML (`<main>`, `<nav>`, `<section>`, `<footer>`).
*   [ ] Keyboard navigable (Tab index).
*   [ ] Color contrast verification.

## Deployment
*   **Netlify/Vercel:** Drag and drop the folder.
*   **Domain:** Map `honconstruction.com` via A record.
*   **Forms:** Use Netlify Forms `data-netlify="true"` or Formspree for the Contact form backend without server code.
