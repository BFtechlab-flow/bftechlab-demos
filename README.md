# BF Tech Lab — website demos

Demo websites for prospective clients. The businesses, people, prices and reviews are fictional; photos are stock images from Unsplash.

| Demo | Industry | Path |
| --- | --- | --- |
| BF Dental | Dental practice | `dental/` |
| BF Animal Hospital | Veterinary clinic | `veterinary/` |
| BF Chiropractic | Chiropractic clinic | `chiropractic/` |
| BF Med Spa | Med spa | `med-spa/` |
| BF Plumbing | Plumber | `plumbing/` |
| BF Roofing | Roofing contractor | `roofing/` |
| BF Landscapes | Landscaping | `landscaping/` |
| BF Trattoria | Restaurant | `restaurant/` |
| BF Law Group | Law firm | `law/` |
| BF Realty | Real estate agency | `real-estate/` |
| BF Motors | Used car dealer | `dealer/` |
| BF Auto Care | Auto repair shop | `auto-repair/` |
| BF Salon | Hair salon | `salon/` |
| BF Fitness | Gym & fitness studio | `fitness/` |

Each demo is a single HTML file (Tailwind CDN + GSAP, no build step), published with GitHub Pages from the `main` branch.
The newer demos are generated from `tools/gen` (`python3 tools/gen/build.py`, then `python3 tools/gen/index_page.py`).
