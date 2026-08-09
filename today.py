import os

# Data Kustom AZWALUWU
DATA = {
    "name": "AZWALUWU",
    "title": "DevOps & Infrastructure Enthusiast",
    "website": "azwaluwu.github.io",
    "website_url": "https://azwaluwu.github.io",
    "linkedin": "Azwa Luwu",
    "linkedin_url": "https://www.linkedin.com/in/azwa-luwu-4849033a3/",
    # Tech Stack: (Teks Lencana, Lebar Lencana dalam Pixel)
    "stack": [
        ("Linux", 60), ("Bash", 56), ("Python", 68), ("Nginx", 60),
        ("AWS", 60), ("Terraform", 82), ("Docker", 68),
        ("GitHub Actions", 118), ("Prometheus", 92), ("Grafana", 70)
    ]
}

# Konfigurasi Tema
THEMES = {
    "dark": {
        "bg": "#0D1117", "stroke": "#30363D",
        "title": "#58A6FF", "subtitle": "#8B949E", "section": "#C9D1D9",
        "link_lbl": "#58A6FF", "link_val": "#C9D1D9",
        "badge_bg": "#161B22", "badge_stroke": "#30363D", "badge_txt": "#E6EDF3",
        "line": "#21262D"
    },
    "light": {
        "bg": "#FFFFFF", "stroke": "#D0D7DE",
        "title": "#0969DA", "subtitle": "#57606A", "section": "#24292F",
        "link_lbl": "#0969DA", "link_val": "#24292F",
        "badge_bg": "#F6F8FA", "badge_stroke": "#D0D7DE", "badge_txt": "#24292F",
        "line": "#D0D7DE"
    }
}

def generate_svg(theme_name, filename):
    t = THEMES[theme_name]
    
    # Generate Stack Badges
    stack_html = ""
    current_x = 0
    current_y = 0
    max_width = 460
    gap = 8
    line_height = 34
    
    for text, width in DATA["stack"]:
        if current_x + width > max_width:
            current_x = 0
            current_y += line_height
            
        stack_html += f'<g transform="translate({current_x}, {current_y})">'
        stack_html += f'<rect x="0" y="0" width="{width}" height="26" rx="6" fill="{t["badge_bg"]}" stroke="{t["badge_stroke"]}" stroke-width="1"/>'
        stack_html += f'<text x="{width/2}" y="17" text-anchor="middle" font-family="Segoe UI, Ubuntu, Sans-Serif" font-size="12" font-weight="500" fill="{t["badge_txt"]}">{text}</text>'
        stack_html += '</g>\n'
        
        current_x += width + gap

    final_height = 240 + current_y + 30

    svg_content = f"""<svg width="520" height="{final_height}" viewBox="0 0 520 {final_height}" fill="none" xmlns="http://www.w3.org/2000/svg">
  <style>
    .title {{ font: 700 22px 'Segoe UI', Ubuntu, Sans-Serif; fill: {t["title"]}; }}
    .subtitle {{ font: 400 14px 'Segoe UI', Ubuntu, Sans-Serif; fill: {t["subtitle"]}; }}
    .section-title {{ font: 600 15px 'Segoe UI', Ubuntu, Sans-Serif; fill: {t["section"]}; }}
    .link-label {{ font: 600 13px 'Segoe UI', Ubuntu, Sans-Serif; fill: {t["link_lbl"]}; }}
    .link-val {{ font: 400 13px 'Segoe UI', Ubuntu, Sans-Serif; fill: {t["link_val"]}; }}
  </style>

  <rect width="519" height="{final_height-1}" rx="10" fill="{t["bg"]}" stroke="{t["stroke"]}" stroke-width="1"/>

  <text x="30" y="45" class="title">{DATA["name"]}</text>
  <text x="30" y="68" class="subtitle">{DATA["title"]}</text>

  <line x1="30" y1="85" x2="490" y2="85" stroke="{t["line"]}" stroke-width="1"/>

  <text x="30" y="112" class="section-title">🔗 Connect &amp; Links</text>
  
  <g transform="translate(30, 125)">
    <text x="0" y="15" class="link-label">Website:</text>
    <a href="{DATA["website_url"]}" target="_blank">
      <text x="80" y="15" class="link-val">{DATA["website"]}</text>
    </a>

    <text x="0" y="38" class="link-label">LinkedIn:</text>
    <a href="{DATA["linkedin_url"]}" target="_blank">
      <text x="80" y="38" class="link-val">{DATA["linkedin"]}</text>
    </a>
  </g>

  <line x1="30" y1="190" x2="490" y2="190" stroke="{t["line"]}" stroke-width="1"/>

  <text x="30" y="217" class="section-title">🛠️ Tech Stack &amp; Tools</text>

  <g transform="translate(30, 232)">
    {stack_html}
  </g>
</svg>
"""
    with open(filename, "w", encoding="utf-8") as f:
        f.write(svg_content)

if __name__ == "__main__":
    generate_svg("dark", "dark_mode.svg")
    generate_svg("light", "light_mode.svg")
