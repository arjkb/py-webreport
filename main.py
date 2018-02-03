
def main():
    a = [('Alice', 20, 'New York'),
         ('Bob', 22, 'Philadelphia'),
         ('Charlotte', 24, 'London'),
         ('Dylan', 21, 'Los Angeles'),
         ('Emily', 23, 'Dallas'),
        ]
    print(a)

    with open('index.html', mode='w', encoding='utf-8') as f:
        f.write("<html>")
        f.write("<head>")
        f.write("<title>My Report</title>")
        f.write("</head>")
        f.write("<body>")
        f.write("<p> This is a sample text</p>")
        f.write("</body>")

    print("Report created as index.html")

if __name__ == '__main__':
    main()
