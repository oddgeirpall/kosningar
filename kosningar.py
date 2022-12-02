import argparse
import csv
import pprint


RES_DEF = {'D': 48708, 
           'B': 34510, 
           'V': 25114,
           'S': 19825, 
           'F': 17672,
           'P': 17233,
           'C': 16628,
           'M': 10879,
           'J': 8181, 
           'O': 845,
           'Y': 144,
           }

SEATS_DEF   = 63
METHOD_DEF  = "dhont"


def main(args):

    if args.file:
        with open(args.file, 'r') as f:
            reader = csv.reader(f)
            res = dict((rows[0],int(rows[1])) for rows in reader)
    else:
        res = RES_DEF

    if args.seats:
        num_seats = args.seats
    else:
        num_seats = SEATS_DEF

    if args.method:
        if args.method == "d" or args.method == "dhont":
            method = "dhont"
        else:
            method = "saintlague"
    else:
        method = METHOD_DEF

    if args.limit:
        tot_votes = sum(res.values())
        limit = tot_votes * args.limit / 100

        for key in res:
            if res[key] < limit:
                res[key] = 0

    const = res.copy()

    seats = dict((x,0) for x in res.keys())

    order = list()

    for i in range(num_seats):
        
        s = max(res, key=res.get)
        seats[s] += 1

        if method == "dhont":
            res[s] = const[s] / (seats[s]+1)
        else:
            res[s] = const[s] / (2*seats[s]+1)

        order.append("{0}. Þingmaður: {1}".format(i+1,s))


    pp = pprint.PrettyPrinter(width=1)

    print("=============================")
    print("Útistandandi atkvæði")
    pp.pprint(res)
    print("=============================")
    print("Fulltrúaskipan")
    pp.pprint(seats)
    print("=============================")
    print("Næsti maður inn færi til: {}".format(max(res, key=res.get)))

    if args.order:
        print(*order, sep="\n")



if __name__ == "__main__":

    def valid_method(method):
        if not method in ["d", "dhont", "sl", "saintlague"]:
            raise argparse.ArgumentTypeError("Method must be either dhont or saintlague")
        return method

    parser = argparse.ArgumentParser()
    parser.add_argument("-f", "--file", required=False)
    parser.add_argument("-s", "--seats", required=False, type=int)
    parser.add_argument("-l", "--limit", required=False, type=int)
    parser.add_argument("-o", "--order", required=False, action='store_true')
    parser.add_argument("-m", "--method", required=False, type=valid_method)

    args = parser.parse_args()

    main(args)
