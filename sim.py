# %% [markdown]
# # Simulating the Collector's Vault
#
# The Marvel Future Fight Collector's Vault is the subject of plenty of advice and
# warnings ( like [this one](https://www.reddit.com/r/future_fight/comments/ch8719/this_is_what_25200000_gold_gets_you_in_the/)
# and [this one](https://www.reddit.com/r/future_fight/comments/b0fwtc/collectors_vault_winnings/) ). Whether it's a reasonable way to spend gold (if you've got plenty) or just a way to waste it is up for debate. However, an event that you can play at most two times on one day every few weeks is difficult to evaluate by just discussing in the forums. The mechanisms of the event make theoretical statistical considerations fairly complicated. So, let's simulate it and see what we get.
#
# ## Vault types
#
# There have been different variations on the Collector's Vault; the current incarnation as of this writing is described at
# [the announcement for the July 2022 Collector's Vault](https://forum.netmarble.com/futurefight_en/view/76/1762161), and it's been in this format since at least January 2022. There is a "Personal Vault" where you're *almost* guaranteed to get a 4* artifact, and there are "General Vaults" where you and up to 1,500 other players each try to get a single C.T.P of Veteran or 6* artifact. This latter kind is the most like older versions of the Collector's Vault; the major changes in the latest version is a somewhat lower cost per turn, more opportunities throughout the day to choose a Vault to "open", and fewer players allowed in each Vault. It's also the first version in which Netmarble has made the mechanism and probabilities explict, allowing us to program a simulation.
#
# The General Vaults are of two types:
#
# ### General Vault - C.T.P. of Veteran
#
# | Item | Purchase Limit |Acquisition Chance |
# |------|----------------|-------------------|
# | Norn Stone of each type x15 | 110000 | 23.6280% |
# | Rank 1 Black Anti-Matter x5 | 110000 | 15.7520% |
# | Norn Stone of Chaos x5 | 110000 | 15.7520% |
# | Gear Up Kit x25 | 110000 | 11.8140% |
# | Dimension Debris x30 | 110000 | 11.8140% |
# | 3* Type Enhancement Kit x3 | 110000 | 14.6996% |
# | 3* Enchanted Uru x1 | 110000 | 6.2999% |
# | Tier-2 Mega Advancement Ticket x1 | 5 | 0.0005% |
# | Titan Component Pack x40 | No limit | 0.1248% |
# | Essence of Dimension x50 | No limit | 0.0720% |
# | Cosmic Cube Fragment x60 | No limit | 0.0360% |
# | Extreme Obelisk x1 | No limit | 0.0072% |
#
# ### General Vault - 6* Exclusive Passive Skill Artifact
# | Item | Purchase Limit |Acquisition Chance |
# |------|----------------|-------------------|
# | Gear Up Kit x20 | 110000 | 23.6280% |
# | Dimension Debris x20 | 110000 | 15.7520% |
# | Norn Stone of each type x15 | 110000 | 15.7520% |
# | Rank 1 Black Anti-Matter x5 | 110000 | 11.8140% |
# | Norn Stone of Chaos x5 | 110000 | 11.8140% |
# | 3* ISO-8 x1 | 110000 | 14.6996% |
# | Lv. 2 Artifact x1 | 110000 | 6.2999% |
# | Mega Uniform Upgrade Ticket: Mythic x1 | 5 | 0.0005% |
# | Essence of Dimension x40 | No limit | 0.1248% |
# | Cosmic Cube Fragement x50 | No limit | 0.0720% |
# | Titan Component Pack x60 | No limit | 0.0360% |
# | 6* Rank Up Ticket x1 | No limit | 0.0072% |
#
# Event though the prizes each turn are different, the stats are the same; for instance, the second entry in the list has a 15.7520% chance of being received, whether it's 5 Rank 1 Black Anti-Matter or 20 Dimension Debris. This means simulating the two can be done the same way, and the only change is the specific prizes you might get in the end. We'll come back to this.
#
# ## How the Vault (or the simulation) works
#
# Python isn't the fastest, but it's pretty easy to read and throw together without being too clever. Let's build up the simulation code while talking about the mechanism of the Vault.
#
# First, we'll note the number of users allowed in each Vault and how much gold you need for each "turn", that is, each time you want to buy an item.

# %%
users = 1500
price = 25000

# %% [markdown]
# As we noted, we can use either of the General Vaults to check the statistics and run the simulation. Since it's listed first, we'll use the CTP of Veteran one:

# %%
inf = float('inf') # this is just a shortcut for those items that have no limit

