def generate_routes(last_move):

    routes = []
    possible_moves = ['U', 'D', 'L', 'R']
    possible_moves.remove(last_move)
    for move in possible_moves:
        routes.append([move])
    
    print(routes)
    
    while len(routes[-1]) < 3:
        for i in range(len(routes)):
            possible_moves = ['U', 'D', 'L', 'R']
            possible_moves.remove(routes[i][-1])
            for move in possible_moves:
                routes.append(routes[i].append(move))
            routes[i] = None

    while None in routes:
        routes.remove(None)
            
    return routes

print(generate_routes('R'))