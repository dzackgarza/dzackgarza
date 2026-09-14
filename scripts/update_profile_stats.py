#!/usr/bin/env python3
from __future__ import annotations

import html
import json
import subprocess
from collections import Counter
from pathlib import Path

LOGIN = "dzackgarza"
ROOT = Path(__file__).resolve().parents[1]
ASSETS = ROOT / "assets"


def gh_json(*args: str):
    return json.loads(subprocess.check_output(["gh", "api", *args], text=True))


def collect():
    user = gh_json(f"users/{LOGIN}")
    repos = []
    page = 1
    while True:
        batch = gh_json(f"users/{LOGIN}/repos?per_page=100&page={page}&sort=updated")
        if not batch:
            break
        repos.extend(batch)
        if len(batch) < 100:
            break
        page += 1

    originals = [repo for repo in repos if not repo["fork"]]
    stars = sum(repo["stargazers_count"] for repo in originals)
    sizes: Counter[str] = Counter()
    for repo in originals:
        languages = gh_json(f"repos/{LOGIN}/{repo['name']}/languages")
        for name, size in languages.items():
            sizes[name] += size
    return user["public_repos"], user["followers"], stars, sizes


def shell(width: int, height: int, body: str) -> str:
    return f'''<svg xmlns="http://www.w3.org/2000/svg" width="{width}" height="{height}" viewBox="0 0 {width} {height}" role="img">
<style>
.bg {{ fill:#fff; stroke:#d0d7de }}
.title,.value,.lang {{ fill:#24292f; font-family:-apple-system,BlinkMacSystemFont,"Segoe UI",sans-serif }}
.title {{ font-size:17px; font-weight:600 }}
.value {{ font-size:21px; font-weight:600 }}
.label {{ fill:#57606a; font:12px -apple-system,BlinkMacSystemFont,"Segoe UI",sans-serif }}
.lang {{ font-size:12px }}
@media (prefers-color-scheme:dark) {{
.bg {{ fill:#0d1117; stroke:#30363d }}
.title,.value,.lang {{ fill:#e6edf3 }}
.label {{ fill:#8b949e }}
}}
</style>
<rect class="bg" x="0.5" y="0.5" width="{width-1}" height="{height-1}" rx="6"/>
{body}
</svg>'''


def stats_svg(repos: int, followers: int, stars: int, languages: int) -> str:
    return shell(330, 170, f'''
<text class="title" x="18" y="28">GitHub</text>
<text class="value" x="18" y="67">{repos}</text><text class="label" x="18" y="87">public repositories</text>
<text class="value" x="164" y="67">{followers}</text><text class="label" x="164" y="87">followers</text>
<text class="value" x="18" y="126">{stars}</text><text class="label" x="18" y="146">stars on original repos</text>
<text class="value" x="164" y="126">{languages}</text><text class="label" x="164" y="146">languages</text>''')


def languages_svg(sizes: Counter[str]) -> str:
    top = sizes.most_common(6)
    total = sum(size for _, size in top) or 1
    parts = ['<text class="title" x="18" y="28">Top languages</text>']
    for i, (name, size) in enumerate(top):
        y = 53 + 21 * i
        pct = size / total
        parts.append(f'<text class="lang" x="18" y="{y}">{html.escape(name)}</text>')
        parts.append(f'<text class="label" x="310" y="{y}" text-anchor="end">{pct:.1%}</text>')
    return shell(330, 170, "\n".join(parts))


def main() -> None:
    repos, followers, stars, sizes = collect()
    ASSETS.mkdir(exist_ok=True)
    (ASSETS / "github-stats.svg").write_text(stats_svg(repos, followers, stars, len(sizes)))
    (ASSETS / "top-languages.svg").write_text(languages_svg(sizes))


if __name__ == "__main__":
    main()
