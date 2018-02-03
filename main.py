
def main():
    people = [('Alice', 20, 'New York'),
         ('Bob', 22, 'Philadelphia'),
         ('Charlotte', 24, 'London'),
         ('Dylan', 21, 'Los Angeles'),
         ('Emily', 23, 'Dallas'),
        ]
    print(people)

    with open('index.html', mode='w', encoding='utf-8') as f:
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

    print("Report created as index.html")

if __name__ == '__main__':
    main()
