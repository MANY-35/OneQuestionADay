def solution(routes):
    routes = sorted(routes, key=lambda x:x[1])
    c = 0
    while routes:
        t = []
        for route in routes:
            if route[0] > routes[0][1]:
                t.append(route)
        c += 1
        routes = t
    return c