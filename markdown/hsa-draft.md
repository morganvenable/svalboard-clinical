---
title: HSA/FSA Reimbursement Draft
hero_title: Draft - Shopify Homepage Box + Nav Item
hero_subtitle: Preview of proposed additions to svalboard.com. Not a live page.
---

<div class="section" markdown="1">

## Proposed Nav Item

Add **"Clinical"** to the main navigation after "Reviews":

Buy | Keys | Layouts | Videos | Reviews | **Clinical** | FAQ | Support

Links to: `clinical.svalboard.com` (or the GitHub Pages URL until the subdomain is set up)

</div>

<div class="section mechanism" markdown="1">

## Proposed 7th Homepage Box

Below is a mockup of how the new box would appear alongside the existing six. The content renders inside Shopify's Dawn `multicolumn` section - you'd add it through the theme customizer, no code changes needed.

</div>

<div style="max-width:400px; margin:2rem auto; background:#fff; border-radius:12px; border:1px solid #e0e0e0; overflow:hidden;">

<div style="background:#121212; padding:3rem 2rem; text-align:center;">
<svg viewBox="0 0 200 120" xmlns="http://www.w3.org/2000/svg" style="max-width:200px;">
  <rect width="200" height="120" fill="#121212"/>
  <rect x="60" y="20" width="80" height="80" rx="40" fill="none" stroke="#fff" stroke-width="2"/>
  <text x="100" y="55" text-anchor="middle" fill="#fff" font-family="Inter, sans-serif" font-size="28" font-weight="700">HSA</text>
  <text x="100" y="75" text-anchor="middle" fill="#fff" font-family="Inter, sans-serif" font-size="12" font-weight="400">FSA ELIGIBLE</text>
</svg>
</div>

<div style="padding:1.5rem;">
<h3 style="font-family:Inter,sans-serif; font-size:1.15rem; font-weight:600; margin:0 0 0.75rem;">HSA & FSA Eligible</h3>
<p style="font-family:Inter,sans-serif; font-size:0.9rem; color:#333; line-height:1.6; margin:0 0 1rem;">
Many Svalboard purchases qualify for HSA/FSA reimbursement with a letter of medical necessity from your provider. We provide condition-specific clinical documentation covering carpal tunnel, cubital tunnel, EDS, muscular dystrophy, and more - ready for your provider to reference.
</p>
<a href="https://morganvenable.github.io/svalboard-clinical/" style="font-family:Inter,sans-serif; font-size:0.9rem; color:#121212; text-decoration:none; font-weight:500; display:inline-flex; align-items:center; gap:4px;">
View clinical resources & get started
<svg viewBox="0 0 14 10" fill="none" style="width:14px; height:10px;" xmlns="http://www.w3.org/2000/svg"><path fill-rule="evenodd" clip-rule="evenodd" d="M8.537.808a.5.5 0 01.817-.162l4 4a.5.5 0 010 .708l-4 4a.5.5 0 11-.708-.708L11.793 5.5H1a.5.5 0 010-1h10.793L8.646 1.354a.5.5 0 01-.109-.546z" fill="currentColor"/></svg>
</a>
</div>

</div>

<div class="section" markdown="1">

## Shopify Implementation Steps

### 1. Add nav item (no code needed)

Shopify Admin > Online Store > Navigation > Main menu > Add menu item:
- **Name:** Clinical
- **Link:** https://morganvenable.github.io/svalboard-clinical/
- **Position:** After "Reviews"

### 2. Add 7th multicolumn block (no code needed)

Shopify Admin > Online Store > Themes > Customize > Home page:
- Find the multicolumn section (the six boxes)
- Click "Add block"
- Set heading: `HSA & FSA Eligible`
- Set body text (paste from above)
- Set link text: `View clinical resources & get started`
- Set link URL: `https://morganvenable.github.io/svalboard-clinical/`
- Upload an image (black background with HSA/FSA graphic, or a product photo in clinical context)

### 3. Grid consideration

7 items in a 3-column grid = 3-3-1 layout. Options:
- **Add an 8th box** (e.g., "Open Source / QMK" or "Community") for a 3-3-2 layout
- **Switch to 4 columns** in section settings for a 4-3 layout
- **Leave as 3-3-1** - the single box on the last row will center and still look fine

### 4. Later: subdomain

Once `clinical.svalboard.com` is pointed via CNAME, update both the nav link and the box link URL.

</div>

<div class="section clinical" markdown="1">

## Copy Variants

If the main copy feels too long for the box, here are shorter options:

**Short version:**
> Your provider can write a letter of medical necessity for Svalboard. We provide the clinical documentation they need - covering CTS, cubital tunnel, EDS, muscular dystrophy, and more.

**Ultra-short version:**
> Get your Svalboard covered by HSA/FSA. We provide clinical documentation your provider can use for a letter of medical necessity.

</div>
