import pprint
import os

def main():
    people = [('Alice', 27, 'New York'),
         ('Bob', 26, 'Philadelphia'),
         ('Charlotte', 25, 'London'),
         ('Dylan', 24, 'Los Angeles'),
         ('Emily', 23, 'Dallas'),
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
            f.write("<td>{}</td> <td>{}</td> <td>{}</td>".format(p[0], p[1], p[2]))
            f.write("</tr>")
        f.write("</table>")

        f.write("</body>")
        f.write("</html>")

    print("Report created at {}/index.html".format(os.getcwd()))

if __name__ == '__main__':
    main()
