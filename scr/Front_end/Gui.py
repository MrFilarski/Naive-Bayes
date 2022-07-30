from tabulate import tabulate


def print_table(headers: [], data: []) -> str:
    return tabulate(data, headers=headers, tablefmt="fancy_grid", stralign="center")
