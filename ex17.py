import random
import math


def generer_ticket_gagnant(nb_tickets, nbMax):
    tickets = [math.trunc(random.random() * nbMax) for _ in range(nb_tickets)]
    return (tickets, random.choice(tickets))


print(generer_ticket_gagnant(10, 43))
# def generer_ticket_gagnant(nb_tickets, nbMax):
#     nombres = range(nbMax)
#     tickets = random.sample(nombres, nb_tickets)
#     return (tickets, random.choice(tickets))


# print(generer_ticket_gagnant(10, 43))
# def generer_ticket_gagnant(nb_tickets, nbMax):
#     tickets = []
#     for i in range(nb_tickets):
#         tickets.append(math.trunc(random.random() * nbMax) + 1)
#     return (tickets, random.choice(tickets))


# print(generer_ticket_gagnant(10, 43))
