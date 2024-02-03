from typing import Dict
from io import StringIO
import pandas as pd
import csv


def parse_statement(text: str) -> Dict:
    """
    Grab the html text response from the web page response.

    Convert the html text to dataframe table and into a json.

    @param text: The HTML text from an HTTP requests get.
    @return: json data from the html text website.
    """

    # Grab the html tables and remove uncessary values.
    tables = pd.read_html(text)
    df = tables[1].dropna(axis=1)

    # Get the date values.
    report = df.iloc[[0]]                           # Dates is always the first row.
    dates = report.drop("Period Ending:", axis=1)   # Remove name row.
    dates = list(dates.values[0])

    # Get the period names.
    period = df["Period Ending:"]
    names = period.drop(0)              # Remove the report filing row.
    labels = names.values

    # Combine the two dataframe into a single dictionary.
    statement = {}
    for label in labels:
        row = df.loc[df.iloc[:, 0] == label]
        values = row.drop("Period Ending:", axis=1).values[0].astype(float)
        pairs = dict(zip(dates, values))
        try:
            # This is for the quarterly.
            del pairs[1234]
        except KeyError:
            # If it is an annually then just continue.
            pass
        statement[label] = pairs

    return statement


def parse_quota(text: str) -> Dict:
    """
    Grab the csv text response from the web page that was download from weblink.

    Read a csv file and into a json file.

    @param text: The HTML text from an HTTP requests get.
    @return: Raw data from the csv text website.
    """

    # Read the response text and convert into a list.
    file_prices = StringIO(text)
    reader = csv.reader(file_prices)
    data = list(reader)
    names = data.pop(0)

    # Create a dataframe for fast selecting.
    df = pd.DataFrame(data, columns=names)

    # Change some of the columns type to numeric.
    for name in names[1:]:                          # Exclude the Date
        try:
            df[name] = pd.to_numeric(df[name])
        except ValueError:
            df[name] = df[name]

    # Convert it into a json.
    data_json = {name : df[name].to_list() for name in names}

    return data_json
