#!/usr/bin/python3
<<<<<<< HEAD


def search_replace(my_list, search, replace):
    return list(map(lambda e: replace if e == search else e, my_list))
=======
def search_replace(my_list, search, replace):
    def s_r_elm(elm):
        return (elm if elm != search else replace)
    return list(map(s_r_elm, my_list))
>>>>>>> 46949fe5db0c6176bf1acc5e0d855f40e65f9c38
