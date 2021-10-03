############
# Printing
############


def print_intervals(intervals):
    """Print intervals more or less pretty"""

    column_name = "interval"
    margin_left = len(column_name)

    # find the maximum space needed to the left
    for i in intervals:
        margin_left = max(len(str(i)), margin_left)

    print(column_name)
    for i in intervals:
        # get the interval plus spacing until the timeline starts (1st column)
        curr_line = str(i)
        curr_line += ''.join([" "] * (margin_left - len(str(i))))

        # interval on the timline (2nd column)
        # IMPORTANT : two characters for each timestep !
        curr_line += ''.join(["  "] * i[0])              # before start
        curr_line += ''.join(["--"] * (i[1] - i[0])) + "-"  # start to end

        print(curr_line)  # removing last '-'

    # leave space for (1st column)
    max_end_time = max(intervals, key=lambda x: x[1])[1] + 1
    last_line = ''.join([" "] * margin_left)

    # x axis description (2nd column)
    last_line += ''.join([str(x) + " " for x in range(max_end_time)])
    last_line += "   time steps"

    print(last_line)


def print_graphs(vertices, edges, directed=True):
    """Pretty view for graphs"""
    import graphviz

    dot = graphviz.Digraph() if directed else graphviz.Graph()

    for n in vertices:
        dot.node(str(n))

    for e in edges:
        label = str(e[2]) if len(e) >= 3 else ""
        dot.edge(str(e[0]), str(e[1]), label=label)

    dot.render('./graph.gv', view=True)
