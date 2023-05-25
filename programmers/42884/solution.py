
def solution(routes):
    routes = sorted(routes, key=lambda x:x[1])
    print(routes)
    
    c = 0
    while routes:
        t = []
        for route in routes:
            if route[0] > routes[0][1]:
                t.append(route)
        print(t)
        routes = t
        
    

routes = [[-20,-15], [-14,-5], [-18,-13], [-5,-3], [-18, -12]]
print(solution(routes))
