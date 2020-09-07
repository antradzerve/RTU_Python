p0 = int(input("Enter the population of the city:  "))
perc = float(input("Enter the yearly population growth (percentage):  "))/100
delta = int(input("How many people leave or come to live in the city each year? Enter a positive or a negative number!  "))
p = int(input("Enter the population amount for which you want to check the number of years needed to reach with given input parameters:  "))

def get_city_year(a, b, c, d):
    population = a + a*b + c
    year = 1
    if population >= d:
        print(f"{year=}")
    else:
        while population <= d:
            if population <=0 or population>d:
                print(-1)
                exit(1)
            population = population + population*b + c
            year += 1
        print(f"The city will reach the population of at least {d} in {year} years")

get_city_year(p0, perc, delta, p)
