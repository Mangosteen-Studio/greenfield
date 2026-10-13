#!/usr/bin/env python3
"""Build standalone presenter and buyer demos. Python standard library only."""
import argparse
import base64
import copy
import json
import math
from pathlib import Path
from urllib.parse import urlparse


def require(condition, message):
    if not condition:
        raise ValueError(message)


def strings(obj, fields):
    require(isinstance(obj, dict), "Expected an object")
    for field in fields:
        require(isinstance(obj.get(field), str) and obj[field].strip(), f"Missing text: {field}")


def build(source, output, overwrite=False):
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
    scenes = data.get("scenes")
    require(isinstance(scenes, list) and 2 <= len(scenes) <= 20, "Use 2–20 scenes")
    scene_ids, public = set(), []
    fields = ["id", "chapter", "headline", "body", "visualLabel", "narration", "question"]
    for scene in scenes:
        strings(scene, fields + ["notes"])
        require(scene["id"] not in scene_ids, "Duplicate scene ID")
        scene_ids.add(scene["id"])
        seconds = scene.get("seconds")
        require(type(seconds) in (int, float) and math.isfinite(seconds) and 3 <= seconds <= 30, "Scene seconds must be 3–30")
        links = scene.get("evidenceIds")
        require(isinstance(links, list) and links and all(isinstance(x, str) and x in ids for x in links), "Unresolved or missing evidenceIds")
        cards = scene.get("cards")
        require(isinstance(cards, list) and 1 <= len(cards) <= 5, "Use 1–5 cards")
        for card in cards:
            strings(card, ["label", "value", "detail"])
        cleaned = {key: scene[key] for key in fields + ["seconds"]}
        cleaned["cards"] = [{key: card[key] for key in ["label", "value", "detail"]} for card in cards]
        if "choices" in scene:
            choices = scene["choices"]
            require(isinstance(choices, list) and 2 <= len(choices) <= 3, "Use 2–3 choices")
            for choice in choices:
                strings(choice, ["label", "result"])
            default = scene.get("defaultChoice", 0)
            require(type(default) is int and 0 <= default < len(choices), "Invalid defaultChoice")
            cleaned["choices"] = [{key: c[key] for key in ["label", "result"]} for c in choices]
            cleaned["defaultChoice"] = default
        if "imagePath" in scene:
            strings(scene, ["imagePath", "imageAlt"])
            path = (source.parent / scene["imagePath"]).resolve()
            mime = {".png": "image/png", ".jpg": "image/jpeg", ".jpeg": "image/jpeg", ".webp": "image/webp"}.get(path.suffix.lower())
            require(mime is not None and path.is_file(), "Image must be a local PNG/JPEG/WebP file")
            require(path.stat().st_size <= 10 * 1024 * 1024, "Image exceeds 10 MiB")
            cleaned["image"] = f"data:{mime};base64," + base64.b64encode(path.read_bytes()).decode("ascii")
            cleaned["imageAlt"] = scene["imageAlt"]
        public.append(cleaned)
    shared = {key: data[key] for key in ["title", "product", "scenarioLabel"]}
    shared["persona"] = {key: data["persona"][key] for key in ["name", "role"]}
    shared["scenes"] = public
    if "cta" in data:
        strings(data["cta"], ["label", "url"])
        url = urlparse(data["cta"]["url"])
        require(url.scheme == "https" and url.hostname and not url.username and not url.password, "CTA requires a public HTTPS URL without credentials")
        shared["cta"] = {key: data["cta"][key] for key in ["label", "url"]}
    template = (Path(__file__).resolve().parents[1] / "assets/player.html").read_text(encoding="utf-8")
    files = {}
    for name, presenter in [("present.html", True), ("send.html", False)]:
        payload = copy.deepcopy(shared)
        payload["presenter"] = presenter
        if presenter:
            for i, scene in enumerate(payload["scenes"]):
                scene["notes"] = scenes[i]["notes"]
        encoded = json.dumps(payload, ensure_ascii=False).replace("<", "\\u003c").replace("&", "\\u0026")
        files[name] = template.replace("__DEMO_DATA__", encoded)
    files["storyboard.json"] = json.dumps(data, indent=2, ensure_ascii=False) + "\n"
    files["narration.txt"] = "\n\n".join(f"{s['chapter']}\n{s['narration']}" for s in scenes) + "\n"
    require(not output.exists() or overwrite, "Output exists; choose a new directory or use --overwrite")
    output.mkdir(parents=True, exist_ok=True)
    for name, content in files.items():
        (output / name).write_text(content, encoding="utf-8")
    print(f"Built {len(scenes)} scenes: {output / 'present.html'} and {output / 'send.html'}")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--input", type=Path, required=True)
    parser.add_argument("--output", type=Path, required=True)
    parser.add_argument("--overwrite", action="store_true")
    args = parser.parse_args()
    try:
        build(args.input.resolve(), args.output.resolve(), args.overwrite)
    except (ValueError, OSError, TypeError) as error:
        parser.exit(1, f"Cannot build demo: {error}\n")
