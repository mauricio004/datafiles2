__author__ = 'MFlores1'

import json
import csv
import pylab
from datetime import datetime


def read_json(filename_json):
    # Load json file
    try:
        with open(filename_json, 'r') as f:
            data = json.load(f)
    except Exception as err:
        print 'Error reading file ' + str(err)

    return data


def commits_analysis(data, filename_output):
    day_dict = {0: 0, 1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0}

    # Write output to .csv file
    try:
        with open(filename_output, 'w') as to_write:
            writer = csv.writer(to_write, delimiter=',')
            for w in data:
                if 'week' in w:
                    # Convert unix timestamp to string
                    date_str = datetime.fromtimestamp(float(w['week']))
                    writer.writerow([date_str, w['total']])
    except Exception as err:
        print 'Error writing file ' + str(err)

    # Sum commits per day of week in dictionary
    for w in data:
        day_dict[0] += w['days'][0]
        day_dict[1] += w['days'][1]
        day_dict[2] += w['days'][2]
        day_dict[3] += w['days'][3]
        day_dict[4] += w['days'][4]
        day_dict[5] += w['days'][5]
        day_dict[6] += w['days'][6]

    # Create list of days
    days = list(day_dict.keys())
    # Create list of commit' totals
    commits = list(day_dict.values())

    # Graph
    pylab.plt.bar(days, commits)
    pylab.title('Commits per day of week')
    pylab.xlabel('Day of week')
    pylab.ylabel('Commits')
    pylab.show()


def releases_analysis(data):
    release_dict = {}
    # Count releases each year
    for r in data:
        release_year = r['created_at'][:4]
        release_dict.setdefault(release_year, 0)
        release_dict[release_year] += 1

    # Print releases per year
    for k in sorted(release_dict.keys()):
        print 'Year: ', k, 'Releases: ', release_dict[k]


def main():
    # Commits
    filename_commits = 'C:\Users\mflores1\datafiles2\data_science_practice\\github_commits.txt'
    filename_output = 'C:\Users\mflores1\datafiles2\data_science_practice\\github_commits_results.csv'
    commits_analysis(read_json(filename_commits), filename_output)

    # Releases
    filename_releases = 'C:\Users\mflores1\datafiles2\data_science_practice\\github_releases.txt'
    releases_analysis(read_json(filename_releases))

if __name__ == '__main__':
    main()
