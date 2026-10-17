#!/usr/bin/env python3
"""Build independent, offline interview presenter and panel HTML from plain-text JSON."""
import argparse
import html
import json
from pathlib import Path


def esc(value):
    return html.escape(value, quote=True)


def require_text(value, label):
    if not isinstance(value, str) or not value.strip():
        raise ValueError(f'{label} must be nonempty text')
    return value


def validate(data):
    if not isinstance(data, dict):
        raise ValueError('plan must be an object')
    for key in ('title', 'candidate', 'company'):
        require_text(data.get(key), key)
    sections = data.get('sections')
    if not isinstance(sections, list) or not sections:
        raise ValueError('sections must be a nonempty list')
    for i, section in enumerate(sections):
        if not isinstance(section, dict):
            raise ValueError(f'section {i} must be an object')
        for key in ('title', 'body'):
            require_text(section.get(key), f'section {i} {key}')
        for key in ('evidence', 'notes'):
            if key in section and not isinstance(section[key], str):
                raise ValueError(f'section {i} {key} must be text')
    if 'privateNotes' in data and not isinstance(data['privateNotes'], str):
        raise ValueError('privateNotes must be text')


def panel_data(data):
    # An independent allowlist: never serialize the input into the shareable file.
    return {**{k: data[k] for k in ('title', 'candidate', 'company')},
            'sections': [{k: s[k] for k in ('title', 'body', 'evidence') if k in s}
                         for s in data['sections']]}


STYLE = '''
:root{font-family:system-ui,sans-serif;color:#142c29;background:#f3f5ef;line-height:1.6}
*{box-sizing:border-box}body{margin:0}header,main,footer{max-width:1050px;margin:auto;padding:24px}
h1{font-size:clamp(2rem,5vw,3.5rem);line-height:1.12;max-width:900px}h2{line-height:1.25}
nav{display:flex;flex-wrap:wrap;gap:12px}a{color:#145d4c;text-underline-offset:4px}
nav a,.step a{display:inline-block;padding:10px 14px;border:1px solid #65796d;border-radius:8px}
section{background:white;border:1px solid #c3cec3;border-radius:12px;padding:28px;margin:24px 0;scroll-margin-top:16px}
p{white-space:pre-wrap;overflow-wrap:anywhere}details{border-top:1px solid #c3cec3;margin-top:20px;padding-top:14px}
summary{cursor:pointer;padding:8px 0}.evidence{font-size:.94rem;color:#3b554f}.step{display:flex;justify-content:space-between;gap:12px;flex-wrap:wrap;margin-top:20px}
.badge{font-weight:650}a:focus-visible,summary:focus-visible{outline:3px solid #a34a00;outline-offset:4px}
@media(max-width:600px){header,main,footer{padding:16px}section{padding:20px}}
@media print{nav,.step{display:none}section{break-inside:avoid}}
'''


def render(data, presenter=False):
    # Both modes escape every field. No scripts, network requests, remote fonts or embedded JSON.
    plan = data if presenter else panel_data(data)
    nav = ''.join(f'<a href="#section-{i}">{esc(s["title"])}</a>'
                  for i, s in enumerate(plan['sections'], 1))
    sections = []
    for i, s in enumerate(plan['sections'], 1):
        evidence = f'<p class="evidence">{esc(s["evidence"])}</p>' if s.get('evidence') else ''
        notes = f'<details><summary>Private speaker notes</summary><p>{esc(s["notes"])}</p></details>' if presenter and s.get('notes') else ''
        prev = f'<a href="#section-{i-1}">Previous</a>' if i > 1 else '<a href="#top">Overview</a>'
        nxt = f'<a href="#section-{i+1}">Next</a>' if i < len(plan['sections']) else '<a href="#top">Back to overview</a>'
        sections.append(f'<section id="section-{i}" aria-labelledby="heading-{i}"><h2 id="heading-{i}">{esc(s["title"])}</h2><p>{esc(s["body"])}</p>{evidence}{notes}<div class="step">{prev}{nxt}</div></section>')
    private = f'<details><summary>Private interview preparation</summary><p>{esc(data["privateNotes"])}</p></details>' if presenter and data.get('privateNotes') else ''
    mode = 'Private presenter copy — do not distribute' if presenter else 'Panel leave-behind'
    return f'''<!doctype html>
<html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><meta name="robots" content="noindex,nofollow"><title>{esc(plan['title'])}</title><style>{STYLE}</style></head>
<body><header id="top"><p class="badge">{mode}</p><h1>{esc(plan['title'])}</h1><p>{esc(plan['candidate'])} · Interview project for {esc(plan['company'])}</p><p>Candidate-created interview exercise. Not an official company publication.</p><nav aria-label="Account plan sections">{nav}</nav>{private}</header><main>{''.join(sections)}</main><footer>Evidence and hypotheses are identified within the plan. Prepared for interview discussion.</footer></body></html>'''


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('plan', type=Path)
    parser.add_argument('--out', type=Path, required=True)
    args = parser.parse_args()
    data = json.loads(args.plan.read_text())
    validate(data)
    args.out.mkdir(parents=True, exist_ok=True)
    for name, presenter in [('present.html', True), ('send.html', False)]:
        (args.out / name).write_text(render(data, presenter), encoding='utf-8')
    print(f'Built present.html and send.html in {args.out}; review before sharing.')


if __name__ == '__main__':
    main()
