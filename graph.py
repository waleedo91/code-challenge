from flask import Flask, render_template
import csv
from collections import Counter

app = Flask(__name__)

@app.route('/')
def home():
    with open('searchLogs.csv') as csv_file:
        csv_reader = csv.DictReader(csv_file)

        search_counter = Counter()

        for row in csv_reader:
            search_counter.update(row['query'].split(';'))
    # print(search_counter.items())

    query = []
    searched = []

    for item in search_counter.items():
        query.append(item[0])
        searched.append(item[1])
    print(query)
    print(searched)

    return render_template('graph.html', labels=query, values=searched)

if __name__ == '__main__':
    app.run()