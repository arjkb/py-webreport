import random
def main():
    people = [('Alice', random.randint(20, 30), 'New York'),
         ('Bob', random.randint(20, 30), 'Philadelphia'),
         ('Charlotte', random.randint(20, 30), 'London'),
         ('Dylan', random.randint(20, 30), 'Los Angeles'),
         ('Emily', random.randint(20, 30), 'Dallas'),
        ]
    print(people)

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

    print("Report created as index.html")

if __name__ == '__main__':
    main()
