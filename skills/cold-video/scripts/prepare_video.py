#!/usr/bin/env python3
"""Prepare a Cold Video production package. Makes no API calls and spends no credits."""
import argparse
import html
import json
import math
import re
import textwrap
from pathlib import Path


def require(value, message):
    if not value:
        raise ValueError(message)


def strings(obj, fields):
    require(isinstance(obj, dict), "Expected an object")
    for field in fields:
        require(isinstance(obj.get(field), str) and obj[field].strip(), f"Missing text: {field}")


def timestamp(seconds):
    millis = round(seconds * 1000)
    hours, millis = divmod(millis, 3600000)
    minutes, millis = divmod(millis, 60000)
    seconds, millis = divmod(millis, 1000)
    return f"{hours:02}:{minutes:02}:{seconds:02}.{millis:03}"


def prepare(source, output, overwrite=False):
    data = json.loads(source.read_text(encoding="utf-8"))
    strings(data, ["title", "product", "scenarioLabel"])
    strings(data.get("persona"), ["name", "role"])
    evidence = data.get("evidence")
    require(isinstance(evidence, list) and evidence, "Evidence must be a nonempty list")
    ids = set()
    for item in evidence:
        strings(item, ["id", "claim", "source", "status"])
        require(item["id"] not in ids, "Duplicate evidence ID")
        require(item["status"] in {"documented", "user-confirmed", "illustrative"}, "Invalid evidence status")
        ids.add(item["id"])
    shots = data.get("shots")
    require(isinstance(shots, list) and 2 <= len(shots) <= 20, "Use 2–20 shots")
    shot_ids, total, words, generated = set(), 0.0, 0, []
    planned, assets = [], {}
    for shot in shots:
        strings(shot, ["id", "headline", "narration", "visual", "mediaType"])
        require(shot["id"] not in shot_ids, "Duplicate shot ID")
        shot_ids.add(shot["id"])
        seconds = shot.get("seconds")
        require(type(seconds) in (int, float) and math.isfinite(seconds) and 2 <= seconds <= 20, "Shot seconds must be 2–20")
        require(shot["mediaType"] in {"product-capture", "diagram", "generated-scene", "title"}, "Invalid mediaType")
        links = shot.get("evidenceIds")
        require(isinstance(links, list) and links and all(isinstance(x, str) and x in ids for x in links), "Unresolved or missing evidenceIds")
        count = len(re.findall(r"\S+", shot["narration"]))
        require(count / seconds * 60 <= 190, f"Narration too fast in shot {shot['id']}")
        words += count
        item = {k: shot[k] for k in ["id", "headline", "narration", "visual", "mediaType", "evidenceIds", "seconds"]}
        item.update(start=round(total, 3), end=round(total + seconds, 3))
        if "assetPath" in shot:
            strings(shot, ["assetPath"])
            asset = (source.parent / shot["assetPath"]).resolve()
            require(asset.is_file() and asset.suffix.lower() in {".png", ".jpg", ".jpeg", ".webp", ".mp4", ".mov", ".webm"}, "Invalid assetPath")
            asset_name = f"assets/shot-{len(planned)+1}{asset.suffix.lower()}"
            assets[asset_name] = asset
            item["assetPath"] = asset_name
        if shot["mediaType"] == "generated-scene":
            strings(shot, ["generationPrompt"])
            item["generationPrompt"] = shot["generationPrompt"]
            generated.append({"shotId": shot["id"], "prompt": shot["generationPrompt"], "seconds": seconds, "variants": 1, "referenceAssets": [], "aspectRatio": "16:9"})
        total += seconds
        planned.append(item)
    require(words / total * 60 <= 190, "Narration exceeds 190 words/minute")
    spec = {k: data[k] for k in ["title", "product", "persona", "scenarioLabel", "evidence"]}
    spec.update(status="production-package-only", duration=round(total, 3), fps=30, width=1920, height=1080, shots=planned, captionsStatus="estimated; retime against final audio")
    plan = {"status": "not-submitted", "provider": None, "modelOrEndpoint": None, "accessRoute": None, "pricingSource": None, "pricingCheckedAt": None, "currency": None, "unitPrice": None, "billingUnits": None, "estimatedFirstPassCost": None, "maximumAuthorizedSpend": None, "regenerationAllowance": 0, "authorizationReference": None, "shots": generated, "note": "Complete with current pricing and actual user authorization before paid generation. No calls have been made."}
    escape = html.escape
    sections = []
    for shot in planned:
        prompt = f'<details><summary>Generation direction</summary><p>{escape(shot["generationPrompt"])}</p></details>' if "generationPrompt" in shot else ""
        sections.append(f'<article><div class="meta">{shot["start"]:g}–{shot["end"]:g}s · {escape(shot["mediaType"])}</div><h2>{escape(shot["headline"])}</h2><div class="visual">{escape(shot["visual"])}</div><p class="label">Narration</p><p>{escape(shot["narration"])}</p>{prompt}</article>')
    document = f'''<!doctype html><html lang="en"><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>{escape(data['title'])}</title><style>*{{box-sizing:border-box}}body{{margin:0;background:#f5f3ed;color:#182e29;font:16px/1.6 -apple-system,BlinkMacSystemFont,"Segoe UI",sans-serif}}main{{max-width:1000px;margin:auto;padding:50px 24px}}.brand,.label,.meta{{font-size:12px;text-transform:uppercase;letter-spacing:1.5px}}h1{{font:52px/1.1 Georgia,serif;letter-spacing:-1.5px;max-width:750px}}h2{{font:29px/1.2 Georgia,serif}}.notice{{background:#dbf090;padding:18px 22px;border-radius:10px}}.grid{{display:grid;grid-template-columns:1fr 1fr;gap:20px;margin-top:28px}}article{{background:#fff;border:1px solid #d4dbd2;padding:25px;border-radius:12px}}.meta{{color:#5c6d66}}.visual{{background:#182e29;color:#f5f3ed;padding:24px;border-radius:9px;min-height:130px}}details{{font-size:13px;color:#5c6d66}}summary{{cursor:pointer;padding:12px 0}}a{{color:#182e29}}footer{{margin-top:30px;font-size:13px}}@media(max-width:650px){{.grid{{grid-template-columns:1fr}}h1{{font-size:38px}}}}</style><main><div class="brand">Cold Video / production storyboard</div><h1>{escape(data['title'])}</h1><p>{escape(data['scenarioLabel'])}</p><div class="notice"><strong>{total:g} seconds · {len(shots)} shots · {len(generated)} generated scenes planned</strong><br>Production package only. Paid provider access, pricing and spending approval are pending. No video has been generated.</div><div class="grid">{''.join(sections)}</div><footer>Editable inputs: <a href="render-spec.json">render specification</a> · <a href="provider-plan.json">provider plan</a> · <a href="narration.txt">narration</a> · <a href="captions-draft.vtt">estimated captions</a></footer></main></html>'''
    captions = ["WEBVTT", "", "NOTE Estimated scene cues. Retime against final audio before delivery.", ""]
    for shot in planned:
        # Long scene narration is divided into readable estimated cues; these are not forced alignments.
        chunks = textwrap.wrap(shot["narration"], width=78)
        for i, chunk in enumerate(chunks):
            start = shot["start"] + shot["seconds"] * i / len(chunks)
            end = shot["start"] + shot["seconds"] * (i+1) / len(chunks)
            captions.extend([f"{timestamp(start)} --> {timestamp(end)}", escape("\n".join(textwrap.wrap(chunk, width=42))), ""])
    title_lines = textwrap.wrap(data["title"], width=31)[:4]
    title_svg = "".join(f'<text x="90" y="{260+i*67}" fill="#f5f3ed" font-family="Georgia,serif" font-size="54">{escape(line)}</text>' for i, line in enumerate(title_lines))
    poster = f'<svg xmlns="http://www.w3.org/2000/svg" width="1280" height="720" viewBox="0 0 1280 720" role="img" aria-label="Cold Video draft poster"><rect width="1280" height="720" fill="#182e29"/><rect x="90" y="90" width="160" height="6" fill="#dbf090"/><text x="90" y="155" fill="#dbf090" font-family="sans-serif" font-size="20">COLD VIDEO · STORYBOARD</text>{title_svg}<text x="90" y="640" fill="#f5f3ed" font-family="sans-serif" font-size="20">Illustrative concept · video generation pending</text></svg>'
    files = {"storyboard.html": document, "render-spec.json": json.dumps(spec, indent=2, ensure_ascii=False)+"\n", "provider-plan.json": json.dumps(plan, indent=2, ensure_ascii=False)+"\n", "narration.txt": "\n\n".join(f"{s['start']:g}–{s['end']:g}s\n{s['narration']}" for s in planned)+"\n", "captions-draft.vtt": "\n".join(captions), "poster.svg": poster}
    require(not output.exists() or overwrite, "Output exists; choose a new directory or use --overwrite")
    output.mkdir(parents=True, exist_ok=True)
    for name, path in assets.items():
        destination = output / name
        destination.parent.mkdir(exist_ok=True)
        destination.write_bytes(path.read_bytes())
    for name, content in files.items():
        (output / name).write_text(content, encoding="utf-8")
    print(f"Prepared {total:g}s storyboard: {output / 'storyboard.html'} (no paid calls; no MP4)")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--input", type=Path, required=True)
    parser.add_argument("--output", type=Path, required=True)
    parser.add_argument("--overwrite", action="store_true")
    args = parser.parse_args()
    try:
        prepare(args.input.resolve(), args.output.resolve(), args.overwrite)
    except (ValueError, OSError, TypeError) as error:
        parser.exit(1, f"Cannot prepare video: {error}\n")
