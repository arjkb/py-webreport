import pprint
import os

def main():
    people = [('Alice', 27, 'New York', 'https://en.wikipedia.org/wiki/New_York'),
         ('Bob', 26, 'Paris', 'https://en.wikipedia.org/wiki/Paris'),
         ('Charlotte', 25, 'Singapore', 'https://en.wikipedia.org/wiki/Singapore'),
         ('Dylan', 24, 'Dubai', 'https://en.wikipedia.org/wiki/Dubai'),
         ('Emily', 23, 'New Delhi', 'https://en.wikipedia.org/wiki/New_Delhi'),
        ]
    pprint.pprint(people)

    with open('index.html', mode='w', encoding='utf-8') as f:
        f.write("<!DOCTYPE html>")
        f.write("<html>")
        f.write("<head>")
        f.write("<title>My Report</title>")
        f.write("</head>")
        f.write("<body>")

        f.write("<table>")
        for p in people:
            f.write("<tr>")
            f.write("<td>{0}</td> <td>{1}</td> <td><a href='{3}' target='_blank'>{2}</a></td>".format(p[0], p[1], p[2], p[3]))
            f.write("</tr>")
        f.write("</table>")

        f.write("</body>")
        f.write("</html>")

    print("Report created at {}/index.html".format(os.getcwd()))

if __name__ == '__main__':
    main()
