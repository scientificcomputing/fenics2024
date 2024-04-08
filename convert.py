import argparse
from textwrap import dedent, indent
from typing import Sequence, NamedTuple
from pathlib import Path
import csv

TEMPLATE = dedent(
    """\
---
title: '{title}'
{authors}
license: CC-BY-4.0
exports:
  - format: pdf
    template: ../../template

---

{text}
{references}

"""
)

author_template = dedent(
    """\
- name: {name}
  affiliations:
    - {affiliation}
  email: {email}"""
)


class Author(NamedTuple):
    name: str
    affiliation: str
    email: str = ""

    def to_str(self):
        return author_template.format(
            name=self.name,
            affiliation=self.affiliation,
            email=self.email,
        )


def read_paper(row: dict[str, str]) -> str:
    authors = []
    for i, (author_name, affiliation) in enumerate(
        zip(
            row["Name of authors (including presenter, comma-separated list)"].split(","),
            row["Affiliation of co-authors (including presenter, comma-separated list)"].split(","),
        )
    ):
        email = row["Username"] if i == 0 else ""

        authors.append(
            Author(
                name=author_name.strip(),
                affiliation=affiliation.strip(),
                email=email,
            )
        )
    authors = "authors:\n" + indent("\n".join([a.to_str() for a in authors]), "  ")

    references = "\n\n".join(row["Reference list"].strip().split("\n"))
    if len(references) > 0:
        references = f"\n# References\n{references}\n"
    return TEMPLATE.format(
        title=row["Abstract title"],
        authors=authors,
        text=row["Abstract text"],
        references=references,
    )


def main(argv: Sequence[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="")
    parser.add_argument("path", type=Path)
    parser.add_argument("-o", "--output", type=Path, default=None)
    args = vars(parser.parse_args(argv))

    outdir = args["output"] or Path("book") / "abstracts"
    outdir.mkdir(parents=True, exist_ok=True)

    # count the words
    if not args["path"].is_file():
        print(f"{args['path']} is not a file")
        return 1

    with open(args["path"], "r") as f:
        reader = csv.DictReader(f)
        for row in reader:
            slug = row["Abstract title"].replace(" ", "-").lower()
            output = read_paper(row)
            (outdir / f"{slug}.md").write_text(output)

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
