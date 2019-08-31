import os
import json
import subprocess

import fire


def generate(title, author, date, domain, checkpoint=None):
    params = {
        "url": "",
        "url_used": "",
        "title": f"{title}",
        "text": "",
        "summary": "",
        "authors": [f"{author}"],
        "publish_date": f"{date}",
        "domain": f"{domain}",
        "warc_date": "",
        "status": "",
        "split": "gen",
        "inst_index": 1,
    }

    if checkpoint == None:
        checkpoint = "models/base/model.ckpt"

    print("\nParameters:\n")
    print(f"Title: {title}")
    print(f"Author: {author}")
    print(f"Date: {date}")
    print(f"Domain: {domain}")
    print(f"Checkpoint: {checkpoint}")

    with open("params.jsonl", "w") as f:
        json.dump(params, f)

    subprocess.run(
        f"PYTHONPATH=$(pwd) python sample/contextual_generate.py -model_config_fn lm/configs/base.json -model_ckpt {checkpoint} -metadata_fn params.jsonl -out_fn generated.jsonl",
        stdout=open(os.devnull, "w"),
        stderr=subprocess.STDOUT,
        shell=True,
    )

    with open("generated.jsonl") as f:
        data = json.load(f)
        print("\nGenerated text:\n")
        print(data["gens_article"][0])

    os.system("rm params.jsonl")
    os.system("rm generated.jsonl")


if __name__ == "__main__":
    fire.Fire(generate)