ctp_items = [
    ("Norn Stone of each type x15", 110000, 0.236280),
    ("Rank 1 Black Anti-Matter x5", 110000, 0.157520),
    ("Norn Stone of Chaos x5", 110000, .157520),
    ("Gear Up Kit x25", 110000,.118140),
    ("Dimension Debris x30", 110000, .118140),
    ("3* Type Enhancement Kit x3", 110000, .146996),
    ("3* Enchanted Uru x1", 110000, .062999),
    ("Tier-2 Mega Advancement Ticket x1", 5, 0.000005),
    ("Titan Component Pack x40", inf, 0.001248 ),
    ("Essence of Dimension x50", inf, 0.000720),
    ("Cosmic Cube Fragment x60", inf, 0.000360),
    ("Extreme Obelisk x1",inf, 0.000072)
]

# %% [markdown]
# Each time you take a "turn" by acquiring an item, one is randomly selected from the list. As the items with limited quantities run out, the probabilities of getting the other items changes a bit. For instance, take a look at this recent run, with the "Chance Info" displayed:
#
# (insert images)
#
# We'll check for the same thing each time we acquire an item:

# %%
import random

def get_item(round_items):
    roll = random.random()
    sum_p = 0.0
    for i in range(len(round_items)):
        (name,num,p) = round_items[i]
        if roll < sum_p + p:
            if num == 1:
                round_items[i] = (name,0,0)
                recalc_p(round_items,p)
            else:
                round_items[i] = (name,num-1,p)
            return i
        else:
            sum_p += p

def recalc_p(round_items,p):
    remaining_p = 1.0-p
    correction = 1 / remaining_p
    for i in range(len(round_items)):
        (name,num,p) = round_items[i]
        round_items[i] = (name,num,p*correction)


# %% [markdown]
# As soon as one of the users gets all four of the "memento" items, the Vault closes and nobody can get any more items. Not coincidentally, the "memento" items are those that don't have a limited quantity.

# %%
needed_items = []
for i in range(len(ctp_items)):
    if ctp_items[i][1] == inf:
        needed_items.append(i)

def has_needed_items( items ):
    for item in needed_items:
        if item not in items:
            return False
    return True

# %% [markdown]
# We also need to keep track of what items the different users have so that we can determine when someone has all the "memento" items (and so that we can tell what items we ended up with). We'll refer to users by number (from 0 to 1499), with "our" user as number 0. If it's our turn, we'll keep track of whatever items we have; if it's a different user's turn we'll just keep track if it's one of the memento items. When we're adding this new item to the list of acquired items, we'll take the opportunity at the same time to see if the user's gathered all the mementos.

# %%
user_nums = []
for i in range(users):
    user_nums.append(i)

def add_user_item(user, item, users_items):
    if item in needed_items or user == 0:
        users_items[user].append(item)
        if item in needed_items:
            if has_needed_items(users_items[user]):
                return True
    return False

# %% [markdown]
# Finally, we set up the simulated "round" of the Vault. We start an empty list of items acquired for each user at the beginning of every fault, and since we are editing the probabilities in the table of items we do that work on a copy. Then on every "turn", we shuffle the order in which all the users hit their buttons; we can only calculate one at a time, but we don't want to give the users first in line an advantage. Then each user gets their item and it's added to their acquired items list as above. You'll recall that also checks to see if they've won; if so, our round is over and we can save who the winner was, how many turns we took, and what items we received.

# %%
def do_round():
    winner = -1
    turns = -1
    users_items = [[] for i in range(users)]
    round_items = ctp_items.copy()
    for turn in range(3600*100):
        random.shuffle(user_nums)
        for user_num in user_nums:
            if add_user_item( user_num, get_item(round_items), users_items):
                turns = len(users_items[0])
                winner = user_num
                break
        if turns >= 0:
            break
    return (winner,turns,users_items[0])

# %% [markdown]
# This, of course, means we are making a few assumptions. First, we assume that people are all taking about the same number of turns, that is, that they aren't acquiring items more quickly or more slowly than anyone else. This isn't true even if they're using the "auto purchase" method (which, for that matter, depends on the connection to Netmarble's servers). If someone is going more slowly than you, however, they'll spend less but are necessarily also less likely to win the big prize---so you're at your worst luck when everyone is going as fast as you are. For the same reason, we're assuming everyone started right away when the Vault opened and that it maxed out the number of users. Finally we assume that at some point the Vault closes. Although it's not realistic, we allow up to 3600*100 turns, or the equivalent of 100 turns per second for the hour that the Vault is open.
#
# Next, we just have to decide how many times we'll run the simulation and what we'll do with the output. Here, we've set it to a modest 10 simulations and we just print the output, which is in the format of a comma-delimited row: the number of the winner, the number of turns our user took, and a list of the indices of all the items our user acquired.

# %%
sims = 100000

for i in range(sims):
    round = do_round()
    print( round[0],round[1],'"' + ','.join(map(str,round[2])) + '"',sep="," )

# %% [markdown]
# The simulation isn't terribly fast. Depending on the system I used, each Collector's Vault "round" took between 0.5 and 1.5 seconds to calculate. I'm sure there are optimizations that could be made, or that programming in C rather than Python would improve the speed significantly.
#