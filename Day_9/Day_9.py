bids = {}

Shouldcontinue = True

def find_highest_bidder(bidding_dics):
    big_amount = bids[user]
    for bidder in bids:
        if big_amount < bids[bidder]:
            big_amount = bids[bidder]
            winner = bidder
    print (f"The winnder is {bidder} Your Bidding Amount is {big_amount}")


while Shouldcontinue:
    user = input("Enter your name: ")
    bid = input("Enter your bid: ")
    bids[user] = bid
    shouldContinue = input("Do you want to continue? [y/n]: ").lower()
    if shouldContinue == "n":
        Shouldcontinue = False
        find_highest_bidder(bids)


