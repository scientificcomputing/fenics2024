from typing import NamedTuple
from enum import IntEnum, auto
from textwrap import dedent
import pandas as pd
import datetime
from pathlib import Path

TALK_DURATION_MIN = 15
TALK_DURATION_SEC = TALK_DURATION_MIN * 60


class Day(IntEnum):
    WEDNESDAY = auto()
    THURSDAY = auto()
    FRIDAY = auto()


template = dedent(
    """---
title: 'FEniCS conferences 2024'
authors:
  - name: Jørgen Dokken
    affiliations:
      - Simula Research Laboratory
    email: dokken@simula.no
  - name: Henrik Finsberg
    affiliations:
      -  Simula Research Laboratory
    email: henriknd@simula.no
  - name: Marie Rognes
    affiliations:
      -  Simula Research Laboratory
    email: meg@simula.no
license: CC-BY-4.0
exports:
  - format: pdf
    template: ../template
---

Here you will find the abstracts for the FEniCS 2024 conference in Oslo

# Presentations
{tables}

# Posters
{posters}
"""
)

table_template = dedent(
    """\
## {time_slot}
{table}
"""
)


class TimeSlot(NamedTuple):
    start: datetime.datetime
    end: datetime.datetime
    day: str

    def num_presentations(self):
        duration = self.end - self.start
        return int(duration.total_seconds() / TALK_DURATION_SEC)

    def __str__(self):
        start_minute = str(self.start.minute).zfill(2)
        end_minute = str(self.end.minute).zfill(2)
        num_presentations = f"Number of presentations: {self.num_presentations()}"
        return f"{self.day}: {self.start.hour}:{start_minute} - {self.end.hour}:{end_minute}\n{num_presentations}"


def day_session_to_time(day: Day, session: int):
    if day == Day.WEDNESDAY:
        if session == 1:
            return TimeSlot(
                start=datetime.datetime(2024, 6, 12, 13, 30),
                end=datetime.datetime(2024, 6, 12, 14, 30),
                day="Wednesday",
            )
        elif session == 2:
            return TimeSlot(
                start=datetime.datetime(2024, 6, 12, 14, 35),
                end=datetime.datetime(2024, 6, 12, 15, 35),
                day="Wednesday",
            )
        elif session == 3:
            return TimeSlot(
                start=datetime.datetime(2024, 6, 12, 15, 45),
                end=datetime.datetime(2024, 6, 12, 17, 00),
                day="Wednesday",
            )

    elif day == Day.THURSDAY:
        if session == 1:
            return TimeSlot(
                start=datetime.datetime(2024, 6, 13, 9, 0),
                end=datetime.datetime(2024, 6, 13, 10, 0),
                day="Thursday",
            )
        elif session == 2:
            return TimeSlot(
                start=datetime.datetime(2024, 6, 13, 10, 10),
                end=datetime.datetime(2024, 6, 13, 11, 10),
                day="Thursday",
            )
        elif session == 3:
            return TimeSlot(
                start=datetime.datetime(2024, 6, 13, 11, 15),
                end=datetime.datetime(2024, 6, 13, 12, 15),
                day="Thursday",
            )
        elif session == 4:
            return TimeSlot(
                start=datetime.datetime(2024, 6, 13, 13, 00),
                end=datetime.datetime(2024, 6, 13, 14, 15),
                day="Thursday",
            )
        elif session == 5:
            return TimeSlot(
                start=datetime.datetime(2024, 6, 13, 14, 25),
                end=datetime.datetime(2024, 6, 13, 15, 25),
                day="Thursday",
            )
        elif session == 6:
            return TimeSlot(
                start=datetime.datetime(2024, 6, 13, 15, 45),
                end=datetime.datetime(2024, 6, 13, 17, 00),
                day="Thursday",
            )

    elif day == Day.FRIDAY:
        if session == 1:
            return TimeSlot(
                start=datetime.datetime(2024, 6, 14, 9, 0),
                end=datetime.datetime(2024, 6, 14, 10, 15),
                day="Friday",
            )
        elif session == 2:
            return TimeSlot(
                start=datetime.datetime(2024, 6, 14, 10, 30),
                end=datetime.datetime(2024, 6, 14, 11, 30),
                day="Friday",
            )

    raise ValueError(f"Unknown day {day} and session {session}")


def main():
    df = pd.read_csv("Timetable FEniCS 2024 - Copy of Form responses 1.csv")
    df["Day_enumerated"] = df["Day"].map(
        {
            "Wednesday": Day.WEDNESDAY,
            "Thursday": Day.THURSDAY,
            "Friday": Day.FRIDAY,
        }
    )
    df_presentation = df[df["Is the submission relating to a poster or presentation?"] == "Presentation"]
    df_poster = df[df["Is the submission relating to a poster or presentation?"] == "Poster"]
    # breakpoint()
    # Group by day and session
    grouped = df_presentation.groupby(
        ["Day_enumerated", "Session"],
        sort=True,
    )

    # breakpoint()

    # Create a table for each group
    tables = []
    for (day, session), group in grouped:
        print(day, session)
        data = []
        time_slot = day_session_to_time(day, int(session))

        for _, item in group.iterrows():
            title = f'[{item["Abstract title"]}](abstracts/{item["Filename"]}.md)'
            presenter = item["Name of presenter"]
            # phd = item["Are you a PhD candidate or a Postdoctoral researcher?"]
            # breakpoint()
            data.append({"Title": title, "Presenter": presenter})

        df_table = pd.DataFrame(data)
        table = df_table.to_markdown(index=False)
        # print(table)
        tables.append(table_template.format(time_slot=time_slot, table=table))

    data = []
    for _, item in df_poster.iterrows():
        title = f'[{item["Abstract title"]}](abstracts/{item["Filename"]}.md)'
        presenter = item["Name of presenter"]
        data.append({"Title": title, "Presenter": presenter})

    df_posters_md = pd.DataFrame(data)
    posters_md = df_posters_md.to_markdown(index=False)

    (Path("book") / "README.md").write_text(template.format(tables="\n\n".join(tables), posters=posters_md))


if __name__ == "__main__":
    main()
